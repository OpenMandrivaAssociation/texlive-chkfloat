# revision 27473
# category Package
# catalog-ctan /macros/latex/contrib/chkfloat
# catalog-date 2012-08-20 08:30:38 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-chkfloat
Version:	0.1
Release:	4
Summary:	Warn whenever a float is placed "to far away"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chkfloat
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chkfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chkfloat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package checks for floats that are placed too far from
their origin. It was motivated by a question on the question
and answer page.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chkfloat/chkfloat.sty
%doc %{_texmfdistdir}/doc/latex/chkfloat/README
%doc %{_texmfdistdir}/doc/latex/chkfloat/chkfloat.pdf
%doc %{_texmfdistdir}/doc/latex/chkfloat/chkfloat.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
