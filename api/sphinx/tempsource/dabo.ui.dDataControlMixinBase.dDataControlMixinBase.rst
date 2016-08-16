
.. include:: _static/headings.txt

.. module:: dabo.ui.dDataControlMixinBase

.. _dabo.ui.dDataControlMixinBase.dDataControlMixinBase:

====================================================================
|doc_title|  **dDataControlMixinBase.dDataControlMixinBase** - class
====================================================================

Provide common functionality for the data-aware controls.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDataControlMixinBase**

.. inheritance-diagram:: dDataControlMixinBase


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase

   .. automethod:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-6558>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-6559>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-6560>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-6561>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-6562>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-6563>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-6564>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-6565>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-6566>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-6567>`                  The caption of the object. (str)
:ref:`Children <no-6568>`                 Returns a list of object references to the children of
:ref:`Class <no-6569>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-6570>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-6571>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-6572>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-6573>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-6574>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-6575>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-6576>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-6577>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-6578>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-6579>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-6580>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-6581>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-6582>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-6583>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-6584>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-6585>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-6586>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-6587>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-6588>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-6589>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-6590>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-6591>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-6592>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-6593>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-6594>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-6595>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-6596>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-6597>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-6598>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-6599>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-6600>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-6601>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-6602>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-6603>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-6604>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-6605>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-6606>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-6607>`                 Specifies the font face. (str)
:ref:`FontInfo <no-6608>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-6609>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-6610>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-6611>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-6612>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-6613>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-6614>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-6615>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-6616>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-6617>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-6618>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-6619>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-6620>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-6621>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-6622>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-6623>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-6624>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-6625>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-6626>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-6627>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-6628>`                 Specifies the base name of the object.
:ref:`Parent <no-6629>`                   The containing object. (obj)
:ref:`PersistSecretData <no-6630>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-6631>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-6632>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-6633>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-6634>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-6635>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-6636>`                     The size of the object. (tuple)
:ref:`Sizer <no-6637>`                    The sizer for the object.
:ref:`Source <no-6638>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-6639>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-6640>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-6641>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-6642>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-6643>`                      The top position of the object. (int)
:ref:`Transparency <no-6644>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-6645>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-6646>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-6647>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-6648>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-6649>`                    The width of the object. (int)
:ref:`WindowHandle <no-6650>`             The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-6572:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)



-------

.. _no-6573:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)



-------

.. _no-6574:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)



-------

.. _no-6617:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)



-------

.. _no-6630:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)



-------

.. _no-6635:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)



-------

.. _no-6638:

**Source** 

Reference to the object to which this control's Value is bound  (object)



-------

.. _no-6646:

**Value** 

Specifies the current state of the control (the value of the field). (varies)



-------


Properties - inherited
========================

.. _no-6558:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6559:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6560:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6561:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6562:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6563:

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

.. _no-6564:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6565:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6566:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6567:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6568:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6569:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6570:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6571:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6575:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6576:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6577:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6578:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6579:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6580:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6581:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6582:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6583:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6584:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6585:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6586:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6587:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6588:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6589:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6590:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6591:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6592:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6593:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6594:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6595:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6596:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6597:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6598:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6599:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6600:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6601:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6602:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6603:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6604:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6605:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6606:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6607:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6608:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6609:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6610:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6611:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6612:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6613:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6614:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6615:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6616:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6618:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6619:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6620:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6621:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6622:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6623:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6624:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6625:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6626:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6627:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6628:

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

.. _no-6629:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6631:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6632:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6633:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6634:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6636:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6637:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6639:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6640:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-6641:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6642:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6643:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6644:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6645:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6647:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6648:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6649:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6650:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-6651>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-6652>`                 Occurs after the control or form is created.
:ref:`Destroy <no-6653>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-6654>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-6655>`               Occurs when the control gets the focus.
:ref:`Idle <no-6656>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-6657>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-6658>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-6659>`               
:ref:`KeyUp <no-6660>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-6661>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-6662>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-6663>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-6664>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-6665>`             
:ref:`MouseLeave <no-6666>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-6667>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-6668>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-6669>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-6670>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-6671>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-6672>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-6673>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-6674>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-6675>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-6676>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-6677>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-6678>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-6679>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-6680>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-6681>`                   Occurs when the control's position changes.
:ref:`Paint <no-6682>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-6683>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-6684>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-6685>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-6686>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-6651:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-6652:

**Create** 

Occurs after the control or form is created.



-------

.. _no-6653:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-6654:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-6655:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-6656:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-6657:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-6658:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-6659:

**KeyEvent** 



-------

.. _no-6660:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-6661:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-6662:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-6663:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-6664:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-6665:

**MouseEvent** 



-------

.. _no-6666:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-6667:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-6668:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-6669:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-6670:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-6671:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-6672:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-6673:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-6674:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-6675:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-6676:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-6677:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-6678:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-6679:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-6680:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-6681:

**Move** 

Occurs when the control's position changes.



-------

.. _no-6682:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-6683:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-6684:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-6685:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-6686:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-6687>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-6688>`             Instantiate object as a child of self.
:ref:`afterInit <no-6689>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-6690>`          
:ref:`afterSetProperties <no-6691>`    
:ref:`autoBindEvents <no-6692>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-6693>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-6694>`   
:ref:`bindEvent <no-6695>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-6696>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-6697>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-6698>`          Makes this object topmost
:ref:`clear <no-6699>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-6700>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-6701>`  Given a position relative to this control, return a position relative
:ref:`copy <no-6702>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-6703>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-6704>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-6705>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-6706>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-6707>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-6708>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-6709>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-6710>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-6711>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-6712>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-6713>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-6714>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-6715>`              Draws text on the object at the specified position
:ref:`endHover <no-6716>`              
:ref:`fitToSizer <no-6717>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-6718>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-6719>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-6720>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-6721>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-6722>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-6723>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-6724>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-6725>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-6726>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-6727>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-6728>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-6729>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-6730>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-6731>`      
:ref:`getSizerProp <no-6732>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-6733>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-6734>`                  Make the object invisible.
:ref:`initEvents <no-6735>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-6736>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-6737>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-6738>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-6739>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-6740>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-6741>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-6742>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-6743>`               
:ref:`paste <no-6744>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-6745>`           
:ref:`processDroppedFiles <no-6746>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-6747>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-6748>`            Raise the passed Dabo event.
:ref:`reCreate <no-6749>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-6750>`              Recreate the object.
:ref:`redraw <no-6751>`                Called when the object is (re)drawn.
:ref:`refresh <no-6752>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-6753>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-6754>`               Destroys the object.
:ref:`removeDrawnObject <no-6755>`     
:ref:`restoreValue <no-6756>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-6757>`             Save control's value to dApp's user settings table.
:ref:`select <no-6758>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-6759>`             Select all text in the control.
:ref:`selectNone <no-6760>`            Select no text in the control.
:ref:`sendToBack <no-6761>`            Places this object behind all others.
:ref:`setAll <no-6762>`                Set all child object properties to the passed value.
:ref:`setFocus <no-6763>`              Sets focus to the object.
:ref:`setPositionInSizer <no-6764>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-6765>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-6766>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-6767>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-6768>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-6769>`                  Make the object visible.
:ref:`showContainingPage <no-6770>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-6771>`       Display a context menu (popup) at the specified position.
:ref:`super <no-6772>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-6773>`           Remove a previously registered event binding.
:ref:`unbindKey <no-6774>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-6775>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-6776>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-6777>`                Update control's value to match the current value from the source.

