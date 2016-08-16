
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.uiApp

.. _dabo.ui.uiwx.uiApp.uiApp:

====================================
|doc_title|  **uiApp.uiApp** - class
====================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **uiApp**

.. inheritance-diagram:: uiApp


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.uiApp.uiApp

   .. automethod:: dabo.ui.uiwx.uiApp.uiApp.__init__

|method_summary| Properties Summary
===================================


======================================= ========================
:ref:`ActiveForm <no-13236>`            Returns the form that currently has focus, or None.(dForm)
:ref:`Application <no-13237>`           Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-13238>`             The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-13239>`           Base key used when saving/restoring preferences  (str)
:ref:`Class <no-13240>`                 The class the object is based on. Read-only.  (class)
:ref:`DrawSizerOutlines <no-13241>`     Determines if sizer outlines are drawn on the ActiveForm.  (bool)
:ref:`LogEvents <no-13242>`             Specifies which events to log.  (list of strings)
:ref:`Name <no-13243>`                  The name of the object.  (str)
:ref:`Parent <no-13244>`                The containing object.  (obj)
:ref:`PreferenceDialogClass <no-13245>` Class to instantiate for the application's preference editing  (dForm/dDialog)
:ref:`PreferenceManager <no-13246>`     Reference to the Preference Management object  (dPref)

======================================= ========================


Properties
==========

.. _no-13236:

**ActiveForm** 

Returns the form that currently has focus, or None.(dForm)



-------

.. _no-13241:

**DrawSizerOutlines** 

Determines if sizer outlines are drawn on the ActiveForm.  (bool)



-------

.. _no-13245:

**PreferenceDialogClass** 

Class to instantiate for the application's preference editing  (dForm/dDialog)



-------


Properties - inherited
========================

.. _no-13237:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13238:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13239:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13240:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13242:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13243:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13244:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13246:

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
:ref:`addToMRU <no-13247>`              Adds the specified menu to the top of the list of
:ref:`afterInit <no-13248>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-13249>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-13250>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-13251>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-13252>`            Bind a sequence of [dEvent, callback] lists.
:ref:`checkForUpdates <no-13253>`       
:ref:`displayInfoMessage <no-13254>`    Display a dialog to the user that includes an option to not show the message again.
:ref:`exit <no-13255>`                  Exit the application event loop.
:ref:`finish <no-13256>`                
:ref:`fontZoomIn <no-13257>`            
:ref:`fontZoomNormal <no-13258>`        
:ref:`fontZoomOut <no-13259>`           
:ref:`getAbsoluteName <no-13260>`       Return the fully qualified name of the object.
:ref:`getMRUListForMenu <no-13261>`     Gets the current list of MRU entries for the given menu.
:ref:`getProperties <no-13262>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-13263>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-13264>`        Hook for subclasses. User subclasses should set properties
:ref:`onCmdWin <no-13265>`              
:ref:`onDebugWin <no-13266>`            
:ref:`onEditCopy <no-13267>`            
:ref:`onEditCut <no-13268>`             
:ref:`onEditFind <no-13269>`            Display a Find dialog.By default, both 'Find' and 'Find/Replace'
:ref:`onEditFindAgain <no-13270>`       Repeat the last search.
:ref:`onEditFindAlone <no-13271>`       
:ref:`onEditPaste <no-13272>`           
:ref:`onEditPreferences <no-13273>`     If a preference handler is defined for the form, use that. Otherwise,
:ref:`onEditRedo <no-13274>`            
:ref:`onEditSelectAll <no-13275>`       
:ref:`onEditUndo <no-13276>`            
:ref:`onEnterInFindDialog <no-13277>`   We need to simulate what happens in the Find dialog when
:ref:`onFileExit <no-13278>`            The MainForm contains the logic in its close methods to
:ref:`onMenuOpenMRU <no-13279>`         Make sure that the MRU items are there and are in the
:ref:`onObjectInspectorWin <no-13280>`  
:ref:`onReloadForm <no-13281>`          Re-creates the active form with a newer class definition.
:ref:`onShowSizerLines <no-13282>`      Toggles whether sizer lines are drawn. This is simply a tool
:ref:`onWinClose <no-13283>`            Close the topmost window, if any.
:ref:`raiseEvent <no-13284>`            Send the event to all registered listeners.
:ref:`setFindDialogIDs <no-13285>`      Since the Find dialog is a wxPython control, we can't determine
:ref:`setMainForm <no-13286>`           Hook called when dApp.MainForm is set.
:ref:`setProperties <no-13287>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-13288>` Sets a group of properties on the object all at once. This
:ref:`setup <no-13289>`                 
:ref:`showCommandWindow <no-13290>`     Display a command window for debugging.
:ref:`start <no-13291>`                 
:ref:`super <no-13292>`                 This method used to call superclass code, but it's been removed.
:ref:`toggleDebugWindow <no-13293>`     Display a debug output window.
:ref:`toggleInspectorWindow <no-13294>` Display the object inspector window.
:ref:`unbindEvent <no-13295>`           Remove a previously registered event binding.

======================================= ========================


Methods
=======

.. _no-13247:

.. function:: dabo.ui.uiwx.uiApp.uiApp.addToMRU(self, menuOrCaption, prompt, bindfunc=None)

   
   Adds the specified menu to the top of the list of
   MRU prompts for that menu.
   



-------

.. _no-13253:

.. function:: dabo.ui.uiwx.uiApp.uiApp.checkForUpdates(self, force=False)



-------

.. _no-13254:

.. function:: dabo.ui.uiwx.uiApp.uiApp.displayInfoMessage(self, msg, defaultShowInFuture=True)

   Display a dialog to the user that includes an option to not show the message again.



