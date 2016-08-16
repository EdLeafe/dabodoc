
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.login

.. _dabo.ui.dialogs.login.Txt:

==================================
|doc_title|  **login.Txt** - class
==================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Txt**

.. inheritance-diagram:: Txt


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTextBox.dTextBox`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.dialogs.login.TxtPass`



|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.login.Txt


|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Alignment <no-9153>`                Specifies the alignment of the text. (str)
:ref:`Application <no-9154>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-9155>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-9156>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-9157>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-9158>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-9159>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-9160>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-9161>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-9162>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-9163>`                  The caption of the object. (str)
:ref:`Children <no-9164>`                 Returns a list of object references to the children of
:ref:`Class <no-9165>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-9166>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-9167>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-9168>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-9169>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-9170>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-9171>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-9172>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-9173>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-9174>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-9175>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-9176>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-9177>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-9178>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-9179>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-9180>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-9181>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-9182>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-9183>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-9184>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-9185>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-9186>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-9187>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-9188>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-9189>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-9190>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-9191>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-9192>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-9193>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-9194>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-9195>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-9196>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-9197>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-9198>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-9199>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-9200>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-9201>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-9202>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-9203>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-9204>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-9205>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-9206>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-9207>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-9208>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-9209>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-9210>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-9211>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-9212>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-9213>`                 Specifies the font face. (str)
:ref:`FontInfo <no-9214>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-9215>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-9216>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-9217>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-9218>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-9219>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-9220>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-9221>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-9222>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-9223>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-9224>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-9225>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-9226>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-9227>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-9228>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-9229>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-9230>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-9231>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-9232>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-9233>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-9234>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-9235>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-9236>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-9237>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-9238>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`Parent <no-9239>`                   The containing object. (obj)
:ref:`PasswordEntry <no-9240>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-9241>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-9242>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-9243>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-9244>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-9245>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-9246>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-9247>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-9248>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-9249>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-9250>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-9251>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-9252>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-9253>`                     The size of the object. (tuple)
:ref:`Sizer <no-9254>`                    The sizer for the object.
:ref:`Source <no-9255>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-9256>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-9257>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-9258>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-9259>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-9260>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-9261>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-9262>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-9263>`                      The top position of the object. (int)
:ref:`Transparency <no-9264>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-9265>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-9266>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-9267>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-9268>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-9269>`                    The width of the object. (int)
:ref:`WindowHandle <no-9270>`             The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties - inherited
========================

.. _no-9153:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-9154:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9155:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9156:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9157:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9158:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9159:

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

.. _no-9160:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9161:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9162:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9163:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9164:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9165:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9166:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9167:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9168:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9169:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9170:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9171:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9172:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9173:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9174:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9175:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9176:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9177:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9178:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9179:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9180:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9181:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9182:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9183:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9184:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9185:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9186:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9187:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9188:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9189:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9190:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9191:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9192:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-9193:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9194:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9195:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9196:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9197:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9198:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9199:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9200:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9201:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-9202:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9203:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9204:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9205:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9206:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-9207:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9208:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9209:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9210:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9211:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9212:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9213:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9214:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9215:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9216:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9217:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9218:

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

.. _no-9219:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9220:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9221:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9222:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9223:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9224:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9225:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9226:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9227:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9228:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9229:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9230:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9231:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9232:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9233:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9234:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9235:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9236:

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

.. _no-9237:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9238:

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

.. _no-9239:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9240:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-9241:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9242:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9243:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9244:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9245:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9246:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9247:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9248:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9249:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9250:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9251:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9252:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9253:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9254:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9255:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9256:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9257:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-9258:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-9259:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-9260:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9261:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9262:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9263:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9264:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9265:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9266:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------

