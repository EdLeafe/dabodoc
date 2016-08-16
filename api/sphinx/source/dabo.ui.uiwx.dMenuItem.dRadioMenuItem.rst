
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMenuItem

.. _dabo.ui.uiwx.dMenuItem.dRadioMenuItem:

=================================================
|doc_title|  **dMenuItem.dRadioMenuItem** - class
=================================================

Creates a radiobox-like item in a menu.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dRadioMenuItem**

.. inheritance-diagram:: dRadioMenuItem


|supclasses| Known Superclasses
===============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-33103>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-33104>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-33105>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-33106>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-33107>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-33108>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-33109>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-33110>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-33111>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-33112>`                Specifies the text of the menu item.
:ref:`Checked <no-33113>`                Is this menu item checked?  (bool)
:ref:`Children <no-33114>`               Returns a list of object references to the children of
:ref:`Class <no-33115>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-33116>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-33117>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-33118>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-33119>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-33120>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-33121>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-33122>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-33123>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-33124>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-33125>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-33126>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-33127>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-33128>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-33129>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-33130>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-33131>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-33132>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-33133>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-33134>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-33135>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicIcon <no-33136>`            Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-33137>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-33138>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-33139>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-33140>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-33141>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-33142>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-33143>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-33144>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-33145>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-33146>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-33147>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-33148>`                Specifies whether the menu item can be interacted with.
:ref:`Font <no-33149>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-33150>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-33151>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-33152>`               Specifies the font face. (str)
:ref:`FontInfo <no-33153>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-33154>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-33155>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-33156>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-33157>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-33158>`                   Specifies the containing form.
:ref:`Height <no-33159>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-33160>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-33161>`               Specifies the help text associated with this menu. (str)
:ref:`HotKey <no-33162>`                 Key combination that will trigger the menu  (str)
:ref:`Hover <no-33163>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-33164>`                   Specifies the icon for the menu item.
:ref:`ItemID <no-33165>`                 Identifying value for this menuitem. NOTE: there is no checking for
:ref:`Left <no-33166>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-33167>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-33168>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-33169>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-33170>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-33171>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-33172>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-33173>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-33174>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-33175>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-33176>`               Specifies the base name of the object.
:ref:`Parent <no-33177>`                 Specifies the parent menu.
:ref:`Position <no-33178>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-33179>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-33180>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-33181>`                  The position of the right side of the object. This is a
:ref:`Size <no-33182>`                   The size of the object. (tuple)
:ref:`Sizer <no-33183>`                  The sizer for the object.
:ref:`StatusText <no-33184>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-33185>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-33186>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-33187>`                    The top position of the object. (int)
:ref:`Transparency <no-33188>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-33189>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-33190>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-33191>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-33192>`                  The width of the object. (int)
:ref:`WindowHandle <no-33193>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-33103:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33104:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33105:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33106:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33107:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33108:

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

.. _no-33109:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33110:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33111:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33112:

**Caption** 

Specifies the text of the menu item.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33113:

**Checked** 

Is this menu item checked?  (bool)


Inherited from: 'dabo.ui.uiwx.dMenuItem._AbstractExtendedMenuItem - can not provide a link

-------

.. _no-33114:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33115:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33116:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33117:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33118:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33119:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33120:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33121:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33122:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33123:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33124:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33125:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33126:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33127:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33128:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33129:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33130:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33131:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33132:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33133:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33134:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33135:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-33136:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-33137:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33138:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33139:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33140:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33141:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33142:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33143:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33144:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33145:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33146:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33147:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33148:

**Enabled** 

Specifies whether the menu item can be interacted with.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33149:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.MenuItem - can not provide a link

-------

.. _no-33150:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33151:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33152:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33153:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33154:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33155:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33156:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33157:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33158:

**Form** 

Specifies the containing form.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33159:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33160:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33161:

**HelpText** 

Specifies the help text associated with this menu. (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-33162:

**HotKey** 

Key combination that will trigger the menu  (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-33163:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33164:

**Icon** 

Specifies the icon for the menu item.


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-33165:

**ItemID** 

Identifying value for this menuitem. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that ItemID values
    are unique within a menu.  (varies)


Inherited from: :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`

-------

.. _no-33166:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33167:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33168:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33169:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33170:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33171:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33172:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33173:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33174:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33175:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33176:

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

.. _no-33177:

**Parent** 

