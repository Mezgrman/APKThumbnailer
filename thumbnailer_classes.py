# Copyright (C) 2013 Julian Metzler
# See the LICENSE file for the full license.

import zipfile
from subprocess import check_output as shell

class APKThumbnailer:
	def __init__(self):
		pass
	
	def make_thumb(self, infile, outfile, size):
		command = "aapt d --values badging %s" % infile
		data = [line.replace("'", "").split(":") for line in shell(command.split()).splitlines()]
		icons = [item for item in data if item[0].startswith("application-icon")]
		if len(icons) == 0:
			return False
		icons = sorted(icons, key = lambda item: int(item[0].split("-")[-1]), reverse = True)
		icon = icons[0][1]
		apkfile = zipfile.ZipFile(infile, mode = 'r')
		icondata = apkfile.read(icon)
		with open(outfile, 'wb') as of:
			of.write(icondata)
