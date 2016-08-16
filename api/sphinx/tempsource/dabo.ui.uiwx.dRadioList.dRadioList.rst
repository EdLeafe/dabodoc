
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dRadioList

.. _dabo.ui.uiwx.dRadioList.dRadioList:

==============================================
|doc_title|  **dRadioList.dRadioList** - class
==============================================


Creates a group of radio buttons, allowing mutually-exclusive choices.

Like a dDropdownList, use this to present the user with multiple choices and
for them to choose from one of the choices. Where the dDropdownList is
suitable for lists of one to a couple hundred choices, a dRadioList is
really only suitable for lists of one to a dozen at most.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dRadioList**

.. inheritance-diagram:: dRadioList


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`



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



   * - no image available



     - .. image:: _static/winWidgets/dRadioList.png
          :scale: 75 %
          :target: _static/winWidgets/dRadioList.png
          :alt: dRadioList



     - .. image:: _static/nixWidgets/dRadioList.png
          :scale: 75 %
          :target: _static/nixWidgets/dRadioList.png
          :alt: dRadioList


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dRadioList.dRadioList

   .. automethod:: dabo.ui.uiwx.dRadioList.dRadioList.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-35214>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-35215>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-35216>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-35217>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-35218>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-35219>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-35220>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-35221>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-35222>`                   The position of the bottom side of the object. This is a
:ref:`ButtonClass <no-35223>`              Class to use for the radio buttons. Default=_dRadioButton  (dRadioButton)
:ref:`ButtonSpacing <no-35224>`            Spacing in pixels between buttons in the control  (int)
:ref:`Caption <no-35225>`                  String to display on the box surrounding the control  (str)
:ref:`Children <no-35226>`                 Returns a list of object references to the children of
:ref:`Choices <no-35227>`                  Specifies the string choices to display in the list.
:ref:`Class <no-35228>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-35229>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-35230>`     Reference to the sizer item that control's this control's layout.
:ref:`Count <no-35231>`                    Number of items in the control.
:ref:`DataField <no-35232>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-35233>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-35234>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-35235>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-35236>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-35237>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-35238>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-35239>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-35240>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-35241>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-35242>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-35243>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-35244>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-35245>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-35246>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-35247>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-35248>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-35249>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-35250>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-35251>`            Dynamically determine the value of the Height property.
:ref:`DynamicKeyValue <no-35252>`          Dynamically determine the value of the KeyValue property.
:ref:`DynamicLeft <no-35253>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-35254>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicOrientation <no-35255>`       Dynamically determine the value of the Orientation property.
:ref:`DynamicPosition <no-35256>`          Dynamically determine the value of the Position property.
:ref:`DynamicPositionValue <no-35257>`     Dynamically determine the value of the PositionValue property.
:ref:`DynamicSize <no-35258>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-35259>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStringValue <no-35260>`       Dynamically determine the value of the StringValue property.
:ref:`DynamicTag <no-35261>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-35262>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-35263>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-35264>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-35265>`             Dynamically determine the value of the Value property.
:ref:`DynamicValueMode <no-35266>`         Dynamically determine the value of the ValueMode property.
:ref:`DynamicVisible <no-35267>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-35268>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-35269>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-35270>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-35271>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-35272>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-35273>`                 Specifies the font face. (str)
:ref:`FontInfo <no-35274>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-35275>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-35276>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-35277>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-35278>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-35279>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-35280>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-35281>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-35282>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-35283>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`KeyValue <no-35284>`                 Specifies the key value or values of the selected item or items.
:ref:`Keys <no-35285>`                     Specifies a mapping between arbitrary values and item positions.
:ref:`Left <no-35286>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-35287>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-35288>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-35289>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-35290>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-35291>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-35292>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-35293>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-35294>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-35295>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-35296>`                 Specifies the base name of the object.
:ref:`Orientation <no-35297>`              Specifies whether this is a vertical or horizontal RadioList.
:ref:`Parent <no-35298>`                   The containing object. (obj)
:ref:`PersistSecretData <no-35299>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-35300>`                 The (x,y) position of the object. (tuple)
:ref:`PositionValue <no-35301>`            Specifies the position (index) of the selected button.
:ref:`PreferenceManager <no-35302>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-35303>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-35304>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-35305>`         Specifies whether the Value of the control gets saved when
:ref:`ShowBox <no-35306>`                  Is the surrounding box visible?  (bool)
:ref:`Size <no-35307>`                     The size of the object. (tuple)
:ref:`Sizer <no-35308>`                    The sizer for the object.
:ref:`SizerClass <no-35309>`               Class to use for the border sizer. Default=dabo.ui.dBorderSizer  (dSizer)
:ref:`SortFunction <no-35310>`             Function used to sort list items when Sorted=True. Default=None,
:ref:`Sorted <no-35311>`                   Are the items in the control automatically sorted? Default=False.
:ref:`Source <no-35312>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-35313>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StringValue <no-35314>`              Specifies the text of the selected button.
:ref:`TabStop <no-35315>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-35316>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-35317>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-35318>`                      The top position of the object. (int)
:ref:`Transparency <no-35319>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-35320>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-35321>`                    Specifies which item is currently selected in the list.
:ref:`ValueMode <no-35322>`                Specifies the information that the Value property refers to.
:ref:`Visible <no-35323>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-35324>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-35325>`                    The width of the object. (int)
:ref:`WindowHandle <no-35326>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-35223:

**ButtonClass** 

Class to use for the radio buttons. Default=_dRadioButton  (dRadioButton)



-------

.. _no-35224:

**ButtonSpacing** 

Spacing in pixels between buttons in the control  (int)



-------

.. _no-35255:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-35297:

**Orientation** 

Specifies whether this is a vertical or horizontal RadioList.
    String. Possible values:
        'Vertical' (the default)
        'Horizontal'



-------

.. _no-35306:

**ShowBox** 

Is the surrounding box visible?  (bool)



-------

.. _no-35309:

**SizerClass** 

Class to use for the border sizer. Default=dabo.ui.dBorderSizer  (dSizer)



-------


Properties - inherited
========================

.. _no-35214:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35215:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35216:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35217:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35218:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35219:

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

.. _no-35220:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35221:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35222:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35225:

**Caption** 

String to display on the box surrounding the control  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35226:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35227:

**Choices** 

Specifies the string choices to display in the list.
    -> List of strings. Read-write at runtime.
    The list index becomes the PositionValue, and the string
    becomes the StringValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35228:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35229:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35230:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35231:

**Count** 

Number of items in the control.
    -> Integer. Read-only.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35232:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35233:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35234:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35235:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35236:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35237:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35238:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35239:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35240:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35241:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35242:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35243:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35244:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35245:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35246:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35247:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35248:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35249:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35250:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35251:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35252:

**DynamicKeyValue** 

Dynamically determine the value of the KeyValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
KeyValue property. If DynamicKeyValue is set to None (the default), KeyValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35253:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35254:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35256:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35257:

**DynamicPositionValue** 

Dynamically determine the value of the PositionValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PositionValue property. If DynamicPositionValue is set to None (the default), PositionValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35258:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35259:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35260:

**DynamicStringValue** 

Dynamically determine the value of the StringValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StringValue property. If DynamicStringValue is set to None (the default), StringValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35261:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35262:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35263:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35264:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35265:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-35266:

**DynamicValueMode** 

Dynamically determine the value of the ValueMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueMode property. If DynamicValueMode is set to None (the default), ValueMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35267:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35268:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35269:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35270:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35271:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35272:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35273:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35274:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35275:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35276:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35277:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35278:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35279:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35280:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35281:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35282:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35283:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35284:

**KeyValue** 

Specifies the key value or values of the selected item or items.
    -> Type can vary. Read-write at runtime.
    Returns the key value or values of the selected item(s), or selects
    the item(s) with the specified KeyValue(s).    An exception will be
    raised if the Keys property hasn't been set up to accomodate.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35285:

**Keys** 

Specifies a mapping between arbitrary values and item positions.
    -> Dictionary. Read-write at runtime.
    The Keys property is a dictionary, where each key resolves into a
    list index (position). If using keys, you should update the Keys
    property whenever you update the Choices property, to make sure they
    are in sync.
    -> Optionally, Keys can be a list/tuple that is a 1:1 mapping of the
    Choices property. So if your 3rd Choices entry is selected, KeyValue
    will return the 3rd entry in the Keys property.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35286:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35287:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35288:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35289:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35290:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35291:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35292:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35293:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35294:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35295:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35296:

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

.. _no-35298:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35299:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35300:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35301:

**PositionValue** 

Specifies the position (index) of the selected button.
    Integer. Read-write at runtime.
    Returns the current position, or sets the current position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35302:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35303:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35304:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35305:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35307:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35308:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35310:

**SortFunction** 

Function used to sort list items when Sorted=True. Default=None,
    which gives the default sorting  (callable or None)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35311:

**Sorted** 

Are the items in the control automatically sorted? Default=False.
    If True, whenever the Choices property is changed, the resulting list
    will be first sorted using the SortFunction property, which defaults to
    None, giving a default sort order.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35312:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35313:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35314:

**StringValue** 

Specifies the text of the selected button.
    String. Read-write at runtime.
    Returns the text of the current item, or changes the current position
    to the position with the specified text. An exception is raised if there
    is no position with matching text.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35315:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-35316:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35317:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35318:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35319:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35320:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35321:

**Value** 