Specifies the parent menu.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33178:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33179:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33180:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33181:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33182:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33183:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33184:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33185:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33186:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33187:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33188:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33189:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33190:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33191:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33192:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33193:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-33194>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-33195>`                 Occurs after the control or form is created.
:ref:`Destroy <no-33196>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-33197>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-33198>`               Occurs when the control gets the focus.
:ref:`Hit <no-33199>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-33200>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-33201>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-33202>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-33203>`               
:ref:`KeyUp <no-33204>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-33205>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-33206>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-33207>`              
:ref:`MenuHighlight <no-33208>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-33209>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-33210>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-33211>`             
:ref:`MouseLeave <no-33212>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-33213>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-33214>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-33215>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-33216>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-33217>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-33218>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-33219>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-33220>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-33221>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-33222>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-33223>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-33224>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-33225>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-33226>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-33227>`                   Occurs when the control's position changes.
:ref:`Paint <no-33228>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-33229>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-33230>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-33231>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-33232>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-33194:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-33195:

**Create** 

Occurs after the control or form is created.



-------

.. _no-33196:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-33197:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-33198:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-33199:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-33200:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-33201:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-33202:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-33203:

**KeyEvent** 



-------

.. _no-33204:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-33205:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-33206:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-33207:

**MenuEvent** 



-------

.. _no-33208:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-33209:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-33210:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-33211:

**MouseEvent** 



-------

.. _no-33212:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-33213:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-33214:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-33215:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-33216:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-33217:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-33218:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-33219:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-33220:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-33221:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-33222:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-33223:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-33224:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-33225:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-33226:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-33227:

**Move** 

Occurs when the control's position changes.



-------

.. _no-33228:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-33229:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-33230:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-33231:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-33232:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-33233>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-33234>`             Instantiate object as a child of self.
:ref:`afterInit <no-33235>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-33236>`          
:ref:`afterSetProperties <no-33237>`    
:ref:`autoBindEvents <no-33238>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-33239>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-33240>`   
:ref:`bindEvent <no-33241>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-33242>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-33243>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-33244>`          Makes this object topmost
:ref:`clear <no-33245>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-33246>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-33247>`  Given a position relative to this control, return a position relative
:ref:`copy <no-33248>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-33249>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-33250>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-33251>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-33252>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-33253>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-33254>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-33255>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-33256>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-33257>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-33258>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-33259>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-33260>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-33261>`              Draws text on the object at the specified position
:ref:`endHover <no-33262>`              
:ref:`fitToSizer <no-33263>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-33264>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-33265>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-33266>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-33267>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-33268>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-33269>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-33270>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-33271>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-33272>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-33273>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-33274>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-33275>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-33276>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-33277>`                  Make the object invisible.
:ref:`initEvents <no-33278>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-33279>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-33280>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-33281>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-33282>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-33283>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-33284>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-33285>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-33286>`               
:ref:`paste <no-33287>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-33288>`           
:ref:`processDroppedFiles <no-33289>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-33290>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-33291>`            Raise the passed Dabo event.
:ref:`reCreate <no-33292>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-33293>`              Recreate the object.
:ref:`redraw <no-33294>`                Called when the object is (re)drawn.
:ref:`refresh <no-33295>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-33296>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-33297>`               Destroys the object.
:ref:`removeDrawnObject <no-33298>`     
:ref:`sendToBack <no-33299>`            Places this object behind all others.
:ref:`setAll <no-33300>`                Set all child object properties to the passed value.
:ref:`setFocus <no-33301>`              Sets focus to the object.
:ref:`setPositionInSizer <no-33302>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-33303>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-33304>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-33305>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-33306>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-33307>`                  Make the object visible.
:ref:`showContainingPage <no-33308>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-33309>`       Display a context menu (popup) at the specified position.
:ref:`super <no-33310>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-33311>`           Remove a previously registered event binding.
:ref:`unbindKey <no-33312>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-33313>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-33314>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-33315>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-33233:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33234:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-33235:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33236:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33237:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33238:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.autoBindEvents(self, force=True)
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

.. _no-33239:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33240:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33241:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33242:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33243:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-33244:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33245:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33246:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33247:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33248:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33249:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33250:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33251:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33252:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-33253:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33254:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33255:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33256:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33257:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33258:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33259:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33260:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33261:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33262:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33263:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33264:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33265:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33266:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33267:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33268:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33269:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33270:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33271:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33272:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33273:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33274:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-33275:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33276:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33277:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33278:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33279:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33280:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33281:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33282:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.lockDisplay(self)
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

.. _no-33283:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33284:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33285:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33286:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33287:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33288:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33289:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33290:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33291:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33292:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33293:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33294:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33295:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33296:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33297:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33298:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33299:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33300:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-33301:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33302:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33303:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-33304:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-33305:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33306:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33307:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33308:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33309:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33310:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33311:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33312:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33313:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33314:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33315:

.. function:: dabo.ui.uiwx.dMenuItem.dRadioMenuItem.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
