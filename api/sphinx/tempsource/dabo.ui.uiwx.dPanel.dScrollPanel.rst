
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPanel

.. _dabo.ui.uiwx.dPanel.dScrollPanel:

============================================
|doc_title|  **dPanel.dScrollPanel** - class
============================================


This is a basic container for controls that allows scrolling.

Panels can contain subpanels to unlimited depth, making them quite
flexible for many uses. Consider laying out your forms on panels
instead, and then adding the panel to the form.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dScrollPanel**

.. inheritance-diagram:: dScrollPanel


|supclasses| Known Superclasses
===============================




|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.dialogs.WizardPage.WizardPage`
* :ref:`dabo.ui.uiwx.dPage.dPage`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dScrollPanel.png
          :scale: 75 %
          :target: _static/winWidgets/dScrollPanel.png
          :alt: dScrollPanel



     - .. image:: _static/nixWidgets/dScrollPanel.png
          :scale: 75 %
          :target: _static/nixWidgets/dScrollPanel.png
          :alt: dScrollPanel


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPanel.dScrollPanel

   .. automethod:: dabo.ui.uiwx.dPanel.dScrollPanel.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-13726>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-13727>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-13728>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-13729>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-13730>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-13731>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-13732>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-13733>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-13734>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-13735>`                 The caption of the object. (str)
