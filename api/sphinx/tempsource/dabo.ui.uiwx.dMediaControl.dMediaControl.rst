
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMediaControl

.. _dabo.ui.uiwx.dMediaControl.dMediaControl:

====================================================
|doc_title|  **dMediaControl.dMediaControl** - class
====================================================

Wraps the wx MediaCtrl to display video and audio content.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dMediaControl**

.. inheritance-diagram:: dMediaControl


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.media.MediaCtrl - can not provide a link



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMediaControl.dMediaControl

   .. automethod:: dabo.ui.uiwx.dMediaControl.dMediaControl.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-23603>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-23604>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-23605>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-23606>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-23607>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-23608>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-23609>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-23610>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-23611>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-23612>`                The caption of the object. (str)
:ref:`Children <no-23613>`               Returns a list of object references to the children of
:ref:`Class <no-23614>`                  The class the object is based on. Read-only.  (class)
:ref:`ContentDimensions <no-23615>`      The native dimensions of the content, minus the player controls, if any.
:ref:`ControllingSizer <no-23616>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-23617>`   Reference to the sizer item that control's this control's layout.
:ref:`CurrentPosition <no-23618>`        The current playback position of the content in either milliseconds (default)
:ref:`DisplayDimensions <no-23619>`      The native dimensions of the content and the player controls, if any.
:ref:`DroppedFileHandler <no-23620>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-23621>`     Reference to the object that will handle text dropped on this control.
:ref:`Duration <no-23622>`               Duration of the content in either milliseconds (default) or seconds, depending
:ref:`DynamicBackColor <no-23623>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-23624>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-23625>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-23626>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-23627>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-23628>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-23629>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-23630>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-23631>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-23632>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-23633>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-23634>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-23635>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-23636>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-23637>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-23638>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-23639>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-23640>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-23641>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-23642>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-23643>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-23644>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-23645>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-23646>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-23647>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-23648>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-23649>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-23650>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-23651>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-23652>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-23653>`               Specifies the font face. (str)
:ref:`FontInfo <no-23654>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-23655>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-23656>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-23657>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-23658>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-23659>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-23660>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-23661>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-23662>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-23663>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-23664>`              Specifies which events to log.  (list of strings)
:ref:`Loop <no-23665>`                   Controls whether the content stops when it reaches the end (False; default),
:ref:`MaximumHeight <no-23666>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-23667>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-23668>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-23669>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-23670>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-23671>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-23672>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-23673>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-23674>`               Specifies the base name of the object.
:ref:`Parent <no-23675>`                 The containing object. (obj)
:ref:`PlaybackRate <no-23676>`           Controls the speed at which the content is played. A rate of 100 (default)
:ref:`Position <no-23677>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-23678>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-23679>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-23680>`                  The position of the right side of the object. This is a
:ref:`ShowControls <no-23681>`           Determines if the player controls are visible. Note that the specific controls
:ref:`Size <no-23682>`                   The size of the object. (tuple)
:ref:`Sizer <no-23683>`                  The sizer for the object.
:ref:`Source <no-23684>`                 This can be either a file path or a URI for the content displayed in this
:ref:`Status <no-23685>`                 The current playback status. One of 'Playing', 'Paused', or 'Stopped'.
:ref:`StatusText <no-23686>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-23687>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-23688>`                    A property that user code can safely use for specific purposes.
:ref:`TimeInSeconds <no-23689>`          Determines whether we specify content length and position in
:ref:`ToolTipText <no-23690>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-23691>`                    The top position of the object. (int)
:ref:`Transparency <no-23692>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-23693>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-23694>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-23695>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Volume <no-23696>`                 Controls the sound level. 100 (default) is full volume; 0 turns the
:ref:`Width <no-23697>`                  The width of the object. (int)
:ref:`WindowHandle <no-23698>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-23615:

**ContentDimensions** 

The native dimensions of the content, minus the player controls, if any.
    (read-only) (2-tuple of int)



-------

.. _no-23618:

**CurrentPosition** 

The current playback position of the content in either milliseconds (default)
    or seconds, depending on the setting of TimeInSeconds.  (int or float)



-------

.. _no-23619:

**DisplayDimensions** 

The native dimensions of the content and the player controls, if any.
    When ShowControls is False, or when audio content is loaded, this is identical
    to ContentDimensions. (read-only) (2-tuple of int)



-------

.. _no-23622:

**Duration** 

Duration of the content in either milliseconds (default) or seconds, depending
    on the value of TimeInSeconds.  (read-only) (int or float)



-------

.. _no-23665:

**Loop** 

Controls whether the content stops when it reaches the end (False; default),
    or whether it restarts at the beginning (True).  (bool)



-------

.. _no-23681:

**ShowControls** 

Determines if the player controls are visible. Note that the specific controls
    that are shown with the control depends on the platform and the type of content.
    Default=True.  (bool)



-------

.. _no-23684:

**Source** 

This can be either a file path or a URI for the content displayed in this
    control. If the value begins with 'http', it is assumed to be a URI rather than
    a local file path. Setting the source to None will clear the control.  (str)



-------

.. _no-23685:

**Status** 

