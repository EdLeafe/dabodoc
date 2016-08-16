
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.__init__

.. _dabo.ui.uiwx.__init__.dFoldPanel:

.. _dabo.ui.uiwx.dFoldPanel:

============================================
|doc_title|  **__init__.dFoldPanel** - class
============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dFoldPanel**

.. inheritance-diagram:: dFoldPanel


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.__init__.dFoldPanel

   .. automethod:: dabo.ui.uiwx.__init__.dFoldPanel.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-20253>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-20254>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BarColor1 <no-20255>`               Main color for the caption bar  (dColor)
:ref:`BarColor2 <no-20256>`               Secondary color for the caption bar. Only used in gradients  (dColor)
:ref:`BarStyle <no-20257>`                "Determines how the bar containing the caption
:ref:`BaseClass <no-20258>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-20259>`             Base key used when saving/restoring preferences  (str)
:ref:`Border <no-20260>`                  Border between the contents and edges of the panel. Default=5  (int)
:ref:`BorderColor <no-20261>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-20262>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-20263>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-20264>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-20265>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-20266>`                 Caption displayed on the panel bar  (str)
:ref:`CaptionForeColor <no-20267>`        Text color of the caption bar  (str or tuple)
:ref:`CaptionHeight <no-20268>`           Height of the caption bar. Read-only  (int)
:ref:`Children <no-20269>`                Returns a list of object references to the children of
:ref:`Class <no-20270>`                   The class the object is based on. Read-only.  (class)
:ref:`Collapsed <no-20271>`               Is the panel main area hidden?  (bool)
:ref:`ControllingSizer <no-20272>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-20273>`    Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-20274>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-20275>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-20276>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBarColor1 <no-20277>`        Dynamically determine the value of the BarColor1 property.
:ref:`DynamicBarColor2 <no-20278>`        Dynamically determine the value of the BarColor2 property.
:ref:`DynamicBarStyle <no-20279>`         Dynamically determine the value of the BarStyle property.
:ref:`DynamicBorderColor <no-20280>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-20281>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-20282>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-20283>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-20284>`          Dynamically determine the value of the Caption property.
:ref:`DynamicCaptionForeColor <no-20285>` Dynamically determine the value of the CaptionForeColor property.
:ref:`DynamicCollapsed <no-20286>`        Dynamically determine the value of the Collapsed property.
:ref:`DynamicEnabled <no-20287>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicExpanded <no-20288>`         Dynamically determine the value of the Expanded property.
:ref:`DynamicFont <no-20289>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-20290>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-20291>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-20292>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-20293>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-20294>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-20295>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-20296>`           Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-20297>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-20298>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-20299>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-20300>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-20301>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-20302>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-20303>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-20304>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-20305>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-20306>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-20307>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-20308>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Expanded <no-20309>`                Is the panel main area visible?  (bool)
:ref:`Font <no-20310>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-20311>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-20312>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-20313>`                Specifies the font face. (str)
:ref:`FontInfo <no-20314>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-20315>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-20316>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-20317>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-20318>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-20319>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-20320>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-20321>`         Specifies the context-sensitive help text associated with this
:ref:`Hover <no-20322>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-20323>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-20324>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-20325>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-20326>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-20327>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-20328>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-20329>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-20330>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-20331>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-20332>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-20333>`                Specifies the base name of the object.
:ref:`PanelPosition <no-20334>`           Position of this panel within the parent container  (int)
:ref:`Parent <no-20335>`                  Reference to the containing dSlidePanelControl.
:ref:`Position <no-20336>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-20337>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-20338>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-20339>`                   The position of the right side of the object. This is a
:ref:`Size <no-20340>`                    The size of the object. (tuple)
:ref:`Sizer <no-20341>`                   The sizer for the object.
:ref:`StatusText <no-20342>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-20343>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-20344>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-20345>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-20346>`                     The top position of the object. (int)
:ref:`Transparency <no-20347>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-20348>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-20349>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-20350>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-20351>`                   The width of the object. (int)
:ref:`WindowHandle <no-20352>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties - inherited
========================

.. _no-20253:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20254:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20255:

**BarColor1** 

Main color for the caption bar  (dColor)


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20256:

**BarColor2** 

Secondary color for the caption bar. Only used in gradients  (dColor)


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20257:

**BarStyle** 

"Determines how the bar containing the caption
    for this panel is drawn. (str)

    Can be one of the following:
        Borderless        (no border, just a plain fill color; default)
        BorderOnly    (simple border, no fill color)
        FilledBorder    (combination of the two above)
        VerticalFill        (vertical gradient fill, using the two caption colors)
        HorizontalFill    (horizontal gradient fill, using the two caption colors)
    


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20258:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20259:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20260:

**Border** 

Border between the contents and edges of the panel. Default=5  (int)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20261:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20262:

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

.. _no-20263:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20264:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20265:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20266:

**Caption** 

Caption displayed on the panel bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20267:

**CaptionForeColor** 

Text color of the caption bar  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20268:

**CaptionHeight** 

Height of the caption bar. Read-only  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20269:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20270:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20271:

**Collapsed** 

Is the panel main area hidden?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20272:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20273:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20274:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20275:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20276:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20277:

**DynamicBarColor1** 

Dynamically determine the value of the BarColor1 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BarColor1 property. If DynamicBarColor1 is set to None (the default), BarColor1
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20278:

**DynamicBarColor2** 

Dynamically determine the value of the BarColor2 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BarColor2 property. If DynamicBarColor2 is set to None (the default), BarColor2
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20279:

**DynamicBarStyle** 

Dynamically determine the value of the BarStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BarStyle property. If DynamicBarStyle is set to None (the default), BarStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20280:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20281:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20282:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20283:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20284:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20285:

**DynamicCaptionForeColor** 

Dynamically determine the value of the CaptionForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CaptionForeColor property. If DynamicCaptionForeColor is set to None (the default), CaptionForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20286:

**DynamicCollapsed** 

Dynamically determine the value of the Collapsed property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Collapsed property. If DynamicCollapsed is set to None (the default), Collapsed
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20287:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20288:

**DynamicExpanded** 

Dynamically determine the value of the Expanded property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Expanded property. If DynamicExpanded is set to None (the default), Expanded
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20289:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20290:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20291:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20292:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20293:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20294:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20295:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20296:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20297:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20298:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20299:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20300:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20301:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20302:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20303:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20304:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20305:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20306:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20307:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20308:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20309:

**Expanded** 

Is the panel main area visible?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20310:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20311:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20312:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20313:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20314:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20315:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20316:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20317:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20318:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20319:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20320:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20321:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20322:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20323:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20324:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20325:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20326:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20327:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20328:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20329:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20330:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20331:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20332:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20333:

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

.. _no-20334:

**PanelPosition** 

Position of this panel within the parent container  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20335:

**Parent** 

Reference to the containing dSlidePanelControl.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20336:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20337:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20338:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20339:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20340:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20341:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20342:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20343:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-20344:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20345:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20346:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20347:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20348:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20349:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20350:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20351:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20352:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-20353>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-20354>`                 Occurs after the control or form is created.
:ref:`Destroy <no-20355>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-20356>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-20357>`               Occurs when the control gets the focus.
:ref:`Idle <no-20358>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-20359>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-20360>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-20361>`               
:ref:`KeyUp <no-20362>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-20363>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-20364>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-20365>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-20366>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-20367>`             
:ref:`MouseLeave <no-20368>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-20369>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-20370>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-20371>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-20372>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-20373>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-20374>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-20375>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-20376>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-20377>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-20378>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-20379>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-20380>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-20381>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-20382>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-20383>`                   Occurs when the control's position changes.
:ref:`Paint <no-20384>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-20385>`                 Occurs when the control or form is resized.
:ref:`SlidePanelCaptionClick <no-20386>` Occurs when the caption bar of a dSlidePanel is clicked.
:ref:`SlidePanelChange <no-20387>`       Occurs when a panel in a dSlidePanelControl control is hidden or shown.
:ref:`TreeBeginDrag <no-20388>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-20389>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-20390>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-20353:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-20354:

**Create** 

Occurs after the control or form is created.



-------

.. _no-20355:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-20356:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-20357:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-20358:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-20359:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-20360:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-20361:

**KeyEvent** 



-------

.. _no-20362:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-20363:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-20364:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-20365:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-20366:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-20367:

**MouseEvent** 



-------

