
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSlidePanelControl

.. _dabo.ui.uiwx.dSlidePanelControl.dSlidePanel:

=======================================================
|doc_title|  **dSlidePanelControl.dSlidePanel** - class
=======================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSlidePanel**

.. inheritance-diagram:: dSlidePanel


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.lib.agw.foldpanelbar.FoldPanelItem - can not provide a link



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dFoldPanel`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dSlidePanel.png
          :scale: 75 %
          :target: _static/winWidgets/dSlidePanel.png
          :alt: dSlidePanel



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel

   .. automethod:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-30337>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-30338>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BarColor1 <no-30339>`               Main color for the caption bar  (dColor)
:ref:`BarColor2 <no-30340>`               Secondary color for the caption bar. Only used in gradients  (dColor)
:ref:`BarStyle <no-30341>`                "Determines how the bar containing the caption
:ref:`BaseClass <no-30342>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-30343>`             Base key used when saving/restoring preferences  (str)
:ref:`Border <no-30344>`                  Border between the contents and edges of the panel. Default=5  (int)
:ref:`BorderColor <no-30345>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-30346>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-30347>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-30348>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-30349>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-30350>`                 Caption displayed on the panel bar  (str)
:ref:`CaptionForeColor <no-30351>`        Text color of the caption bar  (str or tuple)
:ref:`CaptionHeight <no-30352>`           Height of the caption bar. Read-only  (int)
:ref:`Children <no-30353>`                Returns a list of object references to the children of
:ref:`Class <no-30354>`                   The class the object is based on. Read-only.  (class)
:ref:`Collapsed <no-30355>`               Is the panel main area hidden?  (bool)
:ref:`ControllingSizer <no-30356>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-30357>`    Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-30358>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-30359>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-30360>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBarColor1 <no-30361>`        Dynamically determine the value of the BarColor1 property.
:ref:`DynamicBarColor2 <no-30362>`        Dynamically determine the value of the BarColor2 property.
:ref:`DynamicBarStyle <no-30363>`         Dynamically determine the value of the BarStyle property.
:ref:`DynamicBorderColor <no-30364>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-30365>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-30366>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-30367>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-30368>`          Dynamically determine the value of the Caption property.
:ref:`DynamicCaptionForeColor <no-30369>` Dynamically determine the value of the CaptionForeColor property.
:ref:`DynamicCollapsed <no-30370>`        Dynamically determine the value of the Collapsed property.
:ref:`DynamicEnabled <no-30371>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicExpanded <no-30372>`         Dynamically determine the value of the Expanded property.
:ref:`DynamicFont <no-30373>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-30374>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-30375>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-30376>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-30377>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-30378>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-30379>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-30380>`           Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-30381>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-30382>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-30383>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-30384>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-30385>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-30386>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-30387>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-30388>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-30389>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-30390>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-30391>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-30392>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Expanded <no-30393>`                Is the panel main area visible?  (bool)
:ref:`Font <no-30394>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-30395>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-30396>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-30397>`                Specifies the font face. (str)
:ref:`FontInfo <no-30398>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-30399>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-30400>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-30401>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-30402>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-30403>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-30404>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-30405>`         Specifies the context-sensitive help text associated with this
:ref:`Hover <no-30406>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-30407>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-30408>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-30409>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-30410>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-30411>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-30412>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-30413>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-30414>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-30415>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-30416>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-30417>`                Specifies the base name of the object.
:ref:`PanelPosition <no-30418>`           Position of this panel within the parent container  (int)
:ref:`Parent <no-30419>`                  Reference to the containing dSlidePanelControl.
:ref:`Position <no-30420>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-30421>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-30422>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-30423>`                   The position of the right side of the object. This is a
:ref:`Size <no-30424>`                    The size of the object. (tuple)
:ref:`Sizer <no-30425>`                   The sizer for the object.
:ref:`StatusText <no-30426>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-30427>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-30428>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-30429>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-30430>`                     The top position of the object. (int)
:ref:`Transparency <no-30431>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-30432>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-30433>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-30434>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-30435>`                   The width of the object. (int)
:ref:`WindowHandle <no-30436>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-30339:

**BarColor1** 

Main color for the caption bar  (dColor)



-------

.. _no-30340:

**BarColor2** 

Secondary color for the caption bar. Only used in gradients  (dColor)



-------

.. _no-30341:

**BarStyle** 

"Determines how the bar containing the caption
    for this panel is drawn. (str)

    Can be one of the following:
        Borderless        (no border, just a plain fill color; default)
        BorderOnly    (simple border, no fill color)
        FilledBorder    (combination of the two above)
        VerticalFill        (vertical gradient fill, using the two caption colors)
        HorizontalFill    (horizontal gradient fill, using the two caption colors)
    



-------

.. _no-30351:

**CaptionForeColor** 

Text color of the caption bar  (str or tuple)



-------

.. _no-30352:

**CaptionHeight** 

Height of the caption bar. Read-only  (int)



-------

.. _no-30355:

**Collapsed** 

Is the panel main area hidden?  (bool)



-------

.. _no-30361:

**DynamicBarColor1** 

Dynamically determine the value of the BarColor1 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BarColor1 property. If DynamicBarColor1 is set to None (the default), BarColor1
will not be dynamically evaluated.



-------

.. _no-30362:

**DynamicBarColor2** 

Dynamically determine the value of the BarColor2 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BarColor2 property. If DynamicBarColor2 is set to None (the default), BarColor2
will not be dynamically evaluated.



-------

.. _no-30363:

**DynamicBarStyle** 

Dynamically determine the value of the BarStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BarStyle property. If DynamicBarStyle is set to None (the default), BarStyle
will not be dynamically evaluated.



-------

.. _no-30369:

**DynamicCaptionForeColor** 

Dynamically determine the value of the CaptionForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CaptionForeColor property. If DynamicCaptionForeColor is set to None (the default), CaptionForeColor
will not be dynamically evaluated.



-------

.. _no-30370:

**DynamicCollapsed** 

Dynamically determine the value of the Collapsed property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Collapsed property. If DynamicCollapsed is set to None (the default), Collapsed
will not be dynamically evaluated.



-------

.. _no-30372:

**DynamicExpanded** 

Dynamically determine the value of the Expanded property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Expanded property. If DynamicExpanded is set to None (the default), Expanded
will not be dynamically evaluated.



-------

.. _no-30393:

**Expanded** 

Is the panel main area visible?  (bool)



-------

.. _no-30418:

**PanelPosition** 

Position of this panel within the parent container  (int)



-------


Properties - inherited
========================

.. _no-30337:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30338:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30342:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30343:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30344:

**Border** 

Border between the contents and edges of the panel. Default=5  (int)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30345:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30346:

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

.. _no-30347:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30348:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30349:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30350:

**Caption** 

Caption displayed on the panel bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30353:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30354:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30356:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30357:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30358:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30359:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30360:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30364:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30365:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30366:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30367:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30368:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30371:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30373:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30374:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30375:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30376:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30377:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30378:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30379:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30380:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30381:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30382:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30383:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30384:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30385:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30386:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30387:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30388:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30389:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30390:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30391:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30392:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30394:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30395:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30396:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30397:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30398:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30399:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30400:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30401:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30402:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30403:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30404:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30405:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30406:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30407:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30408:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30409:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30410:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30411:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30412:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30413:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30414:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30415:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30416:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30417:

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

.. _no-30419:

**Parent** 

Reference to the containing dSlidePanelControl.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30420:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30421:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30422:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30423:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30424:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30425:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30426:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30427:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-30428:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30429:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30430:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30431:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30432:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30433:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30434:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30435:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30436:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-30437>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-30438>`                 Occurs after the control or form is created.
:ref:`Destroy <no-30439>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-30440>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-30441>`               Occurs when the control gets the focus.
:ref:`Idle <no-30442>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-30443>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-30444>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-30445>`               
:ref:`KeyUp <no-30446>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-30447>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-30448>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-30449>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-30450>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-30451>`             
:ref:`MouseLeave <no-30452>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-30453>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-30454>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-30455>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-30456>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-30457>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-30458>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-30459>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-30460>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-30461>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-30462>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-30463>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-30464>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-30465>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-30466>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-30467>`                   Occurs when the control's position changes.
:ref:`Paint <no-30468>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-30469>`                 Occurs when the control or form is resized.
:ref:`SlidePanelCaptionClick <no-30470>` Occurs when the caption bar of a dSlidePanel is clicked.
:ref:`SlidePanelChange <no-30471>`       Occurs when a panel in a dSlidePanelControl control is hidden or shown.
:ref:`TreeBeginDrag <no-30472>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-30473>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-30474>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-30437:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-30438:

**Create** 

Occurs after the control or form is created.



-------

.. _no-30439:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-30440:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-30441:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-30442:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-30443:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-30444:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-30445:

**KeyEvent** 



-------

.. _no-30446:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-30447:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-30448:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-30449:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-30450:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-30451:

**MouseEvent** 



-------

.. _no-30452:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-30453:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-30454:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-30455:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-30456:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-30457:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-30458:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-30459:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-30460:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-30461:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-30462:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-30463:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-30464:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-30465:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-30466:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-30467:

**Move** 

Occurs when the control's position changes.



-------

.. _no-30468:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-30469:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-30470:

**SlidePanelCaptionClick** 

Occurs when the caption bar of a dSlidePanel is clicked.



-------

.. _no-30471:

**SlidePanelChange** 

Occurs when a panel in a dSlidePanelControl control is hidden or shown.



-------

.. _no-30472:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-30473:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-30474:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-30475>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-30476>`             Instantiate object as a child of self.
:ref:`afterInit <no-30477>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-30478>`          
:ref:`afterSetProperties <no-30479>`    
:ref:`appendSeparator <no-30480>`       This draws a separator line on the panel
:ref:`autoBindEvents <no-30481>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-30482>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-30483>`   
:ref:`bindEvent <no-30484>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-30485>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-30486>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-30487>`          Makes this object topmost
:ref:`clear <no-30488>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-30489>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-30490>`  Given a position relative to this control, return a position relative
:ref:`copy <no-30491>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-30492>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-30493>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-30494>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-30495>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-30496>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-30497>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-30498>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-30499>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-30500>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-30501>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-30502>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-30503>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-30504>`              Draws text on the object at the specified position
:ref:`endHover <no-30505>`              
:ref:`fitToSizer <no-30506>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-30507>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-30508>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-30509>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-30510>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-30511>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-30512>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-30513>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-30514>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-30515>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-30516>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-30517>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-30518>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-30519>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-30520>`                  Make the object invisible.
:ref:`initEvents <no-30521>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-30522>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-30523>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-30524>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-30525>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-30526>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-30527>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-30528>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-30529>`     Given a position relative to the form, return a position relative
:ref:`onChildBorn <no-30530>`           
:ref:`onHover <no-30531>`               
:ref:`paste <no-30532>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-30533>`           
:ref:`processDroppedFiles <no-30534>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-30535>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-30536>`            Raise the passed Dabo event.
:ref:`reCreate <no-30537>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-30538>`              Recreate the object.
:ref:`redraw <no-30539>`                Called when the object is (re)drawn.
:ref:`refresh <no-30540>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-30541>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-30542>`               Destroys the object.
:ref:`removeDrawnObject <no-30543>`     
:ref:`sendToBack <no-30544>`            Places this object behind all others.
:ref:`setAll <no-30545>`                Set all child object properties to the passed value.
:ref:`setFocus <no-30546>`              Sets focus to the object.
:ref:`setPositionInSizer <no-30547>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-30548>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-30549>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-30550>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-30551>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-30552>`                  Make the object visible.
:ref:`showContainingPage <no-30553>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-30554>`       Display a context menu (popup) at the specified position.
:ref:`super <no-30555>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-30556>`           Remove a previously registered event binding.
:ref:`unbindKey <no-30557>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-30558>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-30559>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-30560>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-30480:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.appendSeparator(self, color=None)

   This draws a separator line on the panel



-------

.. _no-30525:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.layout(self)

   Wrap the wx version of the call, if possible.



-------

.. _no-30530:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.onChildBorn(self, evt)



-------


Methods - inherited
=====================

.. _no-30475:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30476:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-30477:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30478:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30479:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30481:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.autoBindEvents(self, force=True)
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

.. _no-30482:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30483:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30484:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30485:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30486:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-30487:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30488:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30489:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30490:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30491:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30492:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30493:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30494:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30495:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-30496:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30497:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30498:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30499:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30500:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30501:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30502:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30503:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30504:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30505:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30506:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30507:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30508:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30509:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30510:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30511:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30512:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30513:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30514:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30515:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30516:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30517:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-30518:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30519:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30520:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30521:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30522:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30523:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30524:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30526:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.lockDisplay(self)
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

.. _no-30527:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30528:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30529:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30531:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30532:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30533:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30534:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30535:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30536:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30537:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30538:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30539:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30540:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30541:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30542:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30543:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30544:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30545:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-30546:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30547:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30548:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-30549:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-30550:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30551:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30552:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30553:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30554:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30555:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30556:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30557:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30558:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30559:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30560:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
