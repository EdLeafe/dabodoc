
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dGauge

.. _dabo.ui.uiwx.dGauge.dGauge:

======================================
|doc_title|  **dGauge.dGauge** - class
======================================

Creates a gauge, which can be used as a progress bar.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dGauge**

.. inheritance-diagram:: dGauge


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



   * - .. image:: _static/macWidgets/dGauge.png
          :scale: 75 %
          :target: _static/macWidgets/dGauge.png
          :alt: dGauge



     - .. image:: _static/winWidgets/dGauge.png
          :scale: 75 %
          :target: _static/winWidgets/dGauge.png
          :alt: dGauge



     - .. image:: _static/nixWidgets/dGauge.png
          :scale: 75 %
          :target: _static/nixWidgets/dGauge.png
          :alt: dGauge


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dGauge.dGauge

   .. automethod:: dabo.ui.uiwx.dGauge.dGauge.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-12284>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-12285>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-12286>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-12287>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-12288>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-12289>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-12290>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-12291>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-12292>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-12293>`                The caption of the object. (str)
:ref:`Children <no-12294>`               Returns a list of object references to the children of
:ref:`Class <no-12295>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-12296>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-12297>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-12298>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-12299>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-12300>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-12301>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-12302>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-12303>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-12304>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-12305>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-12306>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-12307>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-12308>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-12309>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-12310>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-12311>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-12312>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-12313>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-12314>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-12315>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-12316>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicOrientation <no-12317>`     Dynamically determine the value of the Orientation property.
:ref:`DynamicPosition <no-12318>`        Dynamically determine the value of the Position property.
:ref:`DynamicRange <no-12319>`           Dynamically determine the value of the Range property.
:ref:`DynamicSize <no-12320>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-12321>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-12322>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-12323>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-12324>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-12325>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-12326>`           Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-12327>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-12328>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-12329>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-12330>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-12331>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-12332>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-12333>`               Specifies the font face. (str)
:ref:`FontInfo <no-12334>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-12335>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-12336>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-12337>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-12338>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-12339>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-12340>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-12341>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-12342>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-12343>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-12344>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-12345>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-12346>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-12347>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-12348>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-12349>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-12350>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-12351>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-12352>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-12353>`               Specifies the base name of the object.
:ref:`Orientation <no-12354>`            Specifies whether the gauge is displayed as Horizontal or Vertical.  (str)
:ref:`Parent <no-12355>`                 The containing object. (obj)
:ref:`Percentage <no-12356>`             Alternate way of setting/getting the Value, using percentage
:ref:`Position <no-12357>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-12358>`      Reference to the Preference Management object  (dPref)
:ref:`Range <no-12359>`                  Specifies the maximum value for the gauge.  (int)
:ref:`RegID <no-12360>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-12361>`                  The position of the right side of the object. This is a
:ref:`Size <no-12362>`                   The size of the object. (tuple)
:ref:`Sizer <no-12363>`                  The sizer for the object.
:ref:`StatusText <no-12364>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-12365>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-12366>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-12367>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-12368>`                    The top position of the object. (int)
:ref:`Transparency <no-12369>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-12370>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-12371>`                  Specifies the state of the gauge, relative to max value.
:ref:`Visible <no-12372>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-12373>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-12374>`                  The width of the object. (int)
:ref:`WindowHandle <no-12375>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-12317:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-12319:

**DynamicRange** 

Dynamically determine the value of the Range property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Range property. If DynamicRange is set to None (the default), Range
will not be dynamically evaluated.



-------

.. _no-12326:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.



-------

.. _no-12354:

**Orientation** 

Specifies whether the gauge is displayed as Horizontal or Vertical.  (str)



-------

.. _no-12356:

**Percentage** 

Alternate way of setting/getting the Value, using percentage
    of the Range.  (float)



-------


Properties - inherited
========================

.. _no-12284:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12285:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12286:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12287:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12288:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12289:

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

.. _no-12290:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12291:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12292:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12293:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12294:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12295:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12296:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12297:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12298:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12299:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12300:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12301:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12302:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12303:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12304:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12305:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12306:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12307:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12308:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12309:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12310:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12311:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12312:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12313:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12314:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12315:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12316:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12318:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12320:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12321:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12322:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12323:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12324:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12325:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12327:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12328:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12329:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12330:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12331:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12332:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12333:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12334:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12335:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12336:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12337:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12338:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12339:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12340:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12341:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12342:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12343:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12344:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12345:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12346:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12347:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12348:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12349:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12350:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12351:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12352:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12353:

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

.. _no-12355:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12357:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12358:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12359:

**Range** 

Specifies the maximum value for the gauge.  (int)


Inherited from: 'wx._controls.Gauge - can not provide a link

-------

.. _no-12360:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12361:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12362:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12363:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12364:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12365:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-12366:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12367:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12368:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12369:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12370:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12371:

**Value** 

Specifies the state of the gauge, relative to max value.


Inherited from: 'wx._controls.Gauge - can not provide a link

-------

.. _no-12372:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12373:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12374:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12375:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-12376>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-12377>`                 Occurs after the control or form is created.
:ref:`Destroy <no-12378>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-12379>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-12380>`               Occurs when the control gets the focus.
:ref:`Idle <no-12381>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-12382>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-12383>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-12384>`               
:ref:`KeyUp <no-12385>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-12386>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-12387>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-12388>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-12389>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-12390>`             
:ref:`MouseLeave <no-12391>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-12392>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-12393>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-12394>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-12395>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-12396>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-12397>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-12398>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-12399>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-12400>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-12401>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-12402>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-12403>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-12404>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-12405>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-12406>`                   Occurs when the control's position changes.
:ref:`Paint <no-12407>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-12408>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-12409>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-12410>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-12411>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-12376:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-12377:

**Create** 

Occurs after the control or form is created.



-------

.. _no-12378:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-12379:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-12380:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-12381:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-12382:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-12383:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-12384:

**KeyEvent** 



-------

.. _no-12385:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-12386:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-12387:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-12388:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-12389:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-12390:

**MouseEvent** 



-------

.. _no-12391:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-12392:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-12393:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-12394:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-12395:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-12396:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-12397:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-12398:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-12399:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-12400:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-12401:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-12402:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-12403:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-12404:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-12405:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-12406:

**Move** 

Occurs when the control's position changes.



-------

.. _no-12407:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-12408:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-12409:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-12410:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-12411:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-12412>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-12413>`             Instantiate object as a child of self.
:ref:`afterInit <no-12414>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-12415>`          
:ref:`afterSetProperties <no-12416>`    
:ref:`autoBindEvents <no-12417>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-12418>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-12419>`   
:ref:`bindEvent <no-12420>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-12421>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-12422>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-12423>`          Makes this object topmost
:ref:`clear <no-12424>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-12425>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-12426>`  Given a position relative to this control, return a position relative
:ref:`copy <no-12427>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-12428>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-12429>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-12430>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-12431>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-12432>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-12433>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-12434>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-12435>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-12436>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-12437>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-12438>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-12439>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-12440>`              Draws text on the object at the specified position
:ref:`endHover <no-12441>`              
:ref:`fitToSizer <no-12442>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-12443>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-12444>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-12445>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-12446>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-12447>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-12448>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-12449>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-12450>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-12451>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-12452>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-12453>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-12454>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-12455>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-12456>`                  Make the object invisible.
:ref:`initEvents <no-12457>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-12458>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-12459>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-12460>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-12461>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-12462>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-12463>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-12464>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-12465>`               
:ref:`paste <no-12466>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-12467>`           
:ref:`processDroppedFiles <no-12468>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-12469>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-12470>`            Raise the passed Dabo event.
:ref:`reCreate <no-12471>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-12472>`              Recreate the object.
:ref:`redraw <no-12473>`                Called when the object is (re)drawn.
:ref:`refresh <no-12474>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-12475>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-12476>`               Destroys the object.
:ref:`removeDrawnObject <no-12477>`     
:ref:`sendToBack <no-12478>`            Places this object behind all others.
:ref:`setAll <no-12479>`                Set all child object properties to the passed value.
:ref:`setFocus <no-12480>`              Sets focus to the object.
:ref:`setPositionInSizer <no-12481>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-12482>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-12483>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-12484>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-12485>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-12486>`                  Make the object visible.
:ref:`showContainingPage <no-12487>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-12488>`       Display a context menu (popup) at the specified position.
:ref:`super <no-12489>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-12490>`           Remove a previously registered event binding.
:ref:`unbindKey <no-12491>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-12492>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-12493>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-12494>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-12412:

.. function:: dabo.ui.uiwx.dGauge.dGauge.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12413:

.. function:: dabo.ui.uiwx.dGauge.dGauge.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-12414:

.. function:: dabo.ui.uiwx.dGauge.dGauge.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12415:

.. function:: dabo.ui.uiwx.dGauge.dGauge.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12416:

.. function:: dabo.ui.uiwx.dGauge.dGauge.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12417:

.. function:: dabo.ui.uiwx.dGauge.dGauge.autoBindEvents(self, force=True)
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

.. _no-12418:

.. function:: dabo.ui.uiwx.dGauge.dGauge.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12419:

.. function:: dabo.ui.uiwx.dGauge.dGauge.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12420:

.. function:: dabo.ui.uiwx.dGauge.dGauge.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12421:

.. function:: dabo.ui.uiwx.dGauge.dGauge.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12422:

.. function:: dabo.ui.uiwx.dGauge.dGauge.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-12423:

.. function:: dabo.ui.uiwx.dGauge.dGauge.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12424:

.. function:: dabo.ui.uiwx.dGauge.dGauge.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12425:

.. function:: dabo.ui.uiwx.dGauge.dGauge.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12426:

.. function:: dabo.ui.uiwx.dGauge.dGauge.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12427:

.. function:: dabo.ui.uiwx.dGauge.dGauge.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12428:

.. function:: dabo.ui.uiwx.dGauge.dGauge.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12429:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12430:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12431:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-12432:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12433:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12434:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12435:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12436:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12437:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12438:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12439:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12440:

.. function:: dabo.ui.uiwx.dGauge.dGauge.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12441:

.. function:: dabo.ui.uiwx.dGauge.dGauge.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12442:

.. function:: dabo.ui.uiwx.dGauge.dGauge.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12443:

.. function:: dabo.ui.uiwx.dGauge.dGauge.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12444:

.. function:: dabo.ui.uiwx.dGauge.dGauge.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12445:

.. function:: dabo.ui.uiwx.dGauge.dGauge.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12446:

.. function:: dabo.ui.uiwx.dGauge.dGauge.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12447:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12448:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12449:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12450:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12451:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12452:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12453:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-12454:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12455:

.. function:: dabo.ui.uiwx.dGauge.dGauge.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12456:

.. function:: dabo.ui.uiwx.dGauge.dGauge.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12457:

.. function:: dabo.ui.uiwx.dGauge.dGauge.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12458:

.. function:: dabo.ui.uiwx.dGauge.dGauge.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12459:

.. function:: dabo.ui.uiwx.dGauge.dGauge.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12460:

.. function:: dabo.ui.uiwx.dGauge.dGauge.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12461:

.. function:: dabo.ui.uiwx.dGauge.dGauge.lockDisplay(self)
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

.. _no-12462:

.. function:: dabo.ui.uiwx.dGauge.dGauge.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12463:

.. function:: dabo.ui.uiwx.dGauge.dGauge.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12464:

.. function:: dabo.ui.uiwx.dGauge.dGauge.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12465:

.. function:: dabo.ui.uiwx.dGauge.dGauge.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12466:

.. function:: dabo.ui.uiwx.dGauge.dGauge.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12467:

.. function:: dabo.ui.uiwx.dGauge.dGauge.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12468:

.. function:: dabo.ui.uiwx.dGauge.dGauge.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12469:

.. function:: dabo.ui.uiwx.dGauge.dGauge.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12470:

.. function:: dabo.ui.uiwx.dGauge.dGauge.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12471:

.. function:: dabo.ui.uiwx.dGauge.dGauge.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12472:

.. function:: dabo.ui.uiwx.dGauge.dGauge.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12473:

.. function:: dabo.ui.uiwx.dGauge.dGauge.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12474:

.. function:: dabo.ui.uiwx.dGauge.dGauge.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12475:

.. function:: dabo.ui.uiwx.dGauge.dGauge.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12476:

.. function:: dabo.ui.uiwx.dGauge.dGauge.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12477:

.. function:: dabo.ui.uiwx.dGauge.dGauge.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12478:

.. function:: dabo.ui.uiwx.dGauge.dGauge.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12479:

.. function:: dabo.ui.uiwx.dGauge.dGauge.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-12480:

.. function:: dabo.ui.uiwx.dGauge.dGauge.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12481:

.. function:: dabo.ui.uiwx.dGauge.dGauge.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12482:

.. function:: dabo.ui.uiwx.dGauge.dGauge.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-12483:

.. function:: dabo.ui.uiwx.dGauge.dGauge.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-12484:

.. function:: dabo.ui.uiwx.dGauge.dGauge.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12485:

.. function:: dabo.ui.uiwx.dGauge.dGauge.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12486:

.. function:: dabo.ui.uiwx.dGauge.dGauge.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12487:

.. function:: dabo.ui.uiwx.dGauge.dGauge.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12488:

.. function:: dabo.ui.uiwx.dGauge.dGauge.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12489:

.. function:: dabo.ui.uiwx.dGauge.dGauge.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12490:

.. function:: dabo.ui.uiwx.dGauge.dGauge.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12491:

.. function:: dabo.ui.uiwx.dGauge.dGauge.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12492:

.. function:: dabo.ui.uiwx.dGauge.dGauge.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12493:

.. function:: dabo.ui.uiwx.dGauge.dGauge.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12494:

.. function:: dabo.ui.uiwx.dGauge.dGauge.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