.. _no-20368:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-20369:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-20370:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-20371:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-20372:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-20373:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-20374:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-20375:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-20376:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-20377:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-20378:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-20379:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-20380:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-20381:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-20382:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-20383:

**Move** 

Occurs when the control's position changes.



-------

.. _no-20384:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-20385:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-20386:

**SlidePanelCaptionClick** 

Occurs when the caption bar of a dSlidePanel is clicked.



-------

.. _no-20387:

**SlidePanelChange** 

Occurs when a panel in a dSlidePanelControl control is hidden or shown.



-------

.. _no-20388:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-20389:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-20390:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-20391>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-20392>`             Instantiate object as a child of self.
:ref:`afterInit <no-20393>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-20394>`          
:ref:`afterSetProperties <no-20395>`    
:ref:`appendSeparator <no-20396>`       This draws a separator line on the panel
:ref:`autoBindEvents <no-20397>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-20398>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-20399>`   
:ref:`bindEvent <no-20400>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-20401>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-20402>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-20403>`          Makes this object topmost
:ref:`clear <no-20404>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-20405>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-20406>`  Given a position relative to this control, return a position relative
:ref:`copy <no-20407>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-20408>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-20409>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-20410>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-20411>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-20412>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-20413>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-20414>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-20415>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-20416>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-20417>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-20418>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-20419>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-20420>`              Draws text on the object at the specified position
:ref:`endHover <no-20421>`              
:ref:`fitToSizer <no-20422>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-20423>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-20424>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-20425>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-20426>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-20427>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-20428>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-20429>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-20430>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-20431>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-20432>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-20433>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-20434>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-20435>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-20436>`                  Make the object invisible.
:ref:`initEvents <no-20437>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-20438>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-20439>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-20440>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-20441>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-20442>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-20443>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-20444>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-20445>`     Given a position relative to the form, return a position relative
:ref:`onChildBorn <no-20446>`           
:ref:`onHover <no-20447>`               
:ref:`paste <no-20448>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-20449>`           
:ref:`processDroppedFiles <no-20450>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-20451>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-20452>`            Raise the passed Dabo event.
:ref:`reCreate <no-20453>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-20454>`              Recreate the object.
:ref:`redraw <no-20455>`                Called when the object is (re)drawn.
:ref:`refresh <no-20456>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-20457>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-20458>`               Destroys the object.
:ref:`removeDrawnObject <no-20459>`     
:ref:`sendToBack <no-20460>`            Places this object behind all others.
:ref:`setAll <no-20461>`                Set all child object properties to the passed value.
:ref:`setFocus <no-20462>`              Sets focus to the object.
:ref:`setPositionInSizer <no-20463>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-20464>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-20465>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-20466>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-20467>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-20468>`                  Make the object visible.
:ref:`showContainingPage <no-20469>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-20470>`       Display a context menu (popup) at the specified position.
:ref:`super <no-20471>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-20472>`           Remove a previously registered event binding.
:ref:`unbindKey <no-20473>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-20474>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-20475>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-20476>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-20391:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20392:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-20393:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20394:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20395:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20396:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.appendSeparator(self, color=None)
   :noindex:


   This draws a separator line on the panel


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20397:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.autoBindEvents(self, force=True)
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

.. _no-20398:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20399:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20400:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20401:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20402:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-20403:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20404:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20405:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20406:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20407:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20408:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20409:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20410:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20411:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-20412:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20413:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20414:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20415:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20416:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20417:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20418:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20419:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20420:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20421:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20422:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20423:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20424:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20425:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20426:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20427:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20428:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20429:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20430:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20431:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20432:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20433:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-20434:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20435:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20436:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20437:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20438:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20439:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20440:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20441:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.layout(self)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20442:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.lockDisplay(self)
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

.. _no-20443:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20444:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20445:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20446:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.onChildBorn(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSlidePanelControl.dSlidePanel`

-------

.. _no-20447:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20448:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20449:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20450:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20451:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20452:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20453:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20454:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20455:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20456:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20457:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20458:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20459:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20460:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20461:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-20462:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20463:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20464:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-20465:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-20466:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20467:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20468:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20469:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20470:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20471:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20472:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-20473:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20474:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20475:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20476:

.. function:: dabo.ui.uiwx.__init__.dFoldPanel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
