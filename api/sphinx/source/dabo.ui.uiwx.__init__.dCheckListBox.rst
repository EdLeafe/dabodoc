
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.__init__

.. _dabo.ui.uiwx.__init__.dCheckListBox:

.. _dabo.ui.uiwx.dCheckListBox:

===============================================
|doc_title|  **__init__.dCheckListBox** - class
===============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dCheckListBox**

.. inheritance-diagram:: dCheckListBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dCheckList.dCheckList`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.__init__.dCheckListBox

   .. automethod:: dabo.ui.uiwx.__init__.dCheckListBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-20008>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-20009>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-20010>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-20011>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-20012>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-20013>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-20014>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-20015>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-20016>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-20017>`                  The caption of the object. (str)
:ref:`Children <no-20018>`                 Returns a list of object references to the children of
:ref:`Choices <no-20019>`                  Specifies the string choices to display in the list.
:ref:`Class <no-20020>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-20021>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-20022>`     Reference to the sizer item that control's this control's layout.
:ref:`Count <no-20023>`                    Number of items in the control.
:ref:`DataField <no-20024>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-20025>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-20026>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-20027>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-20028>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-20029>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-20030>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-20031>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-20032>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-20033>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-20034>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-20035>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-20036>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-20037>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-20038>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-20039>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-20040>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-20041>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-20042>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-20043>`            Dynamically determine the value of the Height property.
:ref:`DynamicKeyValue <no-20044>`          Dynamically determine the value of the KeyValue property.
:ref:`DynamicLeft <no-20045>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-20046>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-20047>`          Dynamically determine the value of the Position property.
:ref:`DynamicPositionValue <no-20048>`     Dynamically determine the value of the PositionValue property.
:ref:`DynamicSize <no-20049>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-20050>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStringValue <no-20051>`       Dynamically determine the value of the StringValue property.
:ref:`DynamicTag <no-20052>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-20053>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-20054>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-20055>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-20056>`             Dynamically determine the value of the Value property.
:ref:`DynamicValueMode <no-20057>`         Dynamically determine the value of the ValueMode property.
:ref:`DynamicVisible <no-20058>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-20059>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-20060>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-20061>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-20062>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-20063>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-20064>`                 Specifies the font face. (str)
:ref:`FontInfo <no-20065>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-20066>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-20067>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-20068>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-20069>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-20070>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-20071>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-20072>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-20073>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-20074>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`KeyValue <no-20075>`                 Specifies the key value or values of the selected item or items.
:ref:`Keys <no-20076>`                     Specifies a mapping between arbitrary values and item positions.
:ref:`Left <no-20077>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-20078>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-20079>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-20080>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-20081>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-20082>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-20083>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-20084>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-20085>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`MultipleSelect <no-20086>`           MultipleSelect for dCheckList is always True.
:ref:`Name <no-20087>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-20088>`                 Specifies the base name of the object.
:ref:`Parent <no-20089>`                   The containing object. (obj)
:ref:`PersistSecretData <no-20090>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-20091>`                 The (x,y) position of the object. (tuple)
:ref:`PositionValue <no-20092>`            Specifies the position (index) of the selected item(s).
:ref:`PreferenceManager <no-20093>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-20094>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-20095>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-20096>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-20097>`                     The size of the object. (tuple)
:ref:`Sizer <no-20098>`                    The sizer for the object.
:ref:`SortFunction <no-20099>`             Function used to sort list items when Sorted=True. Default=None,
:ref:`Sorted <no-20100>`                   Are the items in the control automatically sorted? Default=False.
:ref:`Source <no-20101>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-20102>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StringValue <no-20103>`              Specifies the text of the selected item.
:ref:`TabStop <no-20104>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-20105>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-20106>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-20107>`                      The top position of the object. (int)
:ref:`Transparency <no-20108>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-20109>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-20110>`                    Specifies which item is currently selected in the list.
:ref:`ValueMode <no-20111>`                Specifies the information that the Value property refers to.
:ref:`Visible <no-20112>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-20113>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-20114>`                    The width of the object. (int)
:ref:`WindowHandle <no-20115>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties - inherited
========================

.. _no-20008:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20009:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20010:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20011:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20012:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20013:

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

.. _no-20014:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20015:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20016:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20017:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20018:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20019:

**Choices** 

Specifies the string choices to display in the list.
    -> List of strings. Read-write at runtime.
    The list index becomes the PositionValue, and the string
    becomes the StringValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20020:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20021:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20022:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20023:

**Count** 

Number of items in the control.
    -> Integer. Read-only.


Inherited from: 'wx._core.ItemContainer - can not provide a link

-------

.. _no-20024:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20025:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20026:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20027:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20028:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20029:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20030:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20031:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20032:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20033:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20034:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20035:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20036:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20037:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20038:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20039:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20040:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20041:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20042:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20043:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20044:

**DynamicKeyValue** 

Dynamically determine the value of the KeyValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
KeyValue property. If DynamicKeyValue is set to None (the default), KeyValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20045:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20046:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20047:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20048:

**DynamicPositionValue** 

Dynamically determine the value of the PositionValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PositionValue property. If DynamicPositionValue is set to None (the default), PositionValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20049:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20050:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20051:

**DynamicStringValue** 

Dynamically determine the value of the StringValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StringValue property. If DynamicStringValue is set to None (the default), StringValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20052:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20053:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20054:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20055:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20056:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-20057:

**DynamicValueMode** 

Dynamically determine the value of the ValueMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueMode property. If DynamicValueMode is set to None (the default), ValueMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20058:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20059:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20060:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20061:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20062:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20063:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20064:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20065:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20066:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20067:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20068:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20069:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20070:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20071:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20072:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20073:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20074:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20075:

**KeyValue** 

Specifies the key value or values of the selected item or items.
    -> Type can vary. Read-write at runtime.
    Returns the key value or values of the selected item(s), or selects
    the item(s) with the specified KeyValue(s).    An exception will be
    raised if the Keys property hasn't been set up to accomodate.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20076:

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

.. _no-20077:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20078:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20079:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20080:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20081:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20082:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20083:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20084:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20085:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20086:

**MultipleSelect** 

MultipleSelect for dCheckList is always True.


Inherited from: :ref:`dabo.ui.uiwx.dCheckList.dCheckList`

-------

.. _no-20087:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20088:

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

.. _no-20089:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20090:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20091:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20092:

**PositionValue** 

Specifies the position (index) of the selected item(s).
    -> Integer or tuple of integers. Read-write at runtime.
    Returns the current position(s), or sets the current position(s).


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20093:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20094:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20095:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20096:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20097:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20098:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20099:

**SortFunction** 

Function used to sort list items when Sorted=True. Default=None,
    which gives the default sorting  (callable or None)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20100:

**Sorted** 

Are the items in the control automatically sorted? Default=False.
    If True, whenever the Choices property is changed, the resulting list
    will be first sorted using the SortFunction property, which defaults to
    None, giving a default sort order.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20101:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20102:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20103:

**StringValue** 

Specifies the text of the selected item.
    -> String or tuple of strings. Read-write at runtime.
    Returns the text of the selected item(s), or selects the item(s)
    with the specified text. An exception is raised if there is no
    position with matching text.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20104:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-20105:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20106:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20107:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20108:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20109:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20110:

**Value** 

Specifies which item is currently selected in the list.
    -> Type can vary. Read-write at runtime.
    Value refers to one of the following, depending on the setting of ValueMode:

        + ValueMode="Position" : the index of the selected item(s) (integer)
        + ValueMode="String"   : the displayed string of the selected item(s) (string)
        + ValueMode="Key"      : the key of the selected item(s) (can vary)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20111:

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

.. _no-20112:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20113:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20114:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20115:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-20116>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-20117>`                 Occurs after the control or form is created.
:ref:`Destroy <no-20118>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-20119>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-20120>`               Occurs when the control gets the focus.
:ref:`Idle <no-20121>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-20122>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-20123>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-20124>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-20125>`               
:ref:`KeyUp <no-20126>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-20127>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-20128>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-20129>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-20130>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-20131>`             
:ref:`MouseLeave <no-20132>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-20133>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-20134>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-20135>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-20136>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-20137>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-20138>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-20139>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-20140>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-20141>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-20142>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-20143>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-20144>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-20145>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-20146>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-20147>`                   Occurs when the control's position changes.
:ref:`Paint <no-20148>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-20149>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-20150>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-20151>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-20152>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-20153>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-20116:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-20117:

**Create** 

Occurs after the control or form is created.



-------

.. _no-20118:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-20119:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-20120:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-20121:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-20122:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-20123:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-20124:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-20125:

**KeyEvent** 



-------

.. _no-20126:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-20127:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-20128:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-20129:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-20130:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-20131:

**MouseEvent** 



-------

.. _no-20132:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-20133:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-20134:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-20135:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-20136:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-20137:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-20138:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-20139:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-20140:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-20141:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-20142:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-20143:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-20144:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-20145:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-20146:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-20147:

**Move** 

Occurs when the control's position changes.



-------

.. _no-20148:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-20149:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-20150:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-20151:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-20152:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-20153:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-20154>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-20155>`             Instantiate object as a child of self.
:ref:`afterInit <no-20156>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-20157>`          
:ref:`afterSetProperties <no-20158>`    
:ref:`appendItem <no-20159>`            Adds a new item to the end of the list
:ref:`autoBindEvents <no-20160>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-20161>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-20162>`   
:ref:`bindEvent <no-20163>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-20164>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-20165>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-20166>`          Makes this object topmost
:ref:`clear <no-20167>`                 Clears the background of custom-drawn objects.
:ref:`clearSelections <no-20168>`       Set all items to unchecked.
:ref:`clone <no-20169>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-20170>`  Given a position relative to this control, return a position relative
:ref:`copy <no-20171>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-20172>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-20173>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-20174>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-20175>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-20176>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-20177>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-20178>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-20179>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-20180>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-20181>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-20182>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-20183>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-20184>`              Draws text on the object at the specified position
:ref:`endHover <no-20185>`              
:ref:`fitToSizer <no-20186>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-20187>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-20188>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-20189>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-20190>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-20191>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-20192>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-20193>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-20194>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-20195>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-20196>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-20197>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-20198>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-20199>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-20200>`      
:ref:`getSizerProp <no-20201>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-20202>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-20203>`                  Make the object invisible.
:ref:`initEvents <no-20204>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-20205>`        Hook for subclasses. User subclasses should set properties
:ref:`insertItem <no-20206>`            Inserts a new item into the specified position.
:ref:`invertSelections <no-20207>`      Switch all the items from False to True, and vice-versa.
:ref:`isContainedBy <no-20208>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-20209>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-20210>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-20211>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-20212>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-20213>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-20214>`               
:ref:`paste <no-20215>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-20216>`           
:ref:`processDroppedFiles <no-20217>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-20218>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-20219>`            Raise the passed Dabo event.
:ref:`reCreate <no-20220>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-20221>`              Recreate the object.
:ref:`redraw <no-20222>`                Called when the object is (re)drawn.
:ref:`refresh <no-20223>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-20224>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-20225>`               Destroys the object.
:ref:`removeAll <no-20226>`             Removes all entries from the control.
:ref:`removeDrawnObject <no-20227>`     
:ref:`removeItem <no-20228>`            Removes the item at the specified position.
:ref:`restoreValue <no-20229>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-20230>`             Save control's value to dApp's user settings table.
:ref:`select <no-20231>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-20232>`             Set all items to checked.
:ref:`selectNone <no-20233>`            Set all items to unchecked.
:ref:`sendToBack <no-20234>`            Places this object behind all others.
:ref:`setAll <no-20235>`                Set all child object properties to the passed value.
:ref:`setFocus <no-20236>`              Sets focus to the object.
:ref:`setPositionInSizer <no-20237>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-20238>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-20239>` Sets a group of properties on the object all at once. This
:ref:`setSelection <no-20240>`          
:ref:`setSizerProp <no-20241>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-20242>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-20243>`                  Make the object visible.
:ref:`showContainingPage <no-20244>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-20245>`       Display a context menu (popup) at the specified position.
:ref:`sort <no-20246>`                  Sorts the list items. By default, the Python 'cmp' function is
:ref:`super <no-20247>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-20248>`           Remove a previously registered event binding.
:ref:`unbindKey <no-20249>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-20250>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-20251>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-20252>`                Update control's value to match the current value from the source.

