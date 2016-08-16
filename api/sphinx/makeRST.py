# -*- coding: utf-8 -*-#

import os
import sys

# force it
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding

import glob
import inspect
import operator

import datetime
import shutil
import re
import time
import filecmp

CROSS                   = 'Cross'
ROUNDED                 = 'Rounded'
SQUARE                  = 'Square'

CORNERS                 = [ROUNDED, SQUARE, CROSS]
CORNER_ID               = 'rounded_corner_r%d_f%d'
CROSS_POS               = (CROSS, CROSS, CROSS, CROSS)
ROUNDED_POS             = (ROUNDED, ROUNDED, ROUNDED, ROUNDED)
ROUNDED_RECTANGLE_ID    = 'rounded_rectangle_r%d_f%d_s%s_p%s'

MAXWIDTH = 120
BACKCOLOUR = (255, 255, 255, 255)

# get config stuff
import conf as sphinx_config

# needed for issubclass check
import dabo
dabo.ui.loadUI("wx")
# needed for describeDaboEvents
from dabo import dEvents

# use "en" for doc
dabo.dLocalize.setLanguage("en")

# need a counter to generate unique links for the property, method and event summaries
uniqueLinkCounter = 0

# used by genGallery
pictureIndex = {}

topLayer = "dabo"

subPackages = ["biz", "db", "lib", "ui"]
### use following for quick(er) Sphinx tests only
##subPackages = ["lib"]


subSubPackages = {'lib': ["autosuper", "datanav"],
				  'ui': ["dialogs", "uiwx"]
				 }

# no links for "inherited from" for the following, also this should be handled by getPropertyList
# also used for methods, checks for the module name only
noInheritLink = ["wx._core", "wx._windows", "wx._controls",
				 "wx.richtext", "wx.lib.pdfwin",
				 "wx.grid",
				 "wx.html", "wx.lib.plot",
				 "simplejson.decoder", "wx.glcanvas",
				 "wx.gizmos", "wx._core",
				 "wx.lib.mixins.listctrl",
				 "wx.lib.masked.textctrl",
				 "wx.lib.pdfwin","wx._misc",
				 "wx.lib.buttons",
				 "wx.calendar", "wx.stc",
				 "wx.aui", "wx.media",
				 "wx.lib.platebtn",
				 ]

noInheritLinkDabo = ["dabo.ui.uiwx.dPanel._BasePanelMixin",
					 "dabo.ui.uiwx.dMenuItem._AbstractExtendedMenuItem",]

# used to generate Index
subPackagesMods = ["dabo_module", "biz_module", "db_module", "lib_module"]

# don't create any TOC with glob for these
noTOCforMods = ["dabo.dConstants", "dabo.settings", "dabo.ui.uiwx.concordance",
				"dabo.ui.uicurses", "dabo.biz.__init__", "dabo.lib.autosuper.__init__",
				"dabo.lib.datanav.__init__", "dabo.ui.dialogs.__init__",
				"dabo.ui.dDockPanel"]

# deprecated, so don't include in TOC
deprecatedClasses = ["dabo.ui.uiwx.dCheckListBox", "dabo.ui.uiwx.dFoldPanel",
                     "dabo.ui.uiwx.dFoldPanelBar"]

# define classes which should use autoclass + members
# otherwise we use getPropertyList, getMethodList and getEventList
docMembers = ["EventMixin", "EasyDialogBuilder", "autosuper", "SplashScreen"]

# classes which cause duplicate index entries
dupNoindex = ["Rect", "Rectangle", "autosuper", "lbl", "txt"]

# following can't be linked at the moment
noSuClassLink = ["dabo.db.dConnection.DaboCursor", "dabo.lib.autosuper.autosuper.autosuper",
				 "wx._controls.StaticBitmap", "wx._controls.BitmapButton",
				 "wx._controls.StaticBox", "wx._controls.Button",
				 "wx._controls.CheckBox", "wx._controls.CheckListBox",
				 "wx._controls.ComboBox", "wx._controls.Choice",
				 "wx._controls.TextCtrl", "wx._controls.Gauge",
				 "wx._controls.StaticBitmap", "wx._controls.StaticText",
				 "wx._controls.StaticLine", "wx._controls.ListBox",
				 "wx._controls.ListCtrl", "wx._controls.SearchCtrl",
				 "wx._controls.Slider", "wx._controls.TextCtrl",
				 "wx._controls.ToolBar", "wx._controls.Notebook",
				 "wx._controls.Listbook", "wx._controls.Choicebook",
				 "wx._controls.Toolbook", "wx._controls.TreeCtrl",
				 "wx._windows.ColourDialog", "wx._windows.Dialog",
				 "wx._windows.FontDialog", "wx._windows.Panel",
				 "wx._windows.ScrolledWindow", "wx._windows.StatusBar",
				 "wx._windows.Printout", "wx._windows.FileDialog",
				 "wx._windows.DirDialog", "wx._windows.Frame",
				 "wx._windows.MiniFrame", "wx._windows.MessageDialog",
				 "wx._windows.SplitterWindow", "wx.richtext.RichTextCtrl",
				 "wx.grid.PyGridCellRenderer", "wx.grid.GridCellChoiceEditor",
				 "wx.grid.Grid", "wx.grid.PyGridTableBase",
				 "wx.html.HtmlWindow", "wx.lib.plot.PlotCanvas",
				 "simplejson.decoder.JSONDecoder", "simplejson.encoder.JSONEncoder",
				 "wx.glcanvas.GLCanvas",
				 "wx.gizmos.EditableListBox", "wx._core.GridBagSizer",
				 "wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin",
				 "wx.lib.masked.textctrl.TextCtrl", "wx.lib.plot.PlotCanvas",
				 "wx._core.app", "wx._core.Menu",
				 "wx._core.MenuBar", "wx._core.MenuItem",
				 "wx.lib.pdfwin.PDFWindow", "wx._core.BoxSizer",
				 "wx._core.Control", "wx._misc.Timer",
				 "wx.lib.buttons.GenBitmapTextToggleButton",
				 "wx.calendar.CalendarCtrl", "wx.stc.StyledTextCtrl",
				 "wx.aui.AuiNotebook", "wx._core.PyEvent",
				 "wx.tools.Editra.src.extern.flatnotebook.FlatNotebook",
				 "threading.Thread", "wx.media.MediaCtrl",
				 "dabo.ui.uiwx.dPanel._BasePanelMixin",
				 "dabo.ui.uiwx.dMenuItem._AbstractExtendedMenuItem",
				 "wx.lib.platebtn.PlateButton",
				 "dabo.ui.uiwx.dBorderSizer.TestForm",
				 "dabo.ui.uiwx.dPageFrameNoTabs.TestForm",

				 "wx.lib.agw.aui",
				 "wx.lib.agw.aui.auibook.AuiNotebook",
				 "wx.lib.agw.FlatNotebook",
				 "wx.lib.agw.hyperlink.HyperLinkCtrl",
				 "wx.lib.agw.foldpanelbar.FoldPanelItem",
				 "wx.lib.agw.foldpanelbar.FoldPanelBar",

				 ]


