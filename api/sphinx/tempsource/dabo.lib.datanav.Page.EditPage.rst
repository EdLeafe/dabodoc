
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.EditPage:

======================================
|doc_title|  **Page.EditPage** - class
======================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **EditPage**

.. inheritance-diagram:: EditPage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.datanav.Page.Page`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.EditPage

   .. automethod:: dabo.lib.datanav.Page.EditPage.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-2708>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-2709>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-2710>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-2711>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-2712>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-2713>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-2714>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-2715>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-2716>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-2717>`                 The text identifying this particular page.  (str)
:ref:`Children <no-2718>`                Child controls of this panel. This excludes the wx-specific
:ref:`Class <no-2719>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-2720>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-2721>`    Reference to the sizer item that control's this control's layout.
:ref:`DataSource <no-2722>`              Table that is the primary source for the fields displayed on the page  (str)
:ref:`DeferredUpdates <no-2723>`         Allow to defer controls updates until page become active.  (bool)
:ref:`DroppedFileHandler <no-2724>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-2725>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-2726>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-2727>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-2728>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-2729>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-2730>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-2731>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-2732>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-2733>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-2734>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-2735>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-2736>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-2737>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-2738>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-2739>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-2740>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-2741>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicImage <no-2742>`            Dynamically determine the value of the Image property.
:ref:`DynamicLeft <no-2743>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-2744>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-2745>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-2746>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-2747>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-2748>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-2749>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-2750>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-2751>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-2752>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-2753>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-2754>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-2755>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-2756>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-2757>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-2758>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-2759>`                Specifies the font face. (str)
:ref:`FontInfo <no-2760>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-2761>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-2762>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-2763>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-2764>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-2765>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-2766>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-2767>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-2768>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-2769>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Image <no-2770>`                   Sets the image that is displayed on the page tab. This is
:ref:`Left <no-2771>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-2772>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-2773>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-2774>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-2775>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-2776>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-2777>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-2778>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-2779>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-2780>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-2781>`                Specifies the base name of the object.
:ref:`Parent <no-2782>`                  The containing object. (obj)
:ref:`Position <no-2783>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-2784>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-2785>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-2786>`                   The position of the right side of the object. This is a
:ref:`Size <no-2787>`                    The size of the object. (tuple)
:ref:`Sizer <no-2788>`                   The sizer for the object.
:ref:`StatusText <no-2789>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-2790>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-2791>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-2792>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-2793>`                     The top position of the object. (int)
:ref:`Transparency <no-2794>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-2795>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateOnPageEnter <no-2796>`       Specifies whether an implicit self.update() happens upon page entry.
:ref:`VerticalScroll <no-2797>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-2798>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-2799>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-2800>`                   The width of the object. (int)
:ref:`WindowHandle <no-2801>`            The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-2722:

**DataSource** 

Table that is the primary source for the fields displayed on the page  (str)



-------


Properties - inherited
========================

.. _no-2708:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2709:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2710:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2711:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2712:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2713:

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

.. _no-2714:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2715:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2716:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2717:

**Caption** 

The text identifying this particular page.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2718:

**Children** 

Child controls of this panel. This excludes the wx-specific
    scroll bars  (list of objects)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2719:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2720:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2721:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2723:

**DeferredUpdates** 

Allow to defer controls updates until page become active.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2724:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2725:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2726:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2727:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2728:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2729:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2730:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2731:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2732:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2733:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2734:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2735:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2736:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2737:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2738:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2739:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2740:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2741:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2742:

**DynamicImage** 

Dynamically determine the value of the Image property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Image property. If DynamicImage is set to None (the default), Image
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2743:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2744:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2745:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2746:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2747:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2748:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2749:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2750:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2751:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2752:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2753:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2754:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2755:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2756:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2757:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2758:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2759:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2760:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2761:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2762:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2763:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2764:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2765:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2766:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2767:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2768:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2769:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2770:

**Image** 

Sets the image that is displayed on the page tab. This is
    determined by the key value passed, which must refer to an
    image already added to the parent pageframe.
    When used to retrieve an image, it returns the index of the
    page's image in the parent pageframe's image list.   (int)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2771:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2772:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2773:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2774:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2775:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2776:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2777:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2778:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2779:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2780:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2781:

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

.. _no-2782:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2783:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2784:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2785:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2786:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2787:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2788:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-2789:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2790:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-2791:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2792:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2793:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2794:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2795:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2796:

**UpdateOnPageEnter** 

