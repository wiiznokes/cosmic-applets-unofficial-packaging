
PACKAGE := 'cosmic-ext-applet-minimon'
VERSION := '0.1.0'
# can't be latest here
COMMIT := 'latest'
REPO := 'https://github.com/Hyperchaotic/minimon-applet.git'

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
    rpmbuild -bb ~/rpmbuild/SPECS/{{PACKAGE}}.spec

fast-build:
    rpmbuild -bb --short-circuit ~/rpmbuild/SPECS/{{PACKAGE}}.spec
