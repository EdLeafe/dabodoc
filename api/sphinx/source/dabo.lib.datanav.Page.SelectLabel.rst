
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.SelectLabel:

=========================================
|doc_title|  **Page.SelectLabel** - class
=========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SelectLabel**

.. inheritance-diagram:: SelectLabel


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.datanav.Page.SelectControlMixin`
* :ref:`dabo.ui.uiwx.dLabel.dLabel`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.SelectLabel


|method_summary| Properties Summary
===================================


======================================= ========================
:ref:`Application <no-3706>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoResize <no-3707>`             Specifies whether the length of the caption determines
:ref:`BackColor <no-3708>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-3709>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-3710>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-3711>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-3712>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-3713>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-3714>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-3715>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-3716>`                The caption of the object. (str)
:ref:`Children <no-3717>`               Returns a list of object references to the children of
:ref:`Class <no-3718>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-3719>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-3720>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-3721>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-3722>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-3723>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-3724>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-3725>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-3726>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-3727>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-3728>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-3729>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-3730>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-3731>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-3732>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-3733>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-3734>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-3735>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-3736>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-3737>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-3738>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-3739>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-3740>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-3741>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-3742>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-3743>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-3744>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-3745>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-3746>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-3747>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-3748>`           Dynamically determine the value of the Width property.
:ref:`DynamicWordWrap <no-3749>`        Dynamically determine the value of the WordWrap property.
:ref:`Enabled <no-3750>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-3751>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-3752>`               Sets the Bold of the Font (int)
:ref:`FontDescription <no-3753>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-3754>`               Sets the face of the Font (int)
:ref:`FontInfo <no-3755>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-3756>`             Sets the Italic of the Font (int)
:ref:`FontSize <no-3757>`               Sets the size of the Font (int)
:ref:`FontUnderline <no-3758>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-3759>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-3760>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-3761>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-3762>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-3763>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-3764>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-3765>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-3766>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-3767>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-3768>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-3769>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-3770>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-3771>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-3772>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-3773>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-3774>`               Specifies the base name of the object.
:ref:`Parent <no-3775>`                 The containing object. (obj)
:ref:`Position <no-3776>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-3777>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-3778>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-3779>`                  The position of the right side of the object. This is a
:ref:`Size <no-3780>`                   The size of the object. (tuple)
:ref:`Sizer <no-3781>`                  The sizer for the object.
:ref:`StatusText <no-3782>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-3783>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-3784>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-3785>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-3786>`                    The top position of the object. (int)
:ref:`Transparency <no-3787>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-3788>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-3789>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-3790>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-3791>`                  The width of the object. (int)
:ref:`WindowHandle <no-3792>`           The platform-specific handle for the window. Read-only. (long)
:ref:`WordWrap <no-3793>`               When True, the Caption is wrapped to the Width. Note

======================================= ========================


Properties - inherited
========================

.. _no-3706:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3707:

**AutoResize** 

Specifies whether the length of the caption determines
    the size of the label. This cannot be True if WordWrap is
    also set to True. Default=True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dLabel.dLabel`

-------

.. _no-3708:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3709:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3710:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3711:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3712:

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

.. _no-3713:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3714:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3715:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3716:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3717:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3718:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3719:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3720:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3721:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3722:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3723:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3724:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3725:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3726:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3727:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3728:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3729:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3730:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3731:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3732:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3733:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3734:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3735:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3736:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3737:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3738:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3739:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3740:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3741:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3742:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3743:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3744:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3745:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3746:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3747:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3748:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3749:

**DynamicWordWrap** 

Dynamically determine the value of the WordWrap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WordWrap property. If DynamicWordWrap is set to None (the default), WordWrap
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dLabel.dLabel`

-------

.. _no-3750:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3751:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3752:

**FontBold** 

Sets the Bold of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3753:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3754:

**FontFace** 

Sets the face of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3755:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3756:

**FontItalic** 

Sets the Italic of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3757:

**FontSize** 

Sets the size of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3758:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3759:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3760:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3761:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3762:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3763:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3764:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3765:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3766:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3767:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3768:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3769:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3770:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3771:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3772:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3773:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3774:

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

.. _no-3775:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3776:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3777:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3778:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3779:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3780:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3781:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3782:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3783:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-3784:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3785:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3786:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3787:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3788:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3789:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3790:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3791:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3792:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3793:

**WordWrap** 

When True, the Caption is wrapped to the Width. Note
    that the control must have sufficient Height to display any
    wrapped text.
    Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dLabel.dLabel`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-3794>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-3795>`                 Occurs after the control or form is created.
:ref:`Destroy <no-3796>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-3797>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-3798>`               Occurs when the control gets the focus.
:ref:`Idle <no-3799>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-3800>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-3801>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-3802>`               
:ref:`KeyUp <no-3803>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-3804>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-3805>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-3806>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-3807>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-3808>`             
:ref:`MouseLeave <no-3809>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-3810>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-3811>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-3812>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-3813>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-3814>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-3815>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-3816>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-3817>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-3818>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-3819>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-3820>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-3821>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-3822>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-3823>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-3824>`                   Occurs when the control's position changes.
:ref:`Paint <no-3825>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-3826>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-3827>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-3828>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-3829>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-3794:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-3795:

**Create** 

Occurs after the control or form is created.



-------

.. _no-3796:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-3797:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-3798:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-3799:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-3800:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-3801:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-3802:

**KeyEvent** 



-------

.. _no-3803:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-3804:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-3805:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-3806:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-3807:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-3808:

**MouseEvent** 



-------

.. _no-3809:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-3810:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-3811:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-3812:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-3813:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-3814:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-3815:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-3816:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-3817:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-3818:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-3819:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-3820:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-3821:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-3822:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-3823:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-3824:

**Move** 

Occurs when the control's position changes.



-------

.. _no-3825:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-3826:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-3827:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-3828:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-3829:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-3830>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-3831>`             Instantiate object as a child of self.
:ref:`afterInit <no-3832>`             
:ref:`afterInitAll <no-3833>`          
:ref:`afterSetProperties <no-3834>`    
:ref:`autoBindEvents <no-3835>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-3836>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-3837>`   
:ref:`bindEvent <no-3838>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-3839>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-3840>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-3841>`          Makes this object topmost
:ref:`clear <no-3842>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-3843>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-3844>`  Given a position relative to this control, return a position relative
:ref:`copy <no-3845>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-3846>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-3847>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-3848>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-3849>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-3850>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-3851>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-3852>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-3853>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-3854>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-3855>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-3856>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-3857>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-3858>`              Draws text on the object at the specified position
:ref:`endHover <no-3859>`              
:ref:`fitToSizer <no-3860>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-3861>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-3862>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-3863>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-3864>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-3865>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-3866>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-3867>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-3868>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-3869>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-3870>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-3871>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-3872>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-3873>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-3874>`                  Make the object invisible.
:ref:`initEvents <no-3875>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-3876>`        
:ref:`isContainedBy <no-3877>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-3878>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-3879>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-3880>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-3881>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-3882>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-3883>`               
:ref:`paste <no-3884>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-3885>`           
:ref:`processDroppedFiles <no-3886>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-3887>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-3888>`            Raise the passed Dabo event.
:ref:`reCreate <no-3889>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-3890>`              Recreate the object.
:ref:`redraw <no-3891>`                Called when the object is (re)drawn.
:ref:`refresh <no-3892>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-3893>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-3894>`               Destroys the object.
:ref:`removeDrawnObject <no-3895>`     
:ref:`sendToBack <no-3896>`            Places this object behind all others.
:ref:`setAll <no-3897>`                Set all child object properties to the passed value.
:ref:`setFocus <no-3898>`              Sets focus to the object.
:ref:`setPositionInSizer <no-3899>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-3900>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-3901>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-3902>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-3903>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-3904>`                  Make the object visible.
:ref:`showContainingPage <no-3905>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-3906>`       Display a context menu (popup) at the specified position.
:ref:`super <no-3907>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-3908>`           Remove a previously registered event binding.
:ref:`unbindKey <no-3909>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-3910>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-3911>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-3912>`                Update the properties of this object and all contained objects.

====================================== ========================


Methods
=======

.. _no-3832:

.. function:: dabo.lib.datanav.Page.SelectLabel.afterInit(self)



-------


Methods - inherited
=====================

.. _no-3830:

.. function:: dabo.lib.datanav.Page.SelectLabel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3831:

.. function:: dabo.lib.datanav.Page.SelectLabel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-3833:

.. function:: dabo.lib.datanav.Page.SelectLabel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3834:

.. function:: dabo.lib.datanav.Page.SelectLabel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3835:

.. function:: dabo.lib.datanav.Page.SelectLabel.autoBindEvents(self, force=True)
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

.. _no-3836:

.. function:: dabo.lib.datanav.Page.SelectLabel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3837:

.. function:: dabo.lib.datanav.Page.SelectLabel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3838:

.. function:: dabo.lib.datanav.Page.SelectLabel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3839:

.. function:: dabo.lib.datanav.Page.SelectLabel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3840:

.. function:: dabo.lib.datanav.Page.SelectLabel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-3841:

.. function:: dabo.lib.datanav.Page.SelectLabel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3842:

.. function:: dabo.lib.datanav.Page.SelectLabel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3843:

.. function:: dabo.lib.datanav.Page.SelectLabel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3844:

.. function:: dabo.lib.datanav.Page.SelectLabel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3845:

.. function:: dabo.lib.datanav.Page.SelectLabel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3846:

.. function:: dabo.lib.datanav.Page.SelectLabel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3847:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3848:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3849:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-3850:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3851:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3852:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3853:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3854:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3855:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3856:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3857:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3858:

.. function:: dabo.lib.datanav.Page.SelectLabel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3859:

.. function:: dabo.lib.datanav.Page.SelectLabel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3860:

.. function:: dabo.lib.datanav.Page.SelectLabel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3861:

.. function:: dabo.lib.datanav.Page.SelectLabel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3862:

.. function:: dabo.lib.datanav.Page.SelectLabel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3863:

.. function:: dabo.lib.datanav.Page.SelectLabel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3864:

.. function:: dabo.lib.datanav.Page.SelectLabel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3865:

.. function:: dabo.lib.datanav.Page.SelectLabel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3866:

.. function:: dabo.lib.datanav.Page.SelectLabel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3867:

.. function:: dabo.lib.datanav.Page.SelectLabel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3868:

.. function:: dabo.lib.datanav.Page.SelectLabel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3869:

.. function:: dabo.lib.datanav.Page.SelectLabel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3870:

.. function:: dabo.lib.datanav.Page.SelectLabel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3871:

.. function:: dabo.lib.datanav.Page.SelectLabel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-3872:

.. function:: dabo.lib.datanav.Page.SelectLabel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3873:

.. function:: dabo.lib.datanav.Page.SelectLabel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3874:

.. function:: dabo.lib.datanav.Page.SelectLabel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3875:

.. function:: dabo.lib.datanav.Page.SelectLabel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3876:

.. function:: dabo.lib.datanav.Page.SelectLabel.initProperties(self)
   :noindex:



Inherited from: :ref:`dabo.lib.datanav.Page.SelectControlMixin`

-------

.. _no-3877:

.. function:: dabo.lib.datanav.Page.SelectLabel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3878:

.. function:: dabo.lib.datanav.Page.SelectLabel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3879:

.. function:: dabo.lib.datanav.Page.SelectLabel.lockDisplay(self)
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

.. _no-3880:

.. function:: dabo.lib.datanav.Page.SelectLabel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3881:

.. function:: dabo.lib.datanav.Page.SelectLabel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3882:

.. function:: dabo.lib.datanav.Page.SelectLabel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3883:

.. function:: dabo.lib.datanav.Page.SelectLabel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3884:

.. function:: dabo.lib.datanav.Page.SelectLabel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3885:

.. function:: dabo.lib.datanav.Page.SelectLabel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3886:

.. function:: dabo.lib.datanav.Page.SelectLabel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3887:

.. function:: dabo.lib.datanav.Page.SelectLabel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3888:

.. function:: dabo.lib.datanav.Page.SelectLabel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3889:

.. function:: dabo.lib.datanav.Page.SelectLabel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3890:

.. function:: dabo.lib.datanav.Page.SelectLabel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3891:

.. function:: dabo.lib.datanav.Page.SelectLabel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3892:

.. function:: dabo.lib.datanav.Page.SelectLabel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3893:

.. function:: dabo.lib.datanav.Page.SelectLabel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3894:

.. function:: dabo.lib.datanav.Page.SelectLabel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3895:

.. function:: dabo.lib.datanav.Page.SelectLabel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3896:

.. function:: dabo.lib.datanav.Page.SelectLabel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3897:

.. function:: dabo.lib.datanav.Page.SelectLabel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-3898:

.. function:: dabo.lib.datanav.Page.SelectLabel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3899:

.. function:: dabo.lib.datanav.Page.SelectLabel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3900:

.. function:: dabo.lib.datanav.Page.SelectLabel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-3901:

.. function:: dabo.lib.datanav.Page.SelectLabel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-3902:

.. function:: dabo.lib.datanav.Page.SelectLabel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3903:

.. function:: dabo.lib.datanav.Page.SelectLabel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3904:

.. function:: dabo.lib.datanav.Page.SelectLabel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3905:

.. function:: dabo.lib.datanav.Page.SelectLabel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3906:

.. function:: dabo.lib.datanav.Page.SelectLabel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3907:

.. function:: dabo.lib.datanav.Page.SelectLabel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3908:

.. function:: dabo.lib.datanav.Page.SelectLabel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3909:

.. function:: dabo.lib.datanav.Page.SelectLabel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3910:

.. function:: dabo.lib.datanav.Page.SelectLabel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3911:

.. function:: dabo.lib.datanav.Page.SelectLabel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3912:

.. function:: dabo.lib.datanav.Page.SelectLabel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
