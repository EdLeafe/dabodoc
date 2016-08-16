
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dImage

.. _dabo.ui.uiwx.dImage.dImage:

======================================
|doc_title|  **dImage.dImage** - class
======================================

Create a simple bitmap to display images.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dImage**

.. inheritance-diagram:: dImage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`
* :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dImage.png
          :scale: 75 %
          :target: _static/macWidgets/dImage.png
          :alt: dImage



     - .. image:: _static/winWidgets/dImage.png
          :scale: 75 %
          :target: _static/winWidgets/dImage.png
          :alt: dImage



     - .. image:: _static/nixWidgets/dImage.png
          :scale: 75 %
          :target: _static/nixWidgets/dImage.png
          :alt: dImage


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dImage.dImage

   .. automethod:: dabo.ui.uiwx.dImage.dImage.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-24287>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-24288>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-24289>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-24290>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-24291>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-24292>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-24293>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-24294>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-24295>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-24296>`                  The caption of the object. (str)
:ref:`Children <no-24297>`                 Returns a list of object references to the children of
:ref:`Class <no-24298>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-24299>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-24300>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-24301>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-24302>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-24303>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-24304>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-24305>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-24306>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-24307>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-24308>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-24309>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-24310>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-24311>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-24312>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-24313>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-24314>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-24315>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-24316>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-24317>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-24318>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-24319>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-24320>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-24321>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-24322>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPicture <no-24323>`           Dynamically determine the value of the Picture property.
:ref:`DynamicPosition <no-24324>`          Dynamically determine the value of the Position property.
:ref:`DynamicScaleMode <no-24325>`         Dynamically determine the value of the ScaleMode property.
:ref:`DynamicSize <no-24326>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-24327>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-24328>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-24329>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-24330>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-24331>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-24332>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-24333>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-24334>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-24335>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-24336>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-24337>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-24338>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-24339>`                 Specifies the font face. (str)
:ref:`FontInfo <no-24340>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-24341>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-24342>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-24343>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-24344>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-24345>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`FrameCount <no-24346>`               Number of frames in the current image. Will be 1 for most images, but can be greater for animated GI
:ref:`Height <no-24347>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-24348>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-24349>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-24350>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-24351>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-24352>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-24353>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-24354>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-24355>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-24356>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-24357>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-24358>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-24359>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-24360>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-24361>`                 Specifies the base name of the object.
:ref:`Parent <no-24362>`                   The containing object. (obj)
:ref:`PersistSecretData <no-24363>`        If True, allow persisting the secret data in encrypted form.
:ref:`Picture <no-24364>`                  The file used as the source for the displayed image.  (str)
:ref:`PictureIndex <no-24365>`             When displaying images from files that can contain multiple
:ref:`Position <no-24366>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-24367>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-24368>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-24369>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-24370>`         Specifies whether the Value of the control gets saved when
:ref:`ScaleMode <no-24371>`                Determines how the image responds to sizing. Can be one
:ref:`Size <no-24372>`                     The size of the object. (tuple)
:ref:`Sizer <no-24373>`                    The sizer for the object.
:ref:`Source <no-24374>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-24375>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-24376>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-24377>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-24378>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-24379>`                      The top position of the object. (int)
:ref:`Transparency <no-24380>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-24381>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-24382>`                    Image content for this control  (binary img data)
:ref:`Visible <no-24383>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-24384>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-24385>`                    The width of the object. (int)
:ref:`WindowHandle <no-24386>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-24325:

**DynamicScaleMode** 

Dynamically determine the value of the ScaleMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ScaleMode property. If DynamicScaleMode is set to None (the default), ScaleMode
will not be dynamically evaluated.



-------

.. _no-24346:

**FrameCount** 

Number of frames in the current image. Will be 1 for most images, but can be greater for animated GIFs, ICOs and some TIFF files. (read-only) (int)



-------

.. _no-24365:

**PictureIndex** 

