
.. include:: _static/headings.txt

.. module:: dabo.ui.dControlMixinBase

.. _dabo.ui.dControlMixinBase.dControlMixinBase:

============================================================
|doc_title|  **dControlMixinBase.dControlMixinBase** - class
============================================================

Provide common functionality for all controls.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dControlMixinBase**

.. inheritance-diagram:: dControlMixinBase


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.dControlMixinBase.dControlMixinBase


|method_summary| Properties Summary
===================================


======================================= ========================
:ref:`Application <no-6355>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-6356>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-6357>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-6358>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-6359>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-6360>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-6361>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-6362>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-6363>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-6364>`                The caption of the object. (str)
:ref:`Children <no-6365>`               Returns a list of object references to the children of
:ref:`Class <no-6366>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-6367>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-6368>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-6369>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-6370>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-6371>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-6372>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-6373>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-6374>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-6375>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-6376>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-6377>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-6378>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-6379>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-6380>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-6381>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-6382>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-6383>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-6384>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-6385>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-6386>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-6387>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-6388>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-6389>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-6390>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-6391>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-6392>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-6393>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-6394>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-6395>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-6396>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-6397>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-6398>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-6399>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-6400>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-6401>`               Specifies the font face. (str)
:ref:`FontInfo <no-6402>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-6403>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-6404>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-6405>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-6406>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-6407>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-6408>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-6409>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-6410>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-6411>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-6412>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-6413>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-6414>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-6415>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-6416>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-6417>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-6418>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-6419>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-6420>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-6421>`               Specifies the base name of the object.
:ref:`Parent <no-6422>`                 The containing object. (obj)
:ref:`Position <no-6423>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-6424>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-6425>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-6426>`                  The position of the right side of the object. This is a
:ref:`Size <no-6427>`                   The size of the object. (tuple)
:ref:`Sizer <no-6428>`                  The sizer for the object.
:ref:`StatusText <no-6429>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-6430>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-6431>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-6432>`                    The top position of the object. (int)
:ref:`Transparency <no-6433>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-6434>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-6435>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-6436>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-6437>`                  The width of the object. (int)
:ref:`WindowHandle <no-6438>`           The platform-specific handle for the window. Read-only. (long)

======================================= ========================


Properties - inherited
========================

.. _no-6355:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6356:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6357:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6358:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6359:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6360:

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

.. _no-6361:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6362:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6363:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6364:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6365:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6366:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6367:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6368:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6369:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6370:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6371:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6372:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6373:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6374:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6375:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6376:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6377:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6378:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6379:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6380:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6381:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6382:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6383:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6384:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6385:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6386:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6387:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6388:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6389:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6390:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6391:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6392:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6393:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6394:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6395:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6396:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6397:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6398:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6399:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6400:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6401:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6402:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6403:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6404:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6405:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6406:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6407:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6408:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6409:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6410:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6411:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6412:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6413:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6414:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6415:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6416:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6417:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6418:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6419:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6420:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6421:

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

.. _no-6422:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6423:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6424:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6425:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6426:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6427:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6428:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6429:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6430:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6431:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6432:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6433:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6434:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6435:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6436:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6437:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6438:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-6439>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-6440>`                 Occurs after the control or form is created.
:ref:`Destroy <no-6441>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-6442>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-6443>`               Occurs when the control gets the focus.
:ref:`Idle <no-6444>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-6445>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-6446>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-6447>`               
:ref:`KeyUp <no-6448>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-6449>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-6450>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-6451>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-6452>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-6453>`             
:ref:`MouseLeave <no-6454>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-6455>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-6456>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-6457>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-6458>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-6459>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-6460>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-6461>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-6462>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-6463>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-6464>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-6465>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-6466>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-6467>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-6468>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-6469>`                   Occurs when the control's position changes.
:ref:`Paint <no-6470>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-6471>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-6472>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-6473>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-6474>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-6439:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-6440:

**Create** 

Occurs after the control or form is created.



