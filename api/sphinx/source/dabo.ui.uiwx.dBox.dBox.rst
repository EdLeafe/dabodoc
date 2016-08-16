
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBox

.. _dabo.ui.uiwx.dBox.dBox:

==================================
|doc_title|  **dBox.dBox** - class
==================================

Creates a box for visually grouping objects on your form.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBox**

.. inheritance-diagram:: dBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|subclasses| Known Subclasses
=============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBox.dBox

   .. automethod:: dabo.ui.uiwx.dBox.dBox.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-26395>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-26396>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-26397>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-26398>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-26399>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-26400>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-26401>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-26402>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-26403>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-26404>`                The caption of the object. (str)
:ref:`Children <no-26405>`               Returns a list of object references to the children of
:ref:`Class <no-26406>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-26407>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-26408>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-26409>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-26410>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-26411>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-26412>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-26413>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-26414>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-26415>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-26416>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-26417>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-26418>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-26419>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-26420>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-26421>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-26422>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-26423>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-26424>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-26425>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-26426>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-26427>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-26428>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-26429>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-26430>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-26431>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-26432>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-26433>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-26434>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-26435>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-26436>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-26437>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-26438>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-26439>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-26440>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-26441>`               Specifies the font face. (str)
:ref:`FontInfo <no-26442>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-26443>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-26444>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-26445>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-26446>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-26447>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-26448>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-26449>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-26450>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-26451>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-26452>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-26453>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-26454>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-26455>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-26456>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-26457>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-26458>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-26459>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-26460>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-26461>`               Specifies the base name of the object.
:ref:`Parent <no-26462>`                 The containing object. (obj)
:ref:`Position <no-26463>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-26464>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-26465>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-26466>`                  The position of the right side of the object. This is a
:ref:`Size <no-26467>`                   The size of the object. (tuple)
:ref:`Sizer <no-26468>`                  The sizer for the object.
:ref:`StatusText <no-26469>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-26470>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-26471>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-26472>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-26473>`                    The top position of the object. (int)
:ref:`Transparency <no-26474>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-26475>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-26476>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-26477>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-26478>`                  The width of the object. (int)
:ref:`WindowHandle <no-26479>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-26395:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26396:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26397:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26398:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26399:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26400:

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

.. _no-26401:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26402:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26403:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26404:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26405:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26406:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26407:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26408:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26409:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26410:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26411:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26412:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26413:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26414:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26415:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26416:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26417:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26418:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26419:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26420:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26421:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26422:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26423:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26424:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26425:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26426:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26427:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26428:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26429:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26430:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26431:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26432:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26433:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26434:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26435:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26436:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26437:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26438:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26439:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26440:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26441:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26442:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26443:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26444:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26445:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26446:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26447:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26448:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26449:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26450:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26451:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26452:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26453:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26454:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26455:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26456:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26457:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26458:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26459:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26460:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26461:

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

.. _no-26462:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26463:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26464:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26465:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26466:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26467:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26468:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26469:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26470:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-26471:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26472:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26473:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26474:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26475:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26476:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26477:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26478:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26479:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-26480>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-26481>`                 Occurs after the control or form is created.
:ref:`Destroy <no-26482>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-26483>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-26484>`               Occurs when the control gets the focus.
:ref:`Idle <no-26485>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-26486>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-26487>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-26488>`               
:ref:`KeyUp <no-26489>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-26490>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-26491>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-26492>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-26493>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-26494>`             
:ref:`MouseLeave <no-26495>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-26496>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-26497>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-26498>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-26499>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-26500>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-26501>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-26502>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-26503>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-26504>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-26505>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-26506>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-26507>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-26508>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-26509>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-26510>`                   Occurs when the control's position changes.
:ref:`Paint <no-26511>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-26512>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-26513>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-26514>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-26515>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-26480:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-26481:

**Create** 

Occurs after the control or form is created.



-------

.. _no-26482:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-26483:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-26484:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-26485:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-26486:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-26487:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-26488:

**KeyEvent** 



-------

.. _no-26489:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-26490:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-26491:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-26492:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-26493:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-26494:

**MouseEvent** 



-------

