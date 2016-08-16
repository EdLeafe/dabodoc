
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDateTextBox

.. _dabo.ui.uiwx.dDateTextBox.dDateTextBox:

==================================================
|doc_title|  **dDateTextBox.dDateTextBox** - class
==================================================


This is a specialized textbox class designed to work with date values.
It provides handy shortcut keystrokes so that users can quickly navigate
to the date value they need. The keystrokes are the same as those used
by Quicken, the popular personal finance program.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDateTextBox**

.. inheritance-diagram:: dDateTextBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTextBox.dTextBox`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Page.SelectDateTextBox`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dDateTextBox.png
          :scale: 75 %
          :target: _static/macWidgets/dDateTextBox.png
          :alt: dDateTextBox



     - no image available



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDateTextBox.dDateTextBox


|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-24730>`                Specifies the alignment of the text. (str)
:ref:`Application <no-24731>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-24732>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-24733>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-24734>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-24735>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-24736>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-24737>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-24738>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-24739>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-24740>`                  The caption of the object. (str)
:ref:`Children <no-24741>`                 Returns a list of object references to the children of
:ref:`Class <no-24742>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-24743>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-24744>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-24745>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-24746>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-24747>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-24748>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-24749>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-24750>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-24751>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-24752>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-24753>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-24754>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-24755>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-24756>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-24757>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-24758>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-24759>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-24760>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-24761>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-24762>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-24763>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-24764>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-24765>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-24766>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-24767>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-24768>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-24769>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-24770>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-24771>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-24772>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-24773>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-24774>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-24775>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-24776>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-24777>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-24778>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-24779>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-24780>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-24781>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-24782>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-24783>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-24784>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-24785>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-24786>`                  Specifies whether the object and children can get user input. (bool)
:ref:`ExtendedCalendar <no-24787>`         When True, the calendar is displayed in a larger format with more controls
:ref:`Font <no-24788>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-24789>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-24790>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-24791>`                 Specifies the font face. (str)
:ref:`FontInfo <no-24792>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-24793>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-24794>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-24795>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-24796>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-24797>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-24798>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-24799>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-24800>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-24801>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-24802>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-24803>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-24804>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-24805>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-24806>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-24807>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-24808>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-24809>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-24810>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-24811>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-24812>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-24813>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-24814>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-24815>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-24816>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`Parent <no-24817>`                   The containing object. (obj)
:ref:`PasswordEntry <no-24818>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-24819>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-24820>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-24821>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-24822>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-24823>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-24824>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-24825>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-24826>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-24827>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-24828>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-24829>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-24830>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-24831>`                     The size of the object. (tuple)
:ref:`Sizer <no-24832>`                    The sizer for the object.
:ref:`Source <no-24833>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-24834>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-24835>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-24836>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-24837>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-24838>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-24839>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-24840>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-24841>`                      The top position of the object. (int)
:ref:`Transparency <no-24842>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-24843>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-24844>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-24845>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-24846>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-24847>`                    The width of the object. (int)
:ref:`WindowHandle <no-24848>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-24787:

**ExtendedCalendar** 

When True, the calendar is displayed in a larger format with more controls
    for quickly moving to any date. Default=False  (bool)



-------


Properties - inherited
========================

.. _no-24730:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-24731:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24732:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24733:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24734:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24735:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24736:

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

.. _no-24737:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24738:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24739:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24740:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24741:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24742:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24743:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24744:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24745:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24746:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24747:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24748:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24749:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24750:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24751:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24752:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24753:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24754:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24755:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24756:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24757:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24758:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24759:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24760:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24761:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24762:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24763:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24764:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24765:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24766:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24767:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24768:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24769:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-24770:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24771:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24772:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24773:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24774:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24775:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24776:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24777:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24778:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-24779:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24780:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24781:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24782:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24783:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-24784:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24785:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24786:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24788:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24789:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24790:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24791:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24792:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24793:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24794:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24795:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24796:

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

.. _no-24797:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24798:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24799:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24800:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24801:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24802:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24803:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24804:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24805:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24806:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24807:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24808:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24809:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24810:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24811:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24812:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24813:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24814:

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

.. _no-24815:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24816:

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

.. _no-24817:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24818:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-24819:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24820:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24821:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24822:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24823:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24824:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24825:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24826:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24827:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24828:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24829:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24830:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24831:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24832:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24833:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24834:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24835:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-24836:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-24837:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-24838:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24839:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24840:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24841:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24842:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24843:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24844:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------

.. _no-24845:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24846:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24847:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24848:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-24849>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-24850>`                 Occurs after the control or form is created.
:ref:`Destroy <no-24851>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-24852>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-24853>`               Occurs when the control gets the focus.
:ref:`Hit <no-24854>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-24855>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-24856>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-24857>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-24858>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-24859>`               
:ref:`KeyUp <no-24860>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-24861>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-24862>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-24863>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-24864>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-24865>`             
:ref:`MouseLeave <no-24866>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-24867>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-24868>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-24869>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-24870>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-24871>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-24872>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-24873>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-24874>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-24875>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-24876>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-24877>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-24878>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-24879>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-24880>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-24881>`                   Occurs when the control's position changes.
:ref:`Paint <no-24882>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-24883>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-24884>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-24885>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-24886>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-24887>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-24849:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-24850:

**Create** 

Occurs after the control or form is created.



-------

.. _no-24851:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-24852:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-24853:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-24854:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-24855:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-24856:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-24857:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-24858:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-24859:

**KeyEvent** 



-------

.. _no-24860:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-24861:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-24862:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-24863:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-24864:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-24865:

**MouseEvent** 



-------

.. _no-24866:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-24867:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-24868:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-24869:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-24870:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-24871:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-24872:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-24873:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-24874:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-24875:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-24876:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-24877:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-24878:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-24879:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-24880:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-24881:

**Move** 

Occurs when the control's position changes.



-------

.. _no-24882:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-24883:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-24884:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-24885:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-24886:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-24887:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================== ========================
:ref:`absoluteCoordinates <no-24888>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-24889>`                    Instantiate object as a child of self.
:ref:`adjustDate <no-24890>`                   Modifies the current date value if the key is one of the
:ref:`afterInit <no-24891>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-24892>`                 
:ref:`afterSetProperties <no-24893>`           
:ref:`autoBindEvents <no-24894>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-24895>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-24896>`          
:ref:`bindEvent <no-24897>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-24898>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-24899>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-24900>`                 Makes this object topmost
:ref:`charsAfterCursor <no-24901>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-24902>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-24903>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-24904>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-24905>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-24906>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-24907>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-24908>`                          Called by uiApp when the user requests a cut operation.
:ref:`dayInterval <no-24909>`                  Adjusts the date by the given number of days; negative
:ref:`drawArc <no-24910>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-24911>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-24912>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-24913>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-24914>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-24915>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-24916>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-24917>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-24918>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-24919>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-24920>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-24921>`                     Draws text on the object at the specified position
:ref:`endHover <no-24922>`                     
:ref:`fitToSizer <no-24923>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-24924>`                   
:ref:`fontZoomIn <no-24925>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-24926>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-24927>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-24928>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-24929>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-24930>`                
:ref:`getCaptureBitmap <no-24931>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-24932>`            Return the dPage or WizardPage that contains self.
:ref:`getDateTuple <no-24933>`                 
:ref:`getDisplayLocker <no-24934>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-24935>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-24936>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-24937>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-24938>`             
:ref:`getSizerProp <no-24939>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-24940>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-24941>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-24942>`                         Make the object invisible.
:ref:`hourInterval <no-24943>`                 Adjusts the date by the given number of hours; negative
:ref:`initEvents <no-24944>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-24945>`               Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-24946>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-24947>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-24948>`                  Locks the visual updates to the control.
:ref:`minuteInterval <no-24949>`               Adjusts the date by the given number of minutes; negative
:ref:`monthInterval <no-24950>`                Adjusts the date by the given number of months; negative
:ref:`moveTabOrderAfter <no-24951>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-24952>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-24953>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-24954>`                      
:ref:`paste <no-24955>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-24956>`                  
:ref:`processDroppedFiles <no-24957>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-24958>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-24959>`                   Raise the passed Dabo event.
:ref:`reCreate <no-24960>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-24961>`                     Recreate the object.
:ref:`redraw <no-24962>`                       Called when the object is (re)drawn.
:ref:`refresh <no-24963>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-24964>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-24965>`                      Destroys the object.
:ref:`removeDrawnObject <no-24966>`            
:ref:`restoreValue <no-24967>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-24968>`                    Save control's value to dApp's user settings table.
:ref:`secondInterval <no-24969>`               Adjusts the date by the given number of seconds; negative
:ref:`select <no-24970>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-24971>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-24972>`                   Select no text in the control.
:ref:`sendToBack <no-24973>`                   Places this object behind all others.
:ref:`setAll <no-24974>`                       Set all child object properties to the passed value.
:ref:`setDate <no-24975>`                      Sets the Value to the passed date if this is holding a date value, or
:ref:`setFocus <no-24976>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-24977>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-24978>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-24979>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-24980>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-24981>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`setToLastMonthDay <no-24982>`            
:ref:`show <no-24983>`                         Make the object visible.
:ref:`showCalendar <no-24984>`                 
:ref:`showContainingPage <no-24985>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-24986>`              Display a context menu (popup) at the specified position.
:ref:`super <no-24987>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-24988>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-24989>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-24990>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-24991>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-24992>`                       Update control's value to match the current value from the source.
:ref:`write <no-24993>`                        write(self, String text)

============================================== ========================


Methods
=======

.. _no-24890:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.adjustDate(self, key, ctrl=False, shift=False)

   
   Modifies the current date value if the key is one of the
   shortcut keys.
   



-------

.. _no-24909:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.dayInterval(self, days)

   
   Adjusts the date by the given number of days; negative
   values move backwards.
   



-------

.. _no-24933:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getDateTuple(self)



-------

.. _no-24943:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.hourInterval(self, hours)

   
   Adjusts the date by the given number of hours; negative
   values move backwards.
   



-------

.. _no-24949:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.minuteInterval(self, minutes)

   
   Adjusts the date by the given number of minutes; negative
   values move backwards.
   



-------

.. _no-24950:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.monthInterval(self, months)

   
   Adjusts the date by the given number of months; negative
   values move backwards.
   



-------

.. _no-24969:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.secondInterval(self, seconds)

   
   Adjusts the date by the given number of seconds; negative
   values move backwards.
   



-------

.. _no-24975:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setDate(self, dt)

   
   Sets the Value to the passed date if this is holding a date value, or
   sets the date portion of the Value if it is a datetime.
   



-------

.. _no-24982:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setToLastMonthDay(self)



-------

.. _no-24984:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.showCalendar(self)



-------


Methods - inherited
=====================

.. _no-24888:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24889:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-24891:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24892:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24893:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24894:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.autoBindEvents(self, force=True)
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

.. _no-24895:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24896:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24897:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24898:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24899:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-24900:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24901:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24902:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24903:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24904:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24905:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24906:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.convertStringValueToDataType(self, strVal, dataType)
   :noindex:


   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-24907:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24908:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24910:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24911:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24912:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-24913:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24914:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24915:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24916:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24917:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24918:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24919:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24920:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24921:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24922:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24923:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24924:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24925:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24926:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24927:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24928:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24929:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24930:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24931:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24932:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24934:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24935:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24936:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24937:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-24938:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24939:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24940:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24941:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.getStringValue(self, value)
   :noindex:


   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-24942:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24944:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24945:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24946:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24947:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24948:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.lockDisplay(self)
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

.. _no-24951:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24952:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24953:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24954:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24955:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24956:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24957:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24958:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24959:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24960:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24961:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24962:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24963:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24964:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24965:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24966:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24967:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24968:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24970:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-24971:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-24972:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-24973:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24974:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-24976:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24977:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24978:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-24979:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-24980:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24981:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24983:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24985:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24986:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24987:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24988:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24989:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24990:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24991:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24992:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24993:

.. function:: dabo.ui.uiwx.dDateTextBox.dDateTextBox.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
