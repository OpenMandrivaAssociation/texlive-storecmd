Name:		texlive-storecmd
Version:	24431
Release:	2
Summary:	Store the name of a defined command in a container
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/storecmd
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storecmd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storecmd.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for command definition that save
the name of the command being defined in a file or a macro
container. The list could be useful for spelling exceptions in
text editors that do not support TeX syntax.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/storecmd/storecmd.sty
%doc %{_texmfdistdir}/doc/latex/storecmd/README
%doc %{_texmfdistdir}/doc/latex/storecmd/storecmd-example.tex
%doc %{_texmfdistdir}/doc/latex/storecmd/storecmd-guide.pdf
%doc %{_texmfdistdir}/doc/latex/storecmd/storecmd-guide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
