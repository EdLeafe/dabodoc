
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dTextBoxMixin

.. _dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase:

========================================================
|doc_title|  **dTextBoxMixin.dTextBoxMixinBase** - class
========================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dTextBoxMixinBase**

.. inheritance-diagram:: dTextBoxMixinBase


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase

   .. automethod:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-31038>`                Specifies the alignment of the text. (str)
:ref:`Application <no-31039>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-31040>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-31041>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-31042>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-31043>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-31044>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-31045>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-31046>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-31047>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-31048>`                  The caption of the object. (str)
:ref:`Children <no-31049>`                 Returns a list of object references to the children of
:ref:`Class <no-31050>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-31051>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-31052>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-31053>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-31054>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-31055>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-31056>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-31057>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-31058>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-31059>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-31060>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-31061>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-31062>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-31063>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-31064>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-31065>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-31066>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-31067>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-31068>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-31069>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-31070>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-31071>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-31072>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-31073>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-31074>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-31075>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-31076>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-31077>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-31078>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-31079>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-31080>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-31081>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-31082>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-31083>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-31084>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-31085>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-31086>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-31087>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-31088>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-31089>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-31090>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-31091>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-31092>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-31093>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-31094>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-31095>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-31096>`                 Specifies the font face. (str)
:ref:`FontInfo <no-31097>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-31098>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-31099>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-31100>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-31101>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-31102>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-31103>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-31104>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-31105>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-31106>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-31107>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-31108>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-31109>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-31110>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-31111>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-31112>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-31113>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-31114>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-31115>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-31116>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-31117>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-31118>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-31119>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-31120>`              Specifies the string displayed if Value is None  (str or None)
:ref:`Parent <no-31121>`                   The containing object. (obj)
:ref:`PersistSecretData <no-31122>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-31123>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-31124>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-31125>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-31126>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-31127>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-31128>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-31129>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-31130>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-31131>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-31132>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-31133>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-31134>`                     The size of the object. (tuple)
:ref:`Sizer <no-31135>`                    The sizer for the object.
:ref:`Source <no-31136>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-31137>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-31138>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-31139>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-31140>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-31141>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-31142>`                      The top position of the object. (int)
:ref:`Transparency <no-31143>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-31144>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-31145>`                    Specifies the current state of the control (the value of the field). (string)
:ref:`Visible <no-31146>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-31147>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-31148>`                    The width of the object. (int)
:ref:`WindowHandle <no-31149>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-31038:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right



-------

.. _no-31058:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.



-------

.. _no-31074:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.



-------

.. _no-31078:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.



-------

.. _no-31079:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.



-------

.. _no-31080:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.



-------

.. _no-31081:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.



-------

.. _no-31082:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.



-------

.. _no-31101:

**ForceCase** 

Determines if we change the case of entered text. Possible values are:

        ===========  =====================
        None or ""   No changes made (default)
        "Upper"      FORCE TO UPPER CASE
        "Lower"      Force to lower case
        "Title"      Force To Title Case
        ===========  =====================

    These can be abbreviated to "u", "l" or "t"  (str)



-------

.. _no-31107:

**InsertionPosition** 

Position of the insertion point within the control  (int)



-------

.. _no-31120:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.



-------

.. _no-31125:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)



-------

.. _no-31129:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)



-------

.. _no-31130:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)



-------

.. _no-31131:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)



-------

.. _no-31132:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)



-------

.. _no-31133:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)



-------

.. _no-31140:

**TextLength** 

The maximum length the entered text can be. (int)



-------


Properties - inherited
========================

.. _no-31039:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31040:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31041:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31042:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31043:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31044:

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

.. _no-31045:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31046:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31047:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31048:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31049:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31050:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31051:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31052:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31053:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31054:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31055:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31056:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31057:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31059:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31060:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31061:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31062:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31063:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31064:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31065:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31066:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31067:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31068:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31069:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31070:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31071:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31072:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31073:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31075:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31076:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31077:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31083:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31084:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31085:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31086:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31087:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31088:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31089:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31090:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31091:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31092:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31093:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31094:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31095:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31096:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31097:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31098:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31099:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31100:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31102:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31103:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31104:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31105:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31106:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31108:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31109:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31110:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31111:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31112:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31113:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31114:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31115:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31116:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31117:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31118:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31119:

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

.. _no-31121:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31122:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31123:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31124:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31126:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31127:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31128:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31134:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31135:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31136:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31137:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31138:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-31139:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31141:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31142:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31143:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31144:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31145:

**Value** 

Specifies the current state of the control (the value of the field). (string)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31146:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31147:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31148:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31149:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-31150>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-31151>`                 Occurs after the control or form is created.
:ref:`Destroy <no-31152>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-31153>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-31154>`               Occurs when the control gets the focus.
:ref:`Idle <no-31155>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-31156>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-31157>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-31158>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-31159>`               
:ref:`KeyUp <no-31160>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-31161>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-31162>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-31163>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-31164>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-31165>`             
:ref:`MouseLeave <no-31166>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-31167>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-31168>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-31169>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-31170>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-31171>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-31172>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-31173>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-31174>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-31175>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-31176>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-31177>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-31178>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-31179>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-31180>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-31181>`                   Occurs when the control's position changes.
:ref:`Paint <no-31182>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-31183>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-31184>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-31185>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-31186>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-31187>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-31150:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-31151:

**Create** 

Occurs after the control or form is created.



-------

.. _no-31152:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-31153:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-31154:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-31155:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-31156:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-31157:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-31158:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-31159:

**KeyEvent** 



-------

.. _no-31160:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-31161:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-31162:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-31163:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-31164:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-31165:

**MouseEvent** 



-------

.. _no-31166:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-31167:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-31168:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-31169:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-31170:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-31171:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-31172:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-31173:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-31174:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-31175:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-31176:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-31177:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-31178:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-31179:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-31180:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-31181:

**Move** 

Occurs when the control's position changes.



-------

.. _no-31182:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-31183:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-31184:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-31185:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-31186:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-31187:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-31188>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-31189>`             Instantiate object as a child of self.
:ref:`afterInit <no-31190>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-31191>`          
:ref:`afterSetProperties <no-31192>`    
:ref:`autoBindEvents <no-31193>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-31194>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-31195>`   
:ref:`bindEvent <no-31196>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-31197>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-31198>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-31199>`          Makes this object topmost
:ref:`charsAfterCursor <no-31200>`      Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-31201>`     Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-31202>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-31203>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-31204>`  Given a position relative to this control, return a position relative
:ref:`copy <no-31205>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-31206>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-31207>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-31208>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-31209>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-31210>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-31211>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-31212>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-31213>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-31214>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-31215>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-31216>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-31217>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-31218>`              Draws text on the object at the specified position
:ref:`endHover <no-31219>`              
:ref:`fitToSizer <no-31220>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-31221>`            
:ref:`fontZoomIn <no-31222>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-31223>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-31224>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-31225>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-31226>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-31227>`         
:ref:`getCaptureBitmap <no-31228>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-31229>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-31230>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-31231>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-31232>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-31233>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-31234>`      
:ref:`getSizerProp <no-31235>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-31236>`         Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-31237>`        Hook function if you want to implement dataTypes other than str
:ref:`hide <no-31238>`                  Make the object invisible.
:ref:`initEvents <no-31239>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-31240>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-31241>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-31242>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-31243>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-31244>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-31245>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-31246>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-31247>`               
:ref:`paste <no-31248>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-31249>`           
:ref:`processDroppedFiles <no-31250>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-31251>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-31252>`            Raise the passed Dabo event.
:ref:`reCreate <no-31253>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-31254>`              Recreate the object.
:ref:`redraw <no-31255>`                Called when the object is (re)drawn.
:ref:`refresh <no-31256>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-31257>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-31258>`               Destroys the object.
:ref:`removeDrawnObject <no-31259>`     
:ref:`restoreValue <no-31260>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-31261>`             Save control's value to dApp's user settings table.
:ref:`select <no-31262>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-31263>`             Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-31264>`            Select no text in the control.
:ref:`sendToBack <no-31265>`            Places this object behind all others.
:ref:`setAll <no-31266>`                Set all child object properties to the passed value.
:ref:`setFocus <no-31267>`              Sets focus to the object.
:ref:`setPositionInSizer <no-31268>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-31269>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-31270>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-31271>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-31272>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-31273>`                  Make the object visible.
:ref:`showContainingPage <no-31274>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-31275>`       Display a context menu (popup) at the specified position.
:ref:`super <no-31276>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-31277>`           Remove a previously registered event binding.
:ref:`unbindKey <no-31278>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-31279>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-31280>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-31281>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-31200:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.charsAfterCursor(self, num=None, includeSelectedText=False)

   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   



-------

.. _no-31201:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.charsBeforeCursor(self, num=None, includeSelectedText=False)

   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   



-------

.. _no-31221:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.flushValue(self)



-------

.. _no-31227:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getBlankValue(self)



-------

.. _no-31237:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getStringValue(self, val)

   Hook function if you want to implement dataTypes other than str



-------

.. _no-31263:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.selectAll(self)

   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   



-------


Methods - inherited
=====================

.. _no-31188:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31189:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-31190:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31191:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31192:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31193:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.autoBindEvents(self, force=True)
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

.. _no-31194:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31195:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31196:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31197:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31198:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-31199:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31202:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31203:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31204:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31205:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31206:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31207:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31208:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31209:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-31210:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31211:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31212:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31213:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31214:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31215:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31216:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31217:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31218:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31219:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31220:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31222:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31223:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31224:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31225:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31226:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31228:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31229:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31230:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31231:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31232:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31233:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-31234:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31235:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31236:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31238:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31239:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31240:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31241:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31242:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31243:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.lockDisplay(self)
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

.. _no-31244:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31245:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31246:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31247:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31248:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31249:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31250:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31251:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31252:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31253:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31254:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31255:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31256:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31257:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31258:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31259:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31260:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31261:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31262:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31264:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31265:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31266:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-31267:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31268:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31269:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-31270:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-31271:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31272:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31273:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31274:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31275:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31276:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31277:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31278:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31279:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31280:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31281:

.. function:: dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
