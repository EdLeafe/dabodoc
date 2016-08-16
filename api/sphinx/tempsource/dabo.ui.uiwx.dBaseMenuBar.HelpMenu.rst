
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBaseMenuBar

.. _dabo.ui.uiwx.dBaseMenuBar.HelpMenu:

==============================================
|doc_title|  **dBaseMenuBar.HelpMenu** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **HelpMenu**

.. inheritance-diagram:: HelpMenu


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dMenu.dMenu`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-29666>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-29667>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-29668>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-29669>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-29670>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-29671>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-29672>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-29673>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-29674>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-29675>`                Specifies the text of the menu.  (str)
:ref:`Children <no-29676>`               Returns a list of object references to the children of
:ref:`Class <no-29677>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-29678>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-29679>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-29680>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-29681>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-29682>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-29683>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-29684>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-29685>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-29686>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-29687>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-29688>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-29689>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-29690>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-29691>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-29692>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-29693>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-29694>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-29695>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-29696>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-29697>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicLeft <no-29698>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-29699>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-29700>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-29701>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-29702>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-29703>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-29704>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-29705>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-29706>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-29707>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-29708>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-29709>`                Specifies whether the menu can be interacted with. Default=True  (bool)
:ref:`Font <no-29710>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-29711>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-29712>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-29713>`               Specifies the font face. (str)
:ref:`FontInfo <no-29714>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-29715>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-29716>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-29717>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-29718>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-29719>`                   Specifies the form that contains the menu.  (dForm)
:ref:`Height <no-29720>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-29721>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-29722>`               Specifies the help text associated with this menu.  (str)
:ref:`Hover <no-29723>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-29724>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-29725>`              Specifies which events to log.  (list of strings)
:ref:`MRU <no-29726>`                    Determines if this menu uses Most Recently Used behavior. Default=False  (bool)
:ref:`MaximumHeight <no-29727>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-29728>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-29729>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MenuID <no-29730>`                 Identifying value for this menu. NOTE: there is no checking for
:ref:`MinimumHeight <no-29731>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-29732>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-29733>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-29734>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-29735>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-29736>`               Specifies the base name of the object.
:ref:`Parent <no-29737>`                 Specifies the parent menu or menubar.  (varies)
:ref:`Position <no-29738>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-29739>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-29740>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-29741>`                  The position of the right side of the object. This is a
:ref:`Size <no-29742>`                   The size of the object. (tuple)
:ref:`Sizer <no-29743>`                  The sizer for the object.
:ref:`StatusText <no-29744>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-29745>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-29746>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-29747>`                    The top position of the object. (int)
:ref:`Transparency <no-29748>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-29749>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-29750>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-29751>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-29752>`                  The width of the object. (int)
:ref:`WindowHandle <no-29753>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-29666:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29667:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29668:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29669:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29670:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29671:

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

.. _no-29672:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29673:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29674:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29675:

**Caption** 

Specifies the text of the menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29676:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29677:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29678:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29679:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29680:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29681:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29682:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29683:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29684:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29685:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29686:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29687:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29688:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29689:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29690:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29691:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29692:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29693:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29694:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29695:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29696:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29697:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29698:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29699:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29700:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29701:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29702:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29703:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29704:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29705:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29706:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29707:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29708:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29709:

**Enabled** 

Specifies whether the menu can be interacted with. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29710:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29711:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29712:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29713:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29714:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29715:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29716:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29717:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29718:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29719:

**Form** 

Specifies the form that contains the menu.  (dForm)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29720:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29721:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29722:

**HelpText** 

Specifies the help text associated with this menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29723:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29724:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29725:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29726:

**MRU** 

Determines if this menu uses Most Recently Used behavior. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29727:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29728:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29729:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29730:

**MenuID** 

Identifying value for this menu. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that MenuID values
    are unique.  (varies)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29731:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29732:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29733:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29734:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29735:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29736:

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

.. _no-29737:

**Parent** 

Specifies the parent menu or menubar.  (varies)


Inherited from: 'wx._core.Menu - can not provide a link

-------

.. _no-29738:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29739:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29740:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29741:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29742:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29743:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29744:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29745:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29746:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29747:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29748:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29749:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29750:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29751:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29752:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29753:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-29754>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-29755>`                 Occurs after the control or form is created.
:ref:`Destroy <no-29756>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-29757>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-29758>`               Occurs when the control gets the focus.
:ref:`Idle <no-29759>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-29760>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-29761>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-29762>`               
:ref:`KeyUp <no-29763>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-29764>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-29765>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-29766>`              
:ref:`MenuHighlight <no-29767>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-29768>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-29769>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-29770>`             
:ref:`MouseLeave <no-29771>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-29772>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-29773>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-29774>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-29775>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-29776>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-29777>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-29778>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-29779>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-29780>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-29781>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-29782>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-29783>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-29784>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-29785>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-29786>`                   Occurs when the control's position changes.
:ref:`Paint <no-29787>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-29788>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-29789>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-29790>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-29791>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-29754:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-29755:

**Create** 

Occurs after the control or form is created.



-------

.. _no-29756:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-29757:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-29758:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-29759:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-29760:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-29761:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-29762:

**KeyEvent** 



-------

.. _no-29763:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-29764:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-29765:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-29766:

**MenuEvent** 



-------

.. _no-29767:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-29768:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-29769:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-29770:

**MouseEvent** 



-------

.. _no-29771:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-29772:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-29773:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-29774:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-29775:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-29776:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-29777:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-29778:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-29779:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-29780:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-29781:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-29782:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-29783:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-29784:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-29785:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-29786:

**Move** 

Occurs when the control's position changes.



-------

.. _no-29787:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-29788:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-29789:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-29790:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-29791:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-29792>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-29793>`             Instantiate object as a child of self.
:ref:`afterInit <no-29794>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-29795>`          
:ref:`afterSetProperties <no-29796>`    
:ref:`append <no-29797>`                Append a dMenuItem with the specified properties.
:ref:`appendItem <no-29798>`            Insert a dMenuItem at the bottom of the menu.
:ref:`appendMenu <no-29799>`            Insert a dMenu at the bottom of the menu.
:ref:`appendSeparator <no-29800>`       Insert a separator at the bottom of the menu.
:ref:`autoBindEvents <no-29801>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-29802>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-29803>`   
:ref:`bindEvent <no-29804>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-29805>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-29806>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-29807>`          Makes this object topmost
:ref:`clear <no-29808>`                 Removes all items in this menu.
:ref:`clearChecks <no-29809>`           Unchecks any checkmark-type menu items.
:ref:`clone <no-29810>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-29811>`  Given a position relative to this control, return a position relative
:ref:`copy <no-29812>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-29813>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-29814>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-29815>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-29816>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-29817>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-29818>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-29819>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-29820>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-29821>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-29822>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-29823>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-29824>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-29825>`              Draws text on the object at the specified position
:ref:`endHover <no-29826>`              
:ref:`fitToSizer <no-29827>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-29828>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-29829>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-29830>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-29831>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-29832>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-29833>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-29834>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-29835>`      Returns an object that locks the current display when created, and
:ref:`getItem <no-29836>`               Returns a reference to the menu item with the specified ItemID or Caption.
:ref:`getItemIndex <no-29837>`          Returns the index of the item with the specified caption; you can
:ref:`getMousePosition <no-29838>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-29839>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-29840>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-29841>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-29842>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-29843>`                  Make the object invisible.
:ref:`initEvents <no-29844>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-29845>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-29846>`                Insert a dMenuItem at the given position with the specified properties.
:ref:`insertItem <no-29847>`            Insert a dMenuItem before the specified position in the menu.
:ref:`insertMenu <no-29848>`            Insert a dMenu before the specified position in the menu.
:ref:`insertSeparator <no-29849>`       Insert a separator before the specified position in the menu.
:ref:`isContainedBy <no-29850>`         Returns True if the containership hierarchy for this control
:ref:`isItemChecked <no-29851>`         
:ref:`iterateCall <no-29852>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-29853>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-29854>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-29855>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-29856>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-29857>`               
:ref:`paste <no-29858>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-29859>`           
:ref:`prepend <no-29860>`               Prepend a dMenuItem with the specified properties.
:ref:`prependItem <no-29861>`           Insert a dMenuItem at the top of the menu.
:ref:`prependMenu <no-29862>`           Insert a dMenu at the top of the menu.
:ref:`prependSeparator <no-29863>`      Insert a separator at the top of the menu.
:ref:`processDroppedFiles <no-29864>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-29865>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-29866>`            Raise the passed Dabo event.
:ref:`reCreate <no-29867>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-29868>`              Recreate the object.
:ref:`redraw <no-29869>`                Called when the object is (re)drawn.
:ref:`refresh <no-29870>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-29871>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-29872>`               Destroys the object.
:ref:`remove <no-29873>`                Removes the specified item from the menu. You may specify the item by
:ref:`removeDrawnObject <no-29874>`     
:ref:`sendToBack <no-29875>`            Places this object behind all others.
:ref:`setAll <no-29876>`                Set all child object properties to the passed value.
:ref:`setCheck <no-29877>`              When using checkmark-type menus, passing either the item
:ref:`setFocus <no-29878>`              Sets focus to the object.
:ref:`setItemCheck <no-29879>`          Pass a menu item and a boolean value, and the checked
:ref:`setPositionInSizer <no-29880>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-29881>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-29882>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-29883>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-29884>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-29885>`                  Make the object visible.
:ref:`showContainingPage <no-29886>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-29887>`       Display a context menu (popup) at the specified position.
:ref:`super <no-29888>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-29889>`           Remove a previously registered event binding.
:ref:`unbindKey <no-29890>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-29891>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-29892>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-29893>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-29792:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29793:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-29794:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29795:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29796:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29797:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.append(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Append a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29798:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.appendItem(self, item)
   :noindex:


   Insert a dMenuItem at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29799:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.appendMenu(self, menu)
   :noindex:


   Insert a dMenu at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29800:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.appendSeparator(self)
   :noindex:


   Insert a separator at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29801:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.autoBindEvents(self, force=True)
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

.. _no-29802:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29803:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29804:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29805:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29806:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-29807:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29808:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.clear(self)
   :noindex:


   Removes all items in this menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29809:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.clearChecks(self)
   :noindex:


   Unchecks any checkmark-type menu items.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29810:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29811:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29812:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29813:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29814:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29815:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29816:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-29817:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29818:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29819:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29820:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29821:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29822:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29823:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29824:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29825:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29826:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29827:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29828:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29829:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29830:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29831:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29832:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29833:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29834:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29835:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29836:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getItem(self, idOrCaption)
   :noindex:


   
   Returns a reference to the menu item with the specified ItemID or Caption.
   The ItemID property is checked first; then the Caption. If no match is found,
   None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29837:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getItemIndex(self, captionOrItem)
   :noindex:


   
   Returns the index of the item with the specified caption; you can
   optionally pass in a reference to the menu item itself. If the item
   isn't found, None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29838:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29839:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29840:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-29841:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29842:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29843:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29844:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29845:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29846:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.insert(self, pos, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Insert a dMenuItem at the given position with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29847:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.insertItem(self, pos, item)
   :noindex:


   Insert a dMenuItem before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29848:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.insertMenu(self, pos, menu)
   :noindex:


   Insert a dMenu before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29849:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.insertSeparator(self, pos)
   :noindex:


   Insert a separator before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29850:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29851:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.isItemChecked(self, capIdxOrItem)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29852:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29853:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.lockDisplay(self)
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

.. _no-29854:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29855:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29856:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29857:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29858:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29859:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29860:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.prepend(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Prepend a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29861:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.prependItem(self, item)
   :noindex:


   Insert a dMenuItem at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29862:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.prependMenu(self, menu)
   :noindex:


   Insert a dMenu at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29863:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.prependSeparator(self)
   :noindex:


   Insert a separator at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29864:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29865:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29866:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29867:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29868:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29869:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29870:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29871:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29872:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29873:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.remove(self, capIdxOrItem, release=True)
   :noindex:


   
   Removes the specified item from the menu. You may specify the item by
   passing its index, its Caption, or by passing the item itself. If release is
   True (the default), the item is destroyed as well. If release is False, a reference
   to the object will be returned, and the caller is responsible for destroying it.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29874:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29875:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29876:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-29877:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setCheck(self, capIdxOrItem, unCheckOthers=True)
   :noindex:


   
   When using checkmark-type menus, passing either the item
   itself, or the index or caption of the item you want checked to
   this method will check that item. If unCheckOthers is True, non-
   matching items will be unchecked.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29878:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29879:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setItemCheck(self, itm, val)
   :noindex:


   
   Pass a menu item and a boolean value, and the checked
   state of that menu item will be set accordingly.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29880:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29881:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-29882:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-29883:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29884:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29885:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29886:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29887:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29888:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29889:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29890:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29891:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29892:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29893:

.. function:: dabo.ui.uiwx.dBaseMenuBar.HelpMenu.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
