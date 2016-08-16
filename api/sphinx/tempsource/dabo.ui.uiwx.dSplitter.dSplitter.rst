
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSplitter

.. _dabo.ui.uiwx.dSplitter.dSplitter:

============================================
|doc_title|  **dSplitter.dSplitter** - class
============================================


Main class for handling split windows. It will contain two
panels (subclass of SplitterPanelMixin), each of which can further
split itself in two.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSplitter**

.. inheritance-diagram:: dSplitter


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|subclasses| Known Subclasses
=============================




|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dSplitter.png
          :scale: 75 %
          :target: _static/macWidgets/dSplitter.png
          :alt: dSplitter



     - .. image:: _static/winWidgets/dSplitter.png
          :scale: 75 %
          :target: _static/winWidgets/dSplitter.png
          :alt: dSplitter



     - .. image:: _static/nixWidgets/dSplitter.png
          :scale: 75 %
          :target: _static/nixWidgets/dSplitter.png
          :alt: dSplitter


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSplitter.dSplitter

   .. automethod:: dabo.ui.uiwx.dSplitter.dSplitter.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-23831>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-23832>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-23833>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-23834>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-23835>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-23836>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-23837>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-23838>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-23839>`                  The position of the bottom side of the object. This is a
:ref:`CanUnsplit <no-23840>`              Can the control be unsplit (i.e., only the first pane visible),
:ref:`Caption <no-23841>`                 The caption of the object. (str)
:ref:`Children <no-23842>`                Returns a list of object references to the children of
:ref:`Class <no-23843>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-23844>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-23845>`    Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-23846>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-23847>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-23848>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-23849>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-23850>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-23851>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-23852>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-23853>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-23854>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-23855>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-23856>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-23857>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-23858>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-23859>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-23860>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-23861>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-23862>`           Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-23863>`             Dynamically determine the value of the Left property.
:ref:`DynamicMinimumPanelSize <no-23864>` Dynamically determine the value of the MinimumPanelSize property.
:ref:`DynamicMousePointer <no-23865>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicOrientation <no-23866>`      Dynamically determine the value of the Orientation property.
:ref:`DynamicPanel1 <no-23867>`           Dynamically determine the value of the Panel1 property.
:ref:`DynamicPanel2 <no-23868>`           Dynamically determine the value of the Panel2 property.
:ref:`DynamicPosition <no-23869>`         Dynamically determine the value of the Position property.
:ref:`DynamicSashPosition <no-23870>`     Dynamically determine the value of the SashPosition property.
:ref:`DynamicSize <no-23871>`             Dynamically determine the value of the Size property.
:ref:`DynamicSplit <no-23872>`            Dynamically determine the value of the Split property.
:ref:`DynamicStatusText <no-23873>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-23874>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-23875>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-23876>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-23877>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-23878>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-23879>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-23880>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-23881>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-23882>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-23883>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-23884>`                Specifies the font face. (str)
:ref:`FontInfo <no-23885>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-23886>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-23887>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-23888>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-23889>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-23890>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-23891>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-23892>`         Specifies the context-sensitive help text associated with this
:ref:`Hover <no-23893>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-23894>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-23895>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-23896>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-23897>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-23898>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-23899>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumPanelSize <no-23900>`        Controls the minimum width/height of the panels.  (int)
:ref:`MinimumSize <no-23901>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-23902>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-23903>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-23904>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-23905>`                Specifies the base name of the object.
:ref:`Orientation <no-23906>`             Determines if the window splits Horizontally or Vertically.  (string)
:ref:`Panel1 <no-23907>`                  Returns the Top/Left panel.  (dPanel)
:ref:`Panel2 <no-23908>`                  Returns the Bottom/Right panel.  (dPanel)
:ref:`PanelClass <no-23909>`              Class used for creating panels. If the class does not descend from
:ref:`Parent <no-23910>`                  The containing object. (obj)
:ref:`Position <no-23911>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-23912>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-23913>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-23914>`                   The position of the right side of the object. This is a
:ref:`SashPercent <no-23915>`             Percentage of the split window given to Panel1. Range=0-100  (float)
:ref:`SashPosition <no-23916>`            Position of the sash when the window is split.  (int)
:ref:`ShowPanelSplitMenu <no-23917>`      Determines if the default context menu for split/unsplit is enabled
:ref:`Size <no-23918>`                    The size of the object. (tuple)
:ref:`Sizer <no-23919>`                   The sizer for the object.
:ref:`Split <no-23920>`                   Returns the split status of the control  (bool)
:ref:`StatusText <no-23921>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-23922>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-23923>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-23924>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-23925>`                     The top position of the object. (int)
:ref:`Transparency <no-23926>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-23927>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-23928>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-23929>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-23930>`                   The width of the object. (int)
:ref:`WindowHandle <no-23931>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-23840:

**CanUnsplit** 

Can the control be unsplit (i.e., only the first pane visible),
    even with a non-zero MinimumPanelSize? Can only be set when the control
    is created; read-only afterwards. Default=True  (bool)



