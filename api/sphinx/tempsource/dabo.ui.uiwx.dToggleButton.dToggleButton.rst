
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dToggleButton

.. _dabo.ui.uiwx.dToggleButton.dToggleButton:

====================================================
|doc_title|  **dToggleButton.dToggleButton** - class
====================================================


Creates a button that toggles on and off, for editing boolean values.

This is functionally equivilent to a dCheckbox, but visually much different.
Also, it implies that pushing it will cause some sort of immediate action to
take place, like you get with a normal button.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dToggleButton**

.. inheritance-diagram:: dToggleButton


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`
* :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`
* wx.lib.buttons.GenBitmapTextToggleButton - can not provide a link



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



   * - .. image:: _static/macWidgets/dToggleButton.png
          :scale: 75 %
          :target: _static/macWidgets/dToggleButton.png
          :alt: dToggleButton



     - .. image:: _static/winWidgets/dToggleButton.png
          :scale: 75 %
          :target: _static/winWidgets/dToggleButton.png
          :alt: dToggleButton



     - .. image:: _static/nixWidgets/dToggleButton.png
          :scale: 75 %
          :target: _static/nixWidgets/dToggleButton.png
          :alt: dToggleButton


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dToggleButton.dToggleButton

   .. automethod:: dabo.ui.uiwx.dToggleButton.dToggleButton.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-13952>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-13953>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-13954>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-13955>`              Base key used when saving/restoring preferences  (str)
:ref:`BezelWidth <no-13956>`               Width of the bezel on the sides of the button. Default=5  (int)
:ref:`BorderColor <no-13957>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-13958>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-13959>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-13960>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-13961>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-13962>`                  The caption of the object. (str)
:ref:`Children <no-13963>`                 Returns a list of object references to the children of
:ref:`Class <no-13964>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-13965>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-13966>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-13967>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-13968>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-13969>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DownPicture <no-13970>`              Picture displayed when the button is pressed  (str)
:ref:`DroppedFileHandler <no-13971>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-13972>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-13973>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-13974>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-13975>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-13976>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-13977>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-13978>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-13979>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-13980>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-13981>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-13982>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-13983>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-13984>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-13985>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-13986>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-13987>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-13988>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-13989>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-13990>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-13991>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-13992>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-13993>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-13994>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-13995>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-13996>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-13997>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-13998>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-13999>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-14000>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-14001>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-14002>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-14003>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-14004>`                 Specifies the font face. (str)
:ref:`FontInfo <no-14005>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-14006>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-14007>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-14008>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-14009>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-14010>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-14011>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-14012>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-14013>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-14014>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-14015>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-14016>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-14017>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-14018>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-14019>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-14020>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-14021>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-14022>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-14023>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-14024>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-14025>`                 Specifies the base name of the object.
:ref:`Parent <no-14026>`                   The containing object. (obj)
:ref:`PersistSecretData <no-14027>`        If True, allow persisting the secret data in encrypted form.
:ref:`Picture <no-14028>`                  Picture used for the normal (unselected) state  (str)
:ref:`Position <no-14029>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-14030>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-14031>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-14032>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-14033>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-14034>`                     The size of the object. (tuple)
:ref:`Sizer <no-14035>`                    The sizer for the object.
:ref:`Source <no-14036>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-14037>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-14038>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-14039>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-14040>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-14041>`                      The top position of the object. (int)
:ref:`Transparency <no-14042>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-14043>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-14044>`                    Specifies the current state of the control (the value of the field).  (varies)
:ref:`Visible <no-14045>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-14046>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-14047>`                    The width of the object. (int)
:ref:`WindowHandle <no-14048>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-13956:

**BezelWidth** 

Width of the bezel on the sides of the button. Default=5  (int)



-------

.. _no-13970:

**DownPicture** 

Picture displayed when the button is pressed  (str)



-------


Properties - inherited
========================

.. _no-13952:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13953:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13954:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13955:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13957:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13958:

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

