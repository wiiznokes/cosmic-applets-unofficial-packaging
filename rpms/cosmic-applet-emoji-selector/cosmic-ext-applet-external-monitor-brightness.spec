ExcludeArch: %{ix86}
# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

%global crate cosmic-applet-emoji-selector

%global ver ###
%global commit ###
%global date ###

Name:           cosmic-applet-emoji-selector
Version:        %{ver}~git%{date}.%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Emoji Selector for COSMIC

SourceLicense:  MPL-2.0
License:        MPL-2.0

URL:            https://github.com/leb-kuchen/emoji-selector-applet-for-cosmic.git
	
Source:         %{name}-%{commit}.tar.xz
Source:         %{name}-%{commit}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  just
BuildRequires:  libxkbcommon-devel
BuildRequires:  git-core
BuildRequires:  systemd-devel

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{crate}-%{commit} -p1 -a1
%cargo_prep -N
# Check if .cargo/config.toml exists
if [ -f .cargo/config.toml ]; then
  # If it exists, append the contents of .vendor/config.toml to .cargo/config.toml
  cat .vendor/config.toml >> .cargo/config.toml
  echo "Appended .vendor/config.toml to .cargo/config.toml"
else
  # If it does not exist, append the contents of .vendor/config.toml to .cargo/config
  cat .vendor/config.toml >> .cargo/config
  echo "Appended .vendor/config.toml to .cargo/config"
fi

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt

%install
mkdir -p %{buildroot}/%{_bindir}
install -Dm0755 target/release/%{name} %{buildroot}/%{_bindir}/%{name}


%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.maciekk64.CosmicExtAppletExternalMonitorBrightness.desktop

%changelog
%autochangelog
