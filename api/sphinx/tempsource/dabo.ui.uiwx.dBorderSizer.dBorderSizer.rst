
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBorderSizer

.. _dabo.ui.uiwx.dBorderSizer.dBorderSizer:

==================================================
|doc_title|  **dBorderSizer.dBorderSizer** - class
==================================================


A BorderSizer is a regular box sizer, but with a visible box around
the perimiter. You must either create the box first and pass it to the
dBorderSizer's constructor, or pass a parent object, and the box
will be created for you in the constructor as a child object of the parent
you passed.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBorderSizer**

.. inheritance-diagram:: dBorderSizer


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`



|subclasses| Known Subclasses
=============================




|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dBorderSizer.png
          :scale: 75 %
          :target: _static/macWidgets/dBorderSizer.png
          :alt: dBorderSizer



     - .. image:: _static/winWidgets/dBorderSizer.png
          :scale: 75 %
          :target: _static/winWidgets/dBorderSizer.png
          :alt: dBorderSizer



     - .. image:: _static/nixWidgets/dBorderSizer.png
          :scale: 75 %
          :target: _static/nixWidgets/dBorderSizer.png
          :alt: dBorderSizer


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBorderSizer.dBorderSizer

   .. automethod:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.__init__

|method_summary| Properties Summary
===================================


====================================== ========================
:ref:`Application <no-19604>`          Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-19605>`            Color of the box background  (str or tuple)
:ref:`BaseClass <no-19606>`            The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-19607>`          Base key used when saving/restoring preferences  (str)
:ref:`Box <no-19608>`                  Reference to the box used in the sizer  (dBox)
:ref:`Caption <no-19609>`              Caption for the box  (str)
:ref:`ChildObjects <no-19610>`         List of all the objects (controls, sizers, spacers) that are directly managed
:ref:`ChildSizers <no-19611>`          List of all the sizers that are directly managed by this sizer  (list of sizers
:ref:`ChildSpacers <no-19612>`         List of all the spacer items that are directly managed by this sizer  (list of spacer items
:ref:`ChildWindows <no-19613>`         List of all the windows that are directly managed by this sizer  (list of controls
:ref:`Children <no-19614>`             List of all the sizer items managed by this sizer  (list of sizerItems
:ref:`Class <no-19615>`                The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-19616>`     Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-19617>` Reference to the sizer item that control's this control's layout.
:ref:`DefaultBorder <no-19618>`        Sets a default value for the border that will be applied to any controls added
:ref:`DefaultBorderAll <no-19619>`     When True, the DefaultBorder property is applied to all of the sides of
:ref:`DefaultBorderBottom <no-19620>`  Affects whether the DefaultBorder property is applied to the Bottom
:ref:`DefaultBorderLeft <no-19621>`    Affects whether the DefaultBorder property is applied to the Left
:ref:`DefaultBorderRight <no-19622>`   Affects whether the DefaultBorder property is applied to the Right
:ref:`DefaultBorderTop <no-19623>`     Affects whether the DefaultBorder property is applied to the Top
:ref:`DefaultSpacing <no-19624>`       Amount of space automatically inserted between elements.  (int)
:ref:`DynamicBackColor <no-19625>`     Dynamically determine the value of the BackColor property.
:ref:`DynamicCaption <no-19626>`       Dynamically determine the value of the Caption property.
:ref:`DynamicDefaultBorder <no-19627>` Dynamically determine the value of the DefaultBorder property.
:ref:`DynamicFontBold <no-19628>`      Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-19629>`      Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-19630>`    Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-19631>`      Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-19632>` Dynamically determine the value of the FontUnderline property.
:ref:`DynamicVisible <no-19633>`       Dynamically determine the value of the Visible property.
:ref:`FontBold <no-19634>`             Controls the bold setting of the box caption  (bool)
:ref:`FontFace <no-19635>`             Controls the type face of the box caption  (str)
:ref:`FontItalic <no-19636>`           Controls the italic setting of the box caption  (bool)
:ref:`FontSize <no-19637>`             Size of the box caption font  (int)
:ref:`FontUnderline <no-19638>`        Controls the underline setting of the box caption  (bool)
:ref:`Form <no-19639>`                 Form with which the sizer is associated.  (dForm or None)
:ref:`Height <no-19640>`               Height of the sizer  (int)
:ref:`LogEvents <no-19641>`            Specifies which events to log.  (list of strings)
:ref:`Name <no-19642>`                 The name of the object.  (str)
:ref:`Orientation <no-19643>`          Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.
:ref:`Parent <no-19644>`               The object that contains this sizer. In the case of nested
:ref:`PreferenceManager <no-19645>`    Reference to the Preference Management object  (dPref)
:ref:`Visible <no-19646>`              Specifies whether the sizer and contained items are shown  (bool)
:ref:`Width <no-19647>`                Width of this sizer  (int)

====================================== ========================


Properties
==========

.. _no-19605:

**BackColor** 

Color of the box background  (str or tuple)



-------

.. _no-19608:

**Box** 

Reference to the box used in the sizer  (dBox)



-------

.. _no-19609:

**Caption** 

Caption for the box  (str)



-------

.. _no-19625:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.



-------

.. _no-19626:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.



-------

.. _no-19628:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.



-------

.. _no-19629:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.



-------

.. _no-19630:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.



-------

.. _no-19631:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.



-------

.. _no-19632:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.



-------

.. _no-19634:

**FontBold** 

Controls the bold setting of the box caption  (bool)



-------

.. _no-19635:

**FontFace** 

Controls the type face of the box caption  (str)



-------

.. _no-19636:

**FontItalic** 

Controls the italic setting of the box caption  (bool)



-------

.. _no-19637:

**FontSize** 

Size of the box caption font  (int)



-------

.. _no-19638:

**FontUnderline** 

Controls the underline setting of the box caption  (bool)



-------


Properties - inherited
========================

.. _no-19604:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19606:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19607:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19610:

**ChildObjects** 

List of all the objects (controls, sizers, spacers) that are directly managed
    by this sizer  (list of objects


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19611:

**ChildSizers** 

List of all the sizers that are directly managed by this sizer  (list of sizers


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19612:

**ChildSpacers** 

List of all the spacer items that are directly managed by this sizer  (list of spacer items


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19613:

**ChildWindows** 

List of all the windows that are directly managed by this sizer  (list of controls


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19614:

**Children** 

List of all the sizer items managed by this sizer  (list of sizerItems


Inherited from: 'wx._core.Sizer - can not provide a link

-------

.. _no-19615:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19616:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19617:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.
        This is useful for getting information about how the item is being
        sized, and for changing those settings.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19618:

**DefaultBorder** 

Sets a default value for the border that will be applied to any controls added
    to the sizer afterwards for whom an explicit value for the border is not set.
    Note that it does not affect the border of items already added to the control.
    This property is useful when you want to add a series of items to a sizer with
    the same border: just set this property once, and then add your items.
    Default=0  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19619:

**DefaultBorderAll** 

When True, the DefaultBorder property is applied to all of the sides of
    any controls added to the sizer. If any of the individual side properties,
    such as DefaultBorderTop, are set to False, this property will return False.
    Setting DefaultBorderAll will effectively set all of the individual side properties
    to that value. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19620:

**DefaultBorderBottom** 

Affects whether the DefaultBorder property is applied to the Bottom
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19621:

**DefaultBorderLeft** 

Affects whether the DefaultBorder property is applied to the Left
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19622:

**DefaultBorderRight** 

Affects whether the DefaultBorder property is applied to the Right
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19623:

**DefaultBorderTop** 

Affects whether the DefaultBorder property is applied to the Top
    side of controls added to the sizer. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19624:

**DefaultSpacing** 

Amount of space automatically inserted between elements.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19627:

**DynamicDefaultBorder** 

Dynamically determine the value of the DefaultBorder property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultBorder property. If DynamicDefaultBorder is set to None (the default), DefaultBorder
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19633:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19639:

**Form** 

Form with which the sizer is associated.  (dForm or None)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19640:

**Height** 

Height of the sizer  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19641:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19642:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19643:

**Orientation** 

Sets the orientation of the sizer, either 'Vertical' or 'Horizontal'.


Inherited from: 'wx._core.BoxSizer - can not provide a link

-------

.. _no-19644:

**Parent** 

The object that contains this sizer. In the case of nested
    sizers, it is the object that the outermost sizer belongs to. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19645:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19646:

**Visible** 

Specifies whether the sizer and contained items are shown  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19647:

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
:ref:`addDefaultSpacer <no-19648>`      
:ref:`addSpacer <no-19649>`             
:ref:`afterInit <no-19650>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`append <no-19651>`                Adds the passed object to the end of the sizer layout.
:ref:`append1x <no-19652>`              Shorthand for sizer.append(obj, 1, "expand").
:ref:`appendItems <no-19653>`           Append each item to the sizer.
:ref:`appendSpacer <no-19654>`          Appends a spacer to the sizer.
:ref:`autoBindEvents <no-19655>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-19656>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-19657>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-19658>`            Bind a sequence of [dEvent, callback] lists.
:ref:`clear <no-19659>`                 This method is called to remove all items from the sizer. If the
:ref:`drawOutline <no-19660>`           There are some cases where being able to see the sizer
:ref:`getAbsoluteName <no-19661>`       Return the fully qualified name of the object.
:ref:`getContainingWindow <no-19662>`   
:ref:`getItem <no-19663>`               Querying sizers for their contents returns sizer items, not
:ref:`getItemProp <no-19664>`           Get the current value of the specified property for the sizer item.
:ref:`getItemProps <no-19665>`          Returns a dict containing all the sizer properties as keys along with
:ref:`getNonBorderedClass <no-19666>`   Return the class that is the non-border sizer version of this class.
:ref:`getPositionInSizer <no-19667>`    Returns the current position of this sizer in its containing sizer, or None
:ref:`getProperties <no-19668>`         Returns a dictionary of property name/value pairs.
:ref:`hideItem <no-19669>`              Hides the passed item
:ref:`initEvents <no-19670>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-19671>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-19672>`                Inserts the passed object into the sizer layout at the specified position.
:ref:`insertSpacer <no-19673>`          Added to be consistent with the sizers' add/insert
:ref:`isContainedBy <no-19674>`         Returns True if this the containership hierarchy for this control
:ref:`layout <no-19675>`                Layout the items in the sizer.
:ref:`listMembers <no-19676>`           Debugging method. This will list all the members of this sizer,
:ref:`prepend <no-19677>`               Insert the object at the beginning of the sizer layout.
:ref:`prependSpacer <no-19678>`         Added to be consistent with the sizers' add/insert
:ref:`raiseEvent <no-19679>`            Send the event to all registered listeners.
:ref:`release <no-19680>`               Normally just destroys the sizer, leaving any objects
:ref:`remove <no-19681>`                This will remove the item from the sizer. It will not cause
:ref:`setItemProp <no-19682>`           Given a sizer item, a property and a value, sets things as you
:ref:`setItemProps <no-19683>`          This accepts a dict of properties and values, and
:ref:`setPositionInSizer <no-19684>`    
:ref:`setProperties <no-19685>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-19686>` Sets a group of properties on the object all at once. This
:ref:`showItem <no-19687>`              Makes sure that the passed item is visible
:ref:`super <no-19688>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-19689>`           Remove a previously registered event binding.

