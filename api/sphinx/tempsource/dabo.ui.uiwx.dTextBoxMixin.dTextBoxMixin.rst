
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dTextBoxMixin

.. _dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin:

====================================================
|doc_title|  **dTextBoxMixin.dTextBoxMixin** - class
====================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dTextBoxMixin**

.. inheritance-diagram:: dTextBoxMixin


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dEditBox.dEditBox`
* :ref:`dabo.ui.uiwx.dMaskedTextBox.dMaskedTextBox`
* :ref:`dabo.ui.uiwx.dNumericBox.dNumericBox`
* :ref:`dabo.ui.uiwx.dSearchBox.dSearchBox`
* :ref:`dabo.ui.uiwx.dTextBox.dTextBox`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin

   .. automethod:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-30787>`                Specifies the alignment of the text. (str)
:ref:`Application <no-30788>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-30789>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-30790>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-30791>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-30792>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-30793>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-30794>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-30795>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-30796>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-30797>`                  The caption of the object. (str)
:ref:`Children <no-30798>`                 Returns a list of object references to the children of
:ref:`Class <no-30799>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-30800>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-30801>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-30802>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-30803>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-30804>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-30805>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-30806>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-30807>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-30808>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-30809>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-30810>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-30811>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-30812>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-30813>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-30814>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-30815>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-30816>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-30817>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-30818>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-30819>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-30820>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-30821>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-30822>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-30823>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-30824>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-30825>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-30826>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-30827>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-30828>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-30829>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-30830>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-30831>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-30832>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-30833>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-30834>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-30835>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-30836>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-30837>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-30838>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-30839>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-30840>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-30841>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-30842>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-30843>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-30844>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-30845>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-30846>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-30847>`                 Specifies the font face. (str)
:ref:`FontInfo <no-30848>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-30849>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-30850>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-30851>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-30852>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-30853>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-30854>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-30855>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-30856>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-30857>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-30858>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-30859>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-30860>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-30861>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-30862>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-30863>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-30864>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-30865>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-30866>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-30867>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-30868>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-30869>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-30870>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-30871>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-30872>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`Parent <no-30873>`                   The containing object. (obj)
:ref:`PasswordEntry <no-30874>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-30875>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-30876>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-30877>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-30878>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-30879>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-30880>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-30881>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-30882>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-30883>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-30884>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-30885>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-30886>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-30887>`                     The size of the object. (tuple)
:ref:`Sizer <no-30888>`                    The sizer for the object.
:ref:`Source <no-30889>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-30890>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-30891>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-30892>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-30893>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-30894>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-30895>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-30896>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-30897>`                      The top position of the object. (int)
:ref:`Transparency <no-30898>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-30899>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-30900>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-30901>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-30902>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-30903>`                    The width of the object. (int)
:ref:`WindowHandle <no-30904>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-30826:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.



-------

.. _no-30835:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.



-------

.. _no-30872:

**NumericBlankToZero** 

Specifies whether a blank textbox gets interpreted as 0.

    When True, if the user clears the textbox value, such as by selecting all
    and pressing the space bar or delete, the value will become 0 when the
    control loses focus.

    When False, the value will revert back to the last numeric value when the
    control loses focus.

    The default comes from dabo.dTextBox_NumericBlankToZero, which defaults to
    False.



-------

.. _no-30874:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)



-------

.. _no-30891:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.



-------

.. _no-30892:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)



-------


Properties - inherited
========================

.. _no-30787:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30788:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30789:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30790:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30791:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30792:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30793:

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

.. _no-30794:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30795:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30796:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30797:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30798:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30799:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30800:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30801:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30802:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30803:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30804:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30805:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30806:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30807:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30808:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30809:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30810:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30811:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30812:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30813:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30814:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30815:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30816:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30817:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30818:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30819:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30820:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30821:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30822:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30823:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30824:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30825:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30827:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30828:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30829:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30830:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30831:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30832:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30833:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30834:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30836:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30837:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30838:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30839:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30840:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-30841:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30842:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30843:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30844:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30845:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30846:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30847:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30848:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30849:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30850:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30851:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30852:

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

.. _no-30853:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30854:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30855:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30856:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30857:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30858:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30859:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30860:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30861:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30862:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30863:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30864:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30865:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30866:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30867:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30868:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30869:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30870:

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

.. _no-30871:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30873:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30875:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30876:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30877:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30878:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30879:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30880:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30881:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30882:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30883:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30884:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30885:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30886:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30887:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30888:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30889:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30890:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30893:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-30894:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30895:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30896:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30897:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30898:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30899:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30900:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30901:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30902:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30903:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30904:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-30905>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-30906>`                 Occurs after the control or form is created.
:ref:`Destroy <no-30907>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-30908>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-30909>`               Occurs when the control gets the focus.
:ref:`Idle <no-30910>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-30911>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-30912>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-30913>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-30914>`               
:ref:`KeyUp <no-30915>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-30916>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-30917>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-30918>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-30919>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-30920>`             
:ref:`MouseLeave <no-30921>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-30922>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-30923>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-30924>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-30925>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-30926>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-30927>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-30928>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-30929>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-30930>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-30931>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-30932>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-30933>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-30934>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-30935>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-30936>`                   Occurs when the control's position changes.
:ref:`Paint <no-30937>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-30938>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-30939>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-30940>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-30941>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-30942>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-30905:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-30906:

**Create** 

Occurs after the control or form is created.



-------

.. _no-30907:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-30908:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-30909:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-30910:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-30911:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-30912:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-30913:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-30914:

**KeyEvent** 



-------

.. _no-30915:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-30916:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-30917:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-30918:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-30919:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-30920:

**MouseEvent** 



-------

.. _no-30921:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-30922:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-30923:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-30924:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-30925:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-30926:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-30927:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-30928:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-30929:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-30930:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-30931:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-30932:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-30933:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-30934:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-30935:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-30936:

**Move** 

Occurs when the control's position changes.



-------

.. _no-30937:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-30938:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-30939:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-30940:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-30941:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-30942:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================== ========================
:ref:`absoluteCoordinates <no-30943>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-30944>`                    Instantiate object as a child of self.
:ref:`afterInit <no-30945>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-30946>`                 
:ref:`afterSetProperties <no-30947>`           
:ref:`autoBindEvents <no-30948>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-30949>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-30950>`          
:ref:`bindEvent <no-30951>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-30952>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-30953>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-30954>`                 Makes this object topmost
:ref:`charsAfterCursor <no-30955>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-30956>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-30957>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-30958>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-30959>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-30960>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-30961>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-30962>`                          Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-30963>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-30964>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-30965>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-30966>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-30967>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-30968>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-30969>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-30970>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-30971>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-30972>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-30973>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-30974>`                     Draws text on the object at the specified position
:ref:`endHover <no-30975>`                     
:ref:`fitToSizer <no-30976>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-30977>`                   
:ref:`fontZoomIn <no-30978>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-30979>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-30980>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-30981>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-30982>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-30983>`                
:ref:`getCaptureBitmap <no-30984>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-30985>`            Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-30986>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-30987>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-30988>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-30989>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-30990>`             
:ref:`getSizerProp <no-30991>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-30992>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-30993>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-30994>`                         Make the object invisible.
:ref:`initEvents <no-30995>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-30996>`               Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-30997>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-30998>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-30999>`                  Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-31000>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-31001>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-31002>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-31003>`                      
:ref:`paste <no-31004>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-31005>`                  
:ref:`processDroppedFiles <no-31006>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-31007>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-31008>`                   Raise the passed Dabo event.
:ref:`reCreate <no-31009>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-31010>`                     Recreate the object.
:ref:`redraw <no-31011>`                       Called when the object is (re)drawn.
:ref:`refresh <no-31012>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-31013>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-31014>`                      Destroys the object.
:ref:`removeDrawnObject <no-31015>`            
:ref:`restoreValue <no-31016>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-31017>`                    Save control's value to dApp's user settings table.
:ref:`select <no-31018>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-31019>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-31020>`                   Select no text in the control.
:ref:`sendToBack <no-31021>`                   Places this object behind all others.
:ref:`setAll <no-31022>`                       Set all child object properties to the passed value.
:ref:`setFocus <no-31023>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-31024>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-31025>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-31026>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-31027>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-31028>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-31029>`                         Make the object visible.
:ref:`showContainingPage <no-31030>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-31031>`              Display a context menu (popup) at the specified position.
:ref:`super <no-31032>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-31033>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-31034>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-31035>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-31036>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-31037>`                       Update control's value to match the current value from the source.

============================================== ========================


Methods
=======

.. _no-30960:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.convertStringValueToDataType(self, strVal, dataType)

   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   



-------

.. _no-30993:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getStringValue(self, value)

   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   



-------


Methods - inherited
=====================

.. _no-30943:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30944:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-30945:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30946:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30947:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30948:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.autoBindEvents(self, force=True)
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

.. _no-30949:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30950:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30951:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30952:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30953:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-30954:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30955:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30956:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30957:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30958:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30959:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30961:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30962:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30963:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30964:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30965:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-30966:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30967:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30968:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30969:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30970:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30971:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30972:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30973:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30974:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30975:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30976:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30977:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30978:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30979:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30980:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30981:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30982:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30983:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-30984:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30985:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30986:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30987:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30988:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30989:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-30990:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-30991:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30992:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30994:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30995:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30996:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30997:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30998:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30999:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.lockDisplay(self)
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

.. _no-31000:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31001:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31002:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31003:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31004:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31005:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31006:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31007:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31008:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31009:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31010:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31011:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31012:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31013:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31014:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31015:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31016:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31017:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31018:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31019:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-31020:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31021:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31022:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-31023:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31024:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31025:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-31026:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-31027:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31028:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31029:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31030:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31031:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31032:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31033:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31034:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31035:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31036:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31037:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
