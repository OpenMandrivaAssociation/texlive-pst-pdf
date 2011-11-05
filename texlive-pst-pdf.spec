# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pst-pdf
# catalog-date 2008-10-09 22:29:15 +0200
# catalog-license lppl
# catalog-version 1.1v
Name:		texlive-pst-pdf
Version:	1.1v
Release:	1
Summary:	Make PDF versions of graphics by processing between runs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-pdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package pst-pdf simplifies the use of graphics from
PSTricks and other PostScript code in PDF documents. As in
building a bibliography with BibTEX additional external
programmes are being invoked. In this case they are used to
create a PDF file (\PDFcontainer) that will contain all this
graphics material. In the final document this contents will be
inserted instead of the original PostScript code. The package
works with pstricks and requires a recent version of the
preview package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/pst-pdf/ps4pdf
%{_texmfdistdir}/scripts/pst-pdf/ps4pdf.bat
%{_texmfdistdir}/scripts/pst-pdf/ps4pdf.bat.noMiKTeX
%{_texmfdistdir}/scripts/pst-pdf/ps4pdf.bat.w95
%{_texmfdistdir}/tex/latex/pst-pdf/pst-pdf.sty
%doc %{_texmfdistdir}/doc/latex/pst-pdf/CHANGES
%doc %{_texmfdistdir}/doc/latex/pst-pdf/README
%doc %{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-DE.pdf
%doc %{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-example1.pdf
%doc %{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-example1.tex
%doc %{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-example2.pdf
%doc %{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf-example2.tex
%doc %{_texmfdistdir}/doc/latex/pst-pdf/pst-pdf.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pst-pdf/CHANGES.tex
%doc %{_texmfdistdir}/source/latex/pst-pdf/elephant.ps
%doc %{_texmfdistdir}/source/latex/pst-pdf/insect1.eps
%doc %{_texmfdistdir}/source/latex/pst-pdf/insect15.eps
%doc %{_texmfdistdir}/source/latex/pst-pdf/knuth.png
%doc %{_texmfdistdir}/source/latex/pst-pdf/penguin.eps
%doc %{_texmfdistdir}/source/latex/pst-pdf/psf-demo.eps
%doc %{_texmfdistdir}/source/latex/pst-pdf/pst-pdf.dtx
%doc %{_texmfdistdir}/source/latex/pst-pdf/pst-pdf.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
