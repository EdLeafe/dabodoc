
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dHtmlBox

.. _dabo.ui.uiwx.dHtmlBox.dHtmlBox:

==========================================
|doc_title|  **dHtmlBox.dHtmlBox** - class
==========================================


Creates a scrolled panel that can load and display html pages. The Html Window
can load any html text, file, or url that is fed to it.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dHtmlBox**

.. inheritance-diagram:: dHtmlBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.html.HtmlWindow - can not provide a link



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



   * - .. image:: _static/macWidgets/dHtmlBox.png
          :scale: 75 %
          :target: _static/macWidgets/dHtmlBox.png
          :alt: dHtmlBox



     - .. image:: _static/winWidgets/dHtmlBox.png
          :scale: 75 %
          :target: _static/winWidgets/dHtmlBox.png
          :alt: dHtmlBox



     - .. image:: _static/nixWidgets/dHtmlBox.png
          :scale: 75 %
          :target: _static/nixWidgets/dHtmlBox.png
          :alt: dHtmlBox


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dHtmlBox.dHtmlBox

   .. automethod:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-15843>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-15844>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-15845>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-15846>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-15847>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-15848>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-15849>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-15850>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-15851>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-15852>`                 The caption of the object. (str)
:ref:`Children <no-15853>`                Returns a list of object references to the children of
:ref:`Class <no-15854>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-15855>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-15856>`    Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-15857>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-15858>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-15859>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-15860>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-15861>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-15862>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-15863>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-15864>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-15865>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-15866>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-15867>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-15868>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-15869>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-15870>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-15871>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-15872>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-15873>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-15874>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicLeft <no-15875>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-15876>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-15877>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-15878>`             Dynamically determine the value of the Size property.
:ref:`DynamicSource <no-15879>`           Dynamically determine the value of the Source property.
:ref:`DynamicStatusText <no-15880>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-15881>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-15882>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-15883>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-15884>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-15885>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-15886>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-15887>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-15888>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-15889>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-15890>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-15891>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-15892>`                Specifies the font face. (str)
:ref:`FontInfo <no-15893>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-15894>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-15895>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-15896>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-15897>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-15898>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-15899>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-15900>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-15901>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-15902>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-15903>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-15904>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-15905>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-15906>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-15907>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-15908>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-15909>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-15910>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-15911>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-15912>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-15913>`                Specifies the base name of the object.
:ref:`OpenLinksInBrowser <no-15914>`      When True, clicking on an HREF link will open the URL in the default web browser
:ref:`Page <no-15915>`                    URL or file path of the current page being displayed. (default='')  (string)
:ref:`Parent <no-15916>`                  The containing object. (obj)
:ref:`Position <no-15917>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-15918>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-15919>`                   A unique identifier used for referencing by other objects. (str)
:ref:`RespondToLinks <no-15920>`          When True (default), clicking a link will attempt to load that linked page.  (bool)
:ref:`Right <no-15921>`                   The position of the right side of the object. This is a
:ref:`SelectedText <no-15922>`            Currently selected text. Returns the empty string if nothing is selected. Read-only  (str)
:ref:`ShowScrollBars <no-15923>`          When Tru (default), scrollbars will be shown as needed.  (bool)
:ref:`Size <no-15924>`                    The size of the object. (tuple)
:ref:`Sizer <no-15925>`                   The sizer for the object.
:ref:`Source <no-15926>`                  Html source of the current page being display. (default='')  (string)
:ref:`StatusText <no-15927>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-15928>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-15929>`                     A property that user code can safely use for specific purposes.
:ref:`Text <no-15930>`                    Returns the displayed plain text content of the control, free of any
:ref:`ToolTipText <no-15931>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-15932>`                     The top position of the object. (int)
:ref:`Transparency <no-15933>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-15934>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-15935>`                   Html source of the current page being display. (default='')  (string)
:ref:`VerticalScroll <no-15936>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-15937>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-15938>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-15939>`                   The width of the object. (int)
:ref:`WindowHandle <no-15940>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-15874:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.



-------

.. _no-15879:

**DynamicSource** 

Dynamically determine the value of the Source property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Source property. If DynamicSource is set to None (the default), Source
will not be dynamically evaluated.



-------

.. _no-15885:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.



-------

.. _no-15901:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)



-------

.. _no-15914:

**OpenLinksInBrowser** 

When True, clicking on an HREF link will open the URL in the default web browser
    instead of in the control itself. Default=False.  (bool)



-------

.. _no-15915:

**Page** 

URL or file path of the current page being displayed. (default='')  (string)



-------

.. _no-15920:

**RespondToLinks** 

When True (default), clicking a link will attempt to load that linked page.  (bool)



-------

.. _no-15922:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected. Read-only  (str)



-------

.. _no-15923:

**ShowScrollBars** 

When Tru (default), scrollbars will be shown as needed.  (bool)



-------

.. _no-15926:

**Source** 

Html source of the current page being display. (default='')  (string)



-------

.. _no-15930:

**Text** 

Returns the displayed plain text content of the control, free of any
    HTML markup. Read-only  (str)



-------

.. _no-15935:

**Value** 

Html source of the current page being display. (default='')  (string)



-------

.. _no-15936:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)



-------


Properties - inherited
========================

.. _no-15843:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15844:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15845:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15846:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15847:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15848:

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

.. _no-15849:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15850:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15851:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15852:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15853:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15854:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15855:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15856:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15857:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15858:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15859:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15860:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15861:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15862:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15863:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15864:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15865:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15866:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15867:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15868:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15869:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15870:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15871:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15872:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15873:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15875:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15876:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15877:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15878:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15880:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15881:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15882:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15883:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15884:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15886:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15887:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15888:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15889:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15890:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15891:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15892:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15893:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15894:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15895:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15896:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15897:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15898:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15899:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15900:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15902:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15903:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15904:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15905:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15906:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15907:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15908:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15909:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15910:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15911:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15912:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15913:

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

.. _no-15916:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15917:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15918:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15919:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15921:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15924:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15925:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15927:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15928:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-15929:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15931:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15932:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15933:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15934:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15937:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15938:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15939:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15940:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-15941>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-15942>`                 Occurs after the control or form is created.
:ref:`Destroy <no-15943>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-15944>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-15945>`               Occurs when the control gets the focus.
:ref:`HtmlLinkClicked <no-15946>`        Occurs when a link in a dHtmlBox control is clicked.
:ref:`Idle <no-15947>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-15948>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-15949>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-15950>`               
:ref:`KeyUp <no-15951>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-15952>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-15953>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-15954>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-15955>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-15956>`             
:ref:`MouseLeave <no-15957>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-15958>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-15959>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-15960>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-15961>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-15962>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-15963>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-15964>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-15965>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-15966>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-15967>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-15968>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-15969>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-15970>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-15971>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-15972>`                   Occurs when the control's position changes.
:ref:`Paint <no-15973>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-15974>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-15975>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-15976>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-15977>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-15941:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-15942:

**Create** 

Occurs after the control or form is created.



-------

.. _no-15943:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-15944:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-15945:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-15946:

**HtmlLinkClicked** 

Occurs when a link in a dHtmlBox control is clicked.



-------

.. _no-15947:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-15948:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-15949:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-15950:

**KeyEvent** 



-------

.. _no-15951:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-15952:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-15953:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-15954:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-15955:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-15956:

**MouseEvent** 



-------

.. _no-15957:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-15958:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-15959:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-15960:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-15961:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-15962:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-15963:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-15964:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-15965:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-15966:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-15967:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-15968:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-15969:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-15970:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-15971:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-15972:

**Move** 

Occurs when the control's position changes.



-------

.. _no-15973:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-15974:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-15975:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-15976:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-15977:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-15978>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-15979>`             Instantiate object as a child of self.
:ref:`afterInit <no-15980>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-15981>`          
:ref:`afterSetProperties <no-15982>`    
:ref:`autoBindEvents <no-15983>`        Automatically bind any on*() methods to the associated event.
:ref:`base_OnCellClicked <no-15984>`    Please use HtmlWindow.OnCellClicked instead.
:ref:`base_OnCellMouseHover <no-15985>` Please use HtmlWindow.OnCellMouseHover instead.
:ref:`base_OnLinkClicked <no-15986>`    Please use HtmlWindow.OnLinkClicked instead.
:ref:`base_OnSetTitle <no-15987>`       Please use HtmlWindow.OnSetTitle instead.
:ref:`beforeInit <no-15988>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-15989>`   
:ref:`bindEvent <no-15990>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-15991>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-15992>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-15993>`          Makes this object topmost
:ref:`clear <no-15994>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-15995>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-15996>`  Given a position relative to this control, return a position relative
:ref:`copy <no-15997>`                  Implement the plain text version of copying
:ref:`cut <no-15998>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-15999>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-16000>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-16001>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-16002>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-16003>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-16004>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-16005>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-16006>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-16007>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-16008>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-16009>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-16010>`              Draws text on the object at the specified position
:ref:`endHover <no-16011>`              
:ref:`fitToSizer <no-16012>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-16013>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-16014>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-16015>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-16016>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-16017>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-16018>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-16019>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-16020>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-16021>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-16022>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-16023>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-16024>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-16025>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-16026>`                  Make the object invisible.
:ref:`initEvents <no-16027>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-16028>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-16029>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-16030>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-16031>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-16032>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-16033>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-16034>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-16035>`               
:ref:`paste <no-16036>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-16037>`           
:ref:`processDroppedFiles <no-16038>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-16039>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-16040>`            Raise the passed Dabo event.
:ref:`reCreate <no-16041>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-16042>`              Recreate the object.
:ref:`redraw <no-16043>`                Called when the object is (re)drawn.
:ref:`refresh <no-16044>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-16045>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-16046>`               Destroys the object.
:ref:`removeDrawnObject <no-16047>`     
:ref:`sendToBack <no-16048>`            Places this object behind all others.
:ref:`setAll <no-16049>`                Set all child object properties to the passed value.
:ref:`setFocus <no-16050>`              Sets focus to the object.
:ref:`setImageURLs <no-16051>`          Replace standard image file names with 'file:///img.pth' references
:ref:`setPositionInSizer <no-16052>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-16053>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-16054>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-16055>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-16056>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-16057>`                  Make the object visible.
:ref:`showContainingPage <no-16058>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-16059>`       Display a context menu (popup) at the specified position.
:ref:`super <no-16060>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-16061>`           Remove a previously registered event binding.
:ref:`unbindKey <no-16062>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-16063>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-16064>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-16065>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-15997:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.copy(self)

   Implement the plain text version of copying



-------

.. _no-16051:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setImageURLs(self, val)

   Replace standard image file names with 'file:///img.pth' references



-------


Methods - inherited
=====================

.. _no-15978:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15979:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-15980:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15981:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15982:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15983:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.autoBindEvents(self, force=True)
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

.. _no-15984:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.base_OnCellClicked(*args, \**kwargs)
   :noindex:


   Please use HtmlWindow.OnCellClicked instead.


Inherited from: 'wx.html.HtmlWindow - can not provide a link

-------

.. _no-15985:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.base_OnCellMouseHover(*args, \**kwargs)
   :noindex:


   Please use HtmlWindow.OnCellMouseHover instead.


Inherited from: 'wx.html.HtmlWindow - can not provide a link

-------

.. _no-15986:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.base_OnLinkClicked(*args, \**kwargs)
   :noindex:


   Please use HtmlWindow.OnLinkClicked instead.


Inherited from: 'wx.html.HtmlWindow - can not provide a link

-------

.. _no-15987:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.base_OnSetTitle(*args, \**kwargs)
   :noindex:


   Please use HtmlWindow.OnSetTitle instead.


Inherited from: 'wx.html.HtmlWindow - can not provide a link

-------

.. _no-15988:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15989:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15990:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15991:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15992:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-15993:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15994:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15995:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15996:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15998:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15999:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16000:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16001:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-16002:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16003:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16004:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16005:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16006:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16007:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16008:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16009:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16010:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16011:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16012:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16013:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16014:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16015:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16016:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16017:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16018:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16019:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16020:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16021:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16022:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16023:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-16024:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16025:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16026:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16027:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16028:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16029:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16030:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16031:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.lockDisplay(self)
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

.. _no-16032:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16033:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16034:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16035:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16036:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16037:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16038:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16039:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16040:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16041:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16042:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16043:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16044:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16045:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16046:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16047:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16048:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16049:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-16050:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16052:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16053:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-16054:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-16055:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16056:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16057:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16058:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16059:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16060:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16061:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16062:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16063:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16064:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16065:

.. function:: dabo.ui.uiwx.dHtmlBox.dHtmlBox.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
