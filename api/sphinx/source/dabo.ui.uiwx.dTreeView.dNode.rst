
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dTreeView

.. _dabo.ui.uiwx.dTreeView.dNode:

========================================
|doc_title|  **dTreeView.dNode** - class
========================================

Wrapper class for the tree nodes.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dNode**

.. inheritance-diagram:: dNode


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dTreeView.TestNode`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dTreeView.dNode

   .. automethod:: dabo.ui.uiwx.dTreeView.dNode.__init__

|method_summary| Properties Summary
===================================


====================================== ========================
:ref:`Application <no-26075>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-26076>`            Background color of this node  (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-26077>`            The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-26078>`          Base key used when saving/restoring preferences  (str)
:ref:`Caption <no-26079>`              Returns/sets the text of this node.  (str)
:ref:`Children <no-26080>`             List of all nodes for which this is their parent node.  (list of dNodes)
:ref:`Class <no-26081>`                The class the object is based on. Read-only.  (class)
:ref:`Descendents <no-26082>`          List of all nodes for which this node is a direct ancestor.  (list of dNodes)
:ref:`DynamicBackColor <no-26083>`     Dynamically determine the value of the BackColor property.
:ref:`DynamicCaption <no-26084>`       Dynamically determine the value of the Caption property.
:ref:`DynamicFont <no-26085>`          Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-26086>`      Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-26087>`      Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-26088>`    Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-26089>`      Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-26090>` Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-26091>`     Dynamically determine the value of the ForeColor property.
:ref:`DynamicImage <no-26092>`         Dynamically determine the value of the Image property.
:ref:`DynamicSelected <no-26093>`      Dynamically determine the value of the Selected property.
:ref:`DynamicToolTipText <no-26094>`   Dynamically determine the value of the ToolTipText property.
:ref:`Expanded <no-26095>`             Represents whether the node is Expanded (True) or collapsed.  (bool)
:ref:`Font <no-26096>`                 The font properties of the node. (obj)
:ref:`FontBold <no-26097>`             Specifies if the node font is bold-faced. (bool)
:ref:`FontDescription <no-26098>`      Human-readable description of the node's font settings. (str)
:ref:`FontFace <no-26099>`             Specifies the font face for the node. (str)
:ref:`FontInfo <no-26100>`             Specifies the platform-native font info string for the node. Read-only. (str)
:ref:`FontItalic <no-26101>`           Specifies whether the node's font is italicized. (bool)
:ref:`FontSize <no-26102>`             Specifies the point size of the node's font. (int)
:ref:`FontUnderline <no-26103>`        Specifies whether node text is underlined. (bool)
:ref:`ForeColor <no-26104>`            Foreground (text) color of this node  (str, 3-tuple, or wx.Colour)
:ref:`FullCaption <no-26105>`          Full dot-separated string of the captions of this node and its ancestors (read-only) (str)
:ref:`Image <no-26106>`                Sets the image that is displayed on the node. This is
:ref:`IsRootNode <no-26107>`           Returns True if this is the root node (read-only) (bool)
:ref:`LogEvents <no-26108>`            Specifies which events to log.  (list of strings)
:ref:`Name <no-26109>`                 The name of the object.  (str)
:ref:`Object <no-26110>`               Optional object associated with this node. Default=None  (object)
:ref:`Parent <no-26111>`               The containing object.  (obj)
:ref:`PreferenceManager <no-26112>`    Reference to the Preference Management object  (dPref)
:ref:`Selected <no-26113>`             Is this node selected?.  (bool)
:ref:`Siblings <no-26114>`             List of all nodes with the same parent node.  (list of dNodes)
:ref:`ToolTipText <no-26115>`          Text to display when the mouse hovers over this node. The tree's

====================================== ========================


Properties
==========

.. _no-26076:

**BackColor** 

Background color of this node  (str, 3-tuple, or wx.Colour)



-------

.. _no-26079:

**Caption** 

Returns/sets the text of this node.  (str)



-------

.. _no-26080:

**Children** 

List of all nodes for which this is their parent node.  (list of dNodes)



-------

.. _no-26082:

**Descendents** 

List of all nodes for which this node is a direct ancestor.  (list of dNodes)



-------

.. _no-26083:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.



-------

.. _no-26084:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.



-------

.. _no-26085:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.



-------

.. _no-26086:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.



-------

.. _no-26087:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.



-------

.. _no-26088:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.



-------

.. _no-26089:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.



-------

.. _no-26090:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.



-------

.. _no-26091:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.



-------

.. _no-26092:

**DynamicImage** 

Dynamically determine the value of the Image property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Image property. If DynamicImage is set to None (the default), Image
will not be dynamically evaluated.



-------

.. _no-26093:

**DynamicSelected** 

Dynamically determine the value of the Selected property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Selected property. If DynamicSelected is set to None (the default), Selected
will not be dynamically evaluated.



-------

.. _no-26094:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.



-------

.. _no-26095:

**Expanded** 

Represents whether the node is Expanded (True) or collapsed.  (bool)



-------

.. _no-26096:

**Font** 

The font properties of the node. (obj)



-------

.. _no-26097:

**FontBold** 

Specifies if the node font is bold-faced. (bool)



-------

.. _no-26098:

**FontDescription** 

Human-readable description of the node's font settings. (str)



-------

.. _no-26099:

**FontFace** 

Specifies the font face for the node. (str)



-------

.. _no-26100:

**FontInfo** 

Specifies the platform-native font info string for the node. Read-only. (str)



-------

.. _no-26101:

**FontItalic** 

Specifies whether the node's font is italicized. (bool)



-------

.. _no-26102:

**FontSize** 

Specifies the point size of the node's font. (int)



-------

.. _no-26103:

**FontUnderline** 

Specifies whether node text is underlined. (bool)



-------

.. _no-26104:

**ForeColor** 

Foreground (text) color of this node  (str, 3-tuple, or wx.Colour)



-------

.. _no-26105:

**FullCaption** 

Full dot-separated string of the captions of this node and its ancestors (read-only) (str)



-------

.. _no-26106:

**Image** 

Sets the image that is displayed on the node. This is
    determined by the key value passed, which must refer to an
    image already added to the parent tree.     When used to retrieve
    an image, it returns the index of the node's image in the parent
    tree's image list.   (int)



-------

.. _no-26107:

**IsRootNode** 

Returns True if this is the root node (read-only) (bool)



-------

.. _no-26110:

**Object** 

Optional object associated with this node. Default=None  (object)



-------

.. _no-26113:

**Selected** 

Is this node selected?.  (bool)



-------

.. _no-26114:

**Siblings** 

List of all nodes with the same parent node.  (list of dNodes)



-------

.. _no-26115:

**ToolTipText** 

Text to display when the mouse hovers over this node. The tree's
    UseNodeToolTips property must be True for this to have any effect.  (str)



-------


Properties - inherited
========================

.. _no-26075:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26077:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26078:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26081:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26108:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26109:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26111:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26112:

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
:ref:`afterInit <no-26116>`             
:ref:`appendChild <no-26117>`           
:ref:`autoBindEvents <no-26118>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-26119>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-26120>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-26121>`            Bind a sequence of [dEvent, callback] lists.
:ref:`collapse <no-26122>`              
:ref:`expand <no-26123>`                
:ref:`getAbsoluteName <no-26124>`       Return the fully qualified name of the object.
:ref:`getProperties <no-26125>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-26126>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-26127>`        Hook for subclasses. User subclasses should set properties
:ref:`raiseEvent <no-26128>`            Send the event to all registered listeners.
:ref:`release <no-26129>`               
:ref:`removeChild <no-26130>`           Removes the child node whose text matches the passed value
:ref:`setProperties <no-26131>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-26132>` Sets a group of properties on the object all at once. This
:ref:`show <no-26133>`                  
:ref:`super <no-26134>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-26135>`           Remove a previously registered event binding.

======================================= ========================


Methods
=======

.. _no-26116:

.. function:: dabo.ui.uiwx.dTreeView.dNode.afterInit(self)



-------

.. _no-26117:

.. function:: dabo.ui.uiwx.dTreeView.dNode.appendChild(self, txt)



-------

.. _no-26122:

.. function:: dabo.ui.uiwx.dTreeView.dNode.collapse(self)



-------

.. _no-26123:

.. function:: dabo.ui.uiwx.dTreeView.dNode.expand(self)



-------

.. _no-26129:

.. function:: dabo.ui.uiwx.dTreeView.dNode.release(self)



-------

.. _no-26130:

.. function:: dabo.ui.uiwx.dTreeView.dNode.removeChild(self, txt)

   Removes the child node whose text matches the passed value



-------

.. _no-26133:

.. function:: dabo.ui.uiwx.dTreeView.dNode.show(self)



-------


Methods - inherited
=====================

.. _no-26118:

.. function:: dabo.ui.uiwx.dTreeView.dNode.autoBindEvents(self, force=True)
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

.. _no-26119:

.. function:: dabo.ui.uiwx.dTreeView.dNode.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26120:

.. function:: dabo.ui.uiwx.dTreeView.dNode.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26121:

.. function:: dabo.ui.uiwx.dTreeView.dNode.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26124:

.. function:: dabo.ui.uiwx.dTreeView.dNode.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26125:

.. function:: dabo.ui.uiwx.dTreeView.dNode.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-26126:

.. function:: dabo.ui.uiwx.dTreeView.dNode.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26127:

.. function:: dabo.ui.uiwx.dTreeView.dNode.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26128:

.. function:: dabo.ui.uiwx.dTreeView.dNode.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-26131:

.. function:: dabo.ui.uiwx.dTreeView.dNode.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-26132:

.. function:: dabo.ui.uiwx.dTreeView.dNode.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-26134:

.. function:: dabo.ui.uiwx.dTreeView.dNode.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26135:

.. function:: dabo.ui.uiwx.dTreeView.dNode.unbindEvent(self, eventClass=None, function=None)
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
