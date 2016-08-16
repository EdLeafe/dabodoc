
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDatePicker

.. _dabo.ui.uiwx.dDatePicker.dDatePicker:

================================================
|doc_title|  **dDatePicker.dDatePicker** - class
================================================


Creates a DatePicker control.
Control purpose is to maintain Date field types, but it can
be used for Timestamp data field types too.
It's behavior is similar to dDateTextBox control.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDatePicker**

.. inheritance-diagram:: dDatePicker


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDatePicker.dDatePicker

   .. automethod:: dabo.ui.uiwx.dDatePicker.dDatePicker.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`AllowNullDate <no-31282>`            If True enable Null vale in date. (bool)(Default=False)
:ref:`Application <no-31283>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-31284>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-31285>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-31286>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-31287>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-31288>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-31289>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-31290>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-31291>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-31292>`                  The caption of the object. (str)
:ref:`Children <no-31293>`                 Returns a list of object references to the children of
:ref:`Class <no-31294>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-31295>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-31296>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-31297>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-31298>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-31299>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-31300>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-31301>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-31302>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-31303>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-31304>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-31305>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-31306>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-31307>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-31308>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-31309>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-31310>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-31311>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-31312>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-31313>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-31314>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-31315>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-31316>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-31317>`              Dynamically determine the value of the Left property.
:ref:`DynamicMaxValue <no-31318>`          Dynamically determine the value of the MaxValue property.
:ref:`DynamicMinValue <no-31319>`          Dynamically determine the value of the MinValue property.
:ref:`DynamicMousePointer <no-31320>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-31321>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-31322>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-31323>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-31324>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-31325>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-31326>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-31327>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-31328>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-31329>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-31330>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-31331>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-31332>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-31333>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-31334>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-31335>`                 Specifies the font face. (str)
:ref:`FontInfo <no-31336>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-31337>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-31338>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-31339>`            Specifies whether text is underlined. (bool)
:ref:`ForceShowCentury <no-31340>`         Regardless of locale setting, century is shown if True. (bool)
:ref:`ForeColor <no-31341>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-31342>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-31343>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-31344>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-31345>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InvalidBackColor <no-31346>`         Color value used for illegal values or values out-of-teh bounds. (str)
:ref:`IsDateValid <no-31347>`              Read-only property tells if Value holds valid date type value.
:ref:`IsSecret <no-31348>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-31349>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-31350>`                Specifies which events to log.  (list of strings)
:ref:`MaxValue <no-31351>`                 Holds upper value limit. (date, tuple, str)(Default=None)
:ref:`MaximumHeight <no-31352>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-31353>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-31354>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinValue <no-31355>`                 Holds lower value limit. (date, tuple, str)(Default=None)
:ref:`MinimumHeight <no-31356>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-31357>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-31358>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-31359>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-31360>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-31361>`                 Specifies the base name of the object.
:ref:`Parent <no-31362>`                   The containing object. (obj)
:ref:`PersistSecretData <no-31363>`        If True, allow persisting the secret data in encrypted form.
:ref:`PickerMode <no-31364>`               Creates control with spin or dropdown calendar. (str)
:ref:`Position <no-31365>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-31366>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-31367>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-31368>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-31369>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-31370>`                     The size of the object. (tuple)
:ref:`Sizer <no-31371>`                    The sizer for the object.
:ref:`Source <no-31372>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-31373>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-31374>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-31375>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-31376>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-31377>`                      The top position of the object. (int)
:ref:`Transparency <no-31378>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-31379>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-31380>`                    Specifies the current state of the control (the value of the field).  (varies)
:ref:`ValueMode <no-31381>`                Enables handling Timestamp type. (str)(Default="Date")
:ref:`Visible <no-31382>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-31383>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-31384>`                    The width of the object. (int)
:ref:`WindowHandle <no-31385>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-31282:

**AllowNullDate** 

If True enable Null vale in date. (bool)(Default=False)



-------

.. _no-31318:

**DynamicMaxValue** 

Dynamically determine the value of the MaxValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MaxValue property. If DynamicMaxValue is set to None (the default), MaxValue
will not be dynamically evaluated.



-------

.. _no-31319:

**DynamicMinValue** 

Dynamically determine the value of the MinValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MinValue property. If DynamicMinValue is set to None (the default), MinValue
will not be dynamically evaluated.



-------

.. _no-31340:

**ForceShowCentury** 

Regardless of locale setting, century is shown if True. (bool)
(Default=False)



-------

.. _no-31346:

**InvalidBackColor** 

Color value used for illegal values or values out-of-teh bounds. (str)
(Default="Yellow")



-------

.. _no-31347:

**IsDateValid** 

Read-only property tells if Value holds valid date type value.



-------

.. _no-31351:

**MaxValue** 

Holds upper value limit. (date, tuple, str)(Default=None)



-------

.. _no-31355:

**MinValue** 

Holds lower value limit. (date, tuple, str)(Default=None)



-------

.. _no-31364:

**PickerMode** 

Creates control with spin or dropdown calendar. (str)
Available values are:
    - Spin
    - Dropdown (default)



-------

.. _no-31381:

**ValueMode** 

Enables handling Timestamp type. (str)(Default="Date")



-------


Properties - inherited
========================

.. _no-31283:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31284:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31285:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31286:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31287:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31288:

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

.. _no-31289:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31290:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31291:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31292:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31293:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31294:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31295:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31296:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31297:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31298:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31299:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31300:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31301:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31302:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31303:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31304:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31305:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31306:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31307:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31308:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31309:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31310:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31311:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31312:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31313:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31314:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31315:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31316:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31317:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31320:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31321:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31322:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31323:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31324:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31325:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31326:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31327:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31328:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31329:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31330:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31331:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31332:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31333:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31334:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31335:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31336:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31337:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31338:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31339:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31341:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31342:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31343:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31344:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31345:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31348:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31349:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31350:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31352:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31353:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31354:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31356:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31357:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31358:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31359:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31360:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31361:

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

.. _no-31362:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31363:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31365:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31366:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31367:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31368:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31369:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31370:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31371:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31372:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31373:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31374:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-31375:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31376:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31377:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31378:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31379:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31380:

**Value** 

Specifies the current state of the control (the value of the field).  (varies)


Inherited from: 'wx._controls.DatePickerCtrlBase - can not provide a link

-------

.. _no-31382:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31383:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31384:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31385:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-31386>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-31387>`                 Occurs after the control or form is created.
:ref:`Destroy <no-31388>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-31389>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-31390>`               Occurs when the control gets the focus.
:ref:`Idle <no-31391>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-31392>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-31393>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-31394>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-31395>`               
:ref:`KeyUp <no-31396>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-31397>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-31398>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-31399>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-31400>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-31401>`             
:ref:`MouseLeave <no-31402>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-31403>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-31404>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-31405>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-31406>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-31407>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-31408>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-31409>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-31410>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-31411>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-31412>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-31413>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-31414>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-31415>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-31416>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-31417>`                   Occurs when the control's position changes.
:ref:`Paint <no-31418>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-31419>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-31420>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-31421>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-31422>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-31423>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-31386:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-31387:

**Create** 

Occurs after the control or form is created.



-------

.. _no-31388:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-31389:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-31390:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-31391:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-31392:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-31393:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-31394:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-31395:

**KeyEvent** 



-------

.. _no-31396:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-31397:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-31398:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-31399:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-31400:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-31401:

**MouseEvent** 



-------

.. _no-31402:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-31403:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-31404:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-31405:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-31406:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-31407:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-31408:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-31409:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-31410:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-31411:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-31412:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-31413:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-31414:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-31415:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-31416:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-31417:

**Move** 

Occurs when the control's position changes.



-------

.. _no-31418:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-31419:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-31420:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-31421:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-31422:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-31423:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-31424>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-31425>`             Instantiate object as a child of self.
:ref:`afterInit <no-31426>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-31427>`          
:ref:`afterSetProperties <no-31428>`    
:ref:`autoBindEvents <no-31429>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-31430>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-31431>`   
:ref:`bindEvent <no-31432>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-31433>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-31434>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-31435>`          Makes this object topmost
:ref:`clear <no-31436>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-31437>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-31438>`  Given a position relative to this control, return a position relative
:ref:`copy <no-31439>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-31440>`                   Called by uiApp when the user requests a cut operation.
:ref:`dayInterval <no-31441>`           Adjusts the date by the given number of days; negative
:ref:`drawArc <no-31442>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-31443>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-31444>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-31445>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-31446>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-31447>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-31448>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-31449>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-31450>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-31451>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-31452>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-31453>`              Draws text on the object at the specified position
:ref:`endHover <no-31454>`              
:ref:`fitToSizer <no-31455>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-31456>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-31457>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-31458>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-31459>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-31460>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-31461>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-31462>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-31463>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-31464>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-31465>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-31466>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-31467>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-31468>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-31469>`      
:ref:`getSizerProp <no-31470>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-31471>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-31472>`                  Make the object invisible.
:ref:`initEvents <no-31473>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-31474>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-31475>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-31476>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-31477>`           Locks the visual updates to the control.
:ref:`monthInterval <no-31478>`         Adjusts the date by the given number of months; negative
:ref:`moveTabOrderAfter <no-31479>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-31480>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-31481>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-31482>`               
:ref:`paste <no-31483>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-31484>`           
:ref:`processDroppedFiles <no-31485>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-31486>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-31487>`            Raise the passed Dabo event.
:ref:`reCreate <no-31488>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-31489>`              Recreate the object.
:ref:`redraw <no-31490>`                Called when the object is (re)drawn.
:ref:`refresh <no-31491>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-31492>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-31493>`               Destroys the object.
:ref:`removeDrawnObject <no-31494>`     
:ref:`restoreValue <no-31495>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-31496>`             Save control's value to dApp's user settings table.
:ref:`select <no-31497>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-31498>`             Select all text in the control.
:ref:`selectNone <no-31499>`            Select no text in the control.
:ref:`sendToBack <no-31500>`            Places this object behind all others.
:ref:`setAll <no-31501>`                Set all child object properties to the passed value.
:ref:`setCurrentDate <no-31502>`        
:ref:`setFocus <no-31503>`              Sets focus to the object.
:ref:`setInvalidDate <no-31504>`        
:ref:`setPositionInSizer <no-31505>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-31506>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-31507>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-31508>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-31509>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`setToMonthDay <no-31510>`         
:ref:`setToYearDay <no-31511>`          
:ref:`show <no-31512>`                  Make the object visible.
:ref:`showContainingPage <no-31513>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-31514>`       Display a context menu (popup) at the specified position.
:ref:`super <no-31515>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-31516>`           Remove a previously registered event binding.
:ref:`unbindKey <no-31517>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-31518>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-31519>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-31520>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-31441:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.dayInterval(self, days)

   Adjusts the date by the given number of days; negative
   values move backwards.
   