toRemove = ["__version__.py", "setup.py", "test.py"]

for pkg in subPackages:
	toRemove.append(pkg + "\\__init__.py")

for pkg in subSubPackages:
	for sub in subSubPackages[pkg]:
		toRemove.append(pkg + "\\" + sub + "\\__init__.py")

allPackages = []
allPackages.append("dabo.dabo")
for pkg in subPackages:
	allPackages.append("dabo." + pkg)
for pkg in subSubPackages:
	for sub in subSubPackages[pkg]:
		allPackages.append("dabo." + pkg + "." + sub)

# they cause getattr and similar error in Sphinx
excludedClasses = ["modglob", "connHandler", "FuncProfile", "FuncSource", "HotShotFuncCoverage",
				   "HotShotFuncProfile", "TraceFuncCoverage", "PageCountCanvas",
				   "specHandler", "Event", "TestForm", "Rect",

				   "__builtin__",
					]

# Dabo ones cause import errors, i.e. probably something to do with namespace, just exclude them for now
# TODO: should this be full names, e.g. dabo.ui.uiwx.dPageFrame.onPageChanged to be make sure to exclude the right thing?
excludedFunctions = ["PageFrame", "onPageChanged", "readonly", "main",
					 "autoCreateTables", "setupAutoBiz", "resetHTML",
					 "textChangeHandler",

					 "GetTranslation", "_gdi"]

excludedIcons = ["info.png", "note.png", "seealso.png", "todo.png", "warning.png", "navigation.png"]

# used in postProcess, not sure that we still have a use for it
replaces = {}

eventSummary = """
|method_summary| Events Summary
===============================

"""

propertySummary = """
|method_summary| Properties Summary
===================================

"""

methodSummary = """
|method_summary| Methods Summary
================================

"""

functionSummary = """
|method_summary| Function Summary
=================================

"""

classSummary = """
|class_summary| Class Summary
=============================

"""

DABO_modules = """
Module Summary
==============

.. toctree::
   :maxdepth: 1

   dabo.dApp_module
   dabo.dBug_module
   dabo.dColors_module
   dabo.dConstants_module
   dabo.dEvents_module
   dabo.dException_module
   dabo.dLocalize_module
   dabo.dObject_module
   dabo.dPref_module
   dabo.dReportWriter_module
   dabo.dSecurityManager_module
   dabo.dUserSettingProvider_module
   dabo.settings_module
   dabo.__init___module

"""

MAIN_modules = """
Module Summary
==============

.. toctree::
   :glob:
   :maxdepth: 1

"""

OTHER_TocTree = """
Module Summary
==============

.. toctree::
   :glob:
   :maxdepth: 1

%s

"""

classImage = """
|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**

"""

classImageMac = """

   * - .. image:: _static/macWidgets/%s
          :scale: %s
          :target: _static/macWidgets/%s
          :alt: %s

"""

classImageMacNO = """

   * - no image available

"""

classImageWin = """

     - .. image:: _static/winWidgets/%s
          :scale: %s
          :target: _static/winWidgets/%s
          :alt: %s

"""

classImageNix = """

     - .. image:: _static/nixWidgets/%s
          :scale: %s
          :target: _static/nixWidgets/%s
          :alt: %s

"""

classImageOthNO = """

     - no image available

"""


autosummary = """
.. autosummary::
   :nosignatures:

%s

"""

imagesLinks = """
.. include:: _static/headings.txt

"""

genindex = """
This is the master index for **Dabo - the desktop framework** (**Dabo**).

"""

knownSubs = """
|subclasses| Known Subclasses
=============================

%s

"""

knownSups = """
|supclasses| Known Superclasses
===============================

%s

"""

inheritance = """
|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **%s**

.. inheritance-diagram:: %s
   :parts: 1

%s

%s

%s

%s

%s

|API| Class API
===============

"""

inheritanceDabo = """
|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **%s**

.. inheritance-diagram:: %s

"""

noInheritance = """

%s

%s

%s

%s

%s

|API| Class API
===============

"""

rawhtmlfull = """

.. raw:: html

		<div class="panel">
				<p><img src="_static/dabo_small.png" alt="" style="vertical-align: middle; margin-right: 10px"/>
				<a style="color: rgb(255, 255, 255); font-size: x-large;"><b>Dabo</b></p>

				<ul class="simple" style="margin-left: 0; padding-left: 0;">
%s
				</ul>
		</div>

		<a class="trigger" href="#">Tree</a>

		<script type="text/javascript">
		$(document).ready(function(){
				$(".trigger").click(function(){
						$(".panel").toggle("fast");
						$(this).toggleClass("active");
						return false;
				});
		});
		</script>

"""

rawhtmlsingle = """            <li><a class="reference internal" href="%s"><em><b>%s</b></em></a></li>"""

svnrevisions = """
|svn_main| SVN Revisions
========================

A graphical representation of the SVN commits in the last year.

Click on any date in the picture to
jump to that particular revision page, containing information about committers, log
messages and SVN diffs.


%s


"""

# windows
os.chdir(os.path.join(sphinx_config.docFolder, "_static/winWidgets"))
fullImagesWin = glob.glob("*.png")
kImagesWin = [os.path.splitext(img)[0] for img in fullImagesWin]
# MAC
os.chdir(os.path.join(sphinx_config.docFolder, "_static/macWidgets"))
fullImagesMac = glob.glob("*.png")
kImagesMac = [os.path.splitext(img)[0] for img in fullImagesMac]
# Linux
os.chdir(os.path.join(sphinx_config.docFolder, "_static/nixWidgets"))
fullImagesNix = glob.glob("*.png")
kImagesNix = [os.path.splitext(img)[0] for img in fullImagesNix]
os.chdir(sphinx_config.baseFolder)

moduleauthor = "\n\n.. moduleauthor:: Dabo community <dabo-users@leafe.com>\n\n\n\n"

pattern = re.compile(r'{(.*?)}', re.DOTALL)


def bylength(word1, word2):

	return len(word2) - len(word1)


