
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dControlMixin

.. _dabo.ui.uiwx.dControlMixin.dControlMixin:

====================================================
|doc_title|  **dControlMixin.dControlMixin** - class
====================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dControlMixin**

.. inheritance-diagram:: dControlMixin


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.dControlMixinBase.dControlMixinBase`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`
* :ref:`dabo.ui.uiwx.dAutoComplete.dAutoComplete`
* :ref:`dabo.ui.uiwx.dBitmap.dBitmap`
* :ref:`dabo.ui.uiwx.dBitmapButton.dBitmapButton`
* :ref:`dabo.ui.uiwx.dBorderlessButton.dBorderlessButton`
* :ref:`dabo.ui.uiwx.dBox.dBox`
* :ref:`dabo.ui.uiwx.dButton.dButton`
* :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`
* :ref:`dabo.ui.uiwx.dCollapsiblePanel.dCollapsiblePanel`
* :ref:`dabo.ui.uiwx.dEditableList.dEditableList`
* :ref:`dabo.ui.uiwx.dGauge.dGauge`
* :ref:`dabo.ui.uiwx.dGlWindow.dGlWindow`
* :ref:`dabo.ui.uiwx.dGrid.dGrid`
* :ref:`dabo.ui.uiwx.dHtmlBox.dHtmlBox`
* :ref:`dabo.ui.uiwx.dHyperLink.dHyperLink`
* :ref:`dabo.ui.uiwx.dLabel.dLabel`
* :ref:`dabo.ui.uiwx.dLine.dLine`
* :ref:`dabo.ui.uiwx.dMediaControl.dMediaControl`
* :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`
* :ref:`dabo.ui.uiwx.dPdfWindow.dPdfWindow`
* :ref:`dabo.ui.uiwx.dShell.dShell`
* :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`
* :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl`
* :ref:`dabo.ui.uiwx.dSplitter.dSplitter`
* :ref:`dabo.ui.uiwx.dStatusBar.dStatusBar`
* :ref:`dabo.ui.uiwx.dToolBar.dToolBar`
* :ref:`dabo.ui.uiwx.dTreeView.dTreeView`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dControlMixin.dControlMixin


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-35010>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-35011>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-35012>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-35013>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-35014>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-35015>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-35016>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-35017>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-35018>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-35019>`                The caption of the object. (str)
:ref:`Children <no-35020>`               Returns a list of object references to the children of
:ref:`Class <no-35021>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-35022>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-35023>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-35024>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-35025>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-35026>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-35027>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-35028>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-35029>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-35030>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-35031>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-35032>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-35033>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-35034>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-35035>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-35036>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-35037>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-35038>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-35039>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-35040>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-35041>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-35042>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-35043>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-35044>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-35045>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-35046>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-35047>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-35048>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-35049>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-35050>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-35051>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-35052>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-35053>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-35054>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-35055>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-35056>`               Specifies the font face. (str)
:ref:`FontInfo <no-35057>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-35058>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-35059>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-35060>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-35061>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-35062>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-35063>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-35064>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-35065>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-35066>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-35067>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-35068>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-35069>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-35070>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-35071>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-35072>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-35073>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-35074>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-35075>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-35076>`               Specifies the base name of the object.
:ref:`Parent <no-35077>`                 The containing object. (obj)
:ref:`Position <no-35078>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-35079>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-35080>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-35081>`                  The position of the right side of the object. This is a
:ref:`Size <no-35082>`                   The size of the object. (tuple)
:ref:`Sizer <no-35083>`                  The sizer for the object.
:ref:`StatusText <no-35084>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-35085>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-35086>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-35087>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-35088>`                    The top position of the object. (int)
:ref:`Transparency <no-35089>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-35090>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-35091>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-35092>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-35093>`                  The width of the object. (int)
:ref:`WindowHandle <no-35094>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-35085:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.



-------


Properties - inherited
========================

.. _no-35010:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35011:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35012:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35013:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35014:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35015:

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

.. _no-35016:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35017:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35018:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35019:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35020:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35021:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35022:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35023:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35024:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35025:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35026:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35027:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35028:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35029:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35030:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35031:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35032:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35033:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35034:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35035:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35036:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35037:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35038:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35039:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35040:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35041:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35042:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35043:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35044:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35045:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35046:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35047:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35048:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35049:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35050:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35051:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35052:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35053:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35054:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35055:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35056:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35057:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35058:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35059:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35060:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35061:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35062:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35063:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35064:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35065:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35066:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35067:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35068:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35069:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35070:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35071:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35072:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35073:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35074:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35075:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35076:

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