Specifies whether an implicit self.update() happens upon page entry.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2797:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2798:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2799:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2800:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2801:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-2802>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-2803>`              Occurs when a child control is created.
:ref:`ControlNavigationEvent <no-2804>` 
:ref:`Create <no-2805>`                 Occurs after the control or form is created.
:ref:`Destroy <no-2806>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-2807>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-2808>`               Occurs when the control gets the focus.
:ref:`Idle <no-2809>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-2810>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-2811>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-2812>`               
:ref:`KeyUp <no-2813>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-2814>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-2815>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-2816>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-2817>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-2818>`             
:ref:`MouseLeave <no-2819>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-2820>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-2821>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-2822>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-2823>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-2824>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-2825>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-2826>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-2827>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-2828>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-2829>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-2830>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-2831>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-2832>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-2833>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-2834>`                   Occurs when the control's position changes.
:ref:`PageContextMenu <no-2835>`        Occurs when the user requests a context event for a dPage
:ref:`PageEnter <no-2836>`              Occurs when the page becomes the active page.
:ref:`PageLeave <no-2837>`              Occurs when a different page becomes active.
:ref:`Paint <no-2838>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-2839>`                 Occurs when the control or form is resized.
:ref:`ScrollBottom <no-2840>`           Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-2841>`            
:ref:`ScrollLineDown <no-2842>`         Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-2843>`           Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-2844>`         Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-2845>`           Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-2846>`        Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-2847>`     Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-2848>`              Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-2849>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-2850>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-2851>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-2802:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-2803:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-2804:

**ControlNavigationEvent** 



-------

.. _no-2805:

**Create** 

Occurs after the control or form is created.



-------

.. _no-2806:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-2807:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-2808:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-2809:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-2810:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-2811:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-2812:

**KeyEvent** 



-------

.. _no-2813:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-2814:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-2815:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-2816:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-2817:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-2818:

**MouseEvent** 



-------

.. _no-2819:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-2820:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-2821:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-2822:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-2823:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-2824:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-2825:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-2826:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-2827:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-2828:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-2829:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-2830:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-2831:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-2832:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-2833:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-2834:

**Move** 

Occurs when the control's position changes.



-------

.. _no-2835:

**PageContextMenu** 

Occurs when the user requests a context event for a dPage



-------

.. _no-2836:

**PageEnter** 

Occurs when the page becomes the active page.



-------

.. _no-2837:

**PageLeave** 

Occurs when a different page becomes active.



-------

.. _no-2838:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-2839:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-2840:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-2841:

**ScrollEvent** 



-------

