
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrameNoTabs

.. _dabo.ui.uiwx.dPageFrameNoTabs.TestPage:

==================================================
|doc_title|  **dPageFrameNoTabs.TestPage** - class
==================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **TestPage**

.. inheritance-diagram:: TestPage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPage.dPage`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage


|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-20703>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-20704>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-20705>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-20706>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-20707>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-20708>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-20709>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-20710>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-20711>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-20712>`                 The text identifying this particular page.  (str)
:ref:`Children <no-20713>`                Child controls of this panel. This excludes the wx-specific
:ref:`Class <no-20714>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-20715>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-20716>`    Reference to the sizer item that control's this control's layout.
:ref:`DeferredUpdates <no-20717>`         Allow to defer controls updates until page become active.  (bool)
:ref:`DroppedFileHandler <no-20718>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-20719>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-20720>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-20721>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-20722>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-20723>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-20724>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-20725>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-20726>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-20727>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-20728>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-20729>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-20730>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-20731>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-20732>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-20733>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-20734>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-20735>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicImage <no-20736>`            Dynamically determine the value of the Image property.
:ref:`DynamicLeft <no-20737>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-20738>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-20739>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-20740>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-20741>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-20742>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-20743>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-20744>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-20745>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-20746>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-20747>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-20748>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-20749>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-20750>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-20751>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-20752>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-20753>`                Specifies the font face. (str)
:ref:`FontInfo <no-20754>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-20755>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-20756>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-20757>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-20758>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-20759>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-20760>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-20761>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-20762>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-20763>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Image <no-20764>`                   Sets the image that is displayed on the page tab. This is
:ref:`Left <no-20765>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-20766>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-20767>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-20768>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-20769>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-20770>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-20771>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-20772>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-20773>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-20774>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-20775>`                Specifies the base name of the object.
:ref:`Parent <no-20776>`                  The containing object. (obj)
:ref:`Position <no-20777>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-20778>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-20779>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-20780>`                   The position of the right side of the object. This is a
:ref:`Size <no-20781>`                    The size of the object. (tuple)
:ref:`Sizer <no-20782>`                   The sizer for the object.
:ref:`StatusText <no-20783>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-20784>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-20785>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-20786>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-20787>`                     The top position of the object. (int)
:ref:`Transparency <no-20788>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-20789>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`VerticalScroll <no-20790>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-20791>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-20792>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-20793>`                   The width of the object. (int)
:ref:`WindowHandle <no-20794>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties - inherited
========================

.. _no-20703:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20704:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20705:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20706:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20707:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20708:

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

.. _no-20709:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20710:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20711:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20712:

**Caption** 

The text identifying this particular page.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20713:

**Children** 

Child controls of this panel. This excludes the wx-specific
    scroll bars  (list of objects)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20714:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20715:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20716:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20717:

**DeferredUpdates** 

Allow to defer controls updates until page become active.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-20718:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20719:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20720:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20721:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20722:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20723:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20724:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20725:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20726:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20727:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20728:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20729:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20730:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20731:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20732:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20733:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20734:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20735:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20736:

**DynamicImage** 

Dynamically determine the value of the Image property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Image property. If DynamicImage is set to None (the default), Image
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-20737:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20738:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20739:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20740:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20741:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20742:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20743:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20744:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20745:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20746:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20747:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20748:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20749:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20750:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20751:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20752:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20753:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20754:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20755:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20756:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20757:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20758:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20759:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20760:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20761:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20762:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20763:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20764:

**Image** 

Sets the image that is displayed on the page tab. This is
    determined by the key value passed, which must refer to an
    image already added to the parent pageframe.
    When used to retrieve an image, it returns the index of the
    page's image in the parent pageframe's image list.   (int)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-20765:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20766:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20767:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20768:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20769:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20770:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20771:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20772:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20773:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20774:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20775:

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