.. _no-9267:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9268:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9269:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9270:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-9271>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-9272>`                 Occurs after the control or form is created.
:ref:`Destroy <no-9273>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-9274>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-9275>`               Occurs when the control gets the focus.
:ref:`Hit <no-9276>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-9277>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-9278>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-9279>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-9280>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-9281>`               
:ref:`KeyUp <no-9282>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-9283>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-9284>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-9285>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-9286>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-9287>`             
:ref:`MouseLeave <no-9288>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-9289>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-9290>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-9291>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-9292>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-9293>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-9294>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-9295>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-9296>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-9297>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-9298>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-9299>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-9300>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-9301>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-9302>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-9303>`                   Occurs when the control's position changes.
:ref:`Paint <no-9304>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-9305>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-9306>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-9307>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-9308>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-9309>`           Occurs when the control's value has changed, whether

======================================= ========================


Events
=======

.. _no-9271:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-9272:

**Create** 

Occurs after the control or form is created.



-------

.. _no-9273:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-9274:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-9275:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-9276:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-9277:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-9278:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-9279:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-9280:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-9281:

**KeyEvent** 



-------

.. _no-9282:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-9283:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-9284:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-9285:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-9286:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-9287:

**MouseEvent** 



-------

.. _no-9288:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-9289:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-9290:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-9291:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-9292:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-9293:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-9294:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-9295:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-9296:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-9297:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-9298:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-9299:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-9300:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-9301:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-9302:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-9303:

**Move** 

Occurs when the control's position changes.



-------

.. _no-9304:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-9305:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-9306:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-9307:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-9308:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-9309:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================= ========================
:ref:`absoluteCoordinates <no-9310>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-9311>`                    Instantiate object as a child of self.
:ref:`afterInit <no-9312>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-9313>`                 
:ref:`afterSetProperties <no-9314>`           
:ref:`autoBindEvents <no-9315>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-9316>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-9317>`          
:ref:`bindEvent <no-9318>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-9319>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-9320>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-9321>`                 Makes this object topmost
:ref:`charsAfterCursor <no-9322>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-9323>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-9324>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-9325>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-9326>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-9327>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-9328>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-9329>`                          Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-9330>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-9331>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-9332>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-9333>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-9334>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-9335>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-9336>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-9337>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-9338>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-9339>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-9340>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-9341>`                     Draws text on the object at the specified position
:ref:`endHover <no-9342>`                     
:ref:`fitToSizer <no-9343>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-9344>`                   
:ref:`fontZoomIn <no-9345>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-9346>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-9347>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-9348>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-9349>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-9350>`                
:ref:`getCaptureBitmap <no-9351>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-9352>`            Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-9353>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-9354>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-9355>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-9356>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-9357>`             
:ref:`getSizerProp <no-9358>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-9359>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-9360>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-9361>`                         Make the object invisible.
:ref:`initEvents <no-9362>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-9363>`               
:ref:`isContainedBy <no-9364>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-9365>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-9366>`                  Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-9367>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-9368>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-9369>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-9370>`                      
:ref:`paste <no-9371>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-9372>`                  
:ref:`processDroppedFiles <no-9373>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-9374>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-9375>`                   Raise the passed Dabo event.
:ref:`reCreate <no-9376>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-9377>`                     Recreate the object.
:ref:`redraw <no-9378>`                       Called when the object is (re)drawn.
:ref:`refresh <no-9379>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-9380>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-9381>`                      Destroys the object.
:ref:`removeDrawnObject <no-9382>`            
:ref:`restoreValue <no-9383>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-9384>`                    Save control's value to dApp's user settings table.
:ref:`select <no-9385>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-9386>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-9387>`                   Select no text in the control.
:ref:`sendToBack <no-9388>`                   Places this object behind all others.
:ref:`setAll <no-9389>`                       Set all child object properties to the passed value.
:ref:`setFocus <no-9390>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-9391>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-9392>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-9393>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-9394>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-9395>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-9396>`                         Make the object visible.
:ref:`showContainingPage <no-9397>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-9398>`              Display a context menu (popup) at the specified position.
:ref:`super <no-9399>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-9400>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-9401>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-9402>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-9403>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-9404>`                       Update control's value to match the current value from the source.
:ref:`write <no-9405>`                        write(self, String text)

============================================= ========================


Methods
=======

.. _no-9363:

.. function:: dabo.ui.dialogs.login.Txt.initProperties(self)



-------


Methods - inherited
=====================

.. _no-9310:

.. function:: dabo.ui.dialogs.login.Txt.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9311:

.. function:: dabo.ui.dialogs.login.Txt.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-9312:

.. function:: dabo.ui.dialogs.login.Txt.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9313:

.. function:: dabo.ui.dialogs.login.Txt.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9314:

.. function:: dabo.ui.dialogs.login.Txt.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9315:

.. function:: dabo.ui.dialogs.login.Txt.autoBindEvents(self, force=True)
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

.. _no-9316:

.. function:: dabo.ui.dialogs.login.Txt.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9317:

.. function:: dabo.ui.dialogs.login.Txt.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9318:

.. function:: dabo.ui.dialogs.login.Txt.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9319:

.. function:: dabo.ui.dialogs.login.Txt.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9320:

.. function:: dabo.ui.dialogs.login.Txt.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-9321:

.. function:: dabo.ui.dialogs.login.Txt.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9322:

.. function:: dabo.ui.dialogs.login.Txt.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9323:

.. function:: dabo.ui.dialogs.login.Txt.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9324:

.. function:: dabo.ui.dialogs.login.Txt.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9325:

.. function:: dabo.ui.dialogs.login.Txt.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9326:

.. function:: dabo.ui.dialogs.login.Txt.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9327:

.. function:: dabo.ui.dialogs.login.Txt.convertStringValueToDataType(self, strVal, dataType)
   :noindex:


   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-9328:

.. function:: dabo.ui.dialogs.login.Txt.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9329:

.. function:: dabo.ui.dialogs.login.Txt.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9330:

.. function:: dabo.ui.dialogs.login.Txt.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9331:

.. function:: dabo.ui.dialogs.login.Txt.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9332:

.. function:: dabo.ui.dialogs.login.Txt.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-9333:

.. function:: dabo.ui.dialogs.login.Txt.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9334:

.. function:: dabo.ui.dialogs.login.Txt.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9335:

.. function:: dabo.ui.dialogs.login.Txt.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9336:

.. function:: dabo.ui.dialogs.login.Txt.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9337:

.. function:: dabo.ui.dialogs.login.Txt.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9338:

.. function:: dabo.ui.dialogs.login.Txt.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9339:

.. function:: dabo.ui.dialogs.login.Txt.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9340:

.. function:: dabo.ui.dialogs.login.Txt.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9341:

.. function:: dabo.ui.dialogs.login.Txt.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9342:

.. function:: dabo.ui.dialogs.login.Txt.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9343:

.. function:: dabo.ui.dialogs.login.Txt.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9344:

.. function:: dabo.ui.dialogs.login.Txt.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9345:

.. function:: dabo.ui.dialogs.login.Txt.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9346:

.. function:: dabo.ui.dialogs.login.Txt.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9347:

.. function:: dabo.ui.dialogs.login.Txt.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9348:

.. function:: dabo.ui.dialogs.login.Txt.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9349:

.. function:: dabo.ui.dialogs.login.Txt.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9350:

.. function:: dabo.ui.dialogs.login.Txt.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9351:

.. function:: dabo.ui.dialogs.login.Txt.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9352:

.. function:: dabo.ui.dialogs.login.Txt.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9353:

.. function:: dabo.ui.dialogs.login.Txt.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9354:

.. function:: dabo.ui.dialogs.login.Txt.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9355:

.. function:: dabo.ui.dialogs.login.Txt.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9356:

.. function:: dabo.ui.dialogs.login.Txt.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-9357:

.. function:: dabo.ui.dialogs.login.Txt.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9358:

.. function:: dabo.ui.dialogs.login.Txt.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9359:

.. function:: dabo.ui.dialogs.login.Txt.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9360:

.. function:: dabo.ui.dialogs.login.Txt.getStringValue(self, value)
   :noindex:


   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-9361:

.. function:: dabo.ui.dialogs.login.Txt.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9362:

.. function:: dabo.ui.dialogs.login.Txt.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9364:

.. function:: dabo.ui.dialogs.login.Txt.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9365:

.. function:: dabo.ui.dialogs.login.Txt.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9366:

.. function:: dabo.ui.dialogs.login.Txt.lockDisplay(self)
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

.. _no-9367:

.. function:: dabo.ui.dialogs.login.Txt.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9368:

.. function:: dabo.ui.dialogs.login.Txt.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9369:

.. function:: dabo.ui.dialogs.login.Txt.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9370:

.. function:: dabo.ui.dialogs.login.Txt.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9371:

.. function:: dabo.ui.dialogs.login.Txt.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9372:

.. function:: dabo.ui.dialogs.login.Txt.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9373:

.. function:: dabo.ui.dialogs.login.Txt.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9374:

.. function:: dabo.ui.dialogs.login.Txt.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9375:

.. function:: dabo.ui.dialogs.login.Txt.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9376:

.. function:: dabo.ui.dialogs.login.Txt.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9377:

.. function:: dabo.ui.dialogs.login.Txt.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9378:

.. function:: dabo.ui.dialogs.login.Txt.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9379:

.. function:: dabo.ui.dialogs.login.Txt.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9380:

.. function:: dabo.ui.dialogs.login.Txt.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9381:

.. function:: dabo.ui.dialogs.login.Txt.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9382:

.. function:: dabo.ui.dialogs.login.Txt.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9383:

.. function:: dabo.ui.dialogs.login.Txt.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9384:

.. function:: dabo.ui.dialogs.login.Txt.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9385:

.. function:: dabo.ui.dialogs.login.Txt.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-9386:

.. function:: dabo.ui.dialogs.login.Txt.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-9387:

.. function:: dabo.ui.dialogs.login.Txt.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-9388:

.. function:: dabo.ui.dialogs.login.Txt.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9389:

.. function:: dabo.ui.dialogs.login.Txt.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-9390:

.. function:: dabo.ui.dialogs.login.Txt.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9391:

.. function:: dabo.ui.dialogs.login.Txt.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9392:

.. function:: dabo.ui.dialogs.login.Txt.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-9393:

.. function:: dabo.ui.dialogs.login.Txt.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-9394:

.. function:: dabo.ui.dialogs.login.Txt.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9395:

.. function:: dabo.ui.dialogs.login.Txt.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9396:

.. function:: dabo.ui.dialogs.login.Txt.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9397:

.. function:: dabo.ui.dialogs.login.Txt.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9398:

.. function:: dabo.ui.dialogs.login.Txt.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9399:

.. function:: dabo.ui.dialogs.login.Txt.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9400:

.. function:: dabo.ui.dialogs.login.Txt.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9401:

.. function:: dabo.ui.dialogs.login.Txt.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9402:

.. function:: dabo.ui.dialogs.login.Txt.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9403:

.. function:: dabo.ui.dialogs.login.Txt.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9404:

.. function:: dabo.ui.dialogs.login.Txt.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-9405:

.. function:: dabo.ui.dialogs.login.Txt.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
