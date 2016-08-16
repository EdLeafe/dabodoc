
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSizerMixin

.. _dabo.ui.uiwx.dSizerMixin.dSizerMixin:

================================================
|doc_title|  **dSizerMixin.dSizerMixin** - class
================================================


Provides the interface for interacting with Sizers in Dabo.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSizerMixin**

.. inheritance-diagram:: dSizerMixin


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dBorderSizer.dBorderSizer`
* :ref:`dabo.ui.uiwx.dGridSizer.dGridSizer`
* :ref:`dabo.ui.uiwx.dSizer.dSizer`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSizerMixin.dSizerMixin

   .. automethod:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.__init__

|method_summary| Properties Summary
===================================


====================================== ========================
:ref:`Application <no-31521>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-31522>`            The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-31523>`          Base key used when saving/restoring preferences  (str)
:ref:`ChildObjects <no-31524>`         List of all the objects (controls, sizers, spacers) that are directly managed
:ref:`ChildSizers <no-31525>`          List of all the sizers that are directly managed by this sizer  (list of sizers
:ref:`ChildSpacers <no-31526>`         List of all the spacer items that are directly managed by this sizer  (list of spacer items
:ref:`ChildWindows <no-31527>`         List of all the windows that are directly managed by this sizer  (list of controls
:ref:`Children <no-31528>`             List of all the sizer items managed by this sizer  (list of sizerItems
:ref:`Class <no-31529>`                The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-31530>`     Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-31531>` Reference to the sizer item that control's this control's layout.
:ref:`DefaultBorder <no-31532>`        Sets a default value for the border that will be applied to any controls added
:ref:`DefaultBorderAll <no-31533>`     When True, the DefaultBorder property is applied to all of the sides of
:ref:`DefaultBorderBottom <no-31534>`  Affects whether the DefaultBorder property is applied to the Bottom
:ref:`DefaultBorderLeft <no-31535>`    Affects whether the DefaultBorder property is applied to the Left
:ref:`DefaultBorderRight <no-31536>`   Affects whether the DefaultBorder property is applied to the Right
:ref:`DefaultBorderTop <no-31537>`     Affects whether the DefaultBorder property is applied to the Top
:ref:`DefaultSpacing <no-31538>`       Amount of space automatically inserted between elements.  (int)
:ref:`DynamicDefaultBorder <no-31539>` Dynamically determine the value of the DefaultBorder property.
:ref:`DynamicVisible <no-31540>`       Dynamically determine the value of the Visible property.
:ref:`Form <no-31541>`                 Form with which the sizer is associated.  (dForm or None)
:ref:`Height <no-31542>`               Height of the sizer  (int)
:ref:`LogEvents <no-31543>`            Specifies which events to log.  (list of strings)
:ref:`Name <no-31544>`                 The name of the object.  (str)
:ref:`Orientation <no-31545>`          Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.
:ref:`Parent <no-31546>`               The object that contains this sizer. In the case of nested
:ref:`PreferenceManager <no-31547>`    Reference to the Preference Management object  (dPref)
:ref:`Visible <no-31548>`              Specifies whether the sizer and contained items are shown  (bool)
:ref:`Width <no-31549>`                Width of this sizer  (int)

====================================== ========================


Properties
==========

.. _no-31524:

**ChildObjects** 

List of all the objects (controls, sizers, spacers) that are directly managed
    by this sizer  (list of objects



-------

.. _no-31525:

**ChildSizers** 

List of all the sizers that are directly managed by this sizer  (list of sizers



-------

.. _no-31526:

**ChildSpacers** 

List of all the spacer items that are directly managed by this sizer  (list of spacer items



-------

.. _no-31527:

**ChildWindows** 

List of all the windows that are directly managed by this sizer  (list of controls



-------

.. _no-31528:

**Children** 

List of all the sizer items managed by this sizer  (list of sizerItems



-------

.. _no-31530:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)



-------

.. _no-31531:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.
        This is useful for getting information about how the item is being
        sized, and for changing those settings.



-------

.. _no-31532:

**DefaultBorder** 

Sets a default value for the border that will be applied to any controls added
    to the sizer afterwards for whom an explicit value for the border is not set.
    Note that it does not affect the border of items already added to the control.
    This property is useful when you want to add a series of items to a sizer with
    the same border: just set this property once, and then add your items.
    Default=0  (int)



-------

.. _no-31533:

**DefaultBorderAll** 

When True, the DefaultBorder property is applied to all of the sides of
    any controls added to the sizer. If any of the individual side properties,
    such as DefaultBorderTop, are set to False, this property will return False.
    Setting DefaultBorderAll will effectively set all of the individual side properties
    to that value. Default=True  (bool)



-------

.. _no-31534:

**DefaultBorderBottom** 

Affects whether the DefaultBorder property is applied to the Bottom
    side of controls added to the sizer. Default=True  (bool)



-------

.. _no-31535:

**DefaultBorderLeft** 

Affects whether the DefaultBorder property is applied to the Left
    side of controls added to the sizer. Default=True  (bool)



-------

.. _no-31536:

**DefaultBorderRight** 

Affects whether the DefaultBorder property is applied to the Right
    side of controls added to the sizer. Default=True  (bool)



-------

.. _no-31537:

**DefaultBorderTop** 

Affects whether the DefaultBorder property is applied to the Top
    side of controls added to the sizer. Default=True  (bool)



-------

.. _no-31538:

**DefaultSpacing** 

Amount of space automatically inserted between elements.  (int)



-------

.. _no-31539:

**DynamicDefaultBorder** 

Dynamically determine the value of the DefaultBorder property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultBorder property. If DynamicDefaultBorder is set to None (the default), DefaultBorder
will not be dynamically evaluated.



-------

.. _no-31540:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.



-------

.. _no-31541:

**Form** 

Form with which the sizer is associated.  (dForm or None)



-------

.. _no-31542:

**Height** 

Height of the sizer  (int)



-------

.. _no-31545:

**Orientation** 

Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.



-------

.. _no-31548:

**Visible** 

Specifies whether the sizer and contained items are shown  (bool)



-------

.. _no-31549:

**Width** 

Width of this sizer  (int)



-------


Properties - inherited
========================

.. _no-31521:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31522:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31523:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31529:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31543:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31544:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31546:

**Parent** 

The object that contains this sizer. In the case of nested
    sizers, it is the object that the outermost sizer belongs to. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31547:

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
:ref:`addDefaultSpacer <no-31550>`      
:ref:`addSpacer <no-31551>`             
:ref:`afterInit <no-31552>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`append <no-31553>`                Adds the passed object to the end of the sizer layout.
:ref:`append1x <no-31554>`              Shorthand for sizer.append(obj, 1, "expand").
:ref:`appendItems <no-31555>`           Append each item to the sizer.
:ref:`appendSpacer <no-31556>`          Appends a spacer to the sizer.
:ref:`autoBindEvents <no-31557>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-31558>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-31559>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-31560>`            Bind a sequence of [dEvent, callback] lists.
:ref:`clear <no-31561>`                 This method is called to remove all items from the sizer. If the
:ref:`drawOutline <no-31562>`           There are some cases where being able to see the sizer
:ref:`getAbsoluteName <no-31563>`       Return the fully qualified name of the object.
:ref:`getContainingWindow <no-31564>`   
:ref:`getItem <no-31565>`               Querying sizers for their contents returns sizer items, not
:ref:`getItemProp <no-31566>`           Get the current value of the specified property for the sizer item.
:ref:`getItemProps <no-31567>`          Returns a dict containing all the sizer properties as keys along with
:ref:`getPositionInSizer <no-31568>`    Returns the current position of this sizer in its containing sizer, or None
:ref:`getProperties <no-31569>`         Returns a dictionary of property name/value pairs.
:ref:`hideItem <no-31570>`              Hides the passed item
:ref:`initEvents <no-31571>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-31572>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-31573>`                Inserts the passed object into the sizer layout at the specified position.
:ref:`insertSpacer <no-31574>`          Added to be consistent with the sizers' add/insert
:ref:`isContainedBy <no-31575>`         Returns True if this the containership hierarchy for this control
:ref:`layout <no-31576>`                Layout the items in the sizer.
:ref:`listMembers <no-31577>`           Debugging method. This will list all the members of this sizer,
:ref:`prepend <no-31578>`               Insert the object at the beginning of the sizer layout.
:ref:`prependSpacer <no-31579>`         Added to be consistent with the sizers' add/insert
:ref:`raiseEvent <no-31580>`            Send the event to all registered listeners.
:ref:`release <no-31581>`               Normally just destroys the sizer, leaving any objects
:ref:`remove <no-31582>`                This will remove the item from the sizer. It will not cause
:ref:`setItemProp <no-31583>`           Given a sizer item, a property and a value, sets things as you
:ref:`setItemProps <no-31584>`          This accepts a dict of properties and values, and
:ref:`setPositionInSizer <no-31585>`    
:ref:`setProperties <no-31586>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-31587>` Sets a group of properties on the object all at once. This
:ref:`showItem <no-31588>`              Makes sure that the passed item is visible
:ref:`super <no-31589>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-31590>`           Remove a previously registered event binding.

======================================= ========================


Methods
=======

.. _no-31550:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.addDefaultSpacer(self, pos=None)



-------

.. _no-31551:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.addSpacer(self, val, pos=None, proportion=0)



-------

.. _no-31553:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.append(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)

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



-------

.. _no-31554:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.append1x(self, obj, \**kwargs)

   Shorthand for sizer.append(obj, 1, "expand").



-------

.. _no-31555:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.appendItems(self, items, \*args, \**kwargs)

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



-------

.. _no-31556:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.appendSpacer(self, val, proportion=0)

   Appends a spacer to the sizer.



-------

.. _no-31561:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.clear(self, destroy=False)

   
   This method is called to remove all items from the sizer. If the
   optional 'destroy' parameter is set to True, any contained items
   will be destroyed. Otherwise, they will remain as is, but no longer
   under control of the sizer.
   



-------

.. _no-31562:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.drawOutline(self, win, recurse=False, drawChildren=False)

   
   There are some cases where being able to see the sizer
   is helpful, such as at design time. This method can be called
   to see the outline; it needs to be called whenever the containing
   window is resized or repainted.
   



-------

.. _no-31564:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.getContainingWindow(self, \*args, \**kwargs)



-------

.. _no-31565:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.getItem(self, szItem)

   
   Querying sizers for their contents returns sizer items, not
   the actual items. So given a sizer item, this method will return
   the actual item in the sizer.
   



-------

.. _no-31566:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.getItemProp(self, itm, prop)

   
   Get the current value of the specified property for the sizer item.
   Grid sizers must override with their specific props.
   



-------

.. _no-31567:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.getItemProps(self, itm)

   
   Returns a dict containing all the sizer properties as keys along with
   their associated values.
   



-------

.. _no-31568:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.getPositionInSizer(self)

   
   Returns the current position of this sizer in its containing sizer, or None
   if there isn't a containing sizer.
   



-------

.. _no-31570:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.hideItem(self, itm)

   Hides the passed item



-------

.. _no-31573:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.insert(self, index, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)

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



-------

.. _no-31574:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.insertSpacer(self, pos, val, proportion=0)

   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer at the specified position.
   



-------

.. _no-31575:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.isContainedBy(self, obj)

   
   Returns True if this the containership hierarchy for this control
   includes obj.
   



-------

.. _no-31576:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.layout(self)

   
   Layout the items in the sizer.
   
   This is handled automatically when the sizer is resized, but you'll have
   to call it manually after you are done adding items to the sizer.
   



-------

.. _no-31577:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.listMembers(self, recurse=False, lvl=0)

   
   Debugging method. This will list all the members of this sizer,
   and if recurse is True, drill down into all contained sizers.
   



-------

.. _no-31578:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.prepend(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)

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



-------

.. _no-31579:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.prependSpacer(self, val, proportion=0)

   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer in the first position.
   



-------

.. _no-31581:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.release(self, releaseContents=False)

   
   Normally just destroys the sizer, leaving any objects
   controlled by the sizer intact. But if the 'releaseContents'
   parameter is passed as True, all objects contained in the
   sizer are destroyed first.
   



-------

.. _no-31582:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.remove(self, itm, destroy=None)

   
   This will remove the item from the sizer. It will not cause
   the item to be destroyed unless the 'destroy' parameter is True.
   If the item is not one of this sizer's items, no error will be
   raised - it will simply do nothing.
   



-------

.. _no-31583:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.setItemProp(self, itm, prop, val)

   
   Given a sizer item, a property and a value, sets things as you
   would expect.
   



-------

.. _no-31584:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.setItemProps(self, itm, props)

   
   This accepts a dict of properties and values, and
   applies them to the specified sizer item.
   



-------

.. _no-31585:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.setPositionInSizer(self, obj, pos)



-------

.. _no-31588:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.showItem(self, itm)

   Makes sure that the passed item is visible



-------


Methods - inherited
=====================

.. _no-31552:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31557:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.autoBindEvents(self, force=True)
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

.. _no-31558:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31559:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31560:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31563:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31569:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-31571:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31572:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31580:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-31586:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-31587:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-31589:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31590:

.. function:: dabo.ui.uiwx.dSizerMixin.dSizerMixin.unbindEvent(self, eventClass=None, function=None)
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