When displaying images from files that can contain multiple
    images, such as GIF, TIFF and ICO, this determines which image
    is used. Default=-1, which displays the first image for GIF and TIFF,
    and the main image for ICO.  (int)



-------

.. _no-24371:

**ScaleMode** 

Determines how the image responds to sizing. Can be one
    of the following:

        =============== ===================
        Clip            Only that part of the image that fits in the control's size is displayed
        Proportional    The image resizes to fit the control without changing its original proportions. (default)
        Stretch         The image resizes to the Height/Width of the control.
        =============== ===================

    



-------


Properties - inherited
========================

.. _no-24287:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24288:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24289:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24290:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24291:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24292:

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

.. _no-24293:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24294:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24295:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24296:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24297:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24298:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24299:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24300:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24301:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24302:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24303:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24304:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24305:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24306:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24307:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24308:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24309:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24310:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24311:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24312:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24313:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24314:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24315:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24316:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24317:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24318:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24319:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24320:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24321:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24322:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24323:

**DynamicPicture** 

Dynamically determine the value of the Picture property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Picture property. If DynamicPicture is set to None (the default), Picture
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`

-------

.. _no-24324:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24326:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24327:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24328:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24329:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24330:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24331:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24332:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-24333:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24334:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24335:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24336:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24337:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24338:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24339:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24340:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24341:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24342:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24343:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24344:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24345:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24347:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24348:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24349:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24350:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24351:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24352:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24353:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24354:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24355:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24356:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24357:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24358:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24359:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24360:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24361:

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

.. _no-24362:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24363:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24364:

**Picture** 

The file used as the source for the displayed image.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`

-------

.. _no-24366:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24367:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24368:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24369:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24370:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24372:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24373:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24374:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24375:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24376:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-24377:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24378:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24379:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24380:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24381:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24382:

**Value** 

Image content for this control  (binary img data)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24383:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24384:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24385:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24386:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-24387>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-24388>`                 Occurs after the control or form is created.
:ref:`Destroy <no-24389>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-24390>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-24391>`               Occurs when the control gets the focus.
:ref:`Idle <no-24392>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-24393>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-24394>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-24395>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-24396>`               
:ref:`KeyUp <no-24397>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-24398>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-24399>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-24400>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-24401>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-24402>`             
:ref:`MouseLeave <no-24403>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-24404>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-24405>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-24406>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-24407>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-24408>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-24409>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-24410>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-24411>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-24412>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-24413>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-24414>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-24415>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-24416>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-24417>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-24418>`                   Occurs when the control's position changes.
:ref:`Paint <no-24419>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-24420>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-24421>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-24422>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-24423>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-24424>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-24387:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-24388:

**Create** 

Occurs after the control or form is created.



-------

.. _no-24389:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-24390:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-24391:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-24392:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-24393:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-24394:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-24395:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-24396:

**KeyEvent** 



-------

.. _no-24397:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-24398:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-24399:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-24400:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-24401:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-24402:

**MouseEvent** 



-------

.. _no-24403:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-24404:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-24405:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-24406:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-24407:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-24408:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-24409:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-24410:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-24411:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-24412:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-24413:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-24414:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-24415:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-24416:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-24417:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-24418:

**Move** 

Occurs when the control's position changes.



-------

