
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dTimer

.. _dabo.ui.uiwx.dTimer.dTimer:

======================================
|doc_title|  **dTimer.dTimer** - class
======================================

Creates a timer, for causing something to happen at regular intervals.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dTimer**

.. inheritance-diagram:: dTimer


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dEditor.StyleTimer`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dTimer.dTimer

   .. automethod:: dabo.ui.uiwx.dTimer.dTimer.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-10565>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-10566>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-10567>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-10568>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-10569>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-10570>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-10571>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-10572>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-10573>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-10574>`                The caption of the object. (str)
:ref:`Children <no-10575>`               Returns a list of object references to the children of
:ref:`Class <no-10576>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-10577>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-10578>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-10579>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-10580>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-10581>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-10582>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-10583>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-10584>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-10585>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-10586>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-10587>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-10588>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-10589>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-10590>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-10591>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-10592>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-10593>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-10594>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-10595>`          Dynamically determine the value of the Height property.
:ref:`DynamicInterval <no-10596>`        Dynamically determine the value of the Interval property.
:ref:`DynamicLeft <no-10597>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-10598>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-10599>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-10600>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-10601>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-10602>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-10603>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-10604>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-10605>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-10606>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-10607>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-10608>`                Alternative means of starting/stopping the timer, or determining
:ref:`Font <no-10609>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-10610>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-10611>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-10612>`               Specifies the font face. (str)
:ref:`FontInfo <no-10613>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-10614>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-10615>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-10616>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-10617>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-10618>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-10619>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-10620>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-10621>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Interval <no-10622>`               Specifies the timer interval (milliseconds).
:ref:`Left <no-10623>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-10624>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-10625>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-10626>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-10627>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-10628>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-10629>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-10630>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-10631>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-10632>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-10633>`               Specifies the base name of the object.
:ref:`Parent <no-10634>`                 The containing object. (obj)
:ref:`Position <no-10635>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-10636>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-10637>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-10638>`                  The position of the right side of the object. This is a
:ref:`Size <no-10639>`                   The size of the object. (tuple)
:ref:`Sizer <no-10640>`                  The sizer for the object.
:ref:`StatusText <no-10641>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-10642>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-10643>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-10644>`                    The top position of the object. (int)
:ref:`Transparency <no-10645>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-10646>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-10647>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-10648>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-10649>`                  The width of the object. (int)
:ref:`WindowHandle <no-10650>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-10596:

**DynamicInterval** 

Dynamically determine the value of the Interval property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Interval property. If DynamicInterval is set to None (the default), Interval
will not be dynamically evaluated.



-------

.. _no-10622:

**Interval** 

Specifies the timer interval (milliseconds).



-------


Properties - inherited
========================

.. _no-10565:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10566:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10567:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10568:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10569:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10570:

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

.. _no-10571:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10572:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10573:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10574:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10575:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10576:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10577:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10578:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10579:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10580:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10581:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10582:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10583:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10584:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10585:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10586:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10587:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10588:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10589:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10590:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10591:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10592:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10593:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10594:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10595:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10597:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10598:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10599:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10600:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10601:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10602:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10603:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10604:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10605:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10606:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10607:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10608:

**Enabled** 

Alternative means of starting/stopping the timer, or determining
    its status. If Enabled is set to True and the timer has a positive value
    for its Interval, the timer will be started.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10609:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10610:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10611:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10612:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10613:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10614:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10615:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10616:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10617:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10618:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10619:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10620:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10621:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10623:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10624:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10625:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10626:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10627:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10628:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10629:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10630:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10631:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10632:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10633:

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

.. _no-10634:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10635:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10636:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10637:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10638:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10639:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10640:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10641:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10642:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10643:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10644:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10645:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10646:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10647:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10648:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10649:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10650:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-10651>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-10652>`                 Occurs after the control or form is created.
:ref:`Destroy <no-10653>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-10654>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-10655>`               Occurs when the control gets the focus.
:ref:`Hit <no-10656>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-10657>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-10658>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-10659>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-10660>`               
:ref:`KeyUp <no-10661>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-10662>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-10663>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-10664>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-10665>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-10666>`             
:ref:`MouseLeave <no-10667>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-10668>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-10669>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-10670>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-10671>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-10672>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-10673>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-10674>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-10675>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-10676>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-10677>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-10678>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-10679>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-10680>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-10681>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-10682>`                   Occurs when the control's position changes.
:ref:`Paint <no-10683>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-10684>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-10685>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-10686>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-10687>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-10651:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-10652:

**Create** 

Occurs after the control or form is created.



-------

.. _no-10653:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-10654:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-10655:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-10656:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-10657:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-10658:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-10659:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-10660:

**KeyEvent** 



-------

.. _no-10661:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-10662:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-10663:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-10664:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-10665:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-10666:

**MouseEvent** 



-------

.. _no-10667:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-10668:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-10669:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-10670:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-10671:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-10672:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-10673:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-10674:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-10675:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-10676:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-10677:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-10678:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-10679:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-10680:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-10681:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-10682:

**Move** 

Occurs when the control's position changes.



-------

.. _no-10683:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-10684:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-10685:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-10686:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-10687:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-10688>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-10689>`             Instantiate object as a child of self.
:ref:`afterInit <no-10690>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-10691>`          
:ref:`afterSetProperties <no-10692>`    
:ref:`autoBindEvents <no-10693>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-10694>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-10695>`   
:ref:`bindEvent <no-10696>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-10697>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-10698>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-10699>`          Makes this object topmost
:ref:`clear <no-10700>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-10701>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-10702>`  Given a position relative to this control, return a position relative
:ref:`copy <no-10703>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-10704>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-10705>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-10706>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-10707>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-10708>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-10709>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-10710>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-10711>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-10712>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-10713>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-10714>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-10715>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-10716>`              Draws text on the object at the specified position
:ref:`endHover <no-10717>`              
:ref:`fitToSizer <no-10718>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-10719>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-10720>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-10721>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-10722>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-10723>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-10724>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-10725>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-10726>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-10727>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-10728>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-10729>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-10730>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-10731>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-10732>`                  Make the object invisible.
:ref:`initEvents <no-10733>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-10734>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-10735>`         Returns True if the containership hierarchy for this control
:ref:`isRunning <no-10736>`             
:ref:`iterateCall <no-10737>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-10738>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-10739>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-10740>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-10741>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-10742>`               
:ref:`paste <no-10743>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-10744>`           
:ref:`processDroppedFiles <no-10745>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-10746>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-10747>`            Raise the passed Dabo event.
:ref:`reCreate <no-10748>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-10749>`              Recreate the object.
:ref:`redraw <no-10750>`                Called when the object is (re)drawn.
:ref:`refresh <no-10751>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-10752>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-10753>`               Make sure that the timer is stopped first
:ref:`removeDrawnObject <no-10754>`     
:ref:`sendToBack <no-10755>`            Places this object behind all others.
:ref:`setAll <no-10756>`                Set all child object properties to the passed value.
:ref:`setFocus <no-10757>`              Sets focus to the object.
:ref:`setPositionInSizer <no-10758>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-10759>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-10760>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-10761>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-10762>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-10763>`                  Make the object visible.
:ref:`showContainingPage <no-10764>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-10765>`       Display a context menu (popup) at the specified position.
:ref:`start <no-10766>`                 
:ref:`stop <no-10767>`                  
:ref:`super <no-10768>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-10769>`           Remove a previously registered event binding.
:ref:`unbindKey <no-10770>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-10771>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-10772>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-10773>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-10736:

.. function:: dabo.ui.uiwx.dTimer.dTimer.isRunning(self)



-------

.. _no-10753:

.. function:: dabo.ui.uiwx.dTimer.dTimer.release(self)

   Make sure that the timer is stopped first



-------

.. _no-10766:

.. function:: dabo.ui.uiwx.dTimer.dTimer.start(self, interval=-1)



-------

.. _no-10767:

.. function:: dabo.ui.uiwx.dTimer.dTimer.stop(self)



-------


Methods - inherited
=====================

.. _no-10688:

.. function:: dabo.ui.uiwx.dTimer.dTimer.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10689:

.. function:: dabo.ui.uiwx.dTimer.dTimer.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-10690:

.. function:: dabo.ui.uiwx.dTimer.dTimer.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10691:

.. function:: dabo.ui.uiwx.dTimer.dTimer.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10692:

.. function:: dabo.ui.uiwx.dTimer.dTimer.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10693:

.. function:: dabo.ui.uiwx.dTimer.dTimer.autoBindEvents(self, force=True)
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

.. _no-10694:

.. function:: dabo.ui.uiwx.dTimer.dTimer.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10695:

.. function:: dabo.ui.uiwx.dTimer.dTimer.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10696:

.. function:: dabo.ui.uiwx.dTimer.dTimer.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10697:

.. function:: dabo.ui.uiwx.dTimer.dTimer.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10698:

.. function:: dabo.ui.uiwx.dTimer.dTimer.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-10699:

.. function:: dabo.ui.uiwx.dTimer.dTimer.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10700:

.. function:: dabo.ui.uiwx.dTimer.dTimer.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10701:

.. function:: dabo.ui.uiwx.dTimer.dTimer.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10702:

.. function:: dabo.ui.uiwx.dTimer.dTimer.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10703:

.. function:: dabo.ui.uiwx.dTimer.dTimer.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10704:

.. function:: dabo.ui.uiwx.dTimer.dTimer.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10705:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10706:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10707:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-10708:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10709:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10710:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10711:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10712:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10713:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10714:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10715:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10716:

.. function:: dabo.ui.uiwx.dTimer.dTimer.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10717:

.. function:: dabo.ui.uiwx.dTimer.dTimer.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10718:

.. function:: dabo.ui.uiwx.dTimer.dTimer.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10719:

.. function:: dabo.ui.uiwx.dTimer.dTimer.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10720:

.. function:: dabo.ui.uiwx.dTimer.dTimer.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10721:

.. function:: dabo.ui.uiwx.dTimer.dTimer.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10722:

.. function:: dabo.ui.uiwx.dTimer.dTimer.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10723:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10724:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10725:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10726:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10727:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10728:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10729:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-10730:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10731:

.. function:: dabo.ui.uiwx.dTimer.dTimer.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10732:

.. function:: dabo.ui.uiwx.dTimer.dTimer.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10733:

.. function:: dabo.ui.uiwx.dTimer.dTimer.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10734:

.. function:: dabo.ui.uiwx.dTimer.dTimer.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10735:

.. function:: dabo.ui.uiwx.dTimer.dTimer.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10737:

.. function:: dabo.ui.uiwx.dTimer.dTimer.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10738:

.. function:: dabo.ui.uiwx.dTimer.dTimer.lockDisplay(self)
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

.. _no-10739:

.. function:: dabo.ui.uiwx.dTimer.dTimer.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10740:

.. function:: dabo.ui.uiwx.dTimer.dTimer.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10741:

.. function:: dabo.ui.uiwx.dTimer.dTimer.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10742:

.. function:: dabo.ui.uiwx.dTimer.dTimer.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10743:

.. function:: dabo.ui.uiwx.dTimer.dTimer.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10744:

.. function:: dabo.ui.uiwx.dTimer.dTimer.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10745:

.. function:: dabo.ui.uiwx.dTimer.dTimer.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10746:

.. function:: dabo.ui.uiwx.dTimer.dTimer.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10747:

.. function:: dabo.ui.uiwx.dTimer.dTimer.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10748:

.. function:: dabo.ui.uiwx.dTimer.dTimer.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10749:

.. function:: dabo.ui.uiwx.dTimer.dTimer.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10750:

.. function:: dabo.ui.uiwx.dTimer.dTimer.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10751:

.. function:: dabo.ui.uiwx.dTimer.dTimer.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10752:

.. function:: dabo.ui.uiwx.dTimer.dTimer.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10754:

.. function:: dabo.ui.uiwx.dTimer.dTimer.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10755:

.. function:: dabo.ui.uiwx.dTimer.dTimer.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10756:

.. function:: dabo.ui.uiwx.dTimer.dTimer.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-10757:

.. function:: dabo.ui.uiwx.dTimer.dTimer.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10758:

.. function:: dabo.ui.uiwx.dTimer.dTimer.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10759:

.. function:: dabo.ui.uiwx.dTimer.dTimer.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-10760:

.. function:: dabo.ui.uiwx.dTimer.dTimer.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-10761:

.. function:: dabo.ui.uiwx.dTimer.dTimer.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10762:

.. function:: dabo.ui.uiwx.dTimer.dTimer.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10763:

.. function:: dabo.ui.uiwx.dTimer.dTimer.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10764:

.. function:: dabo.ui.uiwx.dTimer.dTimer.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10765:

.. function:: dabo.ui.uiwx.dTimer.dTimer.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10768:

.. function:: dabo.ui.uiwx.dTimer.dTimer.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10769:

.. function:: dabo.ui.uiwx.dTimer.dTimer.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10770:

.. function:: dabo.ui.uiwx.dTimer.dTimer.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10771:

.. function:: dabo.ui.uiwx.dTimer.dTimer.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10772:

.. function:: dabo.ui.uiwx.dTimer.dTimer.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10773:

.. function:: dabo.ui.uiwx.dTimer.dTimer.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
