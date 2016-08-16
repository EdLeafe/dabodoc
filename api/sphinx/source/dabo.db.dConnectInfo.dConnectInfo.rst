
.. include:: _static/headings.txt

.. module:: dabo.db.dConnectInfo

.. _dabo.db.dConnectInfo.dConnectInfo:

==================================================
|doc_title|  **dConnectInfo.dConnectInfo** - class
==================================================


Holder for the properties for connecting to the backend. Each
backend may have different names for properties, but this object
tries to abstract that. The value stored in the Password must be
encrypted in the format set in the app. This class has  'encrypt' and
'decrypt' functions for doing this, or you can set the PlainTextPassword
property, and the class will encypt that value and set the Password
property for you.

You can create it in several ways, like most Dabo objects. First, you
can pass all the settings as parameters to the constructor::

        ci = dConnectInfo(DbType="MySQL", Host="domain.com",
            User="daboUser", PlainTextPassword="secret", Port=3306,
            Database="myData", Name="mainConnection")

    Or you can create a dictionary of the various props, and pass that
    in the 'connInfo' parameter::

        connDict = {"DbType" : "MySQL", "Host" : "domain.com",
            "User" : "daboUser", "PlainTextPassword" : "secret",
            "Port" : 3306, "Database" : "myData", "Name" : "mainConnection"}
        ci = dConnectInfo(connInfo=connDict)

    Or you can create the object and then set the props
    individually::

        ci = dConnectInfo()
        ci.DbType = "MySQL"
        ci.Host = "domain.com"
        ci.User = "daboUser"
        ci.PlainTextPassword = "secret"
        ci.Database = "myData"
        ci.Name = "mainConnection"

    If you are running a remote app, should set the RemoteHost property instead of Host. The
    DbType will be "web".
    



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dConnectInfo**

