#!/bin/bash -xe

export NAME=cosmic-ext-applet-clipboard-manager

SCRIPT=srpm.sh
RPM_REPO=https://github.com/wiiznokes/cosmic-applets-unofficial-packaging.git
RPM_REPO_NAME=cosmic-applets-unofficial-packaging

git clone $RPM_REPO
cp $RPM_REPO_NAME/rpms/$NAME/* .
cp $RPM_REPO_NAME/scripts/$SCRIPT .

./$SCRIPT
