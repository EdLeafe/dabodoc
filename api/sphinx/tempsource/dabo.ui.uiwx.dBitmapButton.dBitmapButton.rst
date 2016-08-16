
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBitmapButton

.. _dabo.ui.uiwx.dBitmapButton.dBitmapButton:

====================================================
|doc_title|  **dBitmapButton.dBitmapButton** - class
====================================================


Creates a button with a picture.

The button can have up to three pictures associated with it:

Picture: the normal picture shown on the button.
DownPicture: the picture displayed when the button is depressed.
FocusPicture: the picture displayed when the button has the focus.

Otherwise, dBitmapButton behaves the same as a normal dButton.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBitmapButton**

.. inheritance-diagram:: dBitmapButton


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`



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



   * - .. image:: _static/macWidgets/dBitmapButton.png
          :scale: 75 %
          :target: _static/macWidgets/dBitmapButton.png
          :alt: dBitmapButton



     - .. image:: _static/winWidgets/dBitmapButton.png
          :scale: 75 %
          :target: _static/winWidgets/dBitmapButton.png
          :alt: dBitmapButton



     - .. image:: _static/nixWidgets/dBitmapButton.png
          :scale: 75 %
          :target: _static/nixWidgets/dBitmapButton.png
          :alt: dBitmapButton


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBitmapButton.dBitmapButton

   .. automethod:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-34578>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-34579>`               Controls whether the button resizes when the Picture changes. (bool)
