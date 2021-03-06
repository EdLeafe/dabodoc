
.. include:: _static/headings.txt

.. module:: dabo.db.dBackend

.. _dabo.db.dBackend.dBackend:

==========================================
|doc_title|  **dBackend.dBackend** - class
==========================================

Abstract class inherited by the specific Dabo database connectors.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBackend**

.. inheritance-diagram:: dBackend


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.db.dbMsSQL.MSSQL`
* :ref:`dabo.db.dbSQLite.SQLite`



|API| Class API
===============


.. autoclass:: dabo.db.dBackend.dBackend

   .. automethod:: dabo.db.dBackend.dBackend.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1159>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1160>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1161>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1162>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-1163>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-1164>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-1165>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1166>`              The name of the object.  (str)
:ref:`Parent <no-1167>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1168>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties
==========

.. _no-1163:

**Encoding** 

Backend encoding  (str)



-------

.. _no-1164:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    



-------


Properties - inherited
========================

.. _no-1159:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1160:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1161:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1162:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1165:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1166:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1167:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1168:

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
:ref:`addField <no-1169>`                    Add a field to the field clause.
:ref:`addFrom <no-1170>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-1171>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-1172>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-1173>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-1174>`                    Add an expression to the where clause.
:ref:`afterInit <no-1175>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1176>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1177>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-1178>`            Begin a SQL transaction. Override in subclasses if needed.
:ref:`bindEvent <no-1179>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-1180>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-1181>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-1182>`           
:ref:`createJustTable <no-1183>`             
:ref:`createTableAndIndexes <no-1184>`       Creates a table and/or indexes based on the dTable passed to it.
:ref:`encloseNames <no-1185>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-1186>`                    Escape special characters in SQL strings.
:ref:`flush <no-1187>`                       Only used in some backends
:ref:`formSQL <no-1188>`                     Creates the appropriate SQL for the backend, given all
:ref:`formatBLOB <no-1189>`                  Properly format a BLOB value to be included in an UPDATE
:ref:`formatDateTime <no-1190>`              Properly format a datetime value to be included in an UPDATE
:ref:`formatForQuery <no-1191>`              
:ref:`formatJoinType <no-1192>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-1193>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-1194>`             Return the fully qualified name of the object.
:ref:`getConnection <no-1195>`               override in subclasses
:ref:`getCursor <no-1196>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-1197>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-1198>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-1199>`          override in subclasses
:ref:`getFieldInfoFromDescription <no-1200>` Return field information from the cursor description.
:ref:`getFields <no-1201>`                   Return field information from the backend table.
:ref:`getLastInsertID <no-1202>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-1203>`                Return the word to use in the db-specific limit clause.
:ref:`getMainCursorClass <no-1204>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-1205>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-1206>`     Return the basic field structure.
:ref:`getTableRecordCount <no-1207>`         Return the number of records in the backend table.
:ref:`getTables <no-1208>`                   Return a tuple of the tables in the current database.
:ref:`getUpdateTablePrefix <no-1209>`        By default, the update SQL statement will be in the form of
:ref:`getWhereTablePrefix <no-1210>`         By default, the comparisons in the WHERE clauses of
:ref:`getWordMatchFormat <no-1211>`          By default, will return the standard format for an
:ref:`initEvents <no-1212>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1213>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-1214>`             Returns whether or not the table exists.
:ref:`isValidModule <no-1215>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-1216>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-1217>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-1218>`             Most backends will return a non-zero number if there are updates.
:ref:`pregenPK <no-1219>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-1220>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-1221>`               Default is to return the string unchanged. Override
:ref:`raiseEvent <no-1222>`                  Send the event to all registered listeners.
:ref:`removeField <no-1223>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-1224>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-1225>`         Roll back (revert) a SQL transaction.
:ref:`setChildFilterClause <no-1226>`        
:ref:`setFieldClause <no-1227>`              
:ref:`setFromClause <no-1228>`               
:ref:`setGroupByClause <no-1229>`            
:ref:`setJoinClause <no-1230>`               
:ref:`setNonUpdateFields <no-1231>`          Normally, this routine should work for all backends. But
:ref:`setOrderByClause <no-1232>`            
:ref:`setProperties <no-1233>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1234>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-1235>`                      
:ref:`setWhereClause <no-1236>`              
:ref:`super <no-1237>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1238>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-1169:

.. function:: dabo.db.dBackend.dBackend.addField(self, clause, exp, alias=None, autoQuote=True)

   Add a field to the field clause.



-------

.. _no-1170:

.. function:: dabo.db.dBackend.dBackend.addFrom(self, clause, exp, alias=None, autoQuote=True)

   Add a table to the sql statement.



-------

.. _no-1171:

.. function:: dabo.db.dBackend.dBackend.addGroupBy(self, clause, exp, autoQuote=True)

   Add an expression to the group-by clause.



-------

.. _no-1172:

.. function:: dabo.db.dBackend.dBackend.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)

   Add a joined table to the sql statement.



-------

.. _no-1173:

.. function:: dabo.db.dBackend.dBackend.addOrderBy(self, clause, exp, autoQuote=True)

   Add an expression to the order-by clause.



-------

.. _no-1174:

.. function:: dabo.db.dBackend.dBackend.addWhere(self, clause, exp, comp='and', autoQuote=True)

   Add an expression to the where clause.



-------

.. _no-1178:

.. function:: dabo.db.dBackend.dBackend.beginTransaction(self, cursor)

   Begin a SQL transaction. Override in subclasses if needed.



-------

.. _no-1181:

.. function:: dabo.db.dBackend.dBackend.commitTransaction(self, cursor)

   Commit a SQL transaction.



-------

.. _no-1182:

.. function:: dabo.db.dBackend.dBackend.createJustIndexes(self, tabledef, cursor)



-------

.. _no-1183:

.. function:: dabo.db.dBackend.dBackend.createJustTable(self, tabledef, cursor)



-------

.. _no-1184:

.. function:: dabo.db.dBackend.dBackend.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndex=True)

   Creates a table and/or indexes based on the dTable passed to it.



-------

.. _no-1185:

.. function:: dabo.db.dBackend.dBackend.encloseNames(self, exp, autoQuote=True, keywords=None)

   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   



-------

.. _no-1186:

.. function:: dabo.db.dBackend.dBackend.escQuote(self, val)

   
   Escape special characters in SQL strings.
   
   Escapes any single quotes that could cause SQL syntax errors, as well
   as any other characters which have special meanings with the backend
   database's engine.
   



-------

.. _no-1187:

.. function:: dabo.db.dBackend.dBackend.flush(self, cursor)

   Only used in some backends



-------

.. _no-1188:

.. function:: dabo.db.dBackend.dBackend.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)

   
   Creates the appropriate SQL for the backend, given all
   the required clauses. Some backends order these differently, so
   they should override this method with their own ordering.
   



-------

.. _no-1189:

.. function:: dabo.db.dBackend.dBackend.formatBLOB(self, val)

   
   Properly format a BLOB value to be included in an UPDATE
   or INSERT statement for a specific backend.
   



-------

.. _no-1190:

.. function:: dabo.db.dBackend.dBackend.formatDateTime(self, val)

   
   Properly format a datetime value to be included in an UPDATE
   or INSERT statement. Each backend can have different requirements
   for formatting dates, so this is where you encapsulate these rules
   in backend-specific subclasses. If nothing special needs to be done,
   the default is to return the original value.
   



-------

.. _no-1191:

.. function:: dabo.db.dBackend.dBackend.formatForQuery(self, val, fieldType=None)



-------

.. _no-1192:

.. function:: dabo.db.dBackend.dBackend.formatJoinType(self, jt)

   Default formatting for jointype keywords. Override in subclasses if needed.



-------

.. _no-1193:

.. function:: dabo.db.dBackend.dBackend.formatNone(self)

   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   



-------

.. _no-1195:

.. function:: dabo.db.dBackend.dBackend.getConnection(self, connectInfo, \**kwargs)

   override in subclasses



-------

.. _no-1196:

.. function:: dabo.db.dBackend.dBackend.getCursor(self, cursorClass)

   override in subclasses if necessary



-------

.. _no-1197:

.. function:: dabo.db.dBackend.dBackend.getDaboFieldType(self, backendFieldType)

   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   



-------

.. _no-1198:

.. function:: dabo.db.dBackend.dBackend.getDescription(self, cursor)

   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   



-------

.. _no-1199:

.. function:: dabo.db.dBackend.dBackend.getDictCursorClass(self)

   override in subclasses



-------

.. _no-1200:

.. function:: dabo.db.dBackend.dBackend.getFieldInfoFromDescription(self, cursorDescription)

   Return field information from the cursor description.



-------

.. _no-1201:

.. function:: dabo.db.dBackend.dBackend.getFields(self, tableName, cursor)

   
   Return field information from the backend table.
   
   See dCursorMixin.getFields() for a description of the return value.
   



-------

.. _no-1202:

.. function:: dabo.db.dBackend.dBackend.getLastInsertID(self, cursor)

   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK
   value, different databases have their own way of retrieving that value.
   This method should be coded in backend-specific subclasses to address
   that database's approach.
   



-------

.. _no-1203:

.. function:: dabo.db.dBackend.dBackend.getLimitWord(self)

   
   Return the word to use in the db-specific limit clause.
   Override for backends that don't use the word 'limit'
   



-------

.. _no-1204:

.. function:: dabo.db.dBackend.dBackend.getMainCursorClass(self)

   override in subclasses if they need something other than dCursorMixin



-------

.. _no-1206:

.. function:: dabo.db.dBackend.dBackend.getStructureDescription(self, cursor)

   Return the basic field structure.



-------

.. _no-1207:

.. function:: dabo.db.dBackend.dBackend.getTableRecordCount(self, tableName, cursor)

   Return the number of records in the backend table.



-------

.. _no-1208:

.. function:: dabo.db.dBackend.dBackend.getTables(self, cursor, includeSystemTables=False)

   
   Return a tuple of the tables in the current database.
   
   Different backends will do this differently, so override in subclasses.
   



-------

.. _no-1209:

.. function:: dabo.db.dBackend.dBackend.getUpdateTablePrefix(self, tbl, autoQuote=True)

   
   By default, the update SQL statement will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in an update statement.
   



-------

.. _no-1210:

.. function:: dabo.db.dBackend.dBackend.getWhereTablePrefix(self, tbl, autoQuote=True)

   
   By default, the comparisons in the WHERE clauses of
   SQL statements will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in a comparison in the WHERE clause
   of an SQL statement.
   



-------

.. _no-1211:

.. function:: dabo.db.dBackend.dBackend.getWordMatchFormat(self)

   
   By default, will return the standard format for an
   equality test. If search by words is available, the format
   must be implemented in each specific backend.
   
   The format must have the expressions %(table)s, %(field)s,
   and %(value)s, which will be replaced with the table, field,
   and value strings, respectively.
   



-------

.. _no-1214:

.. function:: dabo.db.dBackend.dBackend.isExistingTable(self, table)

   Returns whether or not the table exists.



-------

.. _no-1215:

.. function:: dabo.db.dBackend.dBackend.isValidModule(self)

   Test the dbapi to see if it is supported on this computer.



-------

.. _no-1216:

.. function:: dabo.db.dBackend.dBackend.massageDescription(self, cursor)

   
   Some dbapi programs do strange things to the description.
   In particular, kinterbasdb forces the field names to upper case
   if the field statement in the SQL that was executed contains an
   'as' expression.
   
   This is called after every execute() by the cursor, since the
   description field is updated each time. By default, we simply
   copy it to the 'descriptionClean' attribute.
   