-------

.. _no-6441:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-6442:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-6443:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-6444:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-6445:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-6446:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-6447:

**KeyEvent** 



-------

.. _no-6448:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-6449:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-6450:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-6451:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-6452:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-6453:

**MouseEvent** 



-------

.. _no-6454:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-6455:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-6456:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-6457:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-6458:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-6459:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-6460:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-6461:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-6462:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-6463:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-6464:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-6465:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-6466:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-6467:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-6468:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-6469:

**Move** 

Occurs when the control's position changes.



-------

.. _no-6470:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-6471:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-6472:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-6473:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-6474:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-6475>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-6476>`             Instantiate object as a child of self.
:ref:`afterInit <no-6477>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-6478>`          
:ref:`afterSetProperties <no-6479>`    
:ref:`autoBindEvents <no-6480>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-6481>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-6482>`   
:ref:`bindEvent <no-6483>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-6484>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-6485>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-6486>`          Makes this object topmost
:ref:`clear <no-6487>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-6488>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-6489>`  Given a position relative to this control, return a position relative
:ref:`copy <no-6490>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-6491>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-6492>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-6493>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-6494>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-6495>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-6496>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-6497>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-6498>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-6499>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-6500>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-6501>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-6502>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-6503>`              Draws text on the object at the specified position
:ref:`endHover <no-6504>`              
:ref:`fitToSizer <no-6505>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-6506>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-6507>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-6508>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-6509>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-6510>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-6511>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-6512>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-6513>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-6514>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-6515>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-6516>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-6517>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-6518>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-6519>`                  Make the object invisible.
:ref:`initEvents <no-6520>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-6521>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-6522>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-6523>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-6524>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-6525>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-6526>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-6527>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-6528>`               
:ref:`paste <no-6529>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-6530>`           
:ref:`processDroppedFiles <no-6531>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-6532>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-6533>`            Raise the passed Dabo event.
:ref:`reCreate <no-6534>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-6535>`              Recreate the object.
:ref:`redraw <no-6536>`                Called when the object is (re)drawn.
:ref:`refresh <no-6537>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-6538>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-6539>`               Destroys the object.
:ref:`removeDrawnObject <no-6540>`     
:ref:`sendToBack <no-6541>`            Places this object behind all others.
:ref:`setAll <no-6542>`                Set all child object properties to the passed value.
:ref:`setFocus <no-6543>`              Sets focus to the object.
:ref:`setPositionInSizer <no-6544>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-6545>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-6546>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-6547>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-6548>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-6549>`                  Make the object visible.
:ref:`showContainingPage <no-6550>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-6551>`       Display a context menu (popup) at the specified position.
:ref:`super <no-6552>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-6553>`           Remove a previously registered event binding.
:ref:`unbindKey <no-6554>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-6555>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-6556>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-6557>`                Update the properties of this object and all contained objects.

====================================== ========================


Methods - inherited
=====================

.. _no-6475:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6476:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-6477:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6478:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6479:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6480:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.autoBindEvents(self, force=True)
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

.. _no-6481:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6482:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6483:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6484:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6485:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-6486:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6487:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6488:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6489:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6490:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6491:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6492:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6493:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6494:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-6495:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6496:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6497:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6498:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6499:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6500:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6501:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6502:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6503:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6504:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6505:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6506:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6507:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6508:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6509:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6510:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6511:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6512:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6513:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6514:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6515:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6516:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-6517:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6518:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6519:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6520:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6521:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6522:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6523:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6524:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.lockDisplay(self)
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

.. _no-6525:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6526:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6527:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6528:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6529:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6530:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6531:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6532:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6533:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6534:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6535:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6536:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6537:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6538:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6539:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6540:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6541:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6542:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-6543:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6544:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6545:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-6546:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-6547:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6548:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6549:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6550:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6551:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6552:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6553:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6554:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6555:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6556:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6557:

.. function:: dabo.ui.dControlMixinBase.dControlMixinBase.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
