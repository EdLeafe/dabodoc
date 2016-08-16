
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dGridSizer

.. _dabo.ui.uiwx.dGridSizer.dGridSizer:

==============================================
|doc_title|  **dGridSizer.dGridSizer** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dGridSizer**

.. inheritance-diagram:: dGridSizer


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dGridSizer.png
          :scale: 75 %
          :target: _static/macWidgets/dGridSizer.png
          :alt: dGridSizer



     - no image available



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dGridSizer.dGridSizer

   .. automethod:: dabo.ui.uiwx.dGridSizer.dGridSizer.__init__

|method_summary| Properties Summary
===================================


====================================== ========================
:ref:`Application <no-19690>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-19691>`            The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-19692>`          Base key used when saving/restoring preferences  (str)
:ref:`ChildObjects <no-19693>`         List of all the objects (controls, sizers, spacers) that are directly managed
:ref:`ChildSizers <no-19694>`          List of all the sizers that are directly managed by this sizer  (list of sizers
:ref:`ChildSpacers <no-19695>`         List of all the spacer items that are directly managed by this sizer  (list of spacer items
:ref:`ChildWindows <no-19696>`         List of all the windows that are directly managed by this sizer  (list of controls
:ref:`Children <no-19697>`             List of all the sizer items managed by this sizer  (list of sizerItems
:ref:`Class <no-19698>`                The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-19699>`     Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-19700>` Reference to the sizer item that control's this control's layout.
:ref:`DefaultBorder <no-19701>`        Sets a default value for the border that will be applied to any controls added
:ref:`DefaultBorderAll <no-19702>`     When True, the DefaultBorder property is applied to all of the sides of
:ref:`DefaultBorderBottom <no-19703>`  Affects whether the DefaultBorder property is applied to the Bottom
:ref:`DefaultBorderLeft <no-19704>`    Affects whether the DefaultBorder property is applied to the Left
:ref:`DefaultBorderRight <no-19705>`   Affects whether the DefaultBorder property is applied to the Right
:ref:`DefaultBorderTop <no-19706>`     Affects whether the DefaultBorder property is applied to the Top
:ref:`DefaultSpacing <no-19707>`       Amount of space automatically inserted between elements.  (int)
:ref:`DynamicDefaultBorder <no-19708>` Dynamically determine the value of the DefaultBorder property.
:ref:`DynamicHGap <no-19709>`          Dynamically determine the value of the HGap property.
:ref:`DynamicMaxCols <no-19710>`       Dynamically determine the value of the MaxCols property.
:ref:`DynamicMaxDimension <no-19711>`  Dynamically determine the value of the MaxDimension property.
:ref:`DynamicMaxRows <no-19712>`       Dynamically determine the value of the MaxRows property.
:ref:`DynamicOrientation <no-19713>`   Dynamically determine the value of the Orientation property.
:ref:`DynamicVGap <no-19714>`          Dynamically determine the value of the VGap property.
:ref:`DynamicVisible <no-19715>`       Dynamically determine the value of the Visible property.
:ref:`Form <no-19716>`                 Form with which the sizer is associated.  (dForm or None)
:ref:`HGap <no-19717>`                 Horizontal gap between cells in the sizer  (int)
:ref:`Height <no-19718>`               Height of the sizer  (int)
:ref:`HighCol <no-19719>`              Highest col position that contains any item. Read-only.  (int)
:ref:`HighRow <no-19720>`              Highest row position that contains any item. Read-only.  (int)
:ref:`LogEvents <no-19721>`            Specifies which events to log.  (list of strings)
:ref:`MaxCols <no-19722>`              When adding elements to the sizer, controls the max number of columns to add before a new row is sta
:ref:`MaxDimension <no-19723>`         When adding elements to the sizer, this property determines  if we use rows or columns as the limiti
:ref:`MaxRows <no-19724>`              When adding elements to the sizer, controls the max number of rows to add before a new column is sta
:ref:`Name <no-19725>`                 The name of the object.  (str)
:ref:`Orientation <no-19726>`          Alias for the MaxDimensions property. (char: 'r' or 'c'(default) )
:ref:`Parent <no-19727>`               The object that contains this sizer. In the case of nested
:ref:`PreferenceManager <no-19728>`    Reference to the Preference Management object  (dPref)
:ref:`VGap <no-19729>`                 Vertical gap between cells in the sizer  (int)
:ref:`Visible <no-19730>`              Specifies whether the sizer and contained items are shown  (bool)
:ref:`Width <no-19731>`                Width of this sizer  (int)

====================================== ========================


Properties
==========

.. _no-19709:

**DynamicHGap** 

Dynamically determine the value of the HGap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HGap property. If DynamicHGap is set to None (the default), HGap
will not be dynamically evaluated.



-------

.. _no-19710:

**DynamicMaxCols** 

Dynamically determine the value of the MaxCols property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MaxCols property. If DynamicMaxCols is set to None (the default), MaxCols
will not be dynamically evaluated.



-------

.. _no-19711:

**DynamicMaxDimension** 

Dynamically determine the value of the MaxDimension property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MaxDimension property. If DynamicMaxDimension is set to None (the default), MaxDimension
will not be dynamically evaluated.



-------

.. _no-19712:

**DynamicMaxRows** 

Dynamically determine the value of the MaxRows property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MaxRows property. If DynamicMaxRows is set to None (the default), MaxRows
will not be dynamically evaluated.



-------

.. _no-19713:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-19714:

**DynamicVGap** 

Dynamically determine the value of the VGap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VGap property. If DynamicVGap is set to None (the default), VGap
will not be dynamically evaluated.



-------

.. _no-19719:

**HighCol** 

Highest col position that contains any item. Read-only.  (int)



-------

.. _no-19720:

**HighRow** 

Highest row position that contains any item. Read-only.  (int)



-------

.. _no-19722:

**MaxCols** 

When adding elements to the sizer, controls the max number of columns to add before a new row is started. (int)



-------

.. _no-19723:

**MaxDimension** 

When adding elements to the sizer, this property determines  if we use rows or columns as the limiting value. (char: 'r' or 'c'(default) )



-------

.. _no-19724:

**MaxRows** 

When adding elements to the sizer, controls the max number of rows to add before a new column is started. (int)



-------


Properties - inherited
========================

.. _no-19690:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19691:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19692:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19693:

**ChildObjects** 

List of all the objects (controls, sizers, spacers) that are directly managed
    by this sizer  (list of objects


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19694:

**ChildSizers** 

List of all the sizers that are directly managed by this sizer  (list of sizers


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19695:

**ChildSpacers** 

List of all the spacer items that are directly managed by this sizer  (list of spacer items


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19696:

**ChildWindows** 

List of all the windows that are directly managed by this sizer  (list of controls


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19697:

**Children** 

List of all the sizer items managed by this sizer  (list of sizerItems


Inherited from: 'wx._core.Sizer - can not provide a link

-------

.. _no-19698:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19699:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19700:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.
        This is useful for getting information about how the item is being
        sized, and for changing those settings.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19701:

**DefaultBorder** 

Sets a default value for the border that will be applied to any controls added
    to the sizer afterwards for whom an explicit value for the border is not set.
    Note that it does not affect the border of items already added to the control.
    This property is useful when you want to add a series of items to a sizer with
    the same border: just set this property once, and then add your items.
    Default=0  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19702:

**DefaultBorderAll** 

When True, the DefaultBorder property is applied to all of the sides of
    any controls added to the sizer. If any of the individual side properties,
    such as DefaultBorderTop, are set to False, this property will return False.
    Setting DefaultBorderAll will effectively set all of the individual side properties
    to that value. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19703:

**DefaultBorderBottom** 

Affects whether the DefaultBorder property is applied to the Bottom
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19704:

**DefaultBorderLeft** 

Affects whether the DefaultBorder property is applied to the Left
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19705:

**DefaultBorderRight** 

Affects whether the DefaultBorder property is applied to the Right
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19706:

**DefaultBorderTop** 

Affects whether the DefaultBorder property is applied to the Top
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19707:

**DefaultSpacing** 

Amount of space automatically inserted between elements.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19708:

**DynamicDefaultBorder** 

Dynamically determine the value of the DefaultBorder property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultBorder property. If DynamicDefaultBorder is set to None (the default), DefaultBorder
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19715:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19716:

**Form** 

Form with which the sizer is associated.  (dForm or None)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19717:

**HGap** 

Horizontal gap between cells in the sizer  (int)


Inherited from: 'wx._core.GridSizer - can not provide a link

-------

.. _no-19718:

**Height** 

Height of the sizer  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19721:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19725:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19726:

**Orientation** 

Alias for the MaxDimensions property. (char: 'r' or 'c'(default) )


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19727:

**Parent** 

The object that contains this sizer. In the case of nested
    sizers, it is the object that the outermost sizer belongs to. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19728:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19729:

**VGap** 

Vertical gap between cells in the sizer  (int)


Inherited from: 'wx._core.GridSizer - can not provide a link

-------

.. _no-19730:

**Visible** 

Specifies whether the sizer and contained items are shown  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19731:

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
:ref:`addDefaultSpacer <no-19732>`      
:ref:`addSpacer <no-19733>`             
:ref:`afterInit <no-19734>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`append <no-19735>`                Inserts the passed item at the specified position in the grid. If no
:ref:`append1x <no-19736>`              Shorthand for sizer.append(obj, 1, "expand").
:ref:`appendItems <no-19737>`           Shortcut for appending multiple items at once.
:ref:`appendSpacer <no-19738>`          Alias for append()
:ref:`autoBindEvents <no-19739>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-19740>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-19741>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-19742>`            Bind a sequence of [dEvent, callback] lists.
:ref:`clear <no-19743>`                 This method is called to remove all items from the sizer. If the
:ref:`copyGrid <no-19744>`              This method takes an existing GridSizer, and moves
:ref:`drawOutline <no-19745>`           Need to override this method to draw the outline
:ref:`findFirstEmptyCell <no-19746>`    The idea is this: use the MaxDimension to determine how
:ref:`getAbsoluteName <no-19747>`       Return the fully qualified name of the object.
:ref:`getColExpand <no-19748>`          Returns True if the specified column is growable.
:ref:`getContainingWindow <no-19749>`   
:ref:`getGridPos <no-19750>`            Given an object that is contained in this grid
:ref:`getGridSpan <no-19751>`           Given an object that is contained in this grid
:ref:`getItem <no-19752>`               Querying sizers for their contents returns sizer items, not
:ref:`getItemAtOffset <no-19753>`       Given an object and a (row, col) offset, returns
:ref:`getItemByRowCol <no-19754>`       Returns either the managed item or the sizer item at the
:ref:`getItemProp <no-19755>`           
:ref:`getItemProps <no-19756>`          Returns a dict containing all the sizer properties as keys along with
:ref:`getNeighbor <no-19757>`           Returns the object adjacent to the given object. Possible
:ref:`getPositionInSizer <no-19758>`    Returns the current position of this sizer in its containing sizer, or None
:ref:`getProperties <no-19759>`         Returns a dictionary of property name/value pairs.
:ref:`getRowExpand <no-19760>`          Returns True if the specified row is growable.
:ref:`hideItem <no-19761>`              Hides the passed item
:ref:`initEvents <no-19762>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-19763>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-19764>`                This is not supported for this type of sizer
:ref:`insertSpacer <no-19765>`          Added to be consistent with the sizers' add/insert
:ref:`isContainedBy <no-19766>`         Returns True if this the containership hierarchy for this control
:ref:`layout <no-19767>`                Layout the items in the sizer.
:ref:`listMembers <no-19768>`           Debugging method. This will list all the members of this sizer,
:ref:`moveCell <no-19769>`              Move the contents of the specified cell to the target
:ref:`moveObject <no-19770>`            Moves the object to the given row/col if possible.
:ref:`prepend <no-19771>`               Insert the object at the beginning of the sizer layout.
:ref:`prependSpacer <no-19772>`         Added to be consistent with the sizers' add/insert
:ref:`raiseEvent <no-19773>`            Send the event to all registered listeners.
:ref:`release <no-19774>`               Normally just destroys the sizer, leaving any objects
:ref:`remove <no-19775>`                This will remove the item from the sizer. It will not cause
:ref:`removeCol <no-19776>`             Deletes any items contained in the specified column, and
:ref:`removeRow <no-19777>`             Deletes any items contained in the specified row, and
:ref:`setColExpand <no-19778>`          Sets the 'growable' status of one or more columns.
:ref:`setColSpan <no-19779>`            Sets the col span, keeping the row span the same.
:ref:`setFullCollapse <no-19780>`       Convenience method for setting all columns and rows of the
:ref:`setFullExpand <no-19781>`         Convenience method for setting all columns and rows of the
:ref:`setGridSpan <no-19782>`           Given an object that is contained in this grid
:ref:`setItemProp <no-19783>`           Given a sizer item, a property and a value, sets things as you
:ref:`setItemProps <no-19784>`          This accepts a dict of properties and values, and
:ref:`setPositionInSizer <no-19785>`    
:ref:`setProperties <no-19786>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-19787>` Sets a group of properties on the object all at once. This
:ref:`setRowExpand <no-19788>`          Sets the 'growable' status of one or more rows.
:ref:`setRowSpan <no-19789>`            Sets the row span, keeping the col span the same.
:ref:`showItem <no-19790>`              Makes sure that the passed item is visible
:ref:`super <no-19791>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-19792>`           Remove a previously registered event binding.