======================================= ========================


Methods
=======

.. _no-19666:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getNonBorderedClass(self)

   Return the class that is the non-border sizer version of this class.



-------


Methods - inherited
=====================

.. _no-19648:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.addDefaultSpacer(self, pos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19649:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.addSpacer(self, val, pos=None, proportion=0)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19650:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19651:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.append(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
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

.. _no-19652:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.append1x(self, obj, \**kwargs)
   :noindex:


   Shorthand for sizer.append(obj, 1, "expand").


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19653:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.appendItems(self, items, \*args, \**kwargs)
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

.. _no-19654:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.appendSpacer(self, val, proportion=0)
   :noindex:


   Appends a spacer to the sizer.


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19655:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.autoBindEvents(self, force=True)
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

.. _no-19656:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19657:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19658:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19659:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.clear(self, destroy=False)
   :noindex:


   
   This method is called to remove all items from the sizer. If the
   optional 'destroy' parameter is set to True, any contained items
   will be destroyed. Otherwise, they will remain as is, but no longer
   under control of the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19660:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.drawOutline(self, win, recurse=False, drawChildren=False)
   :noindex:


   
   There are some cases where being able to see the sizer
   is helpful, such as at design time. This method can be called
   to see the outline; it needs to be called whenever the containing
   window is resized or repainted.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19661:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19662:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getContainingWindow(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19663:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getItem(self, szItem)
   :noindex:


   
   Querying sizers for their contents returns sizer items, not
   the actual items. So given a sizer item, this method will return
   the actual item in the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19664:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getItemProp(self, itm, prop)
   :noindex:


   
   Get the current value of the specified property for the sizer item.
   Grid sizers must override with their specific props.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19665:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getItemProps(self, itm)
   :noindex:


   
   Returns a dict containing all the sizer properties as keys along with
   their associated values.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19667:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getPositionInSizer(self)
   :noindex:


   
   Returns the current position of this sizer in its containing sizer, or None
   if there isn't a containing sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19668:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-19669:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.hideItem(self, itm)
   :noindex:


   Hides the passed item


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19670:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19671:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19672:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.insert(self, index, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
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

.. _no-19673:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.insertSpacer(self, pos, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer at the specified position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19674:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.isContainedBy(self, obj)
   :noindex:


   
   Returns True if this the containership hierarchy for this control
   includes obj.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19675:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.layout(self)
   :noindex:


   
   Layout the items in the sizer.
   
   This is handled automatically when the sizer is resized, but you'll have
   to call it manually after you are done adding items to the sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19676:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.listMembers(self, recurse=False, lvl=0)
   :noindex:


   
   Debugging method. This will list all the members of this sizer,
   and if recurse is True, drill down into all contained sizers.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19677:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.prepend(self, obj, layout='normal', proportion=0, alignment=None, halign='left', valign='top', border=None, borderSides=None)
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

.. _no-19678:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.prependSpacer(self, val, proportion=0)
   :noindex:


   
   Added to be consistent with the sizers' add/insert
   design. Inserts a spacer in the first position.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19679:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-19680:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.release(self, releaseContents=False)
   :noindex:


   
   Normally just destroys the sizer, leaving any objects
   controlled by the sizer intact. But if the 'releaseContents'
   parameter is passed as True, all objects contained in the
   sizer are destroyed first.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19681:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.remove(self, itm, destroy=None)
   :noindex:


   
   This will remove the item from the sizer. It will not cause
   the item to be destroyed unless the 'destroy' parameter is True.
   If the item is not one of this sizer's items, no error will be
   raised - it will simply do nothing.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19682:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.setItemProp(self, itm, prop, val)
   :noindex:


   
   Given a sizer item, a property and a value, sets things as you
   would expect.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19683:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.setItemProps(self, itm, props)
   :noindex:


   
   This accepts a dict of properties and values, and
   applies them to the specified sizer item.
   


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19684:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.setPositionInSizer(self, obj, pos)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19685:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-19686:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-19687:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.showItem(self, itm)
   :noindex:


   Makes sure that the passed item is visible


Inherited from: :ref:`dabo.ui.uiwx.dSizerMixin.dSizerMixin`

-------

.. _no-19688:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19689:

.. function:: dabo.ui.uiwx.dBorderSizer.dBorderSizer.unbindEvent(self, eventClass=None, function=None)
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
