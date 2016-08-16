
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.SelectSpinner:

===========================================
|doc_title|  **Page.SelectSpinner** - class
===========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SelectSpinner**

.. inheritance-diagram:: SelectSpinner


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.datanav.Page.SelectControlMixin`
* :ref:`dabo.ui.uiwx.dSpinner.dSpinner`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.SelectSpinner


|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Alignment <no-4376>`                
:ref:`Application <no-4377>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-4378>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-4379>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-4380>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-4381>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-4382>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-4383>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-4384>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-4385>`                   The position of the bottom side of the object. This is a
:ref:`ButtonWidth <no-4386>`              Allows the developer to explicitly specify the width of the up/down buttons.
:ref:`Caption <no-4387>`                  The caption of the object. (str)
:ref:`Children <no-4388>`                 Returns a list of object references to the children of
:ref:`Class <no-4389>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-4390>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-4391>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-4392>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-4393>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-4394>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-4395>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-4396>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-4397>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-4398>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-4399>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-4400>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-4401>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-4402>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-4403>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-4404>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-4405>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-4406>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-4407>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-4408>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-4409>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-4410>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-4411>`            Dynamically determine the value of the Height property.
:ref:`DynamicIncrement <no-4412>`         Dynamically determine the value of the Increment property.
:ref:`DynamicLeft <no-4413>`              Dynamically determine the value of the Left property.
:ref:`DynamicMax <no-4414>`               Dynamically determine the value of the Max property.
:ref:`DynamicMin <no-4415>`               Dynamically determine the value of the Min property.
:ref:`DynamicMousePointer <no-4416>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-4417>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-4418>`              Dynamically determine the value of the Size property.
:ref:`DynamicSpinnerWrap <no-4419>`       Dynamically determine the value of the SpinnerWrap property.
:ref:`DynamicStatusText <no-4420>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-4421>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-4422>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-4423>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-4424>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-4425>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-4426>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-4427>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-4428>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-4429>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-4430>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-4431>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-4432>`                 Specifies the font face. (str)
:ref:`FontInfo <no-4433>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-4434>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-4435>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-4436>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-4437>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-4438>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-4439>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-4440>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-4441>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`Increment <no-4442>`                Amount the control's value changes when the spinner buttons are clicked  (int/float)
:ref:`IsSecret <no-4443>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-4444>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-4445>`                Specifies which events to log.  (list of strings)
:ref:`Max <no-4446>`                      Maximum value for the control  (int/float)
:ref:`MaximumHeight <no-4447>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-4448>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-4449>`             Maximum allowable width for the control in pixels.  (int)
:ref:`Min <no-4450>`                      Minimum value for the control  (int/float)
:ref:`MinimumHeight <no-4451>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-4452>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-4453>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-4454>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-4455>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-4456>`                 Specifies the base name of the object.
:ref:`Parent <no-4457>`                   The containing object. (obj)
:ref:`PersistSecretData <no-4458>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-4459>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-4460>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-4461>`                 
:ref:`RegID <no-4462>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-4463>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-4464>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-4465>`            
:ref:`Size <no-4466>`                     The size of the object. (tuple)
:ref:`Sizer <no-4467>`                    The sizer for the object.
:ref:`Source <no-4468>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`SpinnerWrap <no-4469>`              Specifies whether the spinner value wraps at the high/low value. (bool)
:ref:`StatusText <no-4470>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-4471>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-4472>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-4473>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-4474>`                      The top position of the object. (int)
:ref:`Transparency <no-4475>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-4476>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-4477>`                    Value of the control  (int/float)
:ref:`Visible <no-4478>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-4479>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-4480>`                    The width of the object. (int)
:ref:`WindowHandle <no-4481>`             The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties - inherited
========================

.. _no-4376:

**Alignment** 


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-4377:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4378:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4379:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4380:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4381:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4382:

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

.. _no-4383:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4384:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4385:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4386:

**ButtonWidth** 

Allows the developer to explicitly specify the width of the up/down buttons.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4387:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4388:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4389:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4390:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4391:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4392:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4393:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4394:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4395:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4396:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4397:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4398:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4399:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4400:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4401:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4402:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4403:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4404:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4405:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4406:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4407:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4408:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4409:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4410:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4411:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4412:

**DynamicIncrement** 

Dynamically determine the value of the Increment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Increment property. If DynamicIncrement is set to None (the default), Increment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4413:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4414:

**DynamicMax** 

Dynamically determine the value of the Max property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Max property. If DynamicMax is set to None (the default), Max
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4415:

**DynamicMin** 

Dynamically determine the value of the Min property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Min property. If DynamicMin is set to None (the default), Min
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4416:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4417:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4418:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4419:

**DynamicSpinnerWrap** 

Dynamically determine the value of the SpinnerWrap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SpinnerWrap property. If DynamicSpinnerWrap is set to None (the default), SpinnerWrap
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4420:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4421:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4422:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4423:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4424:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4425:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-4426:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4427:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4428:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4429:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4430:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4431:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4432:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4433:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4434:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4435:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4436:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4437:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4438:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4439:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4440:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4441:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4442:

**Increment** 

Amount the control's value changes when the spinner buttons are clicked  (int/float)


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4443:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4444:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4445:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4446:

**Max** 

Maximum value for the control  (int/float)


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4447:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4448:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4449:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4450:

**Min** 

Minimum value for the control  (int/float)


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4451:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4452:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4453:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4454:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4455:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4456:

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

.. _no-4457:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4458:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4459:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4460:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4461:

**ReadOnly** 


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4462:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4463:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4464:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4465:

**SelectOnEntry** 


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4466:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4467:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4468:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4469:

**SpinnerWrap** 

Specifies whether the spinner value wraps at the high/low value. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4470:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4471:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-4472:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4473:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4474:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4475:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4476:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4477:

**Value** 

Value of the control  (int/float)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4478:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4479:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4480:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4481:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-4482>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-4483>`                 Occurs after the control or form is created.
:ref:`Destroy <no-4484>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-4485>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-4486>`               Occurs when the control gets the focus.
:ref:`Hit <no-4487>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-4488>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-4489>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-4490>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-4491>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-4492>`               
:ref:`KeyUp <no-4493>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-4494>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-4495>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-4496>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-4497>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-4498>`             
:ref:`MouseLeave <no-4499>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-4500>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-4501>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-4502>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-4503>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-4504>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-4505>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-4506>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-4507>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-4508>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-4509>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-4510>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-4511>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-4512>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-4513>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-4514>`                   Occurs when the control's position changes.
:ref:`Paint <no-4515>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-4516>`                 Occurs when the control or form is resized.
:ref:`SpinDown <no-4517>`               Occurs when the spinner is decremented, either by clicking
:ref:`SpinUp <no-4518>`                 Occurs when the spinner is incremented, either by clicking
:ref:`Spinner <no-4519>`                Occurs when the spinner is changed, either by clicking
:ref:`SpinnerEvent <no-4520>`           
:ref:`TreeBeginDrag <no-4521>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-4522>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-4523>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-4524>`           Occurs when the control's value has changed, whether

======================================= ========================


Events
=======

.. _no-4482:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-4483:

**Create** 

Occurs after the control or form is created.



-------

.. _no-4484:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-4485:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-4486:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-4487:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-4488:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-4489:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-4490:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-4491:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-4492:

**KeyEvent** 



-------

.. _no-4493:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-4494:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-4495:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-4496:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-4497:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-4498:

**MouseEvent** 



-------

.. _no-4499:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-4500:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-4501:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-4502:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-4503:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-4504:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-4505:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-4506:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-4507:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-4508:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-4509:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-4510:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-4511:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-4512:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-4513:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-4514:

**Move** 

Occurs when the control's position changes.



-------

.. _no-4515:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-4516:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-4517:

**SpinDown** 

Occurs when the spinner is decremented, either by clicking
the spinner 'down' button or by using the keyboard down arrow.




-------

.. _no-4518:

**SpinUp** 

Occurs when the spinner is incremented, either by clicking
the spinner 'up' button or by using the keyboard up arrow.




-------

.. _no-4519:

**Spinner** 

Occurs when the spinner is changed, either by clicking
one of the spinner buttons or by using the keyboard arrows.




-------

.. _no-4520:

**SpinnerEvent** 



-------

.. _no-4521:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-4522:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-4523:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-4524:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-4525>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-4526>`             Instantiate object as a child of self.
:ref:`afterInit <no-4527>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-4528>`          
:ref:`afterSetProperties <no-4529>`    
:ref:`autoBindEvents <no-4530>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-4531>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-4532>`   
:ref:`bindEvent <no-4533>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-4534>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-4535>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-4536>`          Makes this object topmost
:ref:`clear <no-4537>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-4538>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-4539>`  Given a position relative to this control, return a position relative
:ref:`copy <no-4540>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-4541>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-4542>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-4543>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-4544>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-4545>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-4546>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-4547>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-4548>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-4549>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-4550>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-4551>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-4552>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-4553>`              Draws text on the object at the specified position
:ref:`endHover <no-4554>`              
:ref:`fitToSizer <no-4555>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-4556>`            
:ref:`fontZoomIn <no-4557>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-4558>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-4559>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-4560>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-4561>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-4562>`         
:ref:`getCaptureBitmap <no-4563>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-4564>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-4565>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-4566>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-4567>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-4568>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-4569>`      
:ref:`getSizerProp <no-4570>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-4571>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-4572>`                  Make the object invisible.
:ref:`initEvents <no-4573>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-4574>`        
:ref:`isContainedBy <no-4575>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-4576>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-4577>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-4578>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-4579>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-4580>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-4581>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-4582>`               
:ref:`paste <no-4583>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-4584>`           
:ref:`processDroppedFiles <no-4585>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-4586>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-4587>`            Raise the passed Dabo event.
:ref:`reCreate <no-4588>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-4589>`              Recreate the object.
:ref:`redraw <no-4590>`                Called when the object is (re)drawn.
:ref:`refresh <no-4591>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-4592>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-4593>`               Destroys the object.
:ref:`removeDrawnObject <no-4594>`     
:ref:`restoreValue <no-4595>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-4596>`             Save control's value to dApp's user settings table.
:ref:`select <no-4597>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-4598>`             Select all text in the control.
:ref:`selectNone <no-4599>`            Select no text in the control.
:ref:`sendToBack <no-4600>`            Places this object behind all others.
:ref:`setAll <no-4601>`                Set all child object properties to the passed value.
:ref:`setFocus <no-4602>`              Sets focus to the object.
:ref:`setPositionInSizer <no-4603>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-4604>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-4605>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-4606>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-4607>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-4608>`                  Make the object visible.
:ref:`showContainingPage <no-4609>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-4610>`       Display a context menu (popup) at the specified position.
:ref:`super <no-4611>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-4612>`           Remove a previously registered event binding.
:ref:`unbindKey <no-4613>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-4614>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-4615>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-4616>`                Update control's value to match the current value from the source.

