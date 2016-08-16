
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.BrowsePage:

========================================
|doc_title|  **Page.BrowsePage** - class
========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **BrowsePage**

.. inheritance-diagram:: BrowsePage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.datanav.Page.Page`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.BrowsePage

   .. automethod:: dabo.lib.datanav.Page.BrowsePage.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-2468>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-2469>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-2470>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-2471>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-2472>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-2473>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-2474>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-2475>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-2476>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-2477>`                 The text identifying this particular page.  (str)
:ref:`Children <no-2478>`                Child controls of this panel. This excludes the wx-specific
:ref:`Class <no-2479>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-2480>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-2481>`    Reference to the sizer item that control's this control's layout.
:ref:`DeferredUpdates <no-2482>`         Allow to defer controls updates until page become active.  (bool)
:ref:`DroppedFileHandler <no-2483>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-2484>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-2485>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-2486>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-2487>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-2488>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-2489>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-2490>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-2491>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-2492>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-2493>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-2494>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-2495>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-2496>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-2497>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-2498>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-2499>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-2500>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicImage <no-2501>`            Dynamically determine the value of the Image property.
:ref:`DynamicLeft <no-2502>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-2503>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-2504>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-2505>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-2506>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-2507>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-2508>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-2509>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-2510>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-2511>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-2512>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-2513>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-2514>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-2515>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-2516>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-2517>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-2518>`                Specifies the font face. (str)
:ref:`FontInfo <no-2519>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-2520>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-2521>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-2522>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-2523>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-2524>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-2525>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-2526>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-2527>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-2528>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Image <no-2529>`                   Sets the image that is displayed on the page tab. This is
:ref:`Left <no-2530>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-2531>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-2532>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-2533>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-2534>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-2535>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-2536>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-2537>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-2538>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-2539>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-2540>`                Specifies the base name of the object.
:ref:`Parent <no-2541>`                  The containing object. (obj)
:ref:`Position <no-2542>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-2543>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-2544>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-2545>`                   The position of the right side of the object. This is a
:ref:`Size <no-2546>`                    The size of the object. (tuple)
:ref:`Sizer <no-2547>`                   The sizer for the object.
:ref:`StatusText <no-2548>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-2549>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-2550>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-2551>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-2552>`                     The top position of the object. (int)
:ref:`Transparency <no-2553>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-2554>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateOnPageEnter <no-2555>`       Specifies whether an implicit self.update() happens upon page entry.
:ref:`VerticalScroll <no-2556>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-2557>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-2558>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-2559>`                   The width of the object. (int)
:ref:`WindowHandle <no-2560>`            The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-2468:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2469:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2470:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2471:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2472:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2473:

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

.. _no-2474:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2475:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2476:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2477:

**Caption** 

The text identifying this particular page.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2478:

**Children** 

Child controls of this panel. This excludes the wx-specific
    scroll bars  (list of objects)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2479:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2480:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2481:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2482:

**DeferredUpdates** 

Allow to defer controls updates until page become active.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2483:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2484:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2485:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2486:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2487:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2488:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2489:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2490:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2491:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2492:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2493:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2494:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2495:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2496:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2497:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2498:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2499:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2500:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2501:

**DynamicImage** 

Dynamically determine the value of the Image property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Image property. If DynamicImage is set to None (the default), Image
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2502:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2503:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2504:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2505:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2506:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2507:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2508:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2509:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2510:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2511:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2512:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2513:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2514:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2515:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2516:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2517:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2518:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2519:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2520:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2521:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2522:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2523:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2524:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2525:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2526:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2527:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2528:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2529:

**Image** 

Sets the image that is displayed on the page tab. This is
    determined by the key value passed, which must refer to an
    image already added to the parent pageframe.
    When used to retrieve an image, it returns the index of the
    page's image in the parent pageframe's image list.   (int)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2530:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2531:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2532:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2533:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2534:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2535:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2536:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2537:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2538:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2539:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2540:

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

.. _no-2541:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2542:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2543:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2544:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2545:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2546:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2547:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2548:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2549:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-2550:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2551:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2552:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2553:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2554:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2555:

**UpdateOnPageEnter** 

