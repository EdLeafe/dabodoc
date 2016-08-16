
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDropdownList

.. _dabo.ui.uiwx.dDropdownList.dDropdownList:

====================================================
|doc_title|  **dDropdownList.dDropdownList** - class
====================================================


Creates a dropdown list, which allows the user to select one item.

This is a very simple control, suitable for choosing from one of a handful
of items. Only one column can be displayed. A more powerful, flexible
control for all kinds of lists is dListControl, but dDropdownList does
suffice for simple needs.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDropdownList**

.. inheritance-diagram:: dDropdownList


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Page.SelectionOpDropdown`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - no image available



     - .. image:: _static/nixWidgets/dDropdownList.png
          :scale: 75 %
          :target: _static/nixWidgets/dDropdownList.png
          :alt: dDropdownList


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDropdownList.dDropdownList

   .. automethod:: dabo.ui.uiwx.dDropdownList.dDropdownList.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-26599>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-26600>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-26601>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-26602>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-26603>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-26604>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-26605>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-26606>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-26607>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-26608>`                  The caption of the object. (str)
:ref:`Children <no-26609>`                 Returns a list of object references to the children of
:ref:`Choices <no-26610>`                  Specifies the string choices to display in the list.
:ref:`Class <no-26611>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-26612>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-26613>`     Reference to the sizer item that control's this control's layout.
:ref:`Count <no-26614>`                    Number of items in the control.
:ref:`DataField <no-26615>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-26616>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-26617>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-26618>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-26619>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-26620>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-26621>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-26622>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-26623>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-26624>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-26625>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-26626>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-26627>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-26628>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-26629>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-26630>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-26631>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-26632>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-26633>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-26634>`            Dynamically determine the value of the Height property.
:ref:`DynamicKeyValue <no-26635>`          Dynamically determine the value of the KeyValue property.
:ref:`DynamicLeft <no-26636>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-26637>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-26638>`          Dynamically determine the value of the Position property.
:ref:`DynamicPositionValue <no-26639>`     Dynamically determine the value of the PositionValue property.
:ref:`DynamicSize <no-26640>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-26641>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStringValue <no-26642>`       Dynamically determine the value of the StringValue property.
:ref:`DynamicTag <no-26643>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-26644>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-26645>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-26646>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-26647>`             Dynamically determine the value of the Value property.
:ref:`DynamicValueMode <no-26648>`         Dynamically determine the value of the ValueMode property.
:ref:`DynamicVisible <no-26649>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-26650>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-26651>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-26652>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-26653>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-26654>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-26655>`                 Specifies the font face. (str)
:ref:`FontInfo <no-26656>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-26657>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-26658>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-26659>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-26660>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-26661>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-26662>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-26663>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-26664>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-26665>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`KeyValue <no-26666>`                 Specifies the key value or values of the selected item or items.
:ref:`Keys <no-26667>`                     Specifies a mapping between arbitrary values and item positions.
:ref:`Left <no-26668>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-26669>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-26670>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-26671>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-26672>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-26673>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-26674>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-26675>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-26676>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-26677>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-26678>`                 Specifies the base name of the object.
:ref:`Parent <no-26679>`                   The containing object. (obj)
:ref:`PersistSecretData <no-26680>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-26681>`                 The (x,y) position of the object. (tuple)
:ref:`PositionValue <no-26682>`            Specifies the position (index) of the selected item(s).
:ref:`PreferenceManager <no-26683>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-26684>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-26685>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-26686>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-26687>`                     The size of the object. (tuple)
:ref:`Sizer <no-26688>`                    The sizer for the object.
:ref:`SortFunction <no-26689>`             Function used to sort list items when Sorted=True. Default=None,
:ref:`Sorted <no-26690>`                   Are the items in the control automatically sorted? Default=False.
:ref:`Source <no-26691>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-26692>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StringValue <no-26693>`              Specifies the text of the selected item.
:ref:`TabStop <no-26694>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-26695>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-26696>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-26697>`                      The top position of the object. (int)
:ref:`Transparency <no-26698>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-26699>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-26700>`                    Specifies which item is currently selected in the list.
:ref:`ValueMode <no-26701>`                Specifies the information that the Value property refers to.
:ref:`Visible <no-26702>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-26703>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-26704>`                    The width of the object. (int)
:ref:`WindowHandle <no-26705>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties - inherited
========================

.. _no-26599:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26600:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26601:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26602:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26603:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26604:

**BorderLineStyle** 

Style of line for the border drawn around the control.

    Possible choices are:
        "Solid"  (default)
        "Dash"
        "Dot"
        "DotDash"
        "DashDot"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26605:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26606:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26607:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26608:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26609:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26610:

**Choices** 

Specifies the string choices to display in the list.
    -> List of strings. Read-write at runtime.
    The list index becomes the PositionValue, and the string
    becomes the StringValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26611:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26612:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26613:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26614:

**Count** 

Number of items in the control.
    -> Integer. Read-only.


Inherited from: 'wx._core.ItemContainer - can not provide a link

-------

.. _no-26615:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26616:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26617:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26618:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26619:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26620:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26621:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26622:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26623:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26624:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26625:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26626:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26627:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26628:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26629:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26630:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26631:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26632:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26633:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26634:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26635:

**DynamicKeyValue** 

Dynamically determine the value of the KeyValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
KeyValue property. If DynamicKeyValue is set to None (the default), KeyValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26636:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26637:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26638:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26639:

**DynamicPositionValue** 

Dynamically determine the value of the PositionValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PositionValue property. If DynamicPositionValue is set to None (the default), PositionValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26640:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26641:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26642:

**DynamicStringValue** 

Dynamically determine the value of the StringValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StringValue property. If DynamicStringValue is set to None (the default), StringValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26643:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26644:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26645:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26646:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26647:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-26648:

**DynamicValueMode** 

Dynamically determine the value of the ValueMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueMode property. If DynamicValueMode is set to None (the default), ValueMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26649:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26650:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26651:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26652:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26653:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26654:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26655:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26656:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26657:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26658:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26659:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26660:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26661:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26662:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26663:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26664:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26665:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26666:

**KeyValue** 

Specifies the key value or values of the selected item or items.
    -> Type can vary. Read-write at runtime.
    Returns the key value or values of the selected item(s), or selects
    the item(s) with the specified KeyValue(s).    An exception will be
    raised if the Keys property hasn't been set up to accomodate.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26667:

**Keys** 

Specifies a mapping between arbitrary values and item positions.
    -> Dictionary. Read-write at runtime.
    The Keys property is a dictionary, where each key resolves into a
    list index (position). If using keys, you should update the Keys
    property whenever you update the Choices property, to make sure they
    are in sync.
    -> Optionally, Keys can be a list/tuple that is a 1:1 mapping of the
    Choices property. So if your 3rd Choices entry is selected, KeyValue
    will return the 3rd entry in the Keys property.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26668:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26669:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26670:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26671:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26672:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26673:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26674:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26675:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26676:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26677:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26678:

**NameBase** 

Specifies the base name of the object.

    The base name specified will become the object's Name, unless another sibling
    already has that name, in which case Dabo will find the next unique name by
    adding integers to the end of the base name. For example, if your code says:

        self.NameBase = "txtAddress"

    and there is already a sibling object with that name, your object will end up
    with Name = "txtAddress1".

    This property is write-only at runtime.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26679:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26680:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26681:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26682:

**PositionValue** 

Specifies the position (index) of the selected item(s).
    -> Integer or tuple of integers. Read-write at runtime.
    Returns the current position(s), or sets the current position(s).


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26683:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26684:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26685:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26686:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26687:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26688:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26689:

**SortFunction** 

Function used to sort list items when Sorted=True. Default=None,
    which gives the default sorting  (callable or None)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26690:

**Sorted** 

Are the items in the control automatically sorted? Default=False.
    If True, whenever the Choices property is changed, the resulting list
    will be first sorted using the SortFunction property, which defaults to
    None, giving a default sort order.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26691:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26692:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26693:

**StringValue** 

Specifies the text of the selected item.
    -> String or tuple of strings. Read-write at runtime.
    Returns the text of the selected item(s), or selects the item(s)
    with the specified text. An exception is raised if there is no
    position with matching text.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26694:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-26695:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26696:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26697:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26698:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26699:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26700:

**Value** 

Specifies which item is currently selected in the list.
    -> Type can vary. Read-write at runtime.
    Value refers to one of the following, depending on the setting of ValueMode:

        + ValueMode="Position" : the index of the selected item(s) (integer)
        + ValueMode="String"   : the displayed string of the selected item(s) (string)
        + ValueMode="Key"      : the key of the selected item(s) (can vary)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26701:

**ValueMode** 

