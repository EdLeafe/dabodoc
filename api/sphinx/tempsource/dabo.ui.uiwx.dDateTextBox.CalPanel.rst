
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDateTextBox

.. _dabo.ui.uiwx.dDateTextBox.CalPanel:

==============================================
|doc_title|  **dDateTextBox.CalPanel** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **CalPanel**

.. inheritance-diagram:: CalPanel


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dPanel`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDateTextBox.CalPanel

   .. automethod:: dabo.ui.uiwx.dDateTextBox.CalPanel.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-24522>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-24523>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-24524>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-24525>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-24526>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-24527>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-24528>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-24529>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-24530>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-24531>`                The caption of the object. (str)
:ref:`Children <no-24532>`               Returns a list of object references to the children of
:ref:`Class <no-24533>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-24534>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-24535>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-24536>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-24537>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-24538>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-24539>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-24540>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-24541>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-24542>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-24543>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-24544>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-24545>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-24546>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-24547>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-24548>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-24549>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-24550>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-24551>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-24552>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-24553>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-24554>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-24555>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-24556>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-24557>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-24558>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-24559>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-24560>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-24561>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-24562>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-24563>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-24564>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-24565>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-24566>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-24567>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-24568>`               Specifies the font face. (str)
:ref:`FontInfo <no-24569>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-24570>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-24571>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-24572>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-24573>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-24574>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-24575>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-24576>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-24577>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-24578>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-24579>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-24580>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-24581>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-24582>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-24583>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-24584>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-24585>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-24586>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-24587>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-24588>`               Specifies the base name of the object.
:ref:`Parent <no-24589>`                 The containing object. (obj)
:ref:`Position <no-24590>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-24591>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-24592>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-24593>`                  The position of the right side of the object. This is a
:ref:`Size <no-24594>`                   The size of the object. (tuple)
:ref:`Sizer <no-24595>`                  The sizer for the object.
:ref:`StatusText <no-24596>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-24597>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-24598>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-24599>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-24600>`                    The top position of the object. (int)
:ref:`Transparency <no-24601>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-24602>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-24603>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-24604>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-24605>`                  The width of the object. (int)
:ref:`WindowHandle <no-24606>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-24522:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24523:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24524:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24525:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24526:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24527:

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

.. _no-24528:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24529:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24530:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24531:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24532:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24533:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24534:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24535:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24536:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24537:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24538:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24539:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24540:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24541:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24542:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24543:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24544:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24545:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24546:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24547:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24548:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24549:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24550:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24551:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24552:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24553:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24554:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24555:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24556:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24557:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24558:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24559:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24560:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24561:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24562:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24563:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24564:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24565:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24566:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24567:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24568:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24569:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24570:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24571:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24572:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24573:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24574:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24575:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24576:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24577:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24578:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24579:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24580:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24581:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24582:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24583:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24584:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24585:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24586:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24587:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24588:

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

.. _no-24589:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24590:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24591:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24592:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24593:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24594:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24595:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24596:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24597:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-24598:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24599:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24600:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24601:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24602:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24603:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24604:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24605:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24606:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-24607>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-24608>`              Occurs when a child control is created.
:ref:`Create <no-24609>`                 Occurs after the control or form is created.
:ref:`Destroy <no-24610>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-24611>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-24612>`               Occurs when the control gets the focus.
:ref:`Idle <no-24613>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-24614>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-24615>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-24616>`               
:ref:`KeyUp <no-24617>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-24618>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-24619>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-24620>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-24621>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-24622>`             
:ref:`MouseLeave <no-24623>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-24624>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-24625>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-24626>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-24627>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-24628>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-24629>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-24630>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-24631>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-24632>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-24633>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-24634>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-24635>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-24636>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-24637>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-24638>`                   Occurs when the control's position changes.
:ref:`Paint <no-24639>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-24640>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-24641>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-24642>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-24643>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-24607:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-24608:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-24609:

**Create** 

Occurs after the control or form is created.



-------

.. _no-24610:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-24611:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-24612:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-24613:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-24614:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-24615:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-24616:

**KeyEvent** 



-------

.. _no-24617:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-24618:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-24619:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-24620:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-24621:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-24622:

**MouseEvent** 



-------

.. _no-24623:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-24624:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-24625:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-24626:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-24627:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-24628:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-24629:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-24630:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-24631:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-24632:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-24633:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-24634:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-24635:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-24636:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-24637:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-24638:

**Move** 

Occurs when the control's position changes.



-------

.. _no-24639:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-24640:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-24641:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-24642:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-24643:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-24644>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-24645>`             Instantiate object as a child of self.
:ref:`afterInit <no-24646>`             Create the calendar control, and resize this panel
:ref:`afterInitAll <no-24647>`          
:ref:`afterSetProperties <no-24648>`    
:ref:`autoBindEvents <no-24649>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-24650>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-24651>`   
:ref:`bindEvent <no-24652>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-24653>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-24654>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-24655>`          Makes this object topmost
:ref:`clear <no-24656>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-24657>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-24658>`  Given a position relative to this control, return a position relative
:ref:`copy <no-24659>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-24660>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-24661>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-24662>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-24663>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-24664>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-24665>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-24666>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-24667>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-24668>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-24669>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-24670>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-24671>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-24672>`              Draws text on the object at the specified position
:ref:`endHover <no-24673>`              
:ref:`fitToSizer <no-24674>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-24675>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-24676>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-24677>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-24678>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-24679>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-24680>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-24681>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-24682>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-24683>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-24684>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-24685>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-24686>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-24687>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-24688>`                  Make the object invisible.
:ref:`initEvents <no-24689>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-24690>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-24691>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-24692>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-24693>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-24694>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-24695>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-24696>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-24697>`     Given a position relative to the form, return a position relative
:ref:`onCalKey <no-24698>`              
:ref:`onCalSelection <no-24699>`        
:ref:`onHover <no-24700>`               
:ref:`paste <no-24701>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-24702>`           
:ref:`processDroppedFiles <no-24703>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-24704>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-24705>`            Raise the passed Dabo event.
:ref:`reCreate <no-24706>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-24707>`              Recreate the object.
:ref:`redraw <no-24708>`                Called when the object is (re)drawn.
:ref:`refresh <no-24709>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-24710>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-24711>`               Destroys the object.
:ref:`removeDrawnObject <no-24712>`     
:ref:`sendToBack <no-24713>`            Places this object behind all others.
:ref:`setAll <no-24714>`                Set all child object properties to the passed value.
:ref:`setFocus <no-24715>`              Sets focus to the object.
:ref:`setPositionInSizer <no-24716>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-24717>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-24718>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-24719>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-24720>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-24721>`                  Make the object visible.
:ref:`showContainingPage <no-24722>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-24723>`       Display a context menu (popup) at the specified position.
:ref:`super <no-24724>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-24725>`           Remove a previously registered event binding.
:ref:`unbindKey <no-24726>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-24727>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-24728>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-24729>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-24646:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.afterInit(self)

   
   Create the calendar control, and resize this panel
   to the calendar's size.
   



-------

.. _no-24698:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.onCalKey(self, evt)



-------

.. _no-24699:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.onCalSelection(self, evt)



-------


Methods - inherited
=====================

.. _no-24644:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24645:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-24647:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24648:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24649:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.autoBindEvents(self, force=True)
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

.. _no-24650:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24651:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24652:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24653:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24654:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-24655:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24656:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24657:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24658:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24659:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24660:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24661:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24662:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24663:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-24664:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24665:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24666:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24667:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24668:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24669:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24670:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24671:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24672:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24673:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24674:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24675:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24676:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24677:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24678:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24679:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24680:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24681:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24682:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24683:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24684:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24685:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-24686:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24687:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24688:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24689:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24690:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24691:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24692:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24693:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-24694:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.lockDisplay(self)
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

.. _no-24695:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24696:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24697:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24700:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24701:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24702:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24703:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24704:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24705:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24706:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24707:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24708:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24709:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24710:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24711:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24712:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24713:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24714:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-24715:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24716:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24717:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-24718:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-24719:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24720:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24721:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24722:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24723:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24724:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24725:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24726:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24727:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24728:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24729:

.. function:: dabo.ui.uiwx.dDateTextBox.CalPanel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
