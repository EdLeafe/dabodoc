
.. include:: _static/headings.txt

.. module:: dabo.dObject

.. _dabo.dObject.dObject:

========================================
|doc_title|  **dObject.dObject** - class
========================================

The basic ancestor of all Dabo objects.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dObject**

.. inheritance-diagram:: dObject


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.eventMixin.EventMixin`
* :ref:`dabo.lib.propertyHelperMixin.PropertyHelperMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.biz.dBizobj.dBizobj`
* :ref:`dabo.dApp.dApp`
* :ref:`dabo.dReportWriter.dReportWriter`
* :ref:`dabo.dSecurityManager.dSecurityManager`
* :ref:`dabo.dUserSettingProvider.dUserSettingProvider`
* :ref:`dabo.db.dBackend.dBackend`
* :ref:`dabo.db.dConnectInfo.dConnectInfo`
* :ref:`dabo.db.dConnection.dConnection`
* :ref:`dabo.db.dCursorMixin.dCursorMixin`
* :ref:`dabo.db.dNoEscQuoteStr.dNoEscQuoteStr`
* :ref:`dabo.db.dTable.dField`
* :ref:`dabo.db.dTable.dIndex`
* :ref:`dabo.db.dTable.dTable`
* :ref:`dabo.db.dTable.fType`
* :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`
* :ref:`dabo.ui.uiwx.dFont.dFont`
* :ref:`dabo.ui.uiwx.dPemMixin.DrawObject`
* :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`
* :ref:`dabo.ui.uiwx.dToolBar.dToolBarItem`
* :ref:`dabo.ui.uiwx.dTreeView.dNode`
* :ref:`dabo.ui.uiwx.uiApp.uiApp`



|API| Class API
===============


.. autoclass:: dabo.dObject.dObject

   .. automethod:: dabo.dObject.dObject.__init__

|method_summary| Properties Summary
===================================


================================= ========================
:ref:`Application <no-215>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-216>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-217>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-218>`             The class the object is based on. Read-only.  (class)
:ref:`LogEvents <no-219>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-220>`              The name of the object.  (str)
:ref:`Parent <no-221>`            The containing object.  (obj)
:ref:`PreferenceManager <no-222>` Reference to the Preference Management object  (dPref)

================================= ========================


Properties
==========

.. _no-215:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).



-------

.. _no-216:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)



-------

.. _no-217:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)



-------

.. _no-218:

**Class** 

The class the object is based on. Read-only.  (class)



-------

.. _no-219:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    



-------

.. _no-220:

**Name** 

The name of the object.  (str)



-------

.. _no-221:

**Parent** 

The containing object.  (obj)



-------

.. _no-222:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)



-------


|method_summary| Events Summary
===============================


========== ========================

========== ========================


|method_summary| Methods Summary
================================


===================================== ========================
:ref:`afterInit <no-223>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-224>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-225>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-226>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-227>`            Bind a sequence of [dEvent, callback] lists.
:ref:`getAbsoluteName <no-228>`       Return the fully qualified name of the object.
:ref:`getProperties <no-229>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-230>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-231>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-232>`            Send the event to all registered listeners.
:ref:`setProperties <no-233>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-234>` Sets a group of properties on the object all at once. This
:ref:`super <no-235>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-236>`           Remove a previously registered event binding.

===================================== ========================


Methods
=======

.. _no-223:

.. function:: dabo.dObject.dObject.afterInit(self)

   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   



-------

.. _no-225:

.. function:: dabo.dObject.dObject.beforeInit(self, \*args, \**kwargs)

   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   



-------

.. _no-228:

.. function:: dabo.dObject.dObject.getAbsoluteName(self)

   Return the fully qualified name of the object.



-------

.. _no-230:

.. function:: dabo.dObject.dObject.initEvents(self)

   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   



-------

.. _no-231:

.. function:: dabo.dObject.dObject.initProperties(self)

   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   



-------

.. _no-235:

.. function:: dabo.dObject.dObject.super(self, \*args, \**kwargs)

   This method used to call superclass code, but it's been removed.



-------


Methods - inherited
=====================

.. _no-224:

.. function:: dabo.dObject.dObject.autoBindEvents(self, force=True)
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

.. _no-226:

.. function:: dabo.dObject.dObject.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-227:

.. function:: dabo.dObject.dObject.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-229:

.. function:: dabo.dObject.dObject.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-232:

.. function:: dabo.dObject.dObject.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-233:

.. function:: dabo.dObject.dObject.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-234:

.. function:: dabo.dObject.dObject.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-236:

.. function:: dabo.dObject.dObject.unbindEvent(self, eventClass=None, function=None)
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