Specifies the information that the Value property refers to.
    -> String. Read-write at runtime.

    ============= =========================
    'Position'    Value refers to the position in the choices (integer).
    'String'      Value refers to the displayed string for the selection (default) (string).
    'Key'         Value refers to a separate key, set using the Keys property (can vary).
    ============= =========================

    


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26702:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26703:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26704:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26705:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-26706>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-26707>`                 Occurs after the control or form is created.
:ref:`Destroy <no-26708>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-26709>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-26710>`               Occurs when the control gets the focus.
:ref:`Hit <no-26711>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-26712>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-26713>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-26714>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-26715>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-26716>`               
:ref:`KeyUp <no-26717>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-26718>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-26719>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-26720>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-26721>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-26722>`             
:ref:`MouseLeave <no-26723>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-26724>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-26725>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-26726>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-26727>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-26728>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-26729>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-26730>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-26731>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-26732>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-26733>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-26734>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-26735>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-26736>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-26737>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-26738>`                   Occurs when the control's position changes.
:ref:`Paint <no-26739>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-26740>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-26741>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-26742>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-26743>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-26744>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-26706:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-26707:

**Create** 

Occurs after the control or form is created.



-------

.. _no-26708:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-26709:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-26710:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-26711:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-26712:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-26713:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-26714:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-26715:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-26716:

**KeyEvent** 



-------

.. _no-26717:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-26718:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-26719:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-26720:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-26721:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-26722:

**MouseEvent** 



-------

.. _no-26723:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-26724:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-26725:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-26726:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-26727:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-26728:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-26729:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-26730:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-26731:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-26732:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-26733:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-26734:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-26735:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-26736:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-26737:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-26738:

**Move** 

Occurs when the control's position changes.



-------