.. _no-2842:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-2843:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-2844:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-2845:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-2846:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-2847:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-2848:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-2849:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-2850:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-2851:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-2852>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-2853>`             Instantiate object as a child of self.
:ref:`afterInit <no-2854>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-2855>`          
:ref:`afterSetProperties <no-2856>`    
:ref:`autoBindEvents <no-2857>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-2858>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-2859>`   
:ref:`bindEvent <no-2860>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-2861>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-2862>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-2863>`          Makes this object topmost
:ref:`buildPage <no-2864>`             
:ref:`clear <no-2865>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-2866>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-2867>`  Given a position relative to this control, return a position relative
:ref:`copy <no-2868>`                  Called by uiApp when the user requests a copy operation.
:ref:`createItems <no-2869>`           Subclass hook. Create your items and then call super()
:ref:`cut <no-2870>`                   Called by uiApp when the user requests a cut operation.
:ref:`deleteRecord <no-2871>`          Called by a browse grid when the user wants to delete the current row.
:ref:`drawArc <no-2872>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-2873>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-2874>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-2875>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-2876>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-2877>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-2878>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-2879>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-2880>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-2881>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-2882>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-2883>`              Draws text on the object at the specified position
:ref:`editRecord <no-2884>`            Called by a browse grid when the user wants to edit the current row.
:ref:`endHover <no-2885>`              
:ref:`fitToSizer <no-2886>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-2887>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-2888>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-2889>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-2890>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-2891>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-2892>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-2893>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-2894>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-2895>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-2896>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-2897>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-2898>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-2899>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-2900>`                  Make the object invisible.
:ref:`initEvents <no-2901>`            
:ref:`initProperties <no-2902>`        Hook for subclasses. User subclasses should set properties
:ref:`initSizer <no-2903>`             Set up the default vertical box sizer for the page.
:ref:`isContainedBy <no-2904>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-2905>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-2906>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-2907>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-2908>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-2909>`    Moves this object's tab order before the passed obj.
:ref:`newRecord <no-2910>`             Called by a browse grid when the user wants to add a new row.
:ref:`objectCoordinates <no-2911>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-2912>`               
:ref:`pageDown <no-2913>`              
:ref:`pageHorizontally <no-2914>`      Scroll horizontally one 'page' width.
:ref:`pageLeft <no-2915>`              
:ref:`pageRight <no-2916>`             
:ref:`pageUp <no-2917>`                
:ref:`pageVertically <no-2918>`        Scroll vertically one 'page' height.
:ref:`paste <no-2919>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-2920>`           
:ref:`processDroppedFiles <no-2921>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-2922>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-2923>`            Raise the passed Dabo event.
:ref:`reCreate <no-2924>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-2925>`              Recreate the object.
:ref:`redraw <no-2926>`                Called when the object is (re)drawn.
:ref:`refresh <no-2927>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-2928>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-2929>`               Destroys the object.
:ref:`removeDrawnObject <no-2930>`     
:ref:`scrollHorizontally <no-2931>`    Change the horizontal scroll position by 'amt' units.
:ref:`scrollVertically <no-2932>`      Change the vertical scroll position by 'amt' units.
:ref:`sendToBack <no-2933>`            Places this object behind all others.
:ref:`setAll <no-2934>`                Set all child object properties to the passed value.
:ref:`setFocus <no-2935>`              Sets focus to the object.
:ref:`setPositionInSizer <no-2936>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-2937>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-2938>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-2939>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-2940>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-2941>`                  Make the object visible.
:ref:`showContainingPage <no-2942>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-2943>`       Display a context menu (popup) at the specified position.
:ref:`super <no-2944>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-2945>`           Remove a previously registered event binding.
:ref:`unbindKey <no-2946>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-2947>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-2948>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-2949>`                

====================================== ========================


Methods
=======

.. _no-2864:

.. function:: dabo.lib.datanav.Page.EditPage.buildPage(self)



-------

.. _no-2869:

.. function:: dabo.lib.datanav.Page.EditPage.createItems(self)

   Subclass hook. Create your items and then call super()



-------

.. _no-2901:

.. function:: dabo.lib.datanav.Page.EditPage.initEvents(self)



-------


Methods - inherited
=====================

.. _no-2852:

.. function:: dabo.lib.datanav.Page.EditPage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2853:

.. function:: dabo.lib.datanav.Page.EditPage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-2854:

.. function:: dabo.lib.datanav.Page.EditPage.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2855:

.. function:: dabo.lib.datanav.Page.EditPage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2856:

.. function:: dabo.lib.datanav.Page.EditPage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2857:

.. function:: dabo.lib.datanav.Page.EditPage.autoBindEvents(self, force=True)
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

.. _no-2858:

.. function:: dabo.lib.datanav.Page.EditPage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2859:

.. function:: dabo.lib.datanav.Page.EditPage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2860:

.. function:: dabo.lib.datanav.Page.EditPage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2861:

.. function:: dabo.lib.datanav.Page.EditPage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2862:

.. function:: dabo.lib.datanav.Page.EditPage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-2863:

.. function:: dabo.lib.datanav.Page.EditPage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2865:

.. function:: dabo.lib.datanav.Page.EditPage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2866:

.. function:: dabo.lib.datanav.Page.EditPage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2867:

.. function:: dabo.lib.datanav.Page.EditPage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2868:

.. function:: dabo.lib.datanav.Page.EditPage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2870:

.. function:: dabo.lib.datanav.Page.EditPage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2871:

.. function:: dabo.lib.datanav.Page.EditPage.deleteRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to delete the current row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2872:

.. function:: dabo.lib.datanav.Page.EditPage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2873:

.. function:: dabo.lib.datanav.Page.EditPage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2874:

.. function:: dabo.lib.datanav.Page.EditPage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-2875:

.. function:: dabo.lib.datanav.Page.EditPage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2876:

.. function:: dabo.lib.datanav.Page.EditPage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2877:

.. function:: dabo.lib.datanav.Page.EditPage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2878:

.. function:: dabo.lib.datanav.Page.EditPage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2879:

.. function:: dabo.lib.datanav.Page.EditPage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2880:

.. function:: dabo.lib.datanav.Page.EditPage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2881:

.. function:: dabo.lib.datanav.Page.EditPage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2882:

.. function:: dabo.lib.datanav.Page.EditPage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2883:

.. function:: dabo.lib.datanav.Page.EditPage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2884:

.. function:: dabo.lib.datanav.Page.EditPage.editRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to edit the current row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2885:

.. function:: dabo.lib.datanav.Page.EditPage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2886:

.. function:: dabo.lib.datanav.Page.EditPage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2887:

.. function:: dabo.lib.datanav.Page.EditPage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2888:

.. function:: dabo.lib.datanav.Page.EditPage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2889:

.. function:: dabo.lib.datanav.Page.EditPage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2890:

.. function:: dabo.lib.datanav.Page.EditPage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2891:

.. function:: dabo.lib.datanav.Page.EditPage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2892:

.. function:: dabo.lib.datanav.Page.EditPage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2893:

.. function:: dabo.lib.datanav.Page.EditPage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2894:

.. function:: dabo.lib.datanav.Page.EditPage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2895:

.. function:: dabo.lib.datanav.Page.EditPage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2896:

.. function:: dabo.lib.datanav.Page.EditPage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2897:

.. function:: dabo.lib.datanav.Page.EditPage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-2898:

.. function:: dabo.lib.datanav.Page.EditPage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2899:

.. function:: dabo.lib.datanav.Page.EditPage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2900:

.. function:: dabo.lib.datanav.Page.EditPage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2902:

.. function:: dabo.lib.datanav.Page.EditPage.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2903:

.. function:: dabo.lib.datanav.Page.EditPage.initSizer(self)
   :noindex:


   Set up the default vertical box sizer for the page.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-2904:

.. function:: dabo.lib.datanav.Page.EditPage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2905:

.. function:: dabo.lib.datanav.Page.EditPage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2906:

.. function:: dabo.lib.datanav.Page.EditPage.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-2907:

.. function:: dabo.lib.datanav.Page.EditPage.lockDisplay(self)
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

.. _no-2908:

.. function:: dabo.lib.datanav.Page.EditPage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2909:

.. function:: dabo.lib.datanav.Page.EditPage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2910:

.. function:: dabo.lib.datanav.Page.EditPage.newRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to add a new row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-2911:

.. function:: dabo.lib.datanav.Page.EditPage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2912:

.. function:: dabo.lib.datanav.Page.EditPage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2913:

.. function:: dabo.lib.datanav.Page.EditPage.pageDown(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2914:

.. function:: dabo.lib.datanav.Page.EditPage.pageHorizontally(self, direction)
   :noindex:


   Scroll horizontally one 'page' width.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2915:

.. function:: dabo.lib.datanav.Page.EditPage.pageLeft(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2916:

.. function:: dabo.lib.datanav.Page.EditPage.pageRight(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2917:

.. function:: dabo.lib.datanav.Page.EditPage.pageUp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2918:

.. function:: dabo.lib.datanav.Page.EditPage.pageVertically(self, direction)
   :noindex:


   Scroll vertically one 'page' height.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2919:

.. function:: dabo.lib.datanav.Page.EditPage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2920:

.. function:: dabo.lib.datanav.Page.EditPage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2921:

.. function:: dabo.lib.datanav.Page.EditPage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2922:

.. function:: dabo.lib.datanav.Page.EditPage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2923:

.. function:: dabo.lib.datanav.Page.EditPage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2924:

.. function:: dabo.lib.datanav.Page.EditPage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-2925:

.. function:: dabo.lib.datanav.Page.EditPage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2926:

.. function:: dabo.lib.datanav.Page.EditPage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2927:

.. function:: dabo.lib.datanav.Page.EditPage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2928:

.. function:: dabo.lib.datanav.Page.EditPage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2929:

.. function:: dabo.lib.datanav.Page.EditPage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2930:

.. function:: dabo.lib.datanav.Page.EditPage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2931:

.. function:: dabo.lib.datanav.Page.EditPage.scrollHorizontally(self, amt)
   :noindex:


   Change the horizontal scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2932:

.. function:: dabo.lib.datanav.Page.EditPage.scrollVertically(self, amt)
   :noindex:


   Change the vertical scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-2933:

.. function:: dabo.lib.datanav.Page.EditPage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2934:

.. function:: dabo.lib.datanav.Page.EditPage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-2935:

.. function:: dabo.lib.datanav.Page.EditPage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2936:

.. function:: dabo.lib.datanav.Page.EditPage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2937:

.. function:: dabo.lib.datanav.Page.EditPage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-2938:

.. function:: dabo.lib.datanav.Page.EditPage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-2939:

.. function:: dabo.lib.datanav.Page.EditPage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2940:

.. function:: dabo.lib.datanav.Page.EditPage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2941:

.. function:: dabo.lib.datanav.Page.EditPage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2942:

.. function:: dabo.lib.datanav.Page.EditPage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2943:

.. function:: dabo.lib.datanav.Page.EditPage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2944:

.. function:: dabo.lib.datanav.Page.EditPage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-2945:

.. function:: dabo.lib.datanav.Page.EditPage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-2946:

.. function:: dabo.lib.datanav.Page.EditPage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2947:

.. function:: dabo.lib.datanav.Page.EditPage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2948:

.. function:: dabo.lib.datanav.Page.EditPage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-2949:

.. function:: dabo.lib.datanav.Page.EditPage.update(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------


|
