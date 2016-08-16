
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.WizardPage

.. _dabo.ui.dialogs.WizardPage.WizardPage:

==============================================
|doc_title|  **WizardPage.WizardPage** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **WizardPage**

.. inheritance-diagram:: WizardPage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`



|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.WizardPage.WizardPage

   .. automethod:: dabo.ui.dialogs.WizardPage.WizardPage.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-6778>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-6779>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-6780>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-6781>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-6782>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-6783>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-6784>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-6785>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-6786>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-6787>`                 The text that appears as the title of the page  (str)
:ref:`Children <no-6788>`                Child controls of this panel. This excludes the wx-specific
:ref:`Class <no-6789>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-6790>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-6791>`    Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-6792>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-6793>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-6794>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-6795>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-6796>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-6797>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-6798>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-6799>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-6800>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-6801>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-6802>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-6803>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-6804>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-6805>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-6806>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-6807>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-6808>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-6809>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicLeft <no-6810>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-6811>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-6812>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-6813>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-6814>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-6815>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-6816>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-6817>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-6818>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-6819>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-6820>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-6821>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-6822>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-6823>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-6824>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-6825>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-6826>`                Specifies the font face. (str)
:ref:`FontInfo <no-6827>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-6828>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-6829>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-6830>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-6831>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-6832>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-6833>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-6834>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-6835>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-6836>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-6837>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-6838>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-6839>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-6840>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-6841>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-6842>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-6843>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-6844>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-6845>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-6846>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-6847>`                Specifies the base name of the object.
:ref:`Parent <no-6848>`                  The containing object. (obj)
:ref:`Picture <no-6849>`                 Normally None, but you can set it to some other image to have the wizard display
:ref:`Position <no-6850>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-6851>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-6852>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-6853>`                   The position of the right side of the object. This is a
:ref:`Size <no-6854>`                    The size of the object. (tuple)
:ref:`Sizer <no-6855>`                   The sizer for the object.
:ref:`StatusText <no-6856>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-6857>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-6858>`                     A property that user code can safely use for specific purposes.
:ref:`TitleBold <no-6859>`               Controls whether the title text is bold.  (bool)
:ref:`TitleFace <no-6860>`               Name of the font face used for the Title.  (string)
:ref:`TitleItalic <no-6861>`             Controls whether the title text is italic.  (bool)
:ref:`TitleSize <no-6862>`               Size in points for the Title (default=18).  (int)
:ref:`ToolTipText <no-6863>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-6864>`                     The top position of the object. (int)
:ref:`Transparency <no-6865>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-6866>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`VerticalScroll <no-6867>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-6868>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-6869>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-6870>`                   The width of the object. (int)
:ref:`WindowHandle <no-6871>`            The platform-specific handle for the window. Read-only. (long)
:ref:`Wizard <no-6872>`                  Reference to the wizard form this page is in  (Wizard object)

======================================== ========================


Properties
==========

.. _no-6849:

**Picture** 

Normally None, but you can set it to some other image to have the wizard display
    a different picture for this page  (None or image path)



-------

.. _no-6859:

**TitleBold** 

Controls whether the title text is bold.  (bool)



-------

.. _no-6860:

**TitleFace** 

Name of the font face used for the Title.  (string)



-------

.. _no-6861:

**TitleItalic** 

Controls whether the title text is italic.  (bool)



-------

.. _no-6862:

**TitleSize** 

Size in points for the Title (default=18).  (int)



-------

.. _no-6872:

**Wizard** 

Reference to the wizard form this page is in  (Wizard object)



-------


Properties - inherited
========================

.. _no-6778:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6779:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6780:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6781:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6782:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6783:

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

.. _no-6784:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6785:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6786:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6787:

**Caption** 

The text that appears as the title of the page  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6788:

**Children** 

Child controls of this panel. This excludes the wx-specific
    scroll bars  (list of objects)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6789:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6790:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6791:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6792:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6793:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6794:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6795:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6796:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6797:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6798:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6799:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6800:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6801:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6802:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6803:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6804:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6805:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6806:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6807:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6808:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6809:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6810:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6811:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6812:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6813:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6814:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6815:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6816:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6817:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6818:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6819:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6820:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6821:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6822:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6823:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6824:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6825:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6826:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6827:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6828:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6829:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6830:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6831:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6832:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6833:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6834:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6835:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6836:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6837:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6838:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6839:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6840:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6841:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6842:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6843:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6844:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6845:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6846:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6847:

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

