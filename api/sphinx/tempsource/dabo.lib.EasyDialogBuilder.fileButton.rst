
.. include:: _static/headings.txt

.. module:: dabo.lib.EasyDialogBuilder

.. _dabo.lib.EasyDialogBuilder.fileButton:

=====================================================
|doc_title|  **EasyDialogBuilder.fileButton** - class
=====================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **fileButton**

.. inheritance-diagram:: fileButton


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dButton.dButton`



|API| Class API
===============


.. autoclass:: dabo.lib.EasyDialogBuilder.fileButton

   .. automethod:: dabo.lib.EasyDialogBuilder.fileButton.__init__

|method_summary| Properties Summary
===================================


======================================= ========================
:ref:`Application <no-2232>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-2233>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-2234>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-2235>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-2236>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-2237>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-2238>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-2239>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-2240>`                 The position of the bottom side of the object. This is a
:ref:`CancelButton <no-2241>`           Specifies whether this command button gets clicked on -Escape-.
:ref:`Caption <no-2242>`                The caption of the object. (str)
:ref:`Children <no-2243>`               Returns a list of object references to the children of
:ref:`Class <no-2244>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-2245>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-2246>`   Reference to the sizer item that control's this control's layout.
:ref:`DefaultButton <no-2247>`          Specifies whether this command button gets clicked on -Enter-.
:ref:`DroppedFileHandler <no-2248>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-2249>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-2250>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-2251>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-2252>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-2253>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-2254>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCancelButton <no-2255>`    Dynamically determine the value of the CancelButton property.
:ref:`DynamicCaption <no-2256>`         Dynamically determine the value of the Caption property.
:ref:`DynamicDefaultButton <no-2257>`   Dynamically determine the value of the DefaultButton property.
:ref:`DynamicEnabled <no-2258>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-2259>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-2260>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-2261>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-2262>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-2263>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-2264>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-2265>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-2266>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-2267>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-2268>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-2269>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-2270>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-2271>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-2272>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-2273>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-2274>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-2275>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-2276>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-2277>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-2278>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-2279>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-2280>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-2281>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-2282>`               Specifies the font face. (str)
:ref:`FontInfo <no-2283>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-2284>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-2285>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-2286>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-2287>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-2288>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-2289>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-2290>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-2291>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-2292>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-2293>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-2294>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-2295>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-2296>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-2297>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-2298>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-2299>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-2300>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-2301>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-2302>`               Specifies the base name of the object.
:ref:`Parent <no-2303>`                 The containing object. (obj)
:ref:`Position <no-2304>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-2305>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-2306>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-2307>`                  The position of the right side of the object. This is a
:ref:`Size <no-2308>`                   The size of the object. (tuple)
:ref:`Sizer <no-2309>`                  The sizer for the object.
:ref:`StatusText <no-2310>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-2311>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-2312>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-2313>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-2314>`                    The top position of the object. (int)
:ref:`Transparency <no-2315>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-2316>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-2317>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-2318>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-2319>`                  The width of the object. (int)
:ref:`WindowHandle <no-2320>`           The platform-specific handle for the window. Read-only. (long)

======================================= ========================


Properties - inherited
========================

.. _no-2232:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2233:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2234:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2235:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2236:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2237:

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

.. _no-2238:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2239:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2240:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2241:

**CancelButton** 

Specifies whether this command button gets clicked on -Escape-.


Inherited from: :ref:`dabo.ui.uiwx.dButton.dButton`

-------

.. _no-2242:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2243:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2244:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2245:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2246:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2247:

**DefaultButton** 

Specifies whether this command button gets clicked on -Enter-.


Inherited from: :ref:`dabo.ui.uiwx.dButton.dButton`

-------

.. _no-2248:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2249:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2250:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2251:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2252:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2253:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2254:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2255:

**DynamicCancelButton** 

Dynamically determine the value of the CancelButton property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CancelButton property. If DynamicCancelButton is set to None (the default), CancelButton
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dButton.dButton`

-------

.. _no-2256:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2257:

**DynamicDefaultButton** 

