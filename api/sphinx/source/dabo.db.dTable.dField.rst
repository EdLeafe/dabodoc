
.. include:: _static/headings.txt

.. module:: dabo.db.dTable

.. _dabo.db.dTable.dField:

======================================
|doc_title|  **dTable.dField** - class
======================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dField**

.. inheritance-diagram:: dField


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.db.dTable.dField

   .. automethod:: dabo.db.dTable.dField.__init__

|method_summary| Properties Summary
===================================


================================= ========================
:ref:`AllowNulls <no-949>`        Whether or not nulls are allowed. Default:True (bool)
:ref:`Application <no-950>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-951>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-952>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-953>`             The class the object is based on. Read-only.  (class)
:ref:`DataType <no-954>`          The type of the column. (str)
:ref:`Default <no-955>`           The default value for the field. Default:None (str)
:ref:`IsAutoIncrement <no-956>`   Whether or not the field is an auto incrementing field.
:ref:`IsPK <no-957>`              Whether or not the field has the primary key. (bool)
:ref:`LogEvents <no-958>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-959>`              The name of the table. (str)
:ref:`Parent <no-960>`            The containing object.  (obj)
:ref:`PreferenceManager <no-961>` Reference to the Preference Management object  (dPref)
:ref:`RightDP <no-962>`           The number of decimal places to the right
:ref:`Size <no-963>`              The size required for the column in bytes or character units if it's a string. (int)
:ref:`TotalDP <no-964>`           The total number of decimal places  (int)
:ref:`Type <no-965>`              The type of the column.  (class)

================================= ========================


Properties
==========

.. _no-949:

**AllowNulls** 

Whether or not nulls are allowed. Default:True (bool)



-------

.. _no-954:

**DataType** 

The type of the column. (str)



-------

.. _no-955:

**Default** 

The default value for the field. Default:None (str)



-------

.. _no-956:

**IsAutoIncrement** 

Whether or not the field is an auto incrementing field.
    Default:False  (bool)



-------

.. _no-957:

**IsPK** 

Whether or not the field has the primary key. (bool)



-------

.. _no-962:

**RightDP** 

The number of decimal places to the right
    of the period.  (int)



-------

.. _no-963:

**Size** 

The size required for the column in bytes or character units if it's a string. (int)



-------

.. _no-964:

**TotalDP** 

The total number of decimal places  (int)



-------

.. _no-965:

**Type** 

The type of the column.  (class)



-------


Properties - inherited
========================

.. _no-950:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-951:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-952:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-953:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-958:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-959:

**Name** 

The name of the table. (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-960:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-961:

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


===================================== ========================
:ref:`afterInit <no-966>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-967>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-968>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-969>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-970>`            Bind a sequence of [dEvent, callback] lists.
:ref:`getAbsoluteName <no-971>`       Return the fully qualified name of the object.
:ref:`getProperties <no-972>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-973>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-974>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-975>`            Send the event to all registered listeners.
:ref:`setProperties <no-976>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-977>` Sets a group of properties on the object all at once. This
:ref:`super <no-978>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-979>`           Remove a previously registered event binding.

===================================== ========================


Methods - inherited
=====================

.. _no-966:

.. function:: dabo.db.dTable.dField.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-967:

.. function:: dabo.db.dTable.dField.autoBindEvents(self, force=True)
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

.. _no-968:

.. function:: dabo.db.dTable.dField.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-969:

.. function:: dabo.db.dTable.dField.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-970:

.. function:: dabo.db.dTable.dField.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-971:

.. function:: dabo.db.dTable.dField.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-972:

.. function:: dabo.db.dTable.dField.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-973:

.. function:: dabo.db.dTable.dField.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-974:

.. function:: dabo.db.dTable.dField.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-975:

.. function:: dabo.db.dTable.dField.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-976:

.. function:: dabo.db.dTable.dField.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-977:

.. function:: dabo.db.dTable.dField.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-978:

.. function:: dabo.db.dTable.dField.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-979:

.. function:: dabo.db.dTable.dField.unbindEvent(self, eventClass=None, function=None)
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
