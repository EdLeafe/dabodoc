
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMenuBar

.. _dabo.ui.uiwx.dMenuBar.dMenuBar:

==========================================
|doc_title|  **dMenuBar.dMenuBar** - class
==========================================


Creates a menu bar, which can contain dMenus.

You probably don't want to use this directly. Instead, see dBaseMenuBar
which will give you a dMenuBar with the standard File, Edit, and Help
menus already set up for you.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dMenuBar**

.. inheritance-diagram:: dMenuBar


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMenuBar.dMenuBar

   .. automethod:: dabo.ui.uiwx.dMenuBar.dMenuBar.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-19793>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-19794>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-19795>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-19796>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-19797>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-19798>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-19799>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-19800>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-19801>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-19802>`                The caption of the object. (str)
:ref:`Children <no-19803>`               Returns a list of object references to the children of
:ref:`Class <no-19804>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-19805>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-19806>`   Reference to the sizer item that control's this control's layout.
:ref:`Count <no-19807>`                  Returns the number of child menus. Read-only.  (int)
:ref:`DroppedFileHandler <no-19808>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-19809>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-19810>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-19811>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-19812>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-19813>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-19814>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-19815>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-19816>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-19817>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-19818>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-19819>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-19820>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-19821>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-19822>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-19823>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-19824>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-19825>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-19826>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-19827>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-19828>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-19829>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-19830>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-19831>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-19832>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-19833>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-19834>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-19835>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-19836>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-19837>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-19838>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-19839>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-19840>`               Specifies the font face. (str)
:ref:`FontInfo <no-19841>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-19842>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-19843>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-19844>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-19845>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-19846>`                   Specifies the form that we are a member of.  (dabo.ui.dForm)
:ref:`Height <no-19847>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-19848>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-19849>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-19850>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-19851>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-19852>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-19853>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-19854>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-19855>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-19856>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-19857>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-19858>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-19859>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-19860>`               Specifies the base name of the object.
:ref:`Parent <no-19861>`                 The containing object. (obj)
:ref:`Position <no-19862>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-19863>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-19864>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-19865>`                  The position of the right side of the object. This is a
:ref:`Size <no-19866>`                   The size of the object. (tuple)
:ref:`Sizer <no-19867>`                  The sizer for the object.
:ref:`StatusText <no-19868>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-19869>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-19870>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-19871>`                    The top position of the object. (int)
:ref:`Transparency <no-19872>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-19873>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-19874>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-19875>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-19876>`                  The width of the object. (int)
:ref:`WindowHandle <no-19877>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-19807:

**Count** 

Returns the number of child menus. Read-only.  (int)



-------


Properties - inherited
========================

.. _no-19793:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19794:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19795:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19796:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19797:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19798:

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

.. _no-19799:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19800:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19801:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19802:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19803:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19804:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19805:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19806:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19808:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19809:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19810:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19811:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19812:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19813:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19814:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19815:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19816:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19817:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19818:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19819:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19820:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19821:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19822:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19823:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19824:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19825:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19826:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19827:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19828:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19829:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19830:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19831:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19832:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19833:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19834:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19835:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19836:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19837:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19838:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19839:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19840:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19841:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19842:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19843:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19844:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19845:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19846:

**Form** 

Specifies the form that we are a member of.  (dabo.ui.dForm)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19847:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19848:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19849:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19850:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19851:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19852:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19853:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19854:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19855:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19856:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19857:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19858:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19859:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19860:

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