.. _no-20776:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20777:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20778:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20779:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20780:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20781:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20782:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20783:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20784:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-20785:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20786:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20787:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20788:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20789:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20790:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20791:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20792:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20793:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20794:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-20795>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-20796>`              Occurs when a child control is created.
:ref:`ControlNavigationEvent <no-20797>` 
:ref:`Create <no-20798>`                 Occurs after the control or form is created.
:ref:`Destroy <no-20799>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-20800>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-20801>`               Occurs when the control gets the focus.
:ref:`Idle <no-20802>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-20803>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-20804>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-20805>`               
:ref:`KeyUp <no-20806>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-20807>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-20808>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-20809>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-20810>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-20811>`             
:ref:`MouseLeave <no-20812>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-20813>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-20814>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-20815>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-20816>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-20817>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-20818>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-20819>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-20820>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-20821>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-20822>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-20823>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-20824>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-20825>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-20826>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-20827>`                   Occurs when the control's position changes.
:ref:`PageContextMenu <no-20828>`        Occurs when the user requests a context event for a dPage
:ref:`PageEnter <no-20829>`              Occurs when the page becomes the active page.
:ref:`PageLeave <no-20830>`              Occurs when a different page becomes active.
:ref:`Paint <no-20831>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-20832>`                 Occurs when the control or form is resized.
:ref:`ScrollBottom <no-20833>`           Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-20834>`            
:ref:`ScrollLineDown <no-20835>`         Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-20836>`           Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-20837>`         Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-20838>`           Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-20839>`        Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-20840>`     Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-20841>`              Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-20842>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-20843>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-20844>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-20795:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-20796:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-20797:

**ControlNavigationEvent** 



-------

.. _no-20798:

**Create** 

Occurs after the control or form is created.



-------

.. _no-20799:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-20800:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-20801:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-20802:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-20803:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-20804:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-20805:

**KeyEvent** 



-------

.. _no-20806:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-20807:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-20808:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-20809:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-20810:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-20811:

**MouseEvent** 



-------

.. _no-20812:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-20813:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-20814:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-20815:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-20816:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-20817:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-20818:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-20819:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-20820:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-20821:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-20822:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-20823:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-20824:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-20825:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-20826:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-20827:

**Move** 

Occurs when the control's position changes.



-------

.. _no-20828:

**PageContextMenu** 

Occurs when the user requests a context event for a dPage



-------

.. _no-20829:

**PageEnter** 

Occurs when the page becomes the active page.



-------

.. _no-20830:

**PageLeave** 

Occurs when a different page becomes active.



-------

.. _no-20831:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-20832:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-20833:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-20834:

**ScrollEvent** 



-------

