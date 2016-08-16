
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dTextBox

.. _dabo.ui.uiwx.dTextBox.dTextBox:

==========================================
|doc_title|  **dTextBox.dTextBox** - class
==========================================

Creates a text box for editing one line of string data.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dTextBox**

.. inheritance-diagram:: dTextBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Page.SelectTextBox`
* :ref:`dabo.ui.dialogs.login.Txt`
* :ref:`dabo.ui.uiwx.dDateTextBox.dDateTextBox`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dTextBox.png
          :scale: 75 %
          :target: _static/macWidgets/dTextBox.png
          :alt: dTextBox



     - .. image:: _static/winWidgets/dTextBox.png
          :scale: 75 %
          :target: _static/winWidgets/dTextBox.png
          :alt: dTextBox



     - .. image:: _static/nixWidgets/dTextBox.png
          :scale: 75 %
          :target: _static/nixWidgets/dTextBox.png
          :alt: dTextBox


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dTextBox.dTextBox

   .. automethod:: dabo.ui.uiwx.dTextBox.dTextBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-22109>`                Specifies the alignment of the text. (str)
:ref:`Application <no-22110>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-22111>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-22112>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-22113>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-22114>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-22115>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-22116>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-22117>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-22118>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-22119>`                  The caption of the object. (str)
:ref:`Children <no-22120>`                 Returns a list of object references to the children of
:ref:`Class <no-22121>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-22122>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-22123>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-22124>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-22125>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-22126>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-22127>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-22128>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-22129>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-22130>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-22131>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-22132>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-22133>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-22134>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-22135>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-22136>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-22137>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-22138>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-22139>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-22140>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-22141>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-22142>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-22143>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-22144>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-22145>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-22146>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-22147>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-22148>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-22149>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-22150>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-22151>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-22152>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-22153>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-22154>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-22155>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-22156>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-22157>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-22158>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-22159>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-22160>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-22161>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-22162>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-22163>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-22164>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-22165>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-22166>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-22167>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-22168>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-22169>`                 Specifies the font face. (str)
:ref:`FontInfo <no-22170>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-22171>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-22172>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-22173>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-22174>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-22175>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-22176>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-22177>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-22178>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-22179>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-22180>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-22181>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-22182>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-22183>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-22184>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-22185>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-22186>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-22187>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-22188>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-22189>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-22190>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-22191>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-22192>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-22193>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-22194>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`Parent <no-22195>`                   The containing object. (obj)
:ref:`PasswordEntry <no-22196>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-22197>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-22198>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-22199>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-22200>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-22201>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-22202>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-22203>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-22204>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-22205>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-22206>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-22207>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-22208>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-22209>`                     The size of the object. (tuple)
:ref:`Sizer <no-22210>`                    The sizer for the object.
:ref:`Source <no-22211>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-22212>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-22213>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-22214>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-22215>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-22216>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-22217>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-22218>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-22219>`                      The top position of the object. (int)
:ref:`Transparency <no-22220>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-22221>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-22222>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-22223>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-22224>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-22225>`                    The width of the object. (int)
:ref:`WindowHandle <no-22226>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties - inherited
========================

.. _no-22109:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-22110:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22111:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22112:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22113:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22114:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22115:

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

.. _no-22116:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22117:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22118:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22119:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22120:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22121:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22122:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22123:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22124:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22125:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22126:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22127:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22128:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22129:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22130:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22131:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22132:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22133:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22134:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22135:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22136:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22137:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22138:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22139:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22140:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22141:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22142:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22143:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22144:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22145:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22146:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22147:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22148:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-22149:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22150:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22151:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22152:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22153:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22154:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22155:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22156:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22157:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-22158:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22159:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22160:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22161:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22162:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-22163:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22164:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22165:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22166:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22167:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22168:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22169:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22170:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22171:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22172:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22173:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22174:

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

.. _no-22175:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22176:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22177:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22178:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22179:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22180:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22181:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22182:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22183:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22184:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22185:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22186:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22187:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22188:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22189:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22190:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22191:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22192:

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

.. _no-22193:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22194:

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

.. _no-22195:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22196:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-22197:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22198:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22199:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22200:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22201:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22202:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22203:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22204:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22205:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22206:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22207:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22208:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22209:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22210:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22211:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22212:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22213:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-22214:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-22215:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-22216:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22217:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22218:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22219:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22220:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22221:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22222:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------

.. _no-22223:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22224:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22225:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22226:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-22227>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-22228>`                 Occurs after the control or form is created.
:ref:`Destroy <no-22229>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-22230>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-22231>`               Occurs when the control gets the focus.
:ref:`Hit <no-22232>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-22233>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-22234>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-22235>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-22236>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-22237>`               
:ref:`KeyUp <no-22238>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-22239>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-22240>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-22241>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-22242>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-22243>`             
:ref:`MouseLeave <no-22244>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-22245>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-22246>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-22247>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-22248>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-22249>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-22250>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-22251>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-22252>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-22253>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-22254>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-22255>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-22256>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-22257>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-22258>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-22259>`                   Occurs when the control's position changes.
:ref:`Paint <no-22260>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-22261>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-22262>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-22263>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-22264>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-22265>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-22227:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-22228:

**Create** 

Occurs after the control or form is created.



-------

.. _no-22229:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-22230:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-22231:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-22232:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-22233:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-22234:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-22235:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-22236:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-22237:

**KeyEvent** 



-------

.. _no-22238:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-22239:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-22240:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-22241:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-22242:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-22243:

**MouseEvent** 



-------

.. _no-22244:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-22245:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-22246:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-22247:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-22248:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-22249:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-22250:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-22251:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-22252:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-22253:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-22254:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-22255:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-22256:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-22257:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-22258:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-22259:

**Move** 

Occurs when the control's position changes.



-------

.. _no-22260:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-22261:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-22262:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-22263:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-22264:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-22265:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================== ========================
:ref:`absoluteCoordinates <no-22266>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-22267>`                    Instantiate object as a child of self.
:ref:`afterInit <no-22268>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-22269>`                 
:ref:`afterSetProperties <no-22270>`           
:ref:`autoBindEvents <no-22271>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-22272>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-22273>`          
:ref:`bindEvent <no-22274>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-22275>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-22276>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-22277>`                 Makes this object topmost
:ref:`charsAfterCursor <no-22278>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-22279>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-22280>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-22281>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-22282>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-22283>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-22284>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-22285>`                          Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-22286>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-22287>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-22288>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-22289>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-22290>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-22291>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-22292>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-22293>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-22294>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-22295>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-22296>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-22297>`                     Draws text on the object at the specified position
:ref:`endHover <no-22298>`                     
:ref:`fitToSizer <no-22299>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-22300>`                   
:ref:`fontZoomIn <no-22301>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-22302>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-22303>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-22304>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-22305>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-22306>`                
:ref:`getCaptureBitmap <no-22307>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-22308>`            Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-22309>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-22310>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-22311>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-22312>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-22313>`             
:ref:`getSizerProp <no-22314>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-22315>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-22316>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-22317>`                         Make the object invisible.
:ref:`initEvents <no-22318>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-22319>`               Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-22320>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-22321>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-22322>`                  Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-22323>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-22324>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-22325>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-22326>`                      
:ref:`paste <no-22327>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-22328>`                  
:ref:`processDroppedFiles <no-22329>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-22330>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-22331>`                   Raise the passed Dabo event.
:ref:`reCreate <no-22332>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-22333>`                     Recreate the object.
:ref:`redraw <no-22334>`                       Called when the object is (re)drawn.
:ref:`refresh <no-22335>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-22336>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-22337>`                      Destroys the object.
:ref:`removeDrawnObject <no-22338>`            
:ref:`restoreValue <no-22339>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-22340>`                    Save control's value to dApp's user settings table.
:ref:`select <no-22341>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-22342>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-22343>`                   Select no text in the control.
:ref:`sendToBack <no-22344>`                   Places this object behind all others.
:ref:`setAll <no-22345>`                       Set all child object properties to the passed value.
:ref:`setFocus <no-22346>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-22347>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-22348>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-22349>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-22350>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-22351>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-22352>`                         Make the object visible.
:ref:`showContainingPage <no-22353>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-22354>`              Display a context menu (popup) at the specified position.
:ref:`super <no-22355>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-22356>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-22357>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-22358>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-22359>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-22360>`                       Update control's value to match the current value from the source.
:ref:`write <no-22361>`                        write(self, String text)

============================================== ========================


Methods - inherited
=====================

.. _no-22266:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22267:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-22268:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22269:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22270:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22271:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.autoBindEvents(self, force=True)
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

.. _no-22272:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22273:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22274:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22275:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22276:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-22277:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22278:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22279:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22280:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22281:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22282:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22283:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.convertStringValueToDataType(self, strVal, dataType)
   :noindex:


   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-22284:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22285:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22286:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22287:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22288:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-22289:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22290:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22291:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22292:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22293:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22294:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22295:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22296:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22297:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22298:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22299:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22300:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22301:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22302:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22303:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22304:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22305:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22306:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22307:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22308:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22309:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22310:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22311:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22312:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-22313:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22314:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22315:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22316:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.getStringValue(self, value)
   :noindex:


   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-22317:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22318:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22319:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22320:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22321:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22322:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.lockDisplay(self)
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

.. _no-22323:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22324:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22325:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22326:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22327:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22328:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22329:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22330:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22331:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22332:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22333:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22334:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22335:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22336:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22337:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22338:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22339:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22340:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22341:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-22342:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-22343:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-22344:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22345:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-22346:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22347:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22348:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-22349:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-22350:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22351:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22352:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22353:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22354:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22355:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22356:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22357:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22358:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22359:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22360:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22361:

.. function:: dabo.ui.uiwx.dTextBox.dTextBox.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
