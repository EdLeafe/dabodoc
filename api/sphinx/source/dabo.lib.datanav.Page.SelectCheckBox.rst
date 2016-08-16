
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.SelectCheckBox:

============================================
|doc_title|  **Page.SelectCheckBox** - class
============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SelectCheckBox**

.. inheritance-diagram:: SelectCheckBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.datanav.Page.SelectControlMixin`
* :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.SelectCheckBox


|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Alignment <no-3190>`                Specifies the alignment of the text.
:ref:`Application <no-3191>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-3192>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-3193>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-3194>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-3195>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-3196>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-3197>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-3198>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-3199>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-3200>`                  The caption of the object. (str)
:ref:`Children <no-3201>`                 Returns a list of object references to the children of
:ref:`Class <no-3202>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-3203>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-3204>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-3205>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-3206>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-3207>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-3208>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-3209>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-3210>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-3211>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-3212>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-3213>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-3214>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-3215>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-3216>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-3217>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-3218>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-3219>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-3220>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-3221>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-3222>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-3223>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-3224>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-3225>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-3226>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-3227>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-3228>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-3229>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-3230>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-3231>`               Dynamically determine the value of the Tag property.
:ref:`DynamicThreeState <no-3232>`        Dynamically determine the value of the ThreeState property.
:ref:`DynamicToolTipText <no-3233>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-3234>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-3235>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicUserThreeState <no-3236>`    Dynamically determine the value of the UserThreeState property.
:ref:`DynamicValue <no-3237>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-3238>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-3239>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-3240>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-3241>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-3242>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-3243>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-3244>`                 Specifies the font face. (str)
:ref:`FontInfo <no-3245>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-3246>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-3247>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-3248>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-3249>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-3250>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-3251>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-3252>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-3253>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-3254>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-3255>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-3256>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-3257>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-3258>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-3259>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-3260>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-3261>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-3262>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-3263>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-3264>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-3265>`                 Specifies the base name of the object.
:ref:`Parent <no-3266>`                   The containing object. (obj)
:ref:`PersistSecretData <no-3267>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-3268>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-3269>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-3270>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-3271>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-3272>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-3273>`                     The size of the object. (tuple)
:ref:`Sizer <no-3274>`                    The sizer for the object.
:ref:`Source <no-3275>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-3276>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-3277>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-3278>`                      A property that user code can safely use for specific purposes.
:ref:`ThreeState <no-3279>`               Specifies wether the checkbox support 3 states.
:ref:`ToolTipText <no-3280>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-3281>`                      The top position of the object. (int)
:ref:`Transparency <no-3282>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-3283>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UserThreeState <no-3284>`           Specifies whether the user is allowed to set the third state.
:ref:`Value <no-3285>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-3286>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-3287>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-3288>`                    The width of the object. (int)
:ref:`WindowHandle <no-3289>`             The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties - inherited
========================

.. _no-3190:

**Alignment** 

Specifies the alignment of the text.

        Left  : Checkbox to left of text (default)
        Right : Checkbox to right of text


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-3191:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3192:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3193:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3194:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3195:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3196:

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

.. _no-3197:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3198:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3199:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3200:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3201:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3202:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3203:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3204:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3205:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3206:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3207:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3208:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3209:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3210:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`

-------

.. _no-3211:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3212:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3213:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3214:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3215:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3216:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3217:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3218:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3219:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3220:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3221:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3222:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3223:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3224:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3225:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3226:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3227:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3228:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3229:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3230:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3231:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3232:

**DynamicThreeState** 

Dynamically determine the value of the ThreeState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ThreeState property. If DynamicThreeState is set to None (the default), ThreeState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`

-------

.. _no-3233:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3234:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3235:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3236:

**DynamicUserThreeState** 

Dynamically determine the value of the UserThreeState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UserThreeState property. If DynamicUserThreeState is set to None (the default), UserThreeState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`

-------

.. _no-3237:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-3238:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3239:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3240:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3241:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3242:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3243:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3244:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3245:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3246:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3247:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3248:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3249:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3250:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3251:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3252:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3253:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3254:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3255:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3256:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3257:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3258:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3259:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3260:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3261:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3262:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3263:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3264:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3265:

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

.. _no-3266:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3267:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3268:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3269:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3270:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3271:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3272:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3273:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3274:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-3275:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3276:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3277:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-3278:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3279:

**ThreeState** 

Specifies wether the checkbox support 3 states.

        True  : Checkbox supports 3 states
        False : Checkbox supports 2 states (default)


Inherited from: :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`

-------

.. _no-3280:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3281:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3282:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3283:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3284:

**UserThreeState** 

Specifies whether the user is allowed to set the third state.

        True  : User is allowed to set the third state.
        False : User isn't allowed to set the third state.(default)


Inherited from: :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`

-------

.. _no-3285:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: 'wx._controls.CheckBox - can not provide a link

-------

.. _no-3286:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3287:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3288:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3289:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-3290>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-3291>`                 Occurs after the control or form is created.
:ref:`Destroy <no-3292>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-3293>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-3294>`               Occurs when the control gets the focus.
:ref:`Hit <no-3295>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-3296>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-3297>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-3298>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-3299>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-3300>`               
:ref:`KeyUp <no-3301>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-3302>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-3303>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-3304>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-3305>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-3306>`             
:ref:`MouseLeave <no-3307>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-3308>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-3309>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-3310>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-3311>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-3312>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-3313>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-3314>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-3315>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-3316>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-3317>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-3318>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-3319>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-3320>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-3321>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-3322>`                   Occurs when the control's position changes.
:ref:`Paint <no-3323>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-3324>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-3325>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-3326>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-3327>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-3328>`           Occurs when the control's value has changed, whether

