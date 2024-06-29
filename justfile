
PACKAGE := 'cosmic-ext-applet-clipboard-manager'
VERSION := '0.1.0'
# can't be latest here
COMMIT := '0d806ecb2b715f93bfc77eab92dd9e79a2361b1e'
REPO := 'https://github.com/wiiznokes/clipboard-manager'


vendor:
    . ./scripts/vendor-srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} rpms/{{PACKAGE}}/{{PACKAGE}}.spec {{REPO}}

sources:
    cp {{PACKAGE}}-*.tar.xz ~/rpmbuild/SOURCES/

spec:
    . ./scripts/vendor-srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} rpms/{{PACKAGE}}/{{PACKAGE}}.spec {{REPO}} 1
    cp {{PACKAGE}}.spec ~/rpmbuild/SPECS/

build:
    rpmbuild -bb ~/rpmbuild/SPECS/{{PACKAGE}}.spec