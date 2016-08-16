
.. include:: _static/headings.txt

.. module:: dabo.lib.DesignerClassConverter

.. _dabo.lib.DesignerClassConverter.DesignerClassConverter:

======================================================================
|doc_title|  **DesignerClassConverter.DesignerClassConverter** - class
======================================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **DesignerClassConverter**

.. inheritance-diagram:: DesignerClassConverter


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.lib.DesignerClassConverter.DesignerClassConverter

   .. automethod:: dabo.lib.DesignerClassConverter.DesignerClassConverter.__init__

|method_summary| Properties Summary
===================================


======================================= ========================
:ref:`Application <no-2196>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-2197>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-2198>`            Base key used when saving/restoring preferences  (str)
:ref:`Class <no-2199>`                  The class the object is based on. Read-only.  (class)
:ref:`CreateDesignerControls <no-2200>` When True, classes are mixed-in with the DesignerControlMixin  (bool)
:ref:`LogEvents <no-2201>`              Specifies which events to log.  (list of strings)
:ref:`Name <no-2202>`                   The name of the object.  (str)
:ref:`Parent <no-2203>`                 The containing object.  (obj)
:ref:`PreferenceManager <no-2204>`      Reference to the Preference Management object  (dPref)

======================================= ========================


Properties
==========

.. _no-2200:

**CreateDesignerControls** 

When True, classes are mixed-in with the DesignerControlMixin  (bool)



-------


Properties - inherited
========================

.. _no-2196:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2197:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2198:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2199:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2201:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2202:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2203:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2204:

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
:ref:`addCodeFile <no-2205>`           
:ref:`afterInit <no-2206>`             
:ref:`autoBindEvents <no-2207>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-2208>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-2209>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-2210>`            Bind a sequence of [dEvent, callback] lists.
:ref:`classFromText <no-2211>`         Given a text file, returns a class object that that file
:ref:`cleanAttributes <no-2212>`       Return a dict that is the same as the source dict, dropping any
:ref:`createChildCode <no-2213>`       Takes a list of child object dicts, and adds their code to the
:ref:`createClassText <no-2214>`       
:ref:`createInheritedClass <no-2215>`  When a custom class is contained in a cdxml file, we need
:ref:`createInnerClass <no-2216>`      Define a class that will be used to create an instance of
:ref:`createWizardPages <no-2217>`     Takes a list of wizard page dicts, and adds their code to the
:ref:`dictFromStoredText <no-2218>`    Takes either a path to a text file, an open file containing the text,
:ref:`flattenClassDict <no-2219>`      Given a dict containing a series of nested objects such as would
:ref:`getAbsoluteName <no-2220>`       Return the fully qualified name of the object.
:ref:`getProperties <no-2221>`         Returns a dictionary of property name/value pairs.
:ref:`importJsonSource <no-2222>`      This will read in a JSON source. The parameter can be a
:ref:`importXmlSrc <no-2223>`          This will read in an XML source. The parameter can be a
:ref:`initEvents <no-2224>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-2225>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-2226>`            Send the event to all registered listeners.
:ref:`setProperties <no-2227>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-2228>` Sets a group of properties on the object all at once. This
:ref:`super <no-2229>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-2230>`           Remove a previously registered event binding.
:ref:`uniqename <no-2231>`             

====================================== ========================


Methods
=======

.. _no-2205:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.addCodeFile(self, dct, pth=None, encoding=None)



-------

.. _no-2206:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.afterInit(self)



-------

.. _no-2211:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.classFromText(self, src)

   Given a text file, returns a class object that that file
   represents. You can pass the text as either a file path,
   a file object, or raw XML/JSON text.
   



-------

.. _no-2212:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.cleanAttributes(self, attDict)

   Return a dict that is the same as the source dict, dropping any
   attributes that the Designer added that are not used
   in the runtime objects.
   



-------

.. _no-2213:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.createChildCode(self, childList, specChildList=[], force1x=False)

   Takes a list of child object dicts, and adds their code to the
   generated class text.
   



-------

.. _no-2214:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.createClassText(self, dct, addImports=True, specList=[])



-------

.. _no-2215:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.createInheritedClass(self, pth, specList)

   When a custom class is contained in a cdxml file, we need
   to add that class separately, and inherit from that. We will
   be passed a path to the cdxml file, along with a list of
   dictionaries that contains a dict for each level of specialization
   for this class.
   



-------

.. _no-2216:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.createInnerClass(self, nm, atts, code, custProps)

   Define a class that will be used to create an instance of
   an object that contains its own method code and/or Properties.
   



-------

.. _no-2217:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.createWizardPages(self, pgList, specPgList=[])

   Takes a list of wizard page dicts, and adds their code to the
   generated class text.
   



-------

.. _no-2218:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.dictFromStoredText(self, src)

   Takes either a path to a text file, an open file containing the text,
   or the raw text itself. Determines the format of the stored text, and
   returns the corresponding dict.
   



-------

.. _no-2219:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.flattenClassDict(self, cd, retDict=None)

   Given a dict containing a series of nested objects such as would
   be created by restoring from a stored class file, returns a dict with all classIDs
   as keys, and a dict as the corresponding value. The dict value will have
   keys for the attributes and/or code, depending on what was in the original
   dict. The end result is to take a nested dict structure and return a flattened
   dict with all objects at the top level.
   



-------

.. _no-2222:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.importJsonSource(self, src)

   This will read in a JSON source. The parameter can be a
   file path, an open file object, or the raw XML. It will look for
   a matching code file and, if found, import that code.
   



-------

.. _no-2223:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.importXmlSrc(self, src)

   This will read in an XML source. The parameter can be a
   file path, an open file object, or the raw XML. It will look for
   a matching code file and, if found, import that code.
   



-------

.. _no-2231:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.uniqename(self, nm)



-------


Methods - inherited
=====================

.. _no-2207:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.autoBindEvents(self, force=True)
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

.. _no-2208:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2209:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2210:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2220:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2221:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-2224:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2225:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2226:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-2227:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-2228:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-2229:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2230:

.. function:: dabo.lib.DesignerClassConverter.DesignerClassConverter.unbindEvent(self, eventClass=None, function=None)
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