Specifies which item is currently selected in the list.
    -> Type can vary. Read-write at runtime.
    Value refers to one of the following, depending on the setting of ValueMode:

        + ValueMode="Position" : the index of the selected item(s) (integer)
        + ValueMode="String"   : the displayed string of the selected item(s) (string)
        + ValueMode="Key"      : the key of the selected item(s) (can vary)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35322:

**ValueMode** 

Specifies the information that the Value property refers to.
    -> String. Read-write at runtime.

    ============= =========================
    'Position'    Value refers to the position in the choices (integer).
    'String'      Value refers to the displayed string for the selection (default) (string).
    'Key'         Value refers to a separate key, set using the Keys property (can vary).
    ============= =========================

    


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35323:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35324:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35325:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35326:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-35327>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-35328>`                 Occurs after the control or form is created.
:ref:`Destroy <no-35329>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-35330>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-35331>`               Occurs when the control gets the focus.
:ref:`Hit <no-35332>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-35333>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-35334>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-35335>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-35336>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-35337>`               
:ref:`KeyUp <no-35338>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-35339>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-35340>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-35341>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-35342>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-35343>`             
:ref:`MouseLeave <no-35344>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-35345>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-35346>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-35347>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-35348>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-35349>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-35350>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-35351>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-35352>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-35353>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-35354>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-35355>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-35356>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-35357>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-35358>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-35359>`                   Occurs when the control's position changes.
:ref:`Paint <no-35360>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-35361>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-35362>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-35363>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-35364>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-35365>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-35327:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-35328:

**Create** 

Occurs after the control or form is created.



-------

.. _no-35329:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-35330:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-35331:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-35332:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-35333:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-35334:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-35335:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-35336:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-35337:

**KeyEvent** 



-------

.. _no-35338:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-35339:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-35340:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-35341:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-35342:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-35343:

**MouseEvent** 



-------

.. _no-35344:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-35345:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-35346:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-35347:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-35348:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-35349:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-35350:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-35351:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-35352:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-35353:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-35354:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-35355:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-35356:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-35357:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-35358:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-35359:

**Move** 

Occurs when the control's position changes.



-------

.. _no-35360:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-35361:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-35362:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-35363:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-35364:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-35365:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-35366>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-35367>`             Instantiate object as a child of self.
:ref:`afterInit <no-35368>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-35369>`          
:ref:`afterSetProperties <no-35370>`    
:ref:`appendItem <no-35371>`            Adds a new item to the end of the list
:ref:`autoBindEvents <no-35372>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-35373>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-35374>`   
:ref:`bindEvent <no-35375>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-35376>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-35377>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-35378>`          Makes this object topmost
:ref:`clear <no-35379>`                 Clears the background of custom-drawn objects.
:ref:`clearSelections <no-35380>`       Stub method. Only used in the list box, where there
:ref:`clone <no-35381>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-35382>`  Given a position relative to this control, return a position relative
:ref:`copy <no-35383>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-35384>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-35385>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-35386>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-35387>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-35388>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-35389>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-35390>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-35391>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-35392>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-35393>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-35394>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-35395>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-35396>`              Draws text on the object at the specified position
:ref:`enable <no-35397>`                Enables or disables an individual button.
:ref:`enableKey <no-35398>`             Enables or disables an individual button, referenced by key value.
:ref:`enablePosition <no-35399>`        Enables or disables an individual button, referenced by position (index).
:ref:`enableString <no-35400>`          Enables or disables an individual button, referenced by string display value.
:ref:`endHover <no-35401>`              
:ref:`fitToSizer <no-35402>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-35403>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-35404>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-35405>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-35406>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-35407>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-35408>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-35409>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-35410>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-35411>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-35412>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-35413>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-35414>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-35415>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-35416>`      
:ref:`getSizerProp <no-35417>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-35418>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-35419>`                  Make the object invisible.
:ref:`initEvents <no-35420>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-35421>`        Hook for subclasses. User subclasses should set properties
:ref:`insertItem <no-35422>`            Inserts a new item into the specified position.
:ref:`isContainedBy <no-35423>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-35424>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-35425>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-35426>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-35427>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-35428>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-35429>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-35430>`               
:ref:`paste <no-35431>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-35432>`           
:ref:`processDroppedFiles <no-35433>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-35434>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-35435>`            Raise the passed Dabo event.
:ref:`reCreate <no-35436>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-35437>`              Recreate the object.
:ref:`redraw <no-35438>`                Called when the object is (re)drawn.
:ref:`refresh <no-35439>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-35440>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-35441>`               Destroys the object.
:ref:`removeAll <no-35442>`             Removes all entries from the control.
:ref:`removeDrawnObject <no-35443>`     
:ref:`removeItem <no-35444>`            Removes the item at the specified position.
:ref:`restoreValue <no-35445>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-35446>`             Save control's value to dApp's user settings table.
:ref:`select <no-35447>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-35448>`             Select all text in the control.
:ref:`selectNone <no-35449>`            Select no text in the control.
:ref:`sendToBack <no-35450>`            Places this object behind all others.
:ref:`setAll <no-35451>`                Set all child object properties to the passed value.
:ref:`setFocus <no-35452>`              Sets focus to the object.
:ref:`setPositionInSizer <no-35453>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-35454>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-35455>` Sets a group of properties on the object all at once. This
:ref:`setSelection <no-35456>`          Same as setting property PositionValue.
:ref:`setSizerProp <no-35457>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-35458>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-35459>`                  Shows or hides an individual button.
:ref:`showContainingPage <no-35460>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-35461>`       Display a context menu (popup) at the specified position.
:ref:`showKey <no-35462>`               Shows or hides an individual button, referenced by key value.
:ref:`showPosition <no-35463>`          Shows or hides an individual button, referenced by position (index).
:ref:`showString <no-35464>`            Shows or hides an individual button, referenced by string display value.
:ref:`sort <no-35465>`                  Sorts the list items. By default, the Python 'cmp' function is
:ref:`super <no-35466>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-35467>`           Remove a previously registered event binding.
:ref:`unbindKey <no-35468>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-35469>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-35470>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-35471>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-35397:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.enable(self, itm, val=True)

   
   Enables or disables an individual button.
   
   The itm argument specifies which button to enable/disable, and its type
   depends on the setting of self.ValueType:
   
       ============ ====================
       "position"   The item is referenced by index position.
       "string"     The item is referenced by its string display value.
       "key"        The item is referenced by its key value.
       ============ ====================
   
   