.. _no-19861:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19862:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19863:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19864:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19865:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19866:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19867:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19868:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19869:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19870:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19871:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19872:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19873:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19874:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19875:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19876:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19877:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-19878>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-19879>`                 Occurs after the control or form is created.
:ref:`Destroy <no-19880>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-19881>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-19882>`               Occurs when the control gets the focus.
:ref:`Idle <no-19883>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-19884>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-19885>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-19886>`               
:ref:`KeyUp <no-19887>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-19888>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-19889>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-19890>`              
:ref:`MenuHighlight <no-19891>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-19892>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-19893>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-19894>`             
:ref:`MouseLeave <no-19895>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-19896>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-19897>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-19898>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-19899>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-19900>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-19901>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-19902>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-19903>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-19904>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-19905>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-19906>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-19907>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-19908>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-19909>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-19910>`                   Occurs when the control's position changes.
:ref:`Paint <no-19911>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-19912>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-19913>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-19914>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-19915>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-19878:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-19879:

**Create** 

Occurs after the control or form is created.



-------

.. _no-19880:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-19881:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-19882:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-19883:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-19884:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-19885:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-19886:

**KeyEvent** 



-------

.. _no-19887:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-19888:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-19889:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-19890:

**MenuEvent** 



-------

.. _no-19891:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-19892:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-19893:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-19894:

**MouseEvent** 



-------

.. _no-19895:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-19896:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-19897:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-19898:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-19899:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-19900:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-19901:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-19902:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-19903:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-19904:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-19905:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-19906:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-19907:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-19908:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-19909:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-19910:

**Move** 

Occurs when the control's position changes.



-------