.. _no-6848:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6850:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6851:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6852:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6853:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6854:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6855:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-6856:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6857:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-6858:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6863:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6864:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6865:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6866:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6867:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6868:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6869:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6870:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6871:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-6873>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-6874>`                 Occurs after the control or form is created.
:ref:`Destroy <no-6875>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-6876>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-6877>`               Occurs when the control gets the focus.
:ref:`Idle <no-6878>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-6879>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-6880>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-6881>`               
:ref:`KeyUp <no-6882>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-6883>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-6884>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-6885>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-6886>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-6887>`             
:ref:`MouseLeave <no-6888>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-6889>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-6890>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-6891>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-6892>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-6893>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-6894>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-6895>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-6896>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-6897>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-6898>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-6899>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-6900>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-6901>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-6902>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-6903>`                   Occurs when the control's position changes.
:ref:`Paint <no-6904>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-6905>`                 Occurs when the control or form is resized.
:ref:`ScrollBottom <no-6906>`           Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-6907>`            
:ref:`ScrollLineDown <no-6908>`         Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-6909>`           Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-6910>`         Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-6911>`           Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-6912>`        Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-6913>`     Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-6914>`              Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-6915>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-6916>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-6917>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-6873:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-6874:

**Create** 

Occurs after the control or form is created.



-------

.. _no-6875:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-6876:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-6877:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-6878:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-6879:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-6880:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-6881:

**KeyEvent** 



-------

.. _no-6882:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-6883:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-6884:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-6885:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-6886:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-6887:

**MouseEvent** 



-------

.. _no-6888:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-6889:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-6890:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-6891:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-6892:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-6893:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-6894:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-6895:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-6896:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-6897:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-6898:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-6899:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-6900:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-6901:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-6902:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-6903:

**Move** 

Occurs when the control's position changes.



-------

.. _no-6904:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-6905:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-6906:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-6907:

**ScrollEvent** 



-------

.. _no-6908:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-6909:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-6910:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-6911:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-6912:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-6913:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-6914:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-6915:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-6916:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-6917:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-6918>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-6919>`             Instantiate object as a child of self.
:ref:`afterInit <no-6920>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-6921>`          
:ref:`afterSetProperties <no-6922>`    
:ref:`autoBindEvents <no-6923>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-6924>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-6925>`   
:ref:`bindEvent <no-6926>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-6927>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-6928>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-6929>`          Makes this object topmost
:ref:`clear <no-6930>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-6931>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-6932>`  Given a position relative to this control, return a position relative
:ref:`copy <no-6933>`                  Called by uiApp when the user requests a copy operation.
:ref:`createBody <no-6934>`            This is the method to override in subclasses to add any text
:ref:`cut <no-6935>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-6936>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-6937>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-6938>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-6939>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-6940>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-6941>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-6942>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-6943>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-6944>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-6945>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-6946>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-6947>`              Draws text on the object at the specified position
:ref:`endHover <no-6948>`              
:ref:`fitToSizer <no-6949>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-6950>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-6951>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-6952>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-6953>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-6954>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-6955>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-6956>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-6957>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-6958>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-6959>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-6960>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-6961>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-6962>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-6963>`                  Make the object invisible.
:ref:`initEvents <no-6964>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-6965>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-6966>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-6967>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-6968>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-6969>`           Locks the visual updates to the control.
:ref:`makeSizer <no-6970>`             Create a simple sizer. This can be overridden in subclasses
:ref:`moveTabOrderAfter <no-6971>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-6972>`    Moves this object's tab order before the passed obj.
:ref:`nextPage <no-6973>`              This method can be overridden in subclasses to provide
:ref:`objectCoordinates <no-6974>`     Given a position relative to the form, return a position relative
:ref:`onEnterPage <no-6975>`           This method will be called just as the page is about to
:ref:`onHover <no-6976>`               
:ref:`onLeavePage <no-6977>`           This method is called before the wizard changes pages.
:ref:`pageDown <no-6978>`              
:ref:`pageHorizontally <no-6979>`      Scroll horizontally one 'page' width.
:ref:`pageLeft <no-6980>`              
:ref:`pageRight <no-6981>`             
:ref:`pageUp <no-6982>`                
:ref:`pageVertically <no-6983>`        Scroll vertically one 'page' height.
:ref:`paste <no-6984>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-6985>`           
:ref:`prevPage <no-6986>`              Like nextPage, you can override this method to conditionally
:ref:`processDroppedFiles <no-6987>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-6988>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-6989>`            Raise the passed Dabo event.
:ref:`reCreate <no-6990>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-6991>`              Recreate the object.
:ref:`redraw <no-6992>`                Called when the object is (re)drawn.
:ref:`refresh <no-6993>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-6994>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-6995>`               Destroys the object.
:ref:`removeDrawnObject <no-6996>`     
:ref:`scrollHorizontally <no-6997>`    Change the horizontal scroll position by 'amt' units.
:ref:`scrollVertically <no-6998>`      Change the vertical scroll position by 'amt' units.
:ref:`sendToBack <no-6999>`            Places this object behind all others.
:ref:`setAll <no-7000>`                Set all child object properties to the passed value.
:ref:`setFocus <no-7001>`              Sets focus to the object.
:ref:`setPositionInSizer <no-7002>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-7003>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-7004>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-7005>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-7006>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`setup <no-7007>`                 
:ref:`show <no-7008>`                  Make the object visible.
:ref:`showContainingPage <no-7009>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-7010>`       Display a context menu (popup) at the specified position.
:ref:`super <no-7011>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-7012>`           Remove a previously registered event binding.
:ref:`unbindKey <no-7013>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-7014>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-7015>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-7016>`                Update the properties of this object and all contained objects.

