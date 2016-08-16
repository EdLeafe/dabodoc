
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dRichTextBox

.. _dabo.ui.uiwx.dRichTextBox.dRichTextBox:

==================================================
|doc_title|  **dRichTextBox.dRichTextBox** - class
==================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dRichTextBox**

.. inheritance-diagram:: dRichTextBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`
* wx.richtext.RichTextCtrl - can not provide a link



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dRichTextBox.png
          :scale: 75 %
          :target: _static/winWidgets/dRichTextBox.png
          :alt: dRichTextBox



     - .. image:: _static/nixWidgets/dRichTextBox.png
          :scale: 75 %
          :target: _static/nixWidgets/dRichTextBox.png
          :alt: dRichTextBox


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dRichTextBox.dRichTextBox

   .. automethod:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-18943>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-18944>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-18945>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-18946>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-18947>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-18948>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-18949>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-18950>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-18951>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-18952>`                  The caption of the object. (str)
:ref:`Children <no-18953>`                 Returns a list of object references to the children of
:ref:`Class <no-18954>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-18955>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-18956>`     Reference to the sizer item that control's this control's layout.
:ref:`CurrentBackColor <no-18957>`         Background color at the current insertion point.  (RGB 3-tuple)
:ref:`CurrentFontBold <no-18958>`          Font bold status at the current insertion point.  (str)
:ref:`CurrentFontFace <no-18959>`          Font face at the current insertion point.  (str)
:ref:`CurrentFontItalic <no-18960>`        Font italic status at the current insertion point.  (str)
:ref:`CurrentFontSize <no-18961>`          Font size at the current insertion point.  (int)
:ref:`CurrentFontUnderline <no-18962>`     Font underline status at the current insertion point.  (str)
:ref:`CurrentForeColor <no-18963>`         Background color at the current insertion point.  (RGB 3-tuple)
:ref:`CurrentStyle <no-18964>`             Returns the style in effect at the current insertion point.
:ref:`DataField <no-18965>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-18966>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-18967>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-18968>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-18969>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-18970>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-18971>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-18972>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-18973>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-18974>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-18975>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-18976>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-18977>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-18978>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-18979>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-18980>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-18981>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-18982>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-18983>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-18984>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-18985>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-18986>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-18987>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-18988>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-18989>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-18990>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-18991>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-18992>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-18993>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-18994>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-18995>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-18996>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-18997>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-18998>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-18999>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-19000>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-19001>`                 Specifies the font face. (str)
:ref:`FontInfo <no-19002>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-19003>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-19004>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-19005>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-19006>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-19007>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-19008>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-19009>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-19010>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-19011>`        Current position of the insertion point in the control.  (int)
:ref:`IsSecret <no-19012>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-19013>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-19014>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-19015>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-19016>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-19017>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-19018>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-19019>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-19020>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-19021>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-19022>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-19023>`                 Specifies the base name of the object.
:ref:`Parent <no-19024>`                   The containing object. (obj)
:ref:`PersistSecretData <no-19025>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-19026>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-19027>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-19028>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-19029>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-19030>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-19031>`         Specifies whether the Value of the control gets saved when
:ref:`SelectionBackColor <no-19032>`       Color of the current selection's background.  (RGB 3-tuple)
:ref:`SelectionEnd <no-19033>`             Returns the end position of the current text selection,
:ref:`SelectionFontBold <no-19034>`        Reflects the Bold status of the current selection. This will be
:ref:`SelectionFontFace <no-19035>`        Reflects the FontFace status of the current selection. If multiple
:ref:`SelectionFontItalic <no-19036>`      Reflects the Italic status of the current selection. This will be
:ref:`SelectionFontSize <no-19037>`        Reflects the FontSize status of the current selection. If multiple
:ref:`SelectionFontUnderline <no-19038>`   Reflects the Underline status of the current selection. This will be
:ref:`SelectionForeColor <no-19039>`       Color of the current selection's text.  (RGB 3-tuple)
:ref:`SelectionPlain <no-19040>`           Reflects the Plain status of the current selection. This will be
:ref:`SelectionRange <no-19041>`           Returns/sets the position of the current selected text. No selection
:ref:`SelectionStart <no-19042>`           Returns the beginning position of the current text selection,
:ref:`Size <no-19043>`                     The size of the object. (tuple)
:ref:`Sizer <no-19044>`                    The sizer for the object.
:ref:`Source <no-19045>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-19046>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-19047>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-19048>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-19049>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-19050>`                      The top position of the object. (int)
:ref:`Transparency <no-19051>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-19052>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-19053>`                    Specifies the current state of the control (the value of the field).  (varies)
:ref:`Visible <no-19054>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-19055>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-19056>`                    The width of the object. (int)
:ref:`WindowHandle <no-19057>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-18957:

**CurrentBackColor** 

Background color at the current insertion point.  (RGB 3-tuple)



-------

.. _no-18958:

**CurrentFontBold** 

Font bold status at the current insertion point.  (str)



-------

.. _no-18959:

**CurrentFontFace** 

Font face at the current insertion point.  (str)



-------

.. _no-18960:

**CurrentFontItalic** 

Font italic status at the current insertion point.  (str)



-------

.. _no-18961:

**CurrentFontSize** 

Font size at the current insertion point.  (int)



-------

.. _no-18962:

**CurrentFontUnderline** 

Font underline status at the current insertion point.  (str)



-------

.. _no-18963:

**CurrentForeColor** 

Background color at the current insertion point.  (RGB 3-tuple)



-------

.. _no-18964:

**CurrentStyle** 

Returns the style in effect at the current insertion point.
    In other words, it is the style that will be applied to text that is
    typed at that position. Returns a tuple containing one or more
    of 'Plain', 'Bold', 'Italic', 'Underline'.  (read-only) (tuple)



-------

.. _no-19011:

**InsertionPosition** 

Current position of the insertion point in the control.  (int)



-------

.. _no-19028:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)



-------

.. _no-19032:

**SelectionBackColor** 

Color of the current selection's background.  (RGB 3-tuple)



-------

.. _no-19033:

**SelectionEnd** 

Returns the end position of the current text selection,
    or None if no text is selected. (int)



-------

.. _no-19034:

**SelectionFontBold** 

Reflects the Bold status of the current selection. This will be
    True if every character in the selection is bold; if even one character
    is not bold, this will be False. If there is no selection, this will be
    None. Setting this affects all selected text; it has no effect if no
    text is selected  (bool)



-------

.. _no-19035:

**SelectionFontFace** 

Reflects the FontFace status of the current selection. If multiple
    faces are used throughout the selection, the face at the beginning of
    the selection will be returned. If there is no selection, None will be
    returned. Setting this affects all selected text; it has no effect if no
    text is selected  (str)



-------

.. _no-19036:

**SelectionFontItalic** 

Reflects the Italic status of the current selection. This will be
    True if every character in the selection is Italic; if even one character
    is not Italic, this will be False. If there is no selection, this will be
    None. Setting this affects all selected text; it has no effect if no
    text is selected  (bool)



-------

.. _no-19037:

**SelectionFontSize** 

Reflects the FontSize status of the current selection. If multiple
    sizes are used throughout the selection, the size at the beginning of
    the selection will be returned. If there is no selection, None will be
    returned. Setting this affects all selected text; it has no effect if no
    text is selected  (int)



-------

.. _no-19038:

**SelectionFontUnderline** 

Reflects the Underline status of the current selection. This will be
    True if every character in the selection is underlined; if even one character
    is not underlined, this will be False. If there is no selection, this will be
    None. Setting this affects all selected text; it has no effect if no
    text is selected  (bool)



-------

.. _no-19039:

**SelectionForeColor** 

Color of the current selection's text.  (RGB 3-tuple)



-------

.. _no-19040:

**SelectionPlain** 

Reflects the Plain status of the current selection. This will be
    True if every character in the selection is neither bold, italic or
    underlined. If there is no selection, this will be None. Setting this
    affects all selected text; it has no effect if no text is selected  (bool)



-------

.. _no-19042:

**SelectionStart** 

Returns the beginning position of the current text selection,
    or None if no text is selected. (int)



-------


Properties - inherited
========================

.. _no-18943:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18944:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18945:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18946:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18947:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18948:

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

.. _no-18949:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18950:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18951:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18952:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18953:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18954:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18955:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18956:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18965:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18966:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18967:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18968:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18969:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18970:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18971:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18972:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18973:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18974:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18975:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18976:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18977:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18978:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18979:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18980:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18981:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18982:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18983:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18984:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18985:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18986:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18987:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18988:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18989:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18990:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18991:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18992:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18993:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18994:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-18995:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18996:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18997:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18998:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18999:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19000:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19001:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19002:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19003:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19004:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19005:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19006:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19007:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19008:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19009:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19010:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19012:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19013:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19014:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19015:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19016:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19017:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19018:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19019:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19020:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19021:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19022:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19023:

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

.. _no-19024:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19025:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19026:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19027:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19029:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19030:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19031:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19041:

**SelectionRange** 

Returns/sets the position of the current selected text. No selection
    is represented by (None, None). You can also unselect all text by setting
    this property to None. (2-tuple of int or None)


Inherited from: 'wx.richtext.RichTextCtrl - can not provide a link

-------

.. _no-19043:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19044:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19045:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19046:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19047:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-19048:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19049:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19050:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19051:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19052:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19053:

**Value** 

Specifies the current state of the control (the value of the field).  (varies)


Inherited from: 'wx.richtext.RichTextCtrl - can not provide a link

-------

.. _no-19054:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19055:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19056:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19057:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-19058>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-19059>`                 Occurs after the control or form is created.
:ref:`Destroy <no-19060>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-19061>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-19062>`               Occurs when the control gets the focus.
:ref:`Idle <no-19063>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-19064>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-19065>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-19066>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-19067>`               
:ref:`KeyUp <no-19068>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-19069>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-19070>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-19071>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-19072>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-19073>`             
:ref:`MouseLeave <no-19074>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-19075>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-19076>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-19077>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-19078>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-19079>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-19080>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-19081>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-19082>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-19083>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-19084>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-19085>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-19086>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-19087>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-19088>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-19089>`                   Occurs when the control's position changes.
:ref:`Paint <no-19090>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-19091>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-19092>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-19093>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-19094>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-19095>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-19058:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-19059:

**Create** 

Occurs after the control or form is created.



-------

.. _no-19060:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-19061:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-19062:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-19063:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-19064:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-19065:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-19066:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-19067:

**KeyEvent** 



-------

.. _no-19068:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-19069:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-19070:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-19071:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-19072:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-19073:

**MouseEvent** 



-------

.. _no-19074:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-19075:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-19076:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-19077:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-19078:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-19079:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-19080:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-19081:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-19082:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-19083:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-19084:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-19085:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-19086:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-19087:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-19088:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-19089:

**Move** 

Occurs when the control's position changes.



-------

.. _no-19090:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-19091:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-19092:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-19093:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-19094:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-19095:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-19096>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-19097>`             Instantiate object as a child of self.
:ref:`afterInit <no-19098>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-19099>`          
:ref:`afterSetProperties <no-19100>`    
:ref:`autoBindEvents <no-19101>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-19102>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-19103>`   
:ref:`bindEvent <no-19104>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-19105>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-19106>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-19107>`          Makes this object topmost
:ref:`clear <no-19108>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-19109>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-19110>`  Given a position relative to this control, return a position relative
:ref:`copy <no-19111>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-19112>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-19113>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-19114>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-19115>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-19116>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-19117>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-19118>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-19119>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-19120>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-19121>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-19122>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-19123>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-19124>`              Draws text on the object at the specified position
:ref:`endHover <no-19125>`              
:ref:`fitToSizer <no-19126>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-19127>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-19128>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-19129>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-19130>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-19131>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-19132>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-19133>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-19134>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-19135>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-19136>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-19137>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-19138>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-19139>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-19140>`      
:ref:`getSizerProp <no-19141>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-19142>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-19143>`                  Make the object invisible.
:ref:`initEvents <no-19144>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-19145>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-19146>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-19147>`           Call the given function on this object and all of its Children. If
:ref:`load <no-19148>`                  Takes either a file-like object or a file path, and loads the content
:ref:`lockDisplay <no-19149>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-19150>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-19151>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-19152>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-19153>`               
:ref:`paste <no-19154>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-19155>`           
:ref:`processDroppedFiles <no-19156>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-19157>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-19158>`            Raise the passed Dabo event.
:ref:`reCreate <no-19159>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-19160>`              Recreate the object.
:ref:`redraw <no-19161>`                Called when the object is (re)drawn.
:ref:`refresh <no-19162>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-19163>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-19164>`               Destroys the object.
:ref:`removeDrawnObject <no-19165>`     
:ref:`restoreValue <no-19166>`          Set the control's value to the value in dApp's user settings table.
:ref:`save <no-19167>`                  
:ref:`saveValue <no-19168>`             Save control's value to dApp's user settings table.
:ref:`select <no-19169>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-19170>`             Select all text in the control.
:ref:`selectNone <no-19171>`            Select no text in the control.
:ref:`sendToBack <no-19172>`            Places this object behind all others.
:ref:`setAll <no-19173>`                Set all child object properties to the passed value.
:ref:`setFocus <no-19174>`              Sets focus to the object.
:ref:`setPlain <no-19175>`              Removes all styles from the selected text
:ref:`setPositionInSizer <no-19176>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-19177>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-19178>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-19179>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-19180>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-19181>`                  Make the object visible.
:ref:`showContainingPage <no-19182>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-19183>`       Display a context menu (popup) at the specified position.
:ref:`super <no-19184>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-19185>`           Remove a previously registered event binding.
:ref:`unbindKey <no-19186>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-19187>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-19188>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-19189>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-19148:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.load(self, fileOrObj=None)

   
   Takes either a file-like object or a file path, and loads the content
   into the control.
   



-------

.. _no-19167:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.save(self, filename=None)



-------

.. _no-19175:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setPlain(self)

   Removes all styles from the selected text



-------


Methods - inherited
=====================

.. _no-19096:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19097:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-19098:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19099:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19100:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19101:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.autoBindEvents(self, force=True)
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

.. _no-19102:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19103:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19104:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19105:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19106:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-19107:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19108:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19109:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19110:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19111:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19112:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19113:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19114:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19115:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-19116:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19117:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19118:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19119:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19120:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19121:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19122:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19123:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19124:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19125:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19126:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19127:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19128:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19129:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19130:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19131:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19132:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19133:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19134:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19135:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19136:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19137:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19138:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19139:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-19140:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19141:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19142:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19143:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19144:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19145:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19146:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19147:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19149:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.lockDisplay(self)
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

.. _no-19150:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19151:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19152:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19153:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19154:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19155:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19156:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19157:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19158:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19159:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19160:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19161:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19162:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19163:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19164:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19165:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19166:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19168:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-19169:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-19170:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-19171:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-19172:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19173:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-19174:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19176:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19177:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-19178:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-19179:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19180:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19181:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19182:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19183:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19184:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19185:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19186:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19187:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19188:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19189:

.. function:: dabo.ui.uiwx.dRichTextBox.dRichTextBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
