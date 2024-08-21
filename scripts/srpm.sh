#!/bin/bash -xe

# clone repo, detect last commit, vendor deps, update specfile

if [ "$#" -lt 6 ]; then
    echo "Error: Less than six arguments provided."
    exit 1
fi

# NAME of the crate/package
NAME=$1
# VERSION of the crate/package
VERSION=$2
# COMMIT to target (latest == master)
COMMIT=$3
# REPO link
REPO=$4
# VENDOR?
VENDOR=$5
KEEP_REPO=$6

if [ ! -e "$NAME-$COMMIT" ]; then
    git clone --recurse-submodules $REPO $NAME-$COMMIT
fi

cd $NAME-$COMMIT

# Get latest COMMIT hash if COMMIT is set to latest
if [[ "$COMMIT" == "latest" ]]; then
    COMMIT=$(git rev-parse HEAD)
    cd .. && mv $NAME-LATEST $NAME-$COMMIT && cd $NAME-$COMMIT
fi

# Set short commit
SHORTCOMMIT=$(echo ${COMMIT:0:7})

# Reset to specified COMMIT
git reset --hard $COMMIT

COMMITDATE=$(git log -1 --format=%cd --date=format:%Y%m%d)
COMMITDATESTRING=$(git log -1 --format=%cd --date=iso)

if [ "$VENDOR" -eq 1 ]; then
    echo "VENDOR=1"
    # Vendor dependencies and zip vendor
    cargo vendor >../vendor-config-$SHORTCOMMIT.toml
    tar -pczf vendor-$SHORTCOMMIT.tar.gz vendor && mv vendor-$SHORTCOMMIT.tar.gz ../vendor-$SHORTCOMMIT.tar.gz
    # Back into parent directory
    rm -rf vendor
fi

cd ..


if [ "$KEEP_REPO" -ne 1 ]; then
    rm -rf $NAME-$COMMIT
fi

# Make replacements to specfile
sed -i "/^Version: / s/.*/Version:           $VERSION~^%{commitdate}git%{shortcommit}/" $NAME.spec
sed -i "/^%global commit / s/.*/%global commit $COMMIT/" $NAME.spec

sed -i "/^%global commitdate / s/.*/%global commitdate $COMMITDATE/" $NAME.spec
sed -i "/^%global commitdatestring / s/.*/%global commitdatestring $COMMITDATESTRING/" $NAME.spec

# Should have these sources
# NAME-SHORTCOMMIT.tar.gz
# vendor-%{shortcommit}.tar.gz
# vendor-config-%{shortcommit}.toml
