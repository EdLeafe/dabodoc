
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPemMixin

.. _dabo.ui.uiwx.dPemMixin.dPemMixin:

============================================
|doc_title|  **dPemMixin.dPemMixin** - class
============================================


Provides Property/Event/Method interfaces for dForms and dControls.

Subclasses can extend the property sheet by defining their own get/set
functions along with their own property() statements.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPemMixin**

.. inheritance-diagram:: dPemMixin


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.dControlMixinBase.dControlMixinBase`
* :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`
* :ref:`dabo.ui.uiwx.dMenu.dMenu`
* :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`
* :ref:`dabo.ui.uiwx.dMenuItem.dMenuItem`
* :ref:`dabo.ui.uiwx.dMenuItem.dSeparatorMenuItem`
* :ref:`dabo.ui.uiwx.dTimer.dTimer`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPemMixin.dPemMixin

   .. automethod:: dabo.ui.uiwx.dPemMixin.dPemMixin.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-11623>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-11624>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-11625>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-11626>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-11627>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-11628>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-11629>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-11630>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-11631>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-11632>`                The caption of the object. (str)
:ref:`Children <no-11633>`               Returns a list of object references to the children of
:ref:`Class <no-11634>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-11635>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-11636>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-11637>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-11638>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-11639>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-11640>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-11641>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-11642>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-11643>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-11644>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-11645>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-11646>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-11647>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-11648>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-11649>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-11650>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-11651>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-11652>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-11653>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-11654>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-11655>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-11656>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-11657>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-11658>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-11659>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-11660>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-11661>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-11662>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-11663>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-11664>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-11665>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-11666>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-11667>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-11668>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-11669>`               Specifies the font face. (str)
:ref:`FontInfo <no-11670>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-11671>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-11672>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-11673>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-11674>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-11675>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-11676>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-11677>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-11678>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-11679>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-11680>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-11681>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-11682>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-11683>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-11684>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-11685>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-11686>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-11687>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-11688>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-11689>`               Specifies the base name of the object.
:ref:`Parent <no-11690>`                 The containing object. (obj)
:ref:`Position <no-11691>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-11692>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-11693>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-11694>`                  The position of the right side of the object. This is a
:ref:`Size <no-11695>`                   The size of the object. (tuple)
:ref:`Sizer <no-11696>`                  The sizer for the object.
:ref:`StatusText <no-11697>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-11698>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-11699>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-11700>`                    The top position of the object. (int)
:ref:`Transparency <no-11701>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-11702>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-11703>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-11704>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-11705>`                  The width of the object. (int)
:ref:`WindowHandle <no-11706>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-11624:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)



-------

.. _no-11627:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)



-------

.. _no-11628:

**BorderLineStyle** 

Style of line for the border drawn around the control.

    Possible choices are:
        "Solid"  (default)
        "Dash"
        "Dot"
        "DotDash"
        "DashDot"
    



-------

.. _no-11629:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    



-------

.. _no-11630:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    



-------

.. _no-11632:

**Caption** 

The caption of the object. (str)



-------

.. _no-11635:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)



-------

.. _no-11636:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    



-------

.. _no-11637:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    



-------

.. _no-11638:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    



-------

.. _no-11639:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.



-------

.. _no-11640:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.



-------

.. _no-11641:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.



-------

.. _no-11642:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.



-------

.. _no-11643:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.



-------

.. _no-11644:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.



-------

.. _no-11645:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.



-------

.. _no-11646:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.



-------

.. _no-11647:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.



-------

.. _no-11648:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.



-------

.. _no-11649:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.



-------

.. _no-11650:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.



-------

.. _no-11651:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.



-------

.. _no-11652:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.



-------

.. _no-11653:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.



-------

.. _no-11654:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.



-------

.. _no-11655:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.



-------

.. _no-11656:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.



-------

.. _no-11657:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.



-------

.. _no-11658:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.



-------

.. _no-11659:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.



-------

.. _no-11660:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.



-------

.. _no-11661:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.



-------

.. _no-11662:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.



-------

.. _no-11663:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.



-------

.. _no-11664:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.



-------

.. _no-11665:

**Enabled** 

Specifies whether the object and children can get user input. (bool)



-------

.. _no-11666:

**Font** 

Specifies font object for this control. (dFont)



-------

.. _no-11667:

**FontBold** 

Specifies if the font is bold-faced. (bool)



-------

.. _no-11668:

**FontDescription** 

Human-readable description of the current font settings. (str)



-------

.. _no-11669:

**FontFace** 

Specifies the font face. (str)



-------

.. _no-11670:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)



-------

.. _no-11671:

**FontItalic** 

Specifies whether font is italicized. (bool)



-------

.. _no-11672:

**FontSize** 

Specifies the point size of the font. (int)



-------

.. _no-11673:

**FontUnderline** 

Specifies whether text is underlined. (bool)



-------

.. _no-11674:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)



-------

.. _no-11676:

**Height** 

Specifies the height of the object. (int)



-------

.. _no-11677:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    



-------

.. _no-11678:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    



-------

.. _no-11679:

**Left** 

Specifies the left position of the object. (int)



-------

.. _no-11681:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)



-------

.. _no-11682:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)



-------

.. _no-11683:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)



-------

.. _no-11684:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)



-------

.. _no-11685:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)



-------

.. _no-11686:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)



-------

.. _no-11687:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)



-------

.. _no-11689:

**NameBase** 

Specifies the base name of the object.

    The base name specified will become the object's Name, unless another sibling
    already has that name, in which case Dabo will find the next unique name by
    adding integers to the end of the base name. For example, if your code says:

        self.NameBase = "txtAddress"

    and there is already a sibling object with that name, your object will end up
    with Name = "txtAddress1".

    This property is write-only at runtime.
    



-------

.. _no-11691:

**Position** 

The (x,y) position of the object. (tuple)



-------

.. _no-11693:

**RegID** 

A unique identifier used for referencing by other objects. (str)



-------

.. _no-11695:

**Size** 

The size of the object. (tuple)



-------

.. _no-11696:

**Sizer** 

The sizer for the object.



-------

.. _no-11697:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    



-------

.. _no-11698:

**Tag** 

A property that user code can safely use for specific purposes.



-------

.. _no-11699:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)



-------

.. _no-11700:

**Top** 

The top position of the object. (int)



-------

.. _no-11701:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    



-------

.. _no-11702:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    



-------

.. _no-11703:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)



-------

.. _no-11704:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    



-------

.. _no-11705:

**Width** 

The width of the object. (int)



-------

.. _no-11706:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)



-------


Properties - inherited
========================

.. _no-11623:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11625:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11626:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11631:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11633:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11634:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11675:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11680:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11688:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11690:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11692:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11694:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-11707>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-11708>`                 Occurs after the control or form is created.
:ref:`Destroy <no-11709>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-11710>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-11711>`               Occurs when the control gets the focus.
:ref:`Idle <no-11712>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-11713>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-11714>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-11715>`               
:ref:`KeyUp <no-11716>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-11717>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-11718>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-11719>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-11720>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-11721>`             
:ref:`MouseLeave <no-11722>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-11723>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-11724>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-11725>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-11726>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-11727>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-11728>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-11729>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-11730>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-11731>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-11732>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-11733>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-11734>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-11735>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-11736>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-11737>`                   Occurs when the control's position changes.
:ref:`Paint <no-11738>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-11739>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-11740>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-11741>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-11742>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-11707:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-11708:

**Create** 

Occurs after the control or form is created.



-------

.. _no-11709:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-11710:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-11711:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-11712:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-11713:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-11714:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-11715:

**KeyEvent** 



-------

.. _no-11716:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-11717:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-11718:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-11719:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-11720:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-11721:

**MouseEvent** 



-------

.. _no-11722:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-11723:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-11724:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-11725:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-11726:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-11727:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-11728:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-11729:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-11730:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-11731:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-11732:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-11733:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-11734:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-11735:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-11736:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-11737:

**Move** 

Occurs when the control's position changes.



-------

.. _no-11738:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-11739:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-11740:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-11741:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-11742:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-11743>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-11744>`             Instantiate object as a child of self.
:ref:`afterInit <no-11745>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-11746>`          
:ref:`afterSetProperties <no-11747>`    
:ref:`autoBindEvents <no-11748>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-11749>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-11750>`   
:ref:`bindEvent <no-11751>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-11752>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-11753>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-11754>`          Makes this object topmost
:ref:`clear <no-11755>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-11756>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-11757>`  Given a position relative to this control, return a position relative
:ref:`copy <no-11758>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-11759>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-11760>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-11761>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-11762>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-11763>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-11764>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-11765>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-11766>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-11767>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-11768>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-11769>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-11770>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-11771>`              Draws text on the object at the specified position
:ref:`endHover <no-11772>`              
:ref:`fitToSizer <no-11773>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-11774>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-11775>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-11776>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-11777>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-11778>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-11779>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-11780>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-11781>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-11782>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-11783>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-11784>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-11785>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-11786>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-11787>`                  Make the object invisible.
:ref:`initEvents <no-11788>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-11789>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-11790>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-11791>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-11792>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-11793>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-11794>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-11795>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-11796>`               
:ref:`paste <no-11797>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-11798>`           
:ref:`processDroppedFiles <no-11799>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-11800>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-11801>`            Raise the passed Dabo event.
:ref:`reCreate <no-11802>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-11803>`              Recreate the object.
:ref:`redraw <no-11804>`                Called when the object is (re)drawn.
:ref:`refresh <no-11805>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-11806>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-11807>`               Destroys the object.
:ref:`removeDrawnObject <no-11808>`     
:ref:`sendToBack <no-11809>`            Places this object behind all others.
:ref:`setAll <no-11810>`                Set all child object properties to the passed value.
:ref:`setFocus <no-11811>`              Sets focus to the object.
:ref:`setPositionInSizer <no-11812>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-11813>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-11814>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-11815>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-11816>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-11817>`                  Make the object visible.
:ref:`showContainingPage <no-11818>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-11819>`       Display a context menu (popup) at the specified position.
:ref:`super <no-11820>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-11821>`           Remove a previously registered event binding.
:ref:`unbindKey <no-11822>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-11823>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-11824>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-11825>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-11743:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.absoluteCoordinates(self, pos=None)

   Translates a position value for a control to absolute screen position.



-------

.. _no-11744:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.addObject(self, classRef, Name=None, \*args, \**kwargs)

   
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
   



-------

.. _no-11746:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.afterInitAll(self)



-------

.. _no-11747:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.afterSetProperties(self)



-------

.. _no-11750:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.beforeSetProperties(self, properties)



-------

.. _no-11753:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.bindKey(self, keyCombo, callback, \**kwargs)

   
   Bind a key combination such as "ctrl+c" to a callback function.
   
   See dKeys.keyStrings for the valid string key codes.
   See dKeys.modifierStrings for the valid modifier codes.
   
   Examples::
   
       # When user presses <esc>, close the form:
       form.bindKey("esc", form.Close)
   
       # When user presses <ctrl><alt><w>, close the form:
       form.bindKey("ctrl+alt+w", form.Close)
   
   



-------

.. _no-11754:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.bringToFront(self)

   Makes this object topmost



-------

.. _no-11755:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.clear(self)

   Clears the background of custom-drawn objects.



-------

.. _no-11756:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.clone(self, obj, name=None)

   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   



-------

.. _no-11757:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.containerCoordinates(self, cnt, pos=None)

   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   



-------

.. _no-11758:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.copy(self)

   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   



-------

.. _no-11759:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.cut(self)

   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   



-------

.. _no-11760:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11761:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)

   Draws a bitmap on the object at the specified position.



-------

.. _no-11762:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws a circle of the specified radius around the specified point.
   
   You can set the color and thickness of the line, as well as the
   color and hatching style of the fill. Normally, when persist=True,
   the circle will be re-drawn on paint events, but if you pass False,
   it will be drawn once only.
   
   A drawing object is returned, or None if persist=False. You can
   'remove' the drawing by setting the Visible property of the
   returned object to False. You can also manipulate the position, size,
   color, and fill by changing the various properties of the object.
   



-------

.. _no-11763:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11764:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11765:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   



-------

.. _no-11766:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11767:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11768:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11769:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11770:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   



-------

.. _no-11771:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)

   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   



-------

.. _no-11772:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.endHover(self, evt=None)



-------

.. _no-11773:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.fitToSizer(self, extraWidth=0, extraHeight=0)

   Resize the control to fit the size required by its sizer.



-------

.. _no-11777:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.formCoordinates(self, pos=None)

   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   



-------

.. _no-11779:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getCaptureBitmap(self)

   Return a bitmap snapshot of self as it appears in the UI at this moment.



-------

.. _no-11780:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getContainingPage(self)

   
   Return the dPage or WizardPage that contains self.
   



-------

.. _no-11781:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getDisplayLocker(self)

   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   



-------

.. _no-11782:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getMousePosition(self)

   
   Returns the current mouse position on the entire screen
   relative to this object.
   



-------

.. _no-11783:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getPositionInSizer(self)

   Convenience method to let you call this directly on the object.



-------

.. _no-11785:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getSizerProp(self, prop)

   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   



-------

.. _no-11786:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getSizerProps(self)

   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   



-------

.. _no-11787:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.hide(self)

   Make the object invisible.



-------

.. _no-11790:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.isContainedBy(self, obj)

   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   



-------

.. _no-11792:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.lockDisplay(self)

   
   Locks the visual updates to the control.
   
   This can significantly improve performance when many items are being
   updated at once.
   
   IMPORTANT: you must call unlockDisplay() when you are done, or your
   object will never draw. unlockDisplay() must be called once for every
   time lockDisplay() is called in order to resume repainting of the
   control. Alternatively, you can call lockDisplay() many times, and
   then call unlockDisplayAll() once when you are done.
   
   Note that lockDisplay currently doesn't do anything on GTK.
   



-------

.. _no-11793:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.moveTabOrderAfter(self, obj)

   Moves this object's tab order after the passed obj.



-------

.. _no-11794:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.moveTabOrderBefore(self, obj)

   Moves this object's tab order before the passed obj.



-------

.. _no-11795:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.objectCoordinates(self, pos=None)

   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   



-------

.. _no-11796:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.onHover(self, evt=None)



-------

.. _no-11797:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.paste(self)

   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   



-------

.. _no-11798:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.posIsWithin(self, xpos, ypos=None)



-------

.. _no-11799:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.processDroppedFiles(self, filelist, x, y)

   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   



-------

.. _no-11800:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.processDroppedText(self, txt, x, y)

   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   



-------

.. _no-11801:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)

   Raise the passed Dabo event.



-------

.. _no-11803:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.recreate(self, child=None)

   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   



-------

.. _no-11804:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.redraw(self, dc)

   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   



-------

.. _no-11805:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.refresh(self, fromRefresh=False)

   Repaints this control and all contained objects.



-------

.. _no-11806:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.relativeCoordinates(self, pos=None)

   Translates an absolute screen position to position value for a control.



-------

.. _no-11807:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.release(self)

   Destroys the object.



-------

.. _no-11808:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.removeDrawnObject(self, obj)



-------

.. _no-11809:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.sendToBack(self)

   Places this object behind all others.



-------

.. _no-11810:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)

   
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
   



-------

.. _no-11811:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.setFocus(self)

   Sets focus to the object.



-------

.. _no-11812:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.setPositionInSizer(self, pos)

   Convenience method to let you call this directly on the object.



-------

.. _no-11815:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.setSizerProp(self, prop, val)

   Tells the object's ControllingSizer to adjust the requested property.



-------

.. _no-11816:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.setSizerProps(self, propDict)

   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   



-------

.. _no-11817:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.show(self)

   Make the object visible.



-------

.. _no-11818:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.showContainingPage(self)

   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   



-------

.. _no-11819:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.showContextMenu(self, menu, pos=None, release=True)

   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   



-------

.. _no-11822:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.unbindKey(self, keyCombo)

   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   



-------

.. _no-11823:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.unlockDisplay(self)

   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   



-------

.. _no-11824:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.unlockDisplayAll(self)

   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   



-------

.. _no-11825:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.update(self)

   Update the properties of this object and all contained objects.



-------


Methods - inherited
=====================

.. _no-11745:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11748:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.autoBindEvents(self, force=True)
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

.. _no-11749:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11751:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11752:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11774:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11775:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11776:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11778:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11784:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-11788:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11789:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11791:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11802:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11813:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-11814:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-11820:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11821:

.. function:: dabo.ui.uiwx.dPemMixin.dPemMixin.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------


|
