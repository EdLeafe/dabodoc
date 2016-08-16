# -*- coding: utf-8 -*-#

import os
import sys
import time
import shutil
import stat
import platform

# force it, otherwise the none ASCII stuff causes a problem for Sphinx
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding

import subprocess

import conf as sphinx_config

def FractSec(s):

	min, s = divmod(s, 60)
	h, min = divmod(min, 60)
	return h, min, s

def MakeSphinx(builder, rebuildall):
	if platform.system() == "Windows":
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

	sourceFolder = sphinx_config.docFolder
	targetFolder = os.path.join(os.path.join(sphinx_config.baseFolder, 'build'), builder)
	confFolder = sphinx_config.baseFolder

	if rebuildall:
		# clear targetFolder
		shutil.rmtree(targetFolder, ignore_errors=True)

		# TO REBUILD ALL
		# sphinxErrFile is a dup of sphinxStdErr
		command = sphinx_config.sphinxBuildCmd + ' -ac ' + confFolder +' -b '+ builder + \
				'-D', sphinx_config.graphVizDot + sourceFolder +' ' + targetFolder
		commandArgs = [sphinx_config.sphinxBuildCmd, '-ac', confFolder, '-b', builder,
				sourceFolder, targetFolder]
	else:
		# TO REBUILD CHANGED
		command = sphinx_config.sphinxBuildCmd + ' -c ' + confFolder +' -b '+ builder + \
				sphinx_config.graphVizDot + sourceFolder +' ' + targetFolder
		commandArgs = [sphinx_config.sphinxBuildCmd, '-c', confFolder, '-b', builder,
				'-v', '-D', sphinx_config.graphVizDot, sourceFolder, targetFolder]

	if platform.system() == "Windows":
		p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=None,
			stderr=sphinx_config.sphinxStdErrFile, startupinfo=startupinfo).communicate()
	else:
		p = subprocess.Popen(commandArgs, stdin=subprocess.PIPE, stdout=None,
			stderr=sphinx_config.sphinxStdErrFile).communicate()

	if builder == 'htmlhelp':
		hhpFile = os.path.join(os.path.join(targetFolder), sphinx_config.hhpName)
		command = sphinx_config.hhcExe + hhpFile
		if platform.system() == "Windows":
			p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=None,
				stderr=sphinx_config.sphinxStdErrFile, startupinfo=startupinfo).communicate()
		else:
			p = subprocess.Popen(commandArgs, stdin=subprocess.PIPE, stdout=None,
				stderr=sphinx_config.sphinxStdErrFile).communicate()

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
        rebuildall = (args[1].lower() == 'true')

# hack for Sphinx, clear out build/_images folder not to duplicate stuff
targetFolder = os.path.join(os.path.join(sphinx_config.baseFolder, 'build'), builder)
imgFolder = os.path.join(targetFolder, '_images')
if os.path.isdir(imgFolder):
    print "remove from build folder: %s" % imgFolder
    shutil.rmtree(imgFolder)


# build
MakeSphinx(builder, rebuildall)

# walk the tree to change files to writable
#svnFolder = os.path.join(targetFolder, '_static\\macWidgets\\.svn')
#if os.path.isdir(svnFolder):
#    print "remove from build folder: %s" % svnFolder
#    for top, dirs, files in os.walk(svnFolder):
#        for item in files:
#            os.chmod(os.path.join(top, item), stat.S_IWRITE)
#    shutil.rmtree(svnFolder)
#svnFolder = os.path.join(targetFolder, '_static\\winWidgets\\.svn')
#if os.path.isdir(svnFolder):
#    print "remove from build folder: %s" % svnFolder
#    for top, dirs, files in os.walk(svnFolder):
#        for item in files:
#            os.chmod(os.path.join(top, item), stat.S_IWRITE)
#    shutil.rmtree(svnFolder)
#svnFolder = os.path.join(targetFolder, '_static\\nixWidgets\\.svn')
#if os.path.isdir(svnFolder):
#    print "remove from build folder: %s" % svnFolder
#    for top, dirs, files in os.walk(svnFolder):
#        for item in files:
#            os.chmod(os.path.join(top, item), stat.S_IWRITE)
#    shutil.rmtree(svnFolder)

current = time.time()
h, m, s = FractSec(int(current - start))

sphinx_config.sphinxStdErrFile.close()

# check for errors
errF = open(sphinx_config.sStdErr, 'r')
anyErr = errF.read()
if anyErr:
    print "\nThere were errors during the documentation generation, check: %s" % sphinx_config.sStdErr
else:
    print "\nDabo Documentation Sphinx build '%s' is finished. Elapsed time %02d:%02d:%02d" % (builder, h, m, s)