Dynamically determine the value of the DefaultButton property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultButton property. If DynamicDefaultButton is set to None (the default), DefaultButton
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dButton.dButton`

-------

.. _no-2258:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2259:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2260:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2261:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2262:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2263:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2264:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2265:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2266:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2267:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2268:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2269:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2270:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2271:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2272:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2273:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2274:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2275:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2276:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2277:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2278:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2279:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2280:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2281:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2282:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2283:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2284:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2285:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2286:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2287:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2288:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2289:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2290:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2291:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2292:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2293:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2294:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2295:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2296:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2297:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2298:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2299:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2300:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2301:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2302:

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

.. _no-2303:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2304:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2305:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2306:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2307:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2308:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2309:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2310:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2311:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-2312:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2313:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2314:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2315:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2316:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2317:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2318:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2319:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2320:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-2321>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-2322>`                 Occurs after the control or form is created.
:ref:`Destroy <no-2323>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-2324>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-2325>`               Occurs when the control gets the focus.
:ref:`Hit <no-2326>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-2327>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-2328>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-2329>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-2330>`               
:ref:`KeyUp <no-2331>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-2332>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-2333>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-2334>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-2335>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-2336>`             
:ref:`MouseLeave <no-2337>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-2338>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-2339>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-2340>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-2341>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-2342>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-2343>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-2344>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-2345>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-2346>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-2347>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-2348>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-2349>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-2350>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-2351>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-2352>`                   Occurs when the control's position changes.
:ref:`Paint <no-2353>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-2354>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-2355>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-2356>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-2357>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-2321:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-2322:

**Create** 

Occurs after the control or form is created.



-------

.. _no-2323:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-2324:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-2325:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-2326:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-2327:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-2328:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-2329:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-2330:

**KeyEvent** 



-------

.. _no-2331:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-2332:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-2333:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-2334:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-2335:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-2336:

**MouseEvent** 



-------

.. _no-2337:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-2338:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-2339:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-2340:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-2341:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-2342:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-2343:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-2344:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-2345:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-2346:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-2347:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-2348:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-2349:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-2350:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-2351:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-2352:

**Move** 

Occurs when the control's position changes.



-------

.. _no-2353:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-2354:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-2355:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-2356:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-2357:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-2358>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-2359>`             Instantiate object as a child of self.
:ref:`afterInit <no-2360>`             
:ref:`afterInitAll <no-2361>`          
:ref:`afterSetProperties <no-2362>`    
:ref:`autoBindEvents <no-2363>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-2364>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-2365>`   
:ref:`bindEvent <no-2366>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-2367>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-2368>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-2369>`          Makes this object topmost
:ref:`clear <no-2370>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-2371>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-2372>`  Given a position relative to this control, return a position relative
:ref:`copy <no-2373>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-2374>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-2375>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-2376>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-2377>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-2378>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-2379>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-2380>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-2381>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-2382>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-2383>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-2384>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-2385>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-2386>`              Draws text on the object at the specified position
:ref:`endHover <no-2387>`              
:ref:`fitToSizer <no-2388>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-2389>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-2390>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-2391>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-2392>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-2393>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-2394>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-2395>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-2396>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-2397>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-2398>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-2399>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-2400>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-2401>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-2402>`                  Make the object invisible.
:ref:`initEvents <no-2403>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-2404>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-2405>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-2406>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-2407>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-2408>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-2409>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-2410>`     Given a position relative to the form, return a position relative
:ref:`onHit <no-2411>`                 
:ref:`onHover <no-2412>`               
:ref:`paste <no-2413>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-2414>`           
:ref:`processDroppedFiles <no-2415>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-2416>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-2417>`            Raise the passed Dabo event.
:ref:`reCreate <no-2418>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-2419>`              Recreate the object.
:ref:`redraw <no-2420>`                Called when the object is (re)drawn.
:ref:`refresh <no-2421>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-2422>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-2423>`               Destroys the object.
:ref:`removeDrawnObject <no-2424>`     
:ref:`sendToBack <no-2425>`            Places this object behind all others.
:ref:`setAll <no-2426>`                Set all child object properties to the passed value.
:ref:`setFocus <no-2427>`              Sets focus to the object.
:ref:`setPositionInSizer <no-2428>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-2429>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-2430>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-2431>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-2432>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-2433>`                  Make the object visible.
:ref:`showContainingPage <no-2434>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-2435>`       Display a context menu (popup) at the specified position.
:ref:`super <no-2436>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-2437>`           Remove a previously registered event binding.
:ref:`unbindKey <no-2438>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-2439>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-2440>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-2441>`                Update the properties of this object and all contained objects.

====================================== ========================


Methods
=======

.. _no-2360:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.afterInit(self)



-------

.. _no-2411:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.onHit(self, evt)



-------


Methods - inherited
=====================

.. _no-2358:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2359:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-2361:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2362:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2363:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.autoBindEvents(self, force=True)
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

.. _no-2364:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2365:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2366:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2367:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2368:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-2369:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2370:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2371:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2372:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2373:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2374:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2375:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2376:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2377:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-2378:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2379:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2380:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2381:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2382:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2383:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2384:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2385:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2386:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2387:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2388:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2389:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2390:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2391:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2392:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2393:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2394:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2395:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2396:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2397:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2398:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2399:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-2400:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2401:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2402:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2403:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2404:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2405:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2406:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2407:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.lockDisplay(self)
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

.. _no-2408:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2409:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2410:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2412:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2413:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2414:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2415:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2416:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2417:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2418:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2419:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2420:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2421:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2422:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2423:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2424:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2425:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2426:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-2427:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2428:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2429:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-2430:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-2431:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2432:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2433:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2434:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2435:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2436:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2437:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2438:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2439:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2440:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2441:

.. function:: dabo.lib.EasyDialogBuilder.fileButton.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
