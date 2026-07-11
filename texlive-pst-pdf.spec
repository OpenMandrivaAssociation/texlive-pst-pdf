%global tl_name pst-pdf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2f
Release:	%{tl_revision}.1
Summary:	Make PDF versions of graphics by processing between runs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-pdf
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pst-pdf.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package pst-pdf simplifies the use of graphics from PSTricks and
other PostScript code in PDF documents. As in building a bibliography
with BibTeX, additional external programmes are invoked. In this case
they are used to create a PDF file (\PDFcontainer) that will contain all
the graphics material. In the final document these contents will be
inserted instead of the original PostScript code. The package works with
pstricks and requires a recent version of the preview package.

