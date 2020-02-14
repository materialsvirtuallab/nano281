#!/bin/bash

cd lectures/slides_tex
for filename in *.tex
do
	filename="${filename%.*}"
	pdflatex -shell-escape "$filename"
	bibtex "$filename"
	pdflatex -shell-escape "$filename"
	pdflatex -shell-escape "$filename"
done
mv *.pdf ../slides
rm *.toc *.snm *.aux *.vrb *.log *.nav *.out *.bbl *.blg
rm -r _minted*