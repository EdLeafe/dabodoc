
.. include:: _static/headings.txt

.. module:: dabo.db.dbFirebird

.. _dabo.db.dbFirebird.Firebird:

============================================
|doc_title|  **dbFirebird.Firebird** - class
============================================

Class providing Firebird connectivity. Uses kinterbasdb.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Firebird**

.. inheritance-diagram:: Firebird


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dBackend.dBackend`



|API| Class API
===============


.. autoclass:: dabo.db.dbFirebird.Firebird

   .. automethod:: dabo.db.dbFirebird.Firebird.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-2035>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-2036>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-2037>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-2038>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-2039>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-2040>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-2041>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-2042>`              The name of the object.  (str)
:ref:`Parent <no-2043>`            The containing object.  (obj)
:ref:`PreferenceManager <no-2044>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-2035:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2036:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2037:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2038:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2039:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2040:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2041:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2042:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2043:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2044:

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
:ref:`addField <no-2045>`                    Add a field to the field clause.
:ref:`addFrom <no-2046>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-2047>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-2048>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-2049>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-2050>`                    Add an expression to the where clause.
:ref:`afterInit <no-2051>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-2052>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-2053>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-2054>`            Begin a SQL transaction.
:ref:`bindEvent <no-2055>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-2056>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-2057>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-2058>`           
:ref:`createJustTable <no-2059>`             
:ref:`createTableAndIndexes <no-2060>`       Creates a table and/or indexes based on the dTable passed to it.
:ref:`dblQuoteField <no-2061>`               Takes a string and returns the same string with
:ref:`encloseNames <no-2062>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-2063>`                    
:ref:`flush <no-2064>`                       Firebird requires an explicit commit in order to have changes
:ref:`formSQL <no-2065>`                     Firebird wants the limit clause before the field clause.
:ref:`formatBLOB <no-2066>`                  Properly format a BLOB value to be included in an UPDATE
:ref:`formatDateTime <no-2067>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-2068>`              
:ref:`formatJoinType <no-2069>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-2070>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-2071>`             Return the fully qualified name of the object.
:ref:`getConnection <no-2072>`               
:ref:`getCursor <no-2073>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-2074>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-2075>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-2076>`          
:ref:`getFieldInfoFromDescription <no-2077>` Return field information from the cursor description.
:ref:`getFields <no-2078>`                   
:ref:`getLastInsertID <no-2079>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-2080>`                Override the default 'limit', since Firebird doesn't use that.
:ref:`getMainCursorClass <no-2081>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-2082>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-2083>`     Return the basic field structure.
:ref:`getTableRecordCount <no-2084>`         
:ref:`getTables <no-2085>`                   
:ref:`getUpdateTablePrefix <no-2086>`        By default, the update SQL statement will be in the form of
:ref:`getWhereTablePrefix <no-2087>`         By default, the comparisons in the WHERE clauses of
:ref:`getWordMatchFormat <no-2088>`          By default, will return the standard format for an
:ref:`initEvents <no-2089>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-2090>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-2091>`             Returns whether or not the table exists.
:ref:`isValidModule <no-2092>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-2093>`          Force all the field names to lower case.
:ref:`noResultsOnDelete <no-2094>`           Firebird does not return the number of records deleted, so
:ref:`noResultsOnSave <no-2095>`             Firebird does not return the number of records updated, so
:ref:`pregenPK <no-2096>`                    Determines the generator for which a 'before-insert' trigger
:ref:`prepareWhere <no-2097>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-2098>`               Firebird requires that all field names be surrounded
:ref:`raiseEvent <no-2099>`                  Send the event to all registered listeners.
:ref:`removeField <no-2100>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-2101>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-2102>`         Roll back (revert) a SQL transaction.
:ref:`setChildFilterClause <no-2103>`        
:ref:`setFieldClause <no-2104>`              
:ref:`setFromClause <no-2105>`               
:ref:`setGroupByClause <no-2106>`            
:ref:`setJoinClause <no-2107>`               
:ref:`setNonUpdateFields <no-2108>`          Normally, this routine should work for all backends. But
:ref:`setOrderByClause <no-2109>`            
:ref:`setProperties <no-2110>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-2111>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-2112>`                      
:ref:`setWhereClause <no-2113>`              
:ref:`super <no-2114>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-2115>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-2054:

.. function:: dabo.db.dbFirebird.Firebird.beginTransaction(self, cursor)

   Begin a SQL transaction.



