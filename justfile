set working-directory := 'dev'
set export

NAME := 'cosmic-ext-applet-clipboard-manager'
REPO := 'https://github.com/wiiznokes/clipboard-manager.git'
VERSION := '0.1.0'
COMMIT := 'latest'

all: init sources spec build

init:
    cp ../rpms/{{NAME}}/* .
    ../scripts/srpm.sh

sources:
    cp vendor-* ~/rpmbuild/SOURCES/
    cp *.patch ~/rpmbuild/SOURCES/ || true

spec:
    cp ../rpms/{{NAME}}/{{NAME}}.spec .
    VENDOR=0 ../scripts/srpm.sh
    cp {{NAME}}.spec ~/rpmbuild/SPECS/

build:
    rpmbuild --undefine=_disable_source_fetch -bb ~/rpmbuild/SPECS/{{NAME}}.spec

fast-build:
    rpmbuild -bb --short-circuit ~/rpmbuild/SPECS/{{NAME}}.spec
