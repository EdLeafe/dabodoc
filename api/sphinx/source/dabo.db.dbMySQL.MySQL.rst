
.. include:: _static/headings.txt

.. module:: dabo.db.dbMySQL

.. _dabo.db.dbMySQL.MySQL:

======================================
|doc_title|  **dbMySQL.MySQL** - class
======================================

Class providing MySQL connectivity. Uses MySQLdb.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **MySQL**

.. inheritance-diagram:: MySQL


|supclasses| Known Superclasses
===============================

* :ref:`dabo.db.dBackend.dBackend`



|API| Class API
===============


.. autoclass:: dabo.db.dbMySQL.MySQL

   .. automethod:: dabo.db.dbMySQL.MySQL.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1794>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1795>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1796>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1797>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-1798>`          Backend encoding  (str)
:ref:`KeepAliveInterval <no-1799>` Specifies how often a KeepAlive query should be sent to the server.
:ref:`LogEvents <no-1800>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1801>`              The name of the object.  (str)
:ref:`Parent <no-1802>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1803>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-1794:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1795:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1796:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1797:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1798:

**Encoding** 

Backend encoding  (str)


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1799:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server.

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1800:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1801:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1802:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1803:

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
:ref:`addField <no-1804>`                    Add a field to the field clause.
:ref:`addFrom <no-1805>`                     Add a table to the sql statement.
:ref:`addGroupBy <no-1806>`                  Add an expression to the group-by clause.
:ref:`addJoin <no-1807>`                     Add a joined table to the sql statement.
:ref:`addOrderBy <no-1808>`                  Add an expression to the order-by clause.
:ref:`addWhere <no-1809>`                    Add an expression to the where clause.
:ref:`afterInit <no-1810>`                   Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1811>`              Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1812>`                  Subclass hook. Called before the object is fully instantiated.
:ref:`beginTransaction <no-1813>`            Begin a SQL transaction.
:ref:`bindEvent <no-1814>`                   Bind a dEvent to a callback function.
:ref:`bindEvents <no-1815>`                  Bind a sequence of [dEvent, callback] lists.
:ref:`commitTransaction <no-1816>`           Commit a SQL transaction.
:ref:`createJustIndexes <no-1817>`           
:ref:`createJustTable <no-1818>`             
:ref:`createTableAndIndexes <no-1819>`       
:ref:`encloseNames <no-1820>`                When table/field names contain spaces, this will safely enclose them
:ref:`escQuote <no-1821>`                    
:ref:`flush <no-1822>`                       Only used in some backends
:ref:`formSQL <no-1823>`                     Creates the appropriate SQL for the backend, given all
:ref:`formatBLOB <no-1824>`                  Properly format a BLOB value to be included in an UPDATE
:ref:`formatDateTime <no-1825>`              We need to wrap the value in quotes.
:ref:`formatForQuery <no-1826>`              
:ref:`formatJoinType <no-1827>`              Default formatting for jointype keywords. Override in subclasses if needed.
:ref:`formatNone <no-1828>`                  Properly format a None value to be included in an update statement.
:ref:`getAbsoluteName <no-1829>`             Return the fully qualified name of the object.
:ref:`getConnection <no-1830>`               
:ref:`getCursor <no-1831>`                   override in subclasses if necessary
:ref:`getDaboFieldType <no-1832>`            
:ref:`getDescription <no-1833>`              Normally, cursors should always be able to report their
:ref:`getDictCursorClass <no-1834>`          
:ref:`getFieldInfoFromDescription <no-1835>` Return field information from the cursor description.
:ref:`getFields <no-1836>`                   
:ref:`getLastInsertID <no-1837>`             Return the ID of the last inserted row, or None.
:ref:`getLimitWord <no-1838>`                Return the word to use in the db-specific limit clause.
:ref:`getMainCursorClass <no-1839>`          
:ref:`getProperties <no-1840>`               Returns a dictionary of property name/value pairs.
:ref:`getStructureDescription <no-1841>`     Return the basic field structure.
:ref:`getTableRecordCount <no-1842>`         
:ref:`getTables <no-1843>`                   
:ref:`getUpdateTablePrefix <no-1844>`        By default, the update SQL statement will be in the form of
:ref:`getWhereTablePrefix <no-1845>`         By default, the comparisons in the WHERE clauses of
:ref:`getWordMatchFormat <no-1846>`          MySQL's fulltext search expression
:ref:`initEvents <no-1847>`                  Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1848>`              Hook for subclasses. User subclasses should set properties
:ref:`isExistingTable <no-1849>`             Returns whether or not the table exists.
:ref:`isValidModule <no-1850>`               Test the dbapi to see if it is supported on this computer.
:ref:`massageDescription <no-1851>`          Some dbapi programs do strange things to the description.
:ref:`noResultsOnDelete <no-1852>`           Most backends will return a non-zero number if there are deletions.
:ref:`noResultsOnSave <no-1853>`             Most backends will return a non-zero number if there are updates.
:ref:`pregenPK <no-1854>`                    In the case where the database requires that PKs be generated
:ref:`prepareWhere <no-1855>`                Normally, just return the original. Can be overridden as needed
:ref:`processFields <no-1856>`               Default is to return the string unchanged. Override
:ref:`raiseEvent <no-1857>`                  Send the event to all registered listeners.
:ref:`removeField <no-1858>`                 Remove a previously added field from the field clause.
:ref:`removeWhere <no-1859>`                 Remove a previously-added expression from the where clause.
:ref:`rollbackTransaction <no-1860>`         Rollback a SQL transaction.
:ref:`setChildFilterClause <no-1861>`        
:ref:`setFieldClause <no-1862>`              
:ref:`setFromClause <no-1863>`               
:ref:`setGroupByClause <no-1864>`            
:ref:`setJoinClause <no-1865>`               
:ref:`setNonUpdateFields <no-1866>`          Normally, this routine should work for all backends. But
:ref:`setOrderByClause <no-1867>`            
:ref:`setProperties <no-1868>`               Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1869>`       Sets a group of properties on the object all at once. This
:ref:`setSQL <no-1870>`                      
:ref:`setWhereClause <no-1871>`              
:ref:`super <no-1872>`                       This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1873>`                 Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-1813:

.. function:: dabo.db.dbMySQL.MySQL.beginTransaction(self, cursor)

    Begin a SQL transaction.



-------

.. _no-1816:

.. function:: dabo.db.dbMySQL.MySQL.commitTransaction(self, cursor)

    Commit a SQL transaction.



-------

.. _no-1819:

.. function:: dabo.db.dbMySQL.MySQL.createTableAndIndexes(self, tabledef, cursor, createTable=True, createIndexes=True)



-------

.. _no-1821:

.. function:: dabo.db.dbMySQL.MySQL.escQuote(self, val)



-------

.. _no-1825:

.. function:: dabo.db.dbMySQL.MySQL.formatDateTime(self, val)

    We need to wrap the value in quotes. 



-------

.. _no-1830:

.. function:: dabo.db.dbMySQL.MySQL.getConnection(self, connectInfo, \**kwargs)



-------

.. _no-1832:

.. function:: dabo.db.dbMySQL.MySQL.getDaboFieldType(self, backendFieldType)



-------

.. _no-1834:

.. function:: dabo.db.dbMySQL.MySQL.getDictCursorClass(self)



-------

.. _no-1836:

.. function:: dabo.db.dbMySQL.MySQL.getFields(self, tableName, cursor)



-------

.. _no-1839:

.. function:: dabo.db.dbMySQL.MySQL.getMainCursorClass(self)



-------

.. _no-1842:

.. function:: dabo.db.dbMySQL.MySQL.getTableRecordCount(self, tableName, cursor)



-------

.. _no-1843:

.. function:: dabo.db.dbMySQL.MySQL.getTables(self, cursor, includeSystemTables=False)



-------

.. _no-1846:

.. function:: dabo.db.dbMySQL.MySQL.getWordMatchFormat(self)

    MySQL's fulltext search expression



-------

.. _no-1860:

.. function:: dabo.db.dbMySQL.MySQL.rollbackTransaction(self, cursor)

    Rollback a SQL transaction.



-------


Methods - inherited
=====================

.. _no-1804:

.. function:: dabo.db.dbMySQL.MySQL.addField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a field to the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1805:

.. function:: dabo.db.dbMySQL.MySQL.addFrom(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Add a table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1806:

.. function:: dabo.db.dbMySQL.MySQL.addGroupBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the group-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1807:

.. function:: dabo.db.dbMySQL.MySQL.addJoin(self, tbl, joinCondition, exp, joinType=None, autoQuote=True)
   :noindex:


   Add a joined table to the sql statement.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1808:

.. function:: dabo.db.dbMySQL.MySQL.addOrderBy(self, clause, exp, autoQuote=True)
   :noindex:


   Add an expression to the order-by clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1809:

.. function:: dabo.db.dbMySQL.MySQL.addWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Add an expression to the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1810:

.. function:: dabo.db.dbMySQL.MySQL.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1811:

.. function:: dabo.db.dbMySQL.MySQL.autoBindEvents(self, force=True)
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

.. _no-1812:

.. function:: dabo.db.dbMySQL.MySQL.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1814:

.. function:: dabo.db.dbMySQL.MySQL.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1815:

.. function:: dabo.db.dbMySQL.MySQL.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1817:

.. function:: dabo.db.dbMySQL.MySQL.createJustIndexes(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1818:

.. function:: dabo.db.dbMySQL.MySQL.createJustTable(self, tabledef, cursor)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1820:

.. function:: dabo.db.dbMySQL.MySQL.encloseNames(self, exp, autoQuote=True, keywords=None)
   :noindex:


   
   When table/field names contain spaces, this will safely enclose them
   in quotes or whatever delimiter is appropriate for the backend, unless
   autoQuote is False, in which case it leaves things untouched. If there are
   keywords that are part of the expression that should not be enclosed
   within the field name, pass them as a tuple to the keywords parameter.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1822:

.. function:: dabo.db.dbMySQL.MySQL.flush(self, cursor)
   :noindex:


   Only used in some backends


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1823:

.. function:: dabo.db.dbMySQL.MySQL.formSQL(self, fieldClause, fromClause, joinClause, whereClause, groupByClause, orderByClause, limitClause)
   :noindex:


   
   Creates the appropriate SQL for the backend, given all
   the required clauses. Some backends order these differently, so
   they should override this method with their own ordering.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1824:

.. function:: dabo.db.dbMySQL.MySQL.formatBLOB(self, val)
   :noindex:


   
   Properly format a BLOB value to be included in an UPDATE
   or INSERT statement for a specific backend.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1826:

.. function:: dabo.db.dbMySQL.MySQL.formatForQuery(self, val, fieldType=None)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1827:

.. function:: dabo.db.dbMySQL.MySQL.formatJoinType(self, jt)
   :noindex:


   Default formatting for jointype keywords. Override in subclasses if needed.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1828:

.. function:: dabo.db.dbMySQL.MySQL.formatNone(self)
   :noindex:


   
   Properly format a None value to be included in an update statement.
   
   Each backend should override as needed. The default is to return "NULL".
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1829:

.. function:: dabo.db.dbMySQL.MySQL.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1831:

.. function:: dabo.db.dbMySQL.MySQL.getCursor(self, cursorClass)
   :noindex:


   override in subclasses if necessary


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1833:

.. function:: dabo.db.dbMySQL.MySQL.getDescription(self, cursor)
   :noindex:


   
   Normally, cursors should always be able to report their
   description properly. However, some backends such as
   SQLite will not report a description if there is no data in the
   record set. This method provides a way for those backends
   to deal with this. By default, though, just return the contents
   of the description attribute.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1835:

.. function:: dabo.db.dbMySQL.MySQL.getFieldInfoFromDescription(self, cursorDescription)
   :noindex:


   Return field information from the cursor description.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1837:

.. function:: dabo.db.dbMySQL.MySQL.getLastInsertID(self, cursor)
   :noindex:


   
   Return the ID of the last inserted row, or None.
   
   When inserting a new record in a table that auto-generates a PK
   value, different databases have their own way of retrieving that value.
   This method should be coded in backend-specific subclasses to address
   that database's approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1838:

.. function:: dabo.db.dbMySQL.MySQL.getLimitWord(self)
   :noindex:


   
   Return the word to use in the db-specific limit clause.
   Override for backends that don't use the word 'limit'
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1840:

.. function:: dabo.db.dbMySQL.MySQL.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1841:

.. function:: dabo.db.dbMySQL.MySQL.getStructureDescription(self, cursor)
   :noindex:


   Return the basic field structure.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1844:

.. function:: dabo.db.dbMySQL.MySQL.getUpdateTablePrefix(self, tbl, autoQuote=True)
   :noindex:


   
   By default, the update SQL statement will be in the form of
   
       tablename.fieldname
   
   but some backends do no accept this syntax. If not, change
   this method to return an empty string, or whatever should
   preceed the field name in an update statement.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1845:

.. function:: dabo.db.dbMySQL.MySQL.getWhereTablePrefix(self, tbl, autoQuote=True)
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

.. _no-1847:

.. function:: dabo.db.dbMySQL.MySQL.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1848:

.. function:: dabo.db.dbMySQL.MySQL.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1849:

.. function:: dabo.db.dbMySQL.MySQL.isExistingTable(self, table)
   :noindex:


   Returns whether or not the table exists.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1850:

.. function:: dabo.db.dbMySQL.MySQL.isValidModule(self)
   :noindex:


   Test the dbapi to see if it is supported on this computer.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1851:

.. function:: dabo.db.dbMySQL.MySQL.massageDescription(self, cursor)
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

.. _no-1852:

.. function:: dabo.db.dbMySQL.MySQL.noResultsOnDelete(self)
   :noindex:


   
   Most backends will return a non-zero number if there are deletions.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1853:

.. function:: dabo.db.dbMySQL.MySQL.noResultsOnSave(self)
   :noindex:


   
   Most backends will return a non-zero number if there are updates.
   Some do not, so this will have to be customized in those cases.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1854:

.. function:: dabo.db.dbMySQL.MySQL.pregenPK(self, cursor)
   :noindex:


   
   In the case where the database requires that PKs be generated
   before an insert, this method provides a backend-specific
   means of accomplishing this. By default, we return None.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1855:

.. function:: dabo.db.dbMySQL.MySQL.prepareWhere(self, clause, autoQuote=True)
   :noindex:


   
   Normally, just return the original. Can be overridden as needed
   for specific backends.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1856:

.. function:: dabo.db.dbMySQL.MySQL.processFields(self, txt)
   :noindex:


   
   Default is to return the string unchanged. Override
   in cases where the str needs processing.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1857:

.. function:: dabo.db.dbMySQL.MySQL.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1858:

.. function:: dabo.db.dbMySQL.MySQL.removeField(self, clause, exp, alias=None, autoQuote=True)
   :noindex:


   Remove a previously added field from the field clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1859:

.. function:: dabo.db.dbMySQL.MySQL.removeWhere(self, clause, exp, comp='and', autoQuote=True)
   :noindex:


   Remove a previously-added expression from the where clause.


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1861:

.. function:: dabo.db.dbMySQL.MySQL.setChildFilterClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1862:

.. function:: dabo.db.dbMySQL.MySQL.setFieldClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1863:

.. function:: dabo.db.dbMySQL.MySQL.setFromClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1864:

.. function:: dabo.db.dbMySQL.MySQL.setGroupByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1865:

.. function:: dabo.db.dbMySQL.MySQL.setJoinClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1866:

.. function:: dabo.db.dbMySQL.MySQL.setNonUpdateFields(self, cursor, autoQuote=True)
   :noindex:


   
   Normally, this routine should work for all backends. But
   in the case of SQLite, the routine that grabs an empty cursor
   doesn't fill in the description, so that backend has to use
   an alternative approach.
   


Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1867:

.. function:: dabo.db.dbMySQL.MySQL.setOrderByClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1868:

.. function:: dabo.db.dbMySQL.MySQL.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1869:

.. function:: dabo.db.dbMySQL.MySQL.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1870:

.. function:: dabo.db.dbMySQL.MySQL.setSQL(self, sql)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1871:

.. function:: dabo.db.dbMySQL.MySQL.setWhereClause(self, clause, autoQuote=True)
   :noindex:



Inherited from: :ref:`dabo.db.dBackend.dBackend`

-------

.. _no-1872:

.. function:: dabo.db.dbMySQL.MySQL.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1873:

.. function:: dabo.db.dbMySQL.MySQL.unbindEvent(self, eventClass=None, function=None)
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