-------

.. _no-23864:

**DynamicMinimumPanelSize** 

Dynamically determine the value of the MinimumPanelSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MinimumPanelSize property. If DynamicMinimumPanelSize is set to None (the default), MinimumPanelSize
will not be dynamically evaluated.



-------

.. _no-23866:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-23867:

**DynamicPanel1** 

Dynamically determine the value of the Panel1 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Panel1 property. If DynamicPanel1 is set to None (the default), Panel1
will not be dynamically evaluated.



-------

.. _no-23868:

**DynamicPanel2** 

Dynamically determine the value of the Panel2 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Panel2 property. If DynamicPanel2 is set to None (the default), Panel2
will not be dynamically evaluated.



-------

.. _no-23870:

**DynamicSashPosition** 

Dynamically determine the value of the SashPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SashPosition property. If DynamicSashPosition is set to None (the default), SashPosition
will not be dynamically evaluated.



-------

.. _no-23872:

**DynamicSplit** 

Dynamically determine the value of the Split property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Split property. If DynamicSplit is set to None (the default), Split
will not be dynamically evaluated.



-------

.. _no-23900:

**MinimumPanelSize** 

Controls the minimum width/height of the panels.  (int)



-------

.. _no-23906:

**Orientation** 

Determines if the window splits Horizontally or Vertically.  (string)



-------

.. _no-23907:

**Panel1** 

Returns the Top/Left panel.  (dPanel)



-------

.. _no-23908:

**Panel2** 

Returns the Bottom/Right panel.  (dPanel)



-------

.. _no-23909:

**PanelClass** 

Class used for creating panels. If the class does not descend from
    SplitterPanelMixin, that class will be mixed-into the class specified here.
    This must be set before the panels are created; setting it afterward has
    no effect unless you destroy the panels and re-create them.
    Default=dPanel  (dPanel)



-------

.. _no-23915:

**SashPercent** 

Percentage of the split window given to Panel1. Range=0-100  (float)



-------

.. _no-23917:

**ShowPanelSplitMenu** 

Determines if the default context menu for split/unsplit is enabled
    for the panels (default=False)  (bool)



-------

.. _no-23920:

**Split** 

Returns the split status of the control  (bool)



-------


Properties - inherited
========================

.. _no-23831:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23832:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23833:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23834:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23835:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23836:

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

.. _no-23837:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23838:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23839:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23841:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23842:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23843:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23844:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23845:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23846:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23847:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23848:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23849:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23850:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23851:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23852:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23853:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23854:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23855:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23856:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23857:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23858:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23859:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23860:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23861:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23862:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23863:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23865:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23869:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23871:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23873:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23874:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23875:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23876:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23877:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23878:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23879:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23880:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23881:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23882:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23883:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23884:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23885:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23886:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23887:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23888:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23889:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23890:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23891:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23892:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23893:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23894:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23895:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23896:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23897:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23898:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23899:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23901:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23902:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23903:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23904:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23905:

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

.. _no-23910:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23911:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23912:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23913:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23914:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23916:

**SashPosition** 

Position of the sash when the window is split.  (int)


Inherited from: 'wx._windows.SplitterWindow - can not provide a link

-------

.. _no-23918:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23919:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23921:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23922:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-23923:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23924:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23925:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23926:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23927:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23928:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23929:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23930:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23931:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-23932>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-23933>`                 Occurs after the control or form is created.
:ref:`Destroy <no-23934>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-23935>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-23936>`               Occurs when the control gets the focus.
:ref:`Idle <no-23937>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-23938>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-23939>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-23940>`               
:ref:`KeyUp <no-23941>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-23942>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-23943>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-23944>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-23945>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-23946>`             
:ref:`MouseLeave <no-23947>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-23948>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-23949>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-23950>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-23951>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-23952>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-23953>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-23954>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-23955>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-23956>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-23957>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-23958>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-23959>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-23960>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-23961>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-23962>`                   Occurs when the control's position changes.
:ref:`Paint <no-23963>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-23964>`                 Occurs when the control or form is resized.
:ref:`SashDoubleClick <no-23965>`        Occurs when a user double-clicks on the sash of a splitter window.
:ref:`SashEvent <no-23966>`              
:ref:`SashPositionChanged <no-23967>`    Occurs when a user moves the sash of a splitter window.
:ref:`TreeBeginDrag <no-23968>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-23969>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-23970>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-23932:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-23933:

**Create** 

Occurs after the control or form is created.



-------

.. _no-23934:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-23935:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-23936:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-23937:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-23938:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-23939:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-23940:

**KeyEvent** 



-------

.. _no-23941:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-23942:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-23943:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-23944:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-23945:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-23946:

**MouseEvent** 



-------

.. _no-23947:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-23948:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-23949:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-23950:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-23951:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-23952:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-23953:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-23954:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-23955:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-23956:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-23957:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-23958:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-23959:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-23960:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-23961:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-23962:

**Move** 

Occurs when the control's position changes.



-------

.. _no-23963:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-23964:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-23965:

**SashDoubleClick** 

Occurs when a user double-clicks on the sash of a splitter window.



-------

.. _no-23966:

**SashEvent** 



-------

.. _no-23967:

**SashPositionChanged** 

Occurs when a user moves the sash of a splitter window.



-------

.. _no-23968:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-23969:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-23970:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-23971>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-23972>`             Instantiate object as a child of self.
:ref:`afterInit <no-23973>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-23974>`          
:ref:`afterSetProperties <no-23975>`    
:ref:`autoBindEvents <no-23976>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-23977>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-23978>`   
:ref:`bindEvent <no-23979>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-23980>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-23981>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-23982>`          Makes this object topmost
:ref:`canRemove <no-23983>`             
:ref:`clear <no-23984>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-23985>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-23986>`  Given a position relative to this control, return a position relative
:ref:`copy <no-23987>`                  Called by uiApp when the user requests a copy operation.
:ref:`createPanes <no-23988>`           
:ref:`cut <no-23989>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-23990>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-23991>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-23992>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-23993>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-23994>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-23995>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-23996>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-23997>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-23998>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-23999>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-24000>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-24001>`              Draws text on the object at the specified position
:ref:`endHover <no-24002>`              
:ref:`fitToSizer <no-24003>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-24004>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-24005>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-24006>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-24007>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-24008>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-24009>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-24010>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-24011>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-24012>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-24013>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-24014>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-24015>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-24016>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-24017>`                  Make the object invisible.
:ref:`initEvents <no-24018>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-24019>`        Hook for subclasses. User subclasses should set properties
:ref:`initialize <no-24020>`            
:ref:`isContainedBy <no-24021>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-24022>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-24023>`                
:ref:`lockDisplay <no-24024>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-24025>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-24026>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-24027>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-24028>`               
:ref:`paste <no-24029>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-24030>`           
:ref:`processDroppedFiles <no-24031>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-24032>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-24033>`            Raise the passed Dabo event.
:ref:`reCreate <no-24034>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-24035>`              Recreate the object.
:ref:`redraw <no-24036>`                Called when the object is (re)drawn.
:ref:`refresh <no-24037>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-24038>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-24039>`               Destroys the object.
:ref:`remove <no-24040>`                
:ref:`removeDrawnObject <no-24041>`     
:ref:`sendToBack <no-24042>`            Places this object behind all others.
:ref:`setAll <no-24043>`                Set all child object properties to the passed value.
:ref:`setFocus <no-24044>`              Sets focus to the object.
:ref:`setPositionInSizer <no-24045>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-24046>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-24047>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-24048>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-24049>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-24050>`                  Make the object visible.
:ref:`showContainingPage <no-24051>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-24052>`       Display a context menu (popup) at the specified position.
:ref:`split <no-24053>`                 
:ref:`super <no-24054>`                 This method used to call superclass code, but it's been removed.
:ref:`toggleSplit <no-24055>`           Flips the split status of the control.
:ref:`unbindEvent <no-24056>`           Remove a previously registered event binding.
:ref:`unbindKey <no-24057>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-24058>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-24059>`      Immediately unlocks the display, no matter how many previous
:ref:`unsplit <no-24060>`               
:ref:`update <no-24061>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-23983:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.canRemove(self, pnl)



-------

.. _no-23988:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.createPanes(self, cls=None, pane=None, force=False)



-------

.. _no-24020:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.initialize(self, pnl)



-------

.. _no-24023:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.layout(self)



-------

.. _no-24040:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.remove(self, pnl)



-------

.. _no-24053:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.split(self, dir_=None)



-------

.. _no-24055:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.toggleSplit(self)

   Flips the split status of the control.



-------

.. _no-24060:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.unsplit(self, win=None)



-------


Methods - inherited
=====================

.. _no-23971:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23972:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-23973:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23974:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23975:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23976:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.autoBindEvents(self, force=True)
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

.. _no-23977:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23978:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23979:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23980:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23981:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-23982:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23984:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23985:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23986:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23987:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23989:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23990:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23991:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23992:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-23993:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23994:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23995:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23996:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23997:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23998:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23999:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24000:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24001:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24002:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24003:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24004:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24005:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24006:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24007:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24008:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24009:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24010:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24011:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24012:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24013:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24014:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-24015:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24016:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24017:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24018:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24019:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24021:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24022:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24024:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.lockDisplay(self)
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

.. _no-24025:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24026:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24027:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24028:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24029:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24030:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24031:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24032:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24033:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24034:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24035:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24036:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24037:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24038:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24039:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24041:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24042:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24043:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-24044:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24045:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24046:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-24047:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-24048:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24049:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24050:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24051:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24052:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24054:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24056:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24057:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24058:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24059:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24061:

.. function:: dabo.ui.uiwx.dSplitter.dSplitter.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
