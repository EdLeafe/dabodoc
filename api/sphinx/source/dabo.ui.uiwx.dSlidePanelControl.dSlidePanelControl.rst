
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSlidePanelControl

.. _dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl:

==============================================================
|doc_title|  **dSlidePanelControl.dSlidePanelControl** - class
==============================================================


Creates a control consisting of several panels that can be
hidden or revealed by clicking on their 'caption bar'.

This allows you to collapse each panel down to its caption bar,
which either remains in place or drops to the bottom.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSlidePanelControl**

.. inheritance-diagram:: dSlidePanelControl


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.lib.agw.foldpanelbar.FoldPanelBar - can not provide a link



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dFoldPanelBar`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dSlidePanelControl.png
          :scale: 75 %
          :target: _static/macWidgets/dSlidePanelControl.png
          :alt: dSlidePanelControl



     - no image available



     - .. image:: _static/nixWidgets/dSlidePanelControl.png
          :scale: 75 %
          :target: _static/nixWidgets/dSlidePanelControl.png
          :alt: dSlidePanelControl


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl

   .. automethod:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-30561>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-30562>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-30563>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-30564>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-30565>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-30566>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-30567>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-30568>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-30569>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-30570>`                 The caption of the object. (str)
:ref:`Children <no-30571>`                List of all panels in the control  (list))
:ref:`Class <no-30572>`                   The class the object is based on. Read-only.  (class)
:ref:`CollapseToBottom <no-30573>`        When True, all collapsed panels are displayed at the bottom  (bool)
:ref:`ControllingSizer <no-30574>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-30575>`    Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-30576>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-30577>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-30578>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-30579>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-30580>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-30581>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-30582>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-30583>`          Dynamically determine the value of the Caption property.
:ref:`DynamicCollapseToBottom <no-30584>` Dynamically determine the value of the CollapseToBottom property.
:ref:`DynamicEnabled <no-30585>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-30586>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-30587>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-30588>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-30589>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-30590>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-30591>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-30592>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-30593>`           Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-30594>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-30595>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-30596>`         Dynamically determine the value of the Position property.
:ref:`DynamicSingleClick <no-30597>`      Dynamically determine the value of the SingleClick property.
:ref:`DynamicSingleton <no-30598>`        Dynamically determine the value of the Singleton property.
:ref:`DynamicSize <no-30599>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-30600>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-30601>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-30602>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-30603>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-30604>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-30605>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-30606>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-30607>`                 Specifies whether the object and children can get user input. (bool)
:ref:`ExpandContent <no-30608>`           When True, the panels size themselves to the size of this object.
:ref:`Font <no-30609>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-30610>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-30611>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-30612>`                Specifies the font face. (str)
:ref:`FontInfo <no-30613>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-30614>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-30615>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-30616>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-30617>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-30618>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-30619>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-30620>`         Specifies the context-sensitive help text associated with this
:ref:`Hover <no-30621>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-30622>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-30623>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-30624>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-30625>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-30626>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinSizerHeight <no-30627>`          Minimum height for the control. Default=100px  (int)
:ref:`MinSizerWidth <no-30628>`           Minimum width for the control. Default=100px  (int)
:ref:`MinimumHeight <no-30629>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-30630>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-30631>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-30632>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-30633>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-30634>`                Specifies the base name of the object.
:ref:`PanelClass <no-30635>`              Specifies the class of control to use for panels by default. (dSlidePanel)
:ref:`PanelCount <no-30636>`              Number of child panels.  (read-only) (int)
:ref:`Panels <no-30637>`                  List of contained panels. Same as the 'Children' property.  (read-only) (list)
:ref:`Parent <no-30638>`                  The containing object. (obj)
:ref:`Position <no-30639>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-30640>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-30641>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-30642>`                   The position of the right side of the object. This is a
:ref:`SingleClick <no-30643>`             When True, a single click on the caption bar toggles the
:ref:`Singleton <no-30644>`               When True, one and only one panel at a time will be expanded  (bool)
:ref:`Size <no-30645>`                    The size of the object. (tuple)
:ref:`Sizer <no-30646>`                   The sizer for the object.
:ref:`StatusText <no-30647>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-30648>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-30649>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-30650>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-30651>`                     The top position of the object. (int)
:ref:`Transparency <no-30652>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-30653>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-30654>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-30655>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-30656>`                   The width of the object. (int)
:ref:`WindowHandle <no-30657>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-30573:

**CollapseToBottom** 

When True, all collapsed panels are displayed at the bottom  (bool)



-------

.. _no-30584:

**DynamicCollapseToBottom** 

Dynamically determine the value of the CollapseToBottom property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CollapseToBottom property. If DynamicCollapseToBottom is set to None (the default), CollapseToBottom
will not be dynamically evaluated.



-------

.. _no-30597:

**DynamicSingleClick** 

Dynamically determine the value of the SingleClick property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SingleClick property. If DynamicSingleClick is set to None (the default), SingleClick
will not be dynamically evaluated.



-------

.. _no-30598:

**DynamicSingleton** 

Dynamically determine the value of the Singleton property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Singleton property. If DynamicSingleton is set to None (the default), Singleton
will not be dynamically evaluated.



-------

.. _no-30608:

**ExpandContent** 

When True, the panels size themselves to the size of this object.
    Otherwise, panels only take up as much space as they need. (default=True) (bool)



-------

.. _no-30627:

**MinSizerHeight** 

Minimum height for the control. Default=100px  (int)



-------

.. _no-30628:

**MinSizerWidth** 

Minimum width for the control. Default=100px  (int)



-------

.. _no-30635:

**PanelClass** 

Specifies the class of control to use for panels by default. (dSlidePanel)
    This really only applies when using the PanelCount property to set the
    number of panels.



-------

.. _no-30636:

**PanelCount** 

Number of child panels.  (read-only) (int)



-------

.. _no-30637:

**Panels** 

List of contained panels. Same as the 'Children' property.  (read-only) (list)



-------

.. _no-30643:

**SingleClick** 

When True, a single click on the caption bar toggles the
    expanded/collapsed state  (bool)



-------

.. _no-30644:

**Singleton** 

When True, one and only one panel at a time will be expanded  (bool)



-------


Properties - inherited
========================

.. _no-30561:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30562:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30563:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30564:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30565:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30566:

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

.. _no-30567:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30568:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30569:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30570:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30571:

**Children** 

List of all panels in the control  (list))


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30572:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30574:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30575:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30576:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30577:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30578:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30579:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30580:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30581:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30582:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30583:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30585:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30586:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30587:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30588:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30589:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30590:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30591:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30592:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30593:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30594:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30595:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30596:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30599:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30600:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30601:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30602:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30603:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30604:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30605:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30606:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30607:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30609:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30610:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30611:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30612:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30613:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30614:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30615:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30616:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30617:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30618:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30619:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30620:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30621:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30622:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30623:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30624:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30625:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30626:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30629:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30630:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30631:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30632:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30633:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30634:

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

.. _no-30638:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30639:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30640:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30641:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30642:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30645:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30646:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30647:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30648:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-30649:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30650:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30651:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30652:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30653:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30654:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30655:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30656:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30657:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-30658>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-30659>`                 Occurs after the control or form is created.
:ref:`Destroy <no-30660>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-30661>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-30662>`               Occurs when the control gets the focus.
:ref:`Idle <no-30663>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-30664>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-30665>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-30666>`               
:ref:`KeyUp <no-30667>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-30668>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-30669>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-30670>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-30671>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-30672>`             
:ref:`MouseLeave <no-30673>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-30674>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-30675>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-30676>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-30677>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-30678>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-30679>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-30680>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-30681>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-30682>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-30683>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-30684>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-30685>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-30686>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-30687>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-30688>`                   Occurs when the control's position changes.
:ref:`Paint <no-30689>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-30690>`                 Occurs when the control or form is resized.
:ref:`SlidePanelChange <no-30691>`       Occurs when a panel in a dSlidePanelControl control is hidden or shown.
:ref:`TreeBeginDrag <no-30692>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-30693>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-30694>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-30658:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-30659:

**Create** 

Occurs after the control or form is created.



-------

.. _no-30660:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-30661:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-30662:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-30663:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-30664:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-30665:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-30666:

**KeyEvent** 



-------

.. _no-30667:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-30668:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-30669:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-30670:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-30671:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-30672:

**MouseEvent** 



-------

.. _no-30673:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-30674:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-30675:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-30676:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-30677:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-30678:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-30679:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-30680:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-30681:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-30682:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-30683:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-30684:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-30685:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-30686:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-30687:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-30688:

**Move** 

Occurs when the control's position changes.



-------

.. _no-30689:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-30690:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-30691:

**SlidePanelChange** 

Occurs when a panel in a dSlidePanelControl control is hidden or shown.



-------

.. _no-30692:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-30693:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-30694:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-30695>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-30696>`             Instantiate object as a child of self.
:ref:`afterInit <no-30697>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-30698>`          
:ref:`afterSetProperties <no-30699>`    
:ref:`append <no-30700>`                
:ref:`appendPanel <no-30701>`           
:ref:`autoBindEvents <no-30702>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-30703>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-30704>`   
:ref:`bindEvent <no-30705>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-30706>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-30707>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-30708>`          Makes this object topmost
:ref:`clear <no-30709>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-30710>`                 Create another object just like the passed object. It assumes that the
:ref:`collapse <no-30711>`              
:ref:`collapseAll <no-30712>`           
:ref:`containerCoordinates <no-30713>`  Given a position relative to this control, return a position relative
:ref:`copy <no-30714>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-30715>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-30716>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-30717>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-30718>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-30719>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-30720>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-30721>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-30722>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-30723>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-30724>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-30725>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-30726>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-30727>`              Draws text on the object at the specified position
:ref:`endHover <no-30728>`              
:ref:`expand <no-30729>`                
:ref:`expandAll <no-30730>`             
:ref:`fitToSizer <no-30731>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-30732>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-30733>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-30734>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-30735>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-30736>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-30737>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-30738>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-30739>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-30740>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-30741>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-30742>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-30743>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-30744>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-30745>`                  Make the object invisible.
:ref:`initEvents <no-30746>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-30747>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-30748>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-30749>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-30750>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-30751>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-30752>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-30753>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-30754>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-30755>`               
:ref:`onResize <no-30756>`              
:ref:`paste <no-30757>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-30758>`           
:ref:`processDroppedFiles <no-30759>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-30760>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-30761>`            Raise the passed Dabo event.
:ref:`reCreate <no-30762>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-30763>`              Recreate the object.
:ref:`redraw <no-30764>`                Called when the object is (re)drawn.
:ref:`refresh <no-30765>`               
:ref:`relativeCoordinates <no-30766>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-30767>`               Destroys the object.
:ref:`removeDrawnObject <no-30768>`     
:ref:`sendToBack <no-30769>`            Places this object behind all others.
:ref:`setAll <no-30770>`                Set all child object properties to the passed value.
:ref:`setFocus <no-30771>`              Sets focus to the object.
:ref:`setPositionInSizer <no-30772>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-30773>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-30774>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-30775>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-30776>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-30777>`                  Make the object visible.
:ref:`showContainingPage <no-30778>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-30779>`       Display a context menu (popup) at the specified position.
:ref:`sizePanelHeights <no-30780>`      Control the heights of the panels. Originally I thought we only needed
:ref:`super <no-30781>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-30782>`           Remove a previously registered event binding.
:ref:`unbindKey <no-30783>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-30784>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-30785>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-30786>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-30700:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.append(self, pnl=None, \**kwargs)



-------

.. _no-30701:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.appendPanel(self, pnl)



-------

.. _no-30711:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.collapse(self, pnl)



-------

.. _no-30712:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.collapseAll(self)



-------

.. _no-30729:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.expand(self, pnl)



-------

.. _no-30730:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.expandAll(self)



-------

.. _no-30750:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.layout(self)

   Wrap the wx version of the call, if possible.



-------

.. _no-30756:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.onResize(self, evt)



-------

.. _no-30765:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.refresh(self)



-------

.. _no-30780:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.sizePanelHeights(self, force=False)

   
   Control the heights of the panels. Originally I thought we only needed
   this when running in Singleton mode, but now it seems better to run this
   in all modes.
   



-------


Methods - inherited
=====================

.. _no-30695:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30696:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-30697:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30698:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30699:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30702:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.autoBindEvents(self, force=True)
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

.. _no-30703:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30704:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30705:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30706:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30707:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-30708:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30709:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30710:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30713:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30714:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30715:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30716:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30717:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30718:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-30719:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30720:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30721:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30722:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30723:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30724:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30725:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30726:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30727:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30728:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30731:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30732:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30733:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30734:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30735:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30736:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30737:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30738:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30739:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30740:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30741:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30742:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-30743:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30744:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30745:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30746:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30747:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30748:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30749:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30751:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.lockDisplay(self)
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

.. _no-30752:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30753:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30754:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30755:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30757:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30758:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30759:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30760:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30761:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30762:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30763:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30764:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30766:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30767:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30768:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30769:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30770:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-30771:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30772:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30773:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-30774:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-30775:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30776:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30777:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30778:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30779:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30781:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30782:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30783:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30784:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30785:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30786:

.. function:: dabo.ui.uiwx.dSlidePanelControl.dSlidePanelControl.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
