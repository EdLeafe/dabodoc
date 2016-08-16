
.. include:: _static/headings.txt

.. module:: dabo.db.dbOracle

.. _dabo.db.dbOracle.Oracle:

========================================
|doc_title|  **dbOracle.Oracle** - class
========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Oracle**

.. inheritance-diagram:: Oracle


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dBackend.dBackend`



|API| Class API
===============


.. autoclass:: dabo.db.dbOracle.Oracle

   .. automethod:: dabo.db.dbOracle.Oracle.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1239>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1240>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1241>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1242>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-1243>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-1244>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-1245>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1246>`              The name of the object.  (str)
:ref:`Parent <no-1247>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1248>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-1239:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1240:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1241:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1242:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1243:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1244:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1245:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1246:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1247:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1248:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------


|method_summary| Events Summary
===============================


========== ========================

========== ========================


|method_summary| Methods Summary
================================


============================================ ========================
:ref:`addField <no-1249>`                    Add a field to the field clause.
:ref:`addFrom <no-1250>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-1251>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-1252>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-1253>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-1254>`                    Add an expression to the where clause.
:ref:`afterInit <no-1255>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1256>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1257>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-1258>`            Begin a SQL transaction.
:ref:`bindEvent <no-1259>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-1260>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-1261>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-1262>`           
:ref:`createJustTable <no-1263>`             
:ref:`createTableAndIndexes <no-1264>`       Creates a table and/or indexes based on the dTable passed to it.
:ref:`encloseNames <no-1265>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-1266>`                    
:ref:`flush <no-1267>`                       Only used in some backends
:ref:`formSQL <no-1268>`                     Oracle wants the limit clause as where clause.
:ref:`formatBLOB <no-1269>`                  Properly format a BLOB value to be included in an UPDATE
:ref:`formatDateTime <no-1270>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-1271>`              
:ref:`formatJoinType <no-1272>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-1273>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-1274>`             Return the fully qualified name of the object.
:ref:`getConnection <no-1275>`               
:ref:`getCursor <no-1276>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-1277>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-1278>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-1279>`          
:ref:`getFieldInfoFromDescription <no-1280>` Return field information from the cursor description.
:ref:`getFields <no-1281>`                   
:ref:`getLastInsertID <no-1282>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-1283>`                Oracle uses something like "where rownum <= num".
:ref:`getMainCursorClass <no-1284>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-1285>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-1286>`     Return the basic field structure.
:ref:`getTableRecordCount <no-1287>`         
:ref:`getTables <no-1288>`                   
:ref:`getUpdateTablePrefix <no-1289>`        By default, the update SQL statement will be in the form of
:ref:`getWhereTablePrefix <no-1290>`         By default, the comparisons in the WHERE clauses of
:ref:`getWordMatchFormat <no-1291>`          
:ref:`initEvents <no-1292>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1293>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-1294>`             Returns whether or not the table exists.
:ref:`isValidModule <no-1295>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-1296>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-1297>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-1298>`             Most backends will return a non-zero number if there are updates.
:ref:`pregenPK <no-1299>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-1300>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-1301>`               
:ref:`raiseEvent <no-1302>`                  Send the event to all registered listeners.
:ref:`removeField <no-1303>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-1304>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-1305>`         Roll back (revert) a SQL transaction.
:ref:`setChildFilterClause <no-1306>`        
:ref:`setFieldClause <no-1307>`              
:ref:`setFromClause <no-1308>`               
:ref:`setGroupByClause <no-1309>`            
:ref:`setJoinClause <no-1310>`               
:ref:`setNonUpdateFields <no-1311>`          Normally, this routine should work for all backends. But
:ref:`setOrderByClause <no-1312>`            
:ref:`setProperties <no-1313>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1314>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-1315>`                      
:ref:`setWhereClause <no-1316>`              
:ref:`super <no-1317>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1318>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-1258:

.. function:: dabo.db.dbOracle.Oracle.beginTransaction(self, cursor)

    Begin a SQL transaction.



-------

.. _no-1266:

.. function:: dabo.db.dbOracle.Oracle.escQuote(self, val)



-------

.. _no-1268:

.. function:: dabo.db.dbOracle.Oracle.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)

    Oracle wants the limit clause as where clause. 



-------

.. _no-1270:

.. function:: dabo.db.dbOracle.Oracle.formatDateTime(self, val)

    We need to wrap the value in quotes. 



-------

.. _no-1275:

.. function:: dabo.db.dbOracle.Oracle.getConnection(self, connectInfo, \**kwargs)



-------

.. _no-1279:

.. function:: dabo.db.dbOracle.Oracle.getDictCursorClass(self)



-------

.. _no-1281:

.. function:: dabo.db.dbOracle.Oracle.getFields(self, tableName, cursor)



-------

.. _no-1283:

.. function:: dabo.db.dbOracle.Oracle.getLimitWord(self)

    Oracle uses something like "where rownum <= num". 



-------

.. _no-1287:

.. function:: dabo.db.dbOracle.Oracle.getTableRecordCount(self, tableName, cursor)



