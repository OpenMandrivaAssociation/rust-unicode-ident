# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate unicode-ident

Name:           rust-unicode-ident
Version:        1.0.12
Release:        2
Summary:        Determine whether characters have the XID_Start or XID_Continue properties according to Unicode Standard Annex #31
Group:          Development/Rust

License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://crates.io/crates/unicode-ident
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.31
%if %{with check}
BuildRequires:  (crate(criterion) >= 0.5.0 with crate(criterion) < 0.6.0~)
BuildRequires:  (crate(fst/default) >= 0.4.0 with crate(fst/default) < 0.5.0~)
BuildRequires:  (crate(rand/default) >= 0.8.0 with crate(rand/default) < 0.9.0~)
BuildRequires:  (crate(rand/small_rng) >= 0.8.0 with crate(rand/small_rng) < 0.9.0~)
BuildRequires:  (crate(roaring/default) >= 0.10.0 with crate(roaring/default) < 0.11.0~)
BuildRequires:  (crate(ucd-trie) >= 0.1.0 with crate(ucd-trie) < 0.2.0~)
BuildRequires:  (crate(unicode-xid/default) >= 0.2.4 with crate(unicode-xid/default) < 0.3.0~)
%endif

%global _description %{expand:
Determine whether characters have the XID_Start or XID_Continue
properties according to Unicode Standard Annex #31.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(unicode-ident) = 1.0.12
Requires:       cargo
Requires:       rust >= 1.31

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%license %{crate_instdir}/LICENSE-UNICODE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(unicode-ident/default) = 1.0.12
Requires:       cargo
Requires:       crate(unicode-ident) = 1.0.12

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
