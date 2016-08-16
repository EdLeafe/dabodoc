
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBaseMenuBar

.. _dabo.ui.uiwx.dBaseMenuBar.ViewMenu:

==============================================
|doc_title|  **dBaseMenuBar.ViewMenu** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **ViewMenu**

.. inheritance-diagram:: ViewMenu


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dMenu.dMenu`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-29894>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-29895>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-29896>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-29897>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-29898>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-29899>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-29900>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-29901>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-29902>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-29903>`                Specifies the text of the menu.  (str)
:ref:`Children <no-29904>`               Returns a list of object references to the children of
:ref:`Class <no-29905>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-29906>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-29907>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-29908>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-29909>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-29910>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-29911>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-29912>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-29913>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-29914>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-29915>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-29916>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-29917>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-29918>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-29919>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-29920>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-29921>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-29922>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-29923>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-29924>`          Dynamically determine the value of the Height property.
:ref:`DynamicHelpText <no-29925>`        Dynamically determine the value of the HelpText property.
:ref:`DynamicLeft <no-29926>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-29927>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-29928>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-29929>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-29930>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-29931>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-29932>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-29933>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-29934>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-29935>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-29936>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-29937>`                Specifies whether the menu can be interacted with. Default=True  (bool)
:ref:`Font <no-29938>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-29939>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-29940>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-29941>`               Specifies the font face. (str)
:ref:`FontInfo <no-29942>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-29943>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-29944>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-29945>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-29946>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-29947>`                   Specifies the form that contains the menu.  (dForm)
:ref:`Height <no-29948>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-29949>`        Specifies the context-sensitive help text associated with this
:ref:`HelpText <no-29950>`               Specifies the help text associated with this menu.  (str)
:ref:`Hover <no-29951>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-29952>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-29953>`              Specifies which events to log.  (list of strings)
:ref:`MRU <no-29954>`                    Determines if this menu uses Most Recently Used behavior. Default=False  (bool)
:ref:`MaximumHeight <no-29955>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-29956>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-29957>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MenuID <no-29958>`                 Identifying value for this menu. NOTE: there is no checking for
:ref:`MinimumHeight <no-29959>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-29960>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-29961>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-29962>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-29963>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-29964>`               Specifies the base name of the object.
:ref:`Parent <no-29965>`                 Specifies the parent menu or menubar.  (varies)
:ref:`Position <no-29966>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-29967>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-29968>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-29969>`                  The position of the right side of the object. This is a
:ref:`Size <no-29970>`                   The size of the object. (tuple)
:ref:`Sizer <no-29971>`                  The sizer for the object.
:ref:`StatusText <no-29972>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-29973>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-29974>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-29975>`                    The top position of the object. (int)
:ref:`Transparency <no-29976>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-29977>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-29978>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-29979>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-29980>`                  The width of the object. (int)
:ref:`WindowHandle <no-29981>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-29894:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29895:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29896:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29897:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29898:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29899:

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

.. _no-29900:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29901:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29902:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29903:

**Caption** 

Specifies the text of the menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29904:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29905:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29906:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29907:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29908:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29909:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29910:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29911:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29912:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29913:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29914:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29915:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29916:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29917:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29918:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29919:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29920:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29921:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29922:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29923:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29924:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29925:

**DynamicHelpText** 

Dynamically determine the value of the HelpText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HelpText property. If DynamicHelpText is set to None (the default), HelpText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29926:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29927:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29928:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29929:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29930:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29931:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29932:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29933:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29934:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29935:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29936:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29937:

**Enabled** 

Specifies whether the menu can be interacted with. Default=True  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29938:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29939:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29940:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29941:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29942:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29943:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29944:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29945:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29946:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29947:

**Form** 

Specifies the form that contains the menu.  (dForm)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29948:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29949:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29950:

**HelpText** 

Specifies the help text associated with this menu.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29951:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29952:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29953:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29954:

**MRU** 

Determines if this menu uses Most Recently Used behavior. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29955:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29956:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29957:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29958:

**MenuID** 

Identifying value for this menu. NOTE: there is no checking for
    duplicate values; it is the responsibility to ensure that MenuID values
    are unique.  (varies)


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-29959:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29960:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29961:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29962:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29963:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29964:

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

.. _no-29965:

**Parent** 

Specifies the parent menu or menubar.  (varies)


Inherited from: 'wx._core.Menu - can not provide a link

-------

.. _no-29966:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29967:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29968:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29969:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29970:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29971:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29972:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29973:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29974:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29975:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29976:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29977:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29978:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29979:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29980:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29981:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-29982>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-29983>`                 Occurs after the control or form is created.
:ref:`Destroy <no-29984>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-29985>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-29986>`               Occurs when the control gets the focus.
:ref:`Idle <no-29987>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-29988>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-29989>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-29990>`               
:ref:`KeyUp <no-29991>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-29992>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-29993>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-29994>`              
:ref:`MenuHighlight <no-29995>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-29996>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-29997>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-29998>`             
:ref:`MouseLeave <no-29999>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-30000>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-30001>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-30002>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-30003>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-30004>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-30005>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-30006>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-30007>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-30008>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-30009>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-30010>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-30011>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-30012>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-30013>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-30014>`                   Occurs when the control's position changes.
:ref:`Paint <no-30015>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-30016>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-30017>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-30018>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-30019>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-29982:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-29983:

**Create** 

Occurs after the control or form is created.



-------

.. _no-29984:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-29985:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-29986:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-29987:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-29988:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-29989:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-29990:

**KeyEvent** 



-------

.. _no-29991:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-29992:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-29993:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-29994:

**MenuEvent** 



-------

.. _no-29995:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-29996:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-29997:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-29998:

**MouseEvent** 



-------

.. _no-29999:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-30000:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-30001:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-30002:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-30003:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-30004:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-30005:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-30006:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-30007:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-30008:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-30009:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-30010:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-30011:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-30012:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-30013:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-30014:

**Move** 

Occurs when the control's position changes.



-------

.. _no-30015:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-30016:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-30017:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-30018:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-30019:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-30020>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-30021>`             Instantiate object as a child of self.
:ref:`afterInit <no-30022>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-30023>`          
:ref:`afterSetProperties <no-30024>`    
:ref:`append <no-30025>`                Append a dMenuItem with the specified properties.
:ref:`appendItem <no-30026>`            Insert a dMenuItem at the bottom of the menu.
:ref:`appendMenu <no-30027>`            Insert a dMenu at the bottom of the menu.
:ref:`appendSeparator <no-30028>`       Insert a separator at the bottom of the menu.
:ref:`autoBindEvents <no-30029>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-30030>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-30031>`   
:ref:`bindEvent <no-30032>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-30033>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-30034>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-30035>`          Makes this object topmost
:ref:`clear <no-30036>`                 Removes all items in this menu.
:ref:`clearChecks <no-30037>`           Unchecks any checkmark-type menu items.
:ref:`clone <no-30038>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-30039>`  Given a position relative to this control, return a position relative
:ref:`copy <no-30040>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-30041>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-30042>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-30043>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-30044>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-30045>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-30046>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-30047>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-30048>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-30049>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-30050>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-30051>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-30052>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-30053>`              Draws text on the object at the specified position
:ref:`endHover <no-30054>`              
:ref:`fitToSizer <no-30055>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-30056>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-30057>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-30058>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-30059>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-30060>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-30061>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-30062>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-30063>`      Returns an object that locks the current display when created, and
:ref:`getItem <no-30064>`               Returns a reference to the menu item with the specified ItemID or Caption.
:ref:`getItemIndex <no-30065>`          Returns the index of the item with the specified caption; you can
:ref:`getMousePosition <no-30066>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-30067>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-30068>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-30069>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-30070>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-30071>`                  Make the object invisible.
:ref:`initEvents <no-30072>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-30073>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-30074>`                Insert a dMenuItem at the given position with the specified properties.
:ref:`insertItem <no-30075>`            Insert a dMenuItem before the specified position in the menu.
:ref:`insertMenu <no-30076>`            Insert a dMenu before the specified position in the menu.
:ref:`insertSeparator <no-30077>`       Insert a separator before the specified position in the menu.
:ref:`isContainedBy <no-30078>`         Returns True if the containership hierarchy for this control
:ref:`isItemChecked <no-30079>`         
:ref:`iterateCall <no-30080>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-30081>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-30082>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-30083>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-30084>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-30085>`               
:ref:`paste <no-30086>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-30087>`           
:ref:`prepend <no-30088>`               Prepend a dMenuItem with the specified properties.
:ref:`prependItem <no-30089>`           Insert a dMenuItem at the top of the menu.
:ref:`prependMenu <no-30090>`           Insert a dMenu at the top of the menu.
:ref:`prependSeparator <no-30091>`      Insert a separator at the top of the menu.
:ref:`processDroppedFiles <no-30092>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-30093>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-30094>`            Raise the passed Dabo event.
:ref:`reCreate <no-30095>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-30096>`              Recreate the object.
:ref:`redraw <no-30097>`                Called when the object is (re)drawn.
:ref:`refresh <no-30098>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-30099>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-30100>`               Destroys the object.
:ref:`remove <no-30101>`                Removes the specified item from the menu. You may specify the item by
:ref:`removeDrawnObject <no-30102>`     
:ref:`sendToBack <no-30103>`            Places this object behind all others.
:ref:`setAll <no-30104>`                Set all child object properties to the passed value.
:ref:`setCheck <no-30105>`              When using checkmark-type menus, passing either the item
:ref:`setFocus <no-30106>`              Sets focus to the object.
:ref:`setItemCheck <no-30107>`          Pass a menu item and a boolean value, and the checked
:ref:`setPositionInSizer <no-30108>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-30109>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-30110>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-30111>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-30112>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-30113>`                  Make the object visible.
:ref:`showContainingPage <no-30114>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-30115>`       Display a context menu (popup) at the specified position.
:ref:`super <no-30116>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-30117>`           Remove a previously registered event binding.
:ref:`unbindKey <no-30118>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-30119>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-30120>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-30121>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-30020:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30021:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-30022:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30023:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30024:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30025:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.append(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Append a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30026:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.appendItem(self, item)
   :noindex:


   Insert a dMenuItem at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30027:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.appendMenu(self, menu)
   :noindex:


   Insert a dMenu at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30028:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.appendSeparator(self)
   :noindex:


   Insert a separator at the bottom of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30029:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.autoBindEvents(self, force=True)
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

.. _no-30030:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30031:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30032:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30033:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30034:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-30035:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30036:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.clear(self)
   :noindex:


   Removes all items in this menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30037:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.clearChecks(self)
   :noindex:


   Unchecks any checkmark-type menu items.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30038:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30039:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30040:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30041:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30042:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30043:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30044:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-30045:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30046:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30047:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30048:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30049:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30050:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30051:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30052:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30053:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30054:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30055:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30056:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30057:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30058:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30059:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30060:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30061:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30062:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30063:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30064:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getItem(self, idOrCaption)
   :noindex:


   
   Returns a reference to the menu item with the specified ItemID or Caption.
   The ItemID property is checked first; then the Caption. If no match is found,
   None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30065:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getItemIndex(self, captionOrItem)
   :noindex:


   
   Returns the index of the item with the specified caption; you can
   optionally pass in a reference to the menu item itself. If the item
   isn't found, None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30066:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30067:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30068:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-30069:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30070:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30071:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30072:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30073:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30074:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.insert(self, pos, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Insert a dMenuItem at the given position with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30075:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.insertItem(self, pos, item)
   :noindex:


   Insert a dMenuItem before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30076:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.insertMenu(self, pos, menu)
   :noindex:


   Insert a dMenu before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30077:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.insertSeparator(self, pos)
   :noindex:


   Insert a separator before the specified position in the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30078:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30079:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.isItemChecked(self, capIdxOrItem)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30080:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30081:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.lockDisplay(self)
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

.. _no-30082:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30083:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30084:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30085:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30086:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30087:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30088:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.prepend(self, caption, help='', bmp=None, picture=None, menutype='', \*args, \**kwargs)
   :noindex:


   
   Prepend a dMenuItem with the specified properties.
   
   This is a convenient way to add a dMenuItem to a dMenu, give it a caption,
   help string, bitmap, and also bind it to a function, all in one call.
   
   Any additional keyword arguments passed will be interpreted as properties
   of the dMenuItem: if valid property names/values, the dMenuItem will take
   them on; if not valid, an exception will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30089:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.prependItem(self, item)
   :noindex:


   Insert a dMenuItem at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30090:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.prependMenu(self, menu)
   :noindex:


   Insert a dMenu at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30091:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.prependSeparator(self)
   :noindex:


   Insert a separator at the top of the menu.


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30092:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30093:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30094:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30095:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30096:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30097:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30098:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30099:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30100:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30101:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.remove(self, capIdxOrItem, release=True)
   :noindex:


   
   Removes the specified item from the menu. You may specify the item by
   passing its index, its Caption, or by passing the item itself. If release is
   True (the default), the item is destroyed as well. If release is False, a reference
   to the object will be returned, and the caller is responsible for destroying it.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30102:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30103:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30104:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-30105:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setCheck(self, capIdxOrItem, unCheckOthers=True)
   :noindex:


   
   When using checkmark-type menus, passing either the item
   itself, or the index or caption of the item you want checked to
   this method will check that item. If unCheckOthers is True, non-
   matching items will be unchecked.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30106:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30107:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setItemCheck(self, itm, val)
   :noindex:


   
   Pass a menu item and a boolean value, and the checked
   state of that menu item will be set accordingly.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenu.dMenu`

-------

.. _no-30108:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30109:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-30110:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-30111:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30112:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30113:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30114:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30115:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30116:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30117:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30118:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30119:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30120:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30121:

.. function:: dabo.ui.uiwx.dBaseMenuBar.ViewMenu.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