.. _no-20835:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-20836:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-20837:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-20838:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-20839:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-20840:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-20841:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-20842:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-20843:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-20844:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-20845>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-20846>`             Instantiate object as a child of self.
:ref:`afterInit <no-20847>`             
:ref:`afterInitAll <no-20848>`          
:ref:`afterSetProperties <no-20849>`    
:ref:`autoBindEvents <no-20850>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-20851>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-20852>`   
:ref:`bindEvent <no-20853>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-20854>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-20855>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-20856>`          Makes this object topmost
:ref:`clear <no-20857>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-20858>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-20859>`  Given a position relative to this control, return a position relative
:ref:`copy <no-20860>`                  Called by uiApp when the user requests a copy operation.
:ref:`createItems <no-20861>`           Create the controls in the page.
:ref:`cut <no-20862>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-20863>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-20864>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-20865>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-20866>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-20867>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-20868>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-20869>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-20870>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-20871>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-20872>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-20873>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-20874>`              Draws text on the object at the specified position
:ref:`endHover <no-20875>`              
:ref:`fitToSizer <no-20876>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-20877>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-20878>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-20879>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-20880>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-20881>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-20882>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-20883>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-20884>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-20885>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-20886>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-20887>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-20888>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-20889>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-20890>`                  Make the object invisible.
:ref:`initEvents <no-20891>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-20892>`        Hook for subclasses. User subclasses should set properties
:ref:`initSizer <no-20893>`             Set up the default vertical box sizer for the page.
:ref:`isContainedBy <no-20894>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-20895>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-20896>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-20897>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-20898>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-20899>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-20900>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-20901>`               
:ref:`pageDown <no-20902>`              
:ref:`pageHorizontally <no-20903>`      Scroll horizontally one 'page' width.
:ref:`pageLeft <no-20904>`              
:ref:`pageRight <no-20905>`             
:ref:`pageUp <no-20906>`                
:ref:`pageVertically <no-20907>`        Scroll vertically one 'page' height.
:ref:`paste <no-20908>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-20909>`           
:ref:`processDroppedFiles <no-20910>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-20911>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-20912>`            Raise the passed Dabo event.
:ref:`reCreate <no-20913>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-20914>`              Recreate the object.
:ref:`redraw <no-20915>`                Called when the object is (re)drawn.
:ref:`refresh <no-20916>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-20917>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-20918>`               Destroys the object.
:ref:`removeDrawnObject <no-20919>`     
:ref:`scrollHorizontally <no-20920>`    Change the horizontal scroll position by 'amt' units.
:ref:`scrollVertically <no-20921>`      Change the vertical scroll position by 'amt' units.
:ref:`sendToBack <no-20922>`            Places this object behind all others.
:ref:`setAll <no-20923>`                Set all child object properties to the passed value.
:ref:`setFocus <no-20924>`              Sets focus to the object.
:ref:`setLabel <no-20925>`              
:ref:`setPositionInSizer <no-20926>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-20927>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-20928>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-20929>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-20930>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-20931>`                  Make the object visible.
:ref:`showContainingPage <no-20932>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-20933>`       Display a context menu (popup) at the specified position.
:ref:`super <no-20934>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-20935>`           Remove a previously registered event binding.
:ref:`unbindKey <no-20936>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-20937>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-20938>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-20939>`                

======================================= ========================


Methods
=======

.. _no-20847:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.afterInit(self)



-------

.. _no-20925:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setLabel(self, txt)



-------


Methods - inherited
=====================

.. _no-20845:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20846:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-20848:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20849:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20850:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.autoBindEvents(self, force=True)
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

.. _no-20851:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20852:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20853:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20854:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20855:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-20856:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20857:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20858:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20859:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20860:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20861:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.createItems(self)
   :noindex:


   
   Create the controls in the page.
   
   Called when the page is entered for the first time, allowing subclasses
   to delay-populate the page.
   


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-20862:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20863:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20864:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20865:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-20866:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20867:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20868:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20869:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20870:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20871:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20872:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20873:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20874:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20875:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20876:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20877:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20878:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20879:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20880:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20881:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20882:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20883:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20884:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20885:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20886:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20887:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-20888:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20889:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20890:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20891:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20892:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20893:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.initSizer(self)
   :noindex:


   Set up the default vertical box sizer for the page.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-20894:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20895:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20896:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-20897:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.lockDisplay(self)
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

.. _no-20898:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20899:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20900:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20901:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20902:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.pageDown(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20903:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.pageHorizontally(self, direction)
   :noindex:


   Scroll horizontally one 'page' width.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20904:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.pageLeft(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20905:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.pageRight(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20906:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.pageUp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20907:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.pageVertically(self, direction)
   :noindex:


   Scroll vertically one 'page' height.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20908:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20909:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20910:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20911:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20912:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20913:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20914:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20915:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20916:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20917:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20918:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20919:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20920:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.scrollHorizontally(self, amt)
   :noindex:


   Change the horizontal scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20921:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.scrollVertically(self, amt)
   :noindex:


   Change the vertical scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-20922:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20923:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-20924:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20926:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20927:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-20928:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-20929:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20930:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20931:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20932:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20933:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20934:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20935:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20936:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20937:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20938:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20939:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.TestPage.update(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------


|