Specifies whether an implicit self.update() happens upon page entry.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2556:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2557:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2558:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2559:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2560:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-2561>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-2562>`              Occurs when a child control is created.
:ref:`ControlNavigationEvent <no-2563>` 
:ref:`Create <no-2564>`                 Occurs after the control or form is created.
:ref:`Destroy <no-2565>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-2566>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-2567>`               Occurs when the control gets the focus.
:ref:`Idle <no-2568>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-2569>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-2570>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-2571>`               
:ref:`KeyUp <no-2572>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-2573>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-2574>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-2575>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-2576>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-2577>`             
:ref:`MouseLeave <no-2578>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-2579>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-2580>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-2581>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-2582>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-2583>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-2584>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-2585>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-2586>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-2587>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-2588>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-2589>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-2590>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-2591>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-2592>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-2593>`                   Occurs when the control's position changes.
:ref:`PageContextMenu <no-2594>`        Occurs when the user requests a context event for a dPage
:ref:`PageEnter <no-2595>`              Occurs when the page becomes the active page.
:ref:`PageLeave <no-2596>`              Occurs when a different page becomes active.
:ref:`Paint <no-2597>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-2598>`                 Occurs when the control or form is resized.
:ref:`ScrollBottom <no-2599>`           Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-2600>`            
:ref:`ScrollLineDown <no-2601>`         Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-2602>`           Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-2603>`         Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-2604>`           Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-2605>`        Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-2606>`     Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-2607>`              Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-2608>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-2609>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-2610>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-2561:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-2562:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-2563:

**ControlNavigationEvent** 



-------

.. _no-2564:

**Create** 

Occurs after the control or form is created.



-------

.. _no-2565:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-2566:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-2567:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-2568:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-2569:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-2570:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-2571:

**KeyEvent** 



-------

.. _no-2572:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-2573:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-2574:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-2575:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-2576:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-2577:

**MouseEvent** 



-------

.. _no-2578:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-2579:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-2580:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-2581:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-2582:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-2583:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-2584:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-2585:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-2586:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-2587:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-2588:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-2589:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-2590:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-2591:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-2592:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-2593:

**Move** 

Occurs when the control's position changes.



-------

.. _no-2594:

**PageContextMenu** 

Occurs when the user requests a context event for a dPage



-------

.. _no-2595:

**PageEnter** 

Occurs when the page becomes the active page.



-------

.. _no-2596:

**PageLeave** 

Occurs when a different page becomes active.



-------

.. _no-2597:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-2598:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-2599:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-2600:

**ScrollEvent** 



-------

