
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dLabel

.. _dabo.ui.uiwx.dLabel.dLabel:

======================================
|doc_title|  **dLabel.dLabel** - class
======================================

Creates a static label, to make a caption for another control, for example.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dLabel**

.. inheritance-diagram:: dLabel


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.alignmentMixin.AlignmentMixin`
* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Page.SelectLabel`
* :ref:`dabo.lib.datanav.Page.SortLabel`
* :ref:`dabo.ui.dialogs.infoMessage.LblMessage`
* :ref:`dabo.ui.dialogs.login.Lbl`
* :ref:`dabo.ui.dialogs.login.LblMessage`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dLabel.png
          :scale: 75 %
          :target: _static/macWidgets/dLabel.png
          :alt: dLabel



     - .. image:: _static/winWidgets/dLabel.png
          :scale: 75 %
          :target: _static/winWidgets/dLabel.png
          :alt: dLabel



     - .. image:: _static/nixWidgets/dLabel.png
          :scale: 75 %
          :target: _static/nixWidgets/dLabel.png
          :alt: dLabel


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dLabel.dLabel

   .. automethod:: dabo.ui.uiwx.dLabel.dLabel.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-34803>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoResize <no-34804>`             Specifies whether the length of the caption determines
:ref:`BackColor <no-34805>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-34806>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-34807>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-34808>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-34809>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-34810>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-34811>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-34812>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-34813>`                The caption of the object. (str)
:ref:`Children <no-34814>`               Returns a list of object references to the children of
:ref:`Class <no-34815>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-34816>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-34817>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-34818>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-34819>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-34820>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-34821>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-34822>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-34823>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-34824>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-34825>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-34826>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-34827>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-34828>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-34829>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-34830>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-34831>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-34832>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-34833>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-34834>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-34835>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-34836>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-34837>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-34838>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-34839>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-34840>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-34841>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-34842>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-34843>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-34844>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-34845>`           Dynamically determine the value of the Width property.
:ref:`DynamicWordWrap <no-34846>`        Dynamically determine the value of the WordWrap property.
:ref:`Enabled <no-34847>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-34848>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-34849>`               Sets the Bold of the Font (int)
:ref:`FontDescription <no-34850>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-34851>`               Sets the face of the Font (int)
:ref:`FontInfo <no-34852>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-34853>`             Sets the Italic of the Font (int)
:ref:`FontSize <no-34854>`               Sets the size of the Font (int)
:ref:`FontUnderline <no-34855>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-34856>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-34857>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-34858>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-34859>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-34860>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-34861>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-34862>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-34863>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-34864>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-34865>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-34866>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-34867>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-34868>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-34869>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-34870>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-34871>`               Specifies the base name of the object.
:ref:`Parent <no-34872>`                 The containing object. (obj)
:ref:`Position <no-34873>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-34874>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-34875>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-34876>`                  The position of the right side of the object. This is a
:ref:`Size <no-34877>`                   The size of the object. (tuple)
:ref:`Sizer <no-34878>`                  The sizer for the object.
:ref:`StatusText <no-34879>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-34880>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-34881>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-34882>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-34883>`                    The top position of the object. (int)
:ref:`Transparency <no-34884>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-34885>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-34886>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-34887>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-34888>`                  The width of the object. (int)
:ref:`WindowHandle <no-34889>`           The platform-specific handle for the window. Read-only. (long)
:ref:`WordWrap <no-34890>`               When True, the Caption is wrapped to the Width. Note

======================================== ========================


Properties
==========

.. _no-34804:

**AutoResize** 

Specifies whether the length of the caption determines
    the size of the label. This cannot be True if WordWrap is
    also set to True. Default=True.  (bool)



-------

.. _no-34846:

**DynamicWordWrap** 

Dynamically determine the value of the WordWrap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WordWrap property. If DynamicWordWrap is set to None (the default), WordWrap
will not be dynamically evaluated.



-------

.. _no-34890:

**WordWrap** 

When True, the Caption is wrapped to the Width. Note
    that the control must have sufficient Height to display any
    wrapped text.
    Default=False  (bool)



-------


Properties - inherited
========================

.. _no-34803:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34805:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34806:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34807:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34808:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34809:

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

.. _no-34810:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34811:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34812:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34813:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34814:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34815:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34816:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34817:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34818:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34819:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34820:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34821:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34822:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34823:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34824:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34825:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34826:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34827:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34828:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34829:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34830:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34831:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34832:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34833:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34834:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34835:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34836:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34837:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34838:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34839:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34840:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34841:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34842:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34843:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34844:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34845:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34847:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34848:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34849:

**FontBold** 

Sets the Bold of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34850:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34851:

**FontFace** 

Sets the face of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34852:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34853:

**FontItalic** 

Sets the Italic of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34854:

**FontSize** 

Sets the size of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34855:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34856:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34857:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34858:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34859:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34860:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34861:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34862:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34863:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34864:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34865:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34866:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34867:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34868:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34869:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34870:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34871:

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

.. _no-34872:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34873:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34874:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34875:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34876:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34877:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34878:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34879:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34880:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-34881:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34882:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34883:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34884:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34885:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34886:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34887:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34888:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34889:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-34891>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-34892>`                 Occurs after the control or form is created.
:ref:`Destroy <no-34893>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-34894>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-34895>`               Occurs when the control gets the focus.
:ref:`Idle <no-34896>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-34897>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-34898>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-34899>`               
:ref:`KeyUp <no-34900>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-34901>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-34902>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-34903>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-34904>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-34905>`             
:ref:`MouseLeave <no-34906>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-34907>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-34908>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-34909>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-34910>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-34911>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-34912>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-34913>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-34914>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-34915>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-34916>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-34917>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-34918>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-34919>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-34920>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-34921>`                   Occurs when the control's position changes.
:ref:`Paint <no-34922>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-34923>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-34924>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-34925>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-34926>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-34891:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-34892:

**Create** 

Occurs after the control or form is created.



-------

.. _no-34893:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-34894:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-34895:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-34896:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-34897:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-34898:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-34899:

**KeyEvent** 



-------

.. _no-34900:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-34901:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-34902:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-34903:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-34904:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-34905:

**MouseEvent** 



-------

.. _no-34906:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-34907:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-34908:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-34909:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-34910:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-34911:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-34912:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-34913:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-34914:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-34915:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-34916:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-34917:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-34918:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-34919:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-34920:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-34921:

**Move** 

Occurs when the control's position changes.



-------

.. _no-34922:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-34923:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-34924:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-34925:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-34926:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-34927>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-34928>`             Instantiate object as a child of self.
:ref:`afterInit <no-34929>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-34930>`          
:ref:`afterSetProperties <no-34931>`    
:ref:`autoBindEvents <no-34932>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-34933>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-34934>`   
:ref:`bindEvent <no-34935>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-34936>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-34937>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-34938>`          Makes this object topmost
:ref:`clear <no-34939>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-34940>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-34941>`  Given a position relative to this control, return a position relative
:ref:`copy <no-34942>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-34943>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-34944>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-34945>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-34946>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-34947>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-34948>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-34949>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-34950>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-34951>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-34952>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-34953>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-34954>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-34955>`              Draws text on the object at the specified position
:ref:`endHover <no-34956>`              
:ref:`fitToSizer <no-34957>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-34958>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-34959>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-34960>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-34961>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-34962>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-34963>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-34964>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-34965>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-34966>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-34967>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-34968>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-34969>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-34970>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-34971>`                  Make the object invisible.
:ref:`initEvents <no-34972>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-34973>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-34974>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-34975>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-34976>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-34977>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-34978>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-34979>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-34980>`               
:ref:`paste <no-34981>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-34982>`           
:ref:`processDroppedFiles <no-34983>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-34984>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-34985>`            Raise the passed Dabo event.
:ref:`reCreate <no-34986>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-34987>`              Recreate the object.
:ref:`redraw <no-34988>`                Called when the object is (re)drawn.
:ref:`refresh <no-34989>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-34990>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-34991>`               Destroys the object.
:ref:`removeDrawnObject <no-34992>`     
:ref:`sendToBack <no-34993>`            Places this object behind all others.
:ref:`setAll <no-34994>`                Set all child object properties to the passed value.
:ref:`setFocus <no-34995>`              Sets focus to the object.
:ref:`setPositionInSizer <no-34996>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-34997>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-34998>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-34999>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-35000>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-35001>`                  Make the object visible.
:ref:`showContainingPage <no-35002>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-35003>`       Display a context menu (popup) at the specified position.
:ref:`super <no-35004>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-35005>`           Remove a previously registered event binding.
:ref:`unbindKey <no-35006>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-35007>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-35008>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-35009>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-34927:

.. function:: dabo.ui.uiwx.dLabel.dLabel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34928:

.. function:: dabo.ui.uiwx.dLabel.dLabel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-34929:

.. function:: dabo.ui.uiwx.dLabel.dLabel.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34930:

.. function:: dabo.ui.uiwx.dLabel.dLabel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34931:

.. function:: dabo.ui.uiwx.dLabel.dLabel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34932:

.. function:: dabo.ui.uiwx.dLabel.dLabel.autoBindEvents(self, force=True)
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

.. _no-34933:

.. function:: dabo.ui.uiwx.dLabel.dLabel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34934:

.. function:: dabo.ui.uiwx.dLabel.dLabel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34935:

.. function:: dabo.ui.uiwx.dLabel.dLabel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34936:

.. function:: dabo.ui.uiwx.dLabel.dLabel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34937:

.. function:: dabo.ui.uiwx.dLabel.dLabel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-34938:

.. function:: dabo.ui.uiwx.dLabel.dLabel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34939:

.. function:: dabo.ui.uiwx.dLabel.dLabel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34940:

.. function:: dabo.ui.uiwx.dLabel.dLabel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34941:

.. function:: dabo.ui.uiwx.dLabel.dLabel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34942:

.. function:: dabo.ui.uiwx.dLabel.dLabel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34943:

.. function:: dabo.ui.uiwx.dLabel.dLabel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34944:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34945:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34946:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-34947:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34948:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34949:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34950:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34951:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34952:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34953:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34954:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34955:

.. function:: dabo.ui.uiwx.dLabel.dLabel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34956:

.. function:: dabo.ui.uiwx.dLabel.dLabel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34957:

.. function:: dabo.ui.uiwx.dLabel.dLabel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34958:

.. function:: dabo.ui.uiwx.dLabel.dLabel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34959:

.. function:: dabo.ui.uiwx.dLabel.dLabel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34960:

.. function:: dabo.ui.uiwx.dLabel.dLabel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34961:

.. function:: dabo.ui.uiwx.dLabel.dLabel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34962:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34963:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34964:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34965:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34966:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34967:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34968:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-34969:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34970:

.. function:: dabo.ui.uiwx.dLabel.dLabel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34971:

.. function:: dabo.ui.uiwx.dLabel.dLabel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34972:

.. function:: dabo.ui.uiwx.dLabel.dLabel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34973:

.. function:: dabo.ui.uiwx.dLabel.dLabel.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34974:

.. function:: dabo.ui.uiwx.dLabel.dLabel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34975:

.. function:: dabo.ui.uiwx.dLabel.dLabel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34976:

.. function:: dabo.ui.uiwx.dLabel.dLabel.lockDisplay(self)
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

.. _no-34977:

.. function:: dabo.ui.uiwx.dLabel.dLabel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34978:

.. function:: dabo.ui.uiwx.dLabel.dLabel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34979:

.. function:: dabo.ui.uiwx.dLabel.dLabel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34980:

.. function:: dabo.ui.uiwx.dLabel.dLabel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34981:

.. function:: dabo.ui.uiwx.dLabel.dLabel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34982:

.. function:: dabo.ui.uiwx.dLabel.dLabel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34983:

.. function:: dabo.ui.uiwx.dLabel.dLabel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34984:

.. function:: dabo.ui.uiwx.dLabel.dLabel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34985:

.. function:: dabo.ui.uiwx.dLabel.dLabel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34986:

.. function:: dabo.ui.uiwx.dLabel.dLabel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34987:

.. function:: dabo.ui.uiwx.dLabel.dLabel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34988:

.. function:: dabo.ui.uiwx.dLabel.dLabel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34989:

.. function:: dabo.ui.uiwx.dLabel.dLabel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34990:

.. function:: dabo.ui.uiwx.dLabel.dLabel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34991:

.. function:: dabo.ui.uiwx.dLabel.dLabel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34992:

.. function:: dabo.ui.uiwx.dLabel.dLabel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34993:

.. function:: dabo.ui.uiwx.dLabel.dLabel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34994:

.. function:: dabo.ui.uiwx.dLabel.dLabel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-34995:

.. function:: dabo.ui.uiwx.dLabel.dLabel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34996:

.. function:: dabo.ui.uiwx.dLabel.dLabel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34997:

.. function:: dabo.ui.uiwx.dLabel.dLabel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-34998:

.. function:: dabo.ui.uiwx.dLabel.dLabel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-34999:

.. function:: dabo.ui.uiwx.dLabel.dLabel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35000:

.. function:: dabo.ui.uiwx.dLabel.dLabel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35001:

.. function:: dabo.ui.uiwx.dLabel.dLabel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35002:

.. function:: dabo.ui.uiwx.dLabel.dLabel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35003:

.. function:: dabo.ui.uiwx.dLabel.dLabel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35004:

.. function:: dabo.ui.uiwx.dLabel.dLabel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35005:

.. function:: dabo.ui.uiwx.dLabel.dLabel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35006:

.. function:: dabo.ui.uiwx.dLabel.dLabel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35007:

.. function:: dabo.ui.uiwx.dLabel.dLabel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35008:

.. function:: dabo.ui.uiwx.dLabel.dLabel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35009:

.. function:: dabo.ui.uiwx.dLabel.dLabel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
