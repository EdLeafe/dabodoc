
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBaseMenuBar

.. _dabo.ui.uiwx.dBaseMenuBar.EditMenu:

==============================================
|doc_title|  **dBaseMenuBar.EditMenu** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **EditMenu**

.. inheritance-diagram:: EditMenu


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dMenu.dMenu`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBaseMenuBar.EditMenu


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-29210>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-29211>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-29212>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-29213>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-29214>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-29215>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-29216>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-29217>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-29218>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-29219>`                Specifies the text of the menu.  (str)
:ref:`Children <no-29220>`               Returns a list of object references to the children of
:ref:`Class <no-29221>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-29222>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-29223>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-29224>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-29225>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-29226>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-29227>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-29228>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-29229>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-29230>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-29231>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-29232>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-29233>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-29234>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-29235>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-29236>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-29237>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-29238>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-29239>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-29240>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-29241>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicLeft <no-29242>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-29243>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-29244>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-29245>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-29246>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-29247>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-29248>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-29249>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-29250>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-29251>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-29252>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-29253>`                Specifies whether the menu can be interacted with. Default=True  (bool)
:ref:`Font <no-29254>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-29255>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-29256>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-29257>`               Specifies the font face. (str)
:ref:`FontInfo <no-29258>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-29259>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-29260>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-29261>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-29262>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-29263>`                   Specifies the form that contains the menu.  (dForm)
:ref:`Height <no-29264>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-29265>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-29266>`               Specifies the help text associated with this menu.  (str)
:ref:`Hover <no-29267>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-29268>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-29269>`              Specifies which events to log.  (list of strings)
:ref:`MRU <no-29270>`                    Determines if this menu uses Most Recently Used behavior. Default=False  (bool)
:ref:`MaximumHeight <no-29271>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-29272>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-29273>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MenuID <no-29274>`                 Identifying value for this menu. NOTE: there is no checking for
:ref:`MinimumHeight <no-29275>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-29276>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-29277>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-29278>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-29279>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-29280>`               Specifies the base name of the object.
:ref:`Parent <no-29281>`                 Specifies the parent menu or menubar.  (varies)
:ref:`Position <no-29282>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-29283>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-29284>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-29285>`                  The position of the right side of the object. This is a
:ref:`Size <no-29286>`                   The size of the object. (tuple)
:ref:`Sizer <no-29287>`                  The sizer for the object.
:ref:`StatusText <no-29288>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-29289>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-29290>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-29291>`                    The top position of the object. (int)
:ref:`Transparency <no-29292>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-29293>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-29294>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-29295>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-29296>`                  The width of the object. (int)
:ref:`WindowHandle <no-29297>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-29210:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29211:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29212:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29213:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29214:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29215:

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

.. _no-29216:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29217:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29218:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29219:

**Caption** 

Specifies the text of the menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29220:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29221:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29222:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29223:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29224:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29225:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29226:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29227:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29228:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29229:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29230:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29231:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29232:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29233:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29234:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29235:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29236:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29237:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29238:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29239:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29240:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29241:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29242:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29243:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29244:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29245:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29246:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29247:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29248:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29249:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29250:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29251:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29252:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29253:

**Enabled** 

Specifies whether the menu can be interacted with. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29254:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29255:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29256:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29257:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29258:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29259:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29260:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29261:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29262:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29263:

**Form** 

Specifies the form that contains the menu.  (dForm)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29264:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29265:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29266:

**HelpText** 

Specifies the help text associated with this menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29267:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29268:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29269:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29270:

**MRU** 

Determines if this menu uses Most Recently Used behavior. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29271:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29272:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29273:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29274:

**MenuID** 

Identifying value for this menu. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that MenuID values
    are unique.  (varies)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29275:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29276:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29277:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29278:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29279:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29280:

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

.. _no-29281:

**Parent** 

Specifies the parent menu or menubar.  (varies)


Inherited from: 'wx._core.Menu - can not provide a link

-------

.. _no-29282:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29283:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29284:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29285:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29286:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29287:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29288:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29289:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29290:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29291:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29292:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29293:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29294:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29295:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29296:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29297:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-29298>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-29299>`                 Occurs after the control or form is created.
:ref:`Destroy <no-29300>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-29301>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-29302>`               Occurs when the control gets the focus.
:ref:`Idle <no-29303>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-29304>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-29305>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-29306>`               
:ref:`KeyUp <no-29307>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-29308>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-29309>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-29310>`              
:ref:`MenuHighlight <no-29311>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-29312>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-29313>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-29314>`             
:ref:`MouseLeave <no-29315>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-29316>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-29317>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-29318>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-29319>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-29320>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-29321>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-29322>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-29323>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-29324>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-29325>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-29326>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-29327>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-29328>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-29329>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-29330>`                   Occurs when the control's position changes.
:ref:`Paint <no-29331>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-29332>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-29333>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-29334>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-29335>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-29298:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-29299:

**Create** 

Occurs after the control or form is created.



-------

.. _no-29300:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-29301:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-29302:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-29303:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-29304:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-29305:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-29306:

**KeyEvent** 



-------

.. _no-29307:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-29308:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-29309:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-29310:

**MenuEvent** 



-------

.. _no-29311:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-29312:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-29313:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-29314:

**MouseEvent** 



-------

.. _no-29315:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-29316:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-29317:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-29318:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-29319:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-29320:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-29321:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-29322:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-29323:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-29324:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-29325:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-29326:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-29327:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-29328:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-29329:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-29330:

**Move** 

Occurs when the control's position changes.



-------

.. _no-29331:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-29332:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-29333:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-29334:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-29335:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-29336>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-29337>`             Instantiate object as a child of self.
:ref:`afterInit <no-29338>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-29339>`          
:ref:`afterSetProperties <no-29340>`    
:ref:`append <no-29341>`                Append a dMenuItem with the specified properties.
:ref:`appendItem <no-29342>`            Insert a dMenuItem at the bottom of the menu.
:ref:`appendMenu <no-29343>`            Insert a dMenu at the bottom of the menu.
:ref:`appendSeparator <no-29344>`       Insert a separator at the bottom of the menu.
:ref:`autoBindEvents <no-29345>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-29346>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-29347>`   
:ref:`bindEvent <no-29348>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-29349>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-29350>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-29351>`          Makes this object topmost
:ref:`clear <no-29352>`                 Removes all items in this menu.
:ref:`clearChecks <no-29353>`           Unchecks any checkmark-type menu items.
:ref:`clone <no-29354>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-29355>`  Given a position relative to this control, return a position relative
:ref:`copy <no-29356>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-29357>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-29358>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-29359>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-29360>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-29361>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-29362>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-29363>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-29364>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-29365>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-29366>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-29367>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-29368>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-29369>`              Draws text on the object at the specified position
:ref:`endHover <no-29370>`              
:ref:`fitToSizer <no-29371>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-29372>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-29373>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-29374>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-29375>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-29376>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-29377>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-29378>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-29379>`      Returns an object that locks the current display when created, and
:ref:`getItem <no-29380>`               Returns a reference to the menu item with the specified ItemID or Caption.
:ref:`getItemIndex <no-29381>`          Returns the index of the item with the specified caption; you can
:ref:`getMousePosition <no-29382>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-29383>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-29384>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-29385>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-29386>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-29387>`                  Make the object invisible.
:ref:`initEvents <no-29388>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-29389>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-29390>`                Insert a dMenuItem at the given position with the specified properties.
:ref:`insertItem <no-29391>`            Insert a dMenuItem before the specified position in the menu.
:ref:`insertMenu <no-29392>`            Insert a dMenu before the specified position in the menu.
:ref:`insertSeparator <no-29393>`       Insert a separator before the specified position in the menu.
:ref:`isContainedBy <no-29394>`         Returns True if the containership hierarchy for this control
:ref:`isItemChecked <no-29395>`         
:ref:`iterateCall <no-29396>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-29397>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-29398>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-29399>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-29400>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-29401>`               
:ref:`paste <no-29402>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-29403>`           
:ref:`prepend <no-29404>`               Prepend a dMenuItem with the specified properties.
:ref:`prependItem <no-29405>`           Insert a dMenuItem at the top of the menu.
:ref:`prependMenu <no-29406>`           Insert a dMenu at the top of the menu.
:ref:`prependSeparator <no-29407>`      Insert a separator at the top of the menu.
:ref:`processDroppedFiles <no-29408>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-29409>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-29410>`            Raise the passed Dabo event.
:ref:`reCreate <no-29411>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-29412>`              Recreate the object.
:ref:`redraw <no-29413>`                Called when the object is (re)drawn.
:ref:`refresh <no-29414>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-29415>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-29416>`               Destroys the object.
:ref:`remove <no-29417>`                Removes the specified item from the menu. You may specify the item by
:ref:`removeDrawnObject <no-29418>`     
:ref:`sendToBack <no-29419>`            Places this object behind all others.
:ref:`setAll <no-29420>`                Set all child object properties to the passed value.
:ref:`setCheck <no-29421>`              When using checkmark-type menus, passing either the item
:ref:`setFocus <no-29422>`              Sets focus to the object.
:ref:`setItemCheck <no-29423>`          Pass a menu item and a boolean value, and the checked
:ref:`setPositionInSizer <no-29424>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-29425>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-29426>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-29427>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-29428>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-29429>`                  Make the object visible.
:ref:`showContainingPage <no-29430>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-29431>`       Display a context menu (popup) at the specified position.
:ref:`super <no-29432>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-29433>`           Remove a previously registered event binding.
:ref:`unbindKey <no-29434>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-29435>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-29436>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-29437>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-29336:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29337:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-29338:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29339:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29340:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29341:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.append(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Append a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29342:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.appendItem(self, item)
   :noindex:


   Insert a dMenuItem at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29343:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.appendMenu(self, menu)
   :noindex:


   Insert a dMenu at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29344:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.appendSeparator(self)
   :noindex:


   Insert a separator at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29345:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.autoBindEvents(self, force=True)
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

.. _no-29346:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29347:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29348:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29349:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29350:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-29351:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29352:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.clear(self)
   :noindex:


   Removes all items in this menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29353:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.clearChecks(self)
   :noindex:


   Unchecks any checkmark-type menu items.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29354:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29355:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29356:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29357:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29358:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29359:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29360:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-29361:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29362:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29363:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29364:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29365:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29366:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29367:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29368:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29369:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29370:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29371:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29372:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29373:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29374:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29375:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29376:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29377:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29378:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29379:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29380:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getItem(self, idOrCaption)
   :noindex:


   
   Returns a reference to the menu item with the specified ItemID or Caption.
   The ItemID property is checked first; then the Caption. If no match is found,
   None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29381:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getItemIndex(self, captionOrItem)
   :noindex:


   
   Returns the index of the item with the specified caption; you can
   optionally pass in a reference to the menu item itself. If the item
   isn't found, None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29382:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29383:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29384:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-29385:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29386:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29387:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29388:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29389:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29390:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.insert(self, pos, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Insert a dMenuItem at the given position with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29391:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.insertItem(self, pos, item)
   :noindex:


   Insert a dMenuItem before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29392:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.insertMenu(self, pos, menu)
   :noindex:


   Insert a dMenu before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29393:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.insertSeparator(self, pos)
   :noindex:


   Insert a separator before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29394:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29395:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.isItemChecked(self, capIdxOrItem)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29396:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29397:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.lockDisplay(self)
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

.. _no-29398:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29399:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29400:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29401:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29402:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29403:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29404:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.prepend(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Prepend a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29405:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.prependItem(self, item)
   :noindex:


   Insert a dMenuItem at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29406:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.prependMenu(self, menu)
   :noindex:


   Insert a dMenu at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29407:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.prependSeparator(self)
   :noindex:


   Insert a separator at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29408:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29409:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29410:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29411:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29412:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29413:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29414:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29415:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29416:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29417:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.remove(self, capIdxOrItem, release=True)
   :noindex:


   
   Removes the specified item from the menu. You may specify the item by
   passing its index, its Caption, or by passing the item itself. If release is
   True (the default), the item is destroyed as well. If release is False, a reference
   to the object will be returned, and the caller is responsible for destroying it.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29418:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29419:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29420:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-29421:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setCheck(self, capIdxOrItem, unCheckOthers=True)
   :noindex:


   
   When using checkmark-type menus, passing either the item
   itself, or the index or caption of the item you want checked to
   this method will check that item. If unCheckOthers is True, non-
   matching items will be unchecked.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29422:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29423:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setItemCheck(self, itm, val)
   :noindex:


   
   Pass a menu item and a boolean value, and the checked
   state of that menu item will be set accordingly.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29424:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29425:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-29426:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-29427:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29428:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29429:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29430:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29431:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29432:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29433:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29434:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29435:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29436:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29437:

.. function:: dabo.ui.uiwx.dBaseMenuBar.EditMenu.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