======================================= ========================


Methods
=======

.. _no-19735:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.append(self, item, layout='normal', row=-1, col=-1, rowSpan=1, colSpan=1, alignment=None, halign='left', valign='middle', border=0, borderSides=('all',), flag=None)

   
   Inserts the passed item at the specified position in the grid. If no
   position is specified, the item is inserted at the first available open
   cell as specified by the Max* properties.
   



-------

.. _no-19737:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.appendItems(self, items, \*args, \**kwargs)

   Shortcut for appending multiple items at once.



-------

.. _no-19738:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.appendSpacer(self, \*args, \**kwargs)

   Alias for append()



-------

.. _no-19744:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.copyGrid(self, oldGrid)

   
   This method takes an existing GridSizer, and moves
   the contents to the current grid. The properties of each
   cell's item are preserved, but row/column Expand settings
   must be handled separately.
   



-------

.. _no-19745:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.drawOutline(self, win, recurse=False, drawChildren=False)

   
   Need to override this method to draw the outline
   properly for the grid.
   



-------

.. _no-19746:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.findFirstEmptyCell(self)

   
   The idea is this: use the MaxDimension to determine how
   we look through the grid. When we find an empty cell, return
   its coordinates.
   



-------

.. _no-19748:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getColExpand(self, col)

   Returns True if the specified column is growable.



