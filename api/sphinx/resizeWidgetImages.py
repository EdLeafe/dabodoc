# -*- coding: utf-8 -*-#

"""
take a list of images and size them to 400 x nnn and create a _thumb of 200 x nnn
"""

import PIL
from PIL import Image
import os
import glob

import config

def resizeWidgets(widgets):
    for img in images:
        if not "_thumb" in img:
            file, ext = os.path.splitext(img)
            im = Image.open(img)
            orgSize = im.size
            orgFormat = im.format
            # resize the big one
            im.thumbnail((400, 400), Image.ANTIALIAS)
            im.save(img, orgFormat)
            print "resized image: %s\n" % img
            im.thumbnail((128, 128), Image.ANTIALIAS)
            tName = file + "_thumb" + ext
            im.save(tName)
            print "resized image: %s\n" % tName
        

print "resizing window images"
images = glob.glob(os.path.join(config.docFolder, "_static/winWidgets/*.png"))
resizeWidgets(images)

print "resizing mac images"
images = glob.glob(os.path.join(config.docFolder, "_static/macWidgets/*.png"))
resizeWidgets(images)

print "resizing linux images"
images = glob.glob(os.path.join(config.docFolder, "_static/nixWidgets/*.png"))
resizeWidgets(images)