.. _no-19911:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-19912:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-19913:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-19914:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-19915:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-19916>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-19917>`             Instantiate object as a child of self.
:ref:`afterInit <no-19918>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-19919>`          
:ref:`afterSetProperties <no-19920>`    
:ref:`append <no-19921>`                Appends a dMenu to the end of the dMenuBar, and returns a reference
:ref:`appendMenu <no-19922>`            Inserts a dMenu at the end of the dMenuBar, and returns the
:ref:`autoBindEvents <no-19923>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-19924>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-19925>`   
:ref:`bindEvent <no-19926>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-19927>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-19928>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-19929>`          Makes this object topmost
:ref:`clear <no-19930>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-19931>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-19932>`  Given a position relative to this control, return a position relative
:ref:`copy <no-19933>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-19934>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-19935>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-19936>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-19937>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-19938>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-19939>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-19940>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-19941>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-19942>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-19943>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-19944>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-19945>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-19946>`              Draws text on the object at the specified position
:ref:`endHover <no-19947>`              
:ref:`fitToSizer <no-19948>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-19949>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-19950>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-19951>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-19952>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-19953>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-19954>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-19955>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-19956>`      Returns an object that locks the current display when created, and
:ref:`getMenu <no-19957>`               Returns a reference to the menu with the specified MenuID or Caption.
:ref:`getMenuIndex <no-19958>`          Returns the index of the menu with the specified ID or caption.
:ref:`getMousePosition <no-19959>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-19960>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-19961>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-19962>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-19963>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-19964>`                  Make the object invisible.
:ref:`initEvents <no-19965>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-19966>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-19967>`                Inserts a dMenu at the specified position in the dMenuBar, and returns
:ref:`insertMenu <no-19968>`            Inserts a dMenu in the dMenuBar at the specified position, and
:ref:`isContainedBy <no-19969>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-19970>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-19971>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-19972>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-19973>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-19974>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-19975>`               
:ref:`paste <no-19976>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-19977>`           
:ref:`prepend <no-19978>`               Prepends a dMenu to the beginning of the dMenuBar, and returns
:ref:`prependMenu <no-19979>`           Inserts a dMenu at the beginning of the dMenuBar, and returns
:ref:`processDroppedFiles <no-19980>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-19981>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-19982>`            Raise the passed Dabo event.
:ref:`reCreate <no-19983>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-19984>`              Recreate the object.
:ref:`redraw <no-19985>`                Called when the object is (re)drawn.
:ref:`refresh <no-19986>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-19987>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-19988>`               Destroys the object.
:ref:`remove <no-19989>`                Removes the menu at the specified index from the menu bar. You may
:ref:`removeDrawnObject <no-19990>`     
:ref:`sendToBack <no-19991>`            Places this object behind all others.
:ref:`setAll <no-19992>`                Set all child object properties to the passed value.
:ref:`setFocus <no-19993>`              Sets focus to the object.
:ref:`setPositionInSizer <no-19994>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-19995>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-19996>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-19997>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-19998>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-19999>`                  Make the object visible.
:ref:`showContainingPage <no-20000>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-20001>`       Display a context menu (popup) at the specified position.
:ref:`super <no-20002>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-20003>`           Remove a previously registered event binding.
:ref:`unbindKey <no-20004>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-20005>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-20006>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-20007>`                

======================================= ========================


Methods
=======

.. _no-19921:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.append(self, caption, MenuID=None)

   
   Appends a dMenu to the end of the dMenuBar, and returns a reference
   to that menu.
   
   A generic dMenu will be created with the passed caption. Also see the
   appendMenu() function, which takes a dMenu instance as an argument.
   



-------

.. _no-19922:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.appendMenu(self, menu)

   
   Inserts a dMenu at the end of the dMenuBar, and returns the
   reference to that menu.
   



-------

.. _no-19957:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getMenu(self, idOrCaption)

   
   Returns a reference to the menu with the specified MenuID or Caption.
   The MenuID property is checked first; then the Caption. If no match is found,
   None is returned.
   



-------

.. _no-19958:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getMenuIndex(self, idOrCaption)

   
   Returns the index of the menu with the specified ID or caption.
   If the menu isn't found, None is returned.
   



-------

.. _no-19967:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.insert(self, pos, caption, MenuID=None)

   
   Inserts a dMenu at the specified position in the dMenuBar, and returns
   a reference to that menu.
   
   A generic dMenu will be created with the passed caption. Also see the
   insertMenu() function, which takes a dMenu instance as an argument.
   



-------

.. _no-19968:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.insertMenu(self, pos, menu)

   
   Inserts a dMenu in the dMenuBar at the specified position, and
   returns a reference to that menu.
   



-------

.. _no-19978:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.prepend(self, caption, MenuID=None)

   
   Prepends a dMenu to the beginning of the dMenuBar, and returns
   a reference to that menu.
   
   A generic dMenu will be created with the passed caption. Also see the
   prependMenu() function, which takes a dMenu instance as an argument.
   



-------

.. _no-19979:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.prependMenu(self, menu)

   
   Inserts a dMenu at the beginning of the dMenuBar, and returns
   a reference to that menu.
   



-------

.. _no-19989:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.remove(self, indexOrMenu, release=True)

   
   Removes the menu at the specified index from the menu bar. You may
   also pass a reference to the menu, or the menu's Caption, and it will
   find the associated index.
   
   If release is True (the default), the menu is deleted as well. If release
   is False, a reference to the menu object will be returned, and the caller
   is responsible for deleting it.
   



-------

.. _no-20007:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.update(self)



-------


Methods - inherited
=====================

.. _no-19916:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19917:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-19918:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19919:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19920:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19923:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.autoBindEvents(self, force=True)
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

.. _no-19924:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19925:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19926:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19927:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19928:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-19929:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19930:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19931:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19932:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19933:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19934:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19935:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19936:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19937:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-19938:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19939:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19940:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19941:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19942:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19943:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19944:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19945:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19946:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19947:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19948:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19949:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19950:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19951:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19952:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19953:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19954:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19955:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19956:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19959:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19960:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19961:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-19962:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19963:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19964:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19965:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19966:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19969:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19970:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19971:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.lockDisplay(self)
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

.. _no-19972:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19973:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19974:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19975:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19976:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19977:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19980:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19981:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19982:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19983:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19984:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19985:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19986:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19987:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19988:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19990:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19991:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19992:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-19993:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19994:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19995:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-19996:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-19997:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19998:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19999:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20000:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20001:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20002:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20003:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20004:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20005:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20006:

.. function:: dabo.ui.uiwx.dMenuBar.dMenuBar.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