-------

.. _no-19750:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getGridPos(self, obj)

   
   Given an object that is contained in this grid
   sizer, returns a (row,col) tuple for that item's location.
   



-------

.. _no-19751:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getGridSpan(self, obj)

   
   Given an object that is contained in this grid
   sizer, returns a (row,col) tuple for that item's cell span.
   



-------

.. _no-19753:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getItemAtOffset(self, obj, off)

   
   Given an object and a (row, col) offset, returns
   the object at the offset position, or None if no such
   object exists.
   



-------

.. _no-19754:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getItemByRowCol(self, row, col, returnObject=True)

   
   Returns either the managed item or the sizer item at the
   given position if one exists. If not, returns None.
   



-------

.. _no-19755:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getItemProp(self, itm, prop)



-------

.. _no-19757:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getNeighbor(self, obj, dir)

   
   Returns the object adjacent to the given object. Possible
   values for 'dir' are: left, right, up, down.
   



-------

.. _no-19760:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getRowExpand(self, row)

   Returns True if the specified row is growable.



-------

.. _no-19764:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.insert(self, \*args, \**kwargs)

   This is not supported for this type of sizer



-------

.. _no-19769:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.moveCell(self, fromRow, fromCol, toRow, toCol, delay=False)

   
   Move the contents of the specified cell to the target
   location. By default, layout() is called; this can be changed when
   moving a number of cells by specifying delay=True. In this
   event, the calling code is responsible for calling layout() when all
   the moving is done.
   