.. inheritance-diagram:: dConnectInfo


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.db.dConnectInfo.dConnectInfo

   .. automethod:: dabo.db.dConnectInfo.dConnectInfo.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1480>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1481>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1482>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1483>`             The class the object is based on. Read-only.  (class)
:ref:`Crypto <no-1484>`            Reference to the object that provides cryptographic services if run
:ref:`CustomParameters <no-1485>`  Additional parameters passed to backend object connect method. (dict)
:ref:`Database <no-1486>`          The database name to login to. (str)
:ref:`DbType <no-1487>`            Name of the backend database type.  (str)
:ref:`Host <no-1488>`              The host name or ip address. (str)
:ref:`KeepAliveInterval <no-1489>` Specifies how often a KeepAlive query should be sent to the server. (int)
:ref:`LogEvents <no-1490>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1491>`              The name used to reference this connection. (str)
:ref:`Parent <no-1492>`            The containing object.  (obj)
:ref:`Password <no-1493>`          The encrypted password of the user. (str)
:ref:`PlainTextPassword <no-1494>` Write-only property that encrypts the value and stores that
:ref:`Port <no-1495>`              The port to connect on (may not be applicable for all databases). (int)
:ref:`PreferenceManager <no-1496>` Reference to the Preference Management object  (dPref)
:ref:`RemoteHost <no-1497>`        When running as a web app, this holds the host URL. (str)
:ref:`User <no-1498>`              The user name. (str)

================================== ========================


Properties
==========

.. _no-1484:

**Crypto** 

Reference to the object that provides cryptographic services if run
    outside of an application.  (varies)



-------

.. _no-1485:

**CustomParameters** 

Additional parameters passed to backend object connect method. (dict)



-------

.. _no-1486:

**Database** 

The database name to login to. (str)



-------

.. _no-1487:

**DbType** 

Name of the backend database type.  (str)



-------

.. _no-1488:

**Host** 

The host name or ip address. (str)



-------

.. _no-1489:

**KeepAliveInterval** 

Specifies how often a KeepAlive query should be sent to the server. (int)

    Defaults to None, meaning we never send a KeepAlive query. The interval
    is expressed in seconds.
    



-------

.. _no-1493:

**Password** 

The encrypted password of the user. (str)



-------

.. _no-1494:

**PlainTextPassword** 

Write-only property that encrypts the value and stores that
        in the Password property. (str)



-------

.. _no-1495:

**Port** 

The port to connect on (may not be applicable for all databases). (int)



-------

.. _no-1497:

**RemoteHost** 

When running as a web app, this holds the host URL. (str)



-------

.. _no-1498:

**User** 

The user name. (str)



-------


Properties - inherited
========================

.. _no-1480:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1481:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1482:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1483:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1490:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1491:

**Name** 

The name used to reference this connection. (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1492:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1496:

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


====================================== ========================
:ref:`afterInit <no-1499>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1500>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1501>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-1502>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-1503>`            Bind a sequence of [dEvent, callback] lists.
:ref:`decrypt <no-1504>`               
:ref:`encrypt <no-1505>`               
:ref:`getAbsoluteName <no-1506>`       Return the fully qualified name of the object.
:ref:`getBackendObject <no-1507>`      
:ref:`getConnection <no-1508>`         
:ref:`getDictCursorClass <no-1509>`    
:ref:`getMainCursorClass <no-1510>`    
:ref:`getProperties <no-1511>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-1512>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1513>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-1514>`            Send the event to all registered listeners.
:ref:`revealPW <no-1515>`              
:ref:`setConnInfo <no-1516>`           
:ref:`setProperties <no-1517>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1518>` Sets a group of properties on the object all at once. This
:ref:`super <no-1519>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1520>`           Remove a previously registered event binding.

====================================== ========================


Methods
=======

.. _no-1504:

.. function:: dabo.db.dConnectInfo.dConnectInfo.decrypt(self, val)



-------

.. _no-1505:

.. function:: dabo.db.dConnectInfo.dConnectInfo.encrypt(self, val)



-------

.. _no-1507:

.. function:: dabo.db.dConnectInfo.dConnectInfo.getBackendObject(self)



-------

.. _no-1508:

.. function:: dabo.db.dConnectInfo.dConnectInfo.getConnection(self, \**kwargs)



-------

.. _no-1509:

.. function:: dabo.db.dConnectInfo.dConnectInfo.getDictCursorClass(self)



-------

.. _no-1510:

.. function:: dabo.db.dConnectInfo.dConnectInfo.getMainCursorClass(self)



-------

.. _no-1515:

.. function:: dabo.db.dConnectInfo.dConnectInfo.revealPW(self)



-------

.. _no-1516:

.. function:: dabo.db.dConnectInfo.dConnectInfo.setConnInfo(self, connInfo, nm='')



-------


Methods - inherited
=====================

.. _no-1499:

.. function:: dabo.db.dConnectInfo.dConnectInfo.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1500:

.. function:: dabo.db.dConnectInfo.dConnectInfo.autoBindEvents(self, force=True)
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

.. _no-1501:

.. function:: dabo.db.dConnectInfo.dConnectInfo.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1502:

.. function:: dabo.db.dConnectInfo.dConnectInfo.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1503:

.. function:: dabo.db.dConnectInfo.dConnectInfo.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1506:

.. function:: dabo.db.dConnectInfo.dConnectInfo.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1511:

.. function:: dabo.db.dConnectInfo.dConnectInfo.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1512:

.. function:: dabo.db.dConnectInfo.dConnectInfo.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1513:

.. function:: dabo.db.dConnectInfo.dConnectInfo.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1514:

.. function:: dabo.db.dConnectInfo.dConnectInfo.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1517:

.. function:: dabo.db.dConnectInfo.dConnectInfo.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1518:

.. function:: dabo.db.dConnectInfo.dConnectInfo.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1519:

.. function:: dabo.db.dConnectInfo.dConnectInfo.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1520:

.. function:: dabo.db.dConnectInfo.dConnectInfo.unbindEvent(self, eventClass=None, function=None)
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