-------

.. _no-31478:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.monthInterval(self, months)

   Adjusts the date by the given number of months; negative
   values move backwards.
   



-------

.. _no-31502:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setCurrentDate(self)



-------

.. _no-31504:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setInvalidDate(self)



-------

.. _no-31510:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setToMonthDay(self, day)



-------

.. _no-31511:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setToYearDay(self, day)



-------


Methods - inherited
=====================

.. _no-31424:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31425:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-31426:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31427:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31428:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31429:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.autoBindEvents(self, force=True)
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

.. _no-31430:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31431:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31432:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31433:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31434:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-31435:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31436:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31437:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31438:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31439:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31440:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31442:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31443:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31444:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-31445:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31446:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31447:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31448:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31449:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31450:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31451:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31452:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31453:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31454:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31455:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31456:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31457:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31458:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31459:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31460:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31461:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31462:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31463:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31464:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31465:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31466:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31467:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31468:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-31469:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31470:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31471:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31472:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31473:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31474:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31475:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31476:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31477:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.lockDisplay(self)
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

.. _no-31479:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31480:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31481:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31482:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31483:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31484:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31485:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31486:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31487:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31488:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31489:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31490:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31491:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31492:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31493:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31494:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31495:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31496:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31497:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31498:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31499:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31500:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31501:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-31503:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31505:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31506:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-31507:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-31508:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31509:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31512:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31513:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31514:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31515:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31516:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31517:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31518:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31519:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31520:

.. function:: dabo.ui.uiwx.dDatePicker.dDatePicker.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