-------

.. _no-1288:

.. function:: dabo.db.dbOracle.Oracle.getTables(self, cursor, includeSystemTables=False)



-------

.. _no-1291:

.. function:: dabo.db.dbOracle.Oracle.getWordMatchFormat(self)



-------

.. _no-1301:

.. function:: dabo.db.dbOracle.Oracle.processFields(self, txt)



-------


Methods - inherited
=====================

.. _no-1249:

.. function:: dabo.db.dbOracle.Oracle.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1250:

.. function:: dabo.db.dbOracle.Oracle.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1251:

.. function:: dabo.db.dbOracle.Oracle.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1252:

.. function:: dabo.db.dbOracle.Oracle.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1253:

.. function:: dabo.db.dbOracle.Oracle.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1254:

.. function:: dabo.db.dbOracle.Oracle.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1255:

.. function:: dabo.db.dbOracle.Oracle.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1256:

.. function:: dabo.db.dbOracle.Oracle.autoBindEvents(self, force=True)
   :noindex:


   
   Automatically bind any on*() methods to the associated event.
   
   User code only needs to define the callback, and Dabo will automatically
   set up the event binding. This will satisfy lots of common cases where
   you want an object or its parent to respond to the object's events.
   
   To use this feature, just define a method on<EventName>(), or    if you
   want a parent container to respond to the event, make a method in the
   parent on<EventName>_<object Name or RegID>().
   
   For example::
   
       class MyButton(dabo.ui.dButton):
           def onHit(self, evt):
               print "Hit!"
   
       class MyPanel(dabo.ui.dPanel):
           def afterInit(self):
               self.addObject(MyButton, RegID="btn1")
   
           def onHit_btn1(self, evt):
               print "panel: button hit!"
   
   When the button is pressed, you'll see both 'hit' messages because of
   auto event binding.
   
   If you want to bind your events explicitly, you can turn off auto event
   binding by issuing::
   
        dabo.autoBindEvents = False
   
   This feature is inspired by PythonCard.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1257:

.. function:: dabo.db.dbOracle.Oracle.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1259:

.. function:: dabo.db.dbOracle.Oracle.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1260:

.. function:: dabo.db.dbOracle.Oracle.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1261:

.. function:: dabo.db.dbOracle.Oracle.commitTransaction(self, cursor)
   :noindex:


   Commit a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1262:

.. function:: dabo.db.dbOracle.Oracle.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1263:

.. function:: dabo.db.dbOracle.Oracle.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1264:

.. function:: dabo.db.dbOracle.Oracle.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndex=True)
   :noindex:


   Creates a table and/or indexes based on the dTable passed to it.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1265:

.. function:: dabo.db.dbOracle.Oracle.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1267:

.. function:: dabo.db.dbOracle.Oracle.flush(self, cursor)
   :noindex:


   Only used in some backends


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1269:

.. function:: dabo.db.dbOracle.Oracle.formatBLOB(self, val)
   :noindex:


   
   Properly format a BLOB value to be included in an UPDATE
   or INSERT statement for a specific backend.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1271:

.. function:: dabo.db.dbOracle.Oracle.formatForQuery(self, val, fieldType=None)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1272:

.. function:: dabo.db.dbOracle.Oracle.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1273:

.. function:: dabo.db.dbOracle.Oracle.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1274:

.. function:: dabo.db.dbOracle.Oracle.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1276:

.. function:: dabo.db.dbOracle.Oracle.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1277:

.. function:: dabo.db.dbOracle.Oracle.getDaboFieldType(self, backendFieldType)
   :noindex:


   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1278:

.. function:: dabo.db.dbOracle.Oracle.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1280:

.. function:: dabo.db.dbOracle.Oracle.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1282:

.. function:: dabo.db.dbOracle.Oracle.getLastInsertID(self, cursor)
   :noindex:


   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK
   value, different databases have their own way of retrieving that value.
   This method should be coded in backend-specific subclasses to address
   that database's approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1284:

.. function:: dabo.db.dbOracle.Oracle.getMainCursorClass(self)
   :noindex:


   override in subclasses if they need something other than dCursorMixin


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1285:

.. function:: dabo.db.dbOracle.Oracle.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
   :noindex:


   
   Returns a dictionary of property name/value pairs.
   
   If a sequence of properties is passed, just those property values
   will be returned. Otherwise, all property values will be returned.
   The sequence of properties can be a list, tuple, or plain string
   positional arguments. For instance, all of the following are
   equivilent::
   
       print self.getProperties("Caption", "FontInfo", "Form")
       print self.getProperties(["Caption", "FontInfo", "Form"])
       t = ("Caption", "FontInfo", "Form")
       print self.getProperties(t)
       print self.getProperties(\*t)
   
   An exception will be raised if any passed property names don't
   exist, aren't actual properties, or are not readable (do not have
   getter functions).
   
   However, if an exception is raised from the property getter function,
   the exception will get caught and used as the property value in the
   returned property dictionary. This allows the property list to be
   returned even if some properties can't be evaluated correctly by the
   object yet.
   