-------

.. _no-1217:

.. function:: dabo.db.dBackend.dBackend.noResultsOnDelete(self)

   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   



-------

.. _no-1218:

.. function:: dabo.db.dBackend.dBackend.noResultsOnSave(self)

   
   Most backends will return a non-zero number if there are updates.
   Some do not, so this will have to be customized in those cases.
   



-------

.. _no-1219:

.. function:: dabo.db.dBackend.dBackend.pregenPK(self, cursor)

   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   



-------

.. _no-1220:

.. function:: dabo.db.dBackend.dBackend.prepareWhere(self, clause, autoQuote=True)

   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   



-------

.. _no-1221:

.. function:: dabo.db.dBackend.dBackend.processFields(self, txt)

   
   Default is to return the string unchanged. Override
   in cases where the str needs processing.
   



-------

.. _no-1223:

.. function:: dabo.db.dBackend.dBackend.removeField(self, clause, exp, alias=None, autoQuote=True)

   Remove a previously added field from the field clause.



-------

.. _no-1224:

.. function:: dabo.db.dBackend.dBackend.removeWhere(self, clause, exp, comp='and', autoQuote=True)

   Remove a previously-added expression from the where clause.



-------

.. _no-1225:

.. function:: dabo.db.dBackend.dBackend.rollbackTransaction(self, cursor)

   Roll back (revert) a SQL transaction.



-------

.. _no-1226:

.. function:: dabo.db.dBackend.dBackend.setChildFilterClause(self, clause, autoQuote=True)



-------

.. _no-1227:

.. function:: dabo.db.dBackend.dBackend.setFieldClause(self, clause, autoQuote=True)



-------

.. _no-1228:

.. function:: dabo.db.dBackend.dBackend.setFromClause(self, clause, autoQuote=True)



-------

.. _no-1229:

.. function:: dabo.db.dBackend.dBackend.setGroupByClause(self, clause, autoQuote=True)



-------

.. _no-1230:

.. function:: dabo.db.dBackend.dBackend.setJoinClause(self, clause, autoQuote=True)



-------

.. _no-1231:

.. function:: dabo.db.dBackend.dBackend.setNonUpdateFields(self, cursor, autoQuote=True)

   
   Normally, this routine should work for all backends. But
   in the case of SQLite, the routine that grabs an empty cursor
   doesn't fill in the description, so that backend has to use
   an alternative approach.
   



-------

.. _no-1232:

.. function:: dabo.db.dBackend.dBackend.setOrderByClause(self, clause, autoQuote=True)



-------

.. _no-1235:

.. function:: dabo.db.dBackend.dBackend.setSQL(self, sql)



-------

.. _no-1236:

.. function:: dabo.db.dBackend.dBackend.setWhereClause(self, clause, autoQuote=True)



-------


Methods - inherited
=====================

.. _no-1175:

.. function:: dabo.db.dBackend.dBackend.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1176:

.. function:: dabo.db.dBackend.dBackend.autoBindEvents(self, force=True)
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

.. _no-1177:

.. function:: dabo.db.dBackend.dBackend.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1179:

.. function:: dabo.db.dBackend.dBackend.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1180:

.. function:: dabo.db.dBackend.dBackend.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1194:

.. function:: dabo.db.dBackend.dBackend.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1205:

.. function:: dabo.db.dBackend.dBackend.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1212:

.. function:: dabo.db.dBackend.dBackend.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1213:

.. function:: dabo.db.dBackend.dBackend.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1222:

.. function:: dabo.db.dBackend.dBackend.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1233:

.. function:: dabo.db.dBackend.dBackend.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1234:

.. function:: dabo.db.dBackend.dBackend.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1237:

.. function:: dabo.db.dBackend.dBackend.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1238:

.. function:: dabo.db.dBackend.dBackend.unbindEvent(self, eventClass=None, function=None)
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
