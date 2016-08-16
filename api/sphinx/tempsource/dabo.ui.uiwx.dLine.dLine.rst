
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dLine

.. _dabo.ui.uiwx.dLine.dLine:

====================================
|doc_title|  **dLine.dLine** - class
====================================


Creates a horizontal or vertical line.

If Orientation is "Vertical", Height refers to the length of the line.
If Orientation is "Horizontal", Width refers to the length of the line.
The other value refers to how wide the control is, which affects how much
buffer space will enclose the line, which will appear in the center of
this space.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dLine**

.. inheritance-diagram:: dLine


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|subclasses| Known Subclasses
=============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dLine.dLine

   .. automethod:: dabo.ui.uiwx.dLine.dLine.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-28217>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-28218>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-28219>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-28220>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-28221>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-28222>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-28223>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-28224>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-28225>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-28226>`                The caption of the object. (str)
:ref:`Children <no-28227>`               Returns a list of object references to the children of
:ref:`Class <no-28228>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-28229>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-28230>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-28231>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-28232>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-28233>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-28234>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-28235>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-28236>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-28237>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-28238>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-28239>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-28240>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-28241>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-28242>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-28243>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-28244>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-28245>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-28246>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-28247>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-28248>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-28249>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicOrientation <no-28250>`     Dynamically determine the value of the Orientation property.
:ref:`DynamicPosition <no-28251>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-28252>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-28253>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-28254>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-28255>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-28256>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-28257>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-28258>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-28259>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-28260>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-28261>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-28262>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-28263>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-28264>`               Specifies the font face. (str)
:ref:`FontInfo <no-28265>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-28266>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-28267>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-28268>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-28269>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-28270>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-28271>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-28272>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-28273>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-28274>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-28275>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-28276>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-28277>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-28278>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-28279>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-28280>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-28281>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-28282>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-28283>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-28284>`               Specifies the base name of the object.
:ref:`Orientation <no-28285>`            Specifies the Orientation of the line. (str)
:ref:`Parent <no-28286>`                 The containing object. (obj)
:ref:`Position <no-28287>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-28288>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-28289>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-28290>`                  The position of the right side of the object. This is a
:ref:`Size <no-28291>`                   The size of the object. (tuple)
:ref:`Sizer <no-28292>`                  The sizer for the object.
:ref:`StatusText <no-28293>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-28294>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-28295>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-28296>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-28297>`                    The top position of the object. (int)
:ref:`Transparency <no-28298>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-28299>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-28300>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-28301>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-28302>`                  The width of the object. (int)
:ref:`WindowHandle <no-28303>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-28250:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-28285:

**Orientation** 

Specifies the Orientation of the line. (str) 
   Horizontal (default) 
   VerticalThis is determined by the Width and Height properties. If the Width is greater than the Height, it will be Horizontal. Otherwise, it will be Vertical.



-------


Properties - inherited
========================

.. _no-28217:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28218:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28219:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28220:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28221:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28222:

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

.. _no-28223:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28224:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28225:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28226:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28227:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28228:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28229:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28230:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28231:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28232:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28233:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28234:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28235:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28236:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28237:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28238:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28239:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28240:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28241:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28242:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28243:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28244:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28245:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28246:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28247:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28248:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28249:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28251:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28252:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28253:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28254:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28255:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28256:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28257:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28258:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28259:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28260:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28261:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28262:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28263:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28264:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28265:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28266:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28267:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28268:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28269:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28270:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28271:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28272:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28273:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28274:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28275:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28276:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28277:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28278:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28279:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28280:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28281:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28282:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28283:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28284:

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

.. _no-28286:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28287:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28288:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28289:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28290:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28291:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28292:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28293:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28294:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-28295:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28296:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28297:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28298:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28299:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28300:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28301:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28302:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28303:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-28304>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-28305>`                 Occurs after the control or form is created.
:ref:`Destroy <no-28306>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-28307>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-28308>`               Occurs when the control gets the focus.
:ref:`Idle <no-28309>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-28310>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-28311>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-28312>`               
:ref:`KeyUp <no-28313>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-28314>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-28315>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-28316>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-28317>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-28318>`             
:ref:`MouseLeave <no-28319>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-28320>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-28321>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-28322>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-28323>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-28324>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-28325>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-28326>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-28327>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-28328>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-28329>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-28330>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-28331>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-28332>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-28333>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-28334>`                   Occurs when the control's position changes.
:ref:`Paint <no-28335>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-28336>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-28337>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-28338>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-28339>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-28304:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-28305:

**Create** 

Occurs after the control or form is created.



-------

