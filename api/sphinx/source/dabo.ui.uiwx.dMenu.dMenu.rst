
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dMenu

.. _dabo.ui.uiwx.dMenu.dMenu:

====================================
|doc_title|  **dMenu.dMenu** - class
====================================


Creates a menu, which can contain submenus, menu items,
and separators.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dMenu**

.. inheritance-diagram:: dMenu


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dBaseMenuBar.EditMenu`
* :ref:`dabo.ui.uiwx.dBaseMenuBar.FileMenu`
* :ref:`dabo.ui.uiwx.dBaseMenuBar.HelpMenu`
* :ref:`dabo.ui.uiwx.dBaseMenuBar.ViewMenu`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dMenu.dMenu

   .. automethod:: dabo.ui.uiwx.dMenu.dMenu.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-11826>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-11827>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-11828>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-11829>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-11830>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-11831>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-11832>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-11833>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-11834>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-11835>`                Specifies the text of the menu.  (str)
:ref:`Children <no-11836>`               Returns a list of object references to the children of
:ref:`Class <no-11837>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-11838>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-11839>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-11840>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-11841>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-11842>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-11843>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-11844>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-11845>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-11846>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-11847>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-11848>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-11849>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-11850>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-11851>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-11852>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-11853>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-11854>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-11855>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-11856>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-11857>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicLeft <no-11858>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-11859>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-11860>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-11861>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-11862>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-11863>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-11864>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-11865>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-11866>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-11867>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-11868>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-11869>`                Specifies whether the menu can be interacted with. Default=True  (bool)
:ref:`Font <no-11870>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-11871>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-11872>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-11873>`               Specifies the font face. (str)
:ref:`FontInfo <no-11874>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-11875>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-11876>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-11877>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-11878>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-11879>`                   Specifies the form that contains the menu.  (dForm)
:ref:`Height <no-11880>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-11881>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-11882>`               Specifies the help text associated with this menu.  (str)
:ref:`Hover <no-11883>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-11884>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-11885>`              Specifies which events to log.  (list of strings)
:ref:`MRU <no-11886>`                    Determines if this menu uses Most Recently Used behavior. Default=False  (bool)
:ref:`MaximumHeight <no-11887>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-11888>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-11889>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MenuID <no-11890>`                 Identifying value for this menu. NOTE: there is no checking for
:ref:`MinimumHeight <no-11891>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-11892>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-11893>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-11894>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-11895>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-11896>`               Specifies the base name of the object.
:ref:`Parent <no-11897>`                 Specifies the parent menu or menubar.  (varies)
:ref:`Position <no-11898>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-11899>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-11900>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-11901>`                  The position of the right side of the object. This is a
:ref:`Size <no-11902>`                   The size of the object. (tuple)
:ref:`Sizer <no-11903>`                  The sizer for the object.
:ref:`StatusText <no-11904>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-11905>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-11906>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-11907>`                    The top position of the object. (int)
:ref:`Transparency <no-11908>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-11909>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-11910>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-11911>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-11912>`                  The width of the object. (int)
:ref:`WindowHandle <no-11913>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-11857:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.



-------

.. _no-11882:

**HelpText** 

Specifies the help text associated with this menu.  (str)



-------

.. _no-11886:

**MRU** 

Determines if this menu uses Most Recently Used behavior. Default=False  (bool)



-------

.. _no-11890:

**MenuID** 

Identifying value for this menu. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that MenuID values
    are unique.  (varies)



-------


Properties - inherited
========================

.. _no-11826:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11827:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11828:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11829:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11830:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11831:

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

.. _no-11832:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11833:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11834:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11835:

**Caption** 

Specifies the text of the menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11836:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11837:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11838:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11839:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11840:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11841:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11842:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11843:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11844:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11845:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11846:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11847:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11848:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11849:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11850:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11851:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11852:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11853:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11854:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11855:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11856:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11858:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11859:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11860:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11861:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11862:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11863:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11864:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11865:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11866:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11867:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11868:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11869:

**Enabled** 

Specifies whether the menu can be interacted with. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11870:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11871:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11872:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11873:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11874:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11875:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11876:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11877:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11878:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11879:

**Form** 

Specifies the form that contains the menu.  (dForm)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11880:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11881:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11883:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11884:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11885:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11887:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11888:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11889:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11891:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11892:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11893:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11894:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11895:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11896:

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

.. _no-11897:

**Parent** 

Specifies the parent menu or menubar.  (varies)


Inherited from: 'wx._core.Menu - can not provide a link

-------

.. _no-11898:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11899:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11900:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11901:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11902:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11903:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11904:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11905:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11906:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11907:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11908:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11909:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11910:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11911:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11912:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11913:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-11914>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-11915>`                 Occurs after the control or form is created.
:ref:`Destroy <no-11916>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-11917>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-11918>`               Occurs when the control gets the focus.
:ref:`Idle <no-11919>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-11920>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-11921>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-11922>`               
:ref:`KeyUp <no-11923>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-11924>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-11925>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-11926>`              
:ref:`MenuHighlight <no-11927>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-11928>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-11929>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-11930>`             
:ref:`MouseLeave <no-11931>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-11932>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-11933>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-11934>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-11935>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-11936>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-11937>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-11938>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-11939>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-11940>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-11941>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-11942>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-11943>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-11944>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-11945>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-11946>`                   Occurs when the control's position changes.
:ref:`Paint <no-11947>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-11948>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-11949>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-11950>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-11951>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-11914:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-11915:

**Create** 

Occurs after the control or form is created.



-------

.. _no-11916:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-11917:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-11918:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-11919:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-11920:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-11921:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-11922:

**KeyEvent** 



-------

.. _no-11923:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-11924:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-11925:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-11926:

**MenuEvent** 



-------

.. _no-11927:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-11928:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-11929:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-11930:

**MouseEvent** 



-------

.. _no-11931:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-11932:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-11933:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-11934:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-11935:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-11936:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-11937:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-11938:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-11939:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-11940:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-11941:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-11942:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-11943:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-11944:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-11945:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-11946:

**Move** 

Occurs when the control's position changes.



-------

.. _no-11947:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-11948:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-11949:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-11950:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-11951:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-11952>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-11953>`             Instantiate object as a child of self.
:ref:`afterInit <no-11954>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-11955>`          
:ref:`afterSetProperties <no-11956>`    
:ref:`append <no-11957>`                Append a dMenuItem with the specified properties.
:ref:`appendItem <no-11958>`            Insert a dMenuItem at the bottom of the menu.
:ref:`appendMenu <no-11959>`            Insert a dMenu at the bottom of the menu.
:ref:`appendSeparator <no-11960>`       Insert a separator at the bottom of the menu.
:ref:`autoBindEvents <no-11961>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-11962>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-11963>`   
:ref:`bindEvent <no-11964>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-11965>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-11966>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-11967>`          Makes this object topmost
:ref:`clear <no-11968>`                 Removes all items in this menu.
:ref:`clearChecks <no-11969>`           Unchecks any checkmark-type menu items.
:ref:`clone <no-11970>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-11971>`  Given a position relative to this control, return a position relative
:ref:`copy <no-11972>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-11973>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-11974>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-11975>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-11976>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-11977>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-11978>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-11979>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-11980>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-11981>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-11982>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-11983>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-11984>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-11985>`              Draws text on the object at the specified position
:ref:`endHover <no-11986>`              
:ref:`fitToSizer <no-11987>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-11988>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-11989>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-11990>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-11991>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-11992>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-11993>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-11994>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-11995>`      Returns an object that locks the current display when created, and
:ref:`getItem <no-11996>`               Returns a reference to the menu item with the specified ItemID or Caption.
:ref:`getItemIndex <no-11997>`          Returns the index of the item with the specified caption; you can
:ref:`getMousePosition <no-11998>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-11999>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-12000>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-12001>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-12002>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-12003>`                  Make the object invisible.
:ref:`initEvents <no-12004>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-12005>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-12006>`                Insert a dMenuItem at the given position with the specified properties.
:ref:`insertItem <no-12007>`            Insert a dMenuItem before the specified position in the menu.
:ref:`insertMenu <no-12008>`            Insert a dMenu before the specified position in the menu.
:ref:`insertSeparator <no-12009>`       Insert a separator before the specified position in the menu.
:ref:`isContainedBy <no-12010>`         Returns True if the containership hierarchy for this control
:ref:`isItemChecked <no-12011>`         
:ref:`iterateCall <no-12012>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-12013>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-12014>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-12015>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-12016>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-12017>`               
:ref:`paste <no-12018>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-12019>`           
:ref:`prepend <no-12020>`               Prepend a dMenuItem with the specified properties.
:ref:`prependItem <no-12021>`           Insert a dMenuItem at the top of the menu.
:ref:`prependMenu <no-12022>`           Insert a dMenu at the top of the menu.
:ref:`prependSeparator <no-12023>`      Insert a separator at the top of the menu.
:ref:`processDroppedFiles <no-12024>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-12025>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-12026>`            Raise the passed Dabo event.
:ref:`reCreate <no-12027>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-12028>`              Recreate the object.
:ref:`redraw <no-12029>`                Called when the object is (re)drawn.
:ref:`refresh <no-12030>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-12031>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-12032>`               Destroys the object.
:ref:`remove <no-12033>`                Removes the specified item from the menu. You may specify the item by
:ref:`removeDrawnObject <no-12034>`     
:ref:`sendToBack <no-12035>`            Places this object behind all others.
:ref:`setAll <no-12036>`                Set all child object properties to the passed value.
:ref:`setCheck <no-12037>`              When using checkmark-type menus, passing either the item
:ref:`setFocus <no-12038>`              Sets focus to the object.
:ref:`setItemCheck <no-12039>`          Pass a menu item and a boolean value, and the checked
:ref:`setPositionInSizer <no-12040>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-12041>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-12042>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-12043>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-12044>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-12045>`                  Make the object visible.
:ref:`showContainingPage <no-12046>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-12047>`       Display a context menu (popup) at the specified position.
:ref:`super <no-12048>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-12049>`           Remove a previously registered event binding.
:ref:`unbindKey <no-12050>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-12051>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-12052>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-12053>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-11957:

.. function:: dabo.ui.uiwx.dMenu.dMenu.append(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)

   
   Append a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   



-------

.. _no-11958:

.. function:: dabo.ui.uiwx.dMenu.dMenu.appendItem(self, item)

   Insert a dMenuItem at the bottom of the menu.



-------

.. _no-11959:

.. function:: dabo.ui.uiwx.dMenu.dMenu.appendMenu(self, menu)

   Insert a dMenu at the bottom of the menu.



-------

.. _no-11960:

.. function:: dabo.ui.uiwx.dMenu.dMenu.appendSeparator(self)

   Insert a separator at the bottom of the menu.



-------

.. _no-11968:

.. function:: dabo.ui.uiwx.dMenu.dMenu.clear(self)

   Removes all items in this menu.



-------

.. _no-11969:

.. function:: dabo.ui.uiwx.dMenu.dMenu.clearChecks(self)

   Unchecks any checkmark-type menu items.



-------

.. _no-11996:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getItem(self, idOrCaption)

   
   Returns a reference to the menu item with the specified ItemID or Caption.
   The ItemID property is checked first; then the Caption. If no match is found,
   None is returned.
   



-------

.. _no-11997:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getItemIndex(self, captionOrItem)

   
   Returns the index of the item with the specified caption; you can
   optionally pass in a reference to the menu item itself. If the item
   isn't found, None is returned.
   



-------

.. _no-12006:

.. function:: dabo.ui.uiwx.dMenu.dMenu.insert(self, pos, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)

   
   Insert a dMenuItem at the given position with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   



-------

.. _no-12007:

.. function:: dabo.ui.uiwx.dMenu.dMenu.insertItem(self, pos, item)

   Insert a dMenuItem before the specified position in the menu.



-------

.. _no-12008:

.. function:: dabo.ui.uiwx.dMenu.dMenu.insertMenu(self, pos, menu)

   Insert a dMenu before the specified position in the menu.



-------

.. _no-12009:

.. function:: dabo.ui.uiwx.dMenu.dMenu.insertSeparator(self, pos)

   Insert a separator before the specified position in the menu.



-------

.. _no-12011:

.. function:: dabo.ui.uiwx.dMenu.dMenu.isItemChecked(self, capIdxOrItem)



-------

.. _no-12020:

.. function:: dabo.ui.uiwx.dMenu.dMenu.prepend(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)

   
   Prepend a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   



-------

.. _no-12021:

.. function:: dabo.ui.uiwx.dMenu.dMenu.prependItem(self, item)

   Insert a dMenuItem at the top of the menu.



-------

.. _no-12022:

.. function:: dabo.ui.uiwx.dMenu.dMenu.prependMenu(self, menu)

   Insert a dMenu at the top of the menu.



-------

.. _no-12023:

.. function:: dabo.ui.uiwx.dMenu.dMenu.prependSeparator(self)

   Insert a separator at the top of the menu.



-------

.. _no-12033:

.. function:: dabo.ui.uiwx.dMenu.dMenu.remove(self, capIdxOrItem, release=True)

   
   Removes the specified item from the menu. You may specify the item by
   passing its index, its Caption, or by passing the item itself. If release is
   True (the default), the item is destroyed as well. If release is False, a reference
   to the object will be returned, and the caller is responsible for destroying it.
   



-------

.. _no-12037:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setCheck(self, capIdxOrItem, unCheckOthers=True)

   
   When using checkmark-type menus, passing either the item
   itself, or the index or caption of the item you want checked to
   this method will check that item. If unCheckOthers is True, non-
   matching items will be unchecked.
   



-------

.. _no-12039:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setItemCheck(self, itm, val)

   
   Pass a menu item and a boolean value, and the checked
   state of that menu item will be set accordingly.
   



-------


Methods - inherited
=====================

.. _no-11952:

.. function:: dabo.ui.uiwx.dMenu.dMenu.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11953:

.. function:: dabo.ui.uiwx.dMenu.dMenu.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-11954:

.. function:: dabo.ui.uiwx.dMenu.dMenu.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11955:

.. function:: dabo.ui.uiwx.dMenu.dMenu.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11956:

.. function:: dabo.ui.uiwx.dMenu.dMenu.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11961:

.. function:: dabo.ui.uiwx.dMenu.dMenu.autoBindEvents(self, force=True)
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

.. _no-11962:

.. function:: dabo.ui.uiwx.dMenu.dMenu.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11963:

.. function:: dabo.ui.uiwx.dMenu.dMenu.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11964:

.. function:: dabo.ui.uiwx.dMenu.dMenu.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11965:

.. function:: dabo.ui.uiwx.dMenu.dMenu.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11966:

.. function:: dabo.ui.uiwx.dMenu.dMenu.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-11967:

.. function:: dabo.ui.uiwx.dMenu.dMenu.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11970:

.. function:: dabo.ui.uiwx.dMenu.dMenu.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11971:

.. function:: dabo.ui.uiwx.dMenu.dMenu.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11972:

.. function:: dabo.ui.uiwx.dMenu.dMenu.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11973:

.. function:: dabo.ui.uiwx.dMenu.dMenu.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11974:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11975:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11976:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-11977:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11978:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11979:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11980:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11981:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11982:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11983:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11984:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11985:

.. function:: dabo.ui.uiwx.dMenu.dMenu.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11986:

.. function:: dabo.ui.uiwx.dMenu.dMenu.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11987:

.. function:: dabo.ui.uiwx.dMenu.dMenu.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11988:

.. function:: dabo.ui.uiwx.dMenu.dMenu.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11989:

.. function:: dabo.ui.uiwx.dMenu.dMenu.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11990:

.. function:: dabo.ui.uiwx.dMenu.dMenu.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11991:

.. function:: dabo.ui.uiwx.dMenu.dMenu.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11992:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11993:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11994:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11995:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11998:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11999:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12000:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-12001:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12002:

.. function:: dabo.ui.uiwx.dMenu.dMenu.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12003:

.. function:: dabo.ui.uiwx.dMenu.dMenu.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12004:

.. function:: dabo.ui.uiwx.dMenu.dMenu.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12005:

.. function:: dabo.ui.uiwx.dMenu.dMenu.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12010:

.. function:: dabo.ui.uiwx.dMenu.dMenu.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12012:

.. function:: dabo.ui.uiwx.dMenu.dMenu.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12013:

.. function:: dabo.ui.uiwx.dMenu.dMenu.lockDisplay(self)
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

.. _no-12014:

.. function:: dabo.ui.uiwx.dMenu.dMenu.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12015:

.. function:: dabo.ui.uiwx.dMenu.dMenu.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12016:

.. function:: dabo.ui.uiwx.dMenu.dMenu.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12017:

.. function:: dabo.ui.uiwx.dMenu.dMenu.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12018:

.. function:: dabo.ui.uiwx.dMenu.dMenu.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12019:

.. function:: dabo.ui.uiwx.dMenu.dMenu.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12024:

.. function:: dabo.ui.uiwx.dMenu.dMenu.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12025:

.. function:: dabo.ui.uiwx.dMenu.dMenu.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12026:

.. function:: dabo.ui.uiwx.dMenu.dMenu.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12027:

.. function:: dabo.ui.uiwx.dMenu.dMenu.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12028:

.. function:: dabo.ui.uiwx.dMenu.dMenu.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12029:

.. function:: dabo.ui.uiwx.dMenu.dMenu.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12030:

.. function:: dabo.ui.uiwx.dMenu.dMenu.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12031:

.. function:: dabo.ui.uiwx.dMenu.dMenu.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12032:

.. function:: dabo.ui.uiwx.dMenu.dMenu.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12034:

.. function:: dabo.ui.uiwx.dMenu.dMenu.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12035:

.. function:: dabo.ui.uiwx.dMenu.dMenu.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12036:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-12038:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12040:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12041:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-12042:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-12043:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12044:

.. function:: dabo.ui.uiwx.dMenu.dMenu.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12045:

.. function:: dabo.ui.uiwx.dMenu.dMenu.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12046:

.. function:: dabo.ui.uiwx.dMenu.dMenu.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12047:

.. function:: dabo.ui.uiwx.dMenu.dMenu.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12048:

.. function:: dabo.ui.uiwx.dMenu.dMenu.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12049:

.. function:: dabo.ui.uiwx.dMenu.dMenu.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12050:

.. function:: dabo.ui.uiwx.dMenu.dMenu.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12051:

.. function:: dabo.ui.uiwx.dMenu.dMenu.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12052:

.. function:: dabo.ui.uiwx.dMenu.dMenu.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12053:

.. function:: dabo.ui.uiwx.dMenu.dMenu.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
