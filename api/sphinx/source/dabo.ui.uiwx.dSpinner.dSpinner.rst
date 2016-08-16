
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSpinner

.. _dabo.ui.uiwx.dSpinner.dSpinner:

==========================================
|doc_title|  **dSpinner.dSpinner** - class
==========================================


Control for allowing a user to increment a value by discreet steps across a range
of valid values.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSpinner**

.. inheritance-diagram:: dSpinner


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dDataPanel`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Page.SelectSpinner`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dSpinner.png
          :scale: 75 %
          :target: _static/macWidgets/dSpinner.png
          :alt: dSpinner



     - .. image:: _static/winWidgets/dSpinner.png
          :scale: 75 %
          :target: _static/winWidgets/dSpinner.png
          :alt: dSpinner



     - .. image:: _static/nixWidgets/dSpinner.png
          :scale: 75 %
          :target: _static/nixWidgets/dSpinner.png
          :alt: dSpinner


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSpinner.dSpinner

   .. automethod:: dabo.ui.uiwx.dSpinner.dSpinner.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-14201>`                
:ref:`Application <no-14202>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-14203>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-14204>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-14205>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-14206>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-14207>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-14208>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-14209>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-14210>`                   The position of the bottom side of the object. This is a
:ref:`ButtonWidth <no-14211>`              Allows the developer to explicitly specify the width of the up/down buttons.
:ref:`Caption <no-14212>`                  The caption of the object. (str)
:ref:`Children <no-14213>`                 Returns a list of object references to the children of
:ref:`Class <no-14214>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-14215>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-14216>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-14217>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-14218>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-14219>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-14220>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-14221>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-14222>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-14223>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-14224>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-14225>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-14226>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-14227>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-14228>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-14229>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-14230>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-14231>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-14232>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-14233>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-14234>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-14235>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-14236>`            Dynamically determine the value of the Height property.
:ref:`DynamicIncrement <no-14237>`         Dynamically determine the value of the Increment property.
:ref:`DynamicLeft <no-14238>`              Dynamically determine the value of the Left property.
:ref:`DynamicMax <no-14239>`               Dynamically determine the value of the Max property.
:ref:`DynamicMin <no-14240>`               Dynamically determine the value of the Min property.
:ref:`DynamicMousePointer <no-14241>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-14242>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-14243>`              Dynamically determine the value of the Size property.
:ref:`DynamicSpinnerWrap <no-14244>`       Dynamically determine the value of the SpinnerWrap property.
:ref:`DynamicStatusText <no-14245>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-14246>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-14247>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-14248>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-14249>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-14250>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-14251>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-14252>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-14253>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-14254>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-14255>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-14256>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-14257>`                 Specifies the font face. (str)
:ref:`FontInfo <no-14258>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-14259>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-14260>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-14261>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-14262>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-14263>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-14264>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-14265>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-14266>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`Increment <no-14267>`                Amount the control's value changes when the spinner buttons are clicked  (int/float)
:ref:`IsSecret <no-14268>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-14269>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-14270>`                Specifies which events to log.  (list of strings)
:ref:`Max <no-14271>`                      Maximum value for the control  (int/float)
:ref:`MaximumHeight <no-14272>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-14273>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-14274>`             Maximum allowable width for the control in pixels.  (int)
:ref:`Min <no-14275>`                      Minimum value for the control  (int/float)
:ref:`MinimumHeight <no-14276>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-14277>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-14278>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-14279>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-14280>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-14281>`                 Specifies the base name of the object.
:ref:`Parent <no-14282>`                   The containing object. (obj)
:ref:`PersistSecretData <no-14283>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-14284>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-14285>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-14286>`                 
:ref:`RegID <no-14287>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-14288>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-14289>`         Specifies whether the Value of the control gets saved when
:ref:`SelectOnEntry <no-14290>`            
:ref:`Size <no-14291>`                     The size of the object. (tuple)
:ref:`Sizer <no-14292>`                    The sizer for the object.
:ref:`Source <no-14293>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`SpinnerWrap <no-14294>`              Specifies whether the spinner value wraps at the high/low value. (bool)
:ref:`StatusText <no-14295>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-14296>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-14297>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-14298>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-14299>`                      The top position of the object. (int)
:ref:`Transparency <no-14300>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-14301>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-14302>`                    Value of the control  (int/float)
:ref:`Visible <no-14303>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-14304>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-14305>`                    The width of the object. (int)
:ref:`WindowHandle <no-14306>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-14211:

**ButtonWidth** 

Allows the developer to explicitly specify the width of the up/down buttons.