:ref:`BackColor <no-34580>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-34581>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-34582>`            Base key used when saving/restoring preferences  (str)
:ref:`Bitmap <no-34583>`                 The bitmap normally displayed on the button.  (wx.Bitmap)
:ref:`BitmapBorder <no-34584>`           Extra space around the bitmap, used when auto-sizing.  (int)
:ref:`BorderColor <no-34585>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-34586>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-34587>`            Specifies the type of border for this window. (String).
:ref:`BorderWidth <no-34588>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-34589>`                 The position of the bottom side of the object. This is a
:ref:`CancelButton <no-34590>`           Specifies whether this Bitmap button gets clicked on -Escape-.
:ref:`Caption <no-34591>`                The caption of the object. (str)
:ref:`Children <no-34592>`               Returns a list of object references to the children of
:ref:`Class <no-34593>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-34594>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-34595>`   Reference to the sizer item that control's this control's layout.
:ref:`DefaultButton <no-34596>`          Specifies whether this Bitmap button gets clicked on -Enter-.
:ref:`DownBitmap <no-34597>`             The bitmap displayed on the button when it is depressed.  (wx.Bitmap)
:ref:`DownPicture <no-34598>`            Specifies the image displayed on the button when it is depressed.  (str)
:ref:`DroppedFileHandler <no-34599>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-34600>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-34601>`        Dynamically determine the value of the AutoSize property.
:ref:`DynamicBackColor <no-34602>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBitmap <no-34603>`          Dynamically determine the value of the Bitmap property.
:ref:`DynamicBitmapBorder <no-34604>`    Dynamically determine the value of the BitmapBorder property.
:ref:`DynamicBorderColor <no-34605>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-34606>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-34607>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-34608>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCancelButton <no-34609>`    Dynamically determine the value of the CancelButton property.
:ref:`DynamicCaption <no-34610>`         Dynamically determine the value of the Caption property.
:ref:`DynamicDefaultButton <no-34611>`   Dynamically determine the value of the DefaultButton property.
:ref:`DynamicDownBitmap <no-34612>`      Dynamically determine the value of the DownBitmap property.
:ref:`DynamicDownPicture <no-34613>`     Dynamically determine the value of the DownPicture property.
:ref:`DynamicEnabled <no-34614>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFocusBitmap <no-34615>`     Dynamically determine the value of the FocusBitmap property.
:ref:`DynamicFocusPicture <no-34616>`    Dynamically determine the value of the FocusPicture property.
:ref:`DynamicFont <no-34617>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-34618>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-34619>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-34620>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-34621>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-34622>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-34623>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-34624>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-34625>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-34626>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPicture <no-34627>`         Dynamically determine the value of the Picture property.
:ref:`DynamicPosition <no-34628>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-34629>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-34630>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-34631>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-34632>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-34633>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-34634>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-34635>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-34636>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-34637>`                Specifies whether the object and children can get user input. (bool)
:ref:`FocusBitmap <no-34638>`            The bitmap displayed on the button when it receives focus.  (wx.Bitmap)
:ref:`FocusPicture <no-34639>`           Specifies the image displayed on the button when it receives focus.  (str)
:ref:`Font <no-34640>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-34641>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-34642>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-34643>`               Specifies the font face. (str)
:ref:`FontInfo <no-34644>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-34645>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-34646>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-34647>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-34648>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-34649>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-34650>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-34651>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-34652>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-34653>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-34654>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-34655>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-34656>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-34657>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-34658>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-34659>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-34660>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-34661>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-34662>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-34663>`               Specifies the base name of the object.
:ref:`Parent <no-34664>`                 The containing object. (obj)
:ref:`Picture <no-34665>`                Specifies the image normally displayed on the button.  This is the
:ref:`Position <no-34666>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-34667>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-34668>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-34669>`                  The position of the right side of the object. This is a
:ref:`Size <no-34670>`                   The size of the object. (tuple)
:ref:`Sizer <no-34671>`                  The sizer for the object.
:ref:`StatusText <no-34672>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-34673>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-34674>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-34675>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-34676>`                    The top position of the object. (int)
:ref:`Transparency <no-34677>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-34678>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-34679>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-34680>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-34681>`                  The width of the object. (int)
:ref:`WindowHandle <no-34682>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-34579:

**AutoSize** 

Controls whether the button resizes when the Picture changes. (bool)



-------

.. _no-34584:

**BitmapBorder** 

Extra space around the bitmap, used when auto-sizing.  (int)



-------

.. _no-34590:

**CancelButton** 

Specifies whether this Bitmap button gets clicked on -Escape-.



-------

.. _no-34596:

**DefaultButton** 

Specifies whether this Bitmap button gets clicked on -Enter-.



-------

.. _no-34597:

**DownBitmap** 

The bitmap displayed on the button when it is depressed.  (wx.Bitmap)



-------

.. _no-34598:

**DownPicture** 

Specifies the image displayed on the button when it is depressed.  (str)



-------

.. _no-34601:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.



-------

.. _no-34604:

**DynamicBitmapBorder** 

Dynamically determine the value of the BitmapBorder property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BitmapBorder property. If DynamicBitmapBorder is set to None (the default), BitmapBorder
will not be dynamically evaluated.



-------

.. _no-34609:

**DynamicCancelButton** 

Dynamically determine the value of the CancelButton property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CancelButton property. If DynamicCancelButton is set to None (the default), CancelButton
will not be dynamically evaluated.



-------

.. _no-34611:

**DynamicDefaultButton** 

Dynamically determine the value of the DefaultButton property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultButton property. If DynamicDefaultButton is set to None (the default), DefaultButton
will not be dynamically evaluated.



-------

.. _no-34612:

**DynamicDownBitmap** 

Dynamically determine the value of the DownBitmap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DownBitmap property. If DynamicDownBitmap is set to None (the default), DownBitmap
will not be dynamically evaluated.



-------

.. _no-34613:

**DynamicDownPicture** 

Dynamically determine the value of the DownPicture property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DownPicture property. If DynamicDownPicture is set to None (the default), DownPicture
will not be dynamically evaluated.



-------

.. _no-34615:

**DynamicFocusBitmap** 

Dynamically determine the value of the FocusBitmap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FocusBitmap property. If DynamicFocusBitmap is set to None (the default), FocusBitmap
will not be dynamically evaluated.



-------

.. _no-34616:

**DynamicFocusPicture** 

Dynamically determine the value of the FocusPicture property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FocusPicture property. If DynamicFocusPicture is set to None (the default), FocusPicture
will not be dynamically evaluated.



-------

.. _no-34638:

**FocusBitmap** 

The bitmap displayed on the button when it receives focus.  (wx.Bitmap)



-------

.. _no-34639:

**FocusPicture** 

Specifies the image displayed on the button when it receives focus.  (str)



-------


Properties - inherited
========================

.. _no-34578:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34580:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34581:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34582:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34583:

**Bitmap** 

The bitmap normally displayed on the button.  (wx.Bitmap)


Inherited from: :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`

-------

.. _no-34585:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34586:

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

.. _no-34587:

**BorderStyle** 

Specifies the type of border for this window. (String).

        Possible choices are:
            "None" - No border
            "Simple" - Border like a regular button
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34588:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34589:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34591:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34592:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34593:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34594:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34595:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34599:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34600:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34602:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34603:

**DynamicBitmap** 

Dynamically determine the value of the Bitmap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Bitmap property. If DynamicBitmap is set to None (the default), Bitmap
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`

-------

.. _no-34605:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34606:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34607:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34608:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34610:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34614:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34617:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34618:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34619:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34620:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34621:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34622:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34623:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34624:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34625:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34626:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34627:

**DynamicPicture** 

Dynamically determine the value of the Picture property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Picture property. If DynamicPicture is set to None (the default), Picture
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`

-------

.. _no-34628:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34629:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34630:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34631:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34632:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34633:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34634:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34635:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34636:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34637:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34640:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34641:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34642:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34643:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34644:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34645:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34646:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34647:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34648:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34649:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34650:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34651:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34652:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34653:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34654:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34655:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34656:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34657:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34658:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34659:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34660:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34661:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34662:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34663:

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

.. _no-34664:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34665:

**Picture** 

