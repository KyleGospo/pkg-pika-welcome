Name:           pika-welcome
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        A Rust based GTK4 + Libadwaita App for handling initial user setup

License:        MIT
URL:            https://github.com/KyleGospo/pkg-pika-welcome

VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vte-2.91-gtk4)

%global debug_package %{nil}

%description
A Rust based GTK4 + Libadwaita App for handling initial user setup

%prep
{{{ git_dir_setup_macro }}}

%build
cargo build -r

%install
%make_install

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-autostart
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_exec_prefix}/lib/pika/*
%{_datadir}/applications/com.github.pikaos-linux.pikawelcome.desktop
%{_datadir}glib-2.0/schemas/com.github.pikaos-linux.pikawelcome.gschema.xml
%{_datadir}/icons/hicolor/64x64/apps/pika-*
%{_datadir}/icons/hicolor/scalable/apps/com.github.pikaos-linux.pikawelcome.svg
%{_datadir}/pika-welcome/config/*.json

%changelog
{{{ git_dir_changelog }}}