-------

.. _no-13255:

.. function:: dabo.ui.uiwx.uiApp.uiApp.exit(self)

   Exit the application event loop.



-------

.. _no-13256:

.. function:: dabo.ui.uiwx.uiApp.uiApp.finish(self)



-------

.. _no-13257:

.. function:: dabo.ui.uiwx.uiApp.uiApp.fontZoomIn(self)



-------

.. _no-13258:

.. function:: dabo.ui.uiwx.uiApp.uiApp.fontZoomNormal(self)



-------

.. _no-13259:

.. function:: dabo.ui.uiwx.uiApp.uiApp.fontZoomOut(self)



-------

.. _no-13261:

.. function:: dabo.ui.uiwx.uiApp.uiApp.getMRUListForMenu(self, menu)

   Gets the current list of MRU entries for the given menu.



-------

.. _no-13265:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onCmdWin(self, evt)



-------

.. _no-13266:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onDebugWin(self, evt)



-------

.. _no-13267:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditCopy(self, evt, cut=False)



-------

.. _no-13268:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditCut(self, evt)



-------

.. _no-13269:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditFind(self, evt, replace=True)

   
   Display a Find dialog.    By default, both 'Find' and 'Find/Replace'
   will be a single dialog. By calling this method with replace=False,
   you will get a Find-only version of the dialog.
   



-------

.. _no-13270:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditFindAgain(self, evt)

   Repeat the last search.



-------

.. _no-13271:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditFindAlone(self, evt)



-------

.. _no-13272:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditPaste(self, evt)



-------

.. _no-13273:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditPreferences(self, evt)

   
   If a preference handler is defined for the form, use that. Otherwise,
   use the generic preference dialog.
   



-------

.. _no-13274:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditRedo(self, evt)



-------

.. _no-13275:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditSelectAll(self, evt)



-------

.. _no-13276:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEditUndo(self, evt)



-------

.. _no-13277:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onEnterInFindDialog(self, evt)

   
   We need to simulate what happens in the Find dialog when
   the user clicks the Find button. This requires that we manually
   update the find data with the dialog values, and then carry out the
   find as before.
   



-------

.. _no-13278:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onFileExit(self, evt)

   
   The MainForm contains the logic in its close methods to
   cycle through all the forms and determine if they can all be
   safely closed. If it closes them all, it will close itself.
   



-------

.. _no-13279:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onMenuOpenMRU(self, menu)

   
   Make sure that the MRU items are there and are in the
   correct order.
   



-------

.. _no-13280:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onObjectInspectorWin(self, evt)



-------

.. _no-13281:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onReloadForm(self, evt)

   Re-creates the active form with a newer class definition.



-------

.. _no-13282:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onShowSizerLines(self, evt)

   
   Toggles whether sizer lines are drawn. This is simply a tool
   to help people visualize how sizers lay out objects.
   



-------

.. _no-13283:

.. function:: dabo.ui.uiwx.uiApp.uiApp.onWinClose(self, evt)

   Close the topmost window, if any.



-------

.. _no-13285:

.. function:: dabo.ui.uiwx.uiApp.uiApp.setFindDialogIDs(self)

   
   Since the Find dialog is a wxPython control, we can't determine
   which text control holds the Find value, and which holds the Replace
   value. One thing that is certain, though, on all platforms is that the
   Find textbox is physically above the Replace textbox, so we can use
   its position to determine its function.
   



-------

.. _no-13286:

.. function:: dabo.ui.uiwx.uiApp.uiApp.setMainForm(self, frm)

   Hook called when dApp.MainForm is set.



-------

.. _no-13289:

.. function:: dabo.ui.uiwx.uiApp.uiApp.setup(self)



-------

.. _no-13290:

.. function:: dabo.ui.uiwx.uiApp.uiApp.showCommandWindow(self, context=None)

   Display a command window for debugging.



-------

.. _no-13291:

.. function:: dabo.ui.uiwx.uiApp.uiApp.start(self)



-------

.. _no-13293:

.. function:: dabo.ui.uiwx.uiApp.uiApp.toggleDebugWindow(self, context=None)

   Display a debug output window.



-------

.. _no-13294:

.. function:: dabo.ui.uiwx.uiApp.uiApp.toggleInspectorWindow(self, context=None)

   Display the object inspector window.



-------


Methods - inherited
=====================

.. _no-13248:

.. function:: dabo.ui.uiwx.uiApp.uiApp.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13249:

.. function:: dabo.ui.uiwx.uiApp.uiApp.autoBindEvents(self, force=True)
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

.. _no-13250:

.. function:: dabo.ui.uiwx.uiApp.uiApp.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13251:

.. function:: dabo.ui.uiwx.uiApp.uiApp.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13252:

.. function:: dabo.ui.uiwx.uiApp.uiApp.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13260:

.. function:: dabo.ui.uiwx.uiApp.uiApp.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13262:

.. function:: dabo.ui.uiwx.uiApp.uiApp.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-13263:

.. function:: dabo.ui.uiwx.uiApp.uiApp.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13264:

.. function:: dabo.ui.uiwx.uiApp.uiApp.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13284:

.. function:: dabo.ui.uiwx.uiApp.uiApp.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-13287:

.. function:: dabo.ui.uiwx.uiApp.uiApp.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-13288:

.. function:: dabo.ui.uiwx.uiApp.uiApp.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-13292:

.. function:: dabo.ui.uiwx.uiApp.uiApp.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13295:

.. function:: dabo.ui.uiwx.uiApp.uiApp.unbindEvent(self, eventClass=None, function=None)
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