.. _no-2601:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-2602:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-2603:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-2604:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-2605:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-2606:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-2607:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-2608:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-2609:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-2610:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-2611>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-2612>`             Instantiate object as a child of self.
:ref:`afterInit <no-2613>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-2614>`          
:ref:`afterSetProperties <no-2615>`    
:ref:`autoBindEvents <no-2616>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-2617>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-2618>`   
:ref:`bindEvent <no-2619>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-2620>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-2621>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-2622>`          Makes this object topmost
:ref:`clear <no-2623>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-2624>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-2625>`  Given a position relative to this control, return a position relative
:ref:`copy <no-2626>`                  Called by uiApp when the user requests a copy operation.
:ref:`createItems <no-2627>`           
:ref:`cut <no-2628>`                   Called by uiApp when the user requests a cut operation.
:ref:`deleteRecord <no-2629>`          Called by a browse grid when the user wants to delete the current row.
:ref:`drawArc <no-2630>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-2631>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-2632>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-2633>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-2634>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-2635>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-2636>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-2637>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-2638>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-2639>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-2640>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-2641>`              Draws text on the object at the specified position
:ref:`editRecord <no-2642>`            Called by a browse grid when the user wants to edit the current row.
:ref:`endHover <no-2643>`              
:ref:`fitToSizer <no-2644>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-2645>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-2646>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-2647>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-2648>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-2649>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-2650>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-2651>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-2652>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-2653>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-2654>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-2655>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-2656>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-2657>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-2658>`                  Make the object invisible.
:ref:`initEvents <no-2659>`            
:ref:`initProperties <no-2660>`        Hook for subclasses. User subclasses should set properties
:ref:`initSizer <no-2661>`             Set up the default vertical box sizer for the page.
:ref:`isContainedBy <no-2662>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-2663>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-2664>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-2665>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-2666>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-2667>`    Moves this object's tab order before the passed obj.
:ref:`newRecord <no-2668>`             Called by a browse grid when the user wants to add a new row.
:ref:`objectCoordinates <no-2669>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-2670>`               
:ref:`pageDown <no-2671>`              
:ref:`pageHorizontally <no-2672>`      Scroll horizontally one 'page' width.
:ref:`pageLeft <no-2673>`              
:ref:`pageRight <no-2674>`             
:ref:`pageUp <no-2675>`                
:ref:`pageVertically <no-2676>`        Scroll vertically one 'page' height.
:ref:`paste <no-2677>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-2678>`           
:ref:`processDroppedFiles <no-2679>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-2680>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-2681>`            Raise the passed Dabo event.
:ref:`reCreate <no-2682>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-2683>`              Recreate the object.
:ref:`redraw <no-2684>`                Called when the object is (re)drawn.
:ref:`refresh <no-2685>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-2686>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-2687>`               Destroys the object.
:ref:`removeDrawnObject <no-2688>`     
:ref:`scrollHorizontally <no-2689>`    Change the horizontal scroll position by 'amt' units.
:ref:`scrollVertically <no-2690>`      Change the vertical scroll position by 'amt' units.
:ref:`sendToBack <no-2691>`            Places this object behind all others.
:ref:`setAll <no-2692>`                Set all child object properties to the passed value.
:ref:`setFocus <no-2693>`              Sets focus to the object.
:ref:`setPositionInSizer <no-2694>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-2695>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-2696>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-2697>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-2698>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-2699>`                  Make the object visible.
:ref:`showContainingPage <no-2700>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-2701>`       Display a context menu (popup) at the specified position.
:ref:`super <no-2702>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-2703>`           Remove a previously registered event binding.
:ref:`unbindKey <no-2704>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-2705>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-2706>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-2707>`                

====================================== ========================


Methods
=======

.. _no-2627:

.. function:: dabo.lib.datanav.Page.BrowsePage.createItems(self)



-------


Methods - inherited
=====================

.. _no-2611:

.. function:: dabo.lib.datanav.Page.BrowsePage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2612:

.. function:: dabo.lib.datanav.Page.BrowsePage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-2613:

.. function:: dabo.lib.datanav.Page.BrowsePage.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2614:

.. function:: dabo.lib.datanav.Page.BrowsePage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2615:

.. function:: dabo.lib.datanav.Page.BrowsePage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2616:

.. function:: dabo.lib.datanav.Page.BrowsePage.autoBindEvents(self, force=True)
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

.. _no-2617:

.. function:: dabo.lib.datanav.Page.BrowsePage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2618:

.. function:: dabo.lib.datanav.Page.BrowsePage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2619:

.. function:: dabo.lib.datanav.Page.BrowsePage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2620:

.. function:: dabo.lib.datanav.Page.BrowsePage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2621:

.. function:: dabo.lib.datanav.Page.BrowsePage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-2622:

.. function:: dabo.lib.datanav.Page.BrowsePage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2623:

.. function:: dabo.lib.datanav.Page.BrowsePage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2624:

.. function:: dabo.lib.datanav.Page.BrowsePage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2625:

.. function:: dabo.lib.datanav.Page.BrowsePage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2626:

.. function:: dabo.lib.datanav.Page.BrowsePage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2628:

.. function:: dabo.lib.datanav.Page.BrowsePage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2629:

.. function:: dabo.lib.datanav.Page.BrowsePage.deleteRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to delete the current row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2630:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2631:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2632:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-2633:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2634:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2635:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2636:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2637:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2638:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2639:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2640:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2641:

.. function:: dabo.lib.datanav.Page.BrowsePage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2642:

.. function:: dabo.lib.datanav.Page.BrowsePage.editRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to edit the current row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2643:

.. function:: dabo.lib.datanav.Page.BrowsePage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2644:

.. function:: dabo.lib.datanav.Page.BrowsePage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2645:

.. function:: dabo.lib.datanav.Page.BrowsePage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2646:

.. function:: dabo.lib.datanav.Page.BrowsePage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2647:

.. function:: dabo.lib.datanav.Page.BrowsePage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2648:

.. function:: dabo.lib.datanav.Page.BrowsePage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2649:

.. function:: dabo.lib.datanav.Page.BrowsePage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2650:

.. function:: dabo.lib.datanav.Page.BrowsePage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2651:

.. function:: dabo.lib.datanav.Page.BrowsePage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2652:

.. function:: dabo.lib.datanav.Page.BrowsePage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2653:

.. function:: dabo.lib.datanav.Page.BrowsePage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2654:

.. function:: dabo.lib.datanav.Page.BrowsePage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2655:

.. function:: dabo.lib.datanav.Page.BrowsePage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-2656:

.. function:: dabo.lib.datanav.Page.BrowsePage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2657:

.. function:: dabo.lib.datanav.Page.BrowsePage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2658:

.. function:: dabo.lib.datanav.Page.BrowsePage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2659:

.. function:: dabo.lib.datanav.Page.BrowsePage.initEvents(self)
   :noindex:



Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2660:

.. function:: dabo.lib.datanav.Page.BrowsePage.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2661:

.. function:: dabo.lib.datanav.Page.BrowsePage.initSizer(self)
   :noindex:


   Set up the default vertical box sizer for the page.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2662:

.. function:: dabo.lib.datanav.Page.BrowsePage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2663:

.. function:: dabo.lib.datanav.Page.BrowsePage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2664:

.. function:: dabo.lib.datanav.Page.BrowsePage.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-2665:

.. function:: dabo.lib.datanav.Page.BrowsePage.lockDisplay(self)
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

.. _no-2666:

.. function:: dabo.lib.datanav.Page.BrowsePage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2667:

.. function:: dabo.lib.datanav.Page.BrowsePage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2668:

.. function:: dabo.lib.datanav.Page.BrowsePage.newRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to add a new row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2669:

.. function:: dabo.lib.datanav.Page.BrowsePage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2670:

.. function:: dabo.lib.datanav.Page.BrowsePage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2671:

.. function:: dabo.lib.datanav.Page.BrowsePage.pageDown(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2672:

.. function:: dabo.lib.datanav.Page.BrowsePage.pageHorizontally(self, direction)
   :noindex:


   Scroll horizontally one 'page' width.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2673:

.. function:: dabo.lib.datanav.Page.BrowsePage.pageLeft(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2674:

.. function:: dabo.lib.datanav.Page.BrowsePage.pageRight(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2675:

.. function:: dabo.lib.datanav.Page.BrowsePage.pageUp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2676:

.. function:: dabo.lib.datanav.Page.BrowsePage.pageVertically(self, direction)
   :noindex:


   Scroll vertically one 'page' height.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2677:

.. function:: dabo.lib.datanav.Page.BrowsePage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2678:

.. function:: dabo.lib.datanav.Page.BrowsePage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2679:

.. function:: dabo.lib.datanav.Page.BrowsePage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2680:

.. function:: dabo.lib.datanav.Page.BrowsePage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2681:

.. function:: dabo.lib.datanav.Page.BrowsePage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2682:

.. function:: dabo.lib.datanav.Page.BrowsePage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2683:

.. function:: dabo.lib.datanav.Page.BrowsePage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2684:

.. function:: dabo.lib.datanav.Page.BrowsePage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2685:

.. function:: dabo.lib.datanav.Page.BrowsePage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2686:

.. function:: dabo.lib.datanav.Page.BrowsePage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2687:

.. function:: dabo.lib.datanav.Page.BrowsePage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2688:

.. function:: dabo.lib.datanav.Page.BrowsePage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2689:

.. function:: dabo.lib.datanav.Page.BrowsePage.scrollHorizontally(self, amt)
   :noindex:


   Change the horizontal scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2690:

.. function:: dabo.lib.datanav.Page.BrowsePage.scrollVertically(self, amt)
   :noindex:


   Change the vertical scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2691:

.. function:: dabo.lib.datanav.Page.BrowsePage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2692:

.. function:: dabo.lib.datanav.Page.BrowsePage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-2693:

.. function:: dabo.lib.datanav.Page.BrowsePage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2694:

.. function:: dabo.lib.datanav.Page.BrowsePage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2695:

.. function:: dabo.lib.datanav.Page.BrowsePage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-2696:

.. function:: dabo.lib.datanav.Page.BrowsePage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-2697:

.. function:: dabo.lib.datanav.Page.BrowsePage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2698:

.. function:: dabo.lib.datanav.Page.BrowsePage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2699:

.. function:: dabo.lib.datanav.Page.BrowsePage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2700:

.. function:: dabo.lib.datanav.Page.BrowsePage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2701:

.. function:: dabo.lib.datanav.Page.BrowsePage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2702:

.. function:: dabo.lib.datanav.Page.BrowsePage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2703:

.. function:: dabo.lib.datanav.Page.BrowsePage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2704:

.. function:: dabo.lib.datanav.Page.BrowsePage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2705:

.. function:: dabo.lib.datanav.Page.BrowsePage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2706:

.. function:: dabo.lib.datanav.Page.BrowsePage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2707:

.. function:: dabo.lib.datanav.Page.BrowsePage.update(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------


|