======================================= ========================


Events
=======

.. _no-3290:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-3291:

**Create** 

Occurs after the control or form is created.



-------

.. _no-3292:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-3293:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-3294:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-3295:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-3296:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-3297:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-3298:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-3299:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-3300:

**KeyEvent** 



-------

.. _no-3301:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-3302:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-3303:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-3304:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-3305:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-3306:

**MouseEvent** 



-------

.. _no-3307:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-3308:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-3309:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-3310:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-3311:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-3312:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-3313:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-3314:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-3315:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-3316:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-3317:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-3318:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-3319:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-3320:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-3321:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-3322:

**Move** 

Occurs when the control's position changes.



-------

.. _no-3323:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-3324:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-3325:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-3326:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-3327:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-3328:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-3329>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-3330>`             Instantiate object as a child of self.
:ref:`afterInit <no-3331>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-3332>`          
:ref:`afterSetProperties <no-3333>`    
:ref:`autoBindEvents <no-3334>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-3335>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-3336>`   
:ref:`bindEvent <no-3337>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-3338>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-3339>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-3340>`          Makes this object topmost
:ref:`clear <no-3341>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-3342>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-3343>`  Given a position relative to this control, return a position relative
:ref:`copy <no-3344>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-3345>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-3346>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-3347>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-3348>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-3349>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-3350>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-3351>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-3352>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-3353>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-3354>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-3355>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-3356>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-3357>`              Draws text on the object at the specified position
:ref:`endHover <no-3358>`              
:ref:`fitToSizer <no-3359>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-3360>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-3361>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-3362>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-3363>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-3364>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-3365>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-3366>`         
:ref:`getCaptureBitmap <no-3367>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-3368>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-3369>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-3370>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-3371>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-3372>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-3373>`      
:ref:`getSizerProp <no-3374>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-3375>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-3376>`                  Make the object invisible.
:ref:`initEvents <no-3377>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-3378>`        
:ref:`isContainedBy <no-3379>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-3380>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-3381>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-3382>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-3383>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-3384>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-3385>`               
:ref:`paste <no-3386>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-3387>`           
:ref:`processDroppedFiles <no-3388>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-3389>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-3390>`            Raise the passed Dabo event.
:ref:`reCreate <no-3391>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-3392>`              Recreate the object.
:ref:`redraw <no-3393>`                Called when the object is (re)drawn.
:ref:`refresh <no-3394>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-3395>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-3396>`               Destroys the object.
:ref:`removeDrawnObject <no-3397>`     
:ref:`restoreValue <no-3398>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-3399>`             Save control's value to dApp's user settings table.
:ref:`select <no-3400>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-3401>`             Select all text in the control.
:ref:`selectNone <no-3402>`            Select no text in the control.
:ref:`sendToBack <no-3403>`            Places this object behind all others.
:ref:`setAll <no-3404>`                Set all child object properties to the passed value.
:ref:`setFocus <no-3405>`              Sets focus to the object.
:ref:`setPositionInSizer <no-3406>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-3407>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-3408>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-3409>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-3410>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-3411>`                  Make the object visible.
:ref:`showContainingPage <no-3412>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-3413>`       Display a context menu (popup) at the specified position.
:ref:`super <no-3414>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-3415>`           Remove a previously registered event binding.
:ref:`unbindKey <no-3416>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-3417>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-3418>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-3419>`                Update control's value to match the current value from the source.

====================================== ========================


Methods - inherited
=====================

.. _no-3329:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3330:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-3331:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3332:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3333:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3334:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.autoBindEvents(self, force=True)
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

.. _no-3335:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3336:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3337:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3338:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3339:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-3340:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3341:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3342:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3343:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3344:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3345:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3346:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3347:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3348:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-3349:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3350:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3351:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3352:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3353:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3354:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3355:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3356:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3357:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3358:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3359:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3360:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3361:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3362:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3363:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3364:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3365:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3366:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCheckBox.dCheckBox`

-------

.. _no-3367:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3368:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3369:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3370:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3371:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3372:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-3373:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3374:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3375:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3376:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3377:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3378:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.initProperties(self)
   :noindex:



Inherited from: :ref:`dabo.lib.datanav.Page.SelectControlMixin`

-------

.. _no-3379:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3380:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3381:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.lockDisplay(self)
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

.. _no-3382:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3383:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3384:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3385:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3386:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3387:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3388:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3389:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3390:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3391:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-3392:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3393:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3394:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3395:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3396:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3397:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3398:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3399:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-3400:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-3401:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-3402:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-3403:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3404:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-3405:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3406:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3407:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-3408:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-3409:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3410:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3411:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3412:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3413:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3414:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-3415:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-3416:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3417:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3418:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-3419:

.. function:: dabo.lib.datanav.Page.SelectCheckBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
