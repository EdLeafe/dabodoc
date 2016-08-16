
.. include:: _static/headings.txt

.. module:: dabo.db.dbPostgreSQL

.. _dabo.db.dbPostgreSQL.Postgres:

==============================================
|doc_title|  **dbPostgreSQL.Postgres** - class
==============================================

Class providing PostgreSQL connectivity. Uses psycopg.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Postgres**

.. inheritance-diagram:: Postgres


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dBackend.dBackend`



|API| Class API
===============


.. autoclass:: dabo.db.dbPostgreSQL.Postgres

   .. automethod:: dabo.db.dbPostgreSQL.Postgres.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1601>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1602>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1603>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1604>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-1605>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-1606>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-1607>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1608>`              The name of the object.  (str)
:ref:`Parent <no-1609>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1610>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-1601:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1602:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1603:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1604:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1605:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1606:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1607:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1608:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1609:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1610:

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
:ref:`addField <no-1611>`                    Add a field to the field clause.
:ref:`addFrom <no-1612>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-1613>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-1614>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-1615>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-1616>`                    Add an expression to the where clause.
:ref:`afterInit <no-1617>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1618>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1619>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-1620>`            
:ref:`bindEvent <no-1621>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-1622>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-1623>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-1624>`           
:ref:`createJustTable <no-1625>`             
:ref:`createTableAndIndexes <no-1626>`       Creates a table and/or indexes based on the dTable passed to it.
:ref:`encloseNames <no-1627>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-1628>`                    
:ref:`flush <no-1629>`                       Postgres requires an explicit commit in order to have changes
:ref:`formSQL <no-1630>`                     Creates the appropriate SQL for the backend, given all
:ref:`formatBLOB <no-1631>`                  Properly format a BLOB value to be included in an UPDATE
:ref:`formatDateTime <no-1632>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-1633>`              
:ref:`formatJoinType <no-1634>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-1635>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-1636>`             Return the fully qualified name of the object.
:ref:`getConnection <no-1637>`               
:ref:`getCursor <no-1638>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-1639>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-1640>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-1641>`          
:ref:`getFieldInfoFromDescription <no-1642>` Return field information from the cursor description.
:ref:`getFields <no-1643>`                   
:ref:`getLastInsertID <no-1644>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-1645>`                Return the word to use in the db-specific limit clause.
:ref:`getMainCursorClass <no-1646>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-1647>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-1648>`     Return the basic field structure.
:ref:`getTableRecordCount <no-1649>`         
:ref:`getTables <no-1650>`                   
:ref:`getUpdateTablePrefix <no-1651>`        By default, the update SQL statement will be in the form of
:ref:`getWhereTablePrefix <no-1652>`         By default, the comparisons in the WHERE clauses of
:ref:`getWordMatchFormat <no-1653>`          By default, will return the standard format for an
:ref:`initEvents <no-1654>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1655>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-1656>`             Returns whether or not the table exists.
:ref:`isValidModule <no-1657>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-1658>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-1659>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-1660>`             Most backends will return a non-zero number if there are updates.
:ref:`pregenPK <no-1661>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-1662>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-1663>`               Default is to return the string unchanged. Override
:ref:`raiseEvent <no-1664>`                  Send the event to all registered listeners.
:ref:`removeField <no-1665>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-1666>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-1667>`         Roll back (revert) a SQL transaction.
:ref:`setChildFilterClause <no-1668>`        
:ref:`setClientEncoding <no-1669>`           
:ref:`setFieldClause <no-1670>`              
:ref:`setFromClause <no-1671>`               
:ref:`setGroupByClause <no-1672>`            
:ref:`setJoinClause <no-1673>`               
:ref:`setNonUpdateFields <no-1674>`          Normally, this routine should work for all backends. But
:ref:`setOrderByClause <no-1675>`            
:ref:`setProperties <no-1676>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1677>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-1678>`                      
:ref:`setWhereClause <no-1679>`              
:ref:`super <no-1680>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1681>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-1620:

.. function:: dabo.db.dbPostgreSQL.Postgres.beginTransaction(self, cursor)



-------

.. _no-1628:

.. function:: dabo.db.dbPostgreSQL.Postgres.escQuote(self, val)



-------

.. _no-1629:

.. function:: dabo.db.dbPostgreSQL.Postgres.flush(self, cursor)

   
   Postgres requires an explicit commit in order to have changes
   to the database written to disk.
   



-------

.. _no-1632:

.. function:: dabo.db.dbPostgreSQL.Postgres.formatDateTime(self, val)

   We need to wrap the value in quotes.



-------

.. _no-1637:

.. function:: dabo.db.dbPostgreSQL.Postgres.getConnection(self, connectInfo, \**kwargs)



-------

.. _no-1641:

.. function:: dabo.db.dbPostgreSQL.Postgres.getDictCursorClass(self)



-------

.. _no-1643:

.. function:: dabo.db.dbPostgreSQL.Postgres.getFields(self, tableName, cursor, includeSystemFields=False)



-------

.. _no-1644:

.. function:: dabo.db.dbPostgreSQL.Postgres.getLastInsertID(self, cursor)

   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK (such
   as a serial data type) value, different databases have their own way of retrieving that value.
   With Postgres a sequence is created.  The SQL statement determines the sequence name
   ('table_pkid_seq') and needs three parameters the schema name, table name, and the primary
   key field for the table.
   
   cursor.KeyField = primary field
   cursor.Table = returns 'schema.table' for the cursor
   
   Postgres uses 'currval(sequence_name)' to determine the last value of the session.
   If two different sessions are open (two users accessing the same table for example)
   currval() will return the correct value for each session.
   
   



-------

.. _no-1649:

.. function:: dabo.db.dbPostgreSQL.Postgres.getTableRecordCount(self, tableName, cursor)



-------

.. _no-1650:

.. function:: dabo.db.dbPostgreSQL.Postgres.getTables(self, cursor, includeSystemTables=False)



-------

.. _no-1651:

.. function:: dabo.db.dbPostgreSQL.Postgres.getUpdateTablePrefix(self, tbl, autoQuote=True)

   
   By default, the update SQL statement will be in the form of
   
               tablename.fieldname
   
   but Postgres does not accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in an update statement.
   Postgres needs to return an empty string.
   



-------

.. _no-1659:

.. function:: dabo.db.dbPostgreSQL.Postgres.noResultsOnDelete(self)

   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   



-------

.. _no-1660:

.. function:: dabo.db.dbPostgreSQL.Postgres.noResultsOnSave(self)

   
   Most backends will return a non-zero number if there are updates.
   Some do not, so this will have to be customized in those cases.
   



-------

.. _no-1669:

.. function:: dabo.db.dbPostgreSQL.Postgres.setClientEncoding(self, encoding=None)



-------


Methods - inherited
=====================

.. _no-1611:

.. function:: dabo.db.dbPostgreSQL.Postgres.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1612:

.. function:: dabo.db.dbPostgreSQL.Postgres.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1613:

.. function:: dabo.db.dbPostgreSQL.Postgres.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1614:

.. function:: dabo.db.dbPostgreSQL.Postgres.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1615:

.. function:: dabo.db.dbPostgreSQL.Postgres.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1616:

.. function:: dabo.db.dbPostgreSQL.Postgres.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1617:

.. function:: dabo.db.dbPostgreSQL.Postgres.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1618:

.. function:: dabo.db.dbPostgreSQL.Postgres.autoBindEvents(self, force=True)
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

.. _no-1619:

.. function:: dabo.db.dbPostgreSQL.Postgres.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1621:

.. function:: dabo.db.dbPostgreSQL.Postgres.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1622:

.. function:: dabo.db.dbPostgreSQL.Postgres.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1623:

.. function:: dabo.db.dbPostgreSQL.Postgres.commitTransaction(self, cursor)
   :noindex:


   Commit a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1624:

.. function:: dabo.db.dbPostgreSQL.Postgres.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1625:

.. function:: dabo.db.dbPostgreSQL.Postgres.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1626:

.. function:: dabo.db.dbPostgreSQL.Postgres.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndex=True)
   :noindex:


   Creates a table and/or indexes based on the dTable passed to it.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1627:

.. function:: dabo.db.dbPostgreSQL.Postgres.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1630:

.. function:: dabo.db.dbPostgreSQL.Postgres.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)
   :noindex:


   
   Creates the appropriate SQL for the backend, given all
   the required clauses. Some backends order these differently, so
   they should override this method with their own ordering.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1631:

.. function:: dabo.db.dbPostgreSQL.Postgres.formatBLOB(self, val)
   :noindex:


   
   Properly format a BLOB value to be included in an UPDATE
   or INSERT statement for a specific backend.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1633:

.. function:: dabo.db.dbPostgreSQL.Postgres.formatForQuery(self, val, fieldType=None)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1634:

.. function:: dabo.db.dbPostgreSQL.Postgres.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1635:

.. function:: dabo.db.dbPostgreSQL.Postgres.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1636:

.. function:: dabo.db.dbPostgreSQL.Postgres.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1638:

.. function:: dabo.db.dbPostgreSQL.Postgres.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1639:

.. function:: dabo.db.dbPostgreSQL.Postgres.getDaboFieldType(self, backendFieldType)
   :noindex:


   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1640:

.. function:: dabo.db.dbPostgreSQL.Postgres.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1642:

.. function:: dabo.db.dbPostgreSQL.Postgres.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1645:

.. function:: dabo.db.dbPostgreSQL.Postgres.getLimitWord(self)
   :noindex:


   
   Return the word to use in the db-specific limit clause.
   Override for backends that don't use the word 'limit'
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1646:

.. function:: dabo.db.dbPostgreSQL.Postgres.getMainCursorClass(self)
   :noindex:


   override in subclasses if they need something other than dCursorMixin


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1647:

.. function:: dabo.db.dbPostgreSQL.Postgres.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1648:

.. function:: dabo.db.dbPostgreSQL.Postgres.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1652:

.. function:: dabo.db.dbPostgreSQL.Postgres.getWhereTablePrefix(self, tbl, autoQuote=True)
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

.. _no-1653:

.. function:: dabo.db.dbPostgreSQL.Postgres.getWordMatchFormat(self)
   :noindex:


   
   By default, will return the standard format for an
   equality test. If search by words is available, the format
   must be implemented in each specific backend.
   
   The format must have the expressions %(table)s, %(field)s,
   and %(value)s, which will be replaced with the table, field,
   and value strings, respectively.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1654:

.. function:: dabo.db.dbPostgreSQL.Postgres.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1655:

.. function:: dabo.db.dbPostgreSQL.Postgres.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1656:

.. function:: dabo.db.dbPostgreSQL.Postgres.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1657:

.. function:: dabo.db.dbPostgreSQL.Postgres.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1658:

.. function:: dabo.db.dbPostgreSQL.Postgres.massageDescription(self, cursor)
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

.. _no-1661:

.. function:: dabo.db.dbPostgreSQL.Postgres.pregenPK(self, cursor)
   :noindex:


   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1662:

.. function:: dabo.db.dbPostgreSQL.Postgres.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1663:

.. function:: dabo.db.dbPostgreSQL.Postgres.processFields(self, txt)
   :noindex:


   
   Default is to return the string unchanged. Override
   in cases where the str needs processing.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1664:

.. function:: dabo.db.dbPostgreSQL.Postgres.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1665:

.. function:: dabo.db.dbPostgreSQL.Postgres.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1666:

.. function:: dabo.db.dbPostgreSQL.Postgres.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1667:

.. function:: dabo.db.dbPostgreSQL.Postgres.rollbackTransaction(self, cursor)
   :noindex:


   Roll back (revert) a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1668:

.. function:: dabo.db.dbPostgreSQL.Postgres.setChildFilterClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1670:

.. function:: dabo.db.dbPostgreSQL.Postgres.setFieldClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1671:

.. function:: dabo.db.dbPostgreSQL.Postgres.setFromClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1672:

.. function:: dabo.db.dbPostgreSQL.Postgres.setGroupByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1673:

.. function:: dabo.db.dbPostgreSQL.Postgres.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1674:

.. function:: dabo.db.dbPostgreSQL.Postgres.setNonUpdateFields(self, cursor, autoQuote=True)
   :noindex:


   
   Normally, this routine should work for all backends. But
   in the case of SQLite, the routine that grabs an empty cursor
   doesn't fill in the description, so that backend has to use
   an alternative approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1675:

.. function:: dabo.db.dbPostgreSQL.Postgres.setOrderByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1676:

.. function:: dabo.db.dbPostgreSQL.Postgres.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1677:

.. function:: dabo.db.dbPostgreSQL.Postgres.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1678:

.. function:: dabo.db.dbPostgreSQL.Postgres.setSQL(self, sql)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1679:

.. function:: dabo.db.dbPostgreSQL.Postgres.setWhereClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1680:

.. function:: dabo.db.dbPostgreSQL.Postgres.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1681:

.. function:: dabo.db.dbPostgreSQL.Postgres.unbindEvent(self, eventClass=None, function=None)
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
