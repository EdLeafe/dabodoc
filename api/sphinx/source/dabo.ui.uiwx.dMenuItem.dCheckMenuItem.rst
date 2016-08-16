
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMenuItem

.. _dabo.ui.uiwx.dMenuItem.dCheckMenuItem:

=================================================
|doc_title|  **dMenuItem.dCheckMenuItem** - class
=================================================

Creates a checkbox-like item in a menu.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dCheckMenuItem**

.. inheritance-diagram:: dCheckMenuItem


|supclasses| Known Superclasses
===============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-32678>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-32679>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-32680>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-32681>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-32682>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-32683>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-32684>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-32685>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-32686>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-32687>`                Specifies the text of the menu item.
:ref:`Checked <no-32688>`                Is this menu item checked?  (bool)
:ref:`Children <no-32689>`               Returns a list of object references to the children of
:ref:`Class <no-32690>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-32691>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-32692>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-32693>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-32694>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-32695>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-32696>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-32697>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-32698>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-32699>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-32700>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-32701>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-32702>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-32703>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-32704>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-32705>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-32706>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-32707>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-32708>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-32709>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-32710>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicIcon <no-32711>`            Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-32712>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-32713>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-32714>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-32715>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-32716>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-32717>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-32718>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-32719>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-32720>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-32721>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-32722>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-32723>`                Specifies whether the menu item can be interacted with.
:ref:`Font <no-32724>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-32725>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-32726>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-32727>`               Specifies the font face. (str)
:ref:`FontInfo <no-32728>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-32729>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-32730>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-32731>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-32732>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-32733>`                   Specifies the containing form.
:ref:`Height <no-32734>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-32735>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-32736>`               Specifies the help text associated with this menu. (str)
:ref:`HotKey <no-32737>`                 Key combination that will trigger the menu  (str)
:ref:`Hover <no-32738>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-32739>`                   Specifies the icon for the menu item.
:ref:`ItemID <no-32740>`                 Identifying value for this menuitem. NOTE: there is no checking for
:ref:`Left <no-32741>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-32742>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-32743>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-32744>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-32745>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-32746>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-32747>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-32748>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-32749>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-32750>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-32751>`               Specifies the base name of the object.
:ref:`Parent <no-32752>`                 Specifies the parent menu.
:ref:`Position <no-32753>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-32754>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-32755>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-32756>`                  The position of the right side of the object. This is a
:ref:`Size <no-32757>`                   The size of the object. (tuple)
:ref:`Sizer <no-32758>`                  The sizer for the object.
:ref:`StatusText <no-32759>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-32760>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-32761>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-32762>`                    The top position of the object. (int)
:ref:`Transparency <no-32763>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-32764>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-32765>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-32766>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-32767>`                  The width of the object. (int)
:ref:`WindowHandle <no-32768>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-32678:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32679:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32680:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32681:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32682:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32683:

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

.. _no-32684:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32685:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32686:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32687:

**Caption** 

Specifies the text of the menu item.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32688:

**Checked** 

Is this menu item checked?  (bool)


Inherited from: 'dabo.ui.uiwx.dMenuItem._AbstractExtendedMenuItem - can not provide a link

-------

.. _no-32689:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32690:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32691:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32692:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32693:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32694:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32695:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32696:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32697:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32698:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32699:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32700:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32701:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32702:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32703:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32704:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32705:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32706:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32707:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32708:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32709:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32710:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-32711:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-32712:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32713:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32714:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32715:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32716:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32717:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32718:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32719:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32720:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32721:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32722:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32723:

**Enabled** 

Specifies whether the menu item can be interacted with.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32724:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.MenuItem - can not provide a link

-------

.. _no-32725:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32726:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32727:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32728:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32729:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32730:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32731:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32732:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32733:

**Form** 

Specifies the containing form.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32734:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32735:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32736:

**HelpText** 

Specifies the help text associated with this menu. (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-32737:

**HotKey** 

Key combination that will trigger the menu  (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-32738:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32739:

**Icon** 

Specifies the icon for the menu item.


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-32740:

**ItemID** 

Identifying value for this menuitem. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that ItemID values
    are unique within a menu.  (varies)


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-32741:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32742:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32743:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32744:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32745:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32746:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32747:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32748:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32749:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32750:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32751:

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

.. _no-32752:

**Parent** 

Specifies the parent menu.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32753:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32754:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32755:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32756:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32757:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32758:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32759:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32760:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32761:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32762:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32763:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32764:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32765:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32766:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32767:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32768:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-32769>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-32770>`                 Occurs after the control or form is created.
:ref:`Destroy <no-32771>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-32772>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-32773>`               Occurs when the control gets the focus.
:ref:`Hit <no-32774>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-32775>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-32776>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-32777>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-32778>`               
:ref:`KeyUp <no-32779>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-32780>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-32781>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-32782>`              
:ref:`MenuHighlight <no-32783>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-32784>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-32785>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-32786>`             
:ref:`MouseLeave <no-32787>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-32788>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-32789>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-32790>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-32791>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-32792>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-32793>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-32794>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-32795>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-32796>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-32797>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-32798>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-32799>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-32800>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-32801>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-32802>`                   Occurs when the control's position changes.
:ref:`Paint <no-32803>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-32804>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-32805>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-32806>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-32807>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-32769:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-32770:

**Create** 

Occurs after the control or form is created.



-------

.. _no-32771:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-32772:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-32773:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-32774:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-32775:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-32776:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-32777:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-32778:

**KeyEvent** 



-------

.. _no-32779:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-32780:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-32781:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-32782:

**MenuEvent** 



-------

.. _no-32783:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-32784:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-32785:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-32786:

**MouseEvent** 



-------

.. _no-32787:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-32788:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-32789:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-32790:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-32791:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-32792:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-32793:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-32794:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-32795:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-32796:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-32797:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-32798:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-32799:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-32800:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-32801:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-32802:

**Move** 

Occurs when the control's position changes.



-------

.. _no-32803:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-32804:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-32805:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-32806:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-32807:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-32808>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-32809>`             Instantiate object as a child of self.
:ref:`afterInit <no-32810>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-32811>`          
:ref:`afterSetProperties <no-32812>`    
:ref:`autoBindEvents <no-32813>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-32814>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-32815>`   
:ref:`bindEvent <no-32816>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-32817>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-32818>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-32819>`          Makes this object topmost
:ref:`clear <no-32820>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-32821>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-32822>`  Given a position relative to this control, return a position relative
:ref:`copy <no-32823>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-32824>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-32825>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-32826>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-32827>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-32828>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-32829>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-32830>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-32831>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-32832>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-32833>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-32834>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-32835>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-32836>`              Draws text on the object at the specified position
:ref:`endHover <no-32837>`              
:ref:`fitToSizer <no-32838>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-32839>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-32840>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-32841>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-32842>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-32843>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-32844>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-32845>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-32846>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-32847>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-32848>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-32849>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-32850>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-32851>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-32852>`                  Make the object invisible.
:ref:`initEvents <no-32853>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-32854>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-32855>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-32856>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-32857>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-32858>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-32859>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-32860>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-32861>`               
:ref:`paste <no-32862>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-32863>`           
:ref:`processDroppedFiles <no-32864>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-32865>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-32866>`            Raise the passed Dabo event.
:ref:`reCreate <no-32867>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-32868>`              Recreate the object.
:ref:`redraw <no-32869>`                Called when the object is (re)drawn.
:ref:`refresh <no-32870>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-32871>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-32872>`               Destroys the object.
:ref:`removeDrawnObject <no-32873>`     
:ref:`sendToBack <no-32874>`            Places this object behind all others.
:ref:`setAll <no-32875>`                Set all child object properties to the passed value.
:ref:`setFocus <no-32876>`              Sets focus to the object.
:ref:`setPositionInSizer <no-32877>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-32878>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-32879>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-32880>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-32881>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-32882>`                  Make the object visible.
:ref:`showContainingPage <no-32883>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-32884>`       Display a context menu (popup) at the specified position.
:ref:`super <no-32885>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-32886>`           Remove a previously registered event binding.
:ref:`unbindKey <no-32887>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-32888>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-32889>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-32890>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-32808:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32809:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-32810:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32811:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32812:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32813:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.autoBindEvents(self, force=True)
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

.. _no-32814:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32815:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32816:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32817:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32818:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-32819:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32820:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32821:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32822:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32823:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32824:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32825:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32826:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32827:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-32828:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32829:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32830:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32831:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32832:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32833:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32834:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32835:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32836:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32837:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32838:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32839:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32840:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32841:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32842:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32843:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32844:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32845:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32846:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32847:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32848:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32849:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-32850:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32851:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32852:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32853:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32854:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32855:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32856:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32857:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.lockDisplay(self)
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

.. _no-32858:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32859:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32860:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32861:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32862:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32863:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32864:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32865:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32866:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32867:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32868:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32869:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32870:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32871:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32872:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32873:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32874:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32875:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-32876:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32877:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32878:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-32879:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-32880:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32881:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32882:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32883:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32884:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32885:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32886:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32887:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32888:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32889:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32890:

.. function:: dabo.ui.uiwx.dMenuItem.dCheckMenuItem.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
