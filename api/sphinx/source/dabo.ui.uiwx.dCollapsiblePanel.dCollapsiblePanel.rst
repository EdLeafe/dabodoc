
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dCollapsiblePanel

.. _dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel:

============================================================
|doc_title|  **dCollapsiblePanel.dCollapsiblePanel** - class
============================================================


A collapsible pane is a container with an embedded button-like control which can
be used by the user to collapse or expand the pane's contents.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dCollapsiblePanel**

.. inheritance-diagram:: dCollapsiblePanel


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* :ref:`wx.lib.agw.pycollapsiblepane.PyCollapsiblePane`



|subclasses| Known Subclasses
=============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel

   .. automethod:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-21876>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-21877>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-21878>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-21879>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-21880>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-21881>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-21882>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-21883>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-21884>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-21885>`                The caption of the object. (str)
:ref:`Children <no-21886>`               Returns a list of object references to the children of
:ref:`Class <no-21887>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-21888>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-21889>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-21890>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-21891>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-21892>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-21893>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-21894>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-21895>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-21896>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-21897>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-21898>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-21899>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-21900>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-21901>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-21902>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-21903>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-21904>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-21905>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-21906>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-21907>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-21908>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-21909>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-21910>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-21911>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-21912>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-21913>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-21914>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-21915>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-21916>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-21917>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-21918>`                Specifies whether the object and children can get user input. (bool)
:ref:`ExpanderDimensions <no-21919>`     Dimensions of the visible expander control.
:ref:`Font <no-21920>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-21921>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-21922>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-21923>`               Specifies the font face. (str)
:ref:`FontInfo <no-21924>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-21925>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-21926>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-21927>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-21928>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-21929>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-21930>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-21931>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-21932>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-21933>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-21934>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-21935>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-21936>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-21937>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-21938>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-21939>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-21940>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-21941>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-21942>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-21943>`               Specifies the base name of the object.
:ref:`Panel <no-21944>`                  Return panel object reference.
:ref:`PanelStyle <no-21945>`             Specifies pane style and can be 'Label' (default) or 'Button'.
:ref:`Parent <no-21946>`                 The containing object. (obj)
:ref:`Position <no-21947>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-21948>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-21949>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-21950>`                  The position of the right side of the object. This is a
:ref:`Size <no-21951>`                   The size of the object. (tuple)
:ref:`Sizer <no-21952>`                  The sizer for the object.
:ref:`StatusText <no-21953>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-21954>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-21955>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-21956>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-21957>`                    The top position of the object. (int)
:ref:`Transparency <no-21958>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-21959>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-21960>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-21961>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-21962>`                  The width of the object. (int)
:ref:`WindowHandle <no-21963>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-21919:

**ExpanderDimensions** 

Dimensions of the visible expander control.



-------

.. _no-21944:

**Panel** 

Return panel object reference.



-------

.. _no-21945:

**PanelStyle** 

Specifies pane style and can be 'Label' (default) or 'Button'.



-------


Properties - inherited
========================

.. _no-21876:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21877:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21878:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21879:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21880:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21881:

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

.. _no-21882:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21883:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21884:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21885:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21886:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21887:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21888:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21889:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21890:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21891:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21892:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21893:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21894:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21895:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21896:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21897:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21898:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21899:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21900:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21901:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21902:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21903:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21904:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21905:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21906:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21907:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21908:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21909:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21910:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21911:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21912:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21913:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21914:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21915:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21916:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21917:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21918:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21920:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21921:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21922:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21923:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21924:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21925:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21926:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21927:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21928:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21929:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21930:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21931:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21932:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21933:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21934:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21935:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21936:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21937:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21938:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21939:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21940:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21941:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21942:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21943:

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

.. _no-21946:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21947:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21948:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21949:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21950:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21951:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21952:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21953:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21954:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-21955:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21956:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21957:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21958:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21959:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21960:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21961:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21962:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21963:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-21964>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-21965>`                 Occurs after the control or form is created.
:ref:`Destroy <no-21966>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-21967>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-21968>`               Occurs when the control gets the focus.
:ref:`Idle <no-21969>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-21970>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-21971>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-21972>`               
:ref:`KeyUp <no-21973>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-21974>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-21975>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-21976>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-21977>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-21978>`             
:ref:`MouseLeave <no-21979>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-21980>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-21981>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-21982>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-21983>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-21984>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-21985>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-21986>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-21987>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-21988>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-21989>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-21990>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-21991>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-21992>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-21993>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-21994>`                   Occurs when the control's position changes.
:ref:`Paint <no-21995>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-21996>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-21997>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-21998>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-21999>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-21964:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-21965:

**Create** 

Occurs after the control or form is created.



-------

.. _no-21966:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-21967:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-21968:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-21969:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-21970:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-21971:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-21972:

**KeyEvent** 



-------

