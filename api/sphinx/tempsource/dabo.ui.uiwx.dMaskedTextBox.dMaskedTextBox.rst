
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMaskedTextBox

.. _dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox:

======================================================
|doc_title|  **dMaskedTextBox.dMaskedTextBox** - class
======================================================


This is a specialized textbox class that supports a Mask property. The
mask determines what characters are allowed in the textbox, and can also
include formatting characters that are not part of the control's Value.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dMaskedTextBox**

.. inheritance-diagram:: dMaskedTextBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`
* wx.lib.masked.textctrl.TextCtrl - can not provide a link



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dMaskedTextBox.png
          :scale: 75 %
          :target: _static/macWidgets/dMaskedTextBox.png
          :alt: dMaskedTextBox



     - .. image:: _static/winWidgets/dMaskedTextBox.png
          :scale: 75 %
          :target: _static/winWidgets/dMaskedTextBox.png
          :alt: dMaskedTextBox



     - .. image:: _static/nixWidgets/dMaskedTextBox.png
          :scale: 75 %
          :target: _static/nixWidgets/dMaskedTextBox.png
          :alt: dMaskedTextBox


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox

   .. automethod:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-33520>`                Specifies the alignment of the text. (str)
:ref:`Application <no-33521>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-33522>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-33523>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-33524>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-33525>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-33526>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-33527>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-33528>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-33529>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-33530>`                  The caption of the object. (str)
:ref:`Children <no-33531>`                 Returns a list of object references to the children of
:ref:`Class <no-33532>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-33533>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-33534>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-33535>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-33536>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-33537>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-33538>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-33539>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-33540>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-33541>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-33542>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-33543>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-33544>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-33545>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-33546>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-33547>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-33548>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-33549>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-33550>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-33551>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-33552>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-33553>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-33554>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-33555>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-33556>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-33557>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-33558>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-33559>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-33560>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-33561>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-33562>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-33563>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-33564>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-33565>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-33566>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-33567>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-33568>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-33569>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-33570>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-33571>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-33572>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-33573>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-33574>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-33575>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-33576>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-33577>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-33578>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-33579>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-33580>`                 Specifies the font face. (str)
:ref:`FontInfo <no-33581>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-33582>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-33583>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-33584>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-33585>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-33586>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-33587>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Format <no-33588>`                   Several pre-defined formats are available. When you set the Format
:ref:`Height <no-33589>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-33590>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-33591>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InputCodes <no-33592>`               Characters that define the type of input that the control will accept.  (str)
:ref:`InsertionPosition <no-33593>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-33594>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-33595>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-33596>`                Specifies which events to log.  (list of strings)
:ref:`Mask <no-33597>`                     Display Mask for the control.  (str)
:ref:`MaskedValue <no-33598>`              Value of the control, including mask characters, if any. (read-only) (str)
:ref:`MaximumHeight <no-33599>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-33600>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-33601>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-33602>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-33603>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-33604>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-33605>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-33606>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-33607>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-33608>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-33609>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`Parent <no-33610>`                   The containing object. (obj)
:ref:`PasswordEntry <no-33611>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-33612>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-33613>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-33614>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-33615>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-33616>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-33617>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-33618>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-33619>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-33620>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-33621>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-33622>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-33623>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-33624>`                     The size of the object. (tuple)
:ref:`Sizer <no-33625>`                    The sizer for the object.
:ref:`Source <no-33626>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-33627>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-33628>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-33629>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-33630>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-33631>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-33632>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-33633>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-33634>`                      The top position of the object. (int)
:ref:`Transparency <no-33635>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-33636>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UnmaskedValue <no-33637>`            Value of the control, removing mask characters, if any. (read-only) (str)
:ref:`Value <no-33638>`                    Specifies the content of this control. (str) If ValueMode is set to 'Masked',
:ref:`ValueMode <no-33639>`                Specifies the information that the Value property refers to. (str)
:ref:`Visible <no-33640>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-33641>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-33642>`                    The width of the object. (int)
:ref:`WindowHandle <no-33643>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-33588:

**Format** 

Several pre-defined formats are available. When you set the Format
    property, any Mask setting is ignored, and the specified Format is
    used instead. The format codes are NOT case-sensitive.  (str)

    Formats are available in several categories:
        Date (US and European)
        DateTime (US and European)
        Time
        Email
        IP Address
        SSN (US)
        Zip Code (US)
        Phone (US)
        



