
.. include:: _static/headings.txt

.. module:: dabo.db.dbSQLite

.. _dabo.db.dbSQLite.SQLite:

========================================
|doc_title|  **dbSQLite.SQLite** - class
========================================

Class providing SQLite connectivity. Uses sqlite3 or pysqlite2 package.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SQLite**

.. inheritance-diagram:: SQLite


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dBackend.dBackend`



|API| Class API
===============


.. autoclass:: dabo.db.dbSQLite.SQLite

   .. automethod:: dabo.db.dbSQLite.SQLite.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1521>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1522>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1523>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1524>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-1525>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-1526>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-1527>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1528>`              The name of the object.  (str)
:ref:`Parent <no-1529>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1530>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-1521:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1522:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1523:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1524:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1525:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1526:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1527:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1528:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1529:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1530:

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
:ref:`addField <no-1531>`                    Add a field to the field clause.
:ref:`addFrom <no-1532>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-1533>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-1534>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-1535>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-1536>`                    Add an expression to the where clause.
:ref:`afterInit <no-1537>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1538>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1539>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-1540>`            Begin a SQL transaction. Since pysqlite does an implicit
:ref:`bindEvent <no-1541>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-1542>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-1543>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-1544>`           
:ref:`createJustTable <no-1545>`             
:ref:`createTableAndIndexes <no-1546>`       
:ref:`encloseNames <no-1547>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-1548>`                    
:ref:`flush <no-1549>`                       
:ref:`formSQL <no-1550>`                     Creates the appropriate SQL for the backend, given all
:ref:`formatBLOB <no-1551>`                  
:ref:`formatDateTime <no-1552>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-1553>`              
:ref:`formatJoinType <no-1554>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-1555>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-1556>`             Return the fully qualified name of the object.
:ref:`getConnection <no-1557>`               
:ref:`getCursor <no-1558>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-1559>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-1560>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-1561>`          
:ref:`getFieldInfoFromDescription <no-1562>` Return field information from the cursor description.
:ref:`getFields <no-1563>`                   
:ref:`getLastInsertID <no-1564>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-1565>`                Return the word to use in the db-specific limit clause.
:ref:`getMainCursorClass <no-1566>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-1567>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-1568>`     Return the basic field structure.
:ref:`getTableRecordCount <no-1569>`         
:ref:`getTables <no-1570>`                   
:ref:`getUpdateTablePrefix <no-1571>`        Table name prefixes are not allowed.
:ref:`getWhereTablePrefix <no-1572>`         Table name prefixes are not allowed.
:ref:`getWordMatchFormat <no-1573>`          By default, will return the standard format for an
:ref:`initEvents <no-1574>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1575>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-1576>`             Returns whether or not the table exists.
:ref:`isValidModule <no-1577>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-1578>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-1579>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-1580>`             SQLite does not return anything on a successful update
:ref:`pregenPK <no-1581>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-1582>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-1583>`               Default is to return the string unchanged. Override
:ref:`raiseEvent <no-1584>`                  Send the event to all registered listeners.
:ref:`removeField <no-1585>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-1586>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-1587>`         Rollback a SQL transaction.
:ref:`setChildFilterClause <no-1588>`        
:ref:`setFieldClause <no-1589>`              
:ref:`setFromClause <no-1590>`               
:ref:`setGroupByClause <no-1591>`            
:ref:`setJoinClause <no-1592>`               
:ref:`setNonUpdateFields <no-1593>`          
:ref:`setOrderByClause <no-1594>`            
:ref:`setProperties <no-1595>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1596>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-1597>`                      
:ref:`setWhereClause <no-1598>`              
:ref:`super <no-1599>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1600>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-1540:

.. function:: dabo.db.dbSQLite.SQLite.beginTransaction(self, cursor)

   
   Begin a SQL transaction. Since pysqlite does an implicit
   'begin' all the time, simply do nothing.
   



-------

.. _no-1543:

.. function:: dabo.db.dbSQLite.SQLite.commitTransaction(self, cursor)

   Commit a SQL transaction.



-------

.. _no-1546:

.. function:: dabo.db.dbSQLite.SQLite.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndexes=True)



-------

.. _no-1548:

.. function:: dabo.db.dbSQLite.SQLite.escQuote(self, val)



-------

.. _no-1549:

.. function:: dabo.db.dbSQLite.SQLite.flush(self, crs)



-------

.. _no-1551:

.. function:: dabo.db.dbSQLite.SQLite.formatBLOB(self, val)



-------

.. _no-1552:

.. function:: dabo.db.dbSQLite.SQLite.formatDateTime(self, val)

   We need to wrap the value in quotes.



-------

.. _no-1553:

.. function:: dabo.db.dbSQLite.SQLite.formatForQuery(self, val, fieldType=None)



-------

.. _no-1557:

.. function:: dabo.db.dbSQLite.SQLite.getConnection(self, connectInfo, forceCreate=False, \**kwargs)



-------

.. _no-1561:

.. function:: dabo.db.dbSQLite.SQLite.getDictCursorClass(self)



-------

.. _no-1563:

.. function:: dabo.db.dbSQLite.SQLite.getFields(self, tableName, cursor)



-------

.. _no-1569:

.. function:: dabo.db.dbSQLite.SQLite.getTableRecordCount(self, tableName, cursor)



-------

.. _no-1570:

.. function:: dabo.db.dbSQLite.SQLite.getTables(self, cursor, includeSystemTables=False)



-------

.. _no-1571:

.. function:: dabo.db.dbSQLite.SQLite.getUpdateTablePrefix(self, table, autoQuote=True)

   Table name prefixes are not allowed.



-------

.. _no-1572:

.. function:: dabo.db.dbSQLite.SQLite.getWhereTablePrefix(self, table, autoQuote=True)

   Table name prefixes are not allowed.



-------

.. _no-1580:

.. function:: dabo.db.dbSQLite.SQLite.noResultsOnSave(self)

   SQLite does not return anything on a successful update



-------

.. _no-1587:

.. function:: dabo.db.dbSQLite.SQLite.rollbackTransaction(self, cursor)

   Rollback a SQL transaction.



-------

.. _no-1593:

.. function:: dabo.db.dbSQLite.SQLite.setNonUpdateFields(self, cursor)



-------


Methods - inherited
=====================

.. _no-1531:

.. function:: dabo.db.dbSQLite.SQLite.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1532:

.. function:: dabo.db.dbSQLite.SQLite.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1533:

.. function:: dabo.db.dbSQLite.SQLite.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1534:

.. function:: dabo.db.dbSQLite.SQLite.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1535:

.. function:: dabo.db.dbSQLite.SQLite.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1536:

.. function:: dabo.db.dbSQLite.SQLite.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1537:

.. function:: dabo.db.dbSQLite.SQLite.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1538:

.. function:: dabo.db.dbSQLite.SQLite.autoBindEvents(self, force=True)
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

.. _no-1539:

.. function:: dabo.db.dbSQLite.SQLite.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1541:

.. function:: dabo.db.dbSQLite.SQLite.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1542:

.. function:: dabo.db.dbSQLite.SQLite.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1544:

.. function:: dabo.db.dbSQLite.SQLite.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1545:

.. function:: dabo.db.dbSQLite.SQLite.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1547:

.. function:: dabo.db.dbSQLite.SQLite.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1550:

.. function:: dabo.db.dbSQLite.SQLite.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)
   :noindex:


   
   Creates the appropriate SQL for the backend, given all
   the required clauses. Some backends order these differently, so
   they should override this method with their own ordering.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1554:

.. function:: dabo.db.dbSQLite.SQLite.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1555:

.. function:: dabo.db.dbSQLite.SQLite.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1556:

.. function:: dabo.db.dbSQLite.SQLite.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1558:

.. function:: dabo.db.dbSQLite.SQLite.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1559:

.. function:: dabo.db.dbSQLite.SQLite.getDaboFieldType(self, backendFieldType)
   :noindex:


   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1560:

.. function:: dabo.db.dbSQLite.SQLite.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1562:

.. function:: dabo.db.dbSQLite.SQLite.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1564:

.. function:: dabo.db.dbSQLite.SQLite.getLastInsertID(self, cursor)
   :noindex:


   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK
   value, different databases have their own way of retrieving that value.
   This method should be coded in backend-specific subclasses to address
   that database's approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1565:

.. function:: dabo.db.dbSQLite.SQLite.getLimitWord(self)
   :noindex:


   
   Return the word to use in the db-specific limit clause.
   Override for backends that don't use the word 'limit'
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1566:

.. function:: dabo.db.dbSQLite.SQLite.getMainCursorClass(self)
   :noindex:


   override in subclasses if they need something other than dCursorMixin


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1567:

.. function:: dabo.db.dbSQLite.SQLite.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1568:

.. function:: dabo.db.dbSQLite.SQLite.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1573:

.. function:: dabo.db.dbSQLite.SQLite.getWordMatchFormat(self)
   :noindex:


   
   By default, will return the standard format for an
   equality test. If search by words is available, the format
   must be implemented in each specific backend.
   
   The format must have the expressions %(table)s, %(field)s,
   and %(value)s, which will be replaced with the table, field,
   and value strings, respectively.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1574:

.. function:: dabo.db.dbSQLite.SQLite.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1575:

.. function:: dabo.db.dbSQLite.SQLite.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1576:

.. function:: dabo.db.dbSQLite.SQLite.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1577:

.. function:: dabo.db.dbSQLite.SQLite.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1578:

.. function:: dabo.db.dbSQLite.SQLite.massageDescription(self, cursor)
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

.. _no-1579:

.. function:: dabo.db.dbSQLite.SQLite.noResultsOnDelete(self)
   :noindex:


   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1581:

.. function:: dabo.db.dbSQLite.SQLite.pregenPK(self, cursor)
   :noindex:


   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1582:

.. function:: dabo.db.dbSQLite.SQLite.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1583:

.. function:: dabo.db.dbSQLite.SQLite.processFields(self, txt)
   :noindex:


   
   Default is to return the string unchanged. Override
   in cases where the str needs processing.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1584:

.. function:: dabo.db.dbSQLite.SQLite.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1585:

.. function:: dabo.db.dbSQLite.SQLite.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1586:

.. function:: dabo.db.dbSQLite.SQLite.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1588:

.. function:: dabo.db.dbSQLite.SQLite.setChildFilterClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1589:

.. function:: dabo.db.dbSQLite.SQLite.setFieldClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1590:

.. function:: dabo.db.dbSQLite.SQLite.setFromClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1591:

.. function:: dabo.db.dbSQLite.SQLite.setGroupByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1592:

.. function:: dabo.db.dbSQLite.SQLite.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1594:

.. function:: dabo.db.dbSQLite.SQLite.setOrderByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1595:

.. function:: dabo.db.dbSQLite.SQLite.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1596:

.. function:: dabo.db.dbSQLite.SQLite.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1597:

.. function:: dabo.db.dbSQLite.SQLite.setSQL(self, sql)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1598:

.. function:: dabo.db.dbSQLite.SQLite.setWhereClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1599:

.. function:: dabo.db.dbSQLite.SQLite.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1600:

.. function:: dabo.db.dbSQLite.SQLite.unbindEvent(self, eventClass=None, function=None)
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
