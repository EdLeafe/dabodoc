
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMenuItem

.. _dabo.ui.uiwx.dMenuItem.dMenuItem:

============================================
|doc_title|  **dMenuItem.dMenuItem** - class
============================================

Creates a menu item, which is usually represented as a string.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dMenuItem**

.. inheritance-diagram:: dMenuItem


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|subclasses| Known Subclasses
=============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMenuItem.dMenuItem

   .. automethod:: dabo.ui.uiwx.dMenuItem.dMenuItem.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-32891>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-32892>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-32893>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-32894>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-32895>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-32896>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-32897>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-32898>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-32899>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-32900>`                Specifies the text of the menu item.
:ref:`Children <no-32901>`               Returns a list of object references to the children of
:ref:`Class <no-32902>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-32903>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-32904>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-32905>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-32906>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-32907>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-32908>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-32909>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-32910>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-32911>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-32912>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-32913>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-32914>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-32915>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-32916>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-32917>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-32918>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-32919>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-32920>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-32921>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-32922>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicIcon <no-32923>`            Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-32924>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-32925>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-32926>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-32927>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-32928>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-32929>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-32930>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-32931>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-32932>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-32933>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-32934>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-32935>`                Specifies whether the menu item can be interacted with.
:ref:`Font <no-32936>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-32937>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-32938>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-32939>`               Specifies the font face. (str)
:ref:`FontInfo <no-32940>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-32941>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-32942>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-32943>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-32944>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-32945>`                   Specifies the containing form.
:ref:`Height <no-32946>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-32947>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-32948>`               Specifies the help text associated with this menu. (str)
:ref:`HotKey <no-32949>`                 Key combination that will trigger the menu  (str)
:ref:`Hover <no-32950>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-32951>`                   Specifies the icon for the menu item.
:ref:`ItemID <no-32952>`                 Identifying value for this menuitem. NOTE: there is no checking for
:ref:`Left <no-32953>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-32954>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-32955>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-32956>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-32957>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-32958>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-32959>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-32960>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-32961>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-32962>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-32963>`               Specifies the base name of the object.
:ref:`Parent <no-32964>`                 Specifies the parent menu.
:ref:`Position <no-32965>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-32966>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-32967>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-32968>`                  The position of the right side of the object. This is a
:ref:`Size <no-32969>`                   The size of the object. (tuple)
:ref:`Sizer <no-32970>`                  The sizer for the object.
:ref:`StatusText <no-32971>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-32972>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-32973>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-32974>`                    The top position of the object. (int)
:ref:`Transparency <no-32975>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-32976>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-32977>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-32978>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-32979>`                  The width of the object. (int)
:ref:`WindowHandle <no-32980>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-32922:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.



-------

.. _no-32923:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.



-------

.. _no-32948:

**HelpText** 

Specifies the help text associated with this menu. (str)



-------

.. _no-32949:

**HotKey** 

Key combination that will trigger the menu  (str)



-------

.. _no-32951:

**Icon** 

Specifies the icon for the menu item.



-------

.. _no-32952:

**ItemID** 

Identifying value for this menuitem. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that ItemID values
    are unique within a menu.  (varies)



-------


Properties - inherited
========================

.. _no-32891:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32892:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32893:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32894:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32895:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32896:

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

.. _no-32897:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32898:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32899:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32900:

**Caption** 

Specifies the text of the menu item.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32901:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32902:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32903:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32904:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32905:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32906:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32907:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32908:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32909:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32910:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32911:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32912:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32913:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32914:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32915:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32916:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32917:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32918:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32919:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32920:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32921:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32924:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32925:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32926:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32927:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32928:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32929:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32930:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32931:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32932:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32933:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32934:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32935:

**Enabled** 

Specifies whether the menu item can be interacted with.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32936:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.MenuItem - can not provide a link

-------

.. _no-32937:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32938:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32939:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32940:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32941:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32942:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32943:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32944:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32945:

**Form** 

Specifies the containing form.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32946:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32947:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32950:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32953:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32954:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32955:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32956:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32957:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32958:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32959:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32960:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32961:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32962:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32963:

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

.. _no-32964:

**Parent** 

Specifies the parent menu.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32965:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32966:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32967:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32968:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32969:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32970:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32971:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32972:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32973:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32974:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32975:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32976:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32977:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32978:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32979:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32980:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-32981>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-32982>`                 Occurs after the control or form is created.
:ref:`Destroy <no-32983>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-32984>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-32985>`               Occurs when the control gets the focus.
:ref:`Hit <no-32986>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-32987>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-32988>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-32989>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-32990>`               
:ref:`KeyUp <no-32991>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-32992>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-32993>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-32994>`              
:ref:`MenuHighlight <no-32995>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-32996>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-32997>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-32998>`             
:ref:`MouseLeave <no-32999>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-33000>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-33001>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-33002>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-33003>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-33004>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-33005>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-33006>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-33007>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-33008>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-33009>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-33010>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-33011>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-33012>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-33013>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-33014>`                   Occurs when the control's position changes.
:ref:`Paint <no-33015>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-33016>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-33017>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-33018>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-33019>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-32981:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-32982:

**Create** 

Occurs after the control or form is created.



-------

.. _no-32983:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-32984:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-32985:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-32986:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-32987:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-32988:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-32989:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-32990:

**KeyEvent** 



-------

.. _no-32991:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-32992:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-32993:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-32994:

**MenuEvent** 



-------

.. _no-32995:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-32996:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-32997:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-32998:

**MouseEvent** 



-------

.. _no-32999:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-33000:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-33001:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-33002:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-33003:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-33004:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-33005:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-33006:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-33007:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-33008:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-33009:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-33010:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-33011:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-33012:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-33013:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-33014:

**Move** 

Occurs when the control's position changes.



-------

.. _no-33015:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-33016:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-33017:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-33018:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-33019:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-33020>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-33021>`             Instantiate object as a child of self.
:ref:`afterInit <no-33022>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-33023>`          
:ref:`afterSetProperties <no-33024>`    
:ref:`autoBindEvents <no-33025>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-33026>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-33027>`   
:ref:`bindEvent <no-33028>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-33029>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-33030>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-33031>`          Makes this object topmost
:ref:`clear <no-33032>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-33033>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-33034>`  Given a position relative to this control, return a position relative
:ref:`copy <no-33035>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-33036>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-33037>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-33038>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-33039>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-33040>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-33041>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-33042>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-33043>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-33044>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-33045>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-33046>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-33047>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-33048>`              Draws text on the object at the specified position
:ref:`endHover <no-33049>`              
:ref:`fitToSizer <no-33050>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-33051>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-33052>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-33053>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-33054>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-33055>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-33056>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-33057>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-33058>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-33059>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-33060>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-33061>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-33062>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-33063>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-33064>`                  Make the object invisible.
:ref:`initEvents <no-33065>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-33066>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-33067>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-33068>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-33069>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-33070>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-33071>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-33072>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-33073>`               
:ref:`paste <no-33074>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-33075>`           
:ref:`processDroppedFiles <no-33076>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-33077>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-33078>`            Raise the passed Dabo event.
:ref:`reCreate <no-33079>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-33080>`              Recreate the object.
:ref:`redraw <no-33081>`                Called when the object is (re)drawn.
:ref:`refresh <no-33082>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-33083>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-33084>`               Destroys the object.
:ref:`removeDrawnObject <no-33085>`     
:ref:`sendToBack <no-33086>`            Places this object behind all others.
:ref:`setAll <no-33087>`                Set all child object properties to the passed value.
:ref:`setFocus <no-33088>`              Sets focus to the object.
:ref:`setPositionInSizer <no-33089>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-33090>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-33091>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-33092>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-33093>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-33094>`                  Make the object visible.
:ref:`showContainingPage <no-33095>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-33096>`       Display a context menu (popup) at the specified position.
:ref:`super <no-33097>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-33098>`           Remove a previously registered event binding.
:ref:`unbindKey <no-33099>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-33100>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-33101>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-33102>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-33020:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33021:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-33022:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33023:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33024:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33025:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.autoBindEvents(self, force=True)
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

.. _no-33026:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33027:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33028:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33029:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33030:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-33031:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33032:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33033:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33034:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33035:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33036:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33037:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33038:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33039:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-33040:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33041:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33042:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33043:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33044:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33045:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33046:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33047:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33048:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33049:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33050:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33051:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33052:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33053:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33054:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33055:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33056:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33057:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33058:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33059:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33060:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33061:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-33062:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33063:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33064:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33065:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33066:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33067:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33068:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33069:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.lockDisplay(self)
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

.. _no-33070:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33071:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33072:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33073:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33074:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33075:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33076:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33077:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33078:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33079:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33080:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33081:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33082:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33083:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33084:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33085:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33086:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33087:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-33088:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33089:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33090:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-33091:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-33092:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33093:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33094:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33095:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33096:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33097:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33098:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33099:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33100:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33101:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33102:

.. function:: dabo.ui.uiwx.dMenuItem.dMenuItem.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
