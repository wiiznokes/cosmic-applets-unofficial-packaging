# FIXME: Debug artifacts get in the way
%define debug_package %{nil}
ExcludeArch: %{ix86}
# Generated by rust2rpm 26
%bcond_without check

%global ver ###
%global commit ###
%global commitdatestring ###
%global commitdate ###

Name:           cosmic-settings
Version:        %{ver}~git%{commitdate}.%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Settings app for the COSMIC Desktop Environment

SourceLicense:  GPL-3.0 AND GPL-3.0-only
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-3-Clause
# BSL-1.0
# CC0-1.0
# CC0-1.0 OR Apache-2.0
# GPL-3.0
# GPL-3.0-only
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR CC0-1.0
# MIT OR Apache-2.0 OR NCSA
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        0BSD OR MIT OR Apache-2.0 AND Apache-2.0 AND Apache-2.0 OR MIT AND Apache-2.0 WITH LLVM-exception AND Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CC0-1.0 OR Apache-2.0 AND GPL-3.0 AND GPL-3.0-only AND ISC AND MIT AND MIT OR Apache-2.0 AND MIT OR Apache-2.0 OR CC0-1.0 AND MIT OR Apache-2.0 OR NCSA AND MIT OR Apache-2.0 OR Zlib AND MIT OR Zlib OR Apache-2.0 AND MPL-2.0 AND Unlicense OR MIT AND Zlib AND Zlib OR Apache-2.0 OR MIT
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/pop-os/cosmic-settings

Source:         https://github.com/pop-os/cosmic-settings/archive/%{commit}.tar.gz
# To create the below sources:
# * git clone https://github.com/pop-os/cosmic-settings at the specified commit
# * cargo vendor > vendor-config.toml
# * tar -pczf vendor.tar.gz vendor
Source:         vendor.tar.gz
# * mv vendor-config.toml ..
Source2:         vendor-config.toml

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  libinput-devel
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  systemd-devel
BuildRequires:  just

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n cosmic-settings-%{commit} -p1 -a1
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
just rootdir=%{buildroot} install

%if %{with check}
%check
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif

%files
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/cosmic-settings
%{_datadir}/applications/com.system76.CosmicSettings.desktop
%{_metainfodir}/com.system76.CosmicSettings.metainfo.xml
%dir %{_datadir}/cosmic/com.system76.CosmicTheme.Dark.Builder
%{_datadir}/cosmic/com.system76.CosmicTheme.Dark.Builder/v1/*
%dir %{_datadir}/cosmic/com.system76.CosmicTheme.Dark
%{_datadir}/cosmic/com.system76.CosmicTheme.Dark/v1/*
%dir %{_datadir}/cosmic/com.system76.CosmicTheme.Light.Builder
%{_datadir}/cosmic/com.system76.CosmicTheme.Light.Builder/v1/*
%dir %{_datadir}/cosmic/com.system76.CosmicTheme.Light
%{_datadir}/cosmic/com.system76.CosmicTheme.Light/v1/*
%dir %{_datadir}/cosmic/com.system76.CosmicTheme.Mode
%{_datadir}/cosmic/com.system76.CosmicTheme.Mode/v1/*
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-slightly-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-dark-style-square.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-slightly-round.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-light-style-square.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-mode-dark.svg
%{_datadir}/icons/hicolor/scalable/status/illustration-appearance-mode-light.svg
%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicSettings.svg
%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicSettings.svg
%{_datadir}/applications/com.system76.CosmicSettings.About.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Appearance.desktop
%{_datadir}/applications/com.system76.CosmicSettings.DateTime.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Desktop.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Displays.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Firmware.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Keyboard.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Mouse.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Notifications.desktop
%{_datadir}/applications/com.system76.CosmicSettings.RegionLanguage.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Sound.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Touchpad.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Users.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Wallpaper.desktop
%{_datadir}/applications/com.system76.CosmicSettings.Workspaces.desktop
%{_datadir}/polkit-1/rules.d/cosmic-settings.rules

%changelog
%autochangelog