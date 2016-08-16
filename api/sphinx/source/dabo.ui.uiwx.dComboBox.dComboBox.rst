
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dComboBox

.. _dabo.ui.uiwx.dComboBox.dComboBox:

============================================
|doc_title|  **dComboBox.dComboBox** - class
============================================


Creates a combobox, which combines a dropdown list with a textbox.

The user can choose an item in the dropdown, or enter freeform text.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dComboBox**

.. inheritance-diagram:: dComboBox


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



   * - .. image:: _static/macWidgets/dComboBox.png
          :scale: 75 %
          :target: _static/macWidgets/dComboBox.png
          :alt: dComboBox



     - .. image:: _static/winWidgets/dComboBox.png
          :scale: 75 %
          :target: _static/winWidgets/dComboBox.png
          :alt: dComboBox



     - .. image:: _static/nixWidgets/dComboBox.png
          :scale: 75 %
          :target: _static/nixWidgets/dComboBox.png
          :alt: dComboBox


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dComboBox.dComboBox

   .. automethod:: dabo.ui.uiwx.dComboBox.dComboBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`AppendOnEnter <no-18333>`            Flag to determine if user-entered text is appended when they
:ref:`Application <no-18334>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-18335>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-18336>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-18337>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-18338>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-18339>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-18340>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-18341>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-18342>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-18343>`                  The caption of the object. (str)
:ref:`Children <no-18344>`                 Returns a list of object references to the children of
:ref:`Choices <no-18345>`                  Specifies the string choices to display in the list.
:ref:`Class <no-18346>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-18347>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-18348>`     Reference to the sizer item that control's this control's layout.
:ref:`Count <no-18349>`                    Number of items in the control.
:ref:`DataField <no-18350>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-18351>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-18352>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-18353>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-18354>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-18355>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-18356>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-18357>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-18358>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-18359>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-18360>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-18361>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-18362>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-18363>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-18364>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-18365>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-18366>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-18367>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-18368>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-18369>`            Dynamically determine the value of the Height property.
:ref:`DynamicKeyValue <no-18370>`          Dynamically determine the value of the KeyValue property.
:ref:`DynamicLeft <no-18371>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-18372>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-18373>`          Dynamically determine the value of the Position property.
:ref:`DynamicPositionValue <no-18374>`     Dynamically determine the value of the PositionValue property.
:ref:`DynamicSize <no-18375>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-18376>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStringValue <no-18377>`       Dynamically determine the value of the StringValue property.
:ref:`DynamicTag <no-18378>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-18379>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-18380>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-18381>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicUserValue <no-18382>`         Dynamically determine the value of the UserValue property.
:ref:`DynamicValue <no-18383>`             Dynamically determine the value of the Value property.
:ref:`DynamicValueMode <no-18384>`         Dynamically determine the value of the ValueMode property.
:ref:`DynamicVisible <no-18385>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-18386>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-18387>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-18388>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-18389>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-18390>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-18391>`                 Specifies the font face. (str)
:ref:`FontInfo <no-18392>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-18393>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-18394>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-18395>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-18396>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-18397>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-18398>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-18399>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-18400>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-18401>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-18402>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`KeyValue <no-18403>`                 Specifies the key value or values of the selected item or items.
:ref:`Keys <no-18404>`                     Specifies a mapping between arbitrary values and item positions.
:ref:`Left <no-18405>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-18406>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-18407>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-18408>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-18409>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-18410>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-18411>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-18412>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-18413>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-18414>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-18415>`                 Specifies the base name of the object.
:ref:`Parent <no-18416>`                   The containing object. (obj)
:ref:`PersistSecretData <no-18417>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-18418>`                 The (x,y) position of the object. (tuple)
:ref:`PositionValue <no-18419>`            Specifies the position (index) of the selected item(s).
:ref:`PreferenceManager <no-18420>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-18421>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-18422>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-18423>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-18424>`                     The size of the object. (tuple)
:ref:`Sizer <no-18425>`                    The sizer for the object.
:ref:`SortFunction <no-18426>`             Function used to sort list items when Sorted=True. Default=None,
:ref:`Sorted <no-18427>`                   Are the items in the control automatically sorted? Default=False.
:ref:`Source <no-18428>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-18429>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StringValue <no-18430>`              Specifies the text of the selected item.
:ref:`TabStop <no-18431>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-18432>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-18433>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-18434>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-18435>`                      The top position of the object. (int)
:ref:`Transparency <no-18436>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-18437>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UserValue <no-18438>`                Specifies the text displayed in the textbox portion of the ComboBox.
:ref:`Value <no-18439>`                    Specifies which item is currently selected in the list.
:ref:`ValueMode <no-18440>`                Specifies the information that the Value property refers to.
:ref:`Visible <no-18441>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-18442>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-18443>`                    The width of the object. (int)
:ref:`WindowHandle <no-18444>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-18333:

**AppendOnEnter** 

Flag to determine if user-entered text is appended when they
    press 'Enter'  (bool)



-------

.. _no-18382:

**DynamicUserValue** 

Dynamically determine the value of the UserValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UserValue property. If DynamicUserValue is set to None (the default), UserValue
will not be dynamically evaluated.



-------

.. _no-18396:

**ForceCase** 

Determines if we change the case of entered text. Possible values are:

        ============ =====================
        None or ""   No changes made (default)
        "Upper"      FORCE TO UPPER CASE
        "Lower"      Force to lower case
        "Title"      Force To Title Case
        ============ =====================

    These can be abbreviated to "u", "l" or "t"  (str)



-------

.. _no-18433:

**TextLength** 

The maximum length the entered text can be. (int)



-------

.. _no-18438:

**UserValue** 

Specifies the text displayed in the textbox portion of the ComboBox.

    String. Read-write at runtime.

    UserValue can differ from StringValue, which would mean that the user
    has typed in arbitrary text. Unlike StringValue, PositionValue, and
    KeyValue, setting UserValue does not change the currently selected item
    in the list portion of the ComboBox.



-------


Properties - inherited
========================

.. _no-18334:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18335:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18336:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18337:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18338:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18339:

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

.. _no-18340:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18341:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18342:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18343:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18344:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18345:

**Choices** 

Specifies the string choices to display in the list.
    -> List of strings. Read-write at runtime.
    The list index becomes the PositionValue, and the string
    becomes the StringValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18346:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18347:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18348:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18349:

**Count** 

Number of items in the control.
    -> Integer. Read-only.


Inherited from: 'wx._core.ItemContainer - can not provide a link

-------

.. _no-18350:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18351:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18352:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18353:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18354:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18355:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18356:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18357:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18358:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18359:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18360:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18361:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18362:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18363:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18364:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18365:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18366:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18367:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18368:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18369:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18370:

**DynamicKeyValue** 

Dynamically determine the value of the KeyValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
KeyValue property. If DynamicKeyValue is set to None (the default), KeyValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18371:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18372:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18373:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18374:

**DynamicPositionValue** 

Dynamically determine the value of the PositionValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PositionValue property. If DynamicPositionValue is set to None (the default), PositionValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18375:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18376:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18377:

**DynamicStringValue** 

Dynamically determine the value of the StringValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StringValue property. If DynamicStringValue is set to None (the default), StringValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18378:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18379:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18380:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18381:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18383:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-18384:

**DynamicValueMode** 

Dynamically determine the value of the ValueMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueMode property. If DynamicValueMode is set to None (the default), ValueMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18385:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18386:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18387:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18388:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18389:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18390:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18391:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18392:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18393:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18394:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18395:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18397:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18398:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18399:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18400:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18401:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18402:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18403:

**KeyValue** 

Specifies the key value or values of the selected item or items.
    -> Type can vary. Read-write at runtime.
    Returns the key value or values of the selected item(s), or selects
    the item(s) with the specified KeyValue(s).    An exception will be
    raised if the Keys property hasn't been set up to accomodate.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18404:

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

.. _no-18405:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18406:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18407:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18408:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18409:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18410:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18411:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18412:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18413:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18414:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18415:

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

.. _no-18416:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18417:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18418:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18419:

**PositionValue** 

Specifies the position (index) of the selected item(s).
    -> Integer or tuple of integers. Read-write at runtime.
    Returns the current position(s), or sets the current position(s).


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18420:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18421:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18422:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18423:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18424:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18425:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18426:

**SortFunction** 

Function used to sort list items when Sorted=True. Default=None,
    which gives the default sorting  (callable or None)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18427:

**Sorted** 

Are the items in the control automatically sorted? Default=False.
    If True, whenever the Choices property is changed, the resulting list
    will be first sorted using the SortFunction property, which defaults to
    None, giving a default sort order.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18428:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18429:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18430:

**StringValue** 

Specifies the text of the selected item.
    -> String or tuple of strings. Read-write at runtime.
    Returns the text of the selected item(s), or selects the item(s)
    with the specified text. An exception is raised if there is no
    position with matching text.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18431:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-18432:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18434:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18435:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18436:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18437:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18439:

**Value** 

Specifies which item is currently selected in the list.
    -> Type can vary. Read-write at runtime.
    Value refers to one of the following, depending on the setting of ValueMode:

        + ValueMode="Position" : the index of the selected item(s) (integer)
        + ValueMode="String"   : the displayed string of the selected item(s) (string)
        + ValueMode="Key"      : the key of the selected item(s) (can vary)


Inherited from: 'wx._controls.ComboBox - can not provide a link

-------

.. _no-18440:

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

.. _no-18441:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18442:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18443:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18444:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-18445>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-18446>`                 Occurs after the control or form is created.
:ref:`Destroy <no-18447>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-18448>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-18449>`               Occurs when the control gets the focus.
:ref:`Hit <no-18450>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-18451>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-18452>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-18453>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-18454>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-18455>`               
:ref:`KeyUp <no-18456>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-18457>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-18458>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-18459>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-18460>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-18461>`             
:ref:`MouseLeave <no-18462>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-18463>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-18464>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-18465>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-18466>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-18467>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-18468>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-18469>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-18470>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-18471>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-18472>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-18473>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-18474>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-18475>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-18476>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-18477>`                   Occurs when the control's position changes.
:ref:`Paint <no-18478>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-18479>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-18480>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-18481>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-18482>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-18483>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-18445:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-18446:

**Create** 

Occurs after the control or form is created.



-------

.. _no-18447:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-18448:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-18449:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-18450:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-18451:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-18452:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-18453:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-18454:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-18455:

**KeyEvent** 



-------

.. _no-18456:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-18457:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-18458:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-18459:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-18460:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-18461:

**MouseEvent** 



-------

.. _no-18462:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-18463:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-18464:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-18465:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-18466:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-18467:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-18468:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-18469:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-18470:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-18471:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-18472:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-18473:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-18474:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-18475:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-18476:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-18477:

**Move** 

Occurs when the control's position changes.



-------

.. _no-18478:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-18479:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-18480:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-18481:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-18482:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-18483:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-18484>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-18485>`             Instantiate object as a child of self.
:ref:`afterAppendOnEnter <no-18486>`    Hook method that provides a means to interact with the newly-
:ref:`afterInit <no-18487>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-18488>`          
:ref:`afterSetProperties <no-18489>`    
:ref:`appendItem <no-18490>`            Adds a new item to the end of the list
:ref:`autoBindEvents <no-18491>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeAppendOnEnter <no-18492>`   Hook method that is called when user-defined text is entered
:ref:`beforeInit <no-18493>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-18494>`   
:ref:`bindEvent <no-18495>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-18496>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-18497>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-18498>`          Makes this object topmost
:ref:`clear <no-18499>`                 Clears the background of custom-drawn objects.
:ref:`clearSelections <no-18500>`       Stub method. Only used in the list box, where there
:ref:`clone <no-18501>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-18502>`  Given a position relative to this control, return a position relative
:ref:`copy <no-18503>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-18504>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-18505>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-18506>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-18507>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-18508>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-18509>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-18510>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-18511>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-18512>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-18513>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-18514>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-18515>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-18516>`              Draws text on the object at the specified position
:ref:`endHover <no-18517>`              
:ref:`fitToSizer <no-18518>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-18519>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-18520>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-18521>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-18522>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-18523>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-18524>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-18525>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-18526>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-18527>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-18528>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-18529>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-18530>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-18531>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-18532>`      
:ref:`getSizerProp <no-18533>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-18534>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-18535>`                  Make the object invisible.
:ref:`initEvents <no-18536>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-18537>`        Hook for subclasses. User subclasses should set properties
:ref:`insertItem <no-18538>`            Inserts a new item into the specified position.
:ref:`isContainedBy <no-18539>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-18540>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-18541>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-18542>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-18543>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-18544>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-18545>`               
:ref:`paste <no-18546>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-18547>`           
:ref:`processDroppedFiles <no-18548>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-18549>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-18550>`            Raise the passed Dabo event.
:ref:`reCreate <no-18551>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-18552>`              Recreate the object.
:ref:`redraw <no-18553>`                Called when the object is (re)drawn.
:ref:`refresh <no-18554>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-18555>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-18556>`               Destroys the object.
:ref:`removeAll <no-18557>`             Removes all entries from the control.
:ref:`removeDrawnObject <no-18558>`     
:ref:`removeItem <no-18559>`            Removes the item at the specified position.
:ref:`restoreValue <no-18560>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-18561>`             Save control's value to dApp's user settings table.
:ref:`select <no-18562>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-18563>`             Select all text in the control.
:ref:`selectNone <no-18564>`            Select no text in the control.
:ref:`sendToBack <no-18565>`            Places this object behind all others.
:ref:`setAll <no-18566>`                Set all child object properties to the passed value.
:ref:`setFocus <no-18567>`              Sets focus to the object.
:ref:`setPositionInSizer <no-18568>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-18569>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-18570>` Sets a group of properties on the object all at once. This
:ref:`setSelection <no-18571>`          Same as setting property PositionValue.
:ref:`setSizerProp <no-18572>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-18573>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-18574>`                  Make the object visible.
:ref:`showContainingPage <no-18575>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-18576>`       Display a context menu (popup) at the specified position.
:ref:`sort <no-18577>`                  Sorts the list items. By default, the Python 'cmp' function is
:ref:`super <no-18578>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-18579>`           Remove a previously registered event binding.
:ref:`unbindKey <no-18580>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-18581>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-18582>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-18583>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-18486:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.afterAppendOnEnter(self)

   
   Hook method that provides a means to interact with the newly-
   changed list of items after a new item has been added by the user
   pressing Enter, but before control returns to the program.
   



