
.. include:: _static/headings.txt

.. module:: dabo.db.dNoEscQuoteStr

.. _dabo.db.dNoEscQuoteStr.dNoEscQuoteStr:

======================================================
|doc_title|  **dNoEscQuoteStr.dNoEscQuoteStr** - class
======================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dNoEscQuoteStr**

.. inheritance-diagram:: dNoEscQuoteStr


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr

   .. automethod:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.__init__

|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-1057>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1058>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-1059>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-1060>`             The class the object is based on. Read-only.  (class)
:ref:`LogEvents <no-1061>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-1062>`              The name of the object.  (str)
:ref:`Parent <no-1063>`            The containing object.  (obj)
:ref:`PreferenceManager <no-1064>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties - inherited
========================

.. _no-1057:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1058:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1059:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1060:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1061:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1062:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1063:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1064:

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
:ref:`afterInit <no-1065>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-1066>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-1067>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-1068>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-1069>`            Bind a sequence of [dEvent, callback] lists.
:ref:`getAbsoluteName <no-1070>`       Return the fully qualified name of the object.
:ref:`getProperties <no-1071>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-1072>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-1073>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-1074>`            Send the event to all registered listeners.
:ref:`setProperties <no-1075>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-1076>` Sets a group of properties on the object all at once. This
:ref:`super <no-1077>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-1078>`           Remove a previously registered event binding.

====================================== ========================


Methods - inherited
=====================

.. _no-1065:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1066:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.autoBindEvents(self, force=True)
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

.. _no-1067:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1068:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1069:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-1070:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1071:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-1072:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1073:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1074:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-1075:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-1076:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-1077:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1078:

.. function:: dabo.db.dNoEscQuoteStr.dNoEscQuoteStr.unbindEvent(self, eventClass=None, function=None)
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
