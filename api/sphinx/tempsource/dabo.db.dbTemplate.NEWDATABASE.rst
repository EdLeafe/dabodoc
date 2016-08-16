
.. include:: _static/headings.txt

.. module:: dabo.db.dbTemplate

.. _dabo.db.dbTemplate.NEWDATABASE:

===============================================
|doc_title|  **dbTemplate.NEWDATABASE** - class
===============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **NEWDATABASE**

.. inheritance-diagram:: NEWDATABASE


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dBackend.dBackend`



|API| Class API
===============


.. autoclass:: dabo.db.dbTemplate.NEWDATABASE

   .. automethod:: dabo.db.dbTemplate.NEWDATABASE.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1714>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1715>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1716>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1717>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-1718>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-1719>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-1720>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1721>`              The name of the object.  (str)
:ref:`Parent <no-1722>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1723>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-1714:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1715:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1716:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1717:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1718:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1719:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1720:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1721:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1722:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1723:

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
:ref:`addField <no-1724>`                    Add a field to the field clause.
:ref:`addFrom <no-1725>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-1726>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-1727>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-1728>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-1729>`                    Add an expression to the where clause.
:ref:`afterInit <no-1730>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1731>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1732>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-1733>`            Begin a SQL transaction. Override in subclasses if needed.
:ref:`bindEvent <no-1734>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-1735>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-1736>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-1737>`           
:ref:`createJustTable <no-1738>`             
:ref:`createTableAndIndexes <no-1739>`       Creates a table and/or indexes based on the dTable passed to it.
:ref:`encloseNames <no-1740>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-1741>`                    
:ref:`flush <no-1742>`                       Only used in some backends
:ref:`formSQL <no-1743>`                     Creates the appropriate SQL for the backend, given all
:ref:`formatBLOB <no-1744>`                  Properly format a BLOB value to be included in an UPDATE
:ref:`formatDateTime <no-1745>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-1746>`              
:ref:`formatJoinType <no-1747>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-1748>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-1749>`             Return the fully qualified name of the object.
:ref:`getConnection <no-1750>`               
:ref:`getCursor <no-1751>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-1752>`            Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
:ref:`getDescription <no-1753>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-1754>`          
:ref:`getFieldInfoFromDescription <no-1755>` Return field information from the cursor description.
:ref:`getFields <no-1756>`                   
:ref:`getLastInsertID <no-1757>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-1758>`                Return the word to use in the db-specific limit clause.
:ref:`getMainCursorClass <no-1759>`          override in subclasses if they need something other than dCursorMixin
:ref:`getProperties <no-1760>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-1761>`     Return the basic field structure.
:ref:`getTableRecordCount <no-1762>`         
:ref:`getTables <no-1763>`                   
:ref:`getUpdateTablePrefix <no-1764>`        By default, the update SQL statement will be in the form of
:ref:`getWhereTablePrefix <no-1765>`         By default, the comparisons in the WHERE clauses of
:ref:`getWordMatchFormat <no-1766>`          
:ref:`initEvents <no-1767>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1768>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-1769>`             Returns whether or not the table exists.
:ref:`isValidModule <no-1770>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-1771>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-1772>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-1773>`             Most backends will return a non-zero number if there are updates.
:ref:`pregenPK <no-1774>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-1775>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-1776>`               Default is to return the string unchanged. Override
:ref:`raiseEvent <no-1777>`                  Send the event to all registered listeners.
:ref:`removeField <no-1778>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-1779>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-1780>`         Roll back (revert) a SQL transaction.
:ref:`setChildFilterClause <no-1781>`        
:ref:`setFieldClause <no-1782>`              
:ref:`setFromClause <no-1783>`               
:ref:`setGroupByClause <no-1784>`            
:ref:`setJoinClause <no-1785>`               
:ref:`setNonUpdateFields <no-1786>`          Normally, this routine should work for all backends. But
:ref:`setOrderByClause <no-1787>`            
:ref:`setProperties <no-1788>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1789>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-1790>`                      
:ref:`setWhereClause <no-1791>`              
:ref:`super <no-1792>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1793>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-1741:

.. function:: dabo.db.dbTemplate.NEWDATABASE.escQuote(self, val)



-------

.. _no-1745:

.. function:: dabo.db.dbTemplate.NEWDATABASE.formatDateTime(self, val)

   We need to wrap the value in quotes.



-------

.. _no-1750:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getConnection(self, connectInfo, \**kwargs)



-------

.. _no-1754:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getDictCursorClass(self)



-------

.. _no-1756:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getFields(self, tableName)



-------

.. _no-1762:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getTableRecordCount(self, tableName)



-------

.. _no-1763:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getTables(self, cursor, includeSystemTables=False)



-------

.. _no-1766:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getWordMatchFormat(self)



-------


Methods - inherited
=====================

.. _no-1724:

.. function:: dabo.db.dbTemplate.NEWDATABASE.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1725:

.. function:: dabo.db.dbTemplate.NEWDATABASE.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1726:

.. function:: dabo.db.dbTemplate.NEWDATABASE.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1727:

.. function:: dabo.db.dbTemplate.NEWDATABASE.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1728:

.. function:: dabo.db.dbTemplate.NEWDATABASE.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1729:

.. function:: dabo.db.dbTemplate.NEWDATABASE.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1730:

.. function:: dabo.db.dbTemplate.NEWDATABASE.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1731:

.. function:: dabo.db.dbTemplate.NEWDATABASE.autoBindEvents(self, force=True)
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

.. _no-1732:

.. function:: dabo.db.dbTemplate.NEWDATABASE.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1733:

.. function:: dabo.db.dbTemplate.NEWDATABASE.beginTransaction(self, cursor)
   :noindex:


   Begin a SQL transaction. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1734:

.. function:: dabo.db.dbTemplate.NEWDATABASE.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1735:

.. function:: dabo.db.dbTemplate.NEWDATABASE.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1736:

.. function:: dabo.db.dbTemplate.NEWDATABASE.commitTransaction(self, cursor)
   :noindex:


   Commit a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1737:

.. function:: dabo.db.dbTemplate.NEWDATABASE.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1738:

.. function:: dabo.db.dbTemplate.NEWDATABASE.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1739:

.. function:: dabo.db.dbTemplate.NEWDATABASE.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndex=True)
   :noindex:


   Creates a table and/or indexes based on the dTable passed to it.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1740:

.. function:: dabo.db.dbTemplate.NEWDATABASE.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1742:

.. function:: dabo.db.dbTemplate.NEWDATABASE.flush(self, cursor)
   :noindex:


   Only used in some backends


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1743:

.. function:: dabo.db.dbTemplate.NEWDATABASE.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)
   :noindex:


   
   Creates the appropriate SQL for the backend, given all
   the required clauses. Some backends order these differently, so
   they should override this method with their own ordering.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1744:

.. function:: dabo.db.dbTemplate.NEWDATABASE.formatBLOB(self, val)
   :noindex:


   
   Properly format a BLOB value to be included in an UPDATE
   or INSERT statement for a specific backend.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1746:

.. function:: dabo.db.dbTemplate.NEWDATABASE.formatForQuery(self, val, fieldType=None)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1747:

.. function:: dabo.db.dbTemplate.NEWDATABASE.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1748:

.. function:: dabo.db.dbTemplate.NEWDATABASE.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1749:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1751:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1752:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getDaboFieldType(self, backendFieldType)
   :noindex:


   
   Return the Dabo code (I, T, D, ...) for the passed backend Field Type.
   
   If it can't be determined, the field type will be '?'.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1753:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1755:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1757:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getLastInsertID(self, cursor)
   :noindex:


   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK
   value, different databases have their own way of retrieving that value.
   This method should be coded in backend-specific subclasses to address
   that database's approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1758:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getLimitWord(self)
   :noindex:


   
   Return the word to use in the db-specific limit clause.
   Override for backends that don't use the word 'limit'
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1759:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getMainCursorClass(self)
   :noindex:


   override in subclasses if they need something other than dCursorMixin


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1760:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1761:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1764:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getUpdateTablePrefix(self, tbl, autoQuote=True)
   :noindex:


   
   By default, the update SQL statement will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in an update statement.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1765:

.. function:: dabo.db.dbTemplate.NEWDATABASE.getWhereTablePrefix(self, tbl, autoQuote=True)
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

.. _no-1767:

.. function:: dabo.db.dbTemplate.NEWDATABASE.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1768:

.. function:: dabo.db.dbTemplate.NEWDATABASE.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1769:

.. function:: dabo.db.dbTemplate.NEWDATABASE.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1770:

.. function:: dabo.db.dbTemplate.NEWDATABASE.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1771:

.. function:: dabo.db.dbTemplate.NEWDATABASE.massageDescription(self, cursor)
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

.. _no-1772:

.. function:: dabo.db.dbTemplate.NEWDATABASE.noResultsOnDelete(self)
   :noindex:


   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1773:

.. function:: dabo.db.dbTemplate.NEWDATABASE.noResultsOnSave(self)
   :noindex:


   
   Most backends will return a non-zero number if there are updates.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1774:

.. function:: dabo.db.dbTemplate.NEWDATABASE.pregenPK(self, cursor)
   :noindex:


   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1775:

.. function:: dabo.db.dbTemplate.NEWDATABASE.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1776:

.. function:: dabo.db.dbTemplate.NEWDATABASE.processFields(self, txt)
   :noindex:


   
   Default is to return the string unchanged. Override
   in cases where the str needs processing.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1777:

.. function:: dabo.db.dbTemplate.NEWDATABASE.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1778:

.. function:: dabo.db.dbTemplate.NEWDATABASE.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1779:

.. function:: dabo.db.dbTemplate.NEWDATABASE.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1780:

.. function:: dabo.db.dbTemplate.NEWDATABASE.rollbackTransaction(self, cursor)
   :noindex:


   Roll back (revert) a SQL transaction.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1781:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setChildFilterClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1782:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setFieldClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1783:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setFromClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1784:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setGroupByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1785:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1786:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setNonUpdateFields(self, cursor, autoQuote=True)
   :noindex:


   
   Normally, this routine should work for all backends. But
   in the case of SQLite, the routine that grabs an empty cursor
   doesn't fill in the description, so that backend has to use
   an alternative approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1787:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setOrderByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1788:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1789:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1790:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setSQL(self, sql)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1791:

.. function:: dabo.db.dbTemplate.NEWDATABASE.setWhereClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1792:

.. function:: dabo.db.dbTemplate.NEWDATABASE.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1793:

.. function:: dabo.db.dbTemplate.NEWDATABASE.unbindEvent(self, eventClass=None, function=None)
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
