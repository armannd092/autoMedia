#!/bin/sh
(cd export && 
	for file in *.svg; 
	do 
		echo $file;
		inkscape $file --export-area-drawing --export-type png --export-width 999
	done)