.. _no-26739:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-26740:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-26741:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-26742:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-26743:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-26744:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-26745>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-26746>`             Instantiate object as a child of self.
:ref:`afterInit <no-26747>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-26748>`          
:ref:`afterSetProperties <no-26749>`    
:ref:`appendItem <no-26750>`            Adds a new item to the end of the list
:ref:`autoBindEvents <no-26751>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-26752>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-26753>`   
:ref:`bindEvent <no-26754>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-26755>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-26756>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-26757>`          Makes this object topmost
:ref:`clear <no-26758>`                 Clears the background of custom-drawn objects.
:ref:`clearSelections <no-26759>`       Stub method. Only used in the list box, where there
:ref:`clone <no-26760>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-26761>`  Given a position relative to this control, return a position relative
:ref:`copy <no-26762>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-26763>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-26764>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-26765>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-26766>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-26767>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-26768>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-26769>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-26770>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-26771>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-26772>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-26773>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-26774>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-26775>`              Draws text on the object at the specified position
:ref:`endHover <no-26776>`              
:ref:`fitToSizer <no-26777>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-26778>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-26779>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-26780>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-26781>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-26782>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-26783>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-26784>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-26785>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-26786>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-26787>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-26788>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-26789>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-26790>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-26791>`      
:ref:`getSizerProp <no-26792>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-26793>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-26794>`                  Make the object invisible.
:ref:`initEvents <no-26795>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-26796>`        Hook for subclasses. User subclasses should set properties
:ref:`insertItem <no-26797>`            Inserts a new item into the specified position.
:ref:`isContainedBy <no-26798>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-26799>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-26800>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-26801>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-26802>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-26803>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-26804>`               
:ref:`paste <no-26805>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-26806>`           
:ref:`processDroppedFiles <no-26807>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-26808>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-26809>`            Raise the passed Dabo event.
:ref:`reCreate <no-26810>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-26811>`              Recreate the object.
:ref:`redraw <no-26812>`                Called when the object is (re)drawn.
:ref:`refresh <no-26813>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-26814>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-26815>`               Destroys the object.
:ref:`removeAll <no-26816>`             Removes all entries from the control.
:ref:`removeDrawnObject <no-26817>`     
:ref:`removeItem <no-26818>`            Removes the item at the specified position.
:ref:`restoreValue <no-26819>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-26820>`             Save control's value to dApp's user settings table.
:ref:`select <no-26821>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-26822>`             Select all text in the control.
:ref:`selectNone <no-26823>`            Select no text in the control.
:ref:`sendToBack <no-26824>`            Places this object behind all others.
:ref:`setAll <no-26825>`                Set all child object properties to the passed value.
:ref:`setFocus <no-26826>`              Sets focus to the object.
:ref:`setPositionInSizer <no-26827>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-26828>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-26829>` Sets a group of properties on the object all at once. This
:ref:`setSelection <no-26830>`          Same as setting property PositionValue.
:ref:`setSizerProp <no-26831>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-26832>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-26833>`                  Make the object visible.
:ref:`showContainingPage <no-26834>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-26835>`       Display a context menu (popup) at the specified position.
:ref:`sort <no-26836>`                  Sorts the list items. By default, the Python 'cmp' function is
:ref:`super <no-26837>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-26838>`           Remove a previously registered event binding.
:ref:`unbindKey <no-26839>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-26840>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-26841>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-26842>`                Update control's value to match the current value from the source.

======================================= ========================


Methods - inherited
=====================

.. _no-26745:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26746:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.addObject(self, classRef, Name=None, \*args, \**kwargs)
   :noindex:


   
   Instantiate object as a child of self.
   
   The classRef argument must be a Dabo UI class definition. (it must inherit
   dPemMixin). Alternatively, it can be a saved class definition in XML format,
   as created by the Class Designer.
   
   The name argument, if passed, will be sent along to the object's
   constructor, which will attempt to set its Name accordingly. If the name
   argument is not passed (or None), the object will get a default Name as
   defined in the object's class definition.
   
   Additional positional and/or keyword arguments will be sent along to the
   object's constructor.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26747:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26748:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26749:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26750:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.appendItem(self, txt, select=False)
   :noindex:


   Adds a new item to the end of the list


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26751:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.autoBindEvents(self, force=True)
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

.. _no-26752:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26753:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26754:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26755:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26756:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.bindKey(self, keyCombo, callback, \**kwargs)
   :noindex:


   
   Bind a key combination such as "ctrl+c" to a callback function.
   
   See dKeys.keyStrings for the valid string key codes.
   See dKeys.modifierStrings for the valid modifier codes.
   
   Examples::
   
       # When user presses <esc>, close the form:
       form.bindKey("esc", form.Close)
   
       # When user presses <ctrl><alt><w>, close the form:
       form.bindKey("ctrl+alt+w", form.Close)
   
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26757:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26758:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26759:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.clearSelections(self)
   :noindex:


   
   Stub method. Only used in the list box, where there
   can be multiple selections.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26760:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26761:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26762:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26763:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26764:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26765:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26766:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a circle of the specified radius around the specified point.
   
   You can set the color and thickness of the line, as well as the
   color and hatching style of the fill. Normally, when persist=True,
   the circle will be re-drawn on paint events, but if you pass False,
   it will be drawn once only.
   
   A drawing object is returned, or None if persist=False. You can
   'remove' the drawing by setting the Visible property of the
   returned object to False. You can also manipulate the position, size,
   color, and fill by changing the various properties of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26767:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26768:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26769:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26770:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26771:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26772:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26773:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26774:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26775:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26776:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26777:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26778:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26779:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26780:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26781:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26782:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26783:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26784:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26785:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26786:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26787:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26788:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26789:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26790:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-26791:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26792:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26793:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26794:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26795:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26796:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26797:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.insertItem(self, pos, txt, select=False)
   :noindex:


   Inserts a new item into the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26798:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26799:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26800:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.lockDisplay(self)
   :noindex:


   
   Locks the visual updates to the control.
   
   This can significantly improve performance when many items are being
   updated at once.
   
   IMPORTANT: you must call unlockDisplay() when you are done, or your
   object will never draw. unlockDisplay() must be called once for every
   time lockDisplay() is called in order to resume repainting of the
   control. Alternatively, you can call lockDisplay() many times, and
   then call unlockDisplayAll() once when you are done.
   
   Note that lockDisplay currently doesn't do anything on GTK.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26801:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26802:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26803:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26804:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26805:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26806:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26807:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26808:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26809:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26810:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26811:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26812:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26813:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26814:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26815:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26816:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.removeAll(self)
   :noindex:


   Removes all entries from the control.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26817:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26818:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.removeItem(self, pos)
   :noindex:


   Removes the item at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26819:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26820:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-26821:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-26822:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-26823:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-26824:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26825:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
   :noindex:


   
   Set all child object properties to the passed value.
   
   No bad effects will happen if the property doesn't apply to a child - only
   children with the property will have their property updated.
   
   If 'recurse' is True, setAll() will be called on each child as well.
   
   If 'filt' is not empty, only children that match the expression in 'filt'
   will be affected. The expression will be evaluated assuming the child
   object is prefixed to the expression. For example, if you want to only
   affect objects that are instances of dButton, you'd call::
   
       form.setAll("FontBold", True, filt="BaseClass == dabo.ui.dButton")
   
   If the instancesOf sequence is passed, the property will only be set if
   the child object is an instance of one of the passed classes.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26826:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26827:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26828:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-26829:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-26830:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setSelection(self, index)
   :noindex:


   Same as setting property PositionValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26831:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26832:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26833:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26834:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26835:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26836:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.sort(self, sortFunction=None)
   :noindex:


   
   Sorts the list items. By default, the Python 'cmp' function is
   used, but this can be overridden with a custom sortFunction.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-26837:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26838:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26839:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26840:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26841:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26842:

.. function:: dabo.ui.uiwx.dDropdownList.dDropdownList.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
