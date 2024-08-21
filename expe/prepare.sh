#!/bin/bash -xe

check_variable() {
    local var_name=$1
    if [ -z "${!var_name+x}" ]; then
        echo "Error: '$var_name' is not defined."
        exit 1
    fi
}

check_variable PACKAGE

git clone --recurse-submodules https://github.com/wiiznokes/cosmic-applets-unofficial-packaging.git
cp cosmic-applets-unofficial-packaging/rpms/$PACKAGE/* .
cp scripts/srpm.sh .