====================================== ========================


Methods - inherited
=====================

.. _no-4525:

.. function:: dabo.lib.datanav.Page.SelectSpinner.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4526:

.. function:: dabo.lib.datanav.Page.SelectSpinner.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-4527:

.. function:: dabo.lib.datanav.Page.SelectSpinner.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4528:

.. function:: dabo.lib.datanav.Page.SelectSpinner.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4529:

.. function:: dabo.lib.datanav.Page.SelectSpinner.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4530:

.. function:: dabo.lib.datanav.Page.SelectSpinner.autoBindEvents(self, force=True)
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

.. _no-4531:

.. function:: dabo.lib.datanav.Page.SelectSpinner.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4532:

.. function:: dabo.lib.datanav.Page.SelectSpinner.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4533:

.. function:: dabo.lib.datanav.Page.SelectSpinner.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-4534:

.. function:: dabo.lib.datanav.Page.SelectSpinner.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-4535:

.. function:: dabo.lib.datanav.Page.SelectSpinner.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-4536:

.. function:: dabo.lib.datanav.Page.SelectSpinner.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4537:

.. function:: dabo.lib.datanav.Page.SelectSpinner.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4538:

.. function:: dabo.lib.datanav.Page.SelectSpinner.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4539:

.. function:: dabo.lib.datanav.Page.SelectSpinner.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4540:

.. function:: dabo.lib.datanav.Page.SelectSpinner.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4541:

.. function:: dabo.lib.datanav.Page.SelectSpinner.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4542:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4543:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4544:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-4545:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4546:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4547:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4548:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4549:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4550:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4551:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4552:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4553:

.. function:: dabo.lib.datanav.Page.SelectSpinner.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4554:

.. function:: dabo.lib.datanav.Page.SelectSpinner.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4555:

.. function:: dabo.lib.datanav.Page.SelectSpinner.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4556:

.. function:: dabo.lib.datanav.Page.SelectSpinner.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4557:

.. function:: dabo.lib.datanav.Page.SelectSpinner.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4558:

.. function:: dabo.lib.datanav.Page.SelectSpinner.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4559:

.. function:: dabo.lib.datanav.Page.SelectSpinner.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4560:

.. function:: dabo.lib.datanav.Page.SelectSpinner.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4561:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4562:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSpinner.dSpinner`

-------

.. _no-4563:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4564:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4565:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4566:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4567:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4568:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-4569:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4570:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4571:

.. function:: dabo.lib.datanav.Page.SelectSpinner.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4572:

.. function:: dabo.lib.datanav.Page.SelectSpinner.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4573:

.. function:: dabo.lib.datanav.Page.SelectSpinner.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4574:

.. function:: dabo.lib.datanav.Page.SelectSpinner.initProperties(self)
   :noindex:



Inherited from: :ref:`dabo.lib.datanav.Page.SelectControlMixin`

-------

.. _no-4575:

.. function:: dabo.lib.datanav.Page.SelectSpinner.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4576:

.. function:: dabo.lib.datanav.Page.SelectSpinner.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4577:

.. function:: dabo.lib.datanav.Page.SelectSpinner.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-4578:

.. function:: dabo.lib.datanav.Page.SelectSpinner.lockDisplay(self)
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

.. _no-4579:

.. function:: dabo.lib.datanav.Page.SelectSpinner.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4580:

.. function:: dabo.lib.datanav.Page.SelectSpinner.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4581:

.. function:: dabo.lib.datanav.Page.SelectSpinner.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4582:

.. function:: dabo.lib.datanav.Page.SelectSpinner.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4583:

.. function:: dabo.lib.datanav.Page.SelectSpinner.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4584:

.. function:: dabo.lib.datanav.Page.SelectSpinner.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4585:

.. function:: dabo.lib.datanav.Page.SelectSpinner.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4586:

.. function:: dabo.lib.datanav.Page.SelectSpinner.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4587:

.. function:: dabo.lib.datanav.Page.SelectSpinner.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4588:

.. function:: dabo.lib.datanav.Page.SelectSpinner.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4589:

.. function:: dabo.lib.datanav.Page.SelectSpinner.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4590:

.. function:: dabo.lib.datanav.Page.SelectSpinner.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4591:

.. function:: dabo.lib.datanav.Page.SelectSpinner.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4592:

.. function:: dabo.lib.datanav.Page.SelectSpinner.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4593:

.. function:: dabo.lib.datanav.Page.SelectSpinner.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4594:

.. function:: dabo.lib.datanav.Page.SelectSpinner.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4595:

.. function:: dabo.lib.datanav.Page.SelectSpinner.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4596:

.. function:: dabo.lib.datanav.Page.SelectSpinner.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-4597:

.. function:: dabo.lib.datanav.Page.SelectSpinner.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-4598:

.. function:: dabo.lib.datanav.Page.SelectSpinner.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-4599:

.. function:: dabo.lib.datanav.Page.SelectSpinner.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-4600:

.. function:: dabo.lib.datanav.Page.SelectSpinner.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4601:

.. function:: dabo.lib.datanav.Page.SelectSpinner.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-4602:

.. function:: dabo.lib.datanav.Page.SelectSpinner.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4603:

.. function:: dabo.lib.datanav.Page.SelectSpinner.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4604:

.. function:: dabo.lib.datanav.Page.SelectSpinner.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-4605:

.. function:: dabo.lib.datanav.Page.SelectSpinner.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-4606:

.. function:: dabo.lib.datanav.Page.SelectSpinner.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4607:

.. function:: dabo.lib.datanav.Page.SelectSpinner.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4608:

.. function:: dabo.lib.datanav.Page.SelectSpinner.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4609:

.. function:: dabo.lib.datanav.Page.SelectSpinner.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4610:

.. function:: dabo.lib.datanav.Page.SelectSpinner.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4611:

.. function:: dabo.lib.datanav.Page.SelectSpinner.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4612:

.. function:: dabo.lib.datanav.Page.SelectSpinner.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-4613:

.. function:: dabo.lib.datanav.Page.SelectSpinner.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4614:

.. function:: dabo.lib.datanav.Page.SelectSpinner.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4615:

.. function:: dabo.lib.datanav.Page.SelectSpinner.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4616:

.. function:: dabo.lib.datanav.Page.SelectSpinner.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