.. _no-26495:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-26496:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-26497:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-26498:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-26499:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-26500:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-26501:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-26502:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-26503:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-26504:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-26505:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-26506:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-26507:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-26508:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-26509:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-26510:

**Move** 

Occurs when the control's position changes.



-------

.. _no-26511:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-26512:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-26513:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-26514:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-26515:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-26516>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-26517>`             Instantiate object as a child of self.
:ref:`afterInit <no-26518>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-26519>`          
:ref:`afterSetProperties <no-26520>`    
:ref:`autoBindEvents <no-26521>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-26522>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-26523>`   
:ref:`bindEvent <no-26524>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-26525>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-26526>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-26527>`          Makes this object topmost
:ref:`clear <no-26528>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-26529>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-26530>`  Given a position relative to this control, return a position relative
:ref:`copy <no-26531>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-26532>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-26533>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-26534>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-26535>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-26536>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-26537>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-26538>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-26539>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-26540>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-26541>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-26542>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-26543>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-26544>`              Draws text on the object at the specified position
:ref:`endHover <no-26545>`              
:ref:`fitToSizer <no-26546>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-26547>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-26548>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-26549>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-26550>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-26551>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-26552>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-26553>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-26554>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-26555>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-26556>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-26557>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-26558>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-26559>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-26560>`                  Make the object invisible.
:ref:`initEvents <no-26561>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-26562>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-26563>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-26564>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-26565>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-26566>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-26567>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-26568>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-26569>`               
:ref:`paste <no-26570>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-26571>`           
:ref:`processDroppedFiles <no-26572>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-26573>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-26574>`            Raise the passed Dabo event.
:ref:`reCreate <no-26575>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-26576>`              Recreate the object.
:ref:`redraw <no-26577>`                Called when the object is (re)drawn.
:ref:`refresh <no-26578>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-26579>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-26580>`               Destroys the object.
:ref:`removeDrawnObject <no-26581>`     
:ref:`sendToBack <no-26582>`            Places this object behind all others.
:ref:`setAll <no-26583>`                Set all child object properties to the passed value.
:ref:`setFocus <no-26584>`              Sets focus to the object.
:ref:`setPositionInSizer <no-26585>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-26586>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-26587>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-26588>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-26589>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-26590>`                  Make the object visible.
:ref:`showContainingPage <no-26591>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-26592>`       Display a context menu (popup) at the specified position.
:ref:`super <no-26593>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-26594>`           Remove a previously registered event binding.
:ref:`unbindKey <no-26595>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-26596>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-26597>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-26598>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-26516:

.. function:: dabo.ui.uiwx.dBox.dBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26517:

.. function:: dabo.ui.uiwx.dBox.dBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-26518:

.. function:: dabo.ui.uiwx.dBox.dBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26519:

.. function:: dabo.ui.uiwx.dBox.dBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26520:

.. function:: dabo.ui.uiwx.dBox.dBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26521:

.. function:: dabo.ui.uiwx.dBox.dBox.autoBindEvents(self, force=True)
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

.. _no-26522:

.. function:: dabo.ui.uiwx.dBox.dBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26523:

.. function:: dabo.ui.uiwx.dBox.dBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26524:

.. function:: dabo.ui.uiwx.dBox.dBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26525:

.. function:: dabo.ui.uiwx.dBox.dBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26526:

.. function:: dabo.ui.uiwx.dBox.dBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-26527:

.. function:: dabo.ui.uiwx.dBox.dBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26528:

.. function:: dabo.ui.uiwx.dBox.dBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26529:

.. function:: dabo.ui.uiwx.dBox.dBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26530:

.. function:: dabo.ui.uiwx.dBox.dBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26531:

.. function:: dabo.ui.uiwx.dBox.dBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26532:

.. function:: dabo.ui.uiwx.dBox.dBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26533:

.. function:: dabo.ui.uiwx.dBox.dBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26534:

.. function:: dabo.ui.uiwx.dBox.dBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26535:

.. function:: dabo.ui.uiwx.dBox.dBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-26536:

.. function:: dabo.ui.uiwx.dBox.dBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26537:

.. function:: dabo.ui.uiwx.dBox.dBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26538:

.. function:: dabo.ui.uiwx.dBox.dBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26539:

.. function:: dabo.ui.uiwx.dBox.dBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26540:

.. function:: dabo.ui.uiwx.dBox.dBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26541:

.. function:: dabo.ui.uiwx.dBox.dBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26542:

.. function:: dabo.ui.uiwx.dBox.dBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26543:

.. function:: dabo.ui.uiwx.dBox.dBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26544:

.. function:: dabo.ui.uiwx.dBox.dBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26545:

.. function:: dabo.ui.uiwx.dBox.dBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26546:

.. function:: dabo.ui.uiwx.dBox.dBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26547:

.. function:: dabo.ui.uiwx.dBox.dBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26548:

.. function:: dabo.ui.uiwx.dBox.dBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26549:

.. function:: dabo.ui.uiwx.dBox.dBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26550:

.. function:: dabo.ui.uiwx.dBox.dBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26551:

.. function:: dabo.ui.uiwx.dBox.dBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26552:

.. function:: dabo.ui.uiwx.dBox.dBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26553:

.. function:: dabo.ui.uiwx.dBox.dBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26554:

.. function:: dabo.ui.uiwx.dBox.dBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26555:

.. function:: dabo.ui.uiwx.dBox.dBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26556:

.. function:: dabo.ui.uiwx.dBox.dBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26557:

.. function:: dabo.ui.uiwx.dBox.dBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-26558:

.. function:: dabo.ui.uiwx.dBox.dBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26559:

.. function:: dabo.ui.uiwx.dBox.dBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26560:

.. function:: dabo.ui.uiwx.dBox.dBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26561:

.. function:: dabo.ui.uiwx.dBox.dBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26562:

.. function:: dabo.ui.uiwx.dBox.dBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26563:

.. function:: dabo.ui.uiwx.dBox.dBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26564:

.. function:: dabo.ui.uiwx.dBox.dBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26565:

.. function:: dabo.ui.uiwx.dBox.dBox.lockDisplay(self)
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

.. _no-26566:

.. function:: dabo.ui.uiwx.dBox.dBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26567:

.. function:: dabo.ui.uiwx.dBox.dBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26568:

.. function:: dabo.ui.uiwx.dBox.dBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26569:

.. function:: dabo.ui.uiwx.dBox.dBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26570:

.. function:: dabo.ui.uiwx.dBox.dBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26571:

.. function:: dabo.ui.uiwx.dBox.dBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26572:

.. function:: dabo.ui.uiwx.dBox.dBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26573:

.. function:: dabo.ui.uiwx.dBox.dBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26574:

.. function:: dabo.ui.uiwx.dBox.dBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26575:

.. function:: dabo.ui.uiwx.dBox.dBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26576:

.. function:: dabo.ui.uiwx.dBox.dBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26577:

.. function:: dabo.ui.uiwx.dBox.dBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26578:

.. function:: dabo.ui.uiwx.dBox.dBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26579:

.. function:: dabo.ui.uiwx.dBox.dBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26580:

.. function:: dabo.ui.uiwx.dBox.dBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26581:

.. function:: dabo.ui.uiwx.dBox.dBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26582:

.. function:: dabo.ui.uiwx.dBox.dBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26583:

.. function:: dabo.ui.uiwx.dBox.dBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-26584:

.. function:: dabo.ui.uiwx.dBox.dBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26585:

.. function:: dabo.ui.uiwx.dBox.dBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26586:

.. function:: dabo.ui.uiwx.dBox.dBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-26587:

.. function:: dabo.ui.uiwx.dBox.dBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-26588:

.. function:: dabo.ui.uiwx.dBox.dBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26589:

.. function:: dabo.ui.uiwx.dBox.dBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26590:

.. function:: dabo.ui.uiwx.dBox.dBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26591:

.. function:: dabo.ui.uiwx.dBox.dBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26592:

.. function:: dabo.ui.uiwx.dBox.dBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26593:

.. function:: dabo.ui.uiwx.dBox.dBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26594:

.. function:: dabo.ui.uiwx.dBox.dBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26595:

.. function:: dabo.ui.uiwx.dBox.dBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26596:

.. function:: dabo.ui.uiwx.dBox.dBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26597:

.. function:: dabo.ui.uiwx.dBox.dBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26598:

.. function:: dabo.ui.uiwx.dBox.dBox.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
