
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSizer

.. _dabo.ui.uiwx.dSizer.dSizerV:

=======================================
|doc_title|  **dSizer.dSizerV** - class
=======================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSizerV**

.. inheritance-diagram:: dSizerV


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dSizer.dSizer`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSizer.dSizerV

   .. automethod:: dabo.ui.uiwx.dSizer.dSizerV.__init__

|method_summary| Properties Summary
===================================


====================================== ========================
:ref:`Application <no-31978>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-31979>`            The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-31980>`          Base key used when saving/restoring preferences  (str)
:ref:`ChildObjects <no-31981>`         List of all the objects (controls, sizers, spacers) that are directly managed
:ref:`ChildSizers <no-31982>`          List of all the sizers that are directly managed by this sizer  (list of sizers
:ref:`ChildSpacers <no-31983>`         List of all the spacer items that are directly managed by this sizer  (list of spacer items
:ref:`ChildWindows <no-31984>`         List of all the windows that are directly managed by this sizer  (list of controls
:ref:`Children <no-31985>`             List of all the sizer items managed by this sizer  (list of sizerItems
:ref:`Class <no-31986>`                The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-31987>`     Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-31988>` Reference to the sizer item that control's this control's layout.
:ref:`DefaultBorder <no-31989>`        Sets a default value for the border that will be applied to any controls added
:ref:`DefaultBorderAll <no-31990>`     When True, the DefaultBorder property is applied to all of the sides of
:ref:`DefaultBorderBottom <no-31991>`  Affects whether the DefaultBorder property is applied to the Bottom
:ref:`DefaultBorderLeft <no-31992>`    Affects whether the DefaultBorder property is applied to the Left
:ref:`DefaultBorderRight <no-31993>`   Affects whether the DefaultBorder property is applied to the Right
:ref:`DefaultBorderTop <no-31994>`     Affects whether the DefaultBorder property is applied to the Top
:ref:`DefaultSpacing <no-31995>`       Amount of space automatically inserted between elements.  (int)
:ref:`DynamicDefaultBorder <no-31996>` Dynamically determine the value of the DefaultBorder property.
:ref:`DynamicVisible <no-31997>`       Dynamically determine the value of the Visible property.
:ref:`Form <no-31998>`                 Form with which the sizer is associated.  (dForm or None)
:ref:`Height <no-31999>`               Height of the sizer  (int)
:ref:`LogEvents <no-32000>`            Specifies which events to log.  (list of strings)
:ref:`Name <no-32001>`                 The name of the object.  (str)
:ref:`Orientation <no-32002>`          Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.
:ref:`Parent <no-32003>`               The object that contains this sizer. In the case of nested
:ref:`PreferenceManager <no-32004>`    Reference to the Preference Management object  (dPref)
:ref:`Visible <no-32005>`              Specifies whether the sizer and contained items are shown  (bool)
:ref:`Width <no-32006>`                Width of this sizer  (int)

====================================== ========================


Properties - inherited
========================

.. _no-31978:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31979:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31980:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31981:

**ChildObjects** 

List of all the objects (controls, sizers, spacers) that are directly managed
    by this sizer  (list of objects


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31982:

**ChildSizers** 

List of all the sizers that are directly managed by this sizer  (list of sizers


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31983:

**ChildSpacers** 

List of all the spacer items that are directly managed by this sizer  (list of spacer items


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31984:

**ChildWindows** 

List of all the windows that are directly managed by this sizer  (list of controls


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31985:

**Children** 

List of all the sizer items managed by this sizer  (list of sizerItems


Inherited from: 'wx._core.Sizer - can not provide a link

-------

.. _no-31986:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31987:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31988:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.
        This is useful for getting information about how the item is being
        sized, and for changing those settings.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31989:

**DefaultBorder** 

Sets a default value for the border that will be applied to any controls added
    to the sizer afterwards for whom an explicit value for the border is not set.
    Note that it does not affect the border of items already added to the control.
    This property is useful when you want to add a series of items to a sizer with
    the same border: just set this property once, and then add your items.
    Default=0  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31990:

**DefaultBorderAll** 

When True, the DefaultBorder property is applied to all of the sides of
    any controls added to the sizer. If any of the individual side properties,
    such as DefaultBorderTop, are set to False, this property will return False.
    Setting DefaultBorderAll will effectively set all of the individual side properties
    to that value. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31991:

**DefaultBorderBottom** 

Affects whether the DefaultBorder property is applied to the Bottom
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31992:

**DefaultBorderLeft** 

Affects whether the DefaultBorder property is applied to the Left
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31993:

**DefaultBorderRight** 

Affects whether the DefaultBorder property is applied to the Right
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31994:

**DefaultBorderTop** 

Affects whether the DefaultBorder property is applied to the Top
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31995:

**DefaultSpacing** 

Amount of space automatically inserted between elements.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31996:

**DynamicDefaultBorder** 

Dynamically determine the value of the DefaultBorder property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultBorder property. If DynamicDefaultBorder is set to None (the default), DefaultBorder
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31997:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31998:

**Form** 

Form with which the sizer is associated.  (dForm or None)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31999:

**Height** 

Height of the sizer  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32000:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32001:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32002:

**Orientation** 

Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.


Inherited from: 'wx._core.BoxSizer - can not provide a link

-------

.. _no-32003:

**Parent** 

The object that contains this sizer. In the case of nested
    sizers, it is the object that the outermost sizer belongs to. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32004:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32005:

**Visible** 

Specifies whether the sizer and contained items are shown  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32006:

**Width** 

Width of this sizer  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------


|method_summary| Events Summary
===============================


========== ========================

========== ========================


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`addDefaultSpacer <no-32007>`      
:ref:`addSpacer <no-32008>`             
:ref:`afterInit <no-32009>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`append <no-32010>`                Adds the passed object to the end of the sizer layout.
:ref:`append1x <no-32011>`              Shorthand for sizer.append(obj, 1, "expand").
:ref:`appendItems <no-32012>`           Append each item to the sizer.
:ref:`appendSpacer <no-32013>`          Appends a spacer to the sizer.
:ref:`autoBindEvents <no-32014>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-32015>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-32016>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-32017>`            Bind a sequence of [dEvent, callback] lists.
:ref:`clear <no-32018>`                 This method is called to remove all items from the sizer. If the
:ref:`drawOutline <no-32019>`           There are some cases where being able to see the sizer
:ref:`getAbsoluteName <no-32020>`       Return the fully qualified name of the object.
:ref:`getBorderedClass <no-32021>`      Return the class that is the border sizer version of this class.
:ref:`getContainingWindow <no-32022>`   
:ref:`getItem <no-32023>`               Querying sizers for their contents returns sizer items, not
:ref:`getItemProp <no-32024>`           Get the current value of the specified property for the sizer item.
:ref:`getItemProps <no-32025>`          Returns a dict containing all the sizer properties as keys along with
:ref:`getPositionInSizer <no-32026>`    Returns the current position of this sizer in its containing sizer, or None
:ref:`getProperties <no-32027>`         Returns a dictionary of property name/value pairs.
:ref:`hideItem <no-32028>`              Hides the passed item
:ref:`initEvents <no-32029>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-32030>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-32031>`                Inserts the passed object into the sizer layout at the specified position.
:ref:`insertSpacer <no-32032>`          Added to be consistent with the sizers' add/insert
:ref:`isContainedBy <no-32033>`         Returns True if this the containership hierarchy for this control
:ref:`layout <no-32034>`                Layout the items in the sizer.
:ref:`listMembers <no-32035>`           Debugging method. This will list all the members of this sizer,
:ref:`prepend <no-32036>`               Insert the object at the beginning of the sizer layout.
:ref:`prependSpacer <no-32037>`         Added to be consistent with the sizers' add/insert
:ref:`raiseEvent <no-32038>`            Send the event to all registered listeners.
:ref:`release <no-32039>`               Normally just destroys the sizer, leaving any objects
:ref:`remove <no-32040>`                This will remove the item from the sizer. It will not cause
:ref:`setItemProp <no-32041>`           Given a sizer item, a property and a value, sets things as you
:ref:`setItemProps <no-32042>`          This accepts a dict of properties and values, and
:ref:`setPositionInSizer <no-32043>`    
:ref:`setProperties <no-32044>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-32045>` Sets a group of properties on the object all at once. This
:ref:`showItem <no-32046>`              Makes sure that the passed item is visible
:ref:`super <no-32047>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-32048>`           Remove a previously registered event binding.

======================================= ========================


Methods - inherited
=====================

.. _no-32007:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.addDefaultSpacer(self, pos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32008:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.addSpacer(self, val, pos=None, proportion=0)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32009:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32010:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.append(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
   :noindex:


   Adds the passed object to the end of the sizer layout.
   
   +--------------------------------------------------------------------------+
   |Additional arguments:                                                     |
   +=============+============================================================+
   |layout:      |Specifies how the object expands in the opposite dimension  |
   |             |of the sizer. If "normal" (the default), no expansion takes |
   |             |place. If "expand" (a common setting), the item will expand |
   |             |to fill up otherwise unoccupied space in the sizer.         |
   +-------------+------------------------------------------------------------+
   |proportion   |Specifies the proportional amount of space that the object  |
   |             |can grow to in the same dimension as this sizer. If 0 (the  |
   |             |default), the object will maintain its size. If > 0, the    |
   |             |object will get a spacing in the sizer proportional to      |
   |             |other objects in the sizer with proportions > 0. So if this |
   |             |is a horizontal sizer, and the proportion for the object is |
   |             |set to 1, and no other objects in the sizer have proportion |
   |             |set, the object will fill up all extra horizontal space.    |
   +-------------+------------------------------------------------------------+
   |alignment    |Possible values are "top", "middle", and "bottom" for       |
   |             |horizontal sizers, and "left", "center", and "right" for    |
   |             |vertical sizers. Specifies where the object appears within  |
   |             |the available area in the sizer.                            |
   +-------------+------------------------------------------------------------+
   |halign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |valign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |border       |Specifies the number of pixels to put around the object in  |
   |             |the sizer, on the sides specified by the borderSides        |
   |             |argument, or by the value of the DefaultBorderLeft,         |
   |             |DefaultBorderRight, DefaultBorderTop, and                   |
   |             |DefaultBorderBottom boolean properties.                     |
   +-------------+------------------------------------------------------------+
   |borderSides  |Specifies the sides around the object to place the border   |
   |             |specified in the border argument or the DefaultBorder       |
   |             |property. This should be a tuple that contains at least     |
   |             |some of the values ("left", "right", "top", "bottom")       |
   +-------------+------------------------------------------------------------+


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32011:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.append1x(self, obj, \**kwargs)
   :noindex:


   Shorthand for sizer.append(obj, 1, "expand").


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32012:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.appendItems(self, items, \*args, \**kwargs)
   :noindex:


   Append each item to the sizer.
   
   +--------------------------------------------------------------------------+
   |Additional arguments:                                                     |
   +=============+============================================================+
   |layout:      |Specifies how the object expands in the opposite dimension  |
   |             |of the sizer. If "normal" (the default), no expansion takes |
   |             |place. If "expand" (a common setting), the item will expand |
   |             |to fill up otherwise unoccupied space in the sizer.         |
   +-------------+------------------------------------------------------------+
   |proportion   |Specifies the proportional amount of space that the object  |
   |             |can grow to in the same dimension as this sizer. If 0 (the  |
   |             |default), the object will maintain its size. If > 0, the    |
   |             |object will get a spacing in the sizer proportional to      |
   |             |other objects in the sizer with proportions > 0. So if this |
   |             |is a horizontal sizer, and the proportion for the object is |
   |             |set to 1, and no other objects in the sizer have proportion |
   |             |set, the object will fill up all extra horizontal space.    |
   +-------------+------------------------------------------------------------+
   |alignment    |Possible values are "top", "middle", and "bottom" for       |
   |             |horizontal sizers, and "left", "center", and "right" for    |
   |             |vertical sizers. Specifies where the object appears within  |
   |             |the available area in the sizer.                            |
   +-------------+------------------------------------------------------------+
   |halign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |valign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |border       |Specifies the number of pixels to put around the object in  |
   |             |the sizer, on the sides specified by the borderSides        |
   |             |argument, or by the value of the DefaultBorderLeft,         |
   |             |DefaultBorderRight, DefaultBorderTop, and                   |
   |             |DefaultBorderBottom boolean properties.                     |
   +-------------+------------------------------------------------------------+
   |borderSides  |Specifies the sides around the object to place the border   |
   |             |specified in the border argument or the DefaultBorder       |
   |             |property. This should be a tuple that contains at least     |
   |             |some of the values ("left", "right", "top", "bottom")       |
   +-------------+------------------------------------------------------------+


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32013:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.appendSpacer(self, val, proportion=0)
   :noindex:


   Appends a spacer to the sizer.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32014:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.autoBindEvents(self, force=True)
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

.. _no-32015:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32016:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32017:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32018:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.clear(self, destroy=False)
   :noindex:


   
   This method is called to remove all items from the sizer. If the
   optional 'destroy' parameter is set to True, any contained items
   will be destroyed. Otherwise, they will remain as is, but no longer
   under control of the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32019:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.drawOutline(self, win, recurse=False, drawChildren=False)
   :noindex:


   
   There are some cases where being able to see the sizer
   is helpful, such as at design time. This method can be called
   to see the outline; it needs to be called whenever the containing
   window is resized or repainted.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32020:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32021:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getBorderedClass(self)
   :noindex:


   Return the class that is the border sizer version of this class.


Inherited from: :ref:`dabo.ui.uiwx.dSizer.dSizer`

-------

.. _no-32022:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getContainingWindow(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32023:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getItem(self, szItem)
   :noindex:


   
   Querying sizers for their contents returns sizer items, not
   the actual items. So given a sizer item, this method will return
   the actual item in the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32024:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getItemProp(self, itm, prop)
   :noindex:


   
   Get the current value of the specified property for the sizer item.
   Grid sizers must override with their specific props.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32025:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getItemProps(self, itm)
   :noindex:


   
   Returns a dict containing all the sizer properties as keys along with
   their associated values.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32026:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getPositionInSizer(self)
   :noindex:


   
   Returns the current position of this sizer in its containing sizer, or None
   if there isn't a containing sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32027:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-32028:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.hideItem(self, itm)
   :noindex:


   Hides the passed item


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32029:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32030:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32031:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.insert(self, index, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
   :noindex:


   Inserts the passed object into the sizer layout at the specified position.
   
   +--------------------------------------------------------------------------+
   |Additional arguments:                                                     |
   +=============+============================================================+
   |layout:      |Specifies how the object expands in the opposite dimension  |
   |             |of the sizer. If "normal" (the default), no expansion takes |
   |             |place. If "expand" (a common setting), the item will expand |
   |             |to fill up otherwise unoccupied space in the sizer.         |
   +-------------+------------------------------------------------------------+
   |proportion   |Specifies the proportional amount of space that the object  |
   |             |can grow to in the same dimension as this sizer. If 0 (the  |
   |             |default), the object will maintain its size. If > 0, the    |
   |             |object will get a spacing in the sizer proportional to      |
   |             |other objects in the sizer with proportions > 0. So if this |
   |             |is a horizontal sizer, and the proportion for the object is |
   |             |set to 1, and no other objects in the sizer have proportion |
   |             |set, the object will fill up all extra horizontal space.    |
   +-------------+------------------------------------------------------------+
   |alignment    |Possible values are "top", "middle", and "bottom" for       |
   |             |horizontal sizers, and "left", "center", and "right" for    |
   |             |vertical sizers. Specifies where the object appears within  |
   |             |the available area in the sizer.                            |
   +-------------+------------------------------------------------------------+
   |halign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |valign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |border       |Specifies the number of pixels to put around the object in  |
   |             |the sizer, on the sides specified by the borderSides        |
   |             |argument, or by the value of the DefaultBorderLeft,         |
   |             |DefaultBorderRight, DefaultBorderTop, and                   |
   |             |DefaultBorderBottom boolean properties.                     |
   +-------------+------------------------------------------------------------+
   |borderSides  |Specifies the sides around the object to place the border   |
   |             |specified in the border argument or the DefaultBorder       |
   |             |property. This should be a tuple that contains at least     |
   |             |some of the values ("left", "right", "top", "bottom")       |
   +-------------+------------------------------------------------------------+


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32032:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.insertSpacer(self, pos, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer at the specified position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32033:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.isContainedBy(self, obj)
   :noindex:


   
   Returns True if this the containership hierarchy for this control
   includes obj.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32034:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.layout(self)
   :noindex:


   
   Layout the items in the sizer.
   
   This is handled automatically when the sizer is resized, but you'll have
   to call it manually after you are done adding items to the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32035:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.listMembers(self, recurse=False, lvl=0)
   :noindex:


   
   Debugging method. This will list all the members of this sizer,
   and if recurse is True, drill down into all contained sizers.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32036:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.prepend(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
   :noindex:


   Insert the object at the beginning of the sizer layout.
   
   +--------------------------------------------------------------------------+
   |Additional arguments:                                                     |
   +=============+============================================================+
   |layout:      |Specifies how the object expands in the opposite dimension  |
   |             |of the sizer. If "normal" (the default), no expansion takes |
   |             |place. If "expand" (a common setting), the item will expand |
   |             |to fill up otherwise unoccupied space in the sizer.         |
   +-------------+------------------------------------------------------------+
   |proportion   |Specifies the proportional amount of space that the object  |
   |             |can grow to in the same dimension as this sizer. If 0 (the  |
   |             |default), the object will maintain its size. If > 0, the    |
   |             |object will get a spacing in the sizer proportional to      |
   |             |other objects in the sizer with proportions > 0. So if this |
   |             |is a horizontal sizer, and the proportion for the object is |
   |             |set to 1, and no other objects in the sizer have proportion |
   |             |set, the object will fill up all extra horizontal space.    |
   +-------------+------------------------------------------------------------+
   |alignment    |Possible values are "top", "middle", and "bottom" for       |
   |             |horizontal sizers, and "left", "center", and "right" for    |
   |             |vertical sizers. Specifies where the object appears within  |
   |             |the available area in the sizer.                            |
   +-------------+------------------------------------------------------------+
   |halign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |valign       |Only used if the alignment property not set.                |
   +-------------+------------------------------------------------------------+
   |border       |Specifies the number of pixels to put around the object in  |
   |             |the sizer, on the sides specified by the borderSides        |
   |             |argument, or by the value of the DefaultBorderLeft,         |
   |             |DefaultBorderRight, DefaultBorderTop, and                   |
   |             |DefaultBorderBottom boolean properties.                     |
   +-------------+------------------------------------------------------------+
   |borderSides  |Specifies the sides around the object to place the border   |
   |             |specified in the border argument or the DefaultBorder       |
   |             |property. This should be a tuple that contains at least     |
   |             |some of the values ("left", "right", "top", "bottom")       |
   +-------------+------------------------------------------------------------+


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32037:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.prependSpacer(self, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer in the first position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32038:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-32039:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.release(self, releaseContents=False)
   :noindex:


   
   Normally just destroys the sizer, leaving any objects
   controlled by the sizer intact. But if the 'releaseContents'
   parameter is passed as True, all objects contained in the
   sizer are destroyed first.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32040:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.remove(self, itm, destroy=None)
   :noindex:


   
   This will remove the item from the sizer. It will not cause
   the item to be destroyed unless the 'destroy' parameter is True.
   If the item is not one of this sizer's items, no error will be
   raised - it will simply do nothing.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32041:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.setItemProp(self, itm, prop, val)
   :noindex:


   
   Given a sizer item, a property and a value, sets things as you
   would expect.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32042:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.setItemProps(self, itm, props)
   :noindex:


   
   This accepts a dict of properties and values, and
   applies them to the specified sizer item.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32043:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.setPositionInSizer(self, obj, pos)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32044:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-32045:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-32046:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.showItem(self, itm)
   :noindex:


   Makes sure that the passed item is visible


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-32047:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32048:

.. function:: dabo.ui.uiwx.dSizer.dSizerV.unbindEvent(self, eventClass=None, function=None)
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