.. _no-28306:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-28307:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-28308:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-28309:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-28310:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-28311:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-28312:

**KeyEvent** 



-------

.. _no-28313:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-28314:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-28315:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-28316:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-28317:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-28318:

**MouseEvent** 



-------

.. _no-28319:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-28320:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-28321:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-28322:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-28323:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-28324:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-28325:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-28326:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-28327:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-28328:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-28329:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-28330:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-28331:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-28332:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-28333:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-28334:

**Move** 

Occurs when the control's position changes.



-------

.. _no-28335:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-28336:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-28337:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-28338:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-28339:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-28340>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-28341>`             Instantiate object as a child of self.
:ref:`afterInit <no-28342>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-28343>`          
:ref:`afterSetProperties <no-28344>`    
:ref:`autoBindEvents <no-28345>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-28346>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-28347>`   
:ref:`bindEvent <no-28348>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-28349>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-28350>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-28351>`          Makes this object topmost
:ref:`clear <no-28352>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-28353>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-28354>`  Given a position relative to this control, return a position relative
:ref:`copy <no-28355>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-28356>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-28357>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-28358>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-28359>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-28360>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-28361>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-28362>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-28363>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-28364>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-28365>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-28366>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-28367>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-28368>`              Draws text on the object at the specified position
:ref:`endHover <no-28369>`              
:ref:`fitToSizer <no-28370>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-28371>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-28372>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-28373>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-28374>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-28375>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-28376>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-28377>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-28378>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-28379>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-28380>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-28381>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-28382>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-28383>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-28384>`                  Make the object invisible.
:ref:`initEvents <no-28385>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-28386>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-28387>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-28388>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-28389>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-28390>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-28391>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-28392>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-28393>`               
:ref:`paste <no-28394>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-28395>`           
:ref:`processDroppedFiles <no-28396>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-28397>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-28398>`            Raise the passed Dabo event.
:ref:`reCreate <no-28399>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-28400>`              Recreate the object.
:ref:`redraw <no-28401>`                Called when the object is (re)drawn.
:ref:`refresh <no-28402>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-28403>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-28404>`               Destroys the object.
:ref:`removeDrawnObject <no-28405>`     
:ref:`sendToBack <no-28406>`            Places this object behind all others.
:ref:`setAll <no-28407>`                Set all child object properties to the passed value.
:ref:`setFocus <no-28408>`              Sets focus to the object.
:ref:`setPositionInSizer <no-28409>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-28410>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-28411>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-28412>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-28413>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-28414>`                  Make the object visible.
:ref:`showContainingPage <no-28415>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-28416>`       Display a context menu (popup) at the specified position.
:ref:`super <no-28417>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-28418>`           Remove a previously registered event binding.
:ref:`unbindKey <no-28419>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-28420>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-28421>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-28422>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-28340:

.. function:: dabo.ui.uiwx.dLine.dLine.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28341:

.. function:: dabo.ui.uiwx.dLine.dLine.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-28342:

.. function:: dabo.ui.uiwx.dLine.dLine.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28343:

.. function:: dabo.ui.uiwx.dLine.dLine.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28344:

.. function:: dabo.ui.uiwx.dLine.dLine.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28345:

.. function:: dabo.ui.uiwx.dLine.dLine.autoBindEvents(self, force=True)
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

.. _no-28346:

.. function:: dabo.ui.uiwx.dLine.dLine.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28347:

.. function:: dabo.ui.uiwx.dLine.dLine.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28348:

.. function:: dabo.ui.uiwx.dLine.dLine.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28349:

.. function:: dabo.ui.uiwx.dLine.dLine.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28350:

.. function:: dabo.ui.uiwx.dLine.dLine.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-28351:

.. function:: dabo.ui.uiwx.dLine.dLine.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28352:

.. function:: dabo.ui.uiwx.dLine.dLine.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28353:

.. function:: dabo.ui.uiwx.dLine.dLine.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28354:

.. function:: dabo.ui.uiwx.dLine.dLine.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28355:

.. function:: dabo.ui.uiwx.dLine.dLine.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28356:

.. function:: dabo.ui.uiwx.dLine.dLine.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28357:

.. function:: dabo.ui.uiwx.dLine.dLine.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28358:

.. function:: dabo.ui.uiwx.dLine.dLine.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28359:

.. function:: dabo.ui.uiwx.dLine.dLine.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-28360:

.. function:: dabo.ui.uiwx.dLine.dLine.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28361:

.. function:: dabo.ui.uiwx.dLine.dLine.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28362:

.. function:: dabo.ui.uiwx.dLine.dLine.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28363:

.. function:: dabo.ui.uiwx.dLine.dLine.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28364:

.. function:: dabo.ui.uiwx.dLine.dLine.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28365:

.. function:: dabo.ui.uiwx.dLine.dLine.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28366:

.. function:: dabo.ui.uiwx.dLine.dLine.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28367:

.. function:: dabo.ui.uiwx.dLine.dLine.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28368:

.. function:: dabo.ui.uiwx.dLine.dLine.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28369:

.. function:: dabo.ui.uiwx.dLine.dLine.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28370:

.. function:: dabo.ui.uiwx.dLine.dLine.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28371:

.. function:: dabo.ui.uiwx.dLine.dLine.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28372:

.. function:: dabo.ui.uiwx.dLine.dLine.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28373:

.. function:: dabo.ui.uiwx.dLine.dLine.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28374:

.. function:: dabo.ui.uiwx.dLine.dLine.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28375:

.. function:: dabo.ui.uiwx.dLine.dLine.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28376:

.. function:: dabo.ui.uiwx.dLine.dLine.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28377:

.. function:: dabo.ui.uiwx.dLine.dLine.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28378:

.. function:: dabo.ui.uiwx.dLine.dLine.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28379:

.. function:: dabo.ui.uiwx.dLine.dLine.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28380:

.. function:: dabo.ui.uiwx.dLine.dLine.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28381:

.. function:: dabo.ui.uiwx.dLine.dLine.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-28382:

.. function:: dabo.ui.uiwx.dLine.dLine.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28383:

.. function:: dabo.ui.uiwx.dLine.dLine.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28384:

.. function:: dabo.ui.uiwx.dLine.dLine.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28385:

.. function:: dabo.ui.uiwx.dLine.dLine.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28386:

.. function:: dabo.ui.uiwx.dLine.dLine.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28387:

.. function:: dabo.ui.uiwx.dLine.dLine.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28388:

.. function:: dabo.ui.uiwx.dLine.dLine.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28389:

.. function:: dabo.ui.uiwx.dLine.dLine.lockDisplay(self)
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

.. _no-28390:

.. function:: dabo.ui.uiwx.dLine.dLine.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28391:

.. function:: dabo.ui.uiwx.dLine.dLine.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28392:

.. function:: dabo.ui.uiwx.dLine.dLine.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28393:

.. function:: dabo.ui.uiwx.dLine.dLine.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28394:

.. function:: dabo.ui.uiwx.dLine.dLine.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28395:

.. function:: dabo.ui.uiwx.dLine.dLine.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28396:

.. function:: dabo.ui.uiwx.dLine.dLine.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28397:

.. function:: dabo.ui.uiwx.dLine.dLine.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28398:

.. function:: dabo.ui.uiwx.dLine.dLine.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28399:

.. function:: dabo.ui.uiwx.dLine.dLine.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28400:

.. function:: dabo.ui.uiwx.dLine.dLine.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28401:

.. function:: dabo.ui.uiwx.dLine.dLine.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28402:

.. function:: dabo.ui.uiwx.dLine.dLine.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28403:

.. function:: dabo.ui.uiwx.dLine.dLine.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28404:

.. function:: dabo.ui.uiwx.dLine.dLine.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28405:

.. function:: dabo.ui.uiwx.dLine.dLine.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28406:

.. function:: dabo.ui.uiwx.dLine.dLine.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28407:

.. function:: dabo.ui.uiwx.dLine.dLine.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-28408:

.. function:: dabo.ui.uiwx.dLine.dLine.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28409:

.. function:: dabo.ui.uiwx.dLine.dLine.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28410:

.. function:: dabo.ui.uiwx.dLine.dLine.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-28411:

.. function:: dabo.ui.uiwx.dLine.dLine.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-28412:

.. function:: dabo.ui.uiwx.dLine.dLine.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28413:

.. function:: dabo.ui.uiwx.dLine.dLine.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28414:

.. function:: dabo.ui.uiwx.dLine.dLine.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28415:

.. function:: dabo.ui.uiwx.dLine.dLine.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28416:

.. function:: dabo.ui.uiwx.dLine.dLine.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28417:

.. function:: dabo.ui.uiwx.dLine.dLine.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28418:

.. function:: dabo.ui.uiwx.dLine.dLine.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28419:

.. function:: dabo.ui.uiwx.dLine.dLine.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28420:

.. function:: dabo.ui.uiwx.dLine.dLine.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28421:

.. function:: dabo.ui.uiwx.dLine.dLine.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28422:

.. function:: dabo.ui.uiwx.dLine.dLine.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
