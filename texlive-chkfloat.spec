%global tl_name chkfloat
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Warn whenever a float is placed to far away
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chkfloat
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chkfloat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chkfloat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package checks for floats that are placed too far from their origin.
It was motivated by a question on the question and answer page.

