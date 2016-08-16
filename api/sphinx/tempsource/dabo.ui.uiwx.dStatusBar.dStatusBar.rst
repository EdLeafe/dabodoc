
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dStatusBar

.. _dabo.ui.uiwx.dStatusBar.dStatusBar:

==============================================
|doc_title|  **dStatusBar.dStatusBar** - class
==============================================


Creates a status bar, which displays information to the user.

The status bar is displayed at the bottom of the form. Add the status bar
to your form using form.StatusBar=dStatusBar().




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dStatusBar**

.. inheritance-diagram:: dStatusBar


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dStatusBar.dStatusBar

   .. automethod:: dabo.ui.uiwx.dStatusBar.dStatusBar.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-35472>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-35473>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-35474>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-35475>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-35476>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-35477>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-35478>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-35479>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-35480>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-35481>`                The caption of the object. (str)
:ref:`Children <no-35482>`               Returns a list of object references to the children of
:ref:`Class <no-35483>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-35484>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-35485>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-35486>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-35487>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-35488>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-35489>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-35490>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-35491>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-35492>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-35493>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-35494>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-35495>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-35496>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-35497>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-35498>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-35499>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-35500>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-35501>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-35502>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-35503>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-35504>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-35505>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-35506>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-35507>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-35508>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-35509>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-35510>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-35511>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-35512>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-35513>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-35514>`                Specifies whether the object and children can get user input. (bool)
:ref:`FieldCount <no-35515>`             Number of areas, or 'fields', in the status bar. Default=1  (int)
:ref:`Font <no-35516>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-35517>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-35518>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-35519>`               Specifies the font face. (str)
:ref:`FontInfo <no-35520>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-35521>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-35522>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-35523>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-35524>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-35525>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-35526>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-35527>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-35528>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-35529>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-35530>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-35531>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-35532>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-35533>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-35534>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-35535>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-35536>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-35537>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-35538>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-35539>`               Specifies the base name of the object.
:ref:`Parent <no-35540>`                 The containing object. (obj)
:ref:`Position <no-35541>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-35542>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-35543>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-35544>`                  The position of the right side of the object. This is a
:ref:`Size <no-35545>`                   The size of the object. (tuple)
:ref:`Sizer <no-35546>`                  The sizer for the object.
:ref:`StatusText <no-35547>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-35548>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-35549>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-35550>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-35551>`                    The top position of the object. (int)
:ref:`Transparency <no-35552>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-35553>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-35554>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-35555>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-35556>`                  The width of the object. (int)
:ref:`WindowHandle <no-35557>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-35515:

**FieldCount** 

Number of areas, or 'fields', in the status bar. Default=1  (int)



-------


Properties - inherited
========================

.. _no-35472:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35473:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35474:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35475:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35476:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35477:

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

.. _no-35478:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35479:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35480:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35481:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35482:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35483:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35484:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35485:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35486:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35487:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35488:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35489:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35490:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35491:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35492:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35493:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35494:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35495:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35496:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35497:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35498:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35499:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35500:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35501:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35502:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35503:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35504:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35505:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35506:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35507:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35508:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35509:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35510:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35511:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35512:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35513:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35514:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35516:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35517:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35518:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35519:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35520:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35521:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35522:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35523:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35524:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35525:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35526:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35527:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35528:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35529:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35530:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35531:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35532:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35533:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35534:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35535:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35536:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35537:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35538:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35539:

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

.. _no-35540:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35541:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35542:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35543:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35544:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35545:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35546:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35547:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: 'wx._windows.StatusBar - can not provide a link

-------

.. _no-35548:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-35549:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35550:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35551:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35552:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35553:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35554:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35555:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35556:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35557:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-35558>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-35559>`                 Occurs after the control or form is created.
:ref:`Destroy <no-35560>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-35561>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-35562>`               Occurs when the control gets the focus.
:ref:`Idle <no-35563>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-35564>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-35565>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-35566>`               
:ref:`KeyUp <no-35567>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-35568>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-35569>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-35570>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-35571>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-35572>`             
:ref:`MouseLeave <no-35573>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-35574>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-35575>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-35576>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-35577>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-35578>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-35579>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-35580>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-35581>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-35582>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-35583>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-35584>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-35585>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-35586>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-35587>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-35588>`                   Occurs when the control's position changes.
:ref:`Paint <no-35589>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-35590>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-35591>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-35592>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-35593>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-35558:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-35559:

**Create** 

Occurs after the control or form is created.



-------

.. _no-35560:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-35561:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-35562:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-35563:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-35564:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-35565:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-35566:

**KeyEvent** 



-------

.. _no-35567:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-35568:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-35569:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-35570:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-35571:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-35572:

**MouseEvent** 



-------

.. _no-35573:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-35574:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-35575:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-35576:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-35577:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-35578:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-35579:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-35580:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-35581:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-35582:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-35583:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-35584:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-35585:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-35586:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-35587:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-35588:

**Move** 

Occurs when the control's position changes.



-------

.. _no-35589:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-35590:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-35591:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-35592:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-35593:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-35594>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-35595>`             Instantiate object as a child of self.
:ref:`afterInit <no-35596>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-35597>`          
:ref:`afterSetProperties <no-35598>`    
:ref:`autoBindEvents <no-35599>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-35600>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-35601>`   
:ref:`bindEvent <no-35602>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-35603>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-35604>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-35605>`          Makes this object topmost
:ref:`clear <no-35606>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-35607>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-35608>`  Given a position relative to this control, return a position relative
:ref:`copy <no-35609>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-35610>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-35611>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-35612>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-35613>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-35614>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-35615>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-35616>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-35617>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-35618>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-35619>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-35620>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-35621>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-35622>`              Draws text on the object at the specified position
:ref:`endHover <no-35623>`              
:ref:`fitToSizer <no-35624>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-35625>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-35626>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-35627>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-35628>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-35629>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-35630>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-35631>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-35632>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-35633>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-35634>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-35635>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-35636>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-35637>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-35638>`                  Make the object invisible.
:ref:`initEvents <no-35639>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-35640>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-35641>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-35642>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-35643>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-35644>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-35645>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-35646>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-35647>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-35648>`               
:ref:`paste <no-35649>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-35650>`           
:ref:`processDroppedFiles <no-35651>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-35652>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-35653>`            Raise the passed Dabo event.
:ref:`reCreate <no-35654>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-35655>`              Recreate the object.
:ref:`redraw <no-35656>`                Called when the object is (re)drawn.
:ref:`refresh <no-35657>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-35658>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-35659>`               Destroys the object.
:ref:`removeDrawnObject <no-35660>`     
:ref:`sendToBack <no-35661>`            Places this object behind all others.
:ref:`setAll <no-35662>`                Set all child object properties to the passed value.
:ref:`setFocus <no-35663>`              Sets focus to the object.
:ref:`setPositionInSizer <no-35664>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-35665>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-35666>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-35667>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-35668>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-35669>`                  Make the object visible.
:ref:`showContainingPage <no-35670>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-35671>`       Display a context menu (popup) at the specified position.
:ref:`super <no-35672>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-35673>`           Remove a previously registered event binding.
:ref:`unbindKey <no-35674>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-35675>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-35676>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-35677>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-35643:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.layout(self)

   Wrap the wx version of the call, if possible.



-------


Methods - inherited
=====================

.. _no-35594:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35595:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-35596:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35597:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35598:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35599:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.autoBindEvents(self, force=True)
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

.. _no-35600:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35601:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35602:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35603:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35604:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-35605:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35606:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35607:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35608:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35609:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35610:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35611:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35612:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35613:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-35614:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35615:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35616:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35617:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35618:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35619:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35620:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35621:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35622:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35623:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35624:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35625:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35626:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35627:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35628:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35629:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35630:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35631:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35632:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35633:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35634:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35635:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-35636:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35637:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35638:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35639:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35640:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35641:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35642:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35644:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.lockDisplay(self)
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

.. _no-35645:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35646:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35647:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35648:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35649:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35650:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35651:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35652:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35653:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35654:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35655:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35656:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35657:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35658:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35659:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35660:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35661:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35662:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-35663:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35664:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35665:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-35666:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-35667:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35668:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35669:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35670:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35671:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35672:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35673:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35674:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35675:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35676:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35677:

.. function:: dabo.ui.uiwx.dStatusBar.dStatusBar.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
