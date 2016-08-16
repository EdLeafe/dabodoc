
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSlider

.. _dabo.ui.uiwx.dSlider.dSlider:

========================================
|doc_title|  **dSlider.dSlider** - class
========================================


Creates a slider control, allowing editing integer values. Unlike dSpinner,
dSlider does not allow entering a value with the keyboard.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSlider**

.. inheritance-diagram:: dSlider


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`



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



   * - .. image:: _static/macWidgets/dSlider.png
          :scale: 75 %
          :target: _static/macWidgets/dSlider.png
          :alt: dSlider



     - .. image:: _static/winWidgets/dSlider.png
          :scale: 75 %
          :target: _static/winWidgets/dSlider.png
          :alt: dSlider



     - .. image:: _static/nixWidgets/dSlider.png
          :scale: 75 %
          :target: _static/nixWidgets/dSlider.png
          :alt: dSlider


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSlider.dSlider

   .. automethod:: dabo.ui.uiwx.dSlider.dSlider.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-10774>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-10775>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-10776>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-10777>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-10778>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-10779>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-10780>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-10781>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-10782>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-10783>`                  The caption of the object. (str)
:ref:`Children <no-10784>`                 Returns a list of object references to the children of
:ref:`Class <no-10785>`                    The class the object is based on. Read-only.  (class)
:ref:`Continuous <no-10786>`               When True, the Hit event is raised as the slider moves. When False (default),
:ref:`ControllingSizer <no-10787>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-10788>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-10789>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-10790>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-10791>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-10792>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-10793>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-10794>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-10795>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-10796>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-10797>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-10798>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-10799>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-10800>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-10801>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-10802>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-10803>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-10804>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-10805>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-10806>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-10807>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-10808>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-10809>`              Dynamically determine the value of the Left property.
:ref:`DynamicMax <no-10810>`               Dynamically determine the value of the Max property.
:ref:`DynamicMin <no-10811>`               Dynamically determine the value of the Min property.
:ref:`DynamicMousePointer <no-10812>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicOrientation <no-10813>`       Dynamically determine the value of the Orientation property.
:ref:`DynamicPosition <no-10814>`          Dynamically determine the value of the Position property.
:ref:`DynamicShowLabels <no-10815>`        Dynamically determine the value of the ShowLabels property.
:ref:`DynamicSize <no-10816>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-10817>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-10818>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-10819>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-10820>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-10821>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-10822>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-10823>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-10824>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-10825>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-10826>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-10827>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-10828>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-10829>`                 Specifies the font face. (str)
:ref:`FontInfo <no-10830>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-10831>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-10832>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-10833>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-10834>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-10835>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-10836>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-10837>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-10838>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-10839>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-10840>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-10841>`                Specifies which events to log.  (list of strings)
:ref:`Max <no-10842>`                      Specifies the maximum value for the Slider. Default=100  (int)
:ref:`MaximumHeight <no-10843>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-10844>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-10845>`             Maximum allowable width for the control in pixels.  (int)
:ref:`Min <no-10846>`                      Specifies the minimum value for the Slider. Default=0  (int)
:ref:`MinimumHeight <no-10847>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-10848>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-10849>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-10850>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-10851>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-10852>`                 Specifies the base name of the object.
:ref:`Orientation <no-10853>`              Specifies whether the Slider is displayed as Horizontal or Vertical.
:ref:`Parent <no-10854>`                   The containing object. (obj)
:ref:`PersistSecretData <no-10855>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-10856>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-10857>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-10858>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Reversed <no-10859>`                 When True, the position of the Min and Max values are reversed. Must be set
:ref:`Right <no-10860>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-10861>`         Specifies whether the Value of the control gets saved when
:ref:`ShowLabels <no-10862>`               Specifies if the labels are shown on the slider. Must be set when the object is
:ref:`Size <no-10863>`                     The size of the object. (tuple)
:ref:`Sizer <no-10864>`                    The sizer for the object.
:ref:`Source <no-10865>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-10866>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-10867>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-10868>`                      A property that user code can safely use for specific purposes.
:ref:`TickPosition <no-10869>`             Position of the tick marks; must be one of Top, Bottom (default), Left or Right.
:ref:`ToolTipText <no-10870>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-10871>`                      The top position of the object. (int)
:ref:`Transparency <no-10872>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-10873>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-10874>`                    Specifies the current state of the control (the value of the field).  (varies)
:ref:`Visible <no-10875>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-10876>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-10877>`                    The width of the object. (int)
:ref:`WindowHandle <no-10878>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-10786:

**Continuous** 

When True, the Hit event is raised as the slider moves. When False (default),
    it is only raised when the thumb control is released.  (bool)



-------

.. _no-10810:

**DynamicMax** 

Dynamically determine the value of the Max property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Max property. If DynamicMax is set to None (the default), Max
will not be dynamically evaluated.



-------

.. _no-10811:

**DynamicMin** 

Dynamically determine the value of the Min property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Min property. If DynamicMin is set to None (the default), Min
will not be dynamically evaluated.



-------

.. _no-10813:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-10815:

**DynamicShowLabels** 

Dynamically determine the value of the ShowLabels property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowLabels property. If DynamicShowLabels is set to None (the default), ShowLabels
will not be dynamically evaluated.



-------

.. _no-10853:

**Orientation** 

Specifies whether the Slider is displayed as Horizontal or Vertical.
    Default='Horizontal'  (str)



-------

.. _no-10859:

**Reversed** 

When True, the position of the Min and Max values are reversed. Must be set
    when the object is created; setting it afterwards has no effect. Default=False  (bool)



-------

.. _no-10862:

**ShowLabels** 

Specifies if the labels are shown on the slider. Must be set when the object is
    created; setting it afterwards has no effect. Default=True  (bool)



-------

.. _no-10869:

**TickPosition** 

Position of the tick marks; must be one of Top, Bottom (default), Left or Right.
    Not fully supported on all platforms. Must be set during object creation; has no
    effect once created.  (str)



-------


Properties - inherited
========================

.. _no-10774:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10775:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10776:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10777:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10778:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10779:

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

.. _no-10780:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10781:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10782:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10783:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10784:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10785:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10787:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10788:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10789:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10790:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10791:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10792:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10793:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10794:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10795:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10796:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10797:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10798:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10799:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10800:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10801:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10802:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10803:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10804:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10805:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10806:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10807:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10808:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10809:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10812:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10814:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10816:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10817:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10818:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10819:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10820:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10821:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10822:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-10823:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10824:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10825:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10826:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10827:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10828:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10829:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10830:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10831:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10832:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10833:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10834:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10835:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10836:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10837:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10838:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10839:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10840:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10841:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10842:

**Max** 

Specifies the maximum value for the Slider. Default=100  (int)


Inherited from: 'wx._controls.Slider - can not provide a link

-------

.. _no-10843:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10844:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10845:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10846:

**Min** 

Specifies the minimum value for the Slider. Default=0  (int)


Inherited from: 'wx._controls.Slider - can not provide a link

-------

.. _no-10847:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10848:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10849:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10850:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10851:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10852:

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

.. _no-10854:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10855:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10856:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10857:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10858:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10860:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10861:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10863:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10864:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10865:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10866:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10867:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-10868:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10870:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10871:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10872:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10873:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10874:

**Value** 

Specifies the current state of the control (the value of the field).  (varies)


Inherited from: 'wx._controls.Slider - can not provide a link

-------

.. _no-10875:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10876:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10877:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10878:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-10879>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-10880>`                 Occurs after the control or form is created.
:ref:`Destroy <no-10881>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-10882>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-10883>`               Occurs when the control gets the focus.
:ref:`Hit <no-10884>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-10885>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-10886>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-10887>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-10888>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-10889>`               
:ref:`KeyUp <no-10890>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-10891>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-10892>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-10893>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-10894>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-10895>`             
:ref:`MouseLeave <no-10896>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-10897>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-10898>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-10899>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-10900>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-10901>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-10902>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-10903>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-10904>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-10905>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-10906>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-10907>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-10908>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-10909>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-10910>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-10911>`                   Occurs when the control's position changes.
:ref:`Paint <no-10912>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-10913>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-10914>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-10915>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-10916>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-10917>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-10879:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-10880:

**Create** 

Occurs after the control or form is created.



-------

.. _no-10881:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-10882:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-10883:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-10884:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-10885:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-10886:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-10887:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-10888:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-10889:

**KeyEvent** 



-------

.. _no-10890:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-10891:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-10892:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-10893:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-10894:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-10895:

**MouseEvent** 



-------

.. _no-10896:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-10897:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-10898:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-10899:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-10900:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-10901:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-10902:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-10903:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-10904:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-10905:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-10906:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-10907:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-10908:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-10909:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-10910:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-10911:

**Move** 

Occurs when the control's position changes.



-------

.. _no-10912:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-10913:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-10914:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-10915:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-10916:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-10917:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-10918>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-10919>`             Instantiate object as a child of self.
:ref:`afterInit <no-10920>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-10921>`          
:ref:`afterSetProperties <no-10922>`    
:ref:`autoBindEvents <no-10923>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-10924>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-10925>`   
:ref:`bindEvent <no-10926>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-10927>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-10928>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-10929>`          Makes this object topmost
:ref:`clear <no-10930>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-10931>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-10932>`  Given a position relative to this control, return a position relative
:ref:`copy <no-10933>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-10934>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-10935>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-10936>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-10937>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-10938>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-10939>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-10940>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-10941>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-10942>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-10943>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-10944>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-10945>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-10946>`              Draws text on the object at the specified position
:ref:`endHover <no-10947>`              
:ref:`fitToSizer <no-10948>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-10949>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-10950>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-10951>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-10952>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-10953>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-10954>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-10955>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-10956>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-10957>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-10958>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-10959>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-10960>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-10961>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-10962>`      
:ref:`getSizerProp <no-10963>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-10964>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-10965>`                  Make the object invisible.
:ref:`initEvents <no-10966>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-10967>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-10968>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-10969>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-10970>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-10971>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-10972>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-10973>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-10974>`               
:ref:`paste <no-10975>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-10976>`           
:ref:`processDroppedFiles <no-10977>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-10978>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-10979>`            Raise the passed Dabo event.
:ref:`reCreate <no-10980>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-10981>`              Recreate the object.
:ref:`redraw <no-10982>`                Called when the object is (re)drawn.
:ref:`refresh <no-10983>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-10984>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-10985>`               Destroys the object.
:ref:`removeDrawnObject <no-10986>`     
:ref:`restoreValue <no-10987>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-10988>`             Save control's value to dApp's user settings table.
:ref:`select <no-10989>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-10990>`             Select all text in the control.
:ref:`selectNone <no-10991>`            Select no text in the control.
:ref:`sendToBack <no-10992>`            Places this object behind all others.
:ref:`setAll <no-10993>`                Set all child object properties to the passed value.
:ref:`setFocus <no-10994>`              Sets focus to the object.
:ref:`setPositionInSizer <no-10995>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-10996>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-10997>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-10998>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-10999>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-11000>`                  Make the object visible.
:ref:`showContainingPage <no-11001>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-11002>`       Display a context menu (popup) at the specified position.
:ref:`super <no-11003>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-11004>`           Remove a previously registered event binding.
:ref:`unbindKey <no-11005>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-11006>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-11007>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-11008>`                Update control's value to match the current value from the source.