-------

.. _no-33592:

**InputCodes** 

Characters that define the type of input that the control will accept.  (str)

    These are the available input codes and their meaning:

    +-----------+---------------------------------------------------------------+
    |Character  |Meaning                                                        |
    +===========+===============================================================+
    |   #       |Allow numeric only (0-9)                                       |
    +-----------+---------------------------------------------------------------+
    |   _       |Allow spaces                                                   |
    +-----------+---------------------------------------------------------------+
    |   !       |Force upper                                                    |
    +-----------+---------------------------------------------------------------+
    |   ^       |Force lower                                                    |
    +-----------+---------------------------------------------------------------+
    |   R       |Right-align field(s)                                           |
    +-----------+---------------------------------------------------------------+
    |   r       |Right-insert in field(s) (implies R)                           |
    +-----------+---------------------------------------------------------------+
    |   <       |Stay in field until explicit navigation out of it              |
    +-----------+---------------------------------------------------------------+
    |   >       |Allow insert/delete within partially filled fields (as         |
    |           |opposed to the default "overwrite" mode for fixed-width        |
    |           |masked edit controls.)  This allows single-field controls      |
    |           |or each field within a multi-field control to optionally       |
    |           |behave more like standard text controls.                       |
    |           |(See EMAIL or phone number autoformat examples.)               |
    |           |                                                               |
    |           |Note: This also governs whether backspace/delete operations    |
    |           |shift contents of field to right of cursor, or just blank the  |
    |           |erased section.                                                |
    |           |                                                               |
    |           |Also, when combined with 'r', this indicates that the field    |
    |           |or control allows right insert anywhere within the current     |
    |           |non-empty value in the field.(Otherwise right-insert behavior  |
    |           |is only performed to when the entire right-insertable field    |
    |           |is selected or the cursor is at the right edge of the field.   |
    +-----------+---------------------------------------------------------------+
    |   ,       |Allow grouping character in integer fields of numeric controls |
    |           |and auto-group/regroup digits (if the result fits) when leaving|
    |           |such a field.  (If specified, .SetValue() will attempt to      |
    |           |auto-group as well.)                                           |
    |           |',' is also the default grouping character.  To change the     |
    |           |grouping character and/or decimal character, use the groupChar |
    |           |and decimalChar parameters, respectively.                      |
    |           |                                                               |
    |           |Note: typing the "decimal point" character in such fields will |
    |           |clip the value to that left of the cursor for integer          |
    |           |fields of controls with "integer" or "floating point" masks.   |
    |           |If the ',' format code is specified, this will also cause the  |
    |           |resulting digits to be regrouped properly, using the current   |
    |           |grouping character.                                            |
    +-----------+---------------------------------------------------------------+
    |   -       |Prepend and reserve leading space for sign to mask and allow   |
    |           |signed values (negative #s shown in red by default.) Can be    |
    |           |used with argument useParensForNegatives (see below.)          |
    +-----------+---------------------------------------------------------------+
    |   0       |integer fields get leading zeros                               |
    +-----------+---------------------------------------------------------------+
    |   D       |Date[/time] field                                              |
    +-----------+---------------------------------------------------------------+
    |   T       |Time field                                                     |
    +-----------+---------------------------------------------------------------+
    |   F       |Auto-Fit: the control calulates its size from                  |
    |           |the length of the template mask                                |
    +-----------+---------------------------------------------------------------+
    |   V       |validate entered chars against validRegex before allowing them |
    |           |to be entered vs. being allowed by basic mask and then having  |
    |           |the resulting value just colored as invalid.                   |
    |           |(See USSTATE autoformat demo for how this can be used.)        |
    +-----------+---------------------------------------------------------------+
    |   S       |select entire field when navigating to new field               |
    +-----------+---------------------------------------------------------------+


    



-------

.. _no-33597:

**Mask** 

Display Mask for the control.  (str)

    These are the allowed mask characters and their function:

    +-----------+-------------------------------------------------------------------+
    |Character  |Function                                                           +
    +===========+===================================================================+
    |   #       |Allow numeric only (0-9)                                           |
    +-----------+-------------------------------------------------------------------+
    |   N       |Allow letters and numbers (0-9)                                    |
    +-----------+-------------------------------------------------------------------+
    |   A       |Allow uppercase letters only                                       |
    +-----------+-------------------------------------------------------------------+
    |   a       |Allow lowercase letters only                                       |
    +-----------+-------------------------------------------------------------------+
    |   C       |Allow any letter, upper or lower                                   |
    +-----------+-------------------------------------------------------------------+
    |   X       |Allow string.letters, string.punctuation, string.digits            |
    +-----------+-------------------------------------------------------------------+
    |   &       |Allow string.punctuation only (doesn't include all unicode symbols)|
    +-----------+-------------------------------------------------------------------+
    |   \*      |Allow any visible character                                        |
    +-----------+-------------------------------------------------------------------+
    |   |       |explicit field boundary (takes no space in the control; allows mix |
    |           |of adjacent mask characters to be treated as separate fields,      |
    |           |eg: '&|###' means "field 0 = '&', field 1 = '###'", but there's    |
    |           |no fixed characters in between.                                    |
    +-----------+-------------------------------------------------------------------+

    Repetitions of the same mask code can be represented by placing the number
    of repetitions in curly braces after the code. E.g.: CCCCCCCC = C{6} 



-------

.. _no-33598:

**MaskedValue** 

Value of the control, including mask characters, if any. (read-only) (str)



-------

.. _no-33637:

**UnmaskedValue** 

Value of the control, removing mask characters, if any. (read-only) (str)



-------

.. _no-33639:

**ValueMode** 

Specifies the information that the Value property refers to. (str)
    If it is set to 'Masked' (or anything that begins with the letter 'm'), the
    Value property will return the contents of the control, including any mask
    characters. If this is set to anything other than a string that begins with 'm',
    Value will return the control's contents without the mask characters.
    NOTE: This only affects the results of \*reading\* the Value property. Setting
    Value is not affected in any way.



-------


Properties - inherited
========================

.. _no-33520:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-33521:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33522:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33523:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33524:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33525:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33526:

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

.. _no-33527:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33528:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33529:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33530:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33531:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33532:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33533:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33534:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33535:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33536:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33537:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33538:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33539:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33540:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33541:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33542:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33543:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33544:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33545:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33546:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33547:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33548:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33549:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33550:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33551:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33552:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33553:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33554:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33555:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33556:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33557:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33558:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33559:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-33560:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33561:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33562:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33563:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33564:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33565:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33566:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33567:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33568:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-33569:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33570:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33571:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33572:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33573:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-33574:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33575:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33576:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33577:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33578:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33579:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33580:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33581:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33582:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33583:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33584:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33585:

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

.. _no-33586:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33587:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33589:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33590:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33591:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33593:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33594:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33595:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33596:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33599:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33600:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33601:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33602:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33603:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33604:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33605:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33606:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33607:

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

.. _no-33608:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33609:

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

.. _no-33610:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33611:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-33612:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33613:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33614:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33615:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33616:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33617:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33618:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33619:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33620:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33621:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33622:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33623:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33624:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33625:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33626:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33627:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33628:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-33629:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-33630:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-33631:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33632:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33633:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33634:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33635:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33636:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33638:

**Value** 

Specifies the content of this control. (str) If ValueMode is set to 'Masked',
    this will include the mask characters. Otherwise it will be the contents without
    any mask characters.


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------

.. _no-33640:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33641:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33642:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33643:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-33644>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-33645>`                 Occurs after the control or form is created.
:ref:`Destroy <no-33646>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-33647>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-33648>`               Occurs when the control gets the focus.
:ref:`Idle <no-33649>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-33650>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-33651>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-33652>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-33653>`               
:ref:`KeyUp <no-33654>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-33655>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-33656>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-33657>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-33658>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-33659>`             
:ref:`MouseLeave <no-33660>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-33661>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-33662>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-33663>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-33664>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-33665>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-33666>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-33667>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-33668>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-33669>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-33670>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-33671>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-33672>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-33673>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-33674>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-33675>`                   Occurs when the control's position changes.
:ref:`Paint <no-33676>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-33677>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-33678>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-33679>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-33680>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-33681>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-33644:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-33645:

**Create** 

Occurs after the control or form is created.



-------

.. _no-33646:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-33647:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-33648:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-33649:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-33650:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-33651:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-33652:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-33653:

**KeyEvent** 



-------

.. _no-33654:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-33655:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-33656:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-33657:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-33658:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-33659:

**MouseEvent** 



-------

.. _no-33660:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-33661:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-33662:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-33663:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-33664:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-33665:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-33666:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-33667:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-33668:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-33669:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-33670:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-33671:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-33672:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-33673:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-33674:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-33675:

**Move** 

Occurs when the control's position changes.



-------

.. _no-33676:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-33677:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-33678:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-33679:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-33680:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-33681:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================== ========================
:ref:`absoluteCoordinates <no-33682>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-33683>`                    Instantiate object as a child of self.
:ref:`afterInit <no-33684>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-33685>`                 
:ref:`afterSetProperties <no-33686>`           
:ref:`autoBindEvents <no-33687>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-33688>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-33689>`          
:ref:`bindEvent <no-33690>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-33691>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-33692>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-33693>`                 Makes this object topmost
:ref:`charsAfterCursor <no-33694>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-33695>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-33696>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-33697>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-33698>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-33699>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-33700>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-33701>`                          Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-33702>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-33703>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-33704>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-33705>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-33706>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-33707>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-33708>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-33709>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-33710>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-33711>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-33712>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-33713>`                     Draws text on the object at the specified position
:ref:`endHover <no-33714>`                     
:ref:`fitToSizer <no-33715>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-33716>`                   
:ref:`fontZoomIn <no-33717>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-33718>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-33719>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-33720>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-33721>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-33722>`                
:ref:`getCaptureBitmap <no-33723>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-33724>`            Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-33725>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-33726>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-33727>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-33728>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-33729>`             
:ref:`getSizerProp <no-33730>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-33731>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-33732>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-33733>`                         Make the object invisible.
:ref:`initEvents <no-33734>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-33735>`               Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-33736>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-33737>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-33738>`                  Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-33739>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-33740>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-33741>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-33742>`                      
:ref:`paste <no-33743>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-33744>`                  
:ref:`processDroppedFiles <no-33745>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-33746>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-33747>`                   Raise the passed Dabo event.
:ref:`reCreate <no-33748>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-33749>`                     Recreate the object.
:ref:`redraw <no-33750>`                       Called when the object is (re)drawn.
:ref:`refresh <no-33751>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-33752>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-33753>`                      Destroys the object.
:ref:`removeDrawnObject <no-33754>`            
:ref:`restoreValue <no-33755>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-33756>`                    Save control's value to dApp's user settings table.
:ref:`select <no-33757>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-33758>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-33759>`                   Select no text in the control.
:ref:`sendToBack <no-33760>`                   Places this object behind all others.
:ref:`setAll <no-33761>`                       Set all child object properties to the passed value.
:ref:`setFocus <no-33762>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-33763>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-33764>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-33765>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-33766>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-33767>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-33768>`                         Make the object visible.
:ref:`showContainingPage <no-33769>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-33770>`              Display a context menu (popup) at the specified position.
:ref:`super <no-33771>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-33772>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-33773>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-33774>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-33775>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-33776>`                       Update control's value to match the current value from the source.
:ref:`write <no-33777>`                        write(self, String text)

============================================== ========================


Methods - inherited
=====================

.. _no-33682:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33683:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-33684:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33685:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33686:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33687:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.autoBindEvents(self, force=True)
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

.. _no-33688:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33689:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33690:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33691:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33692:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-33693:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33694:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33695:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33696:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33697:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33698:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33699:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.convertStringValueToDataType(self, strVal, dataType)
   :noindex:


   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-33700:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33701:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33702:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33703:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33704:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-33705:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33706:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33707:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33708:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33709:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33710:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33711:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33712:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33713:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33714:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33715:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33716:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33717:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33718:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33719:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33720:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33721:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33722:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33723:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33724:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33725:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33726:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33727:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33728:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-33729:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33730:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33731:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33732:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.getStringValue(self, value)
   :noindex:


   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-33733:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33734:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33735:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33736:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33737:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33738:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.lockDisplay(self)
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

.. _no-33739:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33740:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33741:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33742:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33743:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33744:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33745:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33746:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33747:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33748:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33749:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33750:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33751:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33752:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33753:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33754:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33755:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33756:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33757:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-33758:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-33759:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-33760:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33761:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-33762:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33763:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33764:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-33765:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-33766:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33767:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33768:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33769:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33770:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33771:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33772:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33773:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33774:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33775:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33776:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-33777:

.. function:: dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
