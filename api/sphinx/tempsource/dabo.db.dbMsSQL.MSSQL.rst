
.. include:: _static/headings.txt

.. module:: dabo.db.dbMsSQL

.. _dabo.db.dbMsSQL.MSSQL:

======================================
|doc_title|  **dbMsSQL.MSSQL** - class
======================================

Class providing Microsoft SQL Server connectivity. Uses pymssql.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **MSSQL**

.. inheritance-diagram:: MSSQL


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dBackend.dBackend`



|API| Class API
===============


.. autoclass:: dabo.db.dbMsSQL.MSSQL

   .. automethod:: dabo.db.dbMsSQL.MSSQL.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1079>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1080>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1081>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1082>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-1083>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-1084>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-1085>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1086>`              The name of the object.  (str)
:ref:`Parent <no-1087>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1088>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-1079:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1080:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1081:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1082:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1083:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1084:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1085:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1086:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1087:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1088:

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
:ref:`addField <no-1089>`                    Add a field to the field clause.
:ref:`addFrom <no-1090>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-1091>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-1092>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-1093>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-1094>`                    Add an expression to the where clause.
:ref:`afterInit <no-1095>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1096>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1097>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-1098>`            
:ref:`bindEvent <no-1099>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-1100>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-1101>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-1102>`           
:ref:`createJustTable <no-1103>`             
:ref:`createTableAndIndexes <no-1104>`       Creates a table and/or indexes based on the dTable passed to it.
:ref:`encloseNames <no-1105>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-1106>`                    
:ref:`flush <no-1107>`                       
:ref:`formSQL <no-1108>`                     MS SQL wants the limit clause before the field clause.
:ref:`formatBLOB <no-1109>`                  Properly format a BLOB value to be included in an UPDATE
:ref:`formatDateTime <no-1110>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-1111>`              
:ref:`formatJoinType <no-1112>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-1113>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-1114>`             Return the fully qualified name of the object.
:ref:`getConnection <no-1115>`               The pymssql module requires the connection be created for the FreeTDS libraries first.
:ref:`getCursor <no-1116>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-1117>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-1118>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-1119>`          Since there are two versions of driver package we support both,
:ref:`getFieldInfoFromDescription <no-1120>` Return field information from the cursor description.
:ref:`getFields <no-1121>`                   Returns the list of fields of the passed table
:ref:`getLastInsertID <no-1122>`             Pymssql does not populate the 'lastrowid' attribute of the cursor, so we
:ref:`getLimitWord <no-1123>`                
:ref:`getMainCursorClass <no-1124>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-1125>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-1126>`     Return the basic field structure.
:ref:`getTableRecordCount <no-1127>`         
:ref:`getTables <no-1128>`                   
:ref:`getUpdateTablePrefix <no-1129>`        By default, the update SQL statement will be in the form of
:ref:`getWhereTablePrefix <no-1130>`         By default, the comparisons in the WHERE clauses of
:ref:`getWordMatchFormat <no-1131>`          By default, will return the standard format for an
:ref:`initEvents <no-1132>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1133>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-1134>`             Returns whether or not the table exists.
:ref:`isValidModule <no-1135>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-1136>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-1137>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-1138>`             Most backends will return a non-zero number if there are updates.
:ref:`pregenPK <no-1139>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-1140>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-1141>`               Default is to return the string unchanged. Override
:ref:`raiseEvent <no-1142>`                  Send the event to all registered listeners.
:ref:`removeField <no-1143>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-1144>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-1145>`         Roll back (revert) a SQL transaction.
:ref:`setChildFilterClause <no-1146>`        
:ref:`setFieldClause <no-1147>`              
:ref:`setFromClause <no-1148>`               
:ref:`setGroupByClause <no-1149>`            
:ref:`setJoinClause <no-1150>`               
:ref:`setNonUpdateFields <no-1151>`          Normally, this routine should work for all backends. But
:ref:`setOrderByClause <no-1152>`            
:ref:`setProperties <no-1153>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1154>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-1155>`                      
:ref:`setWhereClause <no-1156>`              
:ref:`super <no-1157>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1158>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-1098:

.. function:: dabo.db.dbMsSQL.MSSQL.beginTransaction(self, cursor)



-------

.. _no-1106:

