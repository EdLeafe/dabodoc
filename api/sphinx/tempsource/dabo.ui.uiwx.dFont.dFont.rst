
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dFont

.. _dabo.ui.uiwx.dFont.dFont:

====================================
|doc_title|  **dFont.dFont** - class
====================================

This class wraps the various font properties into a single object.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dFont**

.. inheritance-diagram:: dFont


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dFont.dFont

   .. automethod:: dabo.ui.uiwx.dFont.dFont.__init__

|method_summary| Properties Summary
===================================


=================================== ========================
:ref:`Application <no-24994>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-24995>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-24996>`       Base key used when saving/restoring preferences  (str)
:ref:`Bold <no-24997>`              Bold setting for this font  (bool)
:ref:`Class <no-24998>`             The class the object is based on. Read-only.  (class)
:ref:`Description <no-24999>`       Read-only plain text description of the font  (str)
:ref:`Face <no-25000>`              Name of the font face  (str)
:ref:`FontBold <no-25001>`          Bold setting for this font  (bool)
:ref:`FontFace <no-25002>`          Name of the font face  (str)
:ref:`FontItalic <no-25003>`        Italic setting for this font  (bool)
:ref:`FontSize <no-25004>`          Size in points for this font  (int)
:ref:`FontUnderline <no-25005>`     Underline setting for this font  (bool)
:ref:`Italic <no-25006>`            Italic setting for this font  (bool)
:ref:`LogEvents <no-25007>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-25008>`              The name of the object.  (str)
:ref:`Parent <no-25009>`            The containing object.  (obj)
:ref:`PreferenceManager <no-25010>` Reference to the Preference Management object  (dPref)
:ref:`Size <no-25011>`              Size in points for this font  (int)
:ref:`Underline <no-25012>`         Underline setting for this font  (bool)

=================================== ========================


Properties
==========

.. _no-24997:

**Bold** 

Bold setting for this font  (bool)



-------

.. _no-24999:

**Description** 

Read-only plain text description of the font  (str)



-------

.. _no-25000:

**Face** 

Name of the font face  (str)



-------

.. _no-25001:

**FontBold** 

Bold setting for this font  (bool)



-------

.. _no-25002:

**FontFace** 

Name of the font face  (str)



-------

.. _no-25003:

**FontItalic** 

Italic setting for this font  (bool)



-------

.. _no-25004:

**FontSize** 

Size in points for this font  (int)



-------

.. _no-25005:

**FontUnderline** 

Underline setting for this font  (bool)



-------

.. _no-25006:

**Italic** 

Italic setting for this font  (bool)



-------

.. _no-25011:

**Size** 

Size in points for this font  (int)



-------

.. _no-25012:

**Underline** 

Underline setting for this font  (bool)



-------


Properties - inherited
========================

.. _no-24994:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24995:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24996:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24998:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25007:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25008:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25009:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25010:

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


======================================= ========================
:ref:`afterInit <no-25013>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-25014>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-25015>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-25016>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-25017>`            Bind a sequence of [dEvent, callback] lists.
:ref:`getAbsoluteName <no-25018>`       Return the fully qualified name of the object.
:ref:`getProperties <no-25019>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-25020>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-25021>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-25022>`            Send the event to all registered listeners.
:ref:`setProperties <no-25023>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-25024>` Sets a group of properties on the object all at once. This
:ref:`super <no-25025>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-25026>`           Remove a previously registered event binding.

======================================= ========================


Methods - inherited
=====================

.. _no-25013:

.. function:: dabo.ui.uiwx.dFont.dFont.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25014:

.. function:: dabo.ui.uiwx.dFont.dFont.autoBindEvents(self, force=True)
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

.. _no-25015:

.. function:: dabo.ui.uiwx.dFont.dFont.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25016:

.. function:: dabo.ui.uiwx.dFont.dFont.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25017:

.. function:: dabo.ui.uiwx.dFont.dFont.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25018:

.. function:: dabo.ui.uiwx.dFont.dFont.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25019:

.. function:: dabo.ui.uiwx.dFont.dFont.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-25020:

.. function:: dabo.ui.uiwx.dFont.dFont.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25021:

.. function:: dabo.ui.uiwx.dFont.dFont.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25022:

.. function:: dabo.ui.uiwx.dFont.dFont.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-25023:

.. function:: dabo.ui.uiwx.dFont.dFont.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-25024:

.. function:: dabo.ui.uiwx.dFont.dFont.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-25025:

.. function:: dabo.ui.uiwx.dFont.dFont.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25026:

.. function:: dabo.ui.uiwx.dFont.dFont.unbindEvent(self, eventClass=None, function=None)
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
