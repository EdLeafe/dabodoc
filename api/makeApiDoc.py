#!/usr/bin/env python

# Run this script to generate the epydoc documentation.

import sys
import types
import os
import dabo
dabo.ui.loadUI("wx")
from getDaboModules import getDaboModules

_outputType = "html"
#_outputType = "pdf"

# I think "included" is the nicest format:
_inheritanceFormat = "included"   ## lists all attributes together, with text that shows where inherited from
#_inheritanceFormat = "grouped"   ## default epydoc: groups the attributes under the classes that define them
#_inheritanceFormat = "listed"    ## lists the attributes next to the class that defines them

_version = dabo.__version__.version

_name = "Dabo %s (Revision %s)" % (_version["version"], _version["revision"])
_url = "http://dabodev.com"

modules = getDaboModules()

modulestring = " ".join(modules)
os.system("""python ./epydoc_cli.py --%s --inheritance %s --url "%s" --name "%s" --no-private %s""" % (_outputType, 
		_inheritanceFormat, _url, _name, modulestring))
