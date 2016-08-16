import dabo
from dabo.dObject import dObject
from dabo.dEvents import dEvent
dabo.ui.loadUI("wx")

def getDaboModules():
	modules = [
		"dabo", 
		"dabo.dApp", 
		"dabo.dSecurityManager", 
		"dabo.dUserSettingProvider", 
		"dabo.db", 
		"dabo.db.dConnection",
		"dabo.db.dCursorMixin", 
		"dabo.db.dConnectInfo", 
		"dabo.db.dbMySQL",
		"dabo.db.dbPostgreSQL", 
		"dabo.db.dbFirebird",
		"dabo.db.dbSQLite",
		"dabo.biz", 
		"dabo.biz.dBizobj",
		"dabo.ui",
		"dabo.ui.uiwx",
		"dabo.lib.datanav"]

	# Now we dynamically gather the ui classes to document:
	controlClasses = []
	formClasses = []
	sizerClasses = []

	for i in dir(dabo.ui):
		item = dabo.ui.__dict__[i]
		if type(item) == type:
			if "Mixin" not in item.__name__:
				if issubclass(item, dabo.ui.dControlMixin):
					controlClasses.append(item)
				if issubclass(item, dabo.ui.dFormMixin):
					formClasses.append(item)
				if issubclass(item, dabo.ui.dSizerMixin):
					sizerClasses.append(item)

	print "Control Classes:"
	for i in controlClasses:
		modules.append("dabo.ui.uiwx.%s" % i.__name__)
		print "\t %s" % i.__name__

	print "Form Classes:"
	for i in formClasses:
		modules.append("dabo.ui.uiwx.%s" % i.__name__)
		print "\t %s" % i.__name__

	print "Sizer Classes:"
	for i in sizerClasses:
		modules.append("dabo.ui.uiwx.%s" % i.__name__)
		print "\t %s" % i.__name__

	return modules

def getDaboClasses():
	classes = []
	import dabo.db.dbMySQL
	import dabo.db.dbPostgreSQL
	import dabo.db.dbFirebird
	import dabo.db.dbSQLite
	import dabo.db.dbMsSQL
	import dabo.dReportWriter
	import dabo.lib
	import dabo.lib.datanav
	import dabo.ui.dialogs

	for module in (dabo, dabo.dSecurityManager, dabo.dEvents,
	               dabo.dUserSettingProvider, dabo.dException,
	               dabo.db, dabo.biz, dabo.ui, dabo.db.dbMySQL, dabo.db.dbSQLite,
	               dabo.db.dbPostgreSQL, dabo.db.dbMsSQL,
	               dabo.db.dbFirebird, dabo.dReportWriter, 
	               dabo.lib, dabo.lib.datanav, dabo.ui.dialogs):
		for i in dir(module):
			c = module.__dict__[i]
			if type(c) == type and issubclass(c, dObject) and \
					(not issubclass(c, dEvent) or c is dEvent):
				if c not in classes:
					classes.append(c)

#	classes.append(dabo.lib)
#	classes.append(dabo.lib.datanav)
	classes.append(dabo.ui)

	def sortfunc(a,b):
		return cmp(a.__name__, b.__name__)
		
	classes.sort(sortfunc)
	return classes
