
.. include:: _static/headings.txt

.. module:: dabo.db.dConnection

.. _dabo.db.dConnection.dConnection:

================================================
|doc_title|  **dConnection.dConnection** - class
================================================

Hold a connection to a backend database.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dConnection**

.. inheritance-diagram:: dConnection


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.db.dConnection.dConnection

   .. automethod:: dabo.db.dConnection.dConnection.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1682>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1683>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1684>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1685>`             The class the object is based on. Read-only.  (class)
:ref:`ConnectInfo <no-1686>`       The connectInfo for the connection.  (dConnectInfo)
:ref:`LogEvents <no-1687>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1688>`              The name of the connection.  (str)
:ref:`Parent <no-1689>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1690>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties
==========

.. _no-1686:

**ConnectInfo** 

The connectInfo for the connection.  (dConnectInfo)



-------


Properties - inherited
========================

.. _no-1682:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1683:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1684:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1685:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1687:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1688:

**Name** 

The name of the connection.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1689:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1690:

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
:ref:`afterInit <no-1691>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1692>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1693>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-1694>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-1695>`            Bind a sequence of [dEvent, callback] lists.
:ref:`close <no-1696>`                 
:ref:`cursor <no-1697>`                Accepts a backend-specific cursor class, mixes in the Dabo
:ref:`getAbsoluteName <no-1698>`       Return the fully qualified name of the object.
:ref:`getBackendObject <no-1699>`      Return a reference to the connectInfo's backend-specific
:ref:`getConnection <no-1700>`         
:ref:`getCursor <no-1701>`             
:ref:`getDaboCursor <no-1702>`         Accepts a backend-specific cursor class, mixes in the Dabo
:ref:`getDictCursorClass <no-1703>`    
:ref:`getMainCursorClass <no-1704>`    
:ref:`getProperties <no-1705>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-1706>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1707>`        Hook for subclasses. User subclasses should set properties
:ref:`isRemote <no-1708>`              Returns True or False, depending on whether a RemoteHost is
:ref:`raiseEvent <no-1709>`            Send the event to all registered listeners.
:ref:`setProperties <no-1710>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1711>` Sets a group of properties on the object all at once. This
:ref:`super <no-1712>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1713>`           Remove a previously registered event binding.

====================================== ========================


Methods
=======

.. _no-1696:

.. function:: dabo.db.dConnection.dConnection.close(self)



-------

.. _no-1697:

.. function:: dabo.db.dConnection.dConnection.cursor(self, cursorClass=None)

   
   Accepts a backend-specific cursor class, mixes in the Dabo
   dCursorMixin class, and returns the result.
   



-------

.. _no-1699:

.. function:: dabo.db.dConnection.dConnection.getBackendObject(self)

   
   Return a reference to the connectInfo's backend-specific
   database object.
   



-------

.. _no-1700:

.. function:: dabo.db.dConnection.dConnection.getConnection(self)



-------

.. _no-1701:

.. function:: dabo.db.dConnection.dConnection.getCursor(self, cursorClass)



-------

.. _no-1702:

.. function:: dabo.db.dConnection.dConnection.getDaboCursor(self, cursorClass=None)

   
   Accepts a backend-specific cursor class, mixes in the Dabo
   dCursorMixin class, and returns the result.
   



-------

.. _no-1703:

.. function:: dabo.db.dConnection.dConnection.getDictCursorClass(self)



-------

.. _no-1704:

.. function:: dabo.db.dConnection.dConnection.getMainCursorClass(self)



-------

.. _no-1708:

.. function:: dabo.db.dConnection.dConnection.isRemote(self)

   
   Returns True or False, depending on whether a RemoteHost is
   specified in this connection.
   



-------


Methods - inherited
=====================

.. _no-1691:

.. function:: dabo.db.dConnection.dConnection.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1692:

.. function:: dabo.db.dConnection.dConnection.autoBindEvents(self, force=True)
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

.. _no-1693:

.. function:: dabo.db.dConnection.dConnection.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1694:

.. function:: dabo.db.dConnection.dConnection.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1695:

.. function:: dabo.db.dConnection.dConnection.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1698:

.. function:: dabo.db.dConnection.dConnection.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1705:

.. function:: dabo.db.dConnection.dConnection.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1706:

.. function:: dabo.db.dConnection.dConnection.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1707:

.. function:: dabo.db.dConnection.dConnection.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1709:

.. function:: dabo.db.dConnection.dConnection.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1710:

.. function:: dabo.db.dConnection.dConnection.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1711:

.. function:: dabo.db.dConnection.dConnection.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1712:

.. function:: dabo.db.dConnection.dConnection.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1713:

.. function:: dabo.db.dConnection.dConnection.unbindEvent(self, eventClass=None, function=None)
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
