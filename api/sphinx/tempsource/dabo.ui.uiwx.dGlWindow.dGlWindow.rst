
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dGlWindow

.. _dabo.ui.uiwx.dGlWindow.dGlWindow:

============================================
|doc_title|  **dGlWindow.dGlWindow** - class
============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dGlWindow**

.. inheritance-diagram:: dGlWindow


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.glcanvas.GLCanvas - can not provide a link



|subclasses| Known Subclasses
=============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dGlWindow.dGlWindow

   .. automethod:: dabo.ui.uiwx.dGlWindow.dGlWindow.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-22848>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-22849>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-22850>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-22851>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-22852>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-22853>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-22854>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-22855>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-22856>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-22857>`                The caption of the object. (str)
:ref:`Children <no-22858>`               Returns a list of object references to the children of
:ref:`Class <no-22859>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-22860>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-22861>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-22862>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-22863>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-22864>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-22865>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-22866>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-22867>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-22868>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-22869>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-22870>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-22871>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-22872>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-22873>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-22874>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-22875>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-22876>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-22877>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-22878>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-22879>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-22880>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-22881>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-22882>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-22883>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-22884>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-22885>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-22886>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-22887>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-22888>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-22889>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-22890>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-22891>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-22892>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-22893>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-22894>`               Specifies the font face. (str)
:ref:`FontInfo <no-22895>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-22896>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-22897>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-22898>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-22899>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-22900>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-22901>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-22902>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-22903>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-22904>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-22905>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-22906>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-22907>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-22908>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-22909>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-22910>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-22911>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-22912>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-22913>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-22914>`               Specifies the base name of the object.
:ref:`Parent <no-22915>`                 The containing object. (obj)
:ref:`Position <no-22916>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-22917>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-22918>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-22919>`                  The position of the right side of the object. This is a
:ref:`Rotate <no-22920>`                 Rotate on Right Mouse Click and Drag
:ref:`Size <no-22921>`                   The size of the object. (tuple)
:ref:`Sizer <no-22922>`                  The sizer for the object.
:ref:`StatusText <no-22923>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-22924>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-22925>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-22926>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-22927>`                    The top position of the object. (int)
:ref:`Transparency <no-22928>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-22929>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-22930>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-22931>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-22932>`                  The width of the object. (int)
:ref:`WindowHandle <no-22933>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-22920:

**Rotate** 

Rotate on Right Mouse Click and Drag



-------


Properties - inherited
========================

.. _no-22848:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22849:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22850:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22851:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22852:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22853:

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

.. _no-22854:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22855:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22856:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22857:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22858:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22859:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22860:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22861:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22862:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22863:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22864:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22865:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22866:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22867:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22868:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22869:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22870:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22871:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22872:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22873:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22874:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22875:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22876:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22877:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22878:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22879:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22880:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22881:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22882:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22883:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22884:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22885:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22886:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22887:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22888:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22889:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22890:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22891:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22892:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22893:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22894:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22895:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22896:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22897:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22898:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22899:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22900:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22901:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22902:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22903:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22904:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22905:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22906:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22907:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22908:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22909:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22910:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22911:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22912:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22913:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22914:

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

.. _no-22915:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22916:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22917:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22918:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22919:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22921:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22922:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22923:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22924:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-22925:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22926:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22927:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22928:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22929:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22930:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22931:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22932:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22933:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-22934>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-22935>`                 Occurs after the control or form is created.
:ref:`Destroy <no-22936>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-22937>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-22938>`               Occurs when the control gets the focus.
:ref:`Idle <no-22939>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-22940>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-22941>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-22942>`               
:ref:`KeyUp <no-22943>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-22944>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-22945>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-22946>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-22947>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-22948>`             
:ref:`MouseLeave <no-22949>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-22950>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-22951>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-22952>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-22953>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-22954>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-22955>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-22956>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-22957>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-22958>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-22959>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-22960>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-22961>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-22962>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-22963>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-22964>`                   Occurs when the control's position changes.
:ref:`Paint <no-22965>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-22966>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-22967>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-22968>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-22969>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-22934:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-22935:

**Create** 

Occurs after the control or form is created.



-------

.. _no-22936:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-22937:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-22938:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-22939:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-22940:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-22941:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-22942:

**KeyEvent** 



-------

.. _no-22943:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-22944:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-22945:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-22946:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-22947:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-22948:

**MouseEvent** 



-------

.. _no-22949:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-22950:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-22951:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-22952:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-22953:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-22954:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-22955:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-22956:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-22957:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-22958:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-22959:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-22960:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-22961:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-22962:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-22963:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-22964:

**Move** 

Occurs when the control's position changes.



-------

.. _no-22965:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-22966:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-22967:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-22968:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-22969:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-22970>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-22971>`             Instantiate object as a child of self.
:ref:`afterInit <no-22972>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-22973>`          
:ref:`afterSetProperties <no-22974>`    
:ref:`autoBindEvents <no-22975>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-22976>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-22977>`   
:ref:`bindEvent <no-22978>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-22979>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-22980>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-22981>`          Makes this object topmost
:ref:`clear <no-22982>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-22983>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-22984>`  Given a position relative to this control, return a position relative
:ref:`copy <no-22985>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-22986>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-22987>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-22988>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-22989>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-22990>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-22991>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-22992>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-22993>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-22994>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-22995>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-22996>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-22997>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-22998>`              Draws text on the object at the specified position
:ref:`endHover <no-22999>`              
:ref:`fitToSizer <no-23000>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-23001>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-23002>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-23003>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-23004>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-23005>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-23006>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-23007>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-23008>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-23009>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-23010>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-23011>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-23012>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-23013>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-23014>`                  Make the object invisible.
:ref:`initEvents <no-23015>`            Hook for subclasses. User code should do custom event binding
:ref:`initGL <no-23016>`                Hook function.  Put your initial GL code in here.
:ref:`initProperties <no-23017>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-23018>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-23019>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-23020>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-23021>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-23022>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-23023>`     Given a position relative to the form, return a position relative
:ref:`onDraw <no-23024>`                Hook function.  Put the code here for what happens when you draw.
:ref:`onHover <no-23025>`               
:ref:`onMouseMove <no-23026>`           
:ref:`onMouseRightDown <no-23027>`      
:ref:`onMouseRightUp <no-23028>`        
:ref:`onPaint <no-23029>`               
:ref:`onResize <no-23030>`              
:ref:`paste <no-23031>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-23032>`           
:ref:`processDroppedFiles <no-23033>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-23034>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-23035>`            Raise the passed Dabo event.
:ref:`reCreate <no-23036>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-23037>`              Recreate the object.
:ref:`redraw <no-23038>`                Called when the object is (re)drawn.
:ref:`refresh <no-23039>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-23040>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-23041>`               Destroys the object.
:ref:`removeDrawnObject <no-23042>`     
:ref:`sendToBack <no-23043>`            Places this object behind all others.
:ref:`setAll <no-23044>`                Set all child object properties to the passed value.
:ref:`setFocus <no-23045>`              Sets focus to the object.
:ref:`setPositionInSizer <no-23046>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-23047>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-23048>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-23049>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-23050>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-23051>`                  Make the object visible.
:ref:`showContainingPage <no-23052>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-23053>`       Display a context menu (popup) at the specified position.
:ref:`super <no-23054>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-23055>`           Remove a previously registered event binding.
:ref:`unbindKey <no-23056>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-23057>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-23058>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-23059>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-23016:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.initGL(self)

   Hook function.  Put your initial GL code in here.



-------

.. _no-23024:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.onDraw(self)

   
   Hook function.  Put the code here for what happens when you draw.
   
   .. note::
       You don't need to swap buffers here....We do this for you automatically.
   
   



-------

.. _no-23026:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.onMouseMove(self, evt)



-------

.. _no-23027:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.onMouseRightDown(self, evt)



-------

.. _no-23028:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.onMouseRightUp(self, evt)



-------

.. _no-23029:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.onPaint(self, event)



-------

.. _no-23030:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.onResize(self, event)



-------


Methods - inherited
=====================

.. _no-22970:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22971:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-22972:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22973:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22974:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22975:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.autoBindEvents(self, force=True)
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

.. _no-22976:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22977:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22978:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22979:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22980:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-22981:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22982:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22983:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22984:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22985:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22986:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22987:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22988:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22989:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-22990:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22991:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22992:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22993:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22994:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22995:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22996:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22997:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22998:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22999:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23000:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23001:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23002:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23003:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23004:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23005:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23006:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23007:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23008:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23009:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23010:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23011:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-23012:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23013:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23014:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23015:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23017:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23018:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23019:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23020:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.lockDisplay(self)
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

.. _no-23021:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23022:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23023:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23025:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23031:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23032:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23033:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23034:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23035:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23036:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23037:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23038:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23039:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23040:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23041:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23042:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23043:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23044:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-23045:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23046:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23047:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-23048:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-23049:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23050:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23051:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23052:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23053:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23054:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23055:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23056:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23057:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23058:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23059:

.. function:: dabo.ui.uiwx.dGlWindow.dGlWindow.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
