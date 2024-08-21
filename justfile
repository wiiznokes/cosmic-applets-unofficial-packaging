
PACKAGE := 'cosmic-ext-applet-clipboard-manager'
VERSION := '0.1.0'
COMMIT := 'latest'
REPO := 'https://github.com/wiiznokes/clipboard-manager.git'

all: init sources spec build

init:
    cp rpms/{{PACKAGE}}/* .
    ./scripts/srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} {{REPO}} 1 1

sources:
    cp vendor-* ~/rpmbuild/SOURCES/
    cp *.patch ~/rpmbuild/SOURCES/ || true

spec:
    cp rpms/{{PACKAGE}}/{{PACKAGE}}.spec .
    . ./scripts/srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} {{REPO}} 0 1
    cp {{PACKAGE}}.spec ~/rpmbuild/SPECS/

build:
    rpmbuild --undefine=_disable_source_fetch -bb ~/rpmbuild/SPECS/{{PACKAGE}}.spec

fast-build:
    rpmbuild -bb --short-circuit ~/rpmbuild/SPECS/{{PACKAGE}}.spec