.. _no-24419:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-24420:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-24421:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-24422:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-24423:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-24424:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================== ========================
:ref:`absoluteCoordinates <no-24425>`    Translates a position value for a control to absolute screen position.
:ref:`addObject <no-24426>`              Instantiate object as a child of self.
:ref:`afterInit <no-24427>`              Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-24428>`           
:ref:`afterSetProperties <no-24429>`     
:ref:`autoBindEvents <no-24430>`         Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-24431>`             Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-24432>`    
:ref:`bindEvent <no-24433>`              Bind a dEvent to a callback function.
:ref:`bindEvents <no-24434>`             Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-24435>`                Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-24436>`           Makes this object topmost
:ref:`clear <no-24437>`                  Clears the background of custom-drawn objects.
:ref:`clone <no-24438>`                  Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-24439>`   Given a position relative to this control, return a position relative
:ref:`copy <no-24440>`                   Called by uiApp when the user requests a copy operation.
:ref:`cut <no-24441>`                    Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-24442>`                Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-24443>`             Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-24444>`             Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-24445>`            Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-24446>`        Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-24447>`           Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-24448>`               Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-24449>`          Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-24450>`            Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-24451>`          Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-24452>`   Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-24453>`               Draws text on the object at the specified position
:ref:`endHover <no-24454>`               
:ref:`fitToSizer <no-24455>`             Resize the control to fit the size required by its sizer.
:ref:`flipHorizontally <no-24456>`       
:ref:`flipVertically <no-24457>`         
:ref:`flushValue <no-24458>`             Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-24459>`             Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-24460>`         Reset the font zoom back to zero.
:ref:`fontZoomOut <no-24461>`            Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-24462>`        Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-24463>`        Return the fully qualified name of the object.
:ref:`getBlankValue <no-24464>`          Return the empty value of the control.
:ref:`getCaptureBitmap <no-24465>`       Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-24466>`      Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-24467>`       Returns an object that locks the current display when created, and
:ref:`getImgType <no-24468>`             
:ref:`getMousePosition <no-24469>`       Returns the current mouse position on the entire screen
:ref:`getOriginalImgSize <no-24470>`     Since the image can be scaled, this returns the size of
:ref:`getPositionInSizer <no-24471>`     Convenience method to let you call this directly on the object.
:ref:`getProperties <no-24472>`          Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-24473>`       
:ref:`getSizerProp <no-24474>`           Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-24475>`          Returns a dict containing the object's sizer property info. The
:ref:`hide <no-24476>`                   Make the object invisible.
:ref:`initEvents <no-24477>`             Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-24478>`         Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-24479>`          Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-24480>`            Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-24481>`            Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-24482>`      Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-24483>`     Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-24484>`      Given a position relative to the form, return a position relative
:ref:`onHover <no-24485>`                
:ref:`paste <no-24486>`                  Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-24487>`            
:ref:`processDroppedFiles <no-24488>`    Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-24489>`     Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-24490>`             Raise the passed Dabo event.
:ref:`reCreate <no-24491>`               Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-24492>`               Recreate the object.
:ref:`redraw <no-24493>`                 Called when the object is (re)drawn.
:ref:`refresh <no-24494>`                Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-24495>`    Translates an absolute screen position to position value for a control.
:ref:`release <no-24496>`                Destroys the object.
:ref:`removeDrawnObject <no-24497>`      
:ref:`restoreValue <no-24498>`           Set the control's value to the value in dApp's user settings table.
:ref:`rotateClockwise <no-24499>`        
:ref:`rotateCounterClockwise <no-24500>` 
:ref:`saveValue <no-24501>`              Save control's value to dApp's user settings table.
:ref:`select <no-24502>`                 Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-24503>`              Select all text in the control.
:ref:`selectNone <no-24504>`             Select no text in the control.
:ref:`sendToBack <no-24505>`             Places this object behind all others.
:ref:`setAll <no-24506>`                 Set all child object properties to the passed value.
:ref:`setFocus <no-24507>`               Sets focus to the object.
:ref:`setPositionInSizer <no-24508>`     Convenience method to let you call this directly on the object.
:ref:`setProperties <no-24509>`          Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-24510>`  Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-24511>`           Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-24512>`          Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-24513>`                   Make the object visible.
:ref:`showContainingPage <no-24514>`     If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-24515>`        Display a context menu (popup) at the specified position.
:ref:`super <no-24516>`                  This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-24517>`            Remove a previously registered event binding.
:ref:`unbindKey <no-24518>`              Unbind a previously bound key combination.
:ref:`unlockDisplay <no-24519>`          Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-24520>`       Immediately unlocks the display, no matter how many previous
:ref:`update <no-24521>`                 

======================================== ========================


Methods
=======

.. _no-24456:

.. function:: dabo.ui.uiwx.dImage.dImage.flipHorizontally(self)



-------

.. _no-24457:

.. function:: dabo.ui.uiwx.dImage.dImage.flipVertically(self)



-------

.. _no-24468:

.. function:: dabo.ui.uiwx.dImage.dImage.getImgType(self)



-------

.. _no-24470:

.. function:: dabo.ui.uiwx.dImage.dImage.getOriginalImgSize(self)

   
   Since the image can be scaled, this returns the size of
   the unscaled image.
   



-------

.. _no-24499:

.. function:: dabo.ui.uiwx.dImage.dImage.rotateClockwise(self)



-------

.. _no-24500:

.. function:: dabo.ui.uiwx.dImage.dImage.rotateCounterClockwise(self)



-------

.. _no-24521:

.. function:: dabo.ui.uiwx.dImage.dImage.update(self)



-------


Methods - inherited
=====================

.. _no-24425:

.. function:: dabo.ui.uiwx.dImage.dImage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24426:

.. function:: dabo.ui.uiwx.dImage.dImage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-24427:

.. function:: dabo.ui.uiwx.dImage.dImage.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24428:

.. function:: dabo.ui.uiwx.dImage.dImage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24429:

.. function:: dabo.ui.uiwx.dImage.dImage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24430:

.. function:: dabo.ui.uiwx.dImage.dImage.autoBindEvents(self, force=True)
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

.. _no-24431:

.. function:: dabo.ui.uiwx.dImage.dImage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24432:

.. function:: dabo.ui.uiwx.dImage.dImage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24433:

.. function:: dabo.ui.uiwx.dImage.dImage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24434:

.. function:: dabo.ui.uiwx.dImage.dImage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24435:

.. function:: dabo.ui.uiwx.dImage.dImage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-24436:

.. function:: dabo.ui.uiwx.dImage.dImage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24437:

.. function:: dabo.ui.uiwx.dImage.dImage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24438:

.. function:: dabo.ui.uiwx.dImage.dImage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24439:

.. function:: dabo.ui.uiwx.dImage.dImage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24440:

.. function:: dabo.ui.uiwx.dImage.dImage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24441:

.. function:: dabo.ui.uiwx.dImage.dImage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24442:

.. function:: dabo.ui.uiwx.dImage.dImage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24443:

.. function:: dabo.ui.uiwx.dImage.dImage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24444:

.. function:: dabo.ui.uiwx.dImage.dImage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-24445:

.. function:: dabo.ui.uiwx.dImage.dImage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24446:

.. function:: dabo.ui.uiwx.dImage.dImage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24447:

.. function:: dabo.ui.uiwx.dImage.dImage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24448:

.. function:: dabo.ui.uiwx.dImage.dImage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24449:

.. function:: dabo.ui.uiwx.dImage.dImage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24450:

.. function:: dabo.ui.uiwx.dImage.dImage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24451:

.. function:: dabo.ui.uiwx.dImage.dImage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24452:

.. function:: dabo.ui.uiwx.dImage.dImage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24453:

.. function:: dabo.ui.uiwx.dImage.dImage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24454:

.. function:: dabo.ui.uiwx.dImage.dImage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24455:

.. function:: dabo.ui.uiwx.dImage.dImage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24458:

.. function:: dabo.ui.uiwx.dImage.dImage.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24459:

.. function:: dabo.ui.uiwx.dImage.dImage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24460:

.. function:: dabo.ui.uiwx.dImage.dImage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24461:

.. function:: dabo.ui.uiwx.dImage.dImage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24462:

.. function:: dabo.ui.uiwx.dImage.dImage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24463:

.. function:: dabo.ui.uiwx.dImage.dImage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24464:

.. function:: dabo.ui.uiwx.dImage.dImage.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24465:

.. function:: dabo.ui.uiwx.dImage.dImage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24466:

.. function:: dabo.ui.uiwx.dImage.dImage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24467:

.. function:: dabo.ui.uiwx.dImage.dImage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24469:

.. function:: dabo.ui.uiwx.dImage.dImage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24471:

.. function:: dabo.ui.uiwx.dImage.dImage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24472:

.. function:: dabo.ui.uiwx.dImage.dImage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-24473:

.. function:: dabo.ui.uiwx.dImage.dImage.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24474:

.. function:: dabo.ui.uiwx.dImage.dImage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24475:

.. function:: dabo.ui.uiwx.dImage.dImage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24476:

.. function:: dabo.ui.uiwx.dImage.dImage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24477:

.. function:: dabo.ui.uiwx.dImage.dImage.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24478:

.. function:: dabo.ui.uiwx.dImage.dImage.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24479:

.. function:: dabo.ui.uiwx.dImage.dImage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24480:

.. function:: dabo.ui.uiwx.dImage.dImage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24481:

.. function:: dabo.ui.uiwx.dImage.dImage.lockDisplay(self)
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

.. _no-24482:

.. function:: dabo.ui.uiwx.dImage.dImage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24483:

.. function:: dabo.ui.uiwx.dImage.dImage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24484:

.. function:: dabo.ui.uiwx.dImage.dImage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24485:

.. function:: dabo.ui.uiwx.dImage.dImage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24486:

.. function:: dabo.ui.uiwx.dImage.dImage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24487:

.. function:: dabo.ui.uiwx.dImage.dImage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24488:

.. function:: dabo.ui.uiwx.dImage.dImage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24489:

.. function:: dabo.ui.uiwx.dImage.dImage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24490:

.. function:: dabo.ui.uiwx.dImage.dImage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24491:

.. function:: dabo.ui.uiwx.dImage.dImage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24492:

.. function:: dabo.ui.uiwx.dImage.dImage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24493:

.. function:: dabo.ui.uiwx.dImage.dImage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24494:

.. function:: dabo.ui.uiwx.dImage.dImage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24495:

.. function:: dabo.ui.uiwx.dImage.dImage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24496:

.. function:: dabo.ui.uiwx.dImage.dImage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24497:

.. function:: dabo.ui.uiwx.dImage.dImage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24498:

.. function:: dabo.ui.uiwx.dImage.dImage.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24501:

.. function:: dabo.ui.uiwx.dImage.dImage.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-24502:

.. function:: dabo.ui.uiwx.dImage.dImage.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-24503:

.. function:: dabo.ui.uiwx.dImage.dImage.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-24504:

.. function:: dabo.ui.uiwx.dImage.dImage.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-24505:

.. function:: dabo.ui.uiwx.dImage.dImage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24506:

.. function:: dabo.ui.uiwx.dImage.dImage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-24507:

.. function:: dabo.ui.uiwx.dImage.dImage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24508:

.. function:: dabo.ui.uiwx.dImage.dImage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24509:

.. function:: dabo.ui.uiwx.dImage.dImage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-24510:

.. function:: dabo.ui.uiwx.dImage.dImage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-24511:

.. function:: dabo.ui.uiwx.dImage.dImage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24512:

.. function:: dabo.ui.uiwx.dImage.dImage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24513:

.. function:: dabo.ui.uiwx.dImage.dImage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24514:

.. function:: dabo.ui.uiwx.dImage.dImage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24515:

.. function:: dabo.ui.uiwx.dImage.dImage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24516:

.. function:: dabo.ui.uiwx.dImage.dImage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24517:

.. function:: dabo.ui.uiwx.dImage.dImage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24518:

.. function:: dabo.ui.uiwx.dImage.dImage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24519:

.. function:: dabo.ui.uiwx.dImage.dImage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24520:

.. function:: dabo.ui.uiwx.dImage.dImage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
