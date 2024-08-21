#!/bin/bash -x

PACKAGE=cosmic-ext-applet-clipboard-manager
VERSION=0.1.0
COMMIT=latest
REPO=https://github.com/wiiznokes/clipboard-manager

git clone --recurse-submodules https://github.com/wiiznokes/cosmic-applets-unofficial-packaging.git
cp cosmic-applets-unofficial-packaging/rpms/$PACKAGE/* .
cp cosmic-applets-unofficial-packaging/scripts/vendor-srpm.sh .
. vendor-srpm.sh $PACKAGE $VERSION $COMMIT $PACKAGE.spec $REPO







#!/bin/bash -x

VENDOR=1
# Names (Source name can sometimes be the same as name)
NAME=cosmic-comp
SOURCE_NAME=cosmic-comp
# Version and commit (latest if using master)
VERSION=0.1.0
COMMIT=LATEST
# Repos
REPO=https://github.com/pop-os/$SOURCE_NAME
RPM_REPO=https://pagure.io/fedora-cosmic/cosmic-packaging.git
# Paths to files
RPM_FILES=cosmic-packaging/rpms/$NAME/*
SCRIPT_FILE=srpm.sh
SCRIPT_DIR=cosmic-packaging/scripts/$SCRIPT_FILE

# Clone the RPM repo
git clone --recurse-submodules $RPM_REPO
# Get extra RPM files
cp $RPM_FILES .
# Get script file
cp $SCRIPT_DIR .
# Run script file
. $SCRIPT_FILE $NAME $SOURCE_NAME $VERSION $COMMIT $REPO $VENDOR