:ref:`Children <no-13736>`                Child controls of this panel. This excludes the wx-specific
:ref:`Class <no-13737>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-13738>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-13739>`    Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-13740>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-13741>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-13742>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-13743>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-13744>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-13745>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-13746>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-13747>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-13748>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-13749>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-13750>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-13751>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-13752>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-13753>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-13754>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-13755>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-13756>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-13757>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicLeft <no-13758>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-13759>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-13760>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-13761>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-13762>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-13763>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-13764>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-13765>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-13766>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-13767>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-13768>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-13769>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-13770>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-13771>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-13772>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-13773>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-13774>`                Specifies the font face. (str)
:ref:`FontInfo <no-13775>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-13776>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-13777>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-13778>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-13779>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-13780>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-13781>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-13782>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-13783>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-13784>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-13785>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-13786>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-13787>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-13788>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-13789>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-13790>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-13791>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-13792>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-13793>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-13794>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-13795>`                Specifies the base name of the object.
:ref:`Parent <no-13796>`                  The containing object. (obj)
:ref:`Position <no-13797>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-13798>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-13799>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-13800>`                   The position of the right side of the object. This is a
:ref:`Size <no-13801>`                    The size of the object. (tuple)
:ref:`Sizer <no-13802>`                   The sizer for the object.
:ref:`StatusText <no-13803>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-13804>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-13805>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-13806>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-13807>`                     The top position of the object. (int)
:ref:`Transparency <no-13808>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-13809>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`VerticalScroll <no-13810>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-13811>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-13812>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-13813>`                   The width of the object. (int)
:ref:`WindowHandle <no-13814>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-13757:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.



-------

.. _no-13767:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.



-------

.. _no-13783:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)



-------

.. _no-13810:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)



-------


Properties - inherited
========================

.. _no-13726:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13727:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13728:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13729:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13730:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13731:

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

.. _no-13732:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13733:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13734:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13735:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13736:

**Children** 

Child controls of this panel. This excludes the wx-specific
    scroll bars  (list of objects)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13737:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13738:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13739:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13740:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13741:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13742:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13743:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13744:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13745:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13746:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13747:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13748:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13749:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13750:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13751:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13752:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13753:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13754:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13755:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13756:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13758:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13759:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13760:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13761:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13762:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13763:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13764:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13765:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13766:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13768:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13769:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13770:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13771:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13772:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13773:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13774:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13775:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13776:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13777:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13778:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13779:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13780:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13781:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13782:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13784:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13785:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13786:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13787:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13788:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13789:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13790:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13791:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13792:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13793:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13794:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13795:

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

.. _no-13796:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13797:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13798:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13799:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13800:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13801:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13802:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13803:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13804:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-13805:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13806:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13807:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13808:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13809:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13811:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13812:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13813:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13814:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-13815>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-13816>`                 Occurs after the control or form is created.
:ref:`Destroy <no-13817>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-13818>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-13819>`               Occurs when the control gets the focus.
:ref:`Idle <no-13820>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-13821>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-13822>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-13823>`               
:ref:`KeyUp <no-13824>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-13825>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-13826>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-13827>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-13828>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-13829>`             
:ref:`MouseLeave <no-13830>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-13831>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-13832>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-13833>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-13834>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-13835>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-13836>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-13837>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-13838>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-13839>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-13840>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-13841>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-13842>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-13843>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-13844>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-13845>`                   Occurs when the control's position changes.
:ref:`Paint <no-13846>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-13847>`                 Occurs when the control or form is resized.
:ref:`ScrollBottom <no-13848>`           Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-13849>`            
:ref:`ScrollLineDown <no-13850>`         Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-13851>`           Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-13852>`         Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-13853>`           Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-13854>`        Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-13855>`     Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-13856>`              Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-13857>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-13858>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-13859>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-13815:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-13816:

**Create** 

Occurs after the control or form is created.



-------

.. _no-13817:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-13818:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-13819:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-13820:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-13821:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-13822:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-13823:

**KeyEvent** 



-------

.. _no-13824:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-13825:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-13826:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-13827:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-13828:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-13829:

**MouseEvent** 



-------

.. _no-13830:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-13831:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-13832:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-13833:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-13834:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-13835:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-13836:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-13837:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-13838:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-13839:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-13840:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-13841:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-13842:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-13843:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-13844:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-13845:

**Move** 

Occurs when the control's position changes.



-------

.. _no-13846:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-13847:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-13848:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-13849:

**ScrollEvent** 



-------

.. _no-13850:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-13851:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-13852:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-13853:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-13854:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-13855:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-13856:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-13857:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-13858:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-13859:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-13860>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-13861>`             Instantiate object as a child of self.
:ref:`afterInit <no-13862>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-13863>`          
:ref:`afterSetProperties <no-13864>`    
:ref:`autoBindEvents <no-13865>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-13866>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-13867>`   
:ref:`bindEvent <no-13868>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-13869>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-13870>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-13871>`          Makes this object topmost
:ref:`clear <no-13872>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-13873>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-13874>`  Given a position relative to this control, return a position relative
:ref:`copy <no-13875>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-13876>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-13877>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-13878>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-13879>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-13880>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-13881>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-13882>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-13883>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-13884>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-13885>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-13886>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-13887>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-13888>`              Draws text on the object at the specified position
:ref:`endHover <no-13889>`              
:ref:`fitToSizer <no-13890>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-13891>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-13892>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-13893>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-13894>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-13895>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-13896>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-13897>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-13898>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-13899>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-13900>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-13901>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-13902>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-13903>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-13904>`                  Make the object invisible.
:ref:`initEvents <no-13905>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-13906>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-13907>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-13908>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-13909>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-13910>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-13911>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-13912>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-13913>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-13914>`               
:ref:`pageDown <no-13915>`              
:ref:`pageHorizontally <no-13916>`      Scroll horizontally one 'page' width.
:ref:`pageLeft <no-13917>`              
:ref:`pageRight <no-13918>`             
:ref:`pageUp <no-13919>`                
:ref:`pageVertically <no-13920>`        Scroll vertically one 'page' height.
:ref:`paste <no-13921>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-13922>`           
:ref:`processDroppedFiles <no-13923>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-13924>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-13925>`            Raise the passed Dabo event.
:ref:`reCreate <no-13926>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-13927>`              Recreate the object.
:ref:`redraw <no-13928>`                Called when the object is (re)drawn.
:ref:`refresh <no-13929>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-13930>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-13931>`               Destroys the object.
:ref:`removeDrawnObject <no-13932>`     
:ref:`scrollHorizontally <no-13933>`    Change the horizontal scroll position by 'amt' units.
:ref:`scrollVertically <no-13934>`      Change the vertical scroll position by 'amt' units.
:ref:`sendToBack <no-13935>`            Places this object behind all others.
:ref:`setAll <no-13936>`                Set all child object properties to the passed value.
:ref:`setFocus <no-13937>`              Sets focus to the object.
:ref:`setPositionInSizer <no-13938>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-13939>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-13940>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-13941>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-13942>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-13943>`                  Make the object visible.
:ref:`showContainingPage <no-13944>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-13945>`       Display a context menu (popup) at the specified position.
:ref:`super <no-13946>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-13947>`           Remove a previously registered event binding.
:ref:`unbindKey <no-13948>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-13949>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-13950>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-13951>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-13915:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.pageDown(self)



-------

.. _no-13916:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.pageHorizontally(self, direction)

   Scroll horizontally one 'page' width.



-------

.. _no-13917:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.pageLeft(self)



-------

.. _no-13918:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.pageRight(self)



-------

.. _no-13919:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.pageUp(self)



-------

.. _no-13920:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.pageVertically(self, direction)

   Scroll vertically one 'page' height.



-------

.. _no-13933:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.scrollHorizontally(self, amt)

   Change the horizontal scroll position by 'amt' units.



-------

.. _no-13934:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.scrollVertically(self, amt)

   Change the vertical scroll position by 'amt' units.



-------


Methods - inherited
=====================

.. _no-13860:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13861:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-13862:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13863:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13864:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13865:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.autoBindEvents(self, force=True)
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

.. _no-13866:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13867:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13868:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13869:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13870:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-13871:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13872:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13873:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13874:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13875:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13876:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13877:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13878:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13879:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-13880:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13881:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13882:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13883:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13884:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13885:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13886:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13887:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13888:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13889:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13890:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13891:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13892:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13893:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13894:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13895:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13896:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13897:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13898:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13899:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13900:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13901:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-13902:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13903:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13904:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13905:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13906:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13907:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13908:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13909:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-13910:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.lockDisplay(self)
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

.. _no-13911:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13912:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13913:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13914:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13921:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13922:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13923:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13924:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13925:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13926:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13927:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13928:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13929:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13930:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13931:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13932:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13935:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13936:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-13937:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13938:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13939:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-13940:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-13941:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13942:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13943:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13944:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13945:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13946:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13947:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13948:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13949:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13950:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13951:

.. function:: dabo.ui.uiwx.dPanel.dScrollPanel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