.. _no-35077:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35078:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35079:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35080:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35081:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35082:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35083:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35084:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35086:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35087:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35088:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35089:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35090:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35091:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35092:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35093:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35094:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-35095>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-35096>`                 Occurs after the control or form is created.
:ref:`Destroy <no-35097>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-35098>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-35099>`               Occurs when the control gets the focus.
:ref:`Idle <no-35100>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-35101>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-35102>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-35103>`               
:ref:`KeyUp <no-35104>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-35105>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-35106>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-35107>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-35108>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-35109>`             
:ref:`MouseLeave <no-35110>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-35111>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-35112>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-35113>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-35114>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-35115>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-35116>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-35117>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-35118>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-35119>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-35120>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-35121>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-35122>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-35123>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-35124>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-35125>`                   Occurs when the control's position changes.
:ref:`Paint <no-35126>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-35127>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-35128>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-35129>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-35130>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-35095:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-35096:

**Create** 

Occurs after the control or form is created.



-------

.. _no-35097:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-35098:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-35099:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-35100:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-35101:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-35102:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-35103:

**KeyEvent** 



-------

.. _no-35104:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-35105:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-35106:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-35107:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-35108:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-35109:

**MouseEvent** 



-------

.. _no-35110:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-35111:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-35112:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-35113:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-35114:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-35115:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-35116:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-35117:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-35118:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-35119:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-35120:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-35121:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-35122:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-35123:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-35124:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-35125:

**Move** 

Occurs when the control's position changes.



-------

.. _no-35126:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-35127:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-35128:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-35129:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-35130:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-35131>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-35132>`             Instantiate object as a child of self.
:ref:`afterInit <no-35133>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-35134>`          
:ref:`afterSetProperties <no-35135>`    
:ref:`autoBindEvents <no-35136>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-35137>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-35138>`   
:ref:`bindEvent <no-35139>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-35140>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-35141>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-35142>`          Makes this object topmost
:ref:`clear <no-35143>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-35144>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-35145>`  Given a position relative to this control, return a position relative
:ref:`copy <no-35146>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-35147>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-35148>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-35149>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-35150>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-35151>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-35152>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-35153>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-35154>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-35155>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-35156>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-35157>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-35158>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-35159>`              Draws text on the object at the specified position
:ref:`endHover <no-35160>`              
:ref:`fitToSizer <no-35161>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-35162>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-35163>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-35164>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-35165>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-35166>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-35167>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-35168>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-35169>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-35170>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-35171>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-35172>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-35173>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-35174>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-35175>`                  Make the object invisible.
:ref:`initEvents <no-35176>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-35177>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-35178>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-35179>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-35180>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-35181>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-35182>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-35183>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-35184>`               
:ref:`paste <no-35185>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-35186>`           
:ref:`processDroppedFiles <no-35187>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-35188>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-35189>`            Raise the passed Dabo event.
:ref:`reCreate <no-35190>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-35191>`              Recreate the object.
:ref:`redraw <no-35192>`                Called when the object is (re)drawn.
:ref:`refresh <no-35193>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-35194>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-35195>`               Destroys the object.
:ref:`removeDrawnObject <no-35196>`     
:ref:`sendToBack <no-35197>`            Places this object behind all others.
:ref:`setAll <no-35198>`                Set all child object properties to the passed value.
:ref:`setFocus <no-35199>`              Sets focus to the object.
:ref:`setPositionInSizer <no-35200>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-35201>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-35202>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-35203>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-35204>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-35205>`                  Make the object visible.
:ref:`showContainingPage <no-35206>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-35207>`       Display a context menu (popup) at the specified position.
:ref:`super <no-35208>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-35209>`           Remove a previously registered event binding.
:ref:`unbindKey <no-35210>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-35211>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-35212>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-35213>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-35131:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35132:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-35133:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35134:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35135:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35136:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.autoBindEvents(self, force=True)
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

.. _no-35137:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35138:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35139:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35140:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35141:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-35142:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35143:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35144:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35145:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35146:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35147:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35148:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35149:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35150:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-35151:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35152:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35153:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35154:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35155:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35156:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35157:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35158:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35159:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35160:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35161:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35162:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35163:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35164:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35165:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35166:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35167:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35168:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35169:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35170:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35171:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35172:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-35173:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35174:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35175:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35176:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35177:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35178:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35179:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35180:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.lockDisplay(self)
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

.. _no-35181:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35182:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35183:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35184:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35185:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35186:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35187:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35188:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35189:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35190:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35191:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35192:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35193:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35194:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35195:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35196:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35197:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35198:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-35199:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35200:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35201:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-35202:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-35203:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35204:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35205:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35206:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35207:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35208:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35209:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35210:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35211:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35212:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35213:

.. function:: dabo.ui.uiwx.dControlMixin.dControlMixin.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
