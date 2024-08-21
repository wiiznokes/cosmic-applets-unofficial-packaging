ExcludeArch: %{ix86}
# Generated by rust2rpm 26
%bcond_without check


%global crate cosmic-applet-emoji-selector
%global id dev.dominiccgeh.CosmicAppletEmojiSelector

%global commit ###
%global shortcommit %{sub %{commit} 1 7}
%global commitdatestring ###
%global commitdate ###

Name:           cosmic-ext-applet-emoji-selector
Version:        %{ver}~git%{date}.%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Emoji Selector for COSMIC

SourceLicense:  MPL-2.0
License:        MPL-2.0

URL:            https://github.com/leb-kuchen/cosmic-ext-applet-emoji-selector.git
	
Source0:        https://github.com/leb-kuchen/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        vendor-%{shortcommit}.tar.gz
Source2:        vendor-config-%{shortcommit}.toml

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  just
BuildRequires:  libxkbcommon-devel
BuildRequires:  git-core

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{name}-%{commit} -p1 -a1
%cargo_prep -N
# Check if .cargo/config.toml exists
if [ -f .cargo/config.toml ]; then
  # If it exists, append the contents of %%{SOURCE2} to .cargo/config.toml
  cat %{SOURCE2} >> .cargo/config.toml
  echo "Appended %{SOURCE2} to .cargo/config.toml"
else
  # If it does not exist, append the contents of %%{SOURCE2} to .cargo/config
  cat %{SOURCE2} >> .cargo/config
  echo "Appended %{SOURCE2} to .cargo/config"
fi

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

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
%{_datadir}/applications/%{id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/dev.dominiccgeh.*.svg
# todo: 1 package for each locale. The size is 32M.
%{_datadir}/%{id}/i18n-json/*

%changelog
%autochangelog