.. _no-21973:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-21974:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-21975:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-21976:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-21977:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-21978:

**MouseEvent** 



-------

.. _no-21979:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-21980:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-21981:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-21982:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-21983:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-21984:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-21985:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-21986:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-21987:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-21988:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-21989:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-21990:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-21991:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-21992:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-21993:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-21994:

**Move** 

Occurs when the control's position changes.



-------

.. _no-21995:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-21996:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-21997:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-21998:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-21999:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-22000>`           Translates a position value for a control to absolute screen position.
:ref:`addObject <no-22001>`                     Instantiate object as a child of self.
:ref:`afterInit <no-22002>`                     Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-22003>`                  
:ref:`afterSetProperties <no-22004>`            
:ref:`autoBindEvents <no-22005>`                Automatically bind any on*() methods to the associated event.
:ref:`base_AcceptsFocus <no-22006>`             Please use PyPanel.AcceptsFocus instead.
:ref:`base_AcceptsFocusFromKeyboard <no-22007>` Please use PyPanel.AcceptsFocusFromKeyboard instead.
:ref:`base_AddChild <no-22008>`                 Please use PyPanel.AddChild instead.
:ref:`base_DoGetBestSize <no-22009>`            Please use PyPanel.DoGetBestSize instead.
:ref:`base_DoGetClientSize <no-22010>`          Please use PyPanel.DoGetClientSize instead.
:ref:`base_DoGetPosition <no-22011>`            Please use PyPanel.DoGetPosition instead.
:ref:`base_DoGetSize <no-22012>`                Please use PyPanel.DoGetSize instead.
:ref:`base_DoGetVirtualSize <no-22013>`         Please use PyPanel.DoGetVirtualSize instead.
:ref:`base_DoMoveWindow <no-22014>`             Please use PyPanel.DoMoveWindow instead.
:ref:`base_DoSetClientSize <no-22015>`          Please use PyPanel.DoSetClientSize instead.
:ref:`base_DoSetSize <no-22016>`                Please use PyPanel.DoSetSize instead.
:ref:`base_DoSetVirtualSize <no-22017>`         Please use PyPanel.DoSetVirtualSize instead.
:ref:`base_Enable <no-22018>`                   Please use PyPanel.Enable instead.
:ref:`base_GetDefaultAttributes <no-22019>`     Please use PyPanel.GetDefaultAttributes instead.
:ref:`base_GetMaxSize <no-22020>`               Please use PyPanel.GetMaxSize instead.
:ref:`base_InitDialog <no-22021>`               Please use PyPanel.InitDialog instead.
:ref:`base_OnInternalIdle <no-22022>`           Please use PyPanel.OnInternalIdle instead.
:ref:`base_RemoveChild <no-22023>`              Please use PyPanel.RemoveChild instead.
:ref:`base_ShouldInheritColours <no-22024>`     Please use PyPanel.ShouldInheritColours instead.
:ref:`base_TransferDataFromWindow <no-22025>`   Please use PyPanel.TransferDataFromWindow instead.
:ref:`base_TransferDataToWindow <no-22026>`     Please use PyPanel.TransferDataToWindow instead.
:ref:`base_Validate <no-22027>`                 Please use PyPanel.Validate instead.
:ref:`beforeInit <no-22028>`                    Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-22029>`           
:ref:`bindEvent <no-22030>`                     Bind a dEvent to a callback function.
:ref:`bindEvents <no-22031>`                    Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-22032>`                       Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-22033>`                  Makes this object topmost
:ref:`clear <no-22034>`                         Clears the background of custom-drawn objects.
:ref:`clone <no-22035>`                         Create another object just like the passed object. It assumes that the
:ref:`collapse <no-22036>`                      
:ref:`containerCoordinates <no-22037>`          Given a position relative to this control, return a position relative
:ref:`copy <no-22038>`                          Called by uiApp when the user requests a copy operation.
:ref:`createItems <no-22039>`                   Create the controls in the pane.
:ref:`cut <no-22040>`                           Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-22041>`                       Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-22042>`                    Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-22043>`                    Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-22044>`                   Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-22045>`               Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-22046>`                  Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-22047>`                      Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-22048>`                 Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-22049>`                   Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-22050>`                 Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-22051>`          Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-22052>`                      Draws text on the object at the specified position
:ref:`endHover <no-22053>`                      
:ref:`expand <no-22054>`                        
:ref:`fitToSizer <no-22055>`                    Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-22056>`                    Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-22057>`                Reset the font zoom back to zero.
:ref:`fontZoomOut <no-22058>`                   Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-22059>`               Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-22060>`               Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-22061>`              Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-22062>`             Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-22063>`              Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-22064>`              Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-22065>`            Convenience method to let you call this directly on the object.
:ref:`getProperties <no-22066>`                 Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-22067>`                  Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-22068>`                 Returns a dict containing the object's sizer property info. The
:ref:`hide <no-22069>`                          Make the object invisible.
:ref:`initEvents <no-22070>`                    Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-22071>`                Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-22072>`                 Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-22073>`                   Call the given function on this object and all of its Children. If
:ref:`layout <no-22074>`                        
:ref:`lockDisplay <no-22075>`                   Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-22076>`             Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-22077>`            Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-22078>`             Given a position relative to the form, return a position relative
:ref:`onHover <no-22079>`                       
:ref:`paste <no-22080>`                         Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-22081>`                   
:ref:`processDroppedFiles <no-22082>`           Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-22083>`            Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-22084>`                    Raise the passed Dabo event.
:ref:`reCreate <no-22085>`                      Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-22086>`                      Recreate the object.
:ref:`redraw <no-22087>`                        Called when the object is (re)drawn.
:ref:`refresh <no-22088>`                       Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-22089>`           Translates an absolute screen position to position value for a control.
:ref:`release <no-22090>`                       Destroys the object.
:ref:`removeDrawnObject <no-22091>`             
:ref:`sendToBack <no-22092>`                    Places this object behind all others.
:ref:`setAll <no-22093>`                        Set all child object properties to the passed value.
:ref:`setFocus <no-22094>`                      Sets focus to the object.
:ref:`setPositionInSizer <no-22095>`            Convenience method to let you call this directly on the object.
:ref:`setProperties <no-22096>`                 Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-22097>`         Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-22098>`                  Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-22099>`                 Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-22100>`                          Make the object visible.
:ref:`showContainingPage <no-22101>`            If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-22102>`               Display a context menu (popup) at the specified position.
:ref:`super <no-22103>`                         This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-22104>`                   Remove a previously registered event binding.
:ref:`unbindKey <no-22105>`                     Unbind a previously bound key combination.
:ref:`unlockDisplay <no-22106>`                 Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-22107>`              Immediately unlocks the display, no matter how many previous
:ref:`update <no-22108>`                        Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-22036:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.collapse(self)



