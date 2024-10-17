Name:		texlive-pst-pdf
Version:	56622
Release:	2
Summary:	Make PDF versions of graphics by processing between runs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-pdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package pst-pdf simplifies the use of graphics from
PSTricks and other PostScript code in PDF documents. As in
building a bibliography with BibTEX, additional external
programmes are invoked. In this case they are used to create a
PDF file (\PDFcontainer) that will contain all the graphics
material. In the final document these contents will be inserted
instead of the original PostScript code. The package works with
pstricks and requires a recent version of the preview package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/pst-pdf
%{_texmfdistdir}/tex/latex/pst-pdf
%doc %{_texmfdistdir}/doc/latex/pst-pdf
#- source
%doc %{_texmfdistdir}/source/latex/pst-pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