.. function:: dabo.db.dbMsSQL.MSSQL.escQuote(self, val)



-------

.. _no-1107:

.. function:: dabo.db.dbMsSQL.MSSQL.flush(self, cursor)



-------

.. _no-1108:

.. function:: dabo.db.dbMsSQL.MSSQL.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)

   MS SQL wants the limit clause before the field clause.



-------

.. _no-1110:

.. function:: dabo.db.dbMsSQL.MSSQL.formatDateTime(self, val)

   We need to wrap the value in quotes.



-------

.. _no-1115:

.. function:: dabo.db.dbMsSQL.MSSQL.getConnection(self, connectInfo, forceCreate=False, \**kwargs)

   
   The pymssql module requires the connection be created for the FreeTDS libraries first.
   Therefore, the DSN is really the name of the connection for FreeTDS :
     __init__(self, dsn, user, passwd, database = None, strip = 0)
   



-------

.. _no-1119:

.. function:: dabo.db.dbMsSQL.MSSQL.getDictCursorClass(self)

   Since there are two versions of driver package we support both,
   deprecated and new one.
   



-------

.. _no-1121:

.. function:: dabo.db.dbMsSQL.MSSQL.getFields(self, tableName, cursor)

   
   Returns the list of fields of the passed table
   field: ( fieldname, dabo data type, key )
   



-------

.. _no-1122:

.. function:: dabo.db.dbMsSQL.MSSQL.getLastInsertID(self, cursor)

   
   Pymssql does not populate the 'lastrowid' attribute of the cursor, so we
   need to get the newly-inserted PK ourselves.
   



-------

.. _no-1123:

.. function:: dabo.db.dbMsSQL.MSSQL.getLimitWord(self)



-------

.. _no-1127:

.. function:: dabo.db.dbMsSQL.MSSQL.getTableRecordCount(self, tableName, cursor)



-------

.. _no-1128:

.. function:: dabo.db.dbMsSQL.MSSQL.getTables(self, cursor, includeSystemTables=False)



-------

.. _no-1137:

.. function:: dabo.db.dbMsSQL.MSSQL.noResultsOnDelete(self)

   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   



-------

.. _no-1138:

.. function:: dabo.db.dbMsSQL.MSSQL.noResultsOnSave(self)

   
   Most backends will return a non-zero number if there are updates.
   Some do not, so this will have to be customized in those cases.
   



-------


Methods - inherited
=====================

.. _no-1089:

.. function:: dabo.db.dbMsSQL.MSSQL.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1090:

.. function:: dabo.db.dbMsSQL.MSSQL.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1091:

.. function:: dabo.db.dbMsSQL.MSSQL.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1092:

.. function:: dabo.db.dbMsSQL.MSSQL.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1093:

.. function:: dabo.db.dbMsSQL.MSSQL.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1094:

.. function:: dabo.db.dbMsSQL.MSSQL.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1095:

.. function:: dabo.db.dbMsSQL.MSSQL.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1096:

.. function:: dabo.db.dbMsSQL.MSSQL.autoBindEvents(self, force=True)
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

.. _no-1097:

.. function:: dabo.db.dbMsSQL.MSSQL.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1099:

.. function:: dabo.db.dbMsSQL.MSSQL.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1100:

.. function:: dabo.db.dbMsSQL.MSSQL.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1101:

.. function:: dabo.db.dbMsSQL.MSSQL.commitTransaction(self, cursor)
   :noindex:


   Commit a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1102:

.. function:: dabo.db.dbMsSQL.MSSQL.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1103:

.. function:: dabo.db.dbMsSQL.MSSQL.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1104:

.. function:: dabo.db.dbMsSQL.MSSQL.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndex=True)
   :noindex:


   Creates a table and/or indexes based on the dTable passed to it.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1105:

.. function:: dabo.db.dbMsSQL.MSSQL.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1109:

.. function:: dabo.db.dbMsSQL.MSSQL.formatBLOB(self, val)
   :noindex:


   
   Properly format a BLOB value to be included in an UPDATE
   or INSERT statement for a specific backend.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1111:

.. function:: dabo.db.dbMsSQL.MSSQL.formatForQuery(self, val, fieldType=None)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1112:

.. function:: dabo.db.dbMsSQL.MSSQL.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1113:

.. function:: dabo.db.dbMsSQL.MSSQL.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1114:

.. function:: dabo.db.dbMsSQL.MSSQL.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1116:

.. function:: dabo.db.dbMsSQL.MSSQL.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1117:

.. function:: dabo.db.dbMsSQL.MSSQL.getDaboFieldType(self, backendFieldType)
   :noindex:


   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1118:

.. function:: dabo.db.dbMsSQL.MSSQL.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1120:

.. function:: dabo.db.dbMsSQL.MSSQL.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1124:

.. function:: dabo.db.dbMsSQL.MSSQL.getMainCursorClass(self)
   :noindex:


   override in subclasses if they need something other than dCursorMixin


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1125:

.. function:: dabo.db.dbMsSQL.MSSQL.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1126:

.. function:: dabo.db.dbMsSQL.MSSQL.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1129:

.. function:: dabo.db.dbMsSQL.MSSQL.getUpdateTablePrefix(self, tbl, autoQuote=True)
   :noindex:


   
   By default, the update SQL statement will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in an update statement.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1130:

.. function:: dabo.db.dbMsSQL.MSSQL.getWhereTablePrefix(self, tbl, autoQuote=True)
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

.. _no-1131:

.. function:: dabo.db.dbMsSQL.MSSQL.getWordMatchFormat(self)
   :noindex:


   
   By default, will return the standard format for an
   equality test. If search by words is available, the format
   must be implemented in each specific backend.
   
   The format must have the expressions %(table)s, %(field)s,
   and %(value)s, which will be replaced with the table, field,
   and value strings, respectively.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1132:

.. function:: dabo.db.dbMsSQL.MSSQL.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1133:

.. function:: dabo.db.dbMsSQL.MSSQL.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1134:

.. function:: dabo.db.dbMsSQL.MSSQL.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1135:

.. function:: dabo.db.dbMsSQL.MSSQL.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1136:

.. function:: dabo.db.dbMsSQL.MSSQL.massageDescription(self, cursor)
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

.. _no-1139:

.. function:: dabo.db.dbMsSQL.MSSQL.pregenPK(self, cursor)
   :noindex:


   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1140:

.. function:: dabo.db.dbMsSQL.MSSQL.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1141:

.. function:: dabo.db.dbMsSQL.MSSQL.processFields(self, txt)
   :noindex:


   
   Default is to return the string unchanged. Override
   in cases where the str needs processing.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1142:

.. function:: dabo.db.dbMsSQL.MSSQL.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1143:

.. function:: dabo.db.dbMsSQL.MSSQL.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1144:

.. function:: dabo.db.dbMsSQL.MSSQL.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1145:

.. function:: dabo.db.dbMsSQL.MSSQL.rollbackTransaction(self, cursor)
   :noindex:


   Roll back (revert) a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1146:

.. function:: dabo.db.dbMsSQL.MSSQL.setChildFilterClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1147:

.. function:: dabo.db.dbMsSQL.MSSQL.setFieldClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1148:

.. function:: dabo.db.dbMsSQL.MSSQL.setFromClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1149:

.. function:: dabo.db.dbMsSQL.MSSQL.setGroupByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1150:

.. function:: dabo.db.dbMsSQL.MSSQL.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1151:

.. function:: dabo.db.dbMsSQL.MSSQL.setNonUpdateFields(self, cursor, autoQuote=True)
   :noindex:


   
   Normally, this routine should work for all backends. But
   in the case of SQLite, the routine that grabs an empty cursor
   doesn't fill in the description, so that backend has to use
   an alternative approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1152:

.. function:: dabo.db.dbMsSQL.MSSQL.setOrderByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1153:

.. function:: dabo.db.dbMsSQL.MSSQL.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1154:

.. function:: dabo.db.dbMsSQL.MSSQL.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1155:

.. function:: dabo.db.dbMsSQL.MSSQL.setSQL(self, sql)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1156:

.. function:: dabo.db.dbMsSQL.MSSQL.setWhereClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1157:

.. function:: dabo.db.dbMsSQL.MSSQL.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1158:

.. function:: dabo.db.dbMsSQL.MSSQL.unbindEvent(self, eventClass=None, function=None)
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
