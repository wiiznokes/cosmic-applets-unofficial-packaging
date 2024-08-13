
PACKAGE := 'cosmic-ext-applet-emoji-selector'
VERSION := '0.1.4'
# can't be latest here
COMMIT := 'a5d94f611acfafca6f203d05b07770f26fb8d69d'
REPO := 'https://github.com/leb-kuchen/cosmic-ext-applet-emoji-selector.git'

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