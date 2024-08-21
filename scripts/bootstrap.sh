#!/bin/bash -xe

PACKAGE=cosmic-ext-applet-clipboard-manager
REPO=https://github.com/wiiznokes/clipboard-manager

git clone --recurse-submodules https://github.com/wiiznokes/cosmic-applets-unofficial-packaging.git
cp cosmic-applets-unofficial-packaging/rpms/$PACKAGE/* .
cp cosmic-applets-unofficial-packaging/scripts/srpm.sh .

./srpm.sh