def MangleDocs(myname, docs, strip=True, replacetabs=True):

	if docs:
		if replacetabs:
			docs = docs.replace("\t", "    ")
		lines = docs.split("\n")
	else:
		lines = ['', '', '']
	twopoints = False
	empty = 0
	tostrip = True
	addspace = 0

	for i, line in enumerate(lines):

		if not line.strip():
			empty += 1
		else:
			empty = 0

		if empty == 2:
			tostrip = True
			empty = 0
			addspace = 0

		if strip and tostrip:
			lines[i] = " "*addspace + lines[i].strip()

		if "::" in line:
			tostrip = False

		if ":note:" in line:
			addspace = 1

	stylesDone, extraDone = False, False

	for i, line in enumerate(lines):
		found = False

		if line.startswith("Description"):
			line = "|description| " + line
			lines[i] = line
			found = True

		elif (line.startswith("Usage") or line.startswith("Base Functionalities")) and "::" not in line:
			line = "|usage| " + line
			lines[i] = line
			found = True

		elif line.startswith("Methods and Settings"):
			line = "|settings| " + line
			lines[i] = line
			found = True

		elif line.startswith("Window Styles") and not stylesDone:
			line = "|styles| " + line
			lines[i] = line
			found = True
			stylesDone = True

		elif line.startswith("Window Extra Styles") and not extraDone:
			line = "|extra_styles| " + line
			lines[i] = line
			found = True
			extraDone = True

		elif line.startswith("License "):
			line = "|license| " + line
			lines[i] = line
			found = True

		elif line.startswith("Supported Platform"):
			line = "|platforms| " + line
			lines[i] = line
			found = True

		elif line.startswith("Events"):
			line = "|events| " + line
			lines[i] = line
			found = True

		elif line.startswith("Appearance"):
			line = "|appearance| " + line
			lines[i] = line
			found = True

		elif line.startswith("Example Usage"):
			line = "|usage| " + line
			lines[i] = line
			found = True

		elif line.startswith("See Also"):
			line = "|link| " + line
			lines[i] = line
			found = True

		elif line.startswith("TODOs"):
			line = "|todos| " + line
			lines[i] = line
			found = True

		elif line.startswith("Vision "):
			line = "|vision| " + line
			lines[i] = line
			found = True

		elif line.startswith("What's New"):
			line = "|whatsnew| " + line
			lines[i] = line
			found = True

		elif line.startswith("Layers, Rows "):
			line = "|layers| " + line
			lines[i] = line
			found = True

		elif line.startswith("Backward Incompatibilities"):
			line = "|backward| " + line
			lines[i] = line
			found = True

		if found:
			lines[i+1] = lines[i+1].strip() + "===================\n"

	return "\n".join(lines)


def WriteSphinxFile(name, docs, hasCross=None, moduleData=None, raw=""):

	# ignore privat stuff, except __init__
	if name.startswith("_") and not "__init__" in name:
		return

	# an index for each module
	cross = ".. _%s:\n\n" % name

	fileName = name + "_module.rst"

	currentmodule = ""

	if moduleData:
		module = ".. module:: %s\n\n" % name
		currentName = moduleData.__name__
	else:
		module = ".. module:: %s\n\n" % name
		currentName = name

	icon = "|doc_title| "

	title = name.split(".")[-1:][0]
	if name in allPackages:
		title += " package"
	else:
		title += " module"

	lenSpace = (len(title) + len(icon) + 5)

	title = "="*lenSpace + "\n%s **" % icon + title + "**\n" + "="*lenSpace + "\n\n"
	highlight = "|\n\n.. highlight:: python\n\n"

	text = module + currentmodule + cross + title + highlight +\
									MangleDocs(name, docs, False) + moduleauthor
	tt3 = ""

	# exclude "_" privat stuff in describe_module
	functions, klasses = describe_module(moduleData)

	if functions or klasses:
		text += "\n\n"

	if functions:
		text += functionSummary + "\n"
		for fun, obj in functions:
			text += "* :meth:`~%s`\n" % (obj.__module__ + "." + obj.__name__)

		if klasses:
			text += "\n\n"

	tclass = []
	if klasses:
		text += classSummary + "\n"
		for kls, obj in klasses:
			# included in tocTree below
			#text += "* :ref:`%s`\n" % (obj.__module__ + "." + kls)
			tclass.append(obj.__module__ + "." + kls)

	glb = glob.glob(name + "*.rst")
	glb.sort(key=str.lower)
	glb = [gl[0:-4] for gl in glb if "_module.rst" not in gl]
	glb2 = []
	for gl in glb:
		if ".__" in gl or "__" not in gl:
			glb2.append(gl)

	strs = ""
	glb2.sort(key=str.lower)
	for gl in glb2:
		strs += "   %s\n" % gl

	if name == "dabo.dabo":
		text += DABO_modules
	else:
		if strs:
			text += OTHER_TocTree % strs
		else:
			if name in noTOCforMods:
				# no toc for these in the _module, there are no sub-mods for them
				text += "\n"
			else:
				text += OTHER_TocTree % ("   " + name + "*")

	with open(fileName, "wt") as fid:
		fid.write(imagesLinks + text + raw)

	tfun = ""

	if functions:
		fun, obj = functions[0]
		objName = obj.__module__
		funName = "%s.rst" % (objName)
		text = ".. module:: %s\n\n" % obj.__module__
		# an index for each function
		text += ".. _%s:\n\n" % (obj.__module__+ "._Functions")

		tfun = obj.__module__ + "._Functions"

		icon = "|doc_title| "

		fixName = obj.__module__.split(".")[-1:][0]
		leno = len(fixName) + 15 + len(icon)
		text += "="*leno + "\n**" + fixName + "** functions\n" + "="*leno + "\n\n"

		text += "This is the description of standalone Python functions in the **%s** module.\n\n" % obj.__module__
		text += "|method_summary| Functions Summary\n" + "="*34 + "\n\n"
		summary = ""
		for fun, obj in functions:
			summary += "   %s\n"%fun

		text += autosummary%summary + "\n"
		text += "|API| Functions API\n" + "="*19 + "\n\n\n"

		for fun, obj in functions:
			text += describe_func(obj)

		with open(funName, "wt") as fid:
			fid.write(imagesLinks + text + raw)

	if klasses:
		for kls, obj in klasses:
			kModName = obj.__module__
			klsName = "%s.rst" % (kModName + "." + kls)
			text = describeDaboKlass(obj, kls, klsName)
			with open(klsName, "wt") as fid:
				fid.write(imagesLinks + text + raw)

def MakeInitDocs(name, raw):
	if not os.path.exists(sphinx_config.rstTempFolder):
		os.makedirs(sphinx_config.rstTempFolder)
	os.chdir(sphinx_config.rstTempFolder)

	# prefix topLayer
	tag = topLayer + "." + name
	docs = __import__(name).__doc__

	# do the dabo_module.rst
	WriteSphinxFile(tag, docs, raw=raw)

	# do the subPackage_module.rst
	for subP in subPackages:
		# prefix topLayer
		tag = topLayer + "." + subP
		docs = __import__(tag, fromlist=subP).__doc__
		WriteSphinxFile(tag, docs, raw=raw)

		if subSubPackages.has_key(subP):
			for subSubP in subSubPackages[subP]:
				# prefix topLayer
				tag = topLayer + "." + subP + "." + subSubP
				#following does not work for subsubs
				#docs = __import__(tag).__doc__
				docs = ''
				WriteSphinxFile(tag, docs, raw=raw)