The current playback status. One of 'Playing', 'Paused', or 'Stopped'.
    (read-only) (str)



-------

.. _no-23689:

**TimeInSeconds** 

Determines whether we specify content length and position in
    seconds (default), or milliseconds. Affects the Duration and
    CurrentPosition properties. Default=True  (bool)



-------


Properties - inherited
========================

.. _no-23603:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23604:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23605:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23606:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23607:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23608:

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

.. _no-23609:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23610:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23611:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23612:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23613:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23614:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23616:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23617:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23620:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23621:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23623:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23624:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23625:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23626:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23627:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23628:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23629:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23630:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23631:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23632:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23633:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23634:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23635:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23636:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23637:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23638:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23639:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23640:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23641:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23642:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23643:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23644:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23645:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23646:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23647:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23648:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23649:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23650:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23651:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23652:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23653:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23654:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23655:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23656:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23657:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23658:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23659:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23660:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23661:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23662:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23663:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23664:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23666:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23667:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23668:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23669:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23670:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23671:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23672:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23673:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23674:

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

.. _no-23675:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23676:

**PlaybackRate** 

Controls the speed at which the content is played. A rate of 100 (default)
    plays at normal speed; a rate of 200 would play back at double speed; 50 at
    half-speed, etc. Note that this has undefined behavior when the content is not
    playing: it can either do nothing, or can start the content playing immediately.
    Once the content stops, though, this value does not persist.  (int)


Inherited from: 'wx.media.MediaCtrl - can not provide a link

-------

.. _no-23677:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23678:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23679:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23680:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23682:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23683:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23686:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23687:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-23688:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23690:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23691:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23692:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23693:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23694:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23695:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23696:

**Volume** 

Controls the sound level. 100 (default) is full volume; 0 turns the
    sound off.  (int)


Inherited from: 'wx.media.MediaCtrl - can not provide a link

-------

.. _no-23697:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23698:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-23699>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-23700>`                 Occurs after the control or form is created.
:ref:`Destroy <no-23701>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-23702>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-23703>`               Occurs when the control gets the focus.
:ref:`Idle <no-23704>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-23705>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-23706>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-23707>`               
:ref:`KeyUp <no-23708>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-23709>`              Occurs when the control loses the focus.
:ref:`MediaEvent <no-23710>`             
:ref:`MediaFinished <no-23711>`          Occurs when the media has finished playing.
:ref:`MediaLoaded <no-23712>`            Occurs when the media has been successfully loaded.
:ref:`MediaPause <no-23713>`             Occurs when playback has been paused.
:ref:`MediaPlay <no-23714>`              Occurs when playback has begun.
:ref:`MediaStateChanged <no-23715>`      Occurs when the playback status has changed from one state to another.
:ref:`MediaStop <no-23716>`              Occurs when playback has been stopped.
:ref:`MenuClose <no-23717>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-23718>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-23719>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-23720>`             
:ref:`MouseLeave <no-23721>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-23722>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-23723>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-23724>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-23725>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-23726>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-23727>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-23728>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-23729>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-23730>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-23731>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-23732>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-23733>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-23734>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-23735>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-23736>`                   Occurs when the control's position changes.
:ref:`Paint <no-23737>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-23738>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-23739>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-23740>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-23741>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-23699:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-23700:

**Create** 

Occurs after the control or form is created.



-------

.. _no-23701:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-23702:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-23703:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-23704:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-23705:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-23706:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-23707:

**KeyEvent** 



-------

.. _no-23708:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-23709:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-23710:

**MediaEvent** 



-------

.. _no-23711:

**MediaFinished** 

Occurs when the media has finished playing.



-------

.. _no-23712:

**MediaLoaded** 

Occurs when the media has been successfully loaded.



-------

.. _no-23713:

**MediaPause** 

Occurs when playback has been paused.



-------

.. _no-23714:

**MediaPlay** 

Occurs when playback has begun.



-------

.. _no-23715:

**MediaStateChanged** 

Occurs when the playback status has changed from one state to another.



-------

.. _no-23716:

**MediaStop** 

Occurs when playback has been stopped.



-------

.. _no-23717:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-23718:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-23719:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-23720:

**MouseEvent** 



-------

.. _no-23721:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-23722:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-23723:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-23724:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-23725:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-23726:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-23727:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-23728:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-23729:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-23730:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-23731:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-23732:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-23733:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-23734:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-23735:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-23736:

**Move** 

Occurs when the control's position changes.



-------

