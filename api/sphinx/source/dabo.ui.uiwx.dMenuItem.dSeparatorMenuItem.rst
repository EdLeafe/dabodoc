
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMenuItem

.. _dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem:

=====================================================
|doc_title|  **dMenuItem.dSeparatorMenuItem** - class
=====================================================

Creates a menu separator.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSeparatorMenuItem**

.. inheritance-diagram:: dSeparatorMenuItem


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem

   .. automethod:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-33316>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-33317>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-33318>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-33319>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-33320>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-33321>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-33322>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-33323>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-33324>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-33325>`                The caption of the object. (str)
:ref:`Children <no-33326>`               Returns a list of object references to the children of
:ref:`Class <no-33327>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-33328>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-33329>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-33330>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-33331>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-33332>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-33333>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-33334>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-33335>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-33336>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-33337>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-33338>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-33339>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-33340>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-33341>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-33342>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-33343>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-33344>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-33345>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-33346>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-33347>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-33348>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-33349>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-33350>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-33351>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-33352>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-33353>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-33354>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-33355>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-33356>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-33357>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-33358>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-33359>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-33360>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-33361>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-33362>`               Specifies the font face. (str)
:ref:`FontInfo <no-33363>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-33364>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-33365>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-33366>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-33367>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-33368>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-33369>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-33370>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-33371>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`ItemID <no-33372>`                 Identifying value for this menuitem. NOTE: there is no checking for
:ref:`Left <no-33373>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-33374>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-33375>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-33376>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-33377>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-33378>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-33379>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-33380>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-33381>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-33382>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-33383>`               Specifies the base name of the object.
:ref:`Parent <no-33384>`                 Specifies the parent menu.
:ref:`Position <no-33385>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-33386>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-33387>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-33388>`                  The position of the right side of the object. This is a
:ref:`Size <no-33389>`                   The size of the object. (tuple)
:ref:`Sizer <no-33390>`                  The sizer for the object.
:ref:`StatusText <no-33391>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-33392>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-33393>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-33394>`                    The top position of the object. (int)
:ref:`Transparency <no-33395>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-33396>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-33397>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-33398>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-33399>`                  The width of the object. (int)
:ref:`WindowHandle <no-33400>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-33372:

**ItemID** 

Identifying value for this menuitem. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that ItemID values
    are unique within a menu.  (varies)



-------


Properties - inherited
========================

.. _no-33316:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33317:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33318:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33319:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33320:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33321:

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

.. _no-33322:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33323:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33324:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33325:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33326:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33327:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33328:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33329:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33330:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33331:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33332:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33333:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33334:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33335:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33336:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33337:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33338:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33339:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33340:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33341:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33342:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33343:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33344:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33345:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33346:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33347:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33348:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33349:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33350:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33351:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33352:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33353:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33354:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33355:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33356:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33357:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33358:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33359:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.MenuItem - can not provide a link

-------

.. _no-33360:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33361:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33362:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33363:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33364:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33365:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33366:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33367:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33368:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33369:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33370:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33371:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33373:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33374:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33375:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33376:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33377:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33378:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33379:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33380:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33381:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33382:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33383:

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

.. _no-33384:

**Parent** 

Specifies the parent menu.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33385:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33386:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33387:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33388:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33389:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33390:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33391:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33392:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33393:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33394:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33395:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33396:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33397:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33398:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33399:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33400:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-33401>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-33402>`                 Occurs after the control or form is created.
:ref:`Destroy <no-33403>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-33404>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-33405>`               Occurs when the control gets the focus.
:ref:`Idle <no-33406>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-33407>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-33408>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-33409>`               
:ref:`KeyUp <no-33410>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-33411>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-33412>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-33413>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-33414>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-33415>`             
:ref:`MouseLeave <no-33416>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-33417>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-33418>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-33419>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-33420>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-33421>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-33422>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-33423>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-33424>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-33425>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-33426>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-33427>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-33428>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-33429>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-33430>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-33431>`                   Occurs when the control's position changes.
:ref:`Paint <no-33432>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-33433>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-33434>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-33435>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-33436>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-33401:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-33402:

**Create** 

Occurs after the control or form is created.



-------

.. _no-33403:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-33404:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-33405:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-33406:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-33407:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-33408:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-33409:

**KeyEvent** 



-------

.. _no-33410:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-33411:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-33412:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-33413:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-33414:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-33415:

**MouseEvent** 



-------

.. _no-33416:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-33417:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-33418:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-33419:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-33420:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-33421:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-33422:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-33423:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-33424:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-33425:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-33426:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-33427:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-33428:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-33429:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-33430:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-33431:

**Move** 

Occurs when the control's position changes.



-------

.. _no-33432:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-33433:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-33434:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-33435:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-33436:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-33437>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-33438>`             Instantiate object as a child of self.
:ref:`afterInit <no-33439>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-33440>`          
:ref:`afterSetProperties <no-33441>`    
:ref:`autoBindEvents <no-33442>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-33443>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-33444>`   
:ref:`bindEvent <no-33445>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-33446>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-33447>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-33448>`          Makes this object topmost
:ref:`clear <no-33449>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-33450>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-33451>`  Given a position relative to this control, return a position relative
:ref:`copy <no-33452>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-33453>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-33454>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-33455>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-33456>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-33457>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-33458>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-33459>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-33460>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-33461>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-33462>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-33463>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-33464>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-33465>`              Draws text on the object at the specified position
:ref:`endHover <no-33466>`              
:ref:`fitToSizer <no-33467>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-33468>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-33469>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-33470>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-33471>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-33472>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-33473>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-33474>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-33475>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-33476>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-33477>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-33478>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-33479>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-33480>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-33481>`                  Make the object invisible.
:ref:`initEvents <no-33482>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-33483>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-33484>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-33485>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-33486>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-33487>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-33488>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-33489>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-33490>`               
:ref:`paste <no-33491>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-33492>`           
:ref:`processDroppedFiles <no-33493>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-33494>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-33495>`            Raise the passed Dabo event.
:ref:`reCreate <no-33496>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-33497>`              Recreate the object.
:ref:`redraw <no-33498>`                Called when the object is (re)drawn.
:ref:`refresh <no-33499>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-33500>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-33501>`               Destroys the object.
:ref:`removeDrawnObject <no-33502>`     
:ref:`sendToBack <no-33503>`            Places this object behind all others.
:ref:`setAll <no-33504>`                Set all child object properties to the passed value.
:ref:`setFocus <no-33505>`              Sets focus to the object.
:ref:`setPositionInSizer <no-33506>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-33507>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-33508>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-33509>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-33510>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-33511>`                  Make the object visible.
:ref:`showContainingPage <no-33512>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-33513>`       Display a context menu (popup) at the specified position.
:ref:`super <no-33514>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-33515>`           Remove a previously registered event binding.
:ref:`unbindKey <no-33516>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-33517>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-33518>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-33519>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-33437:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33438:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-33439:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33440:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33441:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33442:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.autoBindEvents(self, force=True)
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

.. _no-33443:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33444:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33445:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33446:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33447:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-33448:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33449:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33450:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33451:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33452:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33453:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33454:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33455:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33456:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-33457:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33458:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33459:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33460:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33461:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33462:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33463:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33464:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33465:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33466:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33467:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33468:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33469:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33470:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33471:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33472:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33473:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33474:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33475:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33476:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33477:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33478:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-33479:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33480:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33481:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33482:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33483:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33484:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33485:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33486:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.lockDisplay(self)
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

.. _no-33487:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33488:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33489:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33490:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33491:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33492:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33493:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33494:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33495:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33496:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33497:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33498:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33499:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33500:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33501:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33502:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33503:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33504:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-33505:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33506:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33507:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-33508:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-33509:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33510:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33511:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33512:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33513:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33514:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33515:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-33516:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33517:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33518:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33519:

.. function:: dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