Specifies the image normally displayed on the button.  This is the
default if none of the other Picture properties are
specified.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`

-------

.. _no-34666:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34667:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34668:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34669:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34670:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34671:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34672:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34673:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-34674:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34675:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34676:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34677:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34678:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34679:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34680:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34681:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34682:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-34683>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-34684>`                 Occurs after the control or form is created.
:ref:`Destroy <no-34685>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-34686>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-34687>`               Occurs when the control gets the focus.
:ref:`Hit <no-34688>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-34689>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-34690>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-34691>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-34692>`               
:ref:`KeyUp <no-34693>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-34694>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-34695>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-34696>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-34697>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-34698>`             
:ref:`MouseLeave <no-34699>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-34700>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-34701>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-34702>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-34703>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-34704>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-34705>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-34706>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-34707>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-34708>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-34709>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-34710>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-34711>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-34712>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-34713>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-34714>`                   Occurs when the control's position changes.
:ref:`Paint <no-34715>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-34716>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-34717>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-34718>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-34719>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-34683:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-34684:

**Create** 

Occurs after the control or form is created.



-------

.. _no-34685:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-34686:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-34687:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-34688:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-34689:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-34690:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-34691:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-34692:

**KeyEvent** 



-------

.. _no-34693:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-34694:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-34695:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-34696:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-34697:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-34698:

**MouseEvent** 



-------

.. _no-34699:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-34700:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-34701:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-34702:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-34703:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-34704:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-34705:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-34706:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-34707:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-34708:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-34709:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-34710:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-34711:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-34712:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-34713:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-34714:

**Move** 

Occurs when the control's position changes.



-------

.. _no-34715:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-34716:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-34717:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-34718:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-34719:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-34720>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-34721>`             Instantiate object as a child of self.
:ref:`afterInit <no-34722>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-34723>`          
:ref:`afterSetProperties <no-34724>`    
:ref:`autoBindEvents <no-34725>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-34726>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-34727>`   
:ref:`bindEvent <no-34728>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-34729>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-34730>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-34731>`          Makes this object topmost
:ref:`clear <no-34732>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-34733>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-34734>`  Given a position relative to this control, return a position relative
:ref:`copy <no-34735>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-34736>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-34737>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-34738>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-34739>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-34740>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-34741>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-34742>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-34743>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-34744>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-34745>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-34746>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-34747>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-34748>`              Draws text on the object at the specified position
:ref:`endHover <no-34749>`              
:ref:`fitToSizer <no-34750>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-34751>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-34752>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-34753>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-34754>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-34755>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-34756>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-34757>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-34758>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-34759>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-34760>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-34761>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-34762>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-34763>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-34764>`                  Make the object invisible.
:ref:`initEvents <no-34765>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-34766>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-34767>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-34768>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-34769>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-34770>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-34771>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-34772>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-34773>`               
:ref:`paste <no-34774>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-34775>`           
:ref:`processDroppedFiles <no-34776>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-34777>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-34778>`            Raise the passed Dabo event.
:ref:`reCreate <no-34779>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-34780>`              Recreate the object.
:ref:`redraw <no-34781>`                Called when the object is (re)drawn.
:ref:`refresh <no-34782>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-34783>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-34784>`               Destroys the object.
:ref:`removeDrawnObject <no-34785>`     
:ref:`sendToBack <no-34786>`            Places this object behind all others.
:ref:`setAll <no-34787>`                Set all child object properties to the passed value.
:ref:`setFocus <no-34788>`              Sets focus to the object.
:ref:`setPositionInSizer <no-34789>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-34790>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-34791>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-34792>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-34793>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-34794>`                  Make the object visible.
:ref:`showContainingPage <no-34795>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-34796>`       Display a context menu (popup) at the specified position.
:ref:`super <no-34797>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-34798>`           Remove a previously registered event binding.
:ref:`unbindKey <no-34799>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-34800>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-34801>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-34802>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-34720:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34721:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-34722:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34723:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34724:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34725:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.autoBindEvents(self, force=True)
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

.. _no-34726:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34727:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34728:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34729:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34730:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-34731:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34732:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34733:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34734:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34735:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34736:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34737:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34738:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34739:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-34740:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34741:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34742:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34743:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34744:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34745:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34746:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34747:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34748:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34749:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34750:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34751:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34752:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34753:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34754:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34755:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34756:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34757:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34758:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34759:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34760:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34761:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-34762:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34763:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34764:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34765:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34766:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34767:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34768:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34769:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.lockDisplay(self)
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

.. _no-34770:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34771:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34772:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34773:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34774:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34775:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34776:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34777:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34778:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34779:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34780:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34781:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34782:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34783:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34784:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34785:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34786:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34787:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-34788:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34789:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34790:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-34791:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-34792:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34793:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34794:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34795:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34796:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34797:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34798:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34799:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34800:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34801:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34802:

.. function:: dabo.ui.uiwx.dBitmapButton.dBitmapButton.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