.. _no-13959:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13960:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13961:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13962:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13963:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13964:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13965:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13966:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13967:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-13968:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-13969:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-13971:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13972:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13973:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13974:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13975:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13976:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13977:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13978:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13979:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13980:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13981:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13982:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13983:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13984:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13985:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13986:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13987:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13988:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13989:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13990:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13991:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13992:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13993:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13994:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13995:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13996:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13997:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-13998:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13999:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14000:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14001:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14002:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14003:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14004:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14005:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14006:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14007:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14008:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14009:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14010:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14011:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14012:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14013:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14014:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14015:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14016:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14017:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14018:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14019:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14020:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14021:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14022:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14023:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14024:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14025:

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

.. _no-14026:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14027:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14028:

**Picture** 

Picture used for the normal (unselected) state  (str)


Inherited from: :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`

-------

.. _no-14029:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14030:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14031:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14032:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14033:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14034:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14035:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14036:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14037:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14038:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-14039:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14040:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14041:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14042:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14043:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14044:

**Value** 

Specifies the current state of the control (the value of the field).  (varies)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14045:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14046:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14047:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14048:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-14049>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-14050>`                 Occurs after the control or form is created.
:ref:`Destroy <no-14051>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-14052>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-14053>`               Occurs when the control gets the focus.
:ref:`Hit <no-14054>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-14055>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-14056>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-14057>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-14058>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-14059>`               
:ref:`KeyUp <no-14060>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-14061>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-14062>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-14063>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-14064>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-14065>`             
:ref:`MouseLeave <no-14066>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-14067>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-14068>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-14069>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-14070>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-14071>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-14072>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-14073>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-14074>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-14075>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-14076>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-14077>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-14078>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-14079>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-14080>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-14081>`                   Occurs when the control's position changes.
:ref:`Paint <no-14082>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-14083>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-14084>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-14085>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-14086>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-14087>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-14049:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-14050:

**Create** 

Occurs after the control or form is created.



-------

.. _no-14051:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-14052:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-14053:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-14054:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-14055:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-14056:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-14057:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-14058:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-14059:

**KeyEvent** 



-------

.. _no-14060:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-14061:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-14062:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-14063:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-14064:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-14065:

**MouseEvent** 



-------

.. _no-14066:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-14067:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-14068:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-14069:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-14070:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-14071:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-14072:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-14073:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-14074:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-14075:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-14076:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-14077:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-14078:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-14079:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-14080:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-14081:

**Move** 

Occurs when the control's position changes.



-------

.. _no-14082:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-14083:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-14084:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-14085:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-14086:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-14087:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-14088>`           Translates a position value for a control to absolute screen position.
:ref:`addObject <no-14089>`                     Instantiate object as a child of self.
:ref:`afterInit <no-14090>`                     Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-14091>`                  
:ref:`afterSetProperties <no-14092>`            
:ref:`autoBindEvents <no-14093>`                Automatically bind any on*() methods to the associated event.
:ref:`base_AcceptsFocus <no-14094>`             Please use PyControl.AcceptsFocus instead.
:ref:`base_AcceptsFocusFromKeyboard <no-14095>` Please use PyControl.AcceptsFocusFromKeyboard instead.
:ref:`base_AddChild <no-14096>`                 Please use PyControl.AddChild instead.
:ref:`base_DoGetBestSize <no-14097>`            Please use PyControl.DoGetBestSize instead.
:ref:`base_DoGetClientSize <no-14098>`          Please use PyControl.DoGetClientSize instead.
:ref:`base_DoGetPosition <no-14099>`            Please use PyControl.DoGetPosition instead.
:ref:`base_DoGetSize <no-14100>`                Please use PyControl.DoGetSize instead.
:ref:`base_DoGetVirtualSize <no-14101>`         Please use PyControl.DoGetVirtualSize instead.
:ref:`base_DoMoveWindow <no-14102>`             Please use PyControl.DoMoveWindow instead.
:ref:`base_DoSetClientSize <no-14103>`          Please use PyControl.DoSetClientSize instead.
:ref:`base_DoSetSize <no-14104>`                Please use PyControl.DoSetSize instead.
:ref:`base_DoSetVirtualSize <no-14105>`         Please use PyControl.DoSetVirtualSize instead.
:ref:`base_Enable <no-14106>`                   Please use PyControl.Enable instead.
:ref:`base_GetDefaultAttributes <no-14107>`     Please use PyControl.GetDefaultAttributes instead.
:ref:`base_GetMaxSize <no-14108>`               Please use PyControl.GetMaxSize instead.
:ref:`base_InitDialog <no-14109>`               Please use PyControl.InitDialog instead.
:ref:`base_OnInternalIdle <no-14110>`           Please use PyControl.OnInternalIdle instead.
:ref:`base_RemoveChild <no-14111>`              Please use PyControl.RemoveChild instead.
:ref:`base_ShouldInheritColours <no-14112>`     Please use PyControl.ShouldInheritColours instead.
:ref:`base_TransferDataFromWindow <no-14113>`   Please use PyControl.TransferDataFromWindow instead.
:ref:`base_TransferDataToWindow <no-14114>`     Please use PyControl.TransferDataToWindow instead.
:ref:`base_Validate <no-14115>`                 Please use PyControl.Validate instead.
:ref:`beforeInit <no-14116>`                    Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-14117>`           
:ref:`bindEvent <no-14118>`                     Bind a dEvent to a callback function.
:ref:`bindEvents <no-14119>`                    Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-14120>`                       Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-14121>`                  Makes this object topmost
:ref:`clear <no-14122>`                         Clears the background of custom-drawn objects.
:ref:`clone <no-14123>`                         Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-14124>`          Given a position relative to this control, return a position relative
:ref:`copy <no-14125>`                          Called by uiApp when the user requests a copy operation.
:ref:`cut <no-14126>`                           Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-14127>`                       Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-14128>`                    Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-14129>`                    Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-14130>`                   Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-14131>`               Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-14132>`                  Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-14133>`                      Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-14134>`                 Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-14135>`                   Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-14136>`                 Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-14137>`          Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-14138>`                      Draws text on the object at the specified position
:ref:`endHover <no-14139>`                      
:ref:`fitToSizer <no-14140>`                    Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-14141>`                    Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-14142>`                    Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-14143>`                Reset the font zoom back to zero.
:ref:`fontZoomOut <no-14144>`                   Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-14145>`               Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-14146>`               Return the fully qualified name of the object.
:ref:`getBlankValue <no-14147>`                 
:ref:`getCaptureBitmap <no-14148>`              Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-14149>`             Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-14150>`              Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-14151>`              Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-14152>`            Convenience method to let you call this directly on the object.
:ref:`getProperties <no-14153>`                 Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-14154>`              
:ref:`getSizerProp <no-14155>`                  Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-14156>`                 Returns a dict containing the object's sizer property info. The
:ref:`hide <no-14157>`                          Make the object invisible.
:ref:`initEvents <no-14158>`                    Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-14159>`                Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-14160>`                 Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-14161>`                   Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-14162>`                   Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-14163>`             Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-14164>`            Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-14165>`             Given a position relative to the form, return a position relative
:ref:`onHover <no-14166>`                       
:ref:`paste <no-14167>`                         Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-14168>`                   
:ref:`processDroppedFiles <no-14169>`           Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-14170>`            Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-14171>`                    Raise the passed Dabo event.
:ref:`reCreate <no-14172>`                      Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-14173>`                      Recreate the object.
:ref:`redraw <no-14174>`                        Called when the object is (re)drawn.
:ref:`refresh <no-14175>`                       Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-14176>`           Translates an absolute screen position to position value for a control.
:ref:`release <no-14177>`                       Destroys the object.
:ref:`removeDrawnObject <no-14178>`             
:ref:`restoreValue <no-14179>`                  Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-14180>`                     Save control's value to dApp's user settings table.
:ref:`select <no-14181>`                        Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-14182>`                     Select all text in the control.
:ref:`selectNone <no-14183>`                    Select no text in the control.
:ref:`sendToBack <no-14184>`                    Places this object behind all others.
:ref:`setAll <no-14185>`                        Set all child object properties to the passed value.
:ref:`setFocus <no-14186>`                      Sets focus to the object.
:ref:`setPositionInSizer <no-14187>`            Convenience method to let you call this directly on the object.
:ref:`setProperties <no-14188>`                 Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-14189>`         Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-14190>`                  Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-14191>`                 Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-14192>`                          Make the object visible.
:ref:`showContainingPage <no-14193>`            If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-14194>`               Display a context menu (popup) at the specified position.
:ref:`super <no-14195>`                         This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-14196>`                   Remove a previously registered event binding.
:ref:`unbindKey <no-14197>`                     Unbind a previously bound key combination.
:ref:`unlockDisplay <no-14198>`                 Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-14199>`              Immediately unlocks the display, no matter how many previous
:ref:`update <no-14200>`                        Update control's value to match the current value from the source.

=============================================== ========================


Methods
=======

.. _no-14147:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getBlankValue(self)



-------


Methods - inherited
=====================

.. _no-14088:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14089:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-14090:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14091:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14092:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14093:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.autoBindEvents(self, force=True)
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

.. _no-14094:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_AcceptsFocus(*args, \**kwargs)
   :noindex:


   Please use PyControl.AcceptsFocus instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14095:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_AcceptsFocusFromKeyboard(*args, \**kwargs)
   :noindex:


   Please use PyControl.AcceptsFocusFromKeyboard instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14096:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_AddChild(*args, \**kwargs)
   :noindex:


   Please use PyControl.AddChild instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14097:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoGetBestSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetBestSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14098:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoGetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetClientSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14099:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoGetPosition(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetPosition instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14100:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoGetSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14101:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoGetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetVirtualSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14102:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoMoveWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoMoveWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14103:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoSetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetClientSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14104:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoSetSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14105:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_DoSetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetVirtualSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14106:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_Enable(*args, \**kwargs)
   :noindex:


   Please use PyControl.Enable instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14107:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_GetDefaultAttributes(*args, \**kwargs)
   :noindex:


   Please use PyControl.GetDefaultAttributes instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14108:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_GetMaxSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.GetMaxSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14109:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_InitDialog(*args, \**kwargs)
   :noindex:


   Please use PyControl.InitDialog instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14110:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_OnInternalIdle(*args, \**kwargs)
   :noindex:


   Please use PyControl.OnInternalIdle instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14111:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_RemoveChild(*args, \**kwargs)
   :noindex:


   Please use PyControl.RemoveChild instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14112:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_ShouldInheritColours(*args, \**kwargs)
   :noindex:


   Please use PyControl.ShouldInheritColours instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14113:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_TransferDataFromWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.TransferDataFromWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14114:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_TransferDataToWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.TransferDataToWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14115:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.base_Validate(*args, \**kwargs)
   :noindex:


   Please use PyControl.Validate instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-14116:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14117:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14118:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14119:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14120:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-14121:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14122:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14123:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14124:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14125:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14126:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14127:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14128:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14129:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-14130:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14131:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14132:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14133:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14134:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14135:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14136:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14137:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14138:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14139:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14140:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14141:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14142:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14143:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14144:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14145:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14146:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14148:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14149:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14150:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14151:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14152:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14153:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-14154:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14155:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14156:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14157:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14158:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14159:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14160:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14161:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14162:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.lockDisplay(self)
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

.. _no-14163:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14164:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14165:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14166:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14167:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14168:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14169:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14170:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14171:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14172:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14173:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14174:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14175:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14176:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14177:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14178:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14179:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14180:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14181:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-14182:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-14183:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-14184:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14185:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-14186:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14187:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14188:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-14189:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-14190:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14191:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14192:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14193:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14194:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14195:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14196:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14197:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14198:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14199:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14200:

.. function:: dabo.ui.uiwx.dToggleButton.dToggleButton.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
