
.. include:: _static/headings.txt

.. module:: dabo.dUserSettingProvider

.. _dabo.dUserSettingProvider.dUserSettingProvider:

==================================================================
|doc_title|  **dUserSettingProvider.dUserSettingProvider** - class
==================================================================


Class that manages saving and restoring user settings, such as form
size and position.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dUserSettingProvider**

.. inheritance-diagram:: dUserSettingProvider


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.dUserSettingProvider.dUserSettingProvider


|method_summary| Properties Summary
===================================


================================= ========================
:ref:`Application <no-237>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-238>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-239>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-240>`             The class the object is based on. Read-only.  (class)
:ref:`LogEvents <no-241>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-242>`              The name of the object.  (str)
:ref:`Parent <no-243>`            The containing object.  (obj)
:ref:`PreferenceManager <no-244>` Reference to the Preference Management object  (dPref)

================================= ========================


Properties - inherited
========================

.. _no-237:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-238:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-239:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-240:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-241:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-242:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-243:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-244:

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
:ref:`afterInit <no-245>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-246>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-247>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-248>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-249>`            Bind a sequence of [dEvent, callback] lists.
:ref:`deleteAllUserSettings <no-250>` Given a spec, deletes all keys that match that spec.
:ref:`deleteUserSetting <no-251>`     Removes the specified item from the settings file.
:ref:`getAbsoluteName <no-252>`       Return the fully qualified name of the object.
:ref:`getProperties <no-253>`         Returns a dictionary of property name/value pairs.
:ref:`getUserSetting <no-254>`        Return the value of the user settings table that
:ref:`getUserSettingKeys <no-255>`    Return a list of all keys underneath <spec>.
:ref:`initEvents <no-256>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-257>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-258>`            Send the event to all registered listeners.
:ref:`setProperties <no-259>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-260>` Sets a group of properties on the object all at once. This
:ref:`setUserSetting <no-261>`        Persist a value to the user settings file.
:ref:`setUserSettings <no-262>`       Persist a set of setting name: value pairs.
:ref:`super <no-263>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-264>`           Remove a previously registered event binding.

===================================== ========================


Methods
=======

.. _no-250:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.deleteAllUserSettings(self, spec)

   
   Given a spec, deletes all keys that match that spec.
   See the docs for getUserSettingKeys() for an explanation
   on key matching.
   



-------

.. _no-251:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.deleteUserSetting(self, item)

   Removes the specified item from the settings file.



-------

.. _no-254:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.getUserSetting(self, item, default=None)

   
   Return the value of the user settings table that
   corresponds to the preference key passed.
   



-------

.. _no-255:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.getUserSettingKeys(self, spec)

   
   Return a list of all keys underneath <spec>.
   
   For example, if spec is "appWizard.dbDefaults", and there are
   userSettings entries for:
   
       appWizard.dbDefaults.pkm.Host
       appWizard.dbDefaults.pkm.User
       appWizard.dbDefaults.egl.Host
   
   The return value would be ["pkm", "egl"]
   



-------

.. _no-261:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.setUserSetting(self, item, val)

   Persist a value to the user settings file.



-------

.. _no-262:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.setUserSettings(self, dct)

   Persist a set of setting name: value pairs.



-------


Methods - inherited
=====================

.. _no-245:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-246:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.autoBindEvents(self, force=True)
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

.. _no-247:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-248:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-249:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-252:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-253:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-256:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-257:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-258:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-259:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-260:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-263:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-264:

.. function:: dabo.dUserSettingProvider.dUserSettingProvider.unbindEvent(self, eventClass=None, function=None)
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