Inherited from: :ref:`dabo.lib.propertyHelperMixin.PropertyHelperMixin`

-------

.. _no-1286:

.. function:: dabo.db.dbOracle.Oracle.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1289:

.. function:: dabo.db.dbOracle.Oracle.getUpdateTablePrefix(self, tbl, autoQuote=True)
   :noindex:


   
   By default, the update SQL statement will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in an update statement.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1290:

.. function:: dabo.db.dbOracle.Oracle.getWhereTablePrefix(self, tbl, autoQuote=True)
   :noindex:


   
   By default, the comparisons in the WHERE clauses of
   SQL statements will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in a comparison in the WHERE clause
   of an SQL statement.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1292:

.. function:: dabo.db.dbOracle.Oracle.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1293:

.. function:: dabo.db.dbOracle.Oracle.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1294:

.. function:: dabo.db.dbOracle.Oracle.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1295:

.. function:: dabo.db.dbOracle.Oracle.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1296:

.. function:: dabo.db.dbOracle.Oracle.massageDescription(self, cursor)
   :noindex:


   
   Some dbapi programs do strange things to the description.
   In particular, kinterbasdb forces the field names to upper case
   if the field statement in the SQL that was executed contains an
   'as' expression.
   
   This is called after every execute() by the cursor, since the
   description field is updated each time. By default, we simply
   copy it to the 'descriptionClean' attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1297:

.. function:: dabo.db.dbOracle.Oracle.noResultsOnDelete(self)
   :noindex:


   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1298:

.. function:: dabo.db.dbOracle.Oracle.noResultsOnSave(self)
   :noindex:


   
   Most backends will return a non-zero number if there are updates.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1299:

.. function:: dabo.db.dbOracle.Oracle.pregenPK(self, cursor)
   :noindex:


   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1300:

.. function:: dabo.db.dbOracle.Oracle.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1302:

.. function:: dabo.db.dbOracle.Oracle.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
   :noindex:


   
   Send the event to all registered listeners.
   
   If uiEvent is sent, dEvents.Event will be able to parse it for useful
   information to send along to the callback.
   
   Additional arguments, if any, are sent along to the constructor    of the
   event. While this feature exists so that UI-lib event handlers can pass
   along information (such as the keystroke information in a key event), user
   code may pass along additional arguments as well, which    will exist in the
   event.EventData dictionary property.
   
   In most cases, user code should call raiseEvent() with
   the event class (dEvents.Hit, for example) as the only parameter.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1303:

.. function:: dabo.db.dbOracle.Oracle.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1304:

.. function:: dabo.db.dbOracle.Oracle.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1305:

.. function:: dabo.db.dbOracle.Oracle.rollbackTransaction(self, cursor)
   :noindex:


   Roll back (revert) a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1306:

.. function:: dabo.db.dbOracle.Oracle.setChildFilterClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1307:

.. function:: dabo.db.dbOracle.Oracle.setFieldClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1308:

.. function:: dabo.db.dbOracle.Oracle.setFromClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1309:

.. function:: dabo.db.dbOracle.Oracle.setGroupByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1310:

.. function:: dabo.db.dbOracle.Oracle.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1311:

.. function:: dabo.db.dbOracle.Oracle.setNonUpdateFields(self, cursor, autoQuote=True)
   :noindex:


   
   Normally, this routine should work for all backends. But
   in the case of SQLite, the routine that grabs an empty cursor
   doesn't fill in the description, so that backend has to use
   an alternative approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1312:

.. function:: dabo.db.dbOracle.Oracle.setOrderByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1313:

.. function:: dabo.db.dbOracle.Oracle.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
   :noindex:


   
   Sets a group of properties on the object all at once.
   
   You have the following options for sending the properties:
   
       1) Property/Value pair dictionary
       2) Keyword arguments
       3) Both
   
   The following examples all do the same thing::
   
       self.setProperties(FontBold=True, ForeColor="Red")
       self.setProperties({"FontBold": True, "ForeColor": "Red"})
       self.setProperties({"FontBold": True}, ForeColor="Red")
   
   


Inherited from: :ref:`dabo.lib.propertyHelperMixin.PropertyHelperMixin`

-------

.. _no-1314:

.. function:: dabo.db.dbOracle.Oracle.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
   :noindex:


   
   Sets a group of properties on the object all at once. This
   is different from the regular setProperties() method because
   it only accepts a dict containing prop:value pairs, and it
   assumes that the value is always a string. It will convert
   the value to the correct type for the property, and then set
   the property to that converted value. If the value needs to be evaluated
   in a specific namespace, pass that as the 'context' parameter.
   


Inherited from: :ref:`dabo.lib.propertyHelperMixin.PropertyHelperMixin`

-------

.. _no-1315:

.. function:: dabo.db.dbOracle.Oracle.setSQL(self, sql)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1316:

.. function:: dabo.db.dbOracle.Oracle.setWhereClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1317:

.. function:: dabo.db.dbOracle.Oracle.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1318:

.. function:: dabo.db.dbOracle.Oracle.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------


|
