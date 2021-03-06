
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.SelectionOpDropdown:

=================================================
|doc_title|  **Page.SelectionOpDropdown** - class
=================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SelectionOpDropdown**

.. inheritance-diagram:: SelectionOpDropdown


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDropdownList.dDropdownList`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.SelectionOpDropdown


|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-4870>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-4871>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-4872>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-4873>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-4874>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-4875>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-4876>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-4877>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-4878>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-4879>`                  The caption of the object. (str)
:ref:`Children <no-4880>`                 Returns a list of object references to the children of
:ref:`Choices <no-4881>`                  Specifies the string choices to display in the list.
:ref:`Class <no-4882>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-4883>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-4884>`     Reference to the sizer item that control's this control's layout.
:ref:`Count <no-4885>`                    Number of items in the control.
:ref:`DataField <no-4886>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-4887>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-4888>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-4889>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-4890>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-4891>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-4892>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-4893>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-4894>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-4895>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-4896>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-4897>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-4898>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-4899>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-4900>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-4901>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-4902>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-4903>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-4904>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-4905>`            Dynamically determine the value of the Height property.
:ref:`DynamicKeyValue <no-4906>`          Dynamically determine the value of the KeyValue property.
:ref:`DynamicLeft <no-4907>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-4908>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-4909>`          Dynamically determine the value of the Position property.
:ref:`DynamicPositionValue <no-4910>`     Dynamically determine the value of the PositionValue property.
:ref:`DynamicSize <no-4911>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-4912>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStringValue <no-4913>`       Dynamically determine the value of the StringValue property.
:ref:`DynamicTag <no-4914>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-4915>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-4916>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-4917>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-4918>`             Dynamically determine the value of the Value property.
:ref:`DynamicValueMode <no-4919>`         Dynamically determine the value of the ValueMode property.
:ref:`DynamicVisible <no-4920>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-4921>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-4922>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-4923>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-4924>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-4925>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-4926>`                 Specifies the font face. (str)
:ref:`FontInfo <no-4927>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-4928>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-4929>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-4930>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-4931>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-4932>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-4933>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-4934>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-4935>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-4936>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`KeyValue <no-4937>`                 Specifies the key value or values of the selected item or items.
:ref:`Keys <no-4938>`                     Specifies a mapping between arbitrary values and item positions.
:ref:`Left <no-4939>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-4940>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-4941>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-4942>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-4943>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-4944>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-4945>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-4946>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-4947>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-4948>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-4949>`                 Specifies the base name of the object.
:ref:`Parent <no-4950>`                   The containing object. (obj)
:ref:`PersistSecretData <no-4951>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-4952>`                 The (x,y) position of the object. (tuple)
:ref:`PositionValue <no-4953>`            Specifies the position (index) of the selected item(s).
:ref:`PreferenceManager <no-4954>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-4955>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-4956>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-4957>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-4958>`                     The size of the object. (tuple)
:ref:`Sizer <no-4959>`                    The sizer for the object.
:ref:`SortFunction <no-4960>`             Function used to sort list items when Sorted=True. Default=None,
:ref:`Sorted <no-4961>`                   Are the items in the control automatically sorted? Default=False.
:ref:`Source <no-4962>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-4963>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StringValue <no-4964>`              Specifies the text of the selected item.
:ref:`TabStop <no-4965>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-4966>`                      A property that user code can safely use for specific purposes.
:ref:`Target <no-4967>`                   Holds a reference to the edit control.
:ref:`ToolTipText <no-4968>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-4969>`                      The top position of the object. (int)
:ref:`Transparency <no-4970>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-4971>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-4972>`                    Specifies which item is currently selected in the list.
:ref:`ValueMode <no-4973>`                Specifies the information that the Value property refers to.
:ref:`Visible <no-4974>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-4975>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-4976>`                    The width of the object. (int)
:ref:`WindowHandle <no-4977>`             The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-4967:

**Target** 

Holds a reference to the edit control.



-------


Properties - inherited
========================

.. _no-4870:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4871:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4872:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4873:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4874:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4875:

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

.. _no-4876:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4877:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4878:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4879:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4880:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4881:

**Choices** 

Specifies the string choices to display in the list.
    -> List of strings. Read-write at runtime.
    The list index becomes the PositionValue, and the string
    becomes the StringValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4882:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4883:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4884:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4885:

**Count** 

Number of items in the control.
    -> Integer. Read-only.


Inherited from: 'wx._core.ItemContainer - can not provide a link

-------

.. _no-4886:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4887:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4888:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4889:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4890:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4891:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4892:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4893:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4894:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4895:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4896:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4897:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4898:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4899:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4900:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4901:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4902:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4903:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4904:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4905:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4906:

**DynamicKeyValue** 

Dynamically determine the value of the KeyValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
KeyValue property. If DynamicKeyValue is set to None (the default), KeyValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4907:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4908:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4909:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4910:

**DynamicPositionValue** 

Dynamically determine the value of the PositionValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PositionValue property. If DynamicPositionValue is set to None (the default), PositionValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4911:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4912:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4913:

**DynamicStringValue** 

Dynamically determine the value of the StringValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StringValue property. If DynamicStringValue is set to None (the default), StringValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4914:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4915:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4916:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4917:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4918:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-4919:

**DynamicValueMode** 

Dynamically determine the value of the ValueMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueMode property. If DynamicValueMode is set to None (the default), ValueMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4920:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4921:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4922:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4923:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4924:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4925:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4926:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4927:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4928:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4929:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4930:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4931:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4932:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4933:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4934:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4935:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4936:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4937:

**KeyValue** 

Specifies the key value or values of the selected item or items.
    -> Type can vary. Read-write at runtime.
    Returns the key value or values of the selected item(s), or selects
    the item(s) with the specified KeyValue(s).    An exception will be
    raised if the Keys property hasn't been set up to accomodate.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4938:

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

.. _no-4939:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4940:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4941:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4942:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4943:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4944:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4945:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4946:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4947:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4948:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4949:

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

.. _no-4950:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4951:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4952:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4953:

**PositionValue** 

Specifies the position (index) of the selected item(s).
    -> Integer or tuple of integers. Read-write at runtime.
    Returns the current position(s), or sets the current position(s).


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4954:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4955:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4956:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4957:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4958:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4959:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4960:

**SortFunction** 

Function used to sort list items when Sorted=True. Default=None,
    which gives the default sorting  (callable or None)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4961:

**Sorted** 

Are the items in the control automatically sorted? Default=False.
    If True, whenever the Choices property is changed, the resulting list
    will be first sorted using the SortFunction property, which defaults to
    None, giving a default sort order.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4962:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4963:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4964:

**StringValue** 

Specifies the text of the selected item.
    -> String or tuple of strings. Read-write at runtime.
    Returns the text of the selected item(s), or selects the item(s)
    with the specified text. An exception is raised if there is no
    position with matching text.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-4965:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-4966:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4968:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4969:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4970:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4971:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4972:

**Value** 

Specifies which item is currently selected in the list.
    -> Type can vary. Read-write at runtime.
    Value refers to one of the following, depending on the setting of ValueMode:

        + ValueMode="Position" : the index of the selected item(s) (integer)
        + ValueMode="String"   : the displayed string of the selected item(s) (string)
        + ValueMode="Key"      : the key of the selected item(s) (can vary)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4973:

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

.. _no-4974:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4975:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4976:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4977:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-4978>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-4979>`                 Occurs after the control or form is created.
:ref:`Destroy <no-4980>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-4981>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-4982>`               Occurs when the control gets the focus.
:ref:`Hit <no-4983>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-4984>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-4985>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-4986>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-4987>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-4988>`               
:ref:`KeyUp <no-4989>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-4990>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-4991>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-4992>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-4993>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-4994>`             
:ref:`MouseLeave <no-4995>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-4996>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-4997>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-4998>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-4999>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-5000>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-5001>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-5002>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-5003>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-5004>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-5005>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-5006>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-5007>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-5008>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-5009>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-5010>`                   Occurs when the control's position changes.
:ref:`Paint <no-5011>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-5012>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-5013>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-5014>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-5015>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-5016>`           Occurs when the control's value has changed, whether