-------

.. _no-22039:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.createItems(self)

    Create the controls in the pane.
   
   Called when the pane is expanded for the first time, allowing subclasses
   to delay-populate the pane.
   



-------

.. _no-22054:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.expand(self)



-------

.. _no-22074:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.layout(self)



-------


Methods - inherited
=====================

.. _no-22000:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22001:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-22002:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22003:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22004:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22005:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.autoBindEvents(self, force=True)
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

.. _no-22006:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_AcceptsFocus(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AcceptsFocus instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22007:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_AcceptsFocusFromKeyboard(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AcceptsFocusFromKeyboard instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22008:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_AddChild(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AddChild instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22009:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoGetBestSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetBestSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22010:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoGetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetClientSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22011:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoGetPosition(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetPosition instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22012:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoGetSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22013:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoGetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetVirtualSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22014:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoMoveWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoMoveWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22015:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoSetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetClientSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22016:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoSetSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22017:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_DoSetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetVirtualSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22018:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_Enable(*args, \**kwargs)
   :noindex:


   Please use PyPanel.Enable instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22019:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_GetDefaultAttributes(*args, \**kwargs)
   :noindex:


   Please use PyPanel.GetDefaultAttributes instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22020:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_GetMaxSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.GetMaxSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22021:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_InitDialog(*args, \**kwargs)
   :noindex:


   Please use PyPanel.InitDialog instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22022:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_OnInternalIdle(*args, \**kwargs)
   :noindex:


   Please use PyPanel.OnInternalIdle instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22023:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_RemoveChild(*args, \**kwargs)
   :noindex:


   Please use PyPanel.RemoveChild instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22024:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_ShouldInheritColours(*args, \**kwargs)
   :noindex:


   Please use PyPanel.ShouldInheritColours instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22025:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_TransferDataFromWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.TransferDataFromWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22026:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_TransferDataToWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.TransferDataToWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22027:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.base_Validate(*args, \**kwargs)
   :noindex:


   Please use PyPanel.Validate instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-22028:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22029:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22030:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22031:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22032:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-22033:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22034:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22035:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22037:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22038:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22040:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22041:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22042:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22043:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-22044:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22045:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22046:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22047:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22048:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22049:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22050:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22051:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22052:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22053:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22055:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22056:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22057:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22058:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22059:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22060:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22061:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22062:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22063:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22064:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22065:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22066:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-22067:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22068:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22069:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22070:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22071:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22072:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22073:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22075:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.lockDisplay(self)
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

.. _no-22076:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22077:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22078:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22079:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22080:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22081:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22082:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22083:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22084:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22085:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22086:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22087:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22088:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22089:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22090:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22091:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22092:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22093:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-22094:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22095:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22096:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-22097:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-22098:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22099:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22100:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22101:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22102:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22103:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22104:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22105:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22106:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22107:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22108:

.. function:: dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
