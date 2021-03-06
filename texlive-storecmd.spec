# revision 24431
# category Package
# catalog-ctan /macros/latex/contrib/storecmd
# catalog-date 2011-10-27 10:28:55 +0200
# catalog-license lppl1.3
# catalog-version 0.0.2
Name:		texlive-storecmd
Version:	0.0.2
Release:	11
Summary:	Store the name of a defined command in a container
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/storecmd
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storecmd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/storecmd.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-2
+ Revision: 756252
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.0.2-1
+ Revision: 719593
- texlive-storecmd
- texlive-storecmd
- texlive-storecmd
- texlive-storecmd