-------

.. _no-14237:

**DynamicIncrement** 

Dynamically determine the value of the Increment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Increment property. If DynamicIncrement is set to None (the default), Increment
will not be dynamically evaluated.



-------

.. _no-14239:

**DynamicMax** 

Dynamically determine the value of the Max property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Max property. If DynamicMax is set to None (the default), Max
will not be dynamically evaluated.



-------

.. _no-14240:

**DynamicMin** 

Dynamically determine the value of the Min property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Min property. If DynamicMin is set to None (the default), Min
will not be dynamically evaluated.



-------

.. _no-14244:

**DynamicSpinnerWrap** 

Dynamically determine the value of the SpinnerWrap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SpinnerWrap property. If DynamicSpinnerWrap is set to None (the default), SpinnerWrap
will not be dynamically evaluated.



-------

.. _no-14267:

**Increment** 

Amount the control's value changes when the spinner buttons are clicked  (int/float)



-------

.. _no-14271:

**Max** 

Maximum value for the control  (int/float)



-------

.. _no-14275:

**Min** 

Minimum value for the control  (int/float)



-------

.. _no-14286:

**ReadOnly** 



-------

.. _no-14290:

**SelectOnEntry** 



-------

.. _no-14294:

**SpinnerWrap** 

Specifies whether the spinner value wraps at the high/low value. (bool)



-------


Properties - inherited
========================

.. _no-14201:

**Alignment** 


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-14202:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14203:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14204:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14205:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14206:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14207:

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

.. _no-14208:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14209:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14210:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14212:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14213:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14214:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14215:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14216:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14217:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14218:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14219:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14220:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14221:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14222:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14223:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14224:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14225:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14226:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14227:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14228:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14229:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14230:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14231:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14232:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14233:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14234:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14235:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14236:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14238:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14241:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14242:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14243:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14245:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14246:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14247:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14248:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14249:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14250:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-14251:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14252:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14253:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14254:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14255:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14256:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14257:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14258:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14259:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14260:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14261:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14262:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14263:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14264:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14265:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14266:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14268:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14269:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14270:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14272:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14273:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14274:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14276:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14277:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14278:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14279:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14280:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14281:

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

.. _no-14282:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14283:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14284:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14285:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14287:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14288:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14289:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14291:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14292:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14293:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14295:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14296:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-14297:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14298:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14299:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14300:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14301:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14302:

**Value** 

Value of the control  (int/float)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14303:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14304:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14305:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14306:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-14307>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-14308>`                 Occurs after the control or form is created.
:ref:`Destroy <no-14309>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-14310>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-14311>`               Occurs when the control gets the focus.
:ref:`Hit <no-14312>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-14313>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-14314>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-14315>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-14316>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-14317>`               
:ref:`KeyUp <no-14318>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-14319>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-14320>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-14321>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-14322>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-14323>`             
:ref:`MouseLeave <no-14324>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-14325>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-14326>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-14327>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-14328>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-14329>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-14330>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-14331>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-14332>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-14333>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-14334>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-14335>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-14336>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-14337>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-14338>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-14339>`                   Occurs when the control's position changes.
:ref:`Paint <no-14340>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-14341>`                 Occurs when the control or form is resized.
:ref:`SpinDown <no-14342>`               Occurs when the spinner is decremented, either by clicking
:ref:`SpinUp <no-14343>`                 Occurs when the spinner is incremented, either by clicking
:ref:`Spinner <no-14344>`                Occurs when the spinner is changed, either by clicking
:ref:`SpinnerEvent <no-14345>`           
:ref:`TreeBeginDrag <no-14346>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-14347>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-14348>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-14349>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-14307:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-14308:

**Create** 

Occurs after the control or form is created.



-------

.. _no-14309:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-14310:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-14311:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-14312:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-14313:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-14314:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-14315:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-14316:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-14317:

**KeyEvent** 



-------

.. _no-14318:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-14319:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-14320:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-14321:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-14322:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-14323:

**MouseEvent** 



-------

.. _no-14324:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-14325:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-14326:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-14327:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-14328:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-14329:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-14330:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-14331:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-14332:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-14333:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-14334:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-14335:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-14336:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-14337:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-14338:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-14339:

**Move** 

Occurs when the control's position changes.



-------

.. _no-14340:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-14341:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-14342:

**SpinDown** 

Occurs when the spinner is decremented, either by clicking
the spinner 'down' button or by using the keyboard down arrow.




-------

.. _no-14343:

**SpinUp** 

