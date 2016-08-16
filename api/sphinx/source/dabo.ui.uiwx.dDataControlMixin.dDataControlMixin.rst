
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDataControlMixin

.. _dabo.ui.uiwx.dDataControlMixin.dDataControlMixin:

============================================================
|doc_title|  **dDataControlMixin.dDataControlMixin** - class
============================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDataControlMixin**

.. inheritance-diagram:: dDataControlMixin


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`
* :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`
* :ref:`dabo.ui.uiwx.dDatePicker.dDatePicker`
* :ref:`dabo.ui.uiwx.dEditor.dEditor`
* :ref:`dabo.ui.uiwx.dImage.dImage`
* :ref:`dabo.ui.uiwx.dRichTextBox.dRichTextBox`
* :ref:`dabo.ui.uiwx.dSlider.dSlider`
* :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`
* :ref:`dabo.ui.uiwx.dToggleButton.dToggleButton`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin


|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-25548>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-25549>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-25550>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-25551>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-25552>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-25553>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-25554>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-25555>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-25556>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-25557>`                  The caption of the object. (str)
:ref:`Children <no-25558>`                 Returns a list of object references to the children of
:ref:`Class <no-25559>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-25560>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-25561>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-25562>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-25563>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-25564>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-25565>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-25566>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-25567>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-25568>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-25569>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-25570>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-25571>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-25572>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-25573>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-25574>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-25575>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-25576>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-25577>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-25578>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-25579>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-25580>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-25581>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-25582>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-25583>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-25584>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-25585>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-25586>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-25587>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-25588>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-25589>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-25590>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-25591>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-25592>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-25593>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-25594>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-25595>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-25596>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-25597>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-25598>`                 Specifies the font face. (str)
:ref:`FontInfo <no-25599>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-25600>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-25601>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-25602>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-25603>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-25604>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-25605>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-25606>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-25607>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-25608>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-25609>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-25610>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-25611>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-25612>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-25613>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-25614>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-25615>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-25616>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-25617>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-25618>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-25619>`                 Specifies the base name of the object.
:ref:`Parent <no-25620>`                   The containing object. (obj)
:ref:`PersistSecretData <no-25621>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-25622>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-25623>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-25624>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-25625>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-25626>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-25627>`                     The size of the object. (tuple)
:ref:`Sizer <no-25628>`                    The sizer for the object.
:ref:`Source <no-25629>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-25630>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-25631>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-25632>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-25633>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-25634>`                      The top position of the object. (int)
:ref:`Transparency <no-25635>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-25636>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-25637>`                    Specifies the current state of the control (the value of the field).  (varies)
:ref:`Visible <no-25638>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-25639>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-25640>`                    The width of the object. (int)
:ref:`WindowHandle <no-25641>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-25591:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.



-------


Properties - inherited
========================

.. _no-25548:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25549:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25550:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25551:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25552:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25553:

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

.. _no-25554:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25555:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25556:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25557:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25558:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25559:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25560:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25561:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25562:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25563:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25564:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25565:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25566:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25567:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25568:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25569:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25570:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25571:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25572:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25573:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25574:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25575:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25576:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25577:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25578:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25579:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25580:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25581:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25582:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25583:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25584:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25585:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25586:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25587:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25588:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25589:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25590:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25592:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25593:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25594:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25595:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25596:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25597:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25598:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25599:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25600:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25601:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25602:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25603:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25604:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25605:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25606:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25607:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25608:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25609:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25610:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25611:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25612:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25613:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25614:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25615:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25616:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25617:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25618:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25619:

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

.. _no-25620:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25621:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25622:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25623:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25624:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25625:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25626:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25627:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25628:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25629:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25630:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25631:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-25632:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25633:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25634:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25635:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25636:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25637:

**Value** 

Specifies the current state of the control (the value of the field).  (varies)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25638:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25639:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25640:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25641:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-25642>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-25643>`                 Occurs after the control or form is created.
:ref:`Destroy <no-25644>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-25645>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-25646>`               Occurs when the control gets the focus.
:ref:`Idle <no-25647>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-25648>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-25649>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-25650>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-25651>`               
:ref:`KeyUp <no-25652>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-25653>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-25654>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-25655>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-25656>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-25657>`             
:ref:`MouseLeave <no-25658>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-25659>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-25660>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-25661>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-25662>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-25663>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-25664>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-25665>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-25666>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-25667>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-25668>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-25669>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-25670>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-25671>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-25672>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-25673>`                   Occurs when the control's position changes.
:ref:`Paint <no-25674>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-25675>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-25676>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-25677>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-25678>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-25679>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-25642:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-25643:

**Create** 

Occurs after the control or form is created.



-------

.. _no-25644:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-25645:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-25646:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-25647:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-25648:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-25649:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-25650:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-25651:

**KeyEvent** 



-------

.. _no-25652:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-25653:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-25654:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-25655:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-25656:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-25657:

**MouseEvent** 



-------

.. _no-25658:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-25659:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-25660:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-25661:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-25662:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-25663:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-25664:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-25665:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-25666:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-25667:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-25668:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-25669:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-25670:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-25671:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-25672:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-25673:

**Move** 

Occurs when the control's position changes.



-------

.. _no-25674:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-25675:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-25676:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-25677:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-25678:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-25679:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-25680>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-25681>`             Instantiate object as a child of self.
:ref:`afterInit <no-25682>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-25683>`          
:ref:`afterSetProperties <no-25684>`    
:ref:`autoBindEvents <no-25685>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-25686>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-25687>`   
:ref:`bindEvent <no-25688>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-25689>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-25690>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-25691>`          Makes this object topmost
:ref:`clear <no-25692>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-25693>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-25694>`  Given a position relative to this control, return a position relative
:ref:`copy <no-25695>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-25696>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-25697>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-25698>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-25699>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-25700>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-25701>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-25702>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-25703>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-25704>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-25705>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-25706>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-25707>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-25708>`              Draws text on the object at the specified position
:ref:`endHover <no-25709>`              
:ref:`fitToSizer <no-25710>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-25711>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-25712>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-25713>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-25714>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-25715>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-25716>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-25717>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-25718>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-25719>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-25720>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-25721>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-25722>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-25723>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-25724>`      
:ref:`getSizerProp <no-25725>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-25726>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-25727>`                  Make the object invisible.
:ref:`initEvents <no-25728>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-25729>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-25730>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-25731>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-25732>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-25733>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-25734>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-25735>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-25736>`               
:ref:`paste <no-25737>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-25738>`           
:ref:`processDroppedFiles <no-25739>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-25740>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-25741>`            Raise the passed Dabo event.
:ref:`reCreate <no-25742>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-25743>`              Recreate the object.
:ref:`redraw <no-25744>`                Called when the object is (re)drawn.
:ref:`refresh <no-25745>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-25746>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-25747>`               Destroys the object.
:ref:`removeDrawnObject <no-25748>`     
:ref:`restoreValue <no-25749>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-25750>`             Save control's value to dApp's user settings table.
:ref:`select <no-25751>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-25752>`             Select all text in the control.
:ref:`selectNone <no-25753>`            Select no text in the control.
:ref:`sendToBack <no-25754>`            Places this object behind all others.
:ref:`setAll <no-25755>`                Set all child object properties to the passed value.
:ref:`setFocus <no-25756>`              Sets focus to the object.
:ref:`setPositionInSizer <no-25757>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-25758>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-25759>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-25760>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-25761>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-25762>`                  Make the object visible.
:ref:`showContainingPage <no-25763>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-25764>`       Display a context menu (popup) at the specified position.
:ref:`super <no-25765>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-25766>`           Remove a previously registered event binding.
:ref:`unbindKey <no-25767>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-25768>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-25769>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-25770>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-25751:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.select(self, position, length)

   Select all text from <position> for <length> or end of string.



-------

.. _no-25752:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.selectAll(self)

   Select all text in the control.



-------

.. _no-25753:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.selectNone(self)

   Select no text in the control.



-------


Methods - inherited
=====================

.. _no-25680:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25681:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-25682:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25683:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25684:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25685:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.autoBindEvents(self, force=True)
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

.. _no-25686:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25687:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25688:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25689:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25690:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-25691:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25692:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25693:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25694:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25695:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25696:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25697:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25698:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25699:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-25700:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25701:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25702:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25703:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25704:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25705:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25706:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25707:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25708:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25709:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25710:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25711:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25712:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25713:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25714:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25715:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25716:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25717:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25718:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25719:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25720:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25721:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25722:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25723:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-25724:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25725:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25726:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25727:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25728:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25729:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25730:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25731:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25732:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.lockDisplay(self)
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

.. _no-25733:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25734:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25735:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25736:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25737:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25738:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25739:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25740:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25741:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25742:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25743:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25744:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25745:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25746:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25747:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25748:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25749:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25750:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-25754:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25755:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-25756:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25757:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25758:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-25759:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-25760:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25761:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25762:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25763:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25764:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25765:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25766:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25767:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25768:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25769:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25770:

.. function:: dabo.ui.uiwx.dDataControlMixin.dDataControlMixin.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
