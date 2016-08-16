
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dNumericBox

.. _dabo.ui.uiwx.dNumericBox.dNumericBox:

================================================
|doc_title|  **dNumericBox.dNumericBox** - class
================================================

This is a specialized textbox class that maintains numeric values.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dNumericBox**

.. inheritance-diagram:: dNumericBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`
* :ref:`wx.lib.masked.numctrl.NumCtrl`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dNumericBox.dNumericBox

   .. automethod:: dabo.ui.uiwx.dNumericBox.dNumericBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-11266>`                Specifies the alignment of the text. (str)
:ref:`AllowNegative <no-11267>`            Enables/disables negative numbers. (bool)
:ref:`AllowNoneValue <no-11268>`           Enables/disables undefined value - None. (bool)
:ref:`Application <no-11269>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoWidth <no-11270>`                Indicates whether or not the control should set its own
:ref:`BackColor <no-11271>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-11272>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-11273>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-11274>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-11275>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-11276>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-11277>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-11278>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-11279>`                  The caption of the object. (str)
:ref:`Children <no-11280>`                 Returns a list of object references to the children of
:ref:`Class <no-11281>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-11282>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-11283>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-11284>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-11285>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DecimalChar <no-11286>`              Defines character that will be used to represent
:ref:`DecimalWidth <no-11287>`             Tells how many decimal places to show for numeric value. (int)
:ref:`DisableOnEmptyDataSource <no-11288>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-11289>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-11290>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-11291>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-11292>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-11293>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-11294>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-11295>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-11296>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-11297>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-11298>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-11299>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-11300>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-11301>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-11302>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-11303>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-11304>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-11305>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-11306>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-11307>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-11308>`              Dynamically determine the value of the Left property.
:ref:`DynamicMaxValue <no-11309>`          Dynamically determine the value of the MaxValue property.
:ref:`DynamicMinValue <no-11310>`          Dynamically determine the value of the MinValue property.
:ref:`DynamicMousePointer <no-11311>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-11312>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-11313>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-11314>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-11315>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-11316>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-11317>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-11318>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-11319>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-11320>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-11321>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-11322>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-11323>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-11324>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-11325>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-11326>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-11327>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-11328>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-11329>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-11330>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-11331>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-11332>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-11333>`                 Specifies the font face. (str)
:ref:`FontInfo <no-11334>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-11335>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-11336>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-11337>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-11338>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-11339>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-11340>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`GroupChar <no-11341>`                What grouping character will be used if allowed.
:ref:`Height <no-11342>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-11343>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-11344>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-11345>`        Position of the insertion point within the control  (int)
:ref:`IntegerWidth <no-11346>`             Indicates how many places to the right of any decimal point
:ref:`InvalidBackColor <no-11347>`         Color value used for illegal values or values
:ref:`IsSecret <no-11348>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-11349>`                     Specifies the left position of the object. (int)
:ref:`LimitValue <no-11350>`               Limit control value to Min and Max bounds. When set to True,
:ref:`LogEvents <no-11351>`                Specifies which events to log.  (list of strings)
:ref:`MaxValue <no-11352>`                 The maximum value that the control should allow.
:ref:`MaximumHeight <no-11353>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-11354>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-11355>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinValue <no-11356>`                 The minimum value that the control should allow.
:ref:`MinimumHeight <no-11357>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-11358>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-11359>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-11360>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-11361>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-11362>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-11363>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-11364>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`ParensForNegatives <no-11365>`       If true, this will cause negative numbers to be displayed with parens
:ref:`Parent <no-11366>`                   The containing object. (obj)
:ref:`PasswordEntry <no-11367>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-11368>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-11369>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-11370>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-11371>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-11372>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-11373>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-11374>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-11375>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-11376>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-11377>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-11378>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-11379>`           Position of the beginning of the selected text. If no text is
:ref:`SignedForeColor <no-11380>`          Color value used for negative values of the control. (str)
:ref:`Size <no-11381>`                     The size of the object. (tuple)
:ref:`Sizer <no-11382>`                    The sizer for the object.
:ref:`Source <no-11383>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-11384>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-11385>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-11386>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-11387>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-11388>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-11389>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-11390>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-11391>`                      The top position of the object. (int)
:ref:`Transparency <no-11392>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-11393>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-11394>`                    Specifies the current state of the control (the value of the field).
:ref:`Visible <no-11395>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-11396>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-11397>`                    The width of the object. (int)
:ref:`WindowHandle <no-11398>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-11267:

**AllowNegative** 

Enables/disables negative numbers. (bool)
    Default=True



-------

.. _no-11268:

**AllowNoneValue** 

Enables/disables undefined value - None. (bool)
    Default=False



-------

.. _no-11270:

**AutoWidth** 

Indicates whether or not the control should set its own
    width based on the integer and fraction widths. (bool)
    Default=True



-------

.. _no-11286:

**DecimalChar** 

Defines character that will be used to represent
    the decimal point. (str)
    Default value comes from locale setting.



-------

.. _no-11287:

**DecimalWidth** 

Tells how many decimal places to show for numeric value. (int)
    Default=2



-------

.. _no-11309:

**DynamicMaxValue** 

Dynamically determine the value of the MaxValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MaxValue property. If DynamicMaxValue is set to None (the default), MaxValue
will not be dynamically evaluated.



-------

.. _no-11310:

**DynamicMinValue** 

Dynamically determine the value of the MinValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MinValue property. If DynamicMinValue is set to None (the default), MinValue
will not be dynamically evaluated.



-------

.. _no-11341:

**GroupChar** 

What grouping character will be used if allowed.
    If set to None, no grouping is allowed. (str)
    Default value comes from locale setting.



-------

.. _no-11346:

**IntegerWidth** 

Indicates how many places to the right of any decimal point
        should be allowed in the control. (int)
        Default=10



-------

.. _no-11347:

**InvalidBackColor** 

Color value used for illegal values or values
    out-of-bounds. (str)
    Default='Yellow'



-------

.. _no-11350:

**LimitValue** 

Limit control value to Min and Max bounds. When set to True,
    if invalid, will be automatically reseted to default.
    When False, only background color will change. (bool)
    Default=False



-------

.. _no-11352:

**MaxValue** 

The maximum value that the control should allow.
    Set to None if limit is disabled. (int, decimal)
    Default=None



-------

.. _no-11356:

**MinValue** 

The minimum value that the control should allow.
    Set to None if limit is disabled. (int, decimal)
    Default=None



-------

.. _no-11365:

**ParensForNegatives** 

If true, this will cause negative numbers to be displayed with parens
    rather than with sign mark. (bool)
    Default=False



-------

.. _no-11380:

**SignedForeColor** 

Color value used for negative values of the control. (str)
    Default='Red'



-------


Properties - inherited
========================

.. _no-11266:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-11269:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11271:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11272:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11273:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11274:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11275:

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

.. _no-11276:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11277:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11278:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11279:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11280:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11281:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11282:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11283:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11284:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11285:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11288:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11289:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11290:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11291:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11292:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11293:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11294:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11295:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11296:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11297:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11298:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11299:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11300:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11301:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11302:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11303:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11304:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11305:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11306:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11307:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11308:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11311:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11312:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11313:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11314:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11315:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11316:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11317:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11318:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11319:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11320:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11321:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11322:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11323:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11324:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11325:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11326:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-11327:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11328:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11329:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11330:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11331:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11332:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11333:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11334:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11335:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11336:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11337:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11338:

**ForceCase** 

Determines if we change the case of entered text. Possible values are:

        ===========  =====================
        None or ""   No changes made (default)
        "Upper"      FORCE TO UPPER CASE
        "Lower"      Force to lower case
        "Title"      Force To Title Case
        ===========  =====================

    These can be abbreviated to "u", "l" or "t"  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11339:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11340:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11342:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11343:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11344:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11345:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11348:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11349:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11351:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11353:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11354:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11355:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11357:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11358:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11359:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11360:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11361:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11362:

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

.. _no-11363:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11364:

**NumericBlankToZero** 

Specifies whether a blank textbox gets interpreted as 0.

    When True, if the user clears the textbox value, such as by selecting all
    and pressing the space bar or delete, the value will become 0 when the
    control loses focus.

    When False, the value will revert back to the last numeric value when the
    control loses focus.

    The default comes from dabo.dTextBox_NumericBlankToZero, which defaults to
    False.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11366:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11367:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11368:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11369:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11370:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11371:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11372:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11373:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11374:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11375:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)
    Default=False


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11376:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11377:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11378:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11379:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11381:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11382:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11383:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11384:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11385:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11386:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11387:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-11388:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11389:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11390:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11391:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11392:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11393:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11394:

**Value** 

Specifies the current state of the control (the value of the field).
    (int, Decimal)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------

.. _no-11395:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11396:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11397:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11398:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-11399>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-11400>`                 Occurs after the control or form is created.
:ref:`Destroy <no-11401>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-11402>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-11403>`               Occurs when the control gets the focus.
:ref:`Idle <no-11404>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-11405>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-11406>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-11407>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-11408>`               
:ref:`KeyUp <no-11409>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-11410>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-11411>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-11412>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-11413>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-11414>`             
:ref:`MouseLeave <no-11415>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-11416>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-11417>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-11418>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-11419>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-11420>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-11421>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-11422>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-11423>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-11424>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-11425>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-11426>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-11427>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-11428>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-11429>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-11430>`                   Occurs when the control's position changes.
:ref:`Paint <no-11431>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-11432>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-11433>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-11434>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-11435>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-11436>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-11399:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-11400:

**Create** 

Occurs after the control or form is created.



-------

.. _no-11401:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-11402:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-11403:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-11404:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-11405:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-11406:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-11407:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-11408:

**KeyEvent** 



-------

.. _no-11409:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-11410:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-11411:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-11412:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-11413:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-11414:

**MouseEvent** 



-------

.. _no-11415:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-11416:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-11417:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-11418:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-11419:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-11420:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-11421:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-11422:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-11423:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-11424:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-11425:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-11426:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-11427:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-11428:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-11429:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-11430:

**Move** 

Occurs when the control's position changes.



-------

.. _no-11431:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-11432:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-11433:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-11434:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-11435:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-11436:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================== ========================
:ref:`absoluteCoordinates <no-11437>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-11438>`                    Instantiate object as a child of self.
:ref:`afterInit <no-11439>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-11440>`                 
:ref:`afterSetProperties <no-11441>`           
:ref:`autoBindEvents <no-11442>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-11443>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-11444>`          
:ref:`bindEvent <no-11445>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-11446>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-11447>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-11448>`                 Makes this object topmost
:ref:`charsAfterCursor <no-11449>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-11450>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-11451>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-11452>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-11453>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-11454>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-11455>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-11456>`                          Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-11457>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-11458>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-11459>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-11460>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-11461>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-11462>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-11463>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-11464>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-11465>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-11466>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-11467>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-11468>`                     Draws text on the object at the specified position
:ref:`endHover <no-11469>`                     
:ref:`fitToSizer <no-11470>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-11471>`                   
:ref:`fontZoomIn <no-11472>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-11473>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-11474>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-11475>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-11476>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-11477>`                
:ref:`getCaptureBitmap <no-11478>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-11479>`            Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-11480>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-11481>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-11482>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-11483>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-11484>`             
:ref:`getSizerProp <no-11485>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-11486>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-11487>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-11488>`                         Make the object invisible.
:ref:`initEvents <no-11489>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-11490>`               Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-11491>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-11492>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-11493>`                  Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-11494>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-11495>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-11496>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-11497>`                      
:ref:`paste <no-11498>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-11499>`                  
:ref:`processDroppedFiles <no-11500>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-11501>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-11502>`                   Raise the passed Dabo event.
:ref:`reCreate <no-11503>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-11504>`                     Recreate the object.
:ref:`redraw <no-11505>`                       Called when the object is (re)drawn.
:ref:`refresh <no-11506>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-11507>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-11508>`                      Destroys the object.
:ref:`removeDrawnObject <no-11509>`            
:ref:`restoreValue <no-11510>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-11511>`                    Save control's value to dApp's user settings table.
:ref:`select <no-11512>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-11513>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-11514>`                   Select no text in the control.
:ref:`sendToBack <no-11515>`                   Places this object behind all others.
:ref:`setAll <no-11516>`                       Set all child object properties to the passed value.
:ref:`setFocus <no-11517>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-11518>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-11519>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-11520>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-11521>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-11522>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-11523>`                         Make the object visible.
:ref:`showContainingPage <no-11524>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-11525>`              Display a context menu (popup) at the specified position.
:ref:`super <no-11526>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-11527>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-11528>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-11529>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-11530>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-11531>`                       
:ref:`write <no-11532>`                        write(self, String text)

============================================== ========================


Methods
=======

.. _no-11471:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.flushValue(self)



-------

.. _no-11477:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getBlankValue(self)



-------

.. _no-11531:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.update(self)



-------


Methods - inherited
=====================

.. _no-11437:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11438:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-11439:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11440:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11441:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11442:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.autoBindEvents(self, force=True)
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

.. _no-11443:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11444:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11445:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11446:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11447:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-11448:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11449:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11450:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11451:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11452:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11453:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11454:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.convertStringValueToDataType(self, strVal, dataType)
   :noindex:


   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11455:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11456:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11457:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11458:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11459:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-11460:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11461:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11462:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11463:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11464:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11465:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11466:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11467:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11468:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11469:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11470:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11472:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11473:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11474:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11475:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11476:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11478:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11479:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11480:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11481:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11482:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11483:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-11484:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11485:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11486:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11487:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.getStringValue(self, value)
   :noindex:


   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-11488:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11489:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11490:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11491:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11492:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11493:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.lockDisplay(self)
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

.. _no-11494:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11495:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11496:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11497:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11498:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11499:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11500:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11501:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11502:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11503:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11504:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11505:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11506:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11507:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11508:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11509:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11510:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11511:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-11512:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-11513:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-11514:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-11515:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11516:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-11517:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11518:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11519:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-11520:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-11521:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11522:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11523:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11524:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11525:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11526:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11527:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11528:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11529:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11530:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11532:

.. function:: dabo.ui.uiwx.dNumericBox.dNumericBox.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
