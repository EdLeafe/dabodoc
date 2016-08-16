# -*- coding: utf-8 -*-#

"""
check that mac and nic folder has all images
"""

import os
import glob

import config

imagesWin = glob.glob(os.path.join(config.docFolder, "_static/winWidgets/*.png"))
imagesMac = glob.glob(os.path.join(config.docFolder, "_static/macWidgets/*.png"))
imagesNix = glob.glob(os.path.join(config.docFolder, "_static/nixWidgets/*.png"))

print "images missing for MAC"
print "======================"
imagesMacF = []
for img in imagesMac:
    tPath, tFile = os.path.split(img)
    imagesMacF.append(tFile)

for img in imagesWin:
    tPath, tFile = os.path.split(img)
    if not tFile in imagesMacF:
        if not "_thumb" in tFile:
            print tFile

print "======================"
print "images missing for Nix"
print "======================"

imagesNixF = []
for img in imagesNix:
    tPath, tFile = os.path.split(img)
    imagesNixF.append(tFile)

for img in imagesWin:
    tPath, tFile = os.path.split(img)
    if not tFile in imagesNixF:
        if not "_thumb" in tFile:
            print tFile
