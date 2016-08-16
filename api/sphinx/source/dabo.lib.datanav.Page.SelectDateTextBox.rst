
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.SelectDateTextBox:

===============================================
|doc_title|  **Page.SelectDateTextBox** - class
===============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SelectDateTextBox**

.. inheritance-diagram:: SelectDateTextBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.datanav.Page.SelectControlMixin`
* :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.SelectDateTextBox


|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Alignment <no-3442>`                Specifies the alignment of the text. (str)
:ref:`Application <no-3443>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-3444>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-3445>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-3446>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-3447>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-3448>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-3449>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-3450>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-3451>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-3452>`                  The caption of the object. (str)
:ref:`Children <no-3453>`                 Returns a list of object references to the children of
:ref:`Class <no-3454>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-3455>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-3456>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-3457>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-3458>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-3459>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-3460>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-3461>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-3462>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-3463>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-3464>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-3465>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-3466>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-3467>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-3468>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-3469>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-3470>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-3471>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-3472>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-3473>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-3474>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-3475>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-3476>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-3477>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-3478>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-3479>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-3480>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-3481>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-3482>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-3483>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-3484>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-3485>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-3486>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-3487>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-3488>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-3489>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-3490>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-3491>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-3492>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-3493>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-3494>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-3495>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-3496>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-3497>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-3498>`                  Specifies whether the object and children can get user input. (bool)
:ref:`ExtendedCalendar <no-3499>`         When True, the calendar is displayed in a larger format with more controls
:ref:`Font <no-3500>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-3501>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-3502>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-3503>`                 Specifies the font face. (str)
:ref:`FontInfo <no-3504>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-3505>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-3506>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-3507>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-3508>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-3509>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-3510>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-3511>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-3512>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-3513>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-3514>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-3515>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-3516>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-3517>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-3518>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-3519>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-3520>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-3521>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-3522>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-3523>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-3524>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-3525>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-3526>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-3527>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-3528>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`Parent <no-3529>`                   The containing object. (obj)
:ref:`PasswordEntry <no-3530>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-3531>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-3532>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-3533>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-3534>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-3535>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-3536>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-3537>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-3538>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-3539>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-3540>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-3541>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-3542>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-3543>`                     The size of the object. (tuple)
:ref:`Sizer <no-3544>`                    The sizer for the object.
:ref:`Source <no-3545>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-3546>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-3547>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-3548>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-3549>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-3550>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-3551>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-3552>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-3553>`                      The top position of the object. (int)
:ref:`Transparency <no-3554>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-3555>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-3556>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-3557>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-3558>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-3559>`                    The width of the object. (int)
:ref:`WindowHandle <no-3560>`             The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties - inherited
========================

.. _no-3442:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-3443:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3444:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3445:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3446:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3447:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3448:

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

.. _no-3449:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3450:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3451:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3452:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3453:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3454:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3455:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3456:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3457:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3458:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3459:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3460:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3461:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3462:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3463:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3464:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3465:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3466:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3467:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3468:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3469:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3470:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3471:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3472:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3473:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3474:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3475:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3476:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3477:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3478:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3479:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3480:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3481:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-3482:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3483:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3484:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3485:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3486:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3487:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3488:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3489:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3490:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-3491:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3492:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3493:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3494:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3495:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-3496:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3497:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3498:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3499:

**ExtendedCalendar** 

When True, the calendar is displayed in a larger format with more controls
    for quickly moving to any date. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3500:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3501:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3502:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3503:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3504:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3505:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3506:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3507:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3508:

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

.. _no-3509:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3510:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3511:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3512:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3513:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3514:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3515:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3516:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3517:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3518:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3519:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3520:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3521:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3522:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3523:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3524:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3525:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3526:

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

.. _no-3527:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3528:

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

.. _no-3529:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3530:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-3531:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3532:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3533:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3534:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3535:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3536:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3537:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3538:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3539:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3540:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3541:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3542:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3543:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3544:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3545:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3546:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3547:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-3548:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-3549:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-3550:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3551:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3552:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3553:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3554:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3555:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3556:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------

.. _no-3557:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3558:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3559:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3560:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-3561>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-3562>`                 Occurs after the control or form is created.
:ref:`Destroy <no-3563>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-3564>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-3565>`               Occurs when the control gets the focus.
:ref:`Hit <no-3566>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-3567>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-3568>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-3569>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-3570>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-3571>`               
:ref:`KeyUp <no-3572>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-3573>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-3574>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-3575>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-3576>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-3577>`             
:ref:`MouseLeave <no-3578>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-3579>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-3580>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-3581>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-3582>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-3583>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-3584>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-3585>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-3586>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-3587>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-3588>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-3589>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-3590>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-3591>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-3592>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-3593>`                   Occurs when the control's position changes.
:ref:`Paint <no-3594>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-3595>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-3596>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-3597>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-3598>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-3599>`           Occurs when the control's value has changed, whether

