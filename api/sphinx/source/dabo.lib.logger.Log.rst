
.. include:: _static/headings.txt

.. module:: dabo.lib.logger

.. _dabo.lib.logger.Log:

===================================
|doc_title|  **logger.Log** - class
===================================

Generic logger object for Dabo.

The main dabo module will instantiate singleton instances of this, which
custom code can override to redirect the writing of informational and error
messages.

So, to display general informational messages, call:
dabo.log.info("message")

For error messages, call:
dabo.log.error("message")

By default, infoLog writes to stdout and errorLog to stderr. But your code
can redirect these messages however you please. Just set the LogObject property
to an instance that has a write() method that will receive and act on the
message. For example, you can redirect to a file:

dabo.errorLog.LogObject = open("/tmp/error.log", "w")
dabo.infoLog.LogObject = open("/dev/null", "w")

You can set the logs to arbitrary objects. As long as the object has a write()
method that receives a message parameter, it will work.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Log**

.. inheritance-diagram:: Log


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.lib.logger.Log


|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-2442>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-2443>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-2444>`       Base key used when saving/restoring preferences  (str)
:ref:`Caption <no-2445>`           The log's label: will get prepended to the log entry
:ref:`Class <no-2446>`             The class the object is based on. Read-only.  (class)
:ref:`LogEvents <no-2447>`         Specifies which events to log.  (list of strings)
:ref:`LogObject <no-2448>`         The object that is to receive the log messages.
:ref:`LogTimeStamp <no-2449>`      Specifies whether a timestamp is logged with the message. Default: True
:ref:`Name <no-2450>`              The name of the object.  (str)
:ref:`Parent <no-2451>`            The containing object.  (obj)
:ref:`PreferenceManager <no-2452>` Reference to the Preference Management object  (dPref)

================================== ========================


Properties
==========

.. _no-2445:

**Caption** 

The log's label: will get prepended to the log entry



-------

.. _no-2448:

**LogObject** 

The object that is to receive the log messages.



-------

.. _no-2449:

**LogTimeStamp** 

Specifies whether a timestamp is logged with the message. Default: True



-------


Properties - inherited
========================

.. _no-2442:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2443:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2444:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2446:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2447:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2450:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2451:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2452:

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
:ref:`afterInit <no-2453>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-2454>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-2455>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-2456>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-2457>`            Bind a sequence of [dEvent, callback] lists.
:ref:`getAbsoluteName <no-2458>`       Return the fully qualified name of the object.
:ref:`getProperties <no-2459>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-2460>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-2461>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-2462>`            Send the event to all registered listeners.
:ref:`setProperties <no-2463>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-2464>` Sets a group of properties on the object all at once. This
:ref:`super <no-2465>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-2466>`           Remove a previously registered event binding.
:ref:`write <no-2467>`                 Writes the passed message to the log.

====================================== ========================


Methods
=======

.. _no-2467:

.. function:: dabo.lib.logger.Log.write(self, message)

   Writes the passed message to the log.



-------


Methods - inherited
=====================

.. _no-2453:

.. function:: dabo.lib.logger.Log.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2454:

.. function:: dabo.lib.logger.Log.autoBindEvents(self, force=True)
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

.. _no-2455:

.. function:: dabo.lib.logger.Log.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2456:

.. function:: dabo.lib.logger.Log.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2457:

.. function:: dabo.lib.logger.Log.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2458:

.. function:: dabo.lib.logger.Log.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2459:

.. function:: dabo.lib.logger.Log.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-2460:

.. function:: dabo.lib.logger.Log.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2461:

.. function:: dabo.lib.logger.Log.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2462:

.. function:: dabo.lib.logger.Log.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-2463:

.. function:: dabo.lib.logger.Log.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-2464:

.. function:: dabo.lib.logger.Log.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-2465:

.. function:: dabo.lib.logger.Log.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2466:

.. function:: dabo.lib.logger.Log.unbindEvent(self, eventClass=None, function=None)
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
