# -*- coding: utf-8 -*-#

import os
import pydoc
import glob, re, sys, warnings

import galleryToClassIndex

# generate a thumbnail gallery of examples
template = """\
{%% extends "layout.html" %%}
{%% set title = "Thumbnail gallery" %%}


{%% block body %%}

<h3>Click on any image to see full size image, or click on the caption to go to the relevant documentation</h3>
<br/>

%s

{%% endblock %%}
"""


def gen_page(app, sdir, pname):
	"""
	Generate a html page with the thumb images for widgets
	"""
	link = '<div class="gallery_class">'

	link_template = """\
	<table><caption align="bottom"><a href="%s"<b>%s</b></a</caption>
	<tr>
	<td><a href="%s"><img src="%s" border="5" alt="%s"/></a>
	</td>
	</tr>
	</table>
	"""
	
	data = []
	thumbnails = {}
	rows = ["<br/>", link]

	# need to join srcdir
	for item in sorted(glob.glob(os.path.join(app.builder.srcdir, sdir + "\\*_thumb.png"))):
		path, filename = os.path.split(item)
		basename, ext = os.path.splitext(item)
		
		# get rid of _thumb and path
		widgetName = basename.replace("_thumb", "")
		toRemove = app.builder.srcdir + "\\" + sdir + "\\"
		widgetName = widgetName.replace(toRemove, "")
		
		# get rid of srcdir
		thumbFile = item.replace(app.builder.srcdir + "\\", "")
		# get rid of _thumb
		largeFile = thumbFile.replace("_thumb", "")
		# fix up path sep for html
		thumbFile = thumbFile.replace("\\", "/")
		largeFile = largeFile.replace("\\", "/")

		linkName = ""
		linkKey = widgetName
		linkKeyL = len(linkKey)
		if linkKey[linkKeyL-1:linkKeyL].isdigit():
			linkKey = linkKey[:linkKeyL-1]
		if galleryToClassIndex.pictureIndex.has_key(linkKey):
			# lets find the documentation link for this image
			linkName = galleryToClassIndex.pictureIndex[linkKey]
		else:
			linkName = pname
##		print "base: %s" % basename
##		print "toRemove: %s" % toRemove
##		print "widget: %s" % widgetName
##		print "linkKey: %s" % linkKey
##		print "thumb: %s" % thumbFile
##		print "large: %s" % largeFile
##		print "link: %s" % linkName
##		print link_template

		rows.append(link_template % (linkName, widgetName, largeFile, thumbFile, widgetName))

	rows.append("</div>")
	rows.append('<br clear="all"> ')
	
	content = template % '\n'.join(rows)
	gallery_path = os.path.join(app.builder.srcdir, '_templates', pname)


	# check if file has already up to date content
	fhCheck = file(gallery_path, 'r')
	oldContent = fhCheck.read()
	if oldContent.strip() == content.strip():
		print "gallery file is already up to date"
	else:
		fh = file(gallery_path, 'w')
		fh.write(content)
		fh.flush()
		fh.close()
		print "gallery file updated"

	fh = file(gallery_path, 'w')
	fh.write(content)
	fh.flush()
	fh.close()
	
def gen_gallery(app, doctree):
	
	if app.builder.name not in ["html", "singlehtml"]:
		return

	print "gen_gallery: %s, %s" % (app, app.builder.name)

##	outdir = app.builder.outdir
	print "gen_gallery for Mac"
	gen_page(app, "_static\\macWidgets", "gallery_mac.html")
	print "gen_gallery for Win"
	gen_page(app, "_static\\winWidgets", "gallery_win.html")
	print "gen_gallery for Linux"
	gen_page(app, "_static\\nixWidgets", "gallery_nix.html")


def setup(app):

	app.connect('env-updated', gen_gallery)