======================================= ========================


Events
=======

.. _no-3561:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-3562:

**Create** 

Occurs after the control or form is created.



-------

.. _no-3563:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-3564:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-3565:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-3566:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-3567:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-3568:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-3569:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-3570:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-3571:

**KeyEvent** 



-------

.. _no-3572:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-3573:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-3574:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-3575:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-3576:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-3577:

**MouseEvent** 



-------

.. _no-3578:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-3579:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-3580:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-3581:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-3582:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-3583:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-3584:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-3585:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-3586:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-3587:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-3588:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-3589:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-3590:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-3591:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-3592:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-3593:

**Move** 

Occurs when the control's position changes.



-------

.. _no-3594:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-3595:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-3596:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-3597:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-3598:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-3599:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================= ========================
:ref:`absoluteCoordinates <no-3600>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-3601>`                    Instantiate object as a child of self.
:ref:`adjustDate <no-3602>`                   Modifies the current date value if the key is one of the
:ref:`afterInit <no-3603>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-3604>`                 
:ref:`afterSetProperties <no-3605>`           
:ref:`autoBindEvents <no-3606>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-3607>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-3608>`          
:ref:`bindEvent <no-3609>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-3610>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-3611>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-3612>`                 Makes this object topmost
:ref:`charsAfterCursor <no-3613>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-3614>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-3615>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-3616>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-3617>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-3618>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-3619>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-3620>`                          Called by uiApp when the user requests a cut operation.
:ref:`dayInterval <no-3621>`                  Adjusts the date by the given number of days; negative
:ref:`drawArc <no-3622>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-3623>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-3624>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-3625>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-3626>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-3627>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-3628>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-3629>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-3630>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-3631>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-3632>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-3633>`                     Draws text on the object at the specified position
:ref:`endHover <no-3634>`                     
:ref:`fitToSizer <no-3635>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-3636>`                   
:ref:`fontZoomIn <no-3637>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-3638>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-3639>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-3640>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-3641>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-3642>`                
:ref:`getCaptureBitmap <no-3643>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-3644>`            Return the dPage or WizardPage that contains self.
:ref:`getDateTuple <no-3645>`                 
:ref:`getDisplayLocker <no-3646>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-3647>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-3648>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-3649>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-3650>`             
:ref:`getSizerProp <no-3651>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-3652>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-3653>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-3654>`                         Make the object invisible.
:ref:`hourInterval <no-3655>`                 Adjusts the date by the given number of hours; negative
:ref:`initEvents <no-3656>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-3657>`               
:ref:`isContainedBy <no-3658>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-3659>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-3660>`                  Locks the visual updates to the control.
:ref:`minuteInterval <no-3661>`               Adjusts the date by the given number of minutes; negative
:ref:`monthInterval <no-3662>`                Adjusts the date by the given number of months; negative
:ref:`moveTabOrderAfter <no-3663>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-3664>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-3665>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-3666>`                      
:ref:`paste <no-3667>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-3668>`                  
:ref:`processDroppedFiles <no-3669>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-3670>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-3671>`                   Raise the passed Dabo event.
:ref:`reCreate <no-3672>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-3673>`                     Recreate the object.
:ref:`redraw <no-3674>`                       Called when the object is (re)drawn.
:ref:`refresh <no-3675>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-3676>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-3677>`                      Destroys the object.
:ref:`removeDrawnObject <no-3678>`            
:ref:`restoreValue <no-3679>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-3680>`                    Save control's value to dApp's user settings table.
:ref:`secondInterval <no-3681>`               Adjusts the date by the given number of seconds; negative
:ref:`select <no-3682>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-3683>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-3684>`                   Select no text in the control.
:ref:`sendToBack <no-3685>`                   Places this object behind all others.
:ref:`setAll <no-3686>`                       Set all child object properties to the passed value.
:ref:`setDate <no-3687>`                      Sets the Value to the passed date if this is holding a date value, or
:ref:`setFocus <no-3688>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-3689>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-3690>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-3691>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-3692>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-3693>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`setToLastMonthDay <no-3694>`            
:ref:`show <no-3695>`                         Make the object visible.
:ref:`showCalendar <no-3696>`                 
:ref:`showContainingPage <no-3697>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-3698>`              Display a context menu (popup) at the specified position.
:ref:`super <no-3699>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-3700>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-3701>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-3702>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-3703>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-3704>`                       Update control's value to match the current value from the source.
:ref:`write <no-3705>`                        write(self, String text)

============================================= ========================


Methods - inherited
=====================

.. _no-3600:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3601:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-3602:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.adjustDate(self, key, ctrl=False, shift=False)
   :noindex:


   
   Modifies the current date value if the key is one of the
   shortcut keys.
   


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3603:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3604:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3605:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3606:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.autoBindEvents(self, force=True)
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

.. _no-3607:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3608:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3609:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3610:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3611:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-3612:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3613:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3614:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3615:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3616:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3617:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3618:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.convertStringValueToDataType(self, strVal, dataType)
   :noindex:


   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-3619:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3620:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3621:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.dayInterval(self, days)
   :noindex:


   
   Adjusts the date by the given number of days; negative
   values move backwards.
   


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3622:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3623:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3624:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-3625:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3626:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3627:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3628:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3629:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3630:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3631:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3632:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3633:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3634:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3635:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3636:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3637:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3638:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3639:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3640:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3641:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3642:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3643:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3644:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3645:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getDateTuple(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3646:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3647:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3648:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3649:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-3650:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3651:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3652:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3653:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.getStringValue(self, value)
   :noindex:


   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-3654:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3655:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.hourInterval(self, hours)
   :noindex:


   
   Adjusts the date by the given number of hours; negative
   values move backwards.
   


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3656:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3657:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.initProperties(self)
   :noindex:



Inherited from: :ref:`dabo.lib.datanav.Page.SelectControlMixin`

-------

.. _no-3658:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3659:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3660:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.lockDisplay(self)
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

.. _no-3661:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.minuteInterval(self, minutes)
   :noindex:


   
   Adjusts the date by the given number of minutes; negative
   values move backwards.
   


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3662:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.monthInterval(self, months)
   :noindex:


   
   Adjusts the date by the given number of months; negative
   values move backwards.
   


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3663:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3664:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3665:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3666:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3667:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3668:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3669:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3670:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3671:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3672:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3673:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3674:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3675:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3676:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3677:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3678:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3679:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3680:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3681:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.secondInterval(self, seconds)
   :noindex:


   
   Adjusts the date by the given number of seconds; negative
   values move backwards.
   


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3682:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-3683:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-3684:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-3685:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3686:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-3687:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setDate(self, dt)
   :noindex:


   
   Sets the Value to the passed date if this is holding a date value, or
   sets the date portion of the Value if it is a datetime.
   


Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3688:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3689:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3690:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-3691:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-3692:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3693:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3694:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.setToLastMonthDay(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3695:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3696:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.showCalendar(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`

-------

.. _no-3697:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3698:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3699:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3700:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3701:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3702:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3703:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3704:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3705:

.. function:: dabo.lib.datanav.Page.SelectDateTextBox.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
