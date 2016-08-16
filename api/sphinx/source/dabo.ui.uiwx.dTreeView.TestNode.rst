
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dTreeView

.. _dabo.ui.uiwx.dTreeView.TestNode:

===========================================
|doc_title|  **dTreeView.TestNode** - class
===========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **TestNode**

.. inheritance-diagram:: TestNode


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTreeView.dNode`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dTreeView.TestNode


|method_summary| Properties Summary
===================================


====================================== ========================
:ref:`Application <no-26014>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-26015>`            Background color of this node  (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-26016>`            The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-26017>`          Base key used when saving/restoring preferences  (str)
:ref:`Caption <no-26018>`              Returns/sets the text of this node.  (str)
:ref:`Children <no-26019>`             List of all nodes for which this is their parent node.  (list of dNodes)
:ref:`Class <no-26020>`                The class the object is based on. Read-only.  (class)
:ref:`Descendents <no-26021>`          List of all nodes for which this node is a direct ancestor.  (list of dNodes)
:ref:`DynamicBackColor <no-26022>`     Dynamically determine the value of the BackColor property.
:ref:`DynamicCaption <no-26023>`       Dynamically determine the value of the Caption property.
:ref:`DynamicFont <no-26024>`          Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-26025>`      Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-26026>`      Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-26027>`    Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-26028>`      Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-26029>` Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-26030>`     Dynamically determine the value of the ForeColor property.
:ref:`DynamicImage <no-26031>`         Dynamically determine the value of the Image property.
:ref:`DynamicSelected <no-26032>`      Dynamically determine the value of the Selected property.
:ref:`DynamicToolTipText <no-26033>`   Dynamically determine the value of the ToolTipText property.
:ref:`Expanded <no-26034>`             Represents whether the node is Expanded (True) or collapsed.  (bool)
:ref:`Font <no-26035>`                 The font properties of the node. (obj)
:ref:`FontBold <no-26036>`             Specifies if the node font is bold-faced. (bool)
:ref:`FontDescription <no-26037>`      Human-readable description of the node's font settings. (str)
:ref:`FontFace <no-26038>`             Specifies the font face for the node. (str)
:ref:`FontInfo <no-26039>`             Specifies the platform-native font info string for the node. Read-only. (str)
:ref:`FontItalic <no-26040>`           Specifies whether the node's font is italicized. (bool)
:ref:`FontSize <no-26041>`             Specifies the point size of the node's font. (int)
:ref:`FontUnderline <no-26042>`        Specifies whether node text is underlined. (bool)
:ref:`ForeColor <no-26043>`            Foreground (text) color of this node  (str, 3-tuple, or wx.Colour)
:ref:`FullCaption <no-26044>`          Full dot-separated string of the captions of this node and its ancestors (read-only) (str)
:ref:`Image <no-26045>`                Sets the image that is displayed on the node. This is
:ref:`IsRootNode <no-26046>`           Returns True if this is the root node (read-only) (bool)
:ref:`LogEvents <no-26047>`            Specifies which events to log.  (list of strings)
:ref:`Name <no-26048>`                 The name of the object.  (str)
:ref:`Object <no-26049>`               Optional object associated with this node. Default=None  (object)
:ref:`Parent <no-26050>`               The containing object.  (obj)
:ref:`PreferenceManager <no-26051>`    Reference to the Preference Management object  (dPref)
:ref:`Selected <no-26052>`             Is this node selected?.  (bool)
:ref:`Siblings <no-26053>`             List of all nodes with the same parent node.  (list of dNodes)
:ref:`ToolTipText <no-26054>`          Text to display when the mouse hovers over this node. The tree's

====================================== ========================


Properties - inherited
========================

.. _no-26014:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26015:

**BackColor** 

Background color of this node  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26016:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26017:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26018:

**Caption** 

Returns/sets the text of this node.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26019:

**Children** 

List of all nodes for which this is their parent node.  (list of dNodes)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26020:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26021:

**Descendents** 

List of all nodes for which this node is a direct ancestor.  (list of dNodes)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26022:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26023:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26024:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26025:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26026:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26027:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26028:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26029:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26030:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26031:

**DynamicImage** 

Dynamically determine the value of the Image property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Image property. If DynamicImage is set to None (the default), Image
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26032:

**DynamicSelected** 

Dynamically determine the value of the Selected property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Selected property. If DynamicSelected is set to None (the default), Selected
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26033:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26034:

**Expanded** 

Represents whether the node is Expanded (True) or collapsed.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26035:

**Font** 

The font properties of the node. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26036:

**FontBold** 

Specifies if the node font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26037:

**FontDescription** 

Human-readable description of the node's font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26038:

**FontFace** 

Specifies the font face for the node. (str)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26039:

**FontInfo** 

Specifies the platform-native font info string for the node. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26040:

**FontItalic** 

Specifies whether the node's font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26041:

**FontSize** 

Specifies the point size of the node's font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26042:

**FontUnderline** 

Specifies whether node text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26043:

**ForeColor** 

Foreground (text) color of this node  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26044:

**FullCaption** 

Full dot-separated string of the captions of this node and its ancestors (read-only) (str)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26045:

**Image** 

Sets the image that is displayed on the node. This is
    determined by the key value passed, which must refer to an
    image already added to the parent tree.     When used to retrieve
    an image, it returns the index of the node's image in the parent
    tree's image list.   (int)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26046:

**IsRootNode** 

Returns True if this is the root node (read-only) (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26047:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26048:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26049:

**Object** 

Optional object associated with this node. Default=None  (object)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26050:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26051:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26052:

**Selected** 

Is this node selected?.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26053:

**Siblings** 

List of all nodes with the same parent node.  (list of dNodes)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26054:

**ToolTipText** 

Text to display when the mouse hovers over this node. The tree's
    UseNodeToolTips property must be True for this to have any effect.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------


|method_summary| Events Summary
===============================


========== ========================

========== ========================


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`afterInit <no-26055>`             
:ref:`appendChild <no-26056>`           
:ref:`autoBindEvents <no-26057>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-26058>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-26059>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-26060>`            Bind a sequence of [dEvent, callback] lists.
:ref:`collapse <no-26061>`              
:ref:`expand <no-26062>`                
:ref:`getAbsoluteName <no-26063>`       Return the fully qualified name of the object.
:ref:`getProperties <no-26064>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-26065>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-26066>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-26067>`            Send the event to all registered listeners.
:ref:`release <no-26068>`               
:ref:`removeChild <no-26069>`           Removes the child node whose text matches the passed value
:ref:`setProperties <no-26070>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-26071>` Sets a group of properties on the object all at once. This
:ref:`show <no-26072>`                  
:ref:`super <no-26073>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-26074>`           Remove a previously registered event binding.

======================================= ========================


Methods
=======

.. _no-26055:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.afterInit(self)



-------


Methods - inherited
=====================

.. _no-26056:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.appendChild(self, txt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26057:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.autoBindEvents(self, force=True)
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

.. _no-26058:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26059:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26060:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26061:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.collapse(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26062:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.expand(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26063:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26064:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-26065:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26066:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26067:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-26068:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.release(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26069:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.removeChild(self, txt)
   :noindex:


   Removes the child node whose text matches the passed value


Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26070:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-26071:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-26072:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTreeView.dNode`

-------

.. _no-26073:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26074:

.. function:: dabo.ui.uiwx.dTreeView.TestNode.unbindEvent(self, eventClass=None, function=None)
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