====================================== ========================


Methods
=======

.. _no-6934:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.createBody(self)

   
   This is the method to override in subclasses to add any text
   or other controls for this page.
   



-------

.. _no-6970:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.makeSizer(self)

   
   Create a simple sizer. This can be overridden in subclasses
   if specific sizer configurations are needed.
   



-------

.. _no-6973:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.nextPage(self)

   
   This method can be overridden in subclasses to provide
   conditional navigation through the wizard. By default, it returns
   the integer 1, meaning move one page forward in the wizards page
   collection. If you wish to skip the next page in order, you can simply
   return 2, and the wizard will jump forward to the second page in
   its page collection after the current one.
   



-------

.. _no-6975:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.onEnterPage(self, direction)

   
   This method will be called just as the page is about to
   be made visible. You cannot prevent this from happening,
   as you can with onLeavePage(), but you can use this event
   to do whatever preliminary work that page needs before it
   is displayed. The 'direction' parameter is the same as for
   onLeavePage().
   



-------

.. _no-6977:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.onLeavePage(self, direction)

   
   This method is called before the wizard changes pages.
   Returning False will prevent the page from changing. Use
   it to make sure that the user has completed all the required
   actions before proceeding to the next step of the wizard.
   The direction passed to this method will either be 'forward'
   or 'back'.
   



-------

.. _no-6986:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.prevPage(self)

   
   Like nextPage, you can override this method to conditionally
   navigate through the wizard pages. Default = -1
   



-------

.. _no-7007:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setup(self)



-------


Methods - inherited
=====================

.. _no-6918:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6919:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-6920:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6921:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6922:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6923:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.autoBindEvents(self, force=True)
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

.. _no-6924:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6925:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6926:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6927:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6928:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-6929:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6930:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6931:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6932:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6933:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6935:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6936:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6937:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6938:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-6939:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6940:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6941:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6942:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6943:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6944:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6945:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6946:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6947:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6948:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6949:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6950:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6951:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6952:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6953:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6954:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6955:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6956:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6957:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6958:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6959:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6960:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-6961:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6962:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6963:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6964:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6965:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6966:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6967:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6968:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-6969:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.lockDisplay(self)
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

.. _no-6971:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6972:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6974:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6976:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6978:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.pageDown(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6979:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.pageHorizontally(self, direction)
   :noindex:


   Scroll horizontally one 'page' width.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6980:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.pageLeft(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6981:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.pageRight(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6982:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.pageUp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6983:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.pageVertically(self, direction)
   :noindex:


   Scroll vertically one 'page' height.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6984:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6985:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6987:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6988:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6989:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6990:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6991:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6992:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6993:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6994:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6995:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6996:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6997:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.scrollHorizontally(self, amt)
   :noindex:


   Change the horizontal scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6998:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.scrollVertically(self, amt)
   :noindex:


   Change the vertical scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-6999:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7000:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-7001:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7002:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7003:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-7004:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-7005:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7006:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7008:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7009:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7010:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7011:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7012:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-7013:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7014:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7015:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7016:

.. function:: dabo.ui.dialogs.WizardPage.WizardPage.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