======================================= ========================


Methods - inherited
=====================

.. _no-20154:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20155:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-20156:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20157:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20158:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20159:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.appendItem(self, txt, select=False)
   :noindex:


   Adds a new item to the end of the list


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20160:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.autoBindEvents(self, force=True)
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

.. _no-20161:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20162:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20163:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20164:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20165:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-20166:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20167:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20168:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.clearSelections(self)
   :noindex:


   Set all items to unchecked.


Inherited from: :ref:`dabo.ui.uiwx.dCheckList.dCheckList`

-------

.. _no-20169:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20170:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20171:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20172:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20173:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20174:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20175:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-20176:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20177:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20178:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20179:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20180:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20181:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20182:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20183:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20184:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20185:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20186:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20187:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20188:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20189:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20190:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20191:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20192:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20193:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20194:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20195:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20196:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20197:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20198:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20199:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-20200:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20201:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20202:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20203:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20204:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20205:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20206:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.insertItem(self, pos, txt, select=False)
   :noindex:


   Inserts a new item into the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20207:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.invertSelections(self)
   :noindex:


   Switch all the items from False to True, and vice-versa.


Inherited from: :ref:`dabo.ui.uiwx.dCheckList.dCheckList`

-------

.. _no-20208:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20209:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20210:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.lockDisplay(self)
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

.. _no-20211:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20212:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20213:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20214:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20215:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20216:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20217:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20218:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20219:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20220:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20221:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20222:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20223:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20224:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20225:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20226:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.removeAll(self)
   :noindex:


   Removes all entries from the control.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20227:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20228:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.removeItem(self, pos)
   :noindex:


   Removes the item at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20229:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20230:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-20231:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-20232:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.selectAll(self)
   :noindex:


   Set all items to checked.


Inherited from: :ref:`dabo.ui.uiwx.dCheckList.dCheckList`

-------

.. _no-20233:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.selectNone(self)
   :noindex:


   Set all items to unchecked.


Inherited from: :ref:`dabo.ui.uiwx.dCheckList.dCheckList`

-------

.. _no-20234:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20235:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-20236:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20237:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20238:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-20239:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-20240:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setSelection(self, index)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCheckList.dCheckList`

-------

.. _no-20241:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20242:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20243:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20244:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20245:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20246:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.sort(self, sortFunction=None)
   :noindex:


   
   Sorts the list items. By default, the Python 'cmp' function is
   used, but this can be overridden with a custom sortFunction.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-20247:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20248:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20249:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20250:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20251:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20252:

.. function:: dabo.ui.uiwx.__init__.dCheckListBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
