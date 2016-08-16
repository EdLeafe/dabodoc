
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dCheckList

.. _dabo.ui.uiwx.dCheckList.dCheckList:

==============================================
|doc_title|  **dCheckList.dCheckList** - class
==============================================


Creates a listbox, allowing the user to choose one or more items
by checking/unchecking each one.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dCheckList**

.. inheritance-diagram:: dCheckList


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dCheckListBox`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dCheckList.png
          :scale: 75 %
          :target: _static/macWidgets/dCheckList.png
          :alt: dCheckList



     - .. image:: _static/winWidgets/dCheckList.png
          :scale: 75 %
          :target: _static/winWidgets/dCheckList.png
          :alt: dCheckList



     - .. image:: _static/nixWidgets/dCheckList.png
          :scale: 75 %
          :target: _static/nixWidgets/dCheckList.png
          :alt: dCheckList


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dCheckList.dCheckList

   .. automethod:: dabo.ui.uiwx.dCheckList.dCheckList.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-31591>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-31592>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-31593>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-31594>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-31595>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-31596>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-31597>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-31598>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-31599>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-31600>`                  The caption of the object. (str)
:ref:`Children <no-31601>`                 Returns a list of object references to the children of
:ref:`Choices <no-31602>`                  Specifies the string choices to display in the list.
:ref:`Class <no-31603>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-31604>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-31605>`     Reference to the sizer item that control's this control's layout.
:ref:`Count <no-31606>`                    Number of items in the control.
:ref:`DataField <no-31607>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-31608>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-31609>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-31610>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-31611>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-31612>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-31613>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-31614>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-31615>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-31616>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-31617>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-31618>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-31619>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-31620>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-31621>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-31622>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-31623>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-31624>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-31625>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-31626>`            Dynamically determine the value of the Height property.
:ref:`DynamicKeyValue <no-31627>`          Dynamically determine the value of the KeyValue property.
:ref:`DynamicLeft <no-31628>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-31629>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-31630>`          Dynamically determine the value of the Position property.
:ref:`DynamicPositionValue <no-31631>`     Dynamically determine the value of the PositionValue property.
:ref:`DynamicSize <no-31632>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-31633>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStringValue <no-31634>`       Dynamically determine the value of the StringValue property.
:ref:`DynamicTag <no-31635>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-31636>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-31637>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-31638>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-31639>`             Dynamically determine the value of the Value property.
:ref:`DynamicValueMode <no-31640>`         Dynamically determine the value of the ValueMode property.
:ref:`DynamicVisible <no-31641>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-31642>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-31643>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-31644>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-31645>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-31646>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-31647>`                 Specifies the font face. (str)
:ref:`FontInfo <no-31648>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-31649>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-31650>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-31651>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-31652>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-31653>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-31654>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-31655>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-31656>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-31657>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`KeyValue <no-31658>`                 Specifies the key value or values of the selected item or items.
:ref:`Keys <no-31659>`                     Specifies a mapping between arbitrary values and item positions.
:ref:`Left <no-31660>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-31661>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-31662>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-31663>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-31664>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-31665>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-31666>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-31667>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-31668>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`MultipleSelect <no-31669>`           MultipleSelect for dCheckList is always True.
:ref:`Name <no-31670>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-31671>`                 Specifies the base name of the object.
:ref:`Parent <no-31672>`                   The containing object. (obj)
:ref:`PersistSecretData <no-31673>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-31674>`                 The (x,y) position of the object. (tuple)
:ref:`PositionValue <no-31675>`            Specifies the position (index) of the selected item(s).
:ref:`PreferenceManager <no-31676>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-31677>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-31678>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-31679>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-31680>`                     The size of the object. (tuple)
:ref:`Sizer <no-31681>`                    The sizer for the object.
:ref:`SortFunction <no-31682>`             Function used to sort list items when Sorted=True. Default=None,
:ref:`Sorted <no-31683>`                   Are the items in the control automatically sorted? Default=False.
:ref:`Source <no-31684>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-31685>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StringValue <no-31686>`              Specifies the text of the selected item.
:ref:`TabStop <no-31687>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-31688>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-31689>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-31690>`                      The top position of the object. (int)
:ref:`Transparency <no-31691>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-31692>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-31693>`                    Specifies which item is currently selected in the list.
:ref:`ValueMode <no-31694>`                Specifies the information that the Value property refers to.
:ref:`Visible <no-31695>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-31696>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-31697>`                    The width of the object. (int)
:ref:`WindowHandle <no-31698>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-31669:

**MultipleSelect** 

MultipleSelect for dCheckList is always True.



-------


Properties - inherited
========================

.. _no-31591:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31592:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31593:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31594:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31595:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31596:

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

.. _no-31597:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31598:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31599:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31600:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31601:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31602:

**Choices** 

Specifies the string choices to display in the list.
    -> List of strings. Read-write at runtime.
    The list index becomes the PositionValue, and the string
    becomes the StringValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31603:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31604:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31605:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31606:

**Count** 

Number of items in the control.
    -> Integer. Read-only.


Inherited from: 'wx._core.ItemContainer - can not provide a link

-------

.. _no-31607:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31608:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31609:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31610:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31611:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31612:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31613:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31614:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31615:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31616:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31617:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31618:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31619:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31620:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31621:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31622:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31623:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31624:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31625:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31626:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31627:

**DynamicKeyValue** 

Dynamically determine the value of the KeyValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
KeyValue property. If DynamicKeyValue is set to None (the default), KeyValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31628:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31629:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31630:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31631:

**DynamicPositionValue** 

Dynamically determine the value of the PositionValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PositionValue property. If DynamicPositionValue is set to None (the default), PositionValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31632:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31633:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31634:

**DynamicStringValue** 

Dynamically determine the value of the StringValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StringValue property. If DynamicStringValue is set to None (the default), StringValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31635:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31636:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31637:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31638:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31639:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31640:

**DynamicValueMode** 

Dynamically determine the value of the ValueMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueMode property. If DynamicValueMode is set to None (the default), ValueMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31641:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31642:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31643:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31644:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31645:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31646:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31647:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31648:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31649:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31650:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31651:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31652:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31653:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31654:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31655:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31656:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31657:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31658:

**KeyValue** 

Specifies the key value or values of the selected item or items.
    -> Type can vary. Read-write at runtime.
    Returns the key value or values of the selected item(s), or selects
    the item(s) with the specified KeyValue(s).    An exception will be
    raised if the Keys property hasn't been set up to accomodate.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31659:

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

.. _no-31660:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31661:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31662:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31663:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31664:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31665:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31666:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31667:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31668:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31670:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31671:

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

.. _no-31672:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31673:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31674:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31675:

**PositionValue** 

Specifies the position (index) of the selected item(s).
    -> Integer or tuple of integers. Read-write at runtime.
    Returns the current position(s), or sets the current position(s).


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31676:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31677:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31678:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31679:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31680:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31681:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-31682:

**SortFunction** 

Function used to sort list items when Sorted=True. Default=None,
    which gives the default sorting  (callable or None)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31683:

**Sorted** 

Are the items in the control automatically sorted? Default=False.
    If True, whenever the Choices property is changed, the resulting list
    will be first sorted using the SortFunction property, which defaults to
    None, giving a default sort order.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31684:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31685:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31686:

**StringValue** 

Specifies the text of the selected item.
    -> String or tuple of strings. Read-write at runtime.
    Returns the text of the selected item(s), or selects the item(s)
    with the specified text. An exception is raised if there is no
    position with matching text.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31687:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-31688:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31689:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31690:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31691:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31692:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31693:

**Value** 

Specifies which item is currently selected in the list.
    -> Type can vary. Read-write at runtime.
    Value refers to one of the following, depending on the setting of ValueMode:

        + ValueMode="Position" : the index of the selected item(s) (integer)
        + ValueMode="String"   : the displayed string of the selected item(s) (string)
        + ValueMode="Key"      : the key of the selected item(s) (can vary)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31694:

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

.. _no-31695:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31696:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31697:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31698:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-31699>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-31700>`                 Occurs after the control or form is created.
:ref:`Destroy <no-31701>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-31702>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-31703>`               Occurs when the control gets the focus.
:ref:`Idle <no-31704>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-31705>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-31706>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-31707>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-31708>`               
:ref:`KeyUp <no-31709>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-31710>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-31711>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-31712>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-31713>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-31714>`             
:ref:`MouseLeave <no-31715>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-31716>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-31717>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-31718>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-31719>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-31720>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-31721>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-31722>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-31723>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-31724>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-31725>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-31726>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-31727>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-31728>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-31729>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-31730>`                   Occurs when the control's position changes.
:ref:`Paint <no-31731>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-31732>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-31733>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-31734>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-31735>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-31736>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-31699:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-31700:

**Create** 

Occurs after the control or form is created.



-------

.. _no-31701:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-31702:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-31703:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-31704:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-31705:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-31706:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-31707:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-31708:

**KeyEvent** 



-------

.. _no-31709:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-31710:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-31711:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-31712:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-31713:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-31714:

**MouseEvent** 



-------

.. _no-31715:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-31716:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-31717:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-31718:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-31719:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-31720:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-31721:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-31722:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-31723:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-31724:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-31725:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-31726:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-31727:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-31728:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-31729:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-31730:

**Move** 

Occurs when the control's position changes.



-------

.. _no-31731:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-31732:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-31733:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-31734:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-31735:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-31736:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-31737>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-31738>`             Instantiate object as a child of self.
:ref:`afterInit <no-31739>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-31740>`          
:ref:`afterSetProperties <no-31741>`    
:ref:`appendItem <no-31742>`            Adds a new item to the end of the list
:ref:`autoBindEvents <no-31743>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-31744>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-31745>`   
:ref:`bindEvent <no-31746>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-31747>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-31748>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-31749>`          Makes this object topmost
:ref:`clear <no-31750>`                 Clears the background of custom-drawn objects.
:ref:`clearSelections <no-31751>`       Set all items to unchecked.
:ref:`clone <no-31752>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-31753>`  Given a position relative to this control, return a position relative
:ref:`copy <no-31754>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-31755>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-31756>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-31757>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-31758>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-31759>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-31760>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-31761>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-31762>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-31763>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-31764>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-31765>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-31766>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-31767>`              Draws text on the object at the specified position
:ref:`endHover <no-31768>`              
:ref:`fitToSizer <no-31769>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-31770>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-31771>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-31772>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-31773>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-31774>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-31775>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-31776>`         Return the empty value of the control.
:ref:`getCaptureBitmap <no-31777>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-31778>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-31779>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-31780>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-31781>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-31782>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-31783>`      
:ref:`getSizerProp <no-31784>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-31785>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-31786>`                  Make the object invisible.
:ref:`initEvents <no-31787>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-31788>`        Hook for subclasses. User subclasses should set properties
:ref:`insertItem <no-31789>`            Inserts a new item into the specified position.
:ref:`invertSelections <no-31790>`      Switch all the items from False to True, and vice-versa.
:ref:`isContainedBy <no-31791>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-31792>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-31793>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-31794>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-31795>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-31796>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-31797>`               
:ref:`paste <no-31798>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-31799>`           
:ref:`processDroppedFiles <no-31800>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-31801>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-31802>`            Raise the passed Dabo event.
:ref:`reCreate <no-31803>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-31804>`              Recreate the object.
:ref:`redraw <no-31805>`                Called when the object is (re)drawn.
:ref:`refresh <no-31806>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-31807>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-31808>`               Destroys the object.
:ref:`removeAll <no-31809>`             Removes all entries from the control.
:ref:`removeDrawnObject <no-31810>`     
:ref:`removeItem <no-31811>`            Removes the item at the specified position.
:ref:`restoreValue <no-31812>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-31813>`             Save control's value to dApp's user settings table.
:ref:`select <no-31814>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-31815>`             Set all items to checked.
:ref:`selectNone <no-31816>`            Set all items to unchecked.
:ref:`sendToBack <no-31817>`            Places this object behind all others.
:ref:`setAll <no-31818>`                Set all child object properties to the passed value.
:ref:`setFocus <no-31819>`              Sets focus to the object.
:ref:`setPositionInSizer <no-31820>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-31821>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-31822>` Sets a group of properties on the object all at once. This
:ref:`setSelection <no-31823>`          
:ref:`setSizerProp <no-31824>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-31825>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-31826>`                  Make the object visible.
:ref:`showContainingPage <no-31827>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-31828>`       Display a context menu (popup) at the specified position.
:ref:`sort <no-31829>`                  Sorts the list items. By default, the Python 'cmp' function is
:ref:`super <no-31830>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-31831>`           Remove a previously registered event binding.
:ref:`unbindKey <no-31832>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-31833>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-31834>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-31835>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-31751:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.clearSelections(self)

   Set all items to unchecked.



-------

.. _no-31790:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.invertSelections(self)

   Switch all the items from False to True, and vice-versa.



-------

.. _no-31815:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.selectAll(self)

   Set all items to checked.



-------

.. _no-31816:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.selectNone(self)

   Set all items to unchecked.



-------

.. _no-31823:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setSelection(self, index)



-------


Methods - inherited
=====================

.. _no-31737:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31738:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-31739:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31740:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31741:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31742:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.appendItem(self, txt, select=False)
   :noindex:


   Adds a new item to the end of the list


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31743:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.autoBindEvents(self, force=True)
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

.. _no-31744:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31745:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31746:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31747:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31748:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-31749:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31750:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31752:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31753:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31754:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31755:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31756:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31757:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31758:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-31759:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31760:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31761:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31762:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31763:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31764:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31765:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31766:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31767:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31768:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31769:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31770:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31771:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31772:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31773:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31774:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31775:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31776:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31777:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31778:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31779:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31780:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31781:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31782:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-31783:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31784:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31785:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31786:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31787:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31788:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31789:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.insertItem(self, pos, txt, select=False)
   :noindex:


   Inserts a new item into the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31791:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31792:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31793:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.lockDisplay(self)
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

.. _no-31794:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31795:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31796:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31797:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31798:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31799:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31800:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31801:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31802:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31803:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-31804:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31805:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31806:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31807:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31808:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31809:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.removeAll(self)
   :noindex:


   Removes all entries from the control.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31810:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31811:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.removeItem(self, pos)
   :noindex:


   Removes the item at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31812:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31813:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-31814:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-31817:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31818:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-31819:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31820:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31821:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-31822:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-31824:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31825:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31826:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31827:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31828:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31829:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.sort(self, sortFunction=None)
   :noindex:


   
   Sorts the list items. By default, the Python 'cmp' function is
   used, but this can be overridden with a custom sortFunction.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-31830:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-31831:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-31832:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31833:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31834:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-31835:

.. function:: dabo.ui.uiwx.dCheckList.dCheckList.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