-------

.. _no-18492:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.beforeAppendOnEnter(self)

   
   Hook method that is called when user-defined text is entered
   into the combo box and Enter is pressed (when self.AppendOnEnter
   is True). This gives the programmer the ability to interact with such
   events, and optionally prevent them from happening. Returning
   False will prevent the append from happening.
   
   The text value to be appended is stored in self._textToAppend. You
   may modify this value (e.g., force to upper case), or delete it entirely
   (e.g., filter out obscenities and such). If you set self._textToAppend
   to an empty string, nothing will be appended. So this 'before' hook
   gives you two opportunities to prevent the append: return a non-
   empty value, or clear out self._textToAppend.
   



-------


Methods - inherited
=====================

.. _no-18484:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18485:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-18487:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18488:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18489:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18490:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.appendItem(self, txt, select=False)
   :noindex:


   Adds a new item to the end of the list


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18491:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.autoBindEvents(self, force=True)
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

.. _no-18493:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18494:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18495:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18496:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18497:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-18498:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18499:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18500:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.clearSelections(self)
   :noindex:


   
   Stub method. Only used in the list box, where there
   can be multiple selections.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18501:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18502:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18503:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18504:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18505:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18506:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18507:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-18508:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18509:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18510:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18511:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18512:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18513:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18514:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18515:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18516:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18517:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18518:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18519:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18520:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18521:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18522:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18523:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18524:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18525:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18526:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18527:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18528:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18529:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18530:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18531:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-18532:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18533:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18534:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18535:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18536:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18537:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18538:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.insertItem(self, pos, txt, select=False)
   :noindex:


   Inserts a new item into the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18539:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18540:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18541:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.lockDisplay(self)
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

.. _no-18542:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18543:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18544:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18545:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18546:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18547:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18548:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18549:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18550:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18551:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18552:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18553:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18554:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18555:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18556:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18557:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.removeAll(self)
   :noindex:


   Removes all entries from the control.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18558:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18559:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.removeItem(self, pos)
   :noindex:


   Removes the item at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18560:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18561:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-18562:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-18563:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-18564:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-18565:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18566:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-18567:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18568:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18569:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-18570:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-18571:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setSelection(self, index)
   :noindex:


   Same as setting property PositionValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18572:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18573:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18574:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18575:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18576:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18577:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.sort(self, sortFunction=None)
   :noindex:


   
   Sorts the list items. By default, the Python 'cmp' function is
   used, but this can be overridden with a custom sortFunction.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-18578:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18579:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18580:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18581:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18582:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18583:

.. function:: dabo.ui.uiwx.dComboBox.dComboBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