-------

.. _no-19770:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.moveObject(self, obj, targetRow, targetCol, delay=False)

   Moves the object to the given row/col if possible.



-------

.. _no-19776:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.removeCol(self, colNum)

   
   Deletes any items contained in the specified column, and
   then moves all items to the right of it up to fill the space.
   



-------

.. _no-19777:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.removeRow(self, rowNum)

   
   Deletes any items contained in the specified row, and
   then moves all items below it up to fill the space.
   



-------

.. _no-19778:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setColExpand(self, expand, colNum, proportion=0)

   Sets the 'growable' status of one or more columns.



-------

.. _no-19779:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setColSpan(self, obj, colspan)

   Sets the col span, keeping the row span the same.



-------

.. _no-19780:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setFullCollapse(self)

   
   Convenience method for setting all columns and rows of the
   sizer to not be growable.
   



-------

.. _no-19781:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setFullExpand(self)

   
   Convenience method for setting all columns and rows of the
   sizer to be growable. Must be called after all items are added,
   as any rows or columns added after the call will be the default
   of non-growable.
   



-------

.. _no-19782:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setGridSpan(self, obj, row=None, col=None)

   
   Given an object that is contained in this grid
   sizer, sets its span to the given values. Returns
   True if successful, or False if it fails, due to another
   item in the way.
   



