
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBaseMenuBar

.. _dabo.ui.uiwx.dBaseMenuBar.FileMenu:

==============================================
|doc_title|  **dBaseMenuBar.FileMenu** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **FileMenu**

.. inheritance-diagram:: FileMenu


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dMenu.dMenu`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBaseMenuBar.FileMenu

   .. automethod:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-29438>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-29439>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-29440>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-29441>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-29442>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-29443>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-29444>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-29445>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-29446>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-29447>`                Specifies the text of the menu.  (str)
:ref:`Children <no-29448>`               Returns a list of object references to the children of
:ref:`Class <no-29449>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-29450>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-29451>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-29452>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-29453>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-29454>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-29455>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-29456>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-29457>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-29458>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-29459>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-29460>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-29461>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-29462>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-29463>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-29464>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-29465>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-29466>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-29467>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-29468>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-29469>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicLeft <no-29470>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-29471>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-29472>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-29473>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-29474>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-29475>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-29476>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-29477>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-29478>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-29479>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-29480>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-29481>`                Specifies whether the menu can be interacted with. Default=True  (bool)
:ref:`Font <no-29482>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-29483>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-29484>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-29485>`               Specifies the font face. (str)
:ref:`FontInfo <no-29486>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-29487>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-29488>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-29489>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-29490>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-29491>`                   Specifies the form that contains the menu.  (dForm)
:ref:`Height <no-29492>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-29493>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-29494>`               Specifies the help text associated with this menu.  (str)
:ref:`Hover <no-29495>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-29496>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-29497>`              Specifies which events to log.  (list of strings)
:ref:`MRU <no-29498>`                    Determines if this menu uses Most Recently Used behavior. Default=False  (bool)
:ref:`MaximumHeight <no-29499>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-29500>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-29501>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MenuID <no-29502>`                 Identifying value for this menu. NOTE: there is no checking for
:ref:`MinimumHeight <no-29503>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-29504>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-29505>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-29506>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-29507>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-29508>`               Specifies the base name of the object.
:ref:`Parent <no-29509>`                 Specifies the parent menu or menubar.  (varies)
:ref:`Position <no-29510>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-29511>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-29512>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-29513>`                  The position of the right side of the object. This is a
:ref:`Size <no-29514>`                   The size of the object. (tuple)
:ref:`Sizer <no-29515>`                  The sizer for the object.
:ref:`StatusText <no-29516>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-29517>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-29518>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-29519>`                    The top position of the object. (int)
:ref:`Transparency <no-29520>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-29521>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-29522>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-29523>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-29524>`                  The width of the object. (int)
:ref:`WindowHandle <no-29525>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-29438:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29439:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29440:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29441:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29442:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29443:

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

.. _no-29444:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29445:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29446:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29447:

**Caption** 

Specifies the text of the menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29448:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29449:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29450:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29451:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29452:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29453:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29454:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29455:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29456:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29457:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29458:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29459:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29460:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29461:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29462:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29463:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29464:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29465:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29466:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29467:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29468:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29469:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29470:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29471:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29472:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29473:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29474:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29475:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29476:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29477:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29478:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29479:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29480:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29481:

**Enabled** 

Specifies whether the menu can be interacted with. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29482:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29483:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29484:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29485:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29486:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29487:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29488:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29489:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29490:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29491:

**Form** 

Specifies the form that contains the menu.  (dForm)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29492:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29493:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29494:

**HelpText** 

Specifies the help text associated with this menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29495:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29496:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29497:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29498:

**MRU** 

Determines if this menu uses Most Recently Used behavior. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29499:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29500:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29501:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29502:

**MenuID** 

Identifying value for this menu. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that MenuID values
    are unique.  (varies)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29503:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29504:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29505:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29506:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29507:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29508:

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

.. _no-29509:

**Parent** 

Specifies the parent menu or menubar.  (varies)


Inherited from: 'wx._core.Menu - can not provide a link

-------

.. _no-29510:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29511:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29512:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29513:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29514:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29515:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29516:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29517:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29518:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29519:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29520:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29521:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29522:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29523:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29524:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29525:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-29526>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-29527>`                 Occurs after the control or form is created.
:ref:`Destroy <no-29528>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-29529>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-29530>`               Occurs when the control gets the focus.
:ref:`Idle <no-29531>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-29532>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-29533>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-29534>`               
:ref:`KeyUp <no-29535>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-29536>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-29537>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-29538>`              
:ref:`MenuHighlight <no-29539>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-29540>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-29541>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-29542>`             
:ref:`MouseLeave <no-29543>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-29544>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-29545>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-29546>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-29547>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-29548>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-29549>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-29550>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-29551>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-29552>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-29553>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-29554>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-29555>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-29556>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-29557>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-29558>`                   Occurs when the control's position changes.
:ref:`Paint <no-29559>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-29560>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-29561>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-29562>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-29563>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-29526:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-29527:

**Create** 

Occurs after the control or form is created.



-------

.. _no-29528:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-29529:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-29530:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-29531:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-29532:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-29533:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-29534:

**KeyEvent** 



-------

.. _no-29535:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-29536:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-29537:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-29538:

**MenuEvent** 



-------

.. _no-29539:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-29540:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-29541:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-29542:

**MouseEvent** 



-------

.. _no-29543:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-29544:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-29545:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-29546:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-29547:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-29548:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-29549:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-29550:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-29551:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-29552:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-29553:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-29554:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-29555:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-29556:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-29557:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-29558:

**Move** 

Occurs when the control's position changes.



-------

.. _no-29559:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-29560:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-29561:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-29562:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-29563:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-29564>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-29565>`             Instantiate object as a child of self.
:ref:`afterInit <no-29566>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-29567>`          
:ref:`afterSetProperties <no-29568>`    
:ref:`append <no-29569>`                Append a dMenuItem with the specified properties.
:ref:`appendItem <no-29570>`            Insert a dMenuItem at the bottom of the menu.
:ref:`appendMenu <no-29571>`            Insert a dMenu at the bottom of the menu.
:ref:`appendSeparator <no-29572>`       Insert a separator at the bottom of the menu.
:ref:`autoBindEvents <no-29573>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-29574>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-29575>`   
:ref:`bindEvent <no-29576>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-29577>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-29578>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-29579>`          Makes this object topmost
:ref:`clear <no-29580>`                 Removes all items in this menu.
:ref:`clearChecks <no-29581>`           Unchecks any checkmark-type menu items.
:ref:`clone <no-29582>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-29583>`  Given a position relative to this control, return a position relative
:ref:`copy <no-29584>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-29585>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-29586>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-29587>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-29588>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-29589>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-29590>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-29591>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-29592>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-29593>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-29594>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-29595>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-29596>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-29597>`              Draws text on the object at the specified position
:ref:`endHover <no-29598>`              
:ref:`fitToSizer <no-29599>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-29600>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-29601>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-29602>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-29603>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-29604>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-29605>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-29606>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-29607>`      Returns an object that locks the current display when created, and
:ref:`getItem <no-29608>`               Returns a reference to the menu item with the specified ItemID or Caption.
:ref:`getItemIndex <no-29609>`          Returns the index of the item with the specified caption; you can
:ref:`getMousePosition <no-29610>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-29611>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-29612>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-29613>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-29614>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-29615>`                  Make the object invisible.
:ref:`initEvents <no-29616>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-29617>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-29618>`                Insert a dMenuItem at the given position with the specified properties.
:ref:`insertItem <no-29619>`            Insert a dMenuItem before the specified position in the menu.
:ref:`insertMenu <no-29620>`            Insert a dMenu before the specified position in the menu.
:ref:`insertSeparator <no-29621>`       Insert a separator before the specified position in the menu.
:ref:`isContainedBy <no-29622>`         Returns True if the containership hierarchy for this control
:ref:`isItemChecked <no-29623>`         
:ref:`iterateCall <no-29624>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-29625>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-29626>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-29627>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-29628>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-29629>`               
:ref:`paste <no-29630>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-29631>`           
:ref:`prepend <no-29632>`               Prepend a dMenuItem with the specified properties.
:ref:`prependItem <no-29633>`           Insert a dMenuItem at the top of the menu.
:ref:`prependMenu <no-29634>`           Insert a dMenu at the top of the menu.
:ref:`prependSeparator <no-29635>`      Insert a separator at the top of the menu.
:ref:`processDroppedFiles <no-29636>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-29637>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-29638>`            Raise the passed Dabo event.
:ref:`reCreate <no-29639>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-29640>`              Recreate the object.
:ref:`redraw <no-29641>`                Called when the object is (re)drawn.
:ref:`refresh <no-29642>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-29643>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-29644>`               Destroys the object.
:ref:`remove <no-29645>`                Removes the specified item from the menu. You may specify the item by
:ref:`removeDrawnObject <no-29646>`     
:ref:`sendToBack <no-29647>`            Places this object behind all others.
:ref:`setAll <no-29648>`                Set all child object properties to the passed value.
:ref:`setCheck <no-29649>`              When using checkmark-type menus, passing either the item
:ref:`setFocus <no-29650>`              Sets focus to the object.
:ref:`setItemCheck <no-29651>`          Pass a menu item and a boolean value, and the checked
:ref:`setPositionInSizer <no-29652>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-29653>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-29654>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-29655>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-29656>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-29657>`                  Make the object visible.
:ref:`showContainingPage <no-29658>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-29659>`       Display a context menu (popup) at the specified position.
:ref:`super <no-29660>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-29661>`           Remove a previously registered event binding.
:ref:`unbindKey <no-29662>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-29663>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-29664>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-29665>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-29564:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29565:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-29566:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29567:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29568:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29569:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.append(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Append a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29570:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.appendItem(self, item)
   :noindex:


   Insert a dMenuItem at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29571:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.appendMenu(self, menu)
   :noindex:


   Insert a dMenu at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29572:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.appendSeparator(self)
   :noindex:


   Insert a separator at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29573:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.autoBindEvents(self, force=True)
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

.. _no-29574:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29575:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29576:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29577:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29578:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-29579:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29580:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.clear(self)
   :noindex:


   Removes all items in this menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29581:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.clearChecks(self)
   :noindex:


   Unchecks any checkmark-type menu items.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29582:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29583:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29584:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29585:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29586:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29587:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29588:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-29589:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29590:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29591:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29592:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29593:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29594:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29595:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29596:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29597:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29598:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29599:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29600:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29601:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29602:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29603:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29604:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29605:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29606:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29607:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29608:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getItem(self, idOrCaption)
   :noindex:


   
   Returns a reference to the menu item with the specified ItemID or Caption.
   The ItemID property is checked first; then the Caption. If no match is found,
   None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29609:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getItemIndex(self, captionOrItem)
   :noindex:


   
   Returns the index of the item with the specified caption; you can
   optionally pass in a reference to the menu item itself. If the item
   isn't found, None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29610:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29611:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29612:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-29613:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29614:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29615:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29616:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29617:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29618:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.insert(self, pos, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Insert a dMenuItem at the given position with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29619:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.insertItem(self, pos, item)
   :noindex:


   Insert a dMenuItem before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29620:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.insertMenu(self, pos, menu)
   :noindex:


   Insert a dMenu before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29621:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.insertSeparator(self, pos)
   :noindex:


   Insert a separator before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29622:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29623:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.isItemChecked(self, capIdxOrItem)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29624:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29625:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.lockDisplay(self)
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

.. _no-29626:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29627:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29628:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29629:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29630:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29631:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29632:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.prepend(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Prepend a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29633:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.prependItem(self, item)
   :noindex:


   Insert a dMenuItem at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29634:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.prependMenu(self, menu)
   :noindex:


   Insert a dMenu at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29635:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.prependSeparator(self)
   :noindex:


   Insert a separator at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29636:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29637:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29638:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29639:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29640:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29641:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29642:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29643:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29644:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29645:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.remove(self, capIdxOrItem, release=True)
   :noindex:


   
   Removes the specified item from the menu. You may specify the item by
   passing its index, its Caption, or by passing the item itself. If release is
   True (the default), the item is destroyed as well. If release is False, a reference
   to the object will be returned, and the caller is responsible for destroying it.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29646:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29647:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29648:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-29649:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setCheck(self, capIdxOrItem, unCheckOthers=True)
   :noindex:


   
   When using checkmark-type menus, passing either the item
   itself, or the index or caption of the item you want checked to
   this method will check that item. If unCheckOthers is True, non-
   matching items will be unchecked.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29650:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29651:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setItemCheck(self, itm, val)
   :noindex:


   
   Pass a menu item and a boolean value, and the checked
   state of that menu item will be set accordingly.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29652:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29653:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-29654:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-29655:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29656:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29657:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29658:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29659:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29660:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29661:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29662:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29663:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29664:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29665:

.. function:: dabo.ui.uiwx.dBaseMenuBar.FileMenu.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
