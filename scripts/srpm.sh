#!/bin/bash -xe

# clone repo, detect last commit, vendor deps, update specfile
#
#
# PACKAGE: package name
# VERSION: tag, semver
# COMMIT: latest or sha
# REPO: link
# VENDOR: 0 or 1
# KEEP_REPO: 0 or 1

check_variable() {
    local var_name=$1
    if [ -z "${!var_name+x}" ]; then
        echo "Error: '$var_name' is not defined."
        exit 1
    fi
}

check_variable PACKAGE
VERSION=${VERSION:-"0.1.0"}
COMMIT=${VERSION:-"latest"}
check_variable REPO
VENDOR=${VENDOR:-1}
KEEP_REPO=${KEEP_REPO:-0}

if [ ! -e "$PACKAGE" ]; then
    git clone --recurse-submodules $REPO $PACKAGE
fi

cd $PACKAGE

# Get latest COMMIT hash if COMMIT is set to latest
if [[ "$COMMIT" == "latest" ]]; then
    COMMIT=$(git rev-parse HEAD)
fi

SHORTCOMMIT=$(echo ${COMMIT:0:7})

git reset --hard $COMMIT

COMMITDATE=$(git log -1 --format=%cd --date=format:%Y%m%d)
COMMITDATESTRING=$(git log -1 --format=%cd --date=iso)

if [ "$VENDOR" -eq 1 ]; then
    echo "VENDOR=1"
    # Vendor dependencies and zip vendor
    cargo vendor >../vendor-config-$SHORTCOMMIT.toml
    tar -pczf ../vendor-$SHORTCOMMIT.tar.gz vendor
fi

cd ..

if [ "$KEEP_REPO" -ne 1 ]; then
    rm -rf $PACKAGE
else
    echo "KEEP_REPO=1"
fi

# Make replacements to specfile
sed -i "/^Version: / s/.*/Version:           $VERSION~^%{commitdate}git%{shortcommit}/" $PACKAGE.spec
sed -i "/^%global commit / s/.*/%global commit $COMMIT/" $PACKAGE.spec

sed -i "/^%global commitdate / s/.*/%global commitdate $COMMITDATE/" $PACKAGE.spec
sed -i "/^%global commitdatestring / s/.*/%global commitdatestring $COMMITDATESTRING/" $PACKAGE.spec
