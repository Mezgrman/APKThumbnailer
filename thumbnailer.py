#!/usr/bin/env python
# Copyright (C) 2013 Julian Metzler
# See the LICENSE file for the full license.

import sys
import thumbnailer_classes as classes

def main():
	size = int(sys.argv[2])
	infile = sys.argv[3].replace("file://", "")
	outfile = sys.argv[4]
	nailer = classes.APKThumbnailer()
	nailer.make_thumb(infile, outfile, size)

main()
