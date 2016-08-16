
.. include:: _static/headings.txt

.. module:: dabo.ui.dPemMixinBase

.. _dabo.ui.dPemMixinBase.dPemMixinBase:

====================================================
|doc_title|  **dPemMixinBase.dPemMixinBase** - class
====================================================


Provide Property/Event/Method interfaces for dForms and dControls.

Subclasses can extend the property sheet by defining their own get/set
functions along with their own property() statements.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPemMixinBase**

.. inheritance-diagram:: dPemMixinBase


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dGrid.dColumn`
* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.dPemMixinBase.dPemMixinBase


|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-6321>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-6322>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-6323>`       Base key used when saving/restoring preferences  (str)
:ref:`Bottom <no-6324>`            The position of the bottom side of the object. This is a
:ref:`Children <no-6325>`          List of child objects.
:ref:`Class <no-6326>`             The class the object is based on. Read-only.  (class)
:ref:`Form <no-6327>`              Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`LogEvents <no-6328>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-6329>`              The name of the object.  (str)
:ref:`Parent <no-6330>`            The containing object.  (obj)
:ref:`PreferenceManager <no-6331>` Reference to the Preference Management object  (dPref)
:ref:`Right <no-6332>`             The position of the right side of the object. This is a

================================== ========================


Properties
==========

.. _no-6324:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)



-------

.. _no-6325:

**Children** 

List of child objects.



-------

.. _no-6327:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).



-------

.. _no-6332:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)



-------


Properties - inherited
========================

.. _no-6321:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6322:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6323:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6326:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6328:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6329:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6330:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6331:

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
:ref:`addObject <no-6333>`             Create an instance of classRef, and make it a child of self.
:ref:`afterInit <no-6334>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-6335>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-6336>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-6337>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-6338>`            Bind a sequence of [dEvent, callback] lists.
:ref:`clone <no-6339>`                 Abstract method: subclasses MUST override for UI-specifics.
:ref:`fontZoomIn <no-6340>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-6341>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-6342>`           Zoom out on the font, by setting a lower point size.
:ref:`getAbsoluteName <no-6343>`       Return the fully qualified name of the object.
:ref:`getProperties <no-6344>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-6345>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-6346>`        Hook for subclasses. User subclasses should set properties
:ref:`iterateCall <no-6347>`           Call the given function on this object and all of its Children. If
:ref:`raiseEvent <no-6348>`            Send the event to all registered listeners.
:ref:`reCreate <no-6349>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`refresh <no-6350>`               Abstract method.
:ref:`setProperties <no-6351>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-6352>` Sets a group of properties on the object all at once. This
:ref:`super <no-6353>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-6354>`           Remove a previously registered event binding.

====================================== ========================


Methods
=======

.. _no-6333:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.addObject(self, classRef, Name=None, \*args, \**kwargs)

   
   Create an instance of classRef, and make it a child of self.
   
   Abstract method: subclasses MUST override for UI-specifics.
   



-------

.. _no-6339:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.clone(self, obj, name=None)

   Abstract method: subclasses MUST override for UI-specifics.



-------

.. _no-6340:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.fontZoomIn(self, amt=1)

   Zoom in on the font, by setting a higher point size.



-------

.. _no-6341:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.fontZoomNormal(self)

   Reset the font zoom back to zero.



-------

.. _no-6342:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.fontZoomOut(self, amt=1)

   Zoom out on the font, by setting a lower point size.



-------

.. _no-6347:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.iterateCall(self, funcName, \*args, \**kwargs)

   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   



-------

.. _no-6349:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.reCreate(self, child=None)

   Abstract method: subclasses MUST override for UI-specifics.



-------

.. _no-6350:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.refresh(self)

   Abstract method.



-------


Methods - inherited
=====================

.. _no-6334:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6335:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.autoBindEvents(self, force=True)
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

.. _no-6336:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6337:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6338:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6343:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6344:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-6345:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6346:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6348:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-6351:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-6352:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-6353:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6354:

.. function:: dabo.ui.dPemMixinBase.dPemMixinBase.unbindEvent(self, eventClass=None, function=None)
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
