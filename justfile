
PACKAGE := 'cosmic-ext-applet-clipboard-manager'
VERSION := '0.1.0'
# can't be latest here
COMMIT := '22c960d3acbb30a56440add20858818ca91f78ee'
REPO := 'https://github.com/wiiznokes/clipboard-manager'

all: vendor sources spec build

vendor:
    . ./scripts/vendor-srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} rpms/{{PACKAGE}}/{{PACKAGE}}.spec {{REPO}}

sources:
    cp {{PACKAGE}}-*.tar.xz ~/rpmbuild/SOURCES/

spec:
    . ./scripts/vendor-srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} rpms/{{PACKAGE}}/{{PACKAGE}}.spec {{REPO}} 1
    cp {{PACKAGE}}.spec ~/rpmbuild/SPECS/

build:
    rpmbuild -bb ~/rpmbuild/SPECS/{{PACKAGE}}.spec