def MakeModuleDocs(folder=None, raw=""):
	"""Get the .py files from the folder and generate a .rst file for each one found,
	except for the ones defined in "toRemove"
	"""
	os.chdir(sphinx_config.folderToDoc)
	if folder is None:
		otherPython = glob.glob("*.py")
	else:
		pFolder = folder.replace(".", os.path.sep)
		otherPython = glob.glob(pFolder + "/*.py")

	for item in toRemove:
		if folder:
			pFolder = folder + "."
			pFolder = pFolder.replace(".", os.path.sep)
			cItem = pFolder + item
		else:
			cItem = item
		if cItem in otherPython:
			otherPython.remove(cItem)

	os.chdir(sphinx_config.rstTempFolder)

	for item in otherPython:
		moduleName = topLayer + os.path.sep + os.path.splitext(item)[0]
		hasPoint = os.path.sep in moduleName
		try:
			if hasPoint:
				mainName, secondaryName = os.path.split(moduleName)
				moduleName = moduleName.replace(os.path.sep, ".")
				moduleData = __import__(moduleName, fromlist=[secondaryName])
			else:
				moduleData = __import__(moduleName)
		except ImportError:
			# Print a message, and ignore
			print("Could not import %s; skipping..." % moduleName)
			continue

		docs = moduleData.__doc__
		realName = None
		for objects in dir(moduleData):
			if objects.lower() == moduleName:
				realName = objects

		hasCross = None
		if realName is None:

			if "." in moduleName:
				name = moduleName[moduleName.index(".")+1:]
			else:
				name = moduleName

			realName = moduleName
			hasCross = name

		WriteSphinxFile(moduleName, docs, hasCross, moduleData, raw=raw)

def describe_builtin(obj):
	""" Describe a builtin function """

	# Built-in functions cannot be inspected by
	# inspect.getargspec. We have to try and parse
	# the __doc__ attribute of the function.
	docstr = obj.__doc__
	args = ''

	if docstr:
		items = docstr.split('\n')
		if items:
			func_descr = items[0]
			s = func_descr.replace(obj.__name__,'')
			idx1 = s.find('(')
			idx2 = s.find(')',idx1)
			if idx1 != -1 and idx2 != -1 and (idx2>idx1+1):
				args = s[idx1+1:idx2]

def describeDaboMethods(kls, methods, klsfilename):
	""" Describe the methods object passed as argument."""

	global uniqueLinkCounter
	sumDict = {}

	inheritedMethods = ""
	ownMethods = ""
	methods.sort(key=operator.itemgetter(0))
	for method in methods:
		isInherited = False
		strs = ""

		if type(kls) == type:
			m = None
			definedIn = None
			for o in kls.__mro__:
				try:
					m = o.__dict__[method]
					definedIn = o
				except KeyError:
					continue
				break
			if m is None:
				return ""
		else:
			m = getattr(kls, method)
			definedIn = kls

		if definedIn != kls:
			isInherited = True

		args = inspect.getargspec(m)
		args = inspect.formatargspec(args[0], args[1], args[2], args[3])

		# we need to create a unique label for use in the summary table
		uniqueLinkLabel = "no-" + str(uniqueLinkCounter)
		uniqueLinkCounter += 1
		strs += ".. _%s:\n\n" % (uniqueLinkLabel, )

		rArgs = args.replace(" **", " \**").replace(" *", " \*")
		# have to use kls info to prevent duplicate definition, because of Dabo name mangling
		strs += ".. function:: " + kls.__module__ + "." + kls.__name__ + "." + method + rArgs

		if isInherited:
			strs += "\n   :noindex:\n"

		strs += "\n\n"
		doc = ""
		sumDoc = ""
		if m.__doc__ is None:
			strs += "\n"
		else:
			lc = 0
			for line in m.__doc__.splitlines():
				doc += "   " + line.replace("\t", "", 2).replace("\t", "    ") + "\n"
				if lc == 0 and line.strip() != "":
					sumDoc = line.replace("\t", "")
					lc += 1
			strs += doc + "\n\n"

		# summary info
		sumDict[uniqueLinkLabel] = [method, sumDoc[:100].strip() ]

		if isInherited:
			if definedIn.__module__ in noInheritLink:
				strs += "Inherited from: '%s - can not provide a link\n" % (definedIn.__module__ + "." + definedIn.__name__)
			elif definedIn.__module__ + "." + definedIn.__name__ in noInheritLinkDabo:
				strs += "Inherited from: '%s - can not provide a link\n" % (definedIn.__module__ + "." + definedIn.__name__)
			else:
				strs += "Inherited from: :ref:`%s`\n" % (definedIn.__module__ + "." + definedIn.__name__)

		strs += "\n-------\n\n"

		if isInherited:
			inheritedMethods += strs
		else:
			ownMethods += strs

	allStrs = ""

	# do the summary
	allStrs += methodSummary

	# get longest entry
	lEntry = 0
	sortkeys = [(sumDict.get(sumkey)[0], sumkey) for sumkey in sumDict.keys()]
	sortkeys.sort()

	for sorter, key in sortkeys:
		tLen = len(sumDict[key][0]) + len(key)
		if tLen > lEntry:
			lEntry = tLen
	# adjust it for :ref:, spaces and <>
	lEntry = lEntry + 10
	lTabDef = "="*lEntry
	rTabDef = " ========================\n"
	allStrs += "\n" + lTabDef + rTabDef
	for sorter, key in sortkeys:
		theRef = ":ref:`%s <%s>`" % (sumDict[key][0], key)
		allStrs += theRef.ljust(lEntry) + " %s\n" % sumDict[key][1]
	allStrs += "\n" + lTabDef + rTabDef + "\n"

	if ownMethods:
		allStrs += "\nMethods\n"
		allStrs += "=======\n\n"
		allStrs += ownMethods
	if inheritedMethods:
		allStrs += "\nMethods - inherited\n"
		allStrs += "=====================\n\n"
		allStrs += inheritedMethods

	return allStrs

def describeDaboProperties(kls, props):
	""" Describe the properties object passed as argument."""

	global uniqueLinkCounter
	sumDict = {}

	inheritedProps = ""
	ownProps = ""

	for prop in props:
		isInherited = False
		strs = ""

		# we need to create a unique label for use in the summary table
		uniqueLinkLabel = "no-" + str(uniqueLinkCounter)
		uniqueLinkCounter += 1
		strs += ".. _%s:\n\n" % (uniqueLinkLabel, )

		if prop[:9] == "[Dynamic]":
			prop = prop[9:]
		d = kls.getPropertyInfo(prop)

		strs += "**" + prop + "** " + "\n\n"
		sumDoc = ""
		if d["doc"] is None:
			strs += "\n"
		else:
			lc = 0
			doc = ""
			for line in d["doc"].splitlines():
				doc += line.replace("\t", "", 2).replace("\t", "    ") + "\n"
				if lc == 0 and line.strip() != "":
					sumDoc = line.replace("\t", "")
					lc += 1

			strs += doc + "\n\n"

		# summary info
		sumDict[uniqueLinkLabel] = [prop, sumDoc[:100].strip() ]


		if d["definedIn"] != kls:
			definedIn = d["definedIn"]
			isInherited = True
			if definedIn.__module__ in noInheritLink:
				# we shouldn't get here, as we use getPropertyList with onlyDabo=True
				strs += "Inherited from: '%s - can not provide a link\n" % (definedIn.__module__ + "." + definedIn.__name__)
			elif definedIn.__module__ + "." + definedIn.__name__ in noInheritLinkDabo:
				strs += "Inherited from: '%s - can not provide a link\n" % (definedIn.__module__ + "." + definedIn.__name__)
			else:
				strs += "Inherited from: :ref:`%s`\n" % (definedIn.__module__ + "." + definedIn.__name__)

		strs += "\n-------\n\n"

		if isInherited:
			inheritedProps += strs
		else:
			ownProps += strs

	allStrs = ""

	# do the summary
	allStrs += propertySummary

	# get longest entry
	lEntry = 0
	sumkeys = sumDict.keys()
	sumkeys.sort()
	for key in sumkeys:
		tLen = len(sumDict[key][0]) + len(key)
		if tLen > lEntry:
			lEntry = tLen
	# adjust it for :ref:, spaces and <>
	lEntry = lEntry + 10
	lTabDef = "="*lEntry
	rTabDef = " ========================\n"
	allStrs += "\n" + lTabDef + rTabDef
	for key in sumkeys:
		theRef = ":ref:`%s <%s>`" % (sumDict[key][0], key)
		allStrs += theRef.ljust(lEntry) + " %s\n" % sumDict[key][1]
	allStrs += "\n" + lTabDef + rTabDef + "\n"

	if ownProps:
		allStrs += "\nProperties\n"
		allStrs += "==========\n\n"
		allStrs += ownProps
	if inheritedProps:
		allStrs += "\nProperties - inherited\n"
		allStrs += "========================\n\n"
		allStrs += inheritedProps

	return allStrs

def describeDaboEvents(kls, events):
	""" Describe the event objects passed as argument."""

	global uniqueLinkCounter
	sumDict = {}

	allEvents = ""
	for event in events:
		strs = ""
		# we need to create a unique label for use in the summary table
		uniqueLinkLabel = "no-" + str(uniqueLinkCounter)
		uniqueLinkCounter += 1
		strs += ".. _%s:\n\n" % (uniqueLinkLabel, )

		e = dEvents.__dict__[event]

		strs += "**" + event + "** " + "\n\n"
		sumDoc = ""
		if e.__doc__ is None:
			strs += "\n"
		else:
			lc = 0
			doc = ""
			for line in e.__doc__.splitlines():
				doc += line.replace("\t", "", 1).replace("\t", "    ") + "\n"
				if lc == 0 and line.strip() != "":
					sumDoc = line.replace("\t", "")
					lc += 1

			strs += doc + "\n\n"

		# summary info
		sumDict[uniqueLinkLabel] = [event, sumDoc[:100].strip() ]

		strs += "\n-------\n\n"

		allEvents += strs

	allStrs = ""

	# do the summary
	allStrs += eventSummary

	# get longest entry
	lEntry = 0
	sumkeys = sumDict.keys()
	sumkeys.sort()
	for key in sumkeys:
		tLen = len(sumDict[key][0]) + len(key)
		if tLen > lEntry:
			lEntry = tLen
	# adjust it for :ref:, spaces and <>
	lEntry = lEntry + 10
	lTabDef = "="*lEntry
	rTabDef = " ========================\n"
	allStrs += "\n" + lTabDef + rTabDef
	for key in sumkeys:
		theRef = ":ref:`%s <%s>`" % (sumDict[key][0], key)
		allStrs += theRef.ljust(lEntry) + " %s\n" % sumDict[key][1]
	allStrs += "\n" + lTabDef + rTabDef + "\n"


	if allEvents:
		allStrs += "\nEvents\n"
		allStrs += "=======\n\n"
		allStrs += allEvents

	return allStrs

def describe_func(obj, method=False, kls=""):
	"""
	Describe the function object passed as argument.
	If this is a method object, the second argument will
	be passed as True, kls is used to fix up the automethod something.__init__
	"""

	strs = ""

	if method:
		if obj.__name__ == "__init__":
			if kls:
				tmp = kls + "." + obj.__name__
			else:
				tmp = obj.__module__ + "." + obj.__name__
			strs += '   .. automethod:: %s\n' % tmp
			return strs
		else:
			return strs
	else:
		if obj.__name__ in excludedFunctions:
			return strs

	strs += '   .. autofunction:: %s' % (obj.__module__ + "." + obj.__name__)

	try:
		arginfo = inspect.getargspec(obj)
	except TypeError:
		return strs

	args = arginfo[0]
	argsvar = arginfo[1]
	input = []

	if args:
		if args[0] == 'self':
			args.pop(0)

		input = args
		defargs, defval = [], []

		if arginfo[3]:
			dl = len(arginfo[3])
			al = len(args)
			defargs = args[al-dl:al]
			defval = arginfo[3]

	strs += "("
	for indx, item in enumerate(input):
		if indx > 0:
			strs += ", "
		if item in defargs:
			index = defargs.index(item)
			strs += "%s=%s"%(item.strip(), repr(defval[index]).strip())
		else:
			strs += "%s"%item

	strs += ")\n"

	return strs

def describeDaboKlass(obj, klsinc, klsfilename):
	"""Describe the class object passed as argument,
	including its methods

	klsinc is just used to see if we need noindex
	"""

	noIndex = False
	if klsinc in dupNoindex:
		noIndex = True

	subclasses = ""
	superclasses = ""
	try:
		subs = obj.__subclasses__()
	except:
		subs = []

	sups = list(obj.__bases__)

	sortedSubClasses = []
	sortedSupClasses = []

	for item in sups:
		item = repr(item)
		sup = item.replace("<class ", "").replace(">", "")
		if sup.startswith("wx.") or sup.startswith("<type"):
			continue
		sortedSupClasses.append(sup.strip().replace('"', "").replace("'", ""))

	if subs:
		for s in subs:
			s = repr(s)
			start = s.index("'")
			end = s.rindex("'")
			cls = s[start+1:end]
			sortedSubClasses.append(cls)
		sortedSubClasses.sort()
		for cls in sortedSubClasses:
			if "._" in cls:
				# ingore all the privat classes which somehow got here
				continue
			else:
				if cls in noSuClassLink:
					subclasses += "* %s - can not provide a link\n" % cls
				else:
					subclasses += "* :ref:`%s`\n" % cls

		subclasses = knownSubs % subclasses

	if sortedSupClasses:
		sortedSupClasses.sort()
		for s in sortedSupClasses:
			if "wx.lib.agw." in s:
				# intersphinx is not yet working for this
##              cls = "<agw:%s>" % s.replace("wx.lib.agw.", "")
				cls = s
			else:
				cls = s
			if "._" in cls:
				# ingore all the privat classes which somehow got here
				continue
			else:
				if cls in noSuClassLink:
					superclasses += "* %s - can not provide a link\n" % cls
				else:
					superclasses += "* :ref:`%s`\n" % cls

		superclasses = knownSups % superclasses

	name = obj.__module__
	strs = ".. module:: %s\n\n" % name

	# an index for each name within the module
	# if daboHack then this will create one with original name e.g. dabo.ui.uiwx
	strs += ".. _%s:\n\n" % (obj.__module__ + "." + obj.__name__)
	# if source is in package, create another index
	if "__init__" in obj.__module__:
		strs += ".. _%s:\n\n" % (obj.__module__.replace(".__init__", "") + "." + obj.__name__)

	icon = "|doc_title| "

	fixName = obj.__module__.split(".")[-1:][0] + "." + obj.__name__
	lenSpace = (len(fixName) + len(icon) + 13) # emphasize and class text

	strs += "="*lenSpace + "\n%s **"%icon + fixName + "** - class\n" + "="*lenSpace + "\n\n"

	if obj.__doc__:
		strs += MangleDocs(obj.__name__, obj.__doc__) + "\n\n"

	count = 0
	keys = obj.__dict__.keys()
	keys.sort()
	kls = obj

	if "__init__" in keys:
		keys.remove("__init__")
		keys.insert(0, "__init__")

	methodNames = []
	for name in keys:
		item = getattr(obj, name)
		if inspect.ismethod(item):
			methodNames.append((name, item))

	strs += "\n"

	hasPicture = ""
	# is there any image present?
	if kls.__name__ in kImagesMac or kls.__name__ in kImagesWin or kls.__name__ in kImagesNix:
		hasPicture = classImage
		imgScale = "75 %"
		if kls.__name__ in kImagesMac:
			index = kImagesMac.index(kls.__name__)
			imgName = fullImagesMac[index]
			hasPicture += classImageMac % (imgName, imgScale, imgName, kls.__name__)
		else:
			hasPicture += classImageMacNO

		if kls.__name__ in kImagesWin:
			index = kImagesWin.index(kls.__name__)
			imgName = fullImagesWin[index]
			hasPicture += classImageWin % (imgName, imgScale, imgName, kls.__name__)
		else:
			hasPicture += classImageOthNO

		if kls.__name__ in kImagesNix:
			index = kImagesNix.index(kls.__name__)
			imgName = fullImagesNix[index]
			hasPicture += classImageNix % (imgName, imgScale, imgName, kls.__name__)
		else:
			hasPicture += classImageOthNO

		pictureIndex[kls.__name__] = klsfilename.replace(".rst", ".html")

	else:
		hasPicture = ""


	if superclasses:
		strs += inheritanceDabo % (kls.__name__, kls.__name__)
		strs += superclasses

	if subclasses:
		strs += subclasses

	if hasPicture:
		strs += hasPicture

	# just get the class definition and doc, the rest we do manually
	strs += "\n|API| Class API\n"
	strs += "===============\n\n"

	modName = kls.__module__

	if kls.__name__ in docMembers:
		strs += "\n.. autoclass:: %s" % (modName + "." + kls.__name__)
		if noIndex:
			strs += "\n   :noindex:"
		strs += "\n   :members:\n\n"
	else:
		strs += "\n.. autoclass:: %s" % (modName + "." + kls.__name__)
		if noIndex:
			strs += "\n   :noindex:"
		strs += "\n\n"

	for name, item in methodNames:
		strs += describe_func(item, True, modName + "." + kls.__name__)

	if hasattr(kls, "getPropertyList"):
		# as per Paul, only include Dabo's properties
		strs += describeDaboProperties(kls, kls.getPropertyList(refresh=True, onlyDabo=True))

	if hasattr(kls, "getEventList"):
		strs += describeDaboEvents(kls, kls.getEventList())

	if hasattr(kls, "getMethodList"):
		strs += describeDaboMethods(kls, kls.getMethodList(refresh=True), klsfilename)

	return strs

def describe_module(module):

	count = 0

	d = dir(module)
	d.sort()

	klasses, functions, methods = [], [], []

	for name in d:
		obj = getattr(module, name)
		if name == "_":
			continue
		if inspect.isclass(obj):
			if obj.__module__ in excludedClasses or name in excludedClasses:
				continue
			if obj.__module__ != module.__name__:
				continue
			# ignore "_", i.e. privat
			if name.startswith("_"):
				continue
			klasses.append((name, obj))
		elif inspect.isfunction(obj):
			if obj.__module__ != module.__name__:
				continue
			# ignore "_", i.e. privat
			if name.startswith("_"):
				continue
			if name in excludedFunctions:
				continue
			functions.append((name, obj))
		elif inspect.ismethod(obj):
			# ignore "_", i.e. privat
			if name.startswith("_"):
				continue
			methods.append((name, obj))
		elif inspect.isbuiltin(obj):
			describe_builtin(obj)

	klasses.sort(key=operator.itemgetter(0))
	functions.sort(key=operator.itemgetter(0))

	return functions, klasses

def AddPrettyTable(text, isModule, fileName):

	newtext = """<br>
<table border="1" class="docutils"> """
	newtext2 = """<br>
<table border="1" class="last docutils"> """

	text = text.replace('<table border="1" class="docutils">', newtext)

	text = text.replace('<table border="1" class="last docutils">', newtext2)

	othertext = """class="pretty-table"><caption>%s</caption>"""

	currentCaption = " "
	returnCaption = " "

	if isModule:
		thefile = os.path.split(fileName)[1]
		lines = text.split("\n")
		for indx, line in enumerate(lines):
			if 'class="docutils"' in line:
				lines[indx] = lines[indx].replace('class="docutils">', othertext%currentCaption)
				currentCaption = " "
			elif 'class="last docutils"' in line:
				lines[indx] = lines[indx].replace('class="last docutils">', othertext%returnCaption)
				returnCaption = " "

			elif "Window Styles" in line:
				currentCaption = "Window styles for <b>%s</b>"%thefile[0:-12]
			elif "Window Extra" in line:
				currentCaption = "Window extra styles for <b>%s</b>"%thefile[0:-12]
			elif "Events Processing" in line:
				currentCaption = "Events processing for <b>%s</b>"%thefile[0:-12]
			elif '<tt class="descname">' in line:
				start = line.index(">")
				end = line.index("</tt>")
				returnCaption = line[start+1:end]

		return "\n".join(lines)

	lines = text.split("\n")
	skip = False

	currentCaption = " "
	returnCaption = " "

	for indx, line in enumerate(lines):
		if "method-summary-" in line or "Table of Contents" in line:
			skip = True
		elif "</table>" in line:
			skip = False

		if " Code Statistics" in line:
			currentCaption = "Code statistics for <b>Dabo</b> (%s)"%datetime.datetime.now().strftime("%d-%B-%Y")
		elif "&#8211;" in line and "</em>" in line and "<em>" in line:
			em1, em2 = line.index("<em>"), line.index("</em>")
			parameter = line[em1+4:em2]
			currentCaption = "<b>%s</b> parameter settings"%parameter
		elif '<tt class="descname">' in line:
			start = line.index(">")
			end = line.index("</tt>")
			returnCaption = line[start+1:end]
			returnCaption = "Return values for <b>%s</b>"%returnCaption

		if not skip:
			if 'class="docutils">' in line:
				lines[indx] = lines[indx].replace('class="docutils">', othertext%currentCaption)
				currentCaption = " "
			elif 'class="last docutils"' in line:
				lines[indx] = lines[indx].replace('class="last docutils">', othertext%returnCaption)
				returnCaption = " "


	return "\n".join(lines)

def WriteGeneralIndex():

	fid = open("general_index.rst", "wt")
	lastLen = 0
	fid.write(imagesLinks + "\n")
	fid.write("\n.. _daboindex:\n\n")
	fid.write("================================\n")
	fid.write("|doc_title| Master Index\n")
	fid.write("================================\n\n")
	fid.write(genindex)

	# not that great
	fid.write("\nPackage Index")
	fid.write("\n=============\n\n")
	fid.write(".. tocTree::\n")
	fid.write("   :maxdepth: 1\n\n")
	allPkgForIndex = allPackages
	# these are already in dabo.ui, so don't show them here again
	allPkgForIndex.remove("dabo.ui.dialogs")
	allPkgForIndex.remove("dabo.ui.uiwx")
	for item in allPkgForIndex:
		fid.write(("   %s_module\n" % item))
	fid.write("\n\n")

	# now do all the items within each package
	all = glob.glob(sphinx_config.rstTempFolder + "\*.rst")

	dTop = []
	dBiz = []
	dLib = []
	dLibA = []
	dLibD = []
	dDb = []
	dDbx = []
	dUi = []
	dUix = []
	dUid = []

	for item in all:
		if "dabo.biz" in item and not "_module.rst" in item:
			dBiz.append(item)
		elif "dabo.db.db" in item and not "_module.rst" in item:
			dDb.append(item)
		elif "dabo.db" in item and not "_module.rst" in item:
			dDbx.append(item)
		elif "dabo.lib.autosuper" in item and not "_module.rst" in item:
			dLibA.append(item)
		elif "dabo.lib.datanav" in item and not "_module.rst" in item:
			dLibD.append(item)
		elif "dabo.lib" in item and not "_module.rst" in item:
			dLib.append(item)

		elif "dabo.ui.uiwx" in item and not "_module.rst" in item:
			dUix.append(item)
		elif "dabo.ui.dialogs" in item and not "_module.rst" in item:
			dUid.append(item)
		elif "dabo.ui" in item and not "_module.rst" in item:
			dUi.append(item)

		elif "index" in item and not "_module.rst" in item:
			pass
		elif not "_module.rst" in item:
			dTop.append(item)

	fid.write("Dabo\n")
	fid.write("====\n\n")
	fid.write(".. tocTree::\n")
	fid.write("   :maxdepth: 1\n\n")
	for item in dTop:
		fid.write("   %s\n" % os.path.split(item)[1].replace(".rst", ""))
	fid.write("\n\n")

	fid.write("Dabo - db\n")
	fid.write("=========\n\n")
	fid.write(".. tocTree::\n")
	fid.write("   :maxdepth: 1\n\n")
	for item in dDb:
		fid.write("   %s\n" % os.path.split(item)[1].replace(".rst", ""))
	for item in dDbx:
		fid.write("   %s\n" % os.path.split(item)[1].replace(".rst", ""))
	fid.write("\n\n")

	fid.write("Dabo - biz\n")
	fid.write("==========\n\n")
	fid.write(".. tocTree::\n")
	fid.write("   :maxdepth: 1\n\n")
	for item in dBiz:
		fid.write("   %s\n" % os.path.split(item)[1].replace(".rst", ""))
	fid.write("\n\n")

	# write the UI index stuff, use it here and further below
	uiIndexText = WriteUiPackageIndex(dUix, dUid, dLibD)

	fid.write(uiIndexText)

	fid.write("Dabo - lib\n")
	fid.write("==========\n\n")
	fid.write(".. tocTree::\n")
	fid.write("   :maxdepth: 1\n\n")
	for item in dLib:
		fid.write("   %s\n" % os.path.split(item)[1].replace(".rst", ""))
	for item in dLibA:
		fid.write("   %s\n" % os.path.split(item)[1].replace(".rst", ""))
	fid.write("\n\n")

	#
	# a hack to get rid of the toc warning for these
	fid.write(".. tocTree::\n")
	fid.write("   :glob:\n")
	fid.write("   :hidden:\n\n")

	fid.write("   dabo.biz_module\n")
	fid.write("   dabo.dabo_module\n")
	fid.write("   dabo.db_module\n")
	fid.write("   dabo.lib_module\n")
	fid.write("   dabo.ui_module\n")
	fid.write("   dabo.ui*\n")

	fid.close()

	# create the index for the ui_module
	fid = open("dabo.ui_module.rst", "wt")
	fid.write(imagesLinks + "\n")
	fid.write(".. _dabo.ui:\n\n")
	fid.write("=================================\n")
	fid.write("|doc_title| **dabo - ui package**\n")
	fid.write("=================================\n\n")

	fid.write(uiIndexText)
	fid.close()

def WriteUiPackageIndex(dUix, dUid, dLibD):

	indexText = ""
	controlClasses, formClasses, sizerClasses = GetUiClasses()

	indexText += "Dabo - UI - form classes\n"
	indexText += "========================\n\n"
	indexText += ".. tocTree::\n"
	indexText += "   :maxdepth: 1\n\n"

	for item in formClasses:
		indexText += "   %s\n" % item
	indexText += "\n\n"

	indexText += "Dabo - UI - control classes\n"
	indexText += "===========================\n\n"
	indexText += ".. tocTree::\n"
	indexText += "   :maxdepth: 1\n\n"

	for item in controlClasses:
		if not item in deprecatedClasses:
			indexText += "   %s\n" % item
	indexText += "\n\n"

	indexText += "Dabo - UI - sizer classes\n"
	indexText += "=========================\n\n"
	indexText += ".. tocTree::\n"
	indexText += "   :maxdepth: 1\n\n"

	for item in sizerClasses:
		indexText += "   %s\n" % item
	indexText += "\n\n"

	indexText += "Dabo - Dialogs\n"
	indexText += "==============\n\n"
	indexText += ".. tocTree::\n"
	indexText += "   :maxdepth: 1\n\n"
	for item in dUid:
		indexText += "   %s\n" % os.path.split(item)[1].replace(".rst", "")
	indexText += "\n\n"

	indexText += "Dabo - ui other\n"
	indexText += "===============\n\n"
	indexText += ".. tocTree::\n"
	indexText += "   :maxdepth: 1\n\n"

	alreadyCovered = controlClasses + formClasses + sizerClasses
	for item in dUix:
		theItem = os.path.split(item)[1].replace(".rst", "")
		if not theItem in alreadyCovered:
			indexText += "   %s\n" % theItem
	indexText += "\n\n"

	indexText += "Dabo - ui datanav\n"
	indexText += "=================\n\n"
	indexText += ".. tocTree::\n"
	indexText += "   :maxdepth: 1\n\n"
	for item in dLibD:
		indexText += "   %s\n" % os.path.split(item)[1].replace(".rst", "")
	indexText += "\n\n"

	return indexText

def GetUiClasses():
	# Now we dynamically gather the ui classes to document:
	controlClasses = []
	formClasses = []
	sizerClasses = []

	for i in dir(dabo.ui):
		item = dabo.ui.__dict__[i]
		if type(item) == type:
			if "Mixin" not in item.__name__:
				if issubclass(item, dabo.ui.dControlMixin):
					itemName = str(item).replace("<class '", "")
					itemName = itemName.replace("'>", "")
					controlClasses.append(itemName)
				if issubclass(item, dabo.ui.dFormMixin):
					itemName = str(item).replace("<class '", "")
					itemName = itemName.replace("'>", "")
					formClasses.append(itemName)
				if issubclass(item, dabo.ui.dSizerMixin):
					itemName = str(item).replace("<class '", "")
					itemName = itemName.replace("'>", "")
					sizerClasses.append(itemName)

	return controlClasses, formClasses, sizerClasses

def WriteIndex(folder):

	if folder in [sphinx_config.normalHtml]:
		fileName = "index_normal.rst"
	elif folder == sphinx_config.helpHtml:
		fileName = "index_htmlhelp.rst"
	else:
		fileName = "index_latex.rst"

	fid = open("_rst_basefiles/"+fileName, "rt")
	text = fid.read()
	fid.close()

	# create the index.rst with the approriate data
	fid = open("source/index.rst", "wt")
	fid.write(text)
	fid.close()

	# need the | otherwise we might have transitions "--------" at the end of a file, which is not allowed
	raw = "\n|\n"

	return raw

def MakeRst(builder):
	raw = WriteIndex(builder)

	# create the *_module.rst for top layer and packages
	MakeInitDocs(topLayer, raw)
	# create the module docs for the top level
	MakeModuleDocs(None, raw)
	# now process all packages defined in subPackages
	for pkg in subPackages:
		MakeModuleDocs(pkg, raw)
		# now the ones for packages in packages
		if subSubPackages.has_key(pkg):
			for sPkg in subSubPackages[pkg]:
				MakeModuleDocs(pkg + '.' + sPkg, raw)

	WriteGeneralIndex()

def FractSec(s):

	min, s = divmod(s, 60)
	h, min = divmod(min, 60)
	return h, min, s

start = time.time()

args = sys.argv[1:]

if not args:
	builder = 'html'
	rebuildall = False
else:
	if len(args) != 2:
		print "you have to supply two args"
		print "e.g. 'html True' to use the html builder and force a full rebuild"
		sys.exit(2)
	else:
		if args[0] in sphinx_config.validBuilders:
			builder = args[0]
		else:
			print "builder %s is not valid" % args[0]
			sys.exit(2)
		if args[1].lower() == 'true':
			rebuildall = True
		else:
			rebuildall = False


def main():
	print "================================================"
	print "removing files from previous run in %s" % sphinx_config.rstTempFolder
	print "================================================"
	remRst = glob.glob(sphinx_config.rstTempFolder + "//*.rst")
	for item in remRst:
		os.remove(item)


	if rebuildall:
		print "================================================"
		print "removing files, forcing a full rebuild %s" % sphinx_config.docFolder
		print "================================================"

		oldRst = glob.glob(sphinx_config.docFolder + "//*.rst")
		for item in oldRst:
			os.remove(item)

	# generate .rst in tempFolder
	MakeRst(builder)

	# write picture index to a file
	genNote = """This file is generated by makeRST.py and used by genGallery.py,
	please do not change it by hand.
	"""
	indexF = open(os.path.join(sphinx_config.baseFolder, "galleryToClassIndex.py"), "w")
	indexF.write("# -*- coding: utf-8 -*-#\n\n")
	indexF.write('"""%s"""\n\n' % genNote)
	indexF.write("pictureIndex = {}\n")
	for item in pictureIndex:
		indexF.write("pictureIndex['%s'] = '%s'\n" % (item, pictureIndex[item]))
	indexF.close()

	# compare files in rstTempFolder to docFolder, if changed copy to docFolder
	print "========================================"
	print "check if file(s) have changed"
	print "========================================"

	checkRst = glob.glob(sphinx_config.rstTempFolder + "//*.rst")
	for item in checkRst:
		path, fileName = os.path.split(item)
		tmpFile = os.path.join(sphinx_config.rstTempFolder, fileName)
		docFile = os.path.join(sphinx_config.docFolder, fileName)
		if os.path.isfile(docFile):
			if not filecmp.cmp(tmpFile, docFile, False):
				# file has changed, copy it
				shutil.copy(tmpFile, docFile)
				print "changed file, copy to: %s" % docFile
		else:
			shutil.copy(tmpFile, docFile)
			print "new file, copy to: %s" % docFile


	current = time.time()
	h, m, s = FractSec(int(current - start))

	print "\nDabo .rst files created. Elapsed time %02d:%02d:%02d"%(h, m, s)


if __name__ == "__main__":
	main()