-------

.. _no-19788:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setRowExpand(self, expand, rowNum, proportion=0)

   Sets the 'growable' status of one or more rows.



-------

.. _no-19789:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setRowSpan(self, obj, rowspan)

   Sets the row span, keeping the col span the same.



-------


Methods - inherited
=====================

.. _no-19732:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.addDefaultSpacer(self, pos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19733:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.addSpacer(self, val, pos=None, proportion=0)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19734:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19736:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.append1x(self, obj, \**kwargs)
   :noindex:


   Shorthand for sizer.append(obj, 1, "expand").


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19739:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.autoBindEvents(self, force=True)
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

.. _no-19740:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19741:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19742:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19743:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.clear(self, destroy=False)
   :noindex:


   
   This method is called to remove all items from the sizer. If the
   optional 'destroy' parameter is set to True, any contained items
   will be destroyed. Otherwise, they will remain as is, but no longer
   under control of the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19747:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19749:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getContainingWindow(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19752:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getItem(self, szItem)
   :noindex:


   
   Querying sizers for their contents returns sizer items, not
   the actual items. So given a sizer item, this method will return
   the actual item in the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19756:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getItemProps(self, itm)
   :noindex:


   
   Returns a dict containing all the sizer properties as keys along with
   their associated values.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19758:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getPositionInSizer(self)
   :noindex:


   
   Returns the current position of this sizer in its containing sizer, or None
   if there isn't a containing sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19759:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-19761:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.hideItem(self, itm)
   :noindex:


   Hides the passed item


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19762:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19763:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19765:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.insertSpacer(self, pos, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer at the specified position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19766:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.isContainedBy(self, obj)
   :noindex:


   
   Returns True if this the containership hierarchy for this control
   includes obj.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19767:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.layout(self)
   :noindex:


   
   Layout the items in the sizer.
   
   This is handled automatically when the sizer is resized, but you'll have
   to call it manually after you are done adding items to the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19768:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.listMembers(self, recurse=False, lvl=0)
   :noindex:


   
   Debugging method. This will list all the members of this sizer,
   and if recurse is True, drill down into all contained sizers.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19771:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.prepend(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
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

.. _no-19772:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.prependSpacer(self, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer in the first position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19773:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-19774:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.release(self, releaseContents=False)
   :noindex:


   
   Normally just destroys the sizer, leaving any objects
   controlled by the sizer intact. But if the 'releaseContents'
   parameter is passed as True, all objects contained in the
   sizer are destroyed first.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19775:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.remove(self, itm, destroy=None)
   :noindex:


   
   This will remove the item from the sizer. It will not cause
   the item to be destroyed unless the 'destroy' parameter is True.
   If the item is not one of this sizer's items, no error will be
   raised - it will simply do nothing.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19783:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setItemProp(self, itm, prop, val)
   :noindex:


   
   Given a sizer item, a property and a value, sets things as you
   would expect.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19784:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setItemProps(self, itm, props)
   :noindex:


   
   This accepts a dict of properties and values, and
   applies them to the specified sizer item.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19785:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setPositionInSizer(self, obj, pos)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19786:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-19787:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-19790:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.showItem(self, itm)
   :noindex:


   Makes sure that the passed item is visible


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19791:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19792:

.. function:: dabo.ui.uiwx.dGridSizer.dGridSizer.unbindEvent(self, eventClass=None, function=None)
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
