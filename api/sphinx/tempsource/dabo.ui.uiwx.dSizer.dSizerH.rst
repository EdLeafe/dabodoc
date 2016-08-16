
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSizer

.. _dabo.ui.uiwx.dSizer.dSizerH:

=======================================
|doc_title|  **dSizer.dSizerH** - class
=======================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSizerH**

.. inheritance-diagram:: dSizerH


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dSizer.dSizer`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSizer.dSizerH

   .. automethod:: dabo.ui.uiwx.dSizer.dSizerH.__init__

|method_summary| Properties Summary
===================================


====================================== ========================
:ref:`Application <no-31907>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-31908>`            The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-31909>`          Base key used when saving/restoring preferences  (str)
:ref:`ChildObjects <no-31910>`         List of all the objects (controls, sizers, spacers) that are directly managed
:ref:`ChildSizers <no-31911>`          List of all the sizers that are directly managed by this sizer  (list of sizers
:ref:`ChildSpacers <no-31912>`         List of all the spacer items that are directly managed by this sizer  (list of spacer items
:ref:`ChildWindows <no-31913>`         List of all the windows that are directly managed by this sizer  (list of controls
:ref:`Children <no-31914>`             List of all the sizer items managed by this sizer  (list of sizerItems
:ref:`Class <no-31915>`                The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-31916>`     Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-31917>` Reference to the sizer item that control's this control's layout.
:ref:`DefaultBorder <no-31918>`        Sets a default value for the border that will be applied to any controls added
:ref:`DefaultBorderAll <no-31919>`     When True, the DefaultBorder property is applied to all of the sides of
:ref:`DefaultBorderBottom <no-31920>`  Affects whether the DefaultBorder property is applied to the Bottom
:ref:`DefaultBorderLeft <no-31921>`    Affects whether the DefaultBorder property is applied to the Left
:ref:`DefaultBorderRight <no-31922>`   Affects whether the DefaultBorder property is applied to the Right
:ref:`DefaultBorderTop <no-31923>`     Affects whether the DefaultBorder property is applied to the Top
:ref:`DefaultSpacing <no-31924>`       Amount of space automatically inserted between elements.  (int)
:ref:`DynamicDefaultBorder <no-31925>` Dynamically determine the value of the DefaultBorder property.
:ref:`DynamicVisible <no-31926>`       Dynamically determine the value of the Visible property.
:ref:`Form <no-31927>`                 Form with which the sizer is associated.  (dForm or None)
:ref:`Height <no-31928>`               Height of the sizer  (int)
:ref:`LogEvents <no-31929>`            Specifies which events to log.  (list of strings)
:ref:`Name <no-31930>`                 The name of the object.  (str)
:ref:`Orientation <no-31931>`          Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.
:ref:`Parent <no-31932>`               The object that contains this sizer. In the case of nested
:ref:`PreferenceManager <no-31933>`    Reference to the Preference Management object  (dPref)
:ref:`Visible <no-31934>`              Specifies whether the sizer and contained items are shown  (bool)
:ref:`Width <no-31935>`                Width of this sizer  (int)

====================================== ========================


Properties - inherited
========================

.. _no-31907:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31908:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31909:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31910:

**ChildObjects** 

List of all the objects (controls, sizers, spacers) that are directly managed
    by this sizer  (list of objects


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31911:

**ChildSizers** 

List of all the sizers that are directly managed by this sizer  (list of sizers


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31912:

**ChildSpacers** 

List of all the spacer items that are directly managed by this sizer  (list of spacer items


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31913:

**ChildWindows** 

List of all the windows that are directly managed by this sizer  (list of controls


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31914:

**Children** 

List of all the sizer items managed by this sizer  (list of sizerItems


Inherited from: 'wx._core.Sizer - can not provide a link

-------

.. _no-31915:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31916:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31917:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.
        This is useful for getting information about how the item is being
        sized, and for changing those settings.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31918:

**DefaultBorder** 

Sets a default value for the border that will be applied to any controls added
    to the sizer afterwards for whom an explicit value for the border is not set.
    Note that it does not affect the border of items already added to the control.
    This property is useful when you want to add a series of items to a sizer with
    the same border: just set this property once, and then add your items.
    Default=0  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31919:

**DefaultBorderAll** 

When True, the DefaultBorder property is applied to all of the sides of
    any controls added to the sizer. If any of the individual side properties,
    such as DefaultBorderTop, are set to False, this property will return False.
    Setting DefaultBorderAll will effectively set all of the individual side properties
    to that value. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31920:

**DefaultBorderBottom** 

Affects whether the DefaultBorder property is applied to the Bottom
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31921:

**DefaultBorderLeft** 

Affects whether the DefaultBorder property is applied to the Left
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31922:

**DefaultBorderRight** 

Affects whether the DefaultBorder property is applied to the Right
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31923:

**DefaultBorderTop** 

Affects whether the DefaultBorder property is applied to the Top
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31924:

**DefaultSpacing** 

Amount of space automatically inserted between elements.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31925:

**DynamicDefaultBorder** 

Dynamically determine the value of the DefaultBorder property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultBorder property. If DynamicDefaultBorder is set to None (the default), DefaultBorder
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31926:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31927:

**Form** 

Form with which the sizer is associated.  (dForm or None)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31928:

**Height** 

Height of the sizer  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31929:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31930:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31931:

**Orientation** 

Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.


Inherited from: 'wx._core.BoxSizer - can not provide a link

-------

.. _no-31932:

**Parent** 

The object that contains this sizer. In the case of nested
    sizers, it is the object that the outermost sizer belongs to. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31933:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31934:

**Visible** 

Specifies whether the sizer and contained items are shown  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31935:

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
:ref:`addDefaultSpacer <no-31936>`      
:ref:`addSpacer <no-31937>`             
:ref:`afterInit <no-31938>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`append <no-31939>`                Adds the passed object to the end of the sizer layout.
:ref:`append1x <no-31940>`              Shorthand for sizer.append(obj, 1, "expand").
:ref:`appendItems <no-31941>`           Append each item to the sizer.
:ref:`appendSpacer <no-31942>`          Appends a spacer to the sizer.
:ref:`autoBindEvents <no-31943>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-31944>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-31945>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-31946>`            Bind a sequence of [dEvent, callback] lists.
:ref:`clear <no-31947>`                 This method is called to remove all items from the sizer. If the
:ref:`drawOutline <no-31948>`           There are some cases where being able to see the sizer
:ref:`getAbsoluteName <no-31949>`       Return the fully qualified name of the object.
:ref:`getBorderedClass <no-31950>`      Return the class that is the border sizer version of this class.
:ref:`getContainingWindow <no-31951>`   
:ref:`getItem <no-31952>`               Querying sizers for their contents returns sizer items, not
:ref:`getItemProp <no-31953>`           Get the current value of the specified property for the sizer item.
:ref:`getItemProps <no-31954>`          Returns a dict containing all the sizer properties as keys along with
:ref:`getPositionInSizer <no-31955>`    Returns the current position of this sizer in its containing sizer, or None
:ref:`getProperties <no-31956>`         Returns a dictionary of property name/value pairs.
:ref:`hideItem <no-31957>`              Hides the passed item
:ref:`initEvents <no-31958>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-31959>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-31960>`                Inserts the passed object into the sizer layout at the specified position.
:ref:`insertSpacer <no-31961>`          Added to be consistent with the sizers' add/insert
:ref:`isContainedBy <no-31962>`         Returns True if this the containership hierarchy for this control
:ref:`layout <no-31963>`                Layout the items in the sizer.
:ref:`listMembers <no-31964>`           Debugging method. This will list all the members of this sizer,
:ref:`prepend <no-31965>`               Insert the object at the beginning of the sizer layout.
:ref:`prependSpacer <no-31966>`         Added to be consistent with the sizers' add/insert
:ref:`raiseEvent <no-31967>`            Send the event to all registered listeners.
:ref:`release <no-31968>`               Normally just destroys the sizer, leaving any objects
:ref:`remove <no-31969>`                This will remove the item from the sizer. It will not cause
:ref:`setItemProp <no-31970>`           Given a sizer item, a property and a value, sets things as you
:ref:`setItemProps <no-31971>`          This accepts a dict of properties and values, and
:ref:`setPositionInSizer <no-31972>`    
:ref:`setProperties <no-31973>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-31974>` Sets a group of properties on the object all at once. This
:ref:`showItem <no-31975>`              Makes sure that the passed item is visible
:ref:`super <no-31976>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-31977>`           Remove a previously registered event binding.

======================================= ========================


Methods - inherited
=====================

.. _no-31936:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.addDefaultSpacer(self, pos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31937:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.addSpacer(self, val, pos=None, proportion=0)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31938:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31939:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.append(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
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

.. _no-31940:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.append1x(self, obj, \**kwargs)
   :noindex:


   Shorthand for sizer.append(obj, 1, "expand").


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31941:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.appendItems(self, items, \*args, \**kwargs)
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

.. _no-31942:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.appendSpacer(self, val, proportion=0)
   :noindex:


   Appends a spacer to the sizer.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31943:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.autoBindEvents(self, force=True)
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

.. _no-31944:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31945:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31946:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31947:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.clear(self, destroy=False)
   :noindex:


   
   This method is called to remove all items from the sizer. If the
   optional 'destroy' parameter is set to True, any contained items
   will be destroyed. Otherwise, they will remain as is, but no longer
   under control of the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31948:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.drawOutline(self, win, recurse=False, drawChildren=False)
   :noindex:


   
   There are some cases where being able to see the sizer
   is helpful, such as at design time. This method can be called
   to see the outline; it needs to be called whenever the containing
   window is resized or repainted.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31949:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31950:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getBorderedClass(self)
   :noindex:


   Return the class that is the border sizer version of this class.


Inherited from: :ref:`dabo.ui.uiwx.dSizer.dSizer`

-------

.. _no-31951:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getContainingWindow(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31952:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getItem(self, szItem)
   :noindex:


   
   Querying sizers for their contents returns sizer items, not
   the actual items. So given a sizer item, this method will return
   the actual item in the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31953:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getItemProp(self, itm, prop)
   :noindex:


   
   Get the current value of the specified property for the sizer item.
   Grid sizers must override with their specific props.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31954:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getItemProps(self, itm)
   :noindex:


   
   Returns a dict containing all the sizer properties as keys along with
   their associated values.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31955:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getPositionInSizer(self)
   :noindex:


   
   Returns the current position of this sizer in its containing sizer, or None
   if there isn't a containing sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31956:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-31957:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.hideItem(self, itm)
   :noindex:


   Hides the passed item


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31958:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31959:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31960:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.insert(self, index, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
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

.. _no-31961:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.insertSpacer(self, pos, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer at the specified position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31962:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.isContainedBy(self, obj)
   :noindex:


   
   Returns True if this the containership hierarchy for this control
   includes obj.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31963:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.layout(self)
   :noindex:


   
   Layout the items in the sizer.
   
   This is handled automatically when the sizer is resized, but you'll have
   to call it manually after you are done adding items to the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31964:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.listMembers(self, recurse=False, lvl=0)
   :noindex:


   
   Debugging method. This will list all the members of this sizer,
   and if recurse is True, drill down into all contained sizers.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31965:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.prepend(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
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

.. _no-31966:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.prependSpacer(self, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer in the first position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31967:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-31968:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.release(self, releaseContents=False)
   :noindex:


   
   Normally just destroys the sizer, leaving any objects
   controlled by the sizer intact. But if the 'releaseContents'
   parameter is passed as True, all objects contained in the
   sizer are destroyed first.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31969:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.remove(self, itm, destroy=None)
   :noindex:


   
   This will remove the item from the sizer. It will not cause
   the item to be destroyed unless the 'destroy' parameter is True.
   If the item is not one of this sizer's items, no error will be
   raised - it will simply do nothing.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31970:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.setItemProp(self, itm, prop, val)
   :noindex:


   
   Given a sizer item, a property and a value, sets things as you
   would expect.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31971:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.setItemProps(self, itm, props)
   :noindex:


   
   This accepts a dict of properties and values, and
   applies them to the specified sizer item.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31972:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.setPositionInSizer(self, obj, pos)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31973:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-31974:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-31975:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.showItem(self, itm)
   :noindex:


   Makes sure that the passed item is visible


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-31976:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31977:

.. function:: dabo.ui.uiwx.dSizer.dSizerH.unbindEvent(self, eventClass=None, function=None)
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