.. _no-23737:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-23738:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-23739:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-23740:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-23741:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-23742>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-23743>`             Instantiate object as a child of self.
:ref:`afterInit <no-23744>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-23745>`          
:ref:`afterSetProperties <no-23746>`    
:ref:`autoBindEvents <no-23747>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-23748>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-23749>`   
:ref:`bindEvent <no-23750>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-23751>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-23752>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-23753>`          Makes this object topmost
:ref:`clear <no-23754>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-23755>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-23756>`  Given a position relative to this control, return a position relative
:ref:`copy <no-23757>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-23758>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-23759>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-23760>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-23761>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-23762>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-23763>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-23764>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-23765>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-23766>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-23767>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-23768>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-23769>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-23770>`              Draws text on the object at the specified position
:ref:`endHover <no-23771>`              
:ref:`fitToSizer <no-23772>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-23773>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-23774>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-23775>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-23776>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-23777>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-23778>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-23779>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-23780>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-23781>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-23782>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-23783>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-23784>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-23785>`         Returns a dict containing the object's sizer property info. The
:ref:`handleLoadFailure <no-23786>`     This method contains the default behavior when an attempt to load
:ref:`hide <no-23787>`                  Make the object invisible.
:ref:`initEvents <no-23788>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-23789>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-23790>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-23791>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-23792>`           Locks the visual updates to the control.
:ref:`moveByPct <no-23793>`             Moves the CurrentPosition by the specified percentage of the content.
:ref:`moveTabOrderAfter <no-23794>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-23795>`    Moves this object's tab order before the passed obj.
:ref:`moveToPct <no-23796>`             Moves the CurrentPosition to the specified percentage of the content's
:ref:`objectCoordinates <no-23797>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-23798>`               
:ref:`paste <no-23799>`                 Called by uiApp when the user requests a paste operation.
:ref:`play <no-23800>`                  Plays the content. By default, the content is played forward at normal
:ref:`posIsWithin <no-23801>`           
:ref:`processDroppedFiles <no-23802>`   Load the dropped file into the control. Only one file can be
:ref:`processDroppedText <no-23803>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-23804>`            Raise the passed Dabo event.
:ref:`reCreate <no-23805>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-23806>`              Recreate the object.
:ref:`redraw <no-23807>`                Called when the object is (re)drawn.
:ref:`refresh <no-23808>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-23809>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-23810>`               Destroys the object.
:ref:`removeDrawnObject <no-23811>`     
:ref:`reverse <no-23812>`               Reverses the direction of the playing content stream. Has no effect if the
:ref:`scale <no-23813>`                 Size the control to the video's native size. By default, the size is scaled
:ref:`sendToBack <no-23814>`            Places this object behind all others.
:ref:`setAll <no-23815>`                Set all child object properties to the passed value.
:ref:`setFocus <no-23816>`              Sets focus to the object.
:ref:`setPositionInSizer <no-23817>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-23818>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-23819>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-23820>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-23821>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-23822>`                  Make the object visible.
:ref:`showContainingPage <no-23823>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-23824>`       Display a context menu (popup) at the specified position.
:ref:`super <no-23825>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-23826>`           Remove a previously registered event binding.
:ref:`unbindKey <no-23827>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-23828>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-23829>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-23830>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-23786:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.handleLoadFailure(self, val)

   
   This method contains the default behavior when an attempt to load
   content into the control by setting the Source property fails. If you want
   your app to handle things differently, override this method.
   



-------

.. _no-23793:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.moveByPct(self, pct)

   
   Moves the CurrentPosition by the specified percentage of the content.
   Negative values move backward.
   



-------

.. _no-23796:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.moveToPct(self, pct)

   
   Moves the CurrentPosition to the specified percentage of the content's
   Duration. E.g., passing 50 moves to the middle; 75 to 3/4 of the way through.
   Negative values measure from the end; e.g., -10 will set the CurrentPosition
   to 90% through the content.
   



-------

.. _no-23800:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.play(self, rate=None)

   
   Plays the content. By default, the content is played forward at normal
   speed. You can optionally pass a playback rate which will be applied
   to the content. To start the playback in reverse mode, pass in -100.
   



-------

.. _no-23802:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.processDroppedFiles(self, filelist)

   
   Load the dropped file into the control. Only one file can be
   the source, so if by chance more than one file was dropped,
   only use the first.
   



-------

.. _no-23812:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.reverse(self)

   
   Reverses the direction of the playing content stream. Has no effect if the
   content is not playing.
   



-------

.. _no-23813:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.scale(self, prop=1.0)

   
   Size the control to the video's native size. By default, the size is scaled
   to the video's native size, but you can optionally pass a proportion to
   enlarge or reduce the size.
   



-------


Methods - inherited
=====================

.. _no-23742:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23743:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-23744:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23745:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23746:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23747:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.autoBindEvents(self, force=True)
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

.. _no-23748:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23749:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23750:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23751:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23752:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-23753:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23754:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23755:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23756:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23757:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23758:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23759:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23760:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23761:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-23762:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23763:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23764:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23765:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23766:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23767:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23768:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23769:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23770:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23771:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23772:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23773:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23774:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23775:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23776:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23777:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23778:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23779:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23780:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23781:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23782:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23783:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-23784:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23785:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23787:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23788:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23789:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23790:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23791:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23792:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.lockDisplay(self)
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

.. _no-23794:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23795:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23797:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23798:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23799:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23801:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23803:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23804:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23805:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23806:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23807:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23808:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23809:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23810:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23811:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23814:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23815:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-23816:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23817:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23818:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-23819:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-23820:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23821:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23822:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23823:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23824:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23825:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23826:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23827:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23828:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23829:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23830:

.. function:: dabo.ui.uiwx.dMediaControl.dMediaControl.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
