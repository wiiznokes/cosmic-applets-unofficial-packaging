set working-directory := 'dev'
set export

NAME := 'cosmic-ext-applet-external-monitor-brightness'
REPO := 'https://github.com/cosmic-utils/cosmic-ext-applet-external-monitor-brightness.git'
VERSION := '0.1.0'
COMMIT := 'f60e982441fd7b7f11523f8e7eeab168dce17b40'

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

clean:
    rm -rf ./*
    touch .keep