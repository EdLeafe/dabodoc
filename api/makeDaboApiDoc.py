#!/usr/bin/env python

import datetime
import inspect
import types
import os
import sys

args = sys.argv[1:]

if not args:
	branch = "trunk"
else:
	branch = args[0]

os.system("rm -rf dabo")
os.system("svn checkout http://svn.dabodev.com/dabo/%s dabo" % branch)
sys.path.insert(0, "./dabo")
if not os.path.exists("./dabo"):
	sys.exit("Please pass a valid dabo branch such as 'trunk', 'branches/stable' or 'tags/dabo-0.7'")

import dabo

dabo.ui.loadUI("wx")
import dabo.dEvents as dEvents
from getDaboModules import getDaboClasses

## This is my new attempt at API documentation, which doesn't use epydoc and 
## will do a better job of only grabbing the things we actually want to
## to document. It is pretty basic now (4 Oct 2005), but does print out the
## PEM's for every Dabo object it finds, although it will need some help
## finding some things (dSecurityManager, dReportWriter, ...). I want to
## add cascading stylesheets and the ability to print to PDF (for an API
## book).  --pkm

d = datetime.datetime.now()

headerString = """
<html>
<title>%(pageTitle)s</title>
<head>
	<style type="text/css">
		body {
			font-family: Helvetica, Arial, sans-serif;
		}

		#container {
			width: 760px;
			border: 1px solid gray;
			margin: 10px;
			margin-left: auto;
			margin-right: auto;
			padding: 10px;
			background-color: white;
			text-align: left;
		}

		#banner {
			padding: 5px;
			margin-bottom: ;
		}

		#content {
			padding: 5px;
		}

		#footer {
			clear: both;
			padding: 5px;
			margin-top: ;
		}

	</style>
</head>

<body bgcolor="linen">

<font size="-1"><p>New API reference documentation is available at <a href="http://docs.dabodev.com/">http://docs.dabodev.com</a>. Please report any problems or suggestions on the
<a href="http://leafe.com/mailman/listinfo/dabo-users">dabo-users</a> mailing list.</p></font>

<div id="#container">
"""

footerString = """
</div>
<div id="#footer">

<hr>
Dabo %s (rev. %s)<br>
%s

</div>
</div>

</body>
</html>
""" % (dabo.version["version"],
         dabo.version["revision"],
         d.strftime("%e %b %Y %T"))


def formatDoc(doc):
	"""Strip indentation whitespace from the docstring."""
	docLines = doc.splitlines()
	if len(docLines) == 0:
		return doc

	# All whitespace from first line:
	docLines[0] = docLines[0].strip()

	# Use the indentation from the second line (third if the second is blank)
	# for the rest of the lines:
	indent = ""
	if len(docLines) > 1:
		if len(docLines[1].strip()) > 0:
			# use indent from this line
			for l in docLines[1]:
				if l.isspace():
					indent += l
				else:
					break
			docLines[1] = docLines[1].strip()
		else:
			if len(docLines) > 2:
				if len(docLines[2].strip()) > 0:
					# use indent from this line
					for l in docLines[2]:
						if l.isspace():
							indent += l
						else:
							break
					docLines[2] = docLines[2].strip()
	for idx, line in enumerate(docLines):
		if line.find(indent) == 0:
			line = line.replace(indent, "", 1)
			docLines[idx] = line

	doc = '\n'.join(docLines)
	doc = doc.replace("<", "&lt;")
	return doc
	
classes = getDaboClasses()

def joinDynamicProps(propList):
	dynProps = [prop[7:] for prop in propList if prop[:7] == "Dynamic"]
	for dp in dynProps:
#		propList.pop(propList.index("Dynamic%s" % dp))
		propList[propList.index(dp)] = "[Dynamic]%s" % dp
	return propList

def getApiDoc(cls, outputType="html-single"):
	PEM_COLUMNS = float(3)  ## float simply for round() to work right

	className = cls.__name__
	if type(cls) == type:
		objectType = "Class"
		for base in cls.__mro__:
			classDoc = base.__doc__
			if classDoc is not None:
				break
	else:
		objectType = "Module"
		classDoc = cls.__doc__

	if classDoc is None:
		classDoc = ""
	classDoc = formatDoc(classDoc)

	pageTitle = "Dabo API Documentation: %(className)s" % locals()
	html = headerString % locals()
	html += """
<div id="#banner">
<h1>%(objectType)s %(className)s</h1>
<pre>%(classDoc)s</pre>
</div>
<hr>

<div id="#content">
""" % locals()

	def getListing(name, items):
		html = """
<h2>%(name)s</h2>
<table width="100%%" cellpadding="5" cellspacing="0" border="0">
""" % locals()

		idx = -1
		for item in items:
			if item[:7] == "Dynamic":
				# Ignore the Dynamic* props in the listing
				continue
			idx += 1
			if idx % PEM_COLUMNS == 0:
				if idx > 0:
					html += """	</tr>
"""
				html += """	<tr>
"""

			dynamicHref = ""
			if item[:9] == "[Dynamic]":
				item = item[9:]
				dynamicHref = """<a href="#%(name)s_Dynamic%(item)s">[Dynamic]</a>""" % locals()

			definedHere = (cls.__dict__.has_key(item))

			formatBeg, formatEnd = "", ""
			if definedHere:
				formatBeg = "<b>"
				formatEnd = "</b>"

			html += """		<td>%(formatBeg)s%(dynamicHref)s<a href="#%(name)s_%(item)s">%(item)s</a>%(formatEnd)s</td>
""" % locals()

		html += """
	</tr>
</table>
<hr>
"""
		return html

	def getExpandedEntries(name, items):
		html = """
<br><br><br>
<h2>%s</h2>
<table border="1" cellpadding="20" cellspacing="0">
""" % name
		
		if name == "Properties":
			for prop in items:
				if prop[:9] == "[Dynamic]":
					prop = prop[9:]
				d = cls.getPropertyInfo(prop)
				if d["doc"] is None:
					d["doc"] = ""
				d["doc"] = formatDoc(d["doc"])	

				d["definedInString"] = ""
				if d["definedIn"] != cls:
					filename = "./%s.%s.html" % (d["definedIn"].__module__, d["definedIn"].__name__)
					if d["definedIn"] in classes:
						link = """<a href="%s">%s</a>""" % (filename, d["definedIn"].__name__)
					else:
						link = "%s" % d["definedIn"].__name__
					d["definedInString"] = """<br><i>(inherited from <b>%s</b>)</i>""" % link

				html += """
	<tr>
		<td valign="top">
			<b><a name="Properties_%(name)s">%(name)s</a></b>
			<pre>%(doc)s</pre>
			%(definedInString)s
		</td>
	</tr>
""" % d


		if name == "Events":
			for event in items:
				e = dEvents.__dict__[event]
				d = {"name": event,
				     "doc": e.__doc__}
				if d["doc"] is None:
					d["doc"] = ""
				d["doc"] = formatDoc(d["doc"])	

				html += """
	<tr>
		<td valign="top">
			<b><a name="Events_%(name)s">%(name)s</a></b><br>
			<pre>%(doc)s</pre>
		</td>
	</tr>
""" % d

		if name in ("Methods", "Functions"):
			for method in items:
				if type(cls) == type:
					m = None
					definedIn = None
					for o in cls.__mro__:
						try:
							m = o.__dict__[method]
							definedIn = o
						except KeyError:
							continue
						break
					if m is None:
						continue
				else:
					m = getattr(cls, method)
					definedIn = cls

				args = inspect.getargspec(m)
				args = inspect.formatargspec(args[0], args[1], args[2], args[3])

				d = {"typ": name,
						"name": method,
						"doc": m.__doc__,
						"args": args}
				if d["doc"] is None:
					d["doc"] = ""
				d["doc"] = formatDoc(d["doc"])	

				d["definedInString"] = ""
				if definedIn != cls:
					filename = "./%s.%s.html" % (definedIn.__module__, definedIn.__name__)
					if definedIn in classes:
						link = """<a href="%s">%s</a>""" % (filename, definedIn.__name__)
					else:
						link = "%s" % definedIn.__name__
					d["definedInString"] = """<br><i>(inherited from <b>%s</b>)</i>""" % link
	

				html += """
	<tr>
		<td valign="top">
			<a name="%(typ)s_%(name)s"><b>%(name)s</b>%(args)s</a>
			<pre>%(doc)s</pre>
			%(definedInString)s
		</td>
	</tr>
""" % d

		html += """
</table>
"""
		return html

		
	# Property, Event, Method Listings:
	propList = []
	eventList = []
	methodList = []
	funcList = []
	onlyDabo = True
	if type(cls) == type:
		# cls is actually a class (good)
		if cls.__name__ == "dReportWriter":
			onlyDabo = False
		propList = joinDynamicProps(cls.getPropertyList(refresh=True, onlyDabo=onlyDabo))
		eventList = cls.getEventList()
		methodList = cls.getMethodList(refresh=True)
		html += getListing("Properties", propList)
		html += getListing("Events", eventList)
		html += getListing("Methods", methodList)
		html += getExpandedEntries("Properties", propList)
		html += getExpandedEntries("Events", eventList)
		html += getExpandedEntries("Methods", methodList)
	else:
		# cls is not really a class, perhaps a module like dabo.ui
		for i in dir(cls):
			if i.isalpha() and i[0].islower() and type(getattr(cls, i)) == types.FunctionType:
				funcList.append(i)
		html += getListing("Functions", funcList)
		html += getExpandedEntries("Functions", funcList)

	html += footerString
	return html

if os.path.exists("./daboApiDoc"):
	for f in os.listdir("./daboApiDoc"):
		os.remove(os.path.join("./daboApiDoc", f))
	os.rmdir("./daboApiDoc")	
	#sys.exit("Please move existing ./daboApiDoc out of the way first.")

os.mkdir("./daboApiDoc")
os.chdir("./daboApiDoc")


for class_ in classes:
	try:
		module = "%s." % class_.__module__
	except AttributeError:
		# class_ could actually be a module (eg dabo.ui)
		module = ""

	filename = "%s%s.html" % (module, class_.__name__)
	html = getApiDoc(class_)
	f = open(filename, "w")
	f.write(html)
	f.close()

pageTitle = "Dabo API Documentation: Contents"
html = headerString % locals()
html += """
<table border="0" cellpadding="5" cellspacing="0" width="100%">
	<tr>
		<td width="33%">&nbsp;</td>
		<td width="33%" valign="top">
			<b>Dabo:</b><br>"""

remove = []
for idx, class_ in enumerate(classes):
	if type(class_) != type:
		continue
	if "dabo.d" in class_.__module__ and "dabo.db" not in class_.__module__:
		html += """
			<a href="./%s.%s.html">%s</a><br>""" % (class_.__module__, class_.__name__,
		                                          class_.__name__)
		remove.insert(0, idx)
for i in remove:
	del(classes[i])

html += """
			<br>
			<br>
		</td>
		<td width="33%">&nbsp;</td>
	</tr>
	<tr>
		<td width="33%" valign="top">
			<b>db:</b><br>"""

remove = []

for idx, class_ in enumerate(classes):
	if type(class_) != type:
		continue
	if "dabo.db" in class_.__module__:
		html += """
			<a href="./%s.%s.html">%s</a><br>""" % (class_.__module__, class_.__name__,
		                                     class_.__name__)
		remove.insert(0, idx)

for i in remove:
	del(classes[i])

html += """
		</td>
		<td width="33%" valign="top">
			<b>biz:</b><br>"""

remove = []
for idx, class_ in enumerate(classes):
	if type(class_) != type:
		continue
	if "dabo.biz" in class_.__module__:
		html += """
			<a href="./%s.%s.html">%s</a><br>""" % (class_.__module__, class_.__name__,
		                                     class_.__name__)
		remove.insert(0, idx)
for i in remove:
	del(classes[i])

html += """
		</td>
		<td width="33%" valign="top">
			<b><a href="./dabo.ui.html">ui</a>:</b><br>"""

remove = []
for idx, class_ in enumerate(classes):
	if type(class_) != type:
		continue
	if "dabo.ui.dialogs" in class_.__module__:
		html += """
			<a href="./%s.%s.html">dialogs.%s</a><br>""" % (class_.__module__, class_.__name__,
		                                     class_.__name__)
	elif "dabo.ui" in class_.__module__:
		html += """
			<a href="./%s.%s.html">%s</a><br>""" % (class_.__module__, class_.__name__,
		                                     class_.__name__)

		remove.insert(0, idx)
for i in remove:
	del(classes[i])

html += """
		</td>
	</tr>
	<tr>
		<td><b>Datanav Sub-Framework</b> (from dabo.lib import datanav):<br>
"""

remove = []
for idx, class_ in enumerate(classes):
	if type(class_) != type:
		continue
	if "dabo.lib.datanav" in class_.__module__:
		html += """
			<a href="./%s.%s.html">%s</a><br>""" % (class_.__module__, class_.__name__,
		                                     class_.__name__)
		remove.insert(0, idx)
for i in remove:
	del(classes[i])

html += """
		</td>
	</tr>
</table>
"""

html += footerString

filename = "index.html"
f = open(filename, "w")
f.write(html)
f.close()
