
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dLed

.. _dabo.ui.uiwx.dLed.dLed:

==================================
|doc_title|  **dLed.dLed** - class
==================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dLed**

.. inheritance-diagram:: dLed


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dDataPanel`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dLed.png
          :scale: 75 %
          :target: _static/macWidgets/dLed.png
          :alt: dLed



     - .. image:: _static/winWidgets/dLed.png
          :scale: 75 %
          :target: _static/winWidgets/dLed.png
          :alt: dLed



     - .. image:: _static/nixWidgets/dLed.png
          :scale: 75 %
          :target: _static/nixWidgets/dLed.png
          :alt: dLed


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dLed.dLed

   .. automethod:: dabo.ui.uiwx.dLed.dLed.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-22362>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-22363>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-22364>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-22365>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-22366>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-22367>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-22368>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-22369>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-22370>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-22371>`                  The caption of the object. (str)
:ref:`Children <no-22372>`                 Returns a list of object references to the children of
:ref:`Class <no-22373>`                    The class the object is based on. Read-only.  (class)
:ref:`Color <no-22374>`                    The current color of the LED (color)
:ref:`ControllingSizer <no-22375>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-22376>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-22377>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-22378>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-22379>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-22380>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-22381>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-22382>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-22383>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-22384>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-22385>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-22386>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-22387>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-22388>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-22389>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-22390>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-22391>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-22392>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-22393>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-22394>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-22395>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-22396>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-22397>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-22398>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-22399>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-22400>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-22401>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-22402>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-22403>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-22404>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-22405>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-22406>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-22407>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-22408>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-22409>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-22410>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-22411>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-22412>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-22413>`                 Specifies the font face. (str)
:ref:`FontInfo <no-22414>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-22415>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-22416>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-22417>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-22418>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-22419>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-22420>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-22421>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-22422>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-22423>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-22424>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-22425>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-22426>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-22427>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-22428>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-22429>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-22430>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-22431>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-22432>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-22433>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-22434>`                 Specifies the base name of the object.
:ref:`OffColor <no-22435>`                 The color of the LED when it is off.  (color)
:ref:`On <no-22436>`                       Is the LED is on? Default=False  (bool)
:ref:`OnColor <no-22437>`                  The color of the LED when it is on.  (color)
:ref:`Parent <no-22438>`                   The containing object. (obj)
:ref:`PersistSecretData <no-22439>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-22440>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-22441>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-22442>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-22443>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-22444>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-22445>`                     The size of the object. (tuple)
:ref:`Sizer <no-22446>`                    The sizer for the object.
:ref:`Source <no-22447>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-22448>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-22449>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-22450>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-22451>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-22452>`                      The top position of the object. (int)
:ref:`Transparency <no-22453>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-22454>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-22455>`                    Is the LED is on? Default=False  (bool)
:ref:`Visible <no-22456>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-22457>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-22458>`                    The width of the object. (int)
:ref:`WindowHandle <no-22459>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-22374:

**Color** 

The current color of the LED (color)



-------

.. _no-22435:

**OffColor** 

The color of the LED when it is off.  (color)



-------

.. _no-22436:

**On** 

Is the LED is on? Default=False  (bool)



-------

.. _no-22437:

**OnColor** 

The color of the LED when it is on.  (color)



-------


Properties - inherited
========================

.. _no-22362:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22363:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22364:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22365:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22366:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22367:

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

.. _no-22368:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22369:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22370:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22371:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22372:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22373:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22375:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22376:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22377:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22378:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22379:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22380:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22381:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22382:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22383:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22384:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22385:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22386:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22387:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22388:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22389:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22390:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22391:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22392:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22393:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22394:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22395:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22396:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22397:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22398:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22399:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22400:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22401:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22402:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22403:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22404:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22405:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22406:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-22407:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22408:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22409:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22410:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22411:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22412:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22413:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22414:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22415:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22416:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22417:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22418:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22419:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22420:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22421:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22422:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22423:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22424:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22425:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22426:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22427:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22428:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22429:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22430:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22431:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22432:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22433:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22434:

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

.. _no-22438:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22439:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22440:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22441:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22442:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22443:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22444:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22445:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22446:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-22447:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22448:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22449:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-22450:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22451:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22452:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22453:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22454:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22455:

**Value** 

Is the LED is on? Default=False  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22456:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22457:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22458:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22459:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-22460>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-22461>`                 Occurs after the control or form is created.
:ref:`Destroy <no-22462>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-22463>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-22464>`               Occurs when the control gets the focus.
:ref:`Idle <no-22465>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-22466>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-22467>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-22468>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-22469>`               
:ref:`KeyUp <no-22470>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-22471>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-22472>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-22473>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-22474>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-22475>`             
:ref:`MouseLeave <no-22476>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-22477>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-22478>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-22479>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-22480>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-22481>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-22482>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-22483>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-22484>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-22485>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-22486>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-22487>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-22488>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-22489>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-22490>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-22491>`                   Occurs when the control's position changes.
:ref:`Paint <no-22492>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-22493>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-22494>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-22495>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-22496>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-22497>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-22460:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-22461:

**Create** 

Occurs after the control or form is created.



-------

.. _no-22462:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-22463:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-22464:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-22465:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-22466:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-22467:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-22468:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-22469:

**KeyEvent** 



-------

.. _no-22470:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-22471:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-22472:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-22473:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-22474:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-22475:

**MouseEvent** 



-------

.. _no-22476:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-22477:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-22478:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-22479:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-22480:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-22481:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-22482:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-22483:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-22484:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-22485:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-22486:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-22487:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-22488:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-22489:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-22490:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-22491:

**Move** 

Occurs when the control's position changes.



-------

.. _no-22492:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-22493:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-22494:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-22495:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-22496:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-22497:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-22498>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-22499>`             Instantiate object as a child of self.
:ref:`afterInit <no-22500>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-22501>`          
:ref:`afterSetProperties <no-22502>`    
:ref:`autoBindEvents <no-22503>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-22504>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-22505>`   
:ref:`bindEvent <no-22506>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-22507>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-22508>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-22509>`          Makes this object topmost
:ref:`clear <no-22510>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-22511>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-22512>`  Given a position relative to this control, return a position relative
:ref:`copy <no-22513>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-22514>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-22515>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-22516>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-22517>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-22518>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-22519>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-22520>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-22521>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-22522>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-22523>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-22524>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-22525>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-22526>`              Draws text on the object at the specified position
:ref:`endHover <no-22527>`              
:ref:`fitToSizer <no-22528>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-22529>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-22530>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-22531>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-22532>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-22533>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-22534>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-22535>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-22536>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-22537>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-22538>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-22539>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-22540>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-22541>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-22542>`      
:ref:`getSizerProp <no-22543>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-22544>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-22545>`                  Make the object invisible.
:ref:`initEvents <no-22546>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-22547>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-22548>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-22549>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-22550>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-22551>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-22552>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-22553>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-22554>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-22555>`               
:ref:`onResize <no-22556>`              Update the size of the LED.
:ref:`paste <no-22557>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-22558>`           
:ref:`processDroppedFiles <no-22559>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-22560>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-22561>`            Raise the passed Dabo event.
:ref:`reCreate <no-22562>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-22563>`              Recreate the object.
:ref:`redraw <no-22564>`                Called when the object is (re)drawn.
:ref:`refresh <no-22565>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-22566>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-22567>`               Destroys the object.
:ref:`removeDrawnObject <no-22568>`     
:ref:`restoreValue <no-22569>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-22570>`             Save control's value to dApp's user settings table.
:ref:`select <no-22571>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-22572>`             Select all text in the control.
:ref:`selectNone <no-22573>`            Select no text in the control.
:ref:`sendToBack <no-22574>`            Places this object behind all others.
:ref:`setAll <no-22575>`                Set all child object properties to the passed value.
:ref:`setFocus <no-22576>`              Sets focus to the object.
:ref:`setPositionInSizer <no-22577>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-22578>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-22579>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-22580>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-22581>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-22582>`                  Make the object visible.
:ref:`showContainingPage <no-22583>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-22584>`       Display a context menu (popup) at the specified position.
:ref:`super <no-22585>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-22586>`           Remove a previously registered event binding.
:ref:`unbindKey <no-22587>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-22588>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-22589>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-22590>`                

======================================= ========================


Methods
=======

.. _no-22556:

.. function:: dabo.ui.uiwx.dLed.dLed.onResize(self, evt)

   Update the size of the LED.



-------

.. _no-22590:

.. function:: dabo.ui.uiwx.dLed.dLed.update(self)



-------


Methods - inherited
=====================

.. _no-22498:

.. function:: dabo.ui.uiwx.dLed.dLed.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22499:

.. function:: dabo.ui.uiwx.dLed.dLed.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-22500:

.. function:: dabo.ui.uiwx.dLed.dLed.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22501:

.. function:: dabo.ui.uiwx.dLed.dLed.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22502:

.. function:: dabo.ui.uiwx.dLed.dLed.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22503:

.. function:: dabo.ui.uiwx.dLed.dLed.autoBindEvents(self, force=True)
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

.. _no-22504:

.. function:: dabo.ui.uiwx.dLed.dLed.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22505:

.. function:: dabo.ui.uiwx.dLed.dLed.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22506:

.. function:: dabo.ui.uiwx.dLed.dLed.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22507:

.. function:: dabo.ui.uiwx.dLed.dLed.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22508:

.. function:: dabo.ui.uiwx.dLed.dLed.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-22509:

.. function:: dabo.ui.uiwx.dLed.dLed.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22510:

.. function:: dabo.ui.uiwx.dLed.dLed.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22511:

.. function:: dabo.ui.uiwx.dLed.dLed.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22512:

.. function:: dabo.ui.uiwx.dLed.dLed.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22513:

.. function:: dabo.ui.uiwx.dLed.dLed.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22514:

.. function:: dabo.ui.uiwx.dLed.dLed.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22515:

.. function:: dabo.ui.uiwx.dLed.dLed.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22516:

.. function:: dabo.ui.uiwx.dLed.dLed.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22517:

.. function:: dabo.ui.uiwx.dLed.dLed.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-22518:

.. function:: dabo.ui.uiwx.dLed.dLed.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22519:

.. function:: dabo.ui.uiwx.dLed.dLed.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22520:

.. function:: dabo.ui.uiwx.dLed.dLed.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22521:

.. function:: dabo.ui.uiwx.dLed.dLed.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22522:

.. function:: dabo.ui.uiwx.dLed.dLed.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22523:

.. function:: dabo.ui.uiwx.dLed.dLed.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22524:

.. function:: dabo.ui.uiwx.dLed.dLed.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22525:

.. function:: dabo.ui.uiwx.dLed.dLed.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22526:

.. function:: dabo.ui.uiwx.dLed.dLed.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22527:

.. function:: dabo.ui.uiwx.dLed.dLed.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22528:

.. function:: dabo.ui.uiwx.dLed.dLed.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22529:

.. function:: dabo.ui.uiwx.dLed.dLed.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22530:

.. function:: dabo.ui.uiwx.dLed.dLed.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22531:

.. function:: dabo.ui.uiwx.dLed.dLed.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22532:

.. function:: dabo.ui.uiwx.dLed.dLed.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22533:

.. function:: dabo.ui.uiwx.dLed.dLed.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22534:

.. function:: dabo.ui.uiwx.dLed.dLed.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22535:

.. function:: dabo.ui.uiwx.dLed.dLed.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22536:

.. function:: dabo.ui.uiwx.dLed.dLed.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22537:

.. function:: dabo.ui.uiwx.dLed.dLed.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22538:

.. function:: dabo.ui.uiwx.dLed.dLed.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22539:

.. function:: dabo.ui.uiwx.dLed.dLed.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22540:

.. function:: dabo.ui.uiwx.dLed.dLed.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22541:

.. function:: dabo.ui.uiwx.dLed.dLed.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-22542:

.. function:: dabo.ui.uiwx.dLed.dLed.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22543:

.. function:: dabo.ui.uiwx.dLed.dLed.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22544:

.. function:: dabo.ui.uiwx.dLed.dLed.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22545:

.. function:: dabo.ui.uiwx.dLed.dLed.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22546:

.. function:: dabo.ui.uiwx.dLed.dLed.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22547:

.. function:: dabo.ui.uiwx.dLed.dLed.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22548:

.. function:: dabo.ui.uiwx.dLed.dLed.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22549:

.. function:: dabo.ui.uiwx.dLed.dLed.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22550:

.. function:: dabo.ui.uiwx.dLed.dLed.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-22551:

.. function:: dabo.ui.uiwx.dLed.dLed.lockDisplay(self)
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

.. _no-22552:

.. function:: dabo.ui.uiwx.dLed.dLed.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22553:

.. function:: dabo.ui.uiwx.dLed.dLed.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22554:

.. function:: dabo.ui.uiwx.dLed.dLed.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22555:

.. function:: dabo.ui.uiwx.dLed.dLed.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22557:

.. function:: dabo.ui.uiwx.dLed.dLed.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22558:

.. function:: dabo.ui.uiwx.dLed.dLed.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22559:

.. function:: dabo.ui.uiwx.dLed.dLed.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22560:

.. function:: dabo.ui.uiwx.dLed.dLed.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22561:

.. function:: dabo.ui.uiwx.dLed.dLed.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22562:

.. function:: dabo.ui.uiwx.dLed.dLed.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-22563:

.. function:: dabo.ui.uiwx.dLed.dLed.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22564:

.. function:: dabo.ui.uiwx.dLed.dLed.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22565:

.. function:: dabo.ui.uiwx.dLed.dLed.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22566:

.. function:: dabo.ui.uiwx.dLed.dLed.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22567:

.. function:: dabo.ui.uiwx.dLed.dLed.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22568:

.. function:: dabo.ui.uiwx.dLed.dLed.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22569:

.. function:: dabo.ui.uiwx.dLed.dLed.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22570:

.. function:: dabo.ui.uiwx.dLed.dLed.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-22571:

.. function:: dabo.ui.uiwx.dLed.dLed.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-22572:

.. function:: dabo.ui.uiwx.dLed.dLed.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-22573:

.. function:: dabo.ui.uiwx.dLed.dLed.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-22574:

.. function:: dabo.ui.uiwx.dLed.dLed.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22575:

.. function:: dabo.ui.uiwx.dLed.dLed.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-22576:

.. function:: dabo.ui.uiwx.dLed.dLed.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22577:

.. function:: dabo.ui.uiwx.dLed.dLed.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22578:

.. function:: dabo.ui.uiwx.dLed.dLed.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-22579:

.. function:: dabo.ui.uiwx.dLed.dLed.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-22580:

.. function:: dabo.ui.uiwx.dLed.dLed.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22581:

.. function:: dabo.ui.uiwx.dLed.dLed.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22582:

.. function:: dabo.ui.uiwx.dLed.dLed.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22583:

.. function:: dabo.ui.uiwx.dLed.dLed.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22584:

.. function:: dabo.ui.uiwx.dLed.dLed.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22585:

.. function:: dabo.ui.uiwx.dLed.dLed.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-22586:

.. function:: dabo.ui.uiwx.dLed.dLed.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-22587:

.. function:: dabo.ui.uiwx.dLed.dLed.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22588:

.. function:: dabo.ui.uiwx.dLed.dLed.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-22589:

.. function:: dabo.ui.uiwx.dLed.dLed.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
