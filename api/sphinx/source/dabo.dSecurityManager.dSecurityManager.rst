
.. include:: _static/headings.txt

.. module:: dabo.dSecurityManager

.. _dabo.dSecurityManager.dSecurityManager:

==========================================================
|doc_title|  **dSecurityManager.dSecurityManager** - class
==========================================================

Class providing security services for Dabo applications, such as the
user logging in.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSecurityManager**

.. inheritance-diagram:: dSecurityManager


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.dSecurityManager.dSecurityManager


|method_summary| Properties Summary
===================================


================================== ========================
:ref:`Application <no-0>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-1>`            The base Dabo class of the object. Read-only.  (class)
:ref:`PreferenceManager <no-10>`   Reference to the Preference Management object  (dPref)
:ref:`RequireAppLogin <no-11>`     Specifies whether the user is required to login at app startup.
:ref:`UserCaption <no-12>`         The long descriptive name of the logged-on user.
:ref:`UserGroups <no-13>`          The tuple of groups that the user belongs to.
:ref:`UserName <no-14>`            The name of the logged-on user. Read-only.
:ref:`BasePrefKey <no-2>`          Base key used when saving/restoring preferences  (str)
:ref:`Class <no-3>`                The class the object is based on. Read-only.  (class)
:ref:`LogEvents <no-4>`            Specifies which events to log.  (list of strings)
:ref:`LoginAttemptsAllowed <no-5>` Specifies the number of attempts the user has to login successfully.
:ref:`LoginMessage <no-6>`         Specifies the message to initially display on the login form.
:ref:`LoginPause <no-7>`           Number of seconds to wait between successive login attempts.
:ref:`Name <no-8>`                 The name of the object.  (str)
:ref:`Parent <no-9>`               The containing object.  (obj)

================================== ========================


Properties
==========

.. _no-5:

**LoginAttemptsAllowed** 

Specifies the number of attempts the user has to login successfully.



-------

.. _no-6:

**LoginMessage** 

Specifies the message to initially display on the login form.



-------

.. _no-7:

**LoginPause** 

Number of seconds to wait between successive login attempts.



-------

.. _no-11:

**RequireAppLogin** 

Specifies whether the user is required to login at app startup.



-------

.. _no-12:

**UserCaption** 

The long descriptive name of the logged-on user.



-------

.. _no-13:

**UserGroups** 

The tuple of groups that the user belongs to.

Business objects can be configured to selectively allow/deny various types
of access based on the group(s) of the logged-in user.



-------

.. _no-14:

**UserName** 

The name of the logged-on user. Read-only.



-------


Properties - inherited
========================

.. _no-0:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-1:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10:

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


========================================= ========================
:ref:`afterInit <no-15>`                  Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterLoginFailure <no-16>`          Subclass hook called after an unsuccessful login attempt.
:ref:`afterLoginSuccess <no-17>`          Subclass hook called after a successful login.
:ref:`autoBindEvents <no-18>`             Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-19>`                 Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-20>`                  Bind a dEvent to a callback function.
:ref:`bindEvents <no-21>`                 Bind a sequence of [dEvent, callback] lists.
:ref:`getAbsoluteName <no-22>`            Return the fully qualified name of the object.
:ref:`getProperties <no-23>`              Returns a dictionary of property name/value pairs.
:ref:`getUserCaptionFromUserName <no-24>` Return a descriptive name of the user from the short userName.
:ref:`getUserGroupsFromUserName <no-25>`  Return the tuple of groups that userName belongs to.
:ref:`initEvents <no-26>`                 Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-27>`             Hook for subclasses. User subclasses should set properties
:ref:`login <no-28>`                      Ask the ui to display the login form to the user.
:ref:`raiseEvent <no-29>`                 Send the event to all registered listeners.
:ref:`setProperties <no-30>`              Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-31>`      Sets a group of properties on the object all at once. This
:ref:`super <no-32>`                      This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-33>`                Remove a previously registered event binding.
:ref:`validateLogin <no-34>`              Return True if the passed user and password combination is valid.

========================================= ========================


Methods
=======

.. _no-16:

.. function:: dabo.dSecurityManager.dSecurityManager.afterLoginFailure(self)

    Subclass hook called after an unsuccessful login attempt.



-------

.. _no-17:

.. function:: dabo.dSecurityManager.dSecurityManager.afterLoginSuccess(self)

    Subclass hook called after a successful login.



-------

.. _no-24:

.. function:: dabo.dSecurityManager.dSecurityManager.getUserCaptionFromUserName(self, userName)

    Return a descriptive name of the user from the short userName.
   
   This is a subclass hook: you should override this method with your own
   code that converts the short userName into something more descriptive,
   such as 'pmcnett' -> 'Paul McNett'. The default behavior just echoes
   back the userName.
   



-------

.. _no-25:

.. function:: dabo.dSecurityManager.dSecurityManager.getUserGroupsFromUserName(self, userName)

    Return the tuple of groups that userName belongs to.
   
   This is a subclass hook: you must override this method with your own
   code that returns a tuple filled with the groups the user belongs to.
   The identifiers used for the groups must match the group identifiers
   as coded in your business objects.
   



-------

.. _no-28:

.. function:: dabo.dSecurityManager.dSecurityManager.login(self)

   Ask the ui to display the login form to the user.
   
   Validate the results, and return True if validation succeeds.
   



-------

.. _no-34:

.. function:: dabo.dSecurityManager.dSecurityManager.validateLogin(self, user, password)

    Return True if the passed user and password combination is valid.
   
   This is a subclass hook: you must override this method with your own
   code that does whatever is required to verify the login info. This would
   probably include looking up the information in a database.
   



-------


Methods - inherited
=====================

.. _no-15:

.. function:: dabo.dSecurityManager.dSecurityManager.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18:

.. function:: dabo.dSecurityManager.dSecurityManager.autoBindEvents(self, force=True)
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

.. _no-19:

.. function:: dabo.dSecurityManager.dSecurityManager.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20:

.. function:: dabo.dSecurityManager.dSecurityManager.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21:

.. function:: dabo.dSecurityManager.dSecurityManager.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22:

.. function:: dabo.dSecurityManager.dSecurityManager.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23:

.. function:: dabo.dSecurityManager.dSecurityManager.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-26:

.. function:: dabo.dSecurityManager.dSecurityManager.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27:

.. function:: dabo.dSecurityManager.dSecurityManager.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29:

.. function:: dabo.dSecurityManager.dSecurityManager.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-30:

.. function:: dabo.dSecurityManager.dSecurityManager.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-31:

.. function:: dabo.dSecurityManager.dSecurityManager.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-32:

.. function:: dabo.dSecurityManager.dSecurityManager.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33:

.. function:: dabo.dSecurityManager.dSecurityManager.unbindEvent(self, eventClass=None, function=None)
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