====================================== ========================


Methods
=======

.. _no-6718:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.flushValue(self)

   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   



-------

.. _no-6724:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getBlankValue(self)

   Return the empty value of the control.



-------

.. _no-6731:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getShortDataType(self, value)



-------

.. _no-6756:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.restoreValue(self)

   Set the control's value to the value in dApp's user settings table.



-------

.. _no-6757:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.saveValue(self)

   Save control's value to dApp's user settings table.



-------

.. _no-6758:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.select(self, position, length)

   
   Select all text from <position> for <length> or end of string.
   
   UI lib must override.
   



-------

.. _no-6759:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.selectAll(self)

   
   Select all text in the control.
   
   UI lib must override.
   



-------

.. _no-6760:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.selectNone(self)

   
   Select no text in the control.
   
   UI lib must override.
   



-------

.. _no-6777:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.update(self)

   Update control's value to match the current value from the source.



-------


Methods - inherited
=====================

.. _no-6687:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6688:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-6689:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6690:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6691:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6692:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.autoBindEvents(self, force=True)
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

.. _no-6693:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6694:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6695:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6696:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6697:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-6698:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6699:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6700:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6701:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6702:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6703:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6704:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6705:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6706:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-6707:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6708:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6709:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6710:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6711:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6712:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6713:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6714:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6715:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6716:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6717:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6719:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6720:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6721:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6722:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6723:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6725:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6726:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6727:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6728:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6729:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6730:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-6732:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6733:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6734:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6735:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6736:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6737:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6738:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6739:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.lockDisplay(self)
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

.. _no-6740:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6741:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6742:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6743:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6744:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6745:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6746:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6747:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6748:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6749:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6750:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6751:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6752:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6753:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6754:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6755:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6761:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6762:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-6763:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6764:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6765:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-6766:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-6767:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6768:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6769:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6770:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6771:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6772:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6773:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6774:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6775:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6776:

.. function:: dabo.ui.dDataControlMixinBase.dDataControlMixinBase.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