-------

.. _no-35398:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.enableKey(self, itm, val=True)

   Enables or disables an individual button, referenced by key value.



-------

.. _no-35399:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.enablePosition(self, itm, val=True)

   Enables or disables an individual button, referenced by position (index).



-------

.. _no-35400:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.enableString(self, itm, val=True)

   Enables or disables an individual button, referenced by string display value.



-------

.. _no-35425:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.layout(self)

   Wrap the wx version of the call, if possible.



-------

.. _no-35459:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.show(self, itm, val=True)

   
   Shows or hides an individual button.
   
   The itm argument specifies which button to hide/show, and its type
   depends on the setting of self.ValueType:
   
       ============ ====================
       "position"   The item is referenced by index position.
       "string"     The item is referenced by its string display value.
       "key"        The item is referenced by its key value.
       ============ ====================
   
   



-------

.. _no-35462:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.showKey(self, itm, val=True)

   Shows or hides an individual button, referenced by key value.



-------

.. _no-35463:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.showPosition(self, itm, val=True)

   Shows or hides an individual button, referenced by position (index).



-------

.. _no-35464:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.showString(self, itm, val=True)

   Shows or hides an individual button, referenced by string display value.



-------


Methods - inherited
=====================

.. _no-35366:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35367:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-35368:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35369:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35370:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35371:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.appendItem(self, txt, select=False)
   :noindex:


   Adds a new item to the end of the list


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35372:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.autoBindEvents(self, force=True)
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

.. _no-35373:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35374:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35375:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35376:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35377:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-35378:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35379:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35380:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.clearSelections(self)
   :noindex:


   
   Stub method. Only used in the list box, where there
   can be multiple selections.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35381:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35382:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35383:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35384:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35385:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35386:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35387:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-35388:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35389:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35390:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35391:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35392:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35393:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35394:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35395:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35396:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35401:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35402:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35403:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35404:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35405:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35406:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35407:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35408:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35409:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35410:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35411:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35412:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35413:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35414:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35415:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-35416:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35417:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35418:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35419:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35420:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35421:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35422:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.insertItem(self, pos, txt, select=False)
   :noindex:


   Inserts a new item into the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35423:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35424:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35426:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.lockDisplay(self)
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

.. _no-35427:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35428:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35429:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35430:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35431:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35432:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35433:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35434:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35435:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35436:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35437:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35438:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35439:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35440:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35441:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35442:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.removeAll(self)
   :noindex:


   Removes all entries from the control.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35443:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35444:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.removeItem(self, pos)
   :noindex:


   Removes the item at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35445:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35446:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-35447:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-35448:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-35449:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-35450:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35451:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-35452:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35453:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35454:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-35455:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-35456:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setSelection(self, index)
   :noindex:


   Same as setting property PositionValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35457:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35458:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35460:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35461:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35465:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.sort(self, sortFunction=None)
   :noindex:


   
   Sorts the list items. By default, the Python 'cmp' function is
   used, but this can be overridden with a custom sortFunction.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-35466:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35467:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35468:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35469:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35470:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35471:

.. function:: dabo.ui.uiwx.dRadioList.dRadioList.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