======================================= ========================


Methods - inherited
=====================

.. _no-10918:

.. function:: dabo.ui.uiwx.dSlider.dSlider.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10919:

.. function:: dabo.ui.uiwx.dSlider.dSlider.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-10920:

.. function:: dabo.ui.uiwx.dSlider.dSlider.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10921:

.. function:: dabo.ui.uiwx.dSlider.dSlider.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10922:

.. function:: dabo.ui.uiwx.dSlider.dSlider.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10923:

.. function:: dabo.ui.uiwx.dSlider.dSlider.autoBindEvents(self, force=True)
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

.. _no-10924:

.. function:: dabo.ui.uiwx.dSlider.dSlider.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10925:

.. function:: dabo.ui.uiwx.dSlider.dSlider.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10926:

.. function:: dabo.ui.uiwx.dSlider.dSlider.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10927:

.. function:: dabo.ui.uiwx.dSlider.dSlider.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10928:

.. function:: dabo.ui.uiwx.dSlider.dSlider.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-10929:

.. function:: dabo.ui.uiwx.dSlider.dSlider.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10930:

.. function:: dabo.ui.uiwx.dSlider.dSlider.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10931:

.. function:: dabo.ui.uiwx.dSlider.dSlider.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10932:

.. function:: dabo.ui.uiwx.dSlider.dSlider.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10933:

.. function:: dabo.ui.uiwx.dSlider.dSlider.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10934:

.. function:: dabo.ui.uiwx.dSlider.dSlider.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10935:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10936:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10937:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-10938:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10939:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10940:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10941:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10942:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10943:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10944:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10945:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10946:

.. function:: dabo.ui.uiwx.dSlider.dSlider.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10947:

.. function:: dabo.ui.uiwx.dSlider.dSlider.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10948:

.. function:: dabo.ui.uiwx.dSlider.dSlider.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10949:

.. function:: dabo.ui.uiwx.dSlider.dSlider.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10950:

.. function:: dabo.ui.uiwx.dSlider.dSlider.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10951:

.. function:: dabo.ui.uiwx.dSlider.dSlider.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10952:

.. function:: dabo.ui.uiwx.dSlider.dSlider.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10953:

.. function:: dabo.ui.uiwx.dSlider.dSlider.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10954:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10955:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10956:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10957:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10958:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10959:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10960:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10961:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-10962:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10963:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10964:

.. function:: dabo.ui.uiwx.dSlider.dSlider.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10965:

.. function:: dabo.ui.uiwx.dSlider.dSlider.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10966:

.. function:: dabo.ui.uiwx.dSlider.dSlider.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10967:

.. function:: dabo.ui.uiwx.dSlider.dSlider.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10968:

.. function:: dabo.ui.uiwx.dSlider.dSlider.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10969:

.. function:: dabo.ui.uiwx.dSlider.dSlider.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10970:

.. function:: dabo.ui.uiwx.dSlider.dSlider.lockDisplay(self)
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

.. _no-10971:

.. function:: dabo.ui.uiwx.dSlider.dSlider.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10972:

.. function:: dabo.ui.uiwx.dSlider.dSlider.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10973:

.. function:: dabo.ui.uiwx.dSlider.dSlider.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10974:

.. function:: dabo.ui.uiwx.dSlider.dSlider.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10975:

.. function:: dabo.ui.uiwx.dSlider.dSlider.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10976:

.. function:: dabo.ui.uiwx.dSlider.dSlider.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10977:

.. function:: dabo.ui.uiwx.dSlider.dSlider.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10978:

.. function:: dabo.ui.uiwx.dSlider.dSlider.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10979:

.. function:: dabo.ui.uiwx.dSlider.dSlider.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10980:

.. function:: dabo.ui.uiwx.dSlider.dSlider.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10981:

.. function:: dabo.ui.uiwx.dSlider.dSlider.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10982:

.. function:: dabo.ui.uiwx.dSlider.dSlider.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10983:

.. function:: dabo.ui.uiwx.dSlider.dSlider.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10984:

.. function:: dabo.ui.uiwx.dSlider.dSlider.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10985:

.. function:: dabo.ui.uiwx.dSlider.dSlider.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10986:

.. function:: dabo.ui.uiwx.dSlider.dSlider.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10987:

.. function:: dabo.ui.uiwx.dSlider.dSlider.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10988:

.. function:: dabo.ui.uiwx.dSlider.dSlider.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-10989:

.. function:: dabo.ui.uiwx.dSlider.dSlider.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-10990:

.. function:: dabo.ui.uiwx.dSlider.dSlider.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-10991:

.. function:: dabo.ui.uiwx.dSlider.dSlider.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-10992:

.. function:: dabo.ui.uiwx.dSlider.dSlider.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10993:

.. function:: dabo.ui.uiwx.dSlider.dSlider.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-10994:

.. function:: dabo.ui.uiwx.dSlider.dSlider.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10995:

.. function:: dabo.ui.uiwx.dSlider.dSlider.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10996:

.. function:: dabo.ui.uiwx.dSlider.dSlider.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-10997:

.. function:: dabo.ui.uiwx.dSlider.dSlider.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-10998:

.. function:: dabo.ui.uiwx.dSlider.dSlider.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10999:

.. function:: dabo.ui.uiwx.dSlider.dSlider.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11000:

.. function:: dabo.ui.uiwx.dSlider.dSlider.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11001:

.. function:: dabo.ui.uiwx.dSlider.dSlider.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11002:

.. function:: dabo.ui.uiwx.dSlider.dSlider.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11003:

.. function:: dabo.ui.uiwx.dSlider.dSlider.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11004:

.. function:: dabo.ui.uiwx.dSlider.dSlider.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11005:

.. function:: dabo.ui.uiwx.dSlider.dSlider.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11006:

.. function:: dabo.ui.uiwx.dSlider.dSlider.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11007:

.. function:: dabo.ui.uiwx.dSlider.dSlider.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11008:

.. function:: dabo.ui.uiwx.dSlider.dSlider.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