======================================= ========================


Events
=======

.. _no-4978:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-4979:

**Create** 

Occurs after the control or form is created.



-------

.. _no-4980:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-4981:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-4982:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-4983:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-4984:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-4985:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-4986:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-4987:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-4988:

**KeyEvent** 



-------

.. _no-4989:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-4990:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-4991:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-4992:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-4993:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-4994:

**MouseEvent** 



-------

.. _no-4995:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-4996:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-4997:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-4998:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-4999:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-5000:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-5001:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-5002:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-5003:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-5004:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-5005:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-5006:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-5007:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-5008:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-5009:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-5010:

**Move** 

Occurs when the control's position changes.



-------

.. _no-5011:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-5012:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-5013:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-5014:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-5015:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-5016:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-5017>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-5018>`             Instantiate object as a child of self.
:ref:`afterInit <no-5019>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-5020>`          
:ref:`afterSetProperties <no-5021>`    
:ref:`appendItem <no-5022>`            Adds a new item to the end of the list
:ref:`autoBindEvents <no-5023>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-5024>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-5025>`   
:ref:`bindEvent <no-5026>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-5027>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-5028>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-5029>`          Makes this object topmost
:ref:`clear <no-5030>`                 Clears the background of custom-drawn objects.
:ref:`clearSelections <no-5031>`       Stub method. Only used in the list box, where there
:ref:`clone <no-5032>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-5033>`  Given a position relative to this control, return a position relative
:ref:`copy <no-5034>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-5035>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-5036>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-5037>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-5038>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-5039>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-5040>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-5041>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-5042>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-5043>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-5044>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-5045>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-5046>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-5047>`              Draws text on the object at the specified position
:ref:`endHover <no-5048>`              
:ref:`fitToSizer <no-5049>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-5050>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-5051>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-5052>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-5053>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-5054>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-5055>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-5056>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-5057>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-5058>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-5059>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-5060>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-5061>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-5062>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-5063>`      
:ref:`getSizerProp <no-5064>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-5065>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-5066>`                  Make the object invisible.
:ref:`initEvents <no-5067>`            
:ref:`initProperties <no-5068>`        
:ref:`insertItem <no-5069>`            Inserts a new item into the specified position.
:ref:`isContainedBy <no-5070>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-5071>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-5072>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-5073>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-5074>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-5075>`     Given a position relative to the form, return a position relative
:ref:`onChoiceMade <no-5076>`          
:ref:`onHover <no-5077>`               
:ref:`onValueChanged <no-5078>`        
:ref:`paste <no-5079>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-5080>`           
:ref:`processDroppedFiles <no-5081>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-5082>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-5083>`            Raise the passed Dabo event.
:ref:`reCreate <no-5084>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-5085>`              Recreate the object.
:ref:`redraw <no-5086>`                Called when the object is (re)drawn.
:ref:`refresh <no-5087>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-5088>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-5089>`               Destroys the object.
:ref:`removeAll <no-5090>`             Removes all entries from the control.
:ref:`removeDrawnObject <no-5091>`     
:ref:`removeItem <no-5092>`            Removes the item at the specified position.
:ref:`restoreValue <no-5093>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-5094>`             Save control's value to dApp's user settings table.
:ref:`select <no-5095>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-5096>`             Select all text in the control.
:ref:`selectNone <no-5097>`            Select no text in the control.
:ref:`sendToBack <no-5098>`            Places this object behind all others.
:ref:`setAll <no-5099>`                Set all child object properties to the passed value.
:ref:`setFocus <no-5100>`              Sets focus to the object.
:ref:`setPositionInSizer <no-5101>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-5102>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-5103>` Sets a group of properties on the object all at once. This
:ref:`setSelection <no-5104>`          Same as setting property PositionValue.
:ref:`setSizerProp <no-5105>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-5106>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-5107>`                  Make the object visible.
:ref:`showContainingPage <no-5108>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-5109>`       Display a context menu (popup) at the specified position.
:ref:`sort <no-5110>`                  Sorts the list items. By default, the Python 'cmp' function is
:ref:`super <no-5111>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-5112>`           Remove a previously registered event binding.
:ref:`unbindKey <no-5113>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-5114>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-5115>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-5116>`                Update control's value to match the current value from the source.

====================================== ========================


Methods
=======

.. _no-5067:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.initEvents(self)



-------

.. _no-5068:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.initProperties(self)



-------

.. _no-5076:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.onChoiceMade(self, evt)



-------

.. _no-5078:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.onValueChanged(self, evt)



-------


Methods - inherited
=====================

.. _no-5017:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5018:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-5019:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5020:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5021:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5022:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.appendItem(self, txt, select=False)
   :noindex:


   Adds a new item to the end of the list


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-5023:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.autoBindEvents(self, force=True)
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

.. _no-5024:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5025:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5026:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5027:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5028:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-5029:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5030:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5031:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.clearSelections(self)
   :noindex:


   
   Stub method. Only used in the list box, where there
   can be multiple selections.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-5032:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5033:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5034:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5035:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5036:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5037:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5038:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-5039:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5040:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5041:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5042:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5043:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5044:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5045:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5046:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5047:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5048:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5049:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5050:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-5051:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5052:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5053:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5054:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5055:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5056:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-5057:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5058:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5059:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5060:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5061:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5062:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-5063:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-5064:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5065:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5066:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5069:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.insertItem(self, pos, txt, select=False)
   :noindex:


   Inserts a new item into the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-5070:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5071:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5072:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.lockDisplay(self)
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

.. _no-5073:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5074:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5075:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5077:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5079:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5080:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5081:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5082:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5083:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5084:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5085:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5086:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5087:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5088:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5089:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5090:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.removeAll(self)
   :noindex:


   Removes all entries from the control.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-5091:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5092:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.removeItem(self, pos)
   :noindex:


   Removes the item at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-5093:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-5094:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-5095:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-5096:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-5097:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-5098:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5099:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-5100:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5101:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5102:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-5103:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-5104:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setSelection(self, index)
   :noindex:


   Same as setting property PositionValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-5105:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5106:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5107:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5108:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5109:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5110:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.sort(self, sortFunction=None)
   :noindex:


   
   Sorts the list items. By default, the Python 'cmp' function is
   used, but this can be overridden with a custom sortFunction.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-5111:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5112:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5113:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5114:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5115:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5116:

.. function:: dabo.lib.datanav.Page.SelectionOpDropdown.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
