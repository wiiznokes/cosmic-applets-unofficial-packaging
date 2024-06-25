
PACKAGE := 'cosmic-ext-applet-external-monitor-brightness'
VERSION := '0.1.0'
# can't be latest here
COMMIT := '93cfbca9f97481168ed87bf6dabcb693b014610a'
REPO := 'https://github.com/maciekk64/cosmic-ext-applet-external-monitor-brightness'


vendor:
    . ./scripts/vendor-srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} rpms/{{PACKAGE}}/{{PACKAGE}}.spec {{REPO}}

sources:
    cp {{PACKAGE}}-*.tar.xz ~/rpmbuild/SOURCES/

spec:
    . ./scripts/vendor-srpm.sh {{PACKAGE}} {{VERSION}} {{COMMIT}} rpms/{{PACKAGE}}/{{PACKAGE}}.spec {{REPO}} 1
    cp {{PACKAGE}}.spec ~/rpmbuild/SPECS/

build:
    rpmbuild -bb ~/rpmbuild/SPECS/{{PACKAGE}}.spec