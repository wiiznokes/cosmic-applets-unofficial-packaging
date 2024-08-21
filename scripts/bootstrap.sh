#!/bin/bash -xe

export PACKAGE=cosmic-ext-applet-clipboard-manager
export REPO=https://github.com/wiiznokes/clipboard-manager

git clone https://github.com/wiiznokes/cosmic-applets-unofficial-packaging.git
cp cosmic-applets-unofficial-packaging/rpms/$PACKAGE/* .
cp cosmic-applets-unofficial-packaging/scripts/srpm.sh .

./srpm.sh