-------

.. _no-2061:

.. function:: dabo.db.dbFirebird.Firebird.dblQuoteField(self, txt)

   
   Takes a string and returns the same string with
   all occurrences of xx.yy replaced with xx."YY".
   In other words, wrap the field name in double-quotes,
   and change it to upper case.
   



-------

.. _no-2063:

.. function:: dabo.db.dbFirebird.Firebird.escQuote(self, val)



-------

.. _no-2064:

.. function:: dabo.db.dbFirebird.Firebird.flush(self, cursor)

   
   Firebird requires an explicit commit in order to have changes
   to the database written to disk.
   



-------

.. _no-2065:

.. function:: dabo.db.dbFirebird.Firebird.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)

   Firebird wants the limit clause before the field clause.



-------

.. _no-2067:

.. function:: dabo.db.dbFirebird.Firebird.formatDateTime(self, val)

   We need to wrap the value in quotes.



-------

.. _no-2072:

.. function:: dabo.db.dbFirebird.Firebird.getConnection(self, connectInfo, \**kwargs)



-------

.. _no-2076:

.. function:: dabo.db.dbFirebird.Firebird.getDictCursorClass(self)



-------

.. _no-2078:

.. function:: dabo.db.dbFirebird.Firebird.getFields(self, tableName, cursor)



-------

.. _no-2080:

.. function:: dabo.db.dbFirebird.Firebird.getLimitWord(self)

   Override the default 'limit', since Firebird doesn't use that.



-------

.. _no-2084:

.. function:: dabo.db.dbFirebird.Firebird.getTableRecordCount(self, tableName, cursor)



-------

.. _no-2085:

.. function:: dabo.db.dbFirebird.Firebird.getTables(self, cursor, includeSystemTables=False)



-------

.. _no-2093:

.. function:: dabo.db.dbFirebird.Firebird.massageDescription(self, cursor)

   Force all the field names to lower case.



-------

.. _no-2094:

.. function:: dabo.db.dbFirebird.Firebird.noResultsOnDelete(self)

   
   Firebird does not return the number of records deleted, so
   we just have to ignore this, since we can't tell a failed delete apart
   from a successful one.
   



-------

.. _no-2095:

.. function:: dabo.db.dbFirebird.Firebird.noResultsOnSave(self)

   
   Firebird does not return the number of records updated, so
   we just have to ignore this, since we can't tell a failed save apart
   from a successful one.
   



-------

.. _no-2096:

.. function:: dabo.db.dbFirebird.Firebird.pregenPK(self, cursor)

   
   Determines the generator for which a 'before-insert' trigger
   is associated with the cursor's table. If one is found, get its
   next value and return it. If not, return None.
   



-------

.. _no-2098:

.. function:: dabo.db.dbFirebird.Firebird.processFields(self, txt)

   
   Firebird requires that all field names be surrounded
   by double quotes.
   



-------

.. _no-2103:

.. function:: dabo.db.dbFirebird.Firebird.setChildFilterClause(self, clause, autoQuote=True)



-------

.. _no-2104:

.. function:: dabo.db.dbFirebird.Firebird.setFieldClause(self, clause, autoQuote=True)



-------

.. _no-2105:

.. function:: dabo.db.dbFirebird.Firebird.setFromClause(self, clause, autoQuote=True)



-------

.. _no-2106:

.. function:: dabo.db.dbFirebird.Firebird.setGroupByClause(self, clause, autoQuote=True)



-------

.. _no-2109:

.. function:: dabo.db.dbFirebird.Firebird.setOrderByClause(self, clause, autoQuote=True)



-------

.. _no-2112:

.. function:: dabo.db.dbFirebird.Firebird.setSQL(self, sql)



-------

.. _no-2113:

.. function:: dabo.db.dbFirebird.Firebird.setWhereClause(self, clause, autoQuote=True)



-------


Methods - inherited
=====================

.. _no-2045:

.. function:: dabo.db.dbFirebird.Firebird.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2046:

.. function:: dabo.db.dbFirebird.Firebird.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2047:

.. function:: dabo.db.dbFirebird.Firebird.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2048:

.. function:: dabo.db.dbFirebird.Firebird.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2049:

.. function:: dabo.db.dbFirebird.Firebird.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2050:

.. function:: dabo.db.dbFirebird.Firebird.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2051:

.. function:: dabo.db.dbFirebird.Firebird.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2052:

.. function:: dabo.db.dbFirebird.Firebird.autoBindEvents(self, force=True)
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

.. _no-2053:

.. function:: dabo.db.dbFirebird.Firebird.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2055:

.. function:: dabo.db.dbFirebird.Firebird.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2056:

.. function:: dabo.db.dbFirebird.Firebird.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2057:

.. function:: dabo.db.dbFirebird.Firebird.commitTransaction(self, cursor)
   :noindex:


   Commit a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2058:

.. function:: dabo.db.dbFirebird.Firebird.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2059:

.. function:: dabo.db.dbFirebird.Firebird.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2060:

.. function:: dabo.db.dbFirebird.Firebird.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndex=True)
   :noindex:


   Creates a table and/or indexes based on the dTable passed to it.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2062:

.. function:: dabo.db.dbFirebird.Firebird.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2066:

.. function:: dabo.db.dbFirebird.Firebird.formatBLOB(self, val)
   :noindex:


   
   Properly format a BLOB value to be included in an UPDATE
   or INSERT statement for a specific backend.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2068:

.. function:: dabo.db.dbFirebird.Firebird.formatForQuery(self, val, fieldType=None)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2069:

.. function:: dabo.db.dbFirebird.Firebird.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2070:

.. function:: dabo.db.dbFirebird.Firebird.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2071:

.. function:: dabo.db.dbFirebird.Firebird.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2073:

.. function:: dabo.db.dbFirebird.Firebird.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2074:

.. function:: dabo.db.dbFirebird.Firebird.getDaboFieldType(self, backendFieldType)
   :noindex:


   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2075:

.. function:: dabo.db.dbFirebird.Firebird.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2077:

.. function:: dabo.db.dbFirebird.Firebird.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2079:

.. function:: dabo.db.dbFirebird.Firebird.getLastInsertID(self, cursor)
   :noindex:


   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK
   value, different databases have their own way of retrieving that value.
   This method should be coded in backend-specific subclasses to address
   that database's approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2081:

.. function:: dabo.db.dbFirebird.Firebird.getMainCursorClass(self)
   :noindex:


   override in subclasses if they need something other than dCursorMixin


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2082:

.. function:: dabo.db.dbFirebird.Firebird.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-2083:

.. function:: dabo.db.dbFirebird.Firebird.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2086:

.. function:: dabo.db.dbFirebird.Firebird.getUpdateTablePrefix(self, tbl, autoQuote=True)
   :noindex:


   
   By default, the update SQL statement will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in an update statement.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2087:

.. function:: dabo.db.dbFirebird.Firebird.getWhereTablePrefix(self, tbl, autoQuote=True)
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

.. _no-2088:

.. function:: dabo.db.dbFirebird.Firebird.getWordMatchFormat(self)
   :noindex:


   
   By default, will return the standard format for an
   equality test. If search by words is available, the format
   must be implemented in each specific backend.
   
   The format must have the expressions %(table)s, %(field)s,
   and %(value)s, which will be replaced with the table, field,
   and value strings, respectively.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2089:

.. function:: dabo.db.dbFirebird.Firebird.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2090:

.. function:: dabo.db.dbFirebird.Firebird.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2091:

.. function:: dabo.db.dbFirebird.Firebird.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2092:

.. function:: dabo.db.dbFirebird.Firebird.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2097:

.. function:: dabo.db.dbFirebird.Firebird.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2099:

.. function:: dabo.db.dbFirebird.Firebird.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-2100:

.. function:: dabo.db.dbFirebird.Firebird.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2101:

.. function:: dabo.db.dbFirebird.Firebird.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2102:

.. function:: dabo.db.dbFirebird.Firebird.rollbackTransaction(self, cursor)
   :noindex:


   Roll back (revert) a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2107:

.. function:: dabo.db.dbFirebird.Firebird.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2108:

.. function:: dabo.db.dbFirebird.Firebird.setNonUpdateFields(self, cursor, autoQuote=True)
   :noindex:


   
   Normally, this routine should work for all backends. But
   in the case of SQLite, the routine that grabs an empty cursor
   doesn't fill in the description, so that backend has to use
   an alternative approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-2110:

.. function:: dabo.db.dbFirebird.Firebird.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-2111:

.. function:: dabo.db.dbFirebird.Firebird.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-2114:

.. function:: dabo.db.dbFirebird.Firebird.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2115:

.. function:: dabo.db.dbFirebird.Firebird.unbindEvent(self, eventClass=None, function=None)
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