Occurs when the spinner is incremented, either by clicking
the spinner 'up' button or by using the keyboard up arrow.




-------

.. _no-14344:

**Spinner** 

Occurs when the spinner is changed, either by clicking
one of the spinner buttons or by using the keyboard arrows.




-------

.. _no-14345:

**SpinnerEvent** 



-------

.. _no-14346:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-14347:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-14348:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-14349:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-14350>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-14351>`             Instantiate object as a child of self.
:ref:`afterInit <no-14352>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-14353>`          
:ref:`afterSetProperties <no-14354>`    
:ref:`autoBindEvents <no-14355>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-14356>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-14357>`   
:ref:`bindEvent <no-14358>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-14359>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-14360>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-14361>`          Makes this object topmost
:ref:`clear <no-14362>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-14363>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-14364>`  Given a position relative to this control, return a position relative
:ref:`copy <no-14365>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-14366>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-14367>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-14368>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-14369>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-14370>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-14371>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-14372>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-14373>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-14374>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-14375>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-14376>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-14377>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-14378>`              Draws text on the object at the specified position
:ref:`endHover <no-14379>`              
:ref:`fitToSizer <no-14380>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-14381>`            
:ref:`fontZoomIn <no-14382>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-14383>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-14384>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-14385>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-14386>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-14387>`         
:ref:`getCaptureBitmap <no-14388>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-14389>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-14390>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-14391>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-14392>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-14393>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-14394>`      
:ref:`getSizerProp <no-14395>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-14396>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-14397>`                  Make the object invisible.
:ref:`initEvents <no-14398>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-14399>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-14400>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-14401>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-14402>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-14403>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-14404>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-14405>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-14406>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-14407>`               
:ref:`paste <no-14408>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-14409>`           
:ref:`processDroppedFiles <no-14410>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-14411>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-14412>`            Raise the passed Dabo event.
:ref:`reCreate <no-14413>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-14414>`              Recreate the object.
:ref:`redraw <no-14415>`                Called when the object is (re)drawn.
:ref:`refresh <no-14416>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-14417>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-14418>`               Destroys the object.
:ref:`removeDrawnObject <no-14419>`     
:ref:`restoreValue <no-14420>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-14421>`             Save control's value to dApp's user settings table.
:ref:`select <no-14422>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-14423>`             Select all text in the control.
:ref:`selectNone <no-14424>`            Select no text in the control.
:ref:`sendToBack <no-14425>`            Places this object behind all others.
:ref:`setAll <no-14426>`                Set all child object properties to the passed value.
:ref:`setFocus <no-14427>`              Sets focus to the object.
:ref:`setPositionInSizer <no-14428>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-14429>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-14430>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-14431>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-14432>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-14433>`                  Make the object visible.
:ref:`showContainingPage <no-14434>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-14435>`       Display a context menu (popup) at the specified position.
:ref:`super <no-14436>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-14437>`           Remove a previously registered event binding.
:ref:`unbindKey <no-14438>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-14439>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-14440>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-14441>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-14381:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.flushValue(self)



-------

.. _no-14382:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.fontZoomIn(self, amt=1)

   Zoom in on the font, by setting a higher point size.



-------

.. _no-14383:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.fontZoomNormal(self)

   Reset the font zoom back to zero.



-------

.. _no-14384:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.fontZoomOut(self, amt=1)

   Zoom out on the font, by setting a lower point size.



-------

.. _no-14387:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getBlankValue(self)



-------


Methods - inherited
=====================

.. _no-14350:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14351:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-14352:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14353:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14354:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14355:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.autoBindEvents(self, force=True)
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

.. _no-14356:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14357:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14358:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14359:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14360:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-14361:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14362:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14363:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14364:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14365:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14366:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14367:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14368:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14369:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-14370:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14371:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14372:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14373:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14374:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14375:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14376:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14377:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14378:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14379:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14380:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14385:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14386:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14388:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14389:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14390:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14391:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14392:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14393:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-14394:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14395:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14396:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14397:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14398:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14399:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14400:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14401:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14402:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-14403:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.lockDisplay(self)
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

.. _no-14404:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14405:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14406:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14407:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14408:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14409:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14410:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14411:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14412:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14413:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14414:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14415:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14416:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14417:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14418:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14419:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14420:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14421:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-14422:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-14423:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-14424:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-14425:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14426:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-14427:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14428:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14429:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-14430:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-14431:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14432:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14433:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14434:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14435:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14436:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14437:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14438:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14439:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14440:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14441:

.. function:: dabo.ui.uiwx.dSpinner.dSpinner.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
