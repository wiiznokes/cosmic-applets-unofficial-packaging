ExcludeArch: %{ix86}
# Generated by rust2rpm 26
%bcond_without check

%global ver ###
%global commit ###
%global commitdatestring ###
%global commitdate ###

Name:           cosmic-randr
Version:        %{ver}~git%{commitdate}.%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Display configuration command line tool

SourceLicense:  MPL-2.0
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib
License:        0BSD OR MIT OR Apache-2.0 AND Apache-2.0 AND Apache-2.0 OR MIT AND Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT AND ISC AND MIT AND MIT OR Apache-2.0 AND MIT OR Zlib OR Apache-2.0 AND MPL-2.0 AND Unlicense OR MIT AND Zlib
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/pop-os/cosmic-randr

Source:         https://github.com/pop-os/cosmic-randr/archive/%{commit}.tar.gz
# To create the below sources:
# * git clone https://github.com/pop-os/cosmic-randr at the specified commit
# * cargo vendor > vendor-config.toml
# * tar -pczf vendor.tar.gz vendor
Source:         vendor.tar.gz
# * mv vendor-config.toml ..
Source2:         vendor-config.toml

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  wayland-devel
BuildRequires:  just

%global _description %{expand:
Cosmic-randr command line interface.}

%description %{_description}

%prep
%autosetup -n cosmic-randr-%{commit} -p1 -a1
%cargo_prep -N
# Check if .cargo/config.toml exists
if [ -f .cargo/config.toml ]; then
  # If it exists, append the contents of %{SOURCE2} to .cargo/config.toml
  cat %{SOURCE2} >> .cargo/config.toml
  echo "Appended %{SOURCE2} to .cargo/config.toml"
else
  # If it does not exist, append the contents of %{SOURCE2} to .cargo/config
  cat %{SOURCE2} >> .cargo/config
  echo "Appended %{SOURCE2} to .cargo/config"
fi

%build
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt

%install
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install

%if %{with check}
%check
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/cosmic-randr

%changelog
%autochangelog
