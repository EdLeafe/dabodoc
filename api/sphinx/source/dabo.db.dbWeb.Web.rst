
.. include:: _static/headings.txt

.. module:: dabo.db.dbWeb

.. _dabo.db.dbWeb.Web:

==================================
|doc_title|  **dbWeb.Web** - class
==================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Web**

.. inheritance-diagram:: Web


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dbSQLite.SQLite`



|API| Class API
===============


.. autoclass:: dabo.db.dbWeb.Web

   .. automethod:: dabo.db.dbWeb.Web.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-2116>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-2117>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-2118>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-2119>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-2120>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-2121>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-2122>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-2123>`              The name of the object.  (str)
:ref:`Parent <no-2124>`            The containing object.  (obj)
:ref:`PreferenceManager <no-2125>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-2116:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2117:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2118:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2119:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2120:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2121:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2122:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2123:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2124:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2125:

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
:ref:`addField <no-2126>`                    Add a field to the field clause.
:ref:`addFrom <no-2127>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-2128>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-2129>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-2130>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-2131>`                    Add an expression to the where clause.
:ref:`afterInit <no-2132>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-2133>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-2134>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-2135>`            Begin a SQL transaction. Since pysqlite does an implicit
:ref:`bindEvent <no-2136>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-2137>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-2138>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-2139>`           
:ref:`createJustTable <no-2140>`             
:ref:`createTableAndIndexes <no-2141>`       
:ref:`encloseNames <no-2142>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-2143>`                    
:ref:`flush <no-2144>`                       
:ref:`formSQL <no-2145>`                     Creates the appropriate SQL for the backend, given all
:ref:`formatBLOB <no-2146>`                  
:ref:`formatDateTime <no-2147>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-2148>`              
:ref:`formatJoinType <no-2149>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-2150>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-2151>`             Return the fully qualified name of the object.
:ref:`getConnection <no-2152>`               
:ref:`getCursor <no-2153>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-2154>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-2155>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-2156>`          
:ref:`getFieldInfoFromDescription <no-2157>` Return field information from the cursor description.
:ref:`getFields <no-2158>`                   
:ref:`getLastInsertID <no-2159>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-2160>`                Return the word to use in the db-specific limit clause.
:ref:`getMainCursorClass <no-2161>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-2162>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-2163>`     Return the basic field structure.
:ref:`getTableRecordCount <no-2164>`         
:ref:`getTables <no-2165>`                   
:ref:`getUpdateTablePrefix <no-2166>`        Table name prefixes are not allowed.
:ref:`getWhereTablePrefix <no-2167>`         Table name prefixes are not allowed.
:ref:`getWordMatchFormat <no-2168>`          By default, will return the standard format for an
:ref:`initEvents <no-2169>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-2170>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-2171>`             Returns whether or not the table exists.
:ref:`isValidModule <no-2172>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-2173>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-2174>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-2175>`             SQLite does not return anything on a successful update
:ref:`pregenPK <no-2176>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-2177>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-2178>`               Default is to return the string unchanged. Override
:ref:`raiseEvent <no-2179>`                  Send the event to all registered listeners.
:ref:`removeField <no-2180>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-2181>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-2182>`         Rollback a SQL transaction.
:ref:`setChildFilterClause <no-2183>`        
:ref:`setFieldClause <no-2184>`              
:ref:`setFromClause <no-2185>`               
:ref:`setGroupByClause <no-2186>`            
:ref:`setJoinClause <no-2187>`               
:ref:`setNonUpdateFields <no-2188>`          
:ref:`setOrderByClause <no-2189>`            
:ref:`setProperties <no-2190>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-2191>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-2192>`                      
:ref:`setWhereClause <no-2193>`              
:ref:`super <no-2194>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-2195>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-2152:

.. function:: dabo.db.dbWeb.Web.getConnection(self, connectInfo, \**kwargs)



-------

.. _no-2158:

.. function:: dabo.db.dbWeb.Web.getFields(self, tableName, crs=None)



-------

.. _no-2164:

.. function:: dabo.db.dbWeb.Web.getTableRecordCount(self, tableName)



-------

.. _no-2165:

.. function:: dabo.db.dbWeb.Web.getTables(self, cursor, includeSystemTables=False)



-------


Methods - inherited
=====================

.. _no-2126:

.. function:: dabo.db.dbWeb.Web.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2127:

.. function:: dabo.db.dbWeb.Web.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2128:

.. function:: dabo.db.dbWeb.Web.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2129:

.. function:: dabo.db.dbWeb.Web.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2130:

.. function:: dabo.db.dbWeb.Web.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2131:

.. function:: dabo.db.dbWeb.Web.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2132:

.. function:: dabo.db.dbWeb.Web.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2133:

.. function:: dabo.db.dbWeb.Web.autoBindEvents(self, force=True)
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

.. _no-2134:

.. function:: dabo.db.dbWeb.Web.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2135:

.. function:: dabo.db.dbWeb.Web.beginTransaction(self, cursor)
   :noindex:


   
   Begin a SQL transaction. Since pysqlite does an implicit
   'begin' all the time, simply do nothing.
   


Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2136:

.. function:: dabo.db.dbWeb.Web.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2137:

.. function:: dabo.db.dbWeb.Web.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2138:

.. function:: dabo.db.dbWeb.Web.commitTransaction(self, cursor)
   :noindex:


   Commit a SQL transaction.


Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2139:

.. function:: dabo.db.dbWeb.Web.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2140:

.. function:: dabo.db.dbWeb.Web.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2141:

.. function:: dabo.db.dbWeb.Web.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndexes=True)
   :noindex:



Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2142:

.. function:: dabo.db.dbWeb.Web.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2143:

.. function:: dabo.db.dbWeb.Web.escQuote(self, val)
   :noindex:



Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2144:

.. function:: dabo.db.dbWeb.Web.flush(self, crs)
   :noindex:



Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2145:

.. function:: dabo.db.dbWeb.Web.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)
   :noindex:


   
   Creates the appropriate SQL for the backend, given all
   the required clauses. Some backends order these differently, so
   they should override this method with their own ordering.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2146:

.. function:: dabo.db.dbWeb.Web.formatBLOB(self, val)
   :noindex:



Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2147:

.. function:: dabo.db.dbWeb.Web.formatDateTime(self, val)
   :noindex:


   We need to wrap the value in quotes.


Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2148:

.. function:: dabo.db.dbWeb.Web.formatForQuery(self, val, fieldType=None)
   :noindex:



Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2149:

.. function:: dabo.db.dbWeb.Web.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2150:

.. function:: dabo.db.dbWeb.Web.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2151:

.. function:: dabo.db.dbWeb.Web.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2153:

.. function:: dabo.db.dbWeb.Web.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2154:

.. function:: dabo.db.dbWeb.Web.getDaboFieldType(self, backendFieldType)
   :noindex:


   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2155:

.. function:: dabo.db.dbWeb.Web.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2156:

.. function:: dabo.db.dbWeb.Web.getDictCursorClass(self)
   :noindex:



Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2157:

.. function:: dabo.db.dbWeb.Web.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2159:

.. function:: dabo.db.dbWeb.Web.getLastInsertID(self, cursor)
   :noindex:


   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK
   value, different databases have their own way of retrieving that value.
   This method should be coded in backend-specific subclasses to address
   that database's approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2160:

.. function:: dabo.db.dbWeb.Web.getLimitWord(self)
   :noindex:


   
   Return the word to use in the db-specific limit clause.
   Override for backends that don't use the word 'limit'
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2161:

.. function:: dabo.db.dbWeb.Web.getMainCursorClass(self)
   :noindex:


   override in subclasses if they need something other than dCursorMixin


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2162:

.. function:: dabo.db.dbWeb.Web.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-2163:

.. function:: dabo.db.dbWeb.Web.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2166:

.. function:: dabo.db.dbWeb.Web.getUpdateTablePrefix(self, table, autoQuote=True)
   :noindex:


   Table name prefixes are not allowed.


Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2167:

.. function:: dabo.db.dbWeb.Web.getWhereTablePrefix(self, table, autoQuote=True)
   :noindex:


   Table name prefixes are not allowed.


Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2168:

.. function:: dabo.db.dbWeb.Web.getWordMatchFormat(self)
   :noindex:


   
   By default, will return the standard format for an
   equality test. If search by words is available, the format
   must be implemented in each specific backend.
   
   The format must have the expressions %(table)s, %(field)s,
   and %(value)s, which will be replaced with the table, field,
   and value strings, respectively.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2169:

.. function:: dabo.db.dbWeb.Web.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2170:

.. function:: dabo.db.dbWeb.Web.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2171:

.. function:: dabo.db.dbWeb.Web.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2172:

.. function:: dabo.db.dbWeb.Web.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2173:

.. function:: dabo.db.dbWeb.Web.massageDescription(self, cursor)
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

.. _no-2174:

.. function:: dabo.db.dbWeb.Web.noResultsOnDelete(self)
   :noindex:


   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2175:

.. function:: dabo.db.dbWeb.Web.noResultsOnSave(self)
   :noindex:


   SQLite does not return anything on a successful update


Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2176:

.. function:: dabo.db.dbWeb.Web.pregenPK(self, cursor)
   :noindex:


   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2177:

.. function:: dabo.db.dbWeb.Web.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2178:

.. function:: dabo.db.dbWeb.Web.processFields(self, txt)
   :noindex:


   
   Default is to return the string unchanged. Override
   in cases where the str needs processing.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2179:

.. function:: dabo.db.dbWeb.Web.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-2180:

.. function:: dabo.db.dbWeb.Web.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2181:

.. function:: dabo.db.dbWeb.Web.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2182:

.. function:: dabo.db.dbWeb.Web.rollbackTransaction(self, cursor)
   :noindex:


   Rollback a SQL transaction.


Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2183:

.. function:: dabo.db.dbWeb.Web.setChildFilterClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2184:

.. function:: dabo.db.dbWeb.Web.setFieldClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2185:

.. function:: dabo.db.dbWeb.Web.setFromClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2186:

.. function:: dabo.db.dbWeb.Web.setGroupByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2187:

.. function:: dabo.db.dbWeb.Web.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2188:

.. function:: dabo.db.dbWeb.Web.setNonUpdateFields(self, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dbSQLite.SQLite`

-------

.. _no-2189:

.. function:: dabo.db.dbWeb.Web.setOrderByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2190:

.. function:: dabo.db.dbWeb.Web.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-2191:

.. function:: dabo.db.dbWeb.Web.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-2192:

.. function:: dabo.db.dbWeb.Web.setSQL(self, sql)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2193:

.. function:: dabo.db.dbWeb.Web.setWhereClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2194:

.. function:: dabo.db.dbWeb.Web.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2195:

.. function:: dabo.db.dbWeb.Web.unbindEvent(self, eventClass=None, function=None)
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
