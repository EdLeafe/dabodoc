
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dListControl

.. _dabo.ui.uiwx.dListControl.dListControl:

==================================================
|doc_title|  **dListControl.dListControl** - class
==================================================


Creates a list control, which is a flexible, virtual list box.

The List Control is ideal for visually dealing with data sets where each
'row' is a unit, where it doesn't make sense to deal with individual
elements inside of the row. If you need to be able to work with individual
elements, you should use a dGrid.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dListControl**

.. inheritance-diagram:: dListControl


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



   * - .. image:: _static/macWidgets/dListControl.png
          :scale: 75 %
          :target: _static/macWidgets/dListControl.png
          :alt: dListControl



     - .. image:: _static/winWidgets/dListControl.png
          :scale: 75 %
          :target: _static/winWidgets/dListControl.png
          :alt: dListControl



     - .. image:: _static/nixWidgets/dListControl.png
          :scale: 75 %
          :target: _static/nixWidgets/dListControl.png
          :alt: dListControl


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dListControl.dListControl

   .. automethod:: dabo.ui.uiwx.dListControl.dListControl.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-28681>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoConvertToString <no-28682>`      When True (default), all non-string values are forced to strings. When False,
:ref:`BackColor <no-28683>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-28684>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-28685>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-28686>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-28687>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-28688>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-28689>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-28690>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-28691>`                  The caption of the object. (str)
:ref:`Children <no-28692>`                 Returns a list of object references to the children of
:ref:`Choices <no-28693>`                  Since dListControl doesn't have the equivalent to 'Choices' as the
:ref:`Class <no-28694>`                    The class the object is based on. Read-only.  (class)
:ref:`ColumnCount <no-28695>`              Number of columns in the control  (int)
:ref:`Columns <no-28696>`                  Reference to the columns in the control. (read-only) (list)
:ref:`ColumnsAlignment <no-28697>`         Columns data alignment, the 'Left', 'Center' or 'Right' literals can be used
:ref:`ControllingSizer <no-28698>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-28699>`     Reference to the sizer item that control's this control's layout.
:ref:`Count <no-28700>`                    Number of rows in the control (read-only). Alias for RowCount  (int)
:ref:`DataField <no-28701>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-28702>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-28703>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-28704>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-28705>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-28706>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-28707>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-28708>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-28709>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-28710>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-28711>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-28712>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-28713>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-28714>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-28715>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-28716>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-28717>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-28718>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-28719>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeaderVisible <no-28720>`     Dynamically determine the value of the HeaderVisible property.
:ref:`DynamicHeight <no-28721>`            Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalRules <no-28722>`   Dynamically determine the value of the HorizontalRules property.
:ref:`DynamicKeyValue <no-28723>`          Dynamically determine the value of the KeyValue property.
:ref:`DynamicLeft <no-28724>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-28725>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicMultipleSelect <no-28726>`    Dynamically determine the value of the MultipleSelect property.
:ref:`DynamicPosition <no-28727>`          Dynamically determine the value of the Position property.
:ref:`DynamicPositionValue <no-28728>`     Dynamically determine the value of the PositionValue property.
:ref:`DynamicSize <no-28729>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-28730>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStringValue <no-28731>`       Dynamically determine the value of the StringValue property.
:ref:`DynamicTag <no-28732>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-28733>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-28734>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-28735>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-28736>`             Dynamically determine the value of the Value property.
:ref:`DynamicValueColumn <no-28737>`       Dynamically determine the value of the ValueColumn property.
:ref:`DynamicValueMode <no-28738>`         Dynamically determine the value of the ValueMode property.
:ref:`DynamicVerticalRules <no-28739>`     Dynamically determine the value of the VerticalRules property.
:ref:`DynamicVisible <no-28740>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-28741>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-28742>`                  Specifies whether the object and children can get user input. (bool)
:ref:`ExpandColumn <no-28743>`             Designates the column to expand to fill the control when ExpandToFit is True.
:ref:`ExpandToFit <no-28744>`              When True (default), the column designated by ExpandColumn expands to fill the width of the control.
:ref:`Font <no-28745>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-28746>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-28747>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-28748>`                 Specifies the font face. (str)
:ref:`FontInfo <no-28749>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-28750>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-28751>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-28752>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-28753>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-28754>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`HeaderVisible <no-28755>`            Specifies whether the header is shown or not.
:ref:`Height <no-28756>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-28757>`          Specifies the context-sensitive help text associated with this
:ref:`HitIndex <no-28758>`                 Returns the index of the last hit item.
:ref:`HorizontalRules <no-28759>`          Specifies whether light rules are drawn between rows.
:ref:`Hover <no-28760>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-28761>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`KeyValue <no-28762>`                 Specifies the key value or values of the selected item or items.
:ref:`Keys <no-28763>`                     Specifies a mapping between arbitrary values and item positions.
:ref:`LastSelectedIndex <no-28764>`        Returns the index of the last selected item.
:ref:`Left <no-28765>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-28766>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-28767>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-28768>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-28769>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-28770>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-28771>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-28772>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-28773>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`MultipleSelect <no-28774>`           Specifies whether multiple rows can be selected in the list.
:ref:`Name <no-28775>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-28776>`                 Specifies the base name of the object.
:ref:`Parent <no-28777>`                   The containing object. (obj)
:ref:`PersistSecretData <no-28778>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-28779>`                 The (x,y) position of the object. (tuple)
:ref:`PositionValue <no-28780>`            Specifies the position (index) of the selected item(s).
:ref:`PreferenceManager <no-28781>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-28782>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-28783>`                    The position of the right side of the object. This is a
:ref:`RowCount <no-28784>`                 Number of rows in the control (read-only).  (int)
:ref:`SaveRestoreValue <no-28785>`         Specifies whether the Value of the control gets saved when
:ref:`SelectedIndices <no-28786>`          Returns a list of selected row indices.  (list of int)
:ref:`Size <no-28787>`                     The size of the object. (tuple)
:ref:`Sizer <no-28788>`                    The sizer for the object.
:ref:`SortColumn <no-28789>`               Column to be sorted when sort() is called. Default=0  (int)
:ref:`SortFunction <no-28790>`             Function used to sort list items when Sorted=True. Default=None,
:ref:`SortOnHeaderClick <no-28791>`        When True (default), clicking a column header cycles the sorting on that column.  (bool)
:ref:`Sorted <no-28792>`                   Are the items in the control automatically sorted? Default=False.
:ref:`Source <no-28793>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-28794>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StringValue <no-28795>`              Specifies the text of the selected item.
:ref:`TabStop <no-28796>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-28797>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-28798>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-28799>`                      The top position of the object. (int)
:ref:`Transparency <no-28800>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-28801>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-28802>`                    Returns current value (str)
:ref:`ValueColumn <no-28803>`              The column whose text is reflected in Value (default=0).  (int)
:ref:`ValueMode <no-28804>`                Specifies the information that the Value property refers to.
:ref:`Values <no-28805>`                   Returns a list containing the Value of all selected rows  (list of str)
:ref:`VerticalRules <no-28806>`            Specifies whether light rules are drawn between rows.
:ref:`Visible <no-28807>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-28808>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-28809>`                    The width of the object. (int)
:ref:`WindowHandle <no-28810>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-28682:

**AutoConvertToString** 

When True (default), all non-string values are forced to strings. When False,
    attempting to use a non-string value will throw an error.  (bool)



-------

.. _no-28696:

**Columns** 

Reference to the columns in the control. (read-only) (list)



-------

.. _no-28697:

**ColumnsAlignment** 

Columns data alignment, the 'Left', 'Center' or 'Right' literals can be used
    or their abbreviations, e.g. ('c', 'l', 'r').  (tuple of str)



-------

.. _no-28720:

**DynamicHeaderVisible** 

Dynamically determine the value of the HeaderVisible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderVisible property. If DynamicHeaderVisible is set to None (the default), HeaderVisible
will not be dynamically evaluated.



-------

.. _no-28722:

**DynamicHorizontalRules** 

Dynamically determine the value of the HorizontalRules property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalRules property. If DynamicHorizontalRules is set to None (the default), HorizontalRules
will not be dynamically evaluated.



-------

.. _no-28726:

**DynamicMultipleSelect** 

Dynamically determine the value of the MultipleSelect property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MultipleSelect property. If DynamicMultipleSelect is set to None (the default), MultipleSelect
will not be dynamically evaluated.



-------

.. _no-28737:

**DynamicValueColumn** 

Dynamically determine the value of the ValueColumn property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueColumn property. If DynamicValueColumn is set to None (the default), ValueColumn
will not be dynamically evaluated.



-------

.. _no-28739:

**DynamicVerticalRules** 

Dynamically determine the value of the VerticalRules property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalRules property. If DynamicVerticalRules is set to None (the default), VerticalRules
will not be dynamically evaluated.



-------

.. _no-28743:

**ExpandColumn** 

Designates the column to expand to fill the control when ExpandToFit is True.
    Can either be an integer specifying the column number, or the string 'LAST' (default),
    which will expand the rightmost column.  (int or str)



-------

.. _no-28744:

**ExpandToFit** 

When True (default), the column designated by ExpandColumn expands to fill the width of the control.  (bool)



-------

.. _no-28755:

**HeaderVisible** 

Specifies whether the header is shown or not.



-------

.. _no-28758:

**HitIndex** 

Returns the index of the last hit item.



-------

.. _no-28759:

**HorizontalRules** 

Specifies whether light rules are drawn between rows.



-------

.. _no-28764:

**LastSelectedIndex** 

Returns the index of the last selected item.



-------

.. _no-28774:

**MultipleSelect** 

Specifies whether multiple rows can be selected in the list.



-------

.. _no-28784:

**RowCount** 

Number of rows in the control (read-only).  (int)



-------

.. _no-28786:

**SelectedIndices** 

Returns a list of selected row indices.  (list of int)



-------

.. _no-28789:

**SortColumn** 

Column to be sorted when sort() is called. Default=0  (int)



-------

.. _no-28791:

**SortOnHeaderClick** 

When True (default), clicking a column header cycles the sorting on that column.  (bool)



-------

.. _no-28803:

**ValueColumn** 

The column whose text is reflected in Value (default=0).  (int)



-------

.. _no-28805:

**Values** 

Returns a list containing the Value of all selected rows  (list of str)



-------

.. _no-28806:

**VerticalRules** 

Specifies whether light rules are drawn between rows.



-------


Properties - inherited
========================

.. _no-28681:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28683:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28684:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28685:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28686:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28687:

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

.. _no-28688:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28689:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28690:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28691:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28692:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28693:

**Choices** 

Since dListControl doesn't have the equivalent to 'Choices' as the
    other item controls do, this will return an empty list and print a warning
    message. (read-only) (list)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28694:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28695:

**ColumnCount** 

Number of columns in the control  (int)


Inherited from: 'wx._controls.ListCtrl - can not provide a link

-------

.. _no-28698:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28699:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28700:

**Count** 

Number of rows in the control (read-only). Alias for RowCount  (int)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28701:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28702:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28703:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28704:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28705:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28706:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28707:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28708:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28709:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28710:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28711:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28712:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28713:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28714:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28715:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28716:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28717:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28718:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28719:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28721:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28723:

**DynamicKeyValue** 

Dynamically determine the value of the KeyValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
KeyValue property. If DynamicKeyValue is set to None (the default), KeyValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28724:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28725:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28727:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28728:

**DynamicPositionValue** 

Dynamically determine the value of the PositionValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PositionValue property. If DynamicPositionValue is set to None (the default), PositionValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28729:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28730:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28731:

**DynamicStringValue** 

Dynamically determine the value of the StringValue property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StringValue property. If DynamicStringValue is set to None (the default), StringValue
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28732:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28733:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28734:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28735:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28736:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-28738:

**DynamicValueMode** 

Dynamically determine the value of the ValueMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ValueMode property. If DynamicValueMode is set to None (the default), ValueMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28740:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28741:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28742:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28745:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28746:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28747:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28748:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28749:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28750:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28751:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28752:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28753:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28754:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28756:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28757:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28760:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28761:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28762:

**KeyValue** 

Specifies the key value or values of the selected item or items.
    -> Type can vary. Read-write at runtime.
    Returns the key value or values of the selected item(s), or selects
    the item(s) with the specified KeyValue(s).    An exception will be
    raised if the Keys property hasn't been set up to accomodate.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28763:

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

.. _no-28765:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28766:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28767:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28768:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28769:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28770:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28771:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28772:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28773:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28775:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28776:

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

.. _no-28777:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28778:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28779:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28780:

**PositionValue** 

Specifies the position (index) of the selected item(s).
    -> Integer or tuple of integers. Read-write at runtime.
    Returns the current position(s), or sets the current position(s).


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28781:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28782:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28783:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28785:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28787:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28788:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28790:

**SortFunction** 

Function used to sort list items when Sorted=True. Default=None,
    which gives the default sorting  (callable or None)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28792:

**Sorted** 

Are the items in the control automatically sorted? Default=False.
    If True, whenever the Choices property is changed, the resulting list
    will be first sorted using the SortFunction property, which defaults to
    None, giving a default sort order.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28793:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28794:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28795:

**StringValue** 

Specifies the text of the selected item.
    -> String or tuple of strings. Read-write at runtime.
    Returns the text of the selected item(s), or selects the item(s)
    with the specified text. An exception is raised if there is no
    position with matching text.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28796:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-28797:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28798:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28799:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28800:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28801:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28802:

**Value** 

Returns current value (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28804:

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

.. _no-28807:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28808:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28809:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28810:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-28811>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-28812>`                 Occurs after the control or form is created.
:ref:`Destroy <no-28813>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-28814>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-28815>`               Occurs when the control gets the focus.
:ref:`Idle <no-28816>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-28817>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-28818>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-28819>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-28820>`               
:ref:`KeyUp <no-28821>`                  Occurs when any key is released on the focused control or form.
:ref:`ListControlEvent <no-28822>`       
:ref:`ListDeselection <no-28823>`        Occurs when a selected item is deselected in a list control.
:ref:`ListSelection <no-28824>`          Occurs when an item is highlighted in a list control.
:ref:`LostFocus <no-28825>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-28826>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-28827>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-28828>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-28829>`             
:ref:`MouseLeave <no-28830>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-28831>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-28832>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-28833>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-28834>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-28835>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-28836>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-28837>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-28838>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-28839>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-28840>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-28841>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-28842>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-28843>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-28844>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-28845>`                   Occurs when the control's position changes.
:ref:`Paint <no-28846>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-28847>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-28848>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-28849>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-28850>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-28851>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-28811:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-28812:

**Create** 

Occurs after the control or form is created.



-------

.. _no-28813:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-28814:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-28815:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-28816:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-28817:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-28818:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-28819:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-28820:

**KeyEvent** 



-------

.. _no-28821:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-28822:

**ListControlEvent** 



-------

.. _no-28823:

**ListDeselection** 

 Occurs when a selected item is deselected in a list control.



-------

.. _no-28824:

**ListSelection** 

 Occurs when an item is highlighted in a list control.



-------

.. _no-28825:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-28826:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-28827:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-28828:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-28829:

**MouseEvent** 



-------

.. _no-28830:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-28831:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-28832:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-28833:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-28834:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-28835:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-28836:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-28837:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-28838:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-28839:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-28840:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-28841:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-28842:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-28843:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-28844:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-28845:

**Move** 

Occurs when the control's position changes.



-------

.. _no-28846:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-28847:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-28848:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-28849:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-28850:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-28851:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-28852>`   Translates a position value for a control to absolute screen position.
:ref:`addColumn <no-28853>`             Add a column with the selected caption.
:ref:`addImage <no-28854>`              Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-28855>`             Instantiate object as a child of self.
:ref:`afterInit <no-28856>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-28857>`          
:ref:`afterSetProperties <no-28858>`    
:ref:`append <no-28859>`                Appends a row with the associated text in the specified column.
:ref:`appendItem <no-28860>`            Adds a new item to the end of the list
:ref:`appendRows <no-28861>`            Accepts a list/tuple of data. Each element in the sequence
:ref:`autoBindEvents <no-28862>`        Automatically bind any on*() methods to the associated event.
:ref:`autoSizeColumn <no-28863>`        Auto-sizes the specified column.
:ref:`autoSizeColumns <no-28864>`       Auto-sizes all the columns.
:ref:`beforeInit <no-28865>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-28866>`   
:ref:`bindEvent <no-28867>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-28868>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-28869>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-28870>`          Makes this object topmost
:ref:`clear <no-28871>`                 Remove all the rows in the control.
:ref:`clearSelections <no-28872>`       Stub method. Only used in the list box, where there
:ref:`clone <no-28873>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-28874>`  Given a position relative to this control, return a position relative
:ref:`copy <no-28875>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-28876>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-28877>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-28878>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-28879>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-28880>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-28881>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-28882>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-28883>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-28884>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-28885>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-28886>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-28887>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-28888>`              Draws text on the object at the specified position
:ref:`endHover <no-28889>`              
:ref:`fitToSizer <no-28890>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-28891>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-28892>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-28893>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-28894>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-28895>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-28896>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-28897>`         Return the empty value of the control.
:ref:`getCaptionForColumn <no-28898>`   Convenience method for getting the caption for a given column number.
:ref:`getCaptureBitmap <no-28899>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getColumnWidth <no-28900>`        
:ref:`getContainingPage <no-28901>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-28902>`      Returns an object that locks the current display when created, and
:ref:`getItemBackColor <no-28903>`      
:ref:`getItemData <no-28904>`           Retrieve the data associated with the item.
:ref:`getItemForeColor <no-28905>`      
:ref:`getItemImg <no-28906>`            Returns the index of the specified item's image in the
:ref:`getMousePosition <no-28907>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-28908>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-28909>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-28910>`      
:ref:`getSizerProp <no-28911>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-28912>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-28913>`                  Make the object invisible.
:ref:`initEvents <no-28914>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-28915>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-28916>`                Inserts the item at the specified row, or at the beginning if no
:ref:`insertColumn <no-28917>`          Inserts a column at the specified position
:ref:`insertItem <no-28918>`            Inserts a new item into the specified position.
:ref:`insertRows <no-28919>`            Accepts a list/tuple of data. Each element in the sequence
:ref:`isContainedBy <no-28920>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-28921>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-28922>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-28923>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-28924>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-28925>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-28926>`               
:ref:`paste <no-28927>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-28928>`           
:ref:`processDroppedFiles <no-28929>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-28930>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-28931>`            Raise the passed Dabo event.
:ref:`reCreate <no-28932>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-28933>`              Recreate the object.
:ref:`redraw <no-28934>`                Called when the object is (re)drawn.
:ref:`refresh <no-28935>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-28936>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-28937>`               Destroys the object.
:ref:`removeAll <no-28938>`             Remove all the rows in the control.
:ref:`removeColumn <no-28939>`          Removes the specified column, or the last column if
:ref:`removeDrawnObject <no-28940>`     
:ref:`removeItem <no-28941>`            Removes the item at the specified position.
:ref:`removeRow <no-28942>`             Deletes the specified row if it exists, or generates a warning
:ref:`resizeColumn <no-28943>`          
:ref:`resizeLastColumn <no-28944>`      Resize the last column appropriately.
:ref:`restoreValue <no-28945>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-28946>`             Save control's value to dApp's user settings table.
:ref:`select <no-28947>`                Selects the specified row. In a MultipleSelect control, any
:ref:`selectAll <no-28948>`             Selects all rows in a MultipleSelect control, or generates a
:ref:`selectNone <no-28949>`            De-selects all rows.
:ref:`selectOnly <no-28950>`            Selects the specified row. In a MultipleSelect control, any
:ref:`sendToBack <no-28951>`            Places this object behind all others.
:ref:`setAll <no-28952>`                Set all child object properties to the passed value.
:ref:`setCaptionForColumn <no-28953>`   Convenience method for setting the caption for a given column number.
:ref:`setColumnWidth <no-28954>`        Sets the width of the specified column.
:ref:`setColumns <no-28955>`            Accepts a list/tuple of column headings, removes any existing columns,
:ref:`setFocus <no-28956>`              Sets focus to the object.
:ref:`setItemBackColor <no-28957>`      
:ref:`setItemData <no-28958>`           Associate some data with the item.
:ref:`setItemForeColor <no-28959>`      
:ref:`setItemImg <no-28960>`            Sets the specified item's image to the image corresponding
:ref:`setPositionInSizer <no-28961>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-28962>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-28963>` Sets a group of properties on the object all at once. This
:ref:`setResizeColumn <no-28964>`       Specify which column that should be autosized.  Pass either
:ref:`setSelection <no-28965>`          Same as setting property PositionValue.
:ref:`setSizerProp <no-28966>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-28967>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-28968>`                  Make the object visible.
:ref:`showContainingPage <no-28969>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-28970>`       Display a context menu (popup) at the specified position.
:ref:`sort <no-28971>`                  
:ref:`super <no-28972>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-28973>`           Remove a previously registered event binding.
:ref:`unbindKey <no-28974>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-28975>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-28976>`      Immediately unlocks the display, no matter how many previous
:ref:`unselect <no-28977>`              De-selects the specified row. In a MultipleSelect control, any
:ref:`unselectAll <no-28978>`           De-selects all rows.
:ref:`update <no-28979>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-28853:

.. function:: dabo.ui.uiwx.dListControl.dListControl.addColumn(self, caption, align='Left', width=-1)

   Add a column with the selected caption.



-------

.. _no-28854:

.. function:: dabo.ui.uiwx.dListControl.dListControl.addImage(self, img, key=None)

   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   



-------

.. _no-28859:

.. function:: dabo.ui.uiwx.dListControl.dListControl.append(self, tx, col=0, row=None)

   
   Appends a row with the associated text in the specified column.
   If the value for tx is a list/tuple, the values will be set in the columns
   starting with the passed value. If either case results in an attempt to
   add to a non-existent column, it will be ignored.
   



-------

.. _no-28861:

.. function:: dabo.ui.uiwx.dListControl.dListControl.appendRows(self, seq, col=0)

   
   Accepts a list/tuple of data. Each element in the sequence
   will be another row in the control. If the data is plain text, it
   will be added in the specified column. If the data is also a
   list/tuple, it will be appended into columns beginning with the
   specified column.
   



-------

.. _no-28863:

.. function:: dabo.ui.uiwx.dListControl.dListControl.autoSizeColumn(self, col)

   Auto-sizes the specified column.



-------

.. _no-28864:

.. function:: dabo.ui.uiwx.dListControl.dListControl.autoSizeColumns(self, colList=None)

   Auto-sizes all the columns.



-------

.. _no-28871:

.. function:: dabo.ui.uiwx.dListControl.dListControl.clear(self)

   Remove all the rows in the control.



-------

.. _no-28898:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getCaptionForColumn(self, colnum)

   Convenience method for getting the caption for a given column number.



-------

.. _no-28900:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getColumnWidth(self, col)



-------

.. _no-28903:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getItemBackColor(self, itm)



-------

.. _no-28904:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getItemData(self, item)

   Retrieve the data associated with the item.



-------

.. _no-28905:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getItemForeColor(self, itm)



-------

.. _no-28906:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getItemImg(self, itm)

   
   Returns the index of the specified item's image in the
   current image list, or -1 if no image is set for the item.
   



-------

.. _no-28916:

.. function:: dabo.ui.uiwx.dListControl.dListControl.insert(self, tx, row=0, col=0)

   
   Inserts the item at the specified row, or at the beginning if no
   row is specified. Item is inserted at the specified column, as in self.append()
   



-------

.. _no-28917:

.. function:: dabo.ui.uiwx.dListControl.dListControl.insertColumn(self, pos, caption, align='Left', width=-1)

   
   Inserts a column at the specified position
   with the selected caption.
   



-------

.. _no-28919:

.. function:: dabo.ui.uiwx.dListControl.dListControl.insertRows(self, seq, row=0, col=0)

   
   Accepts a list/tuple of data. Each element in the sequence
   will be another row in the control. If the data is plain text, it
   will be inserted in the specified column at the specified row.
   If the data is also a list/tuple, it will be inserted into columns
   beginning with the specified column.
   



-------

.. _no-28938:

.. function:: dabo.ui.uiwx.dListControl.dListControl.removeAll(self)

   Remove all the rows in the control.



-------

.. _no-28939:

.. function:: dabo.ui.uiwx.dListControl.dListControl.removeColumn(self, pos=None)

   
   Removes the specified column, or the last column if
   no column number is passed.
   



-------

.. _no-28942:

.. function:: dabo.ui.uiwx.dListControl.dListControl.removeRow(self, row)

   
   Deletes the specified row if it exists, or generates a warning
   if it does not.
   



-------

.. _no-28947:

.. function:: dabo.ui.uiwx.dListControl.dListControl.select(self, row)

   
   Selects the specified row. In a MultipleSelect control, any
   other selected rows remain selected.
   



-------

.. _no-28948:

.. function:: dabo.ui.uiwx.dListControl.dListControl.selectAll(self)

   
   Selects all rows in a MultipleSelect control, or generates a
   warning if the control is not set to MultipleSelect.
   



-------

.. _no-28949:

.. function:: dabo.ui.uiwx.dListControl.dListControl.selectNone(self)

   De-selects all rows.



-------

.. _no-28950:

.. function:: dabo.ui.uiwx.dListControl.dListControl.selectOnly(self, row)

   
   Selects the specified row. In a MultipleSelect control, any
   other selected rows are de-selected first.
   



-------

.. _no-28953:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setCaptionForColumn(self, colnum, val)

   Convenience method for setting the caption for a given column number.



-------

.. _no-28954:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setColumnWidth(self, col, wd)

   Sets the width of the specified column.



-------

.. _no-28955:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setColumns(self, colList)

   
   Accepts a list/tuple of column headings, removes any existing columns,
   and creates new columns, one for each element in the list. The current
   display settings and data is preserved as much as possible: setting more
   columns will result in empty columns, and setting fewer columns will
   truncate the data.
   



-------

.. _no-28957:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setItemBackColor(self, itm, val)



-------

.. _no-28958:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setItemData(self, item, data)

   Associate some data with the item.



-------

.. _no-28959:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setItemForeColor(self, itm, val)



-------

.. _no-28960:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setItemImg(self, itm, imgKey)

   
   Sets the specified item's image to the image corresponding
   to the specified key. May also optionally pass the index of the
   image in the ImageList rather than the key.
   



-------

.. _no-28971:

.. function:: dabo.ui.uiwx.dListControl.dListControl.sort(self, sortFunction=None)



-------

.. _no-28977:

.. function:: dabo.ui.uiwx.dListControl.dListControl.unselect(self, row)

   
   De-selects the specified row. In a MultipleSelect control, any
   other selected rows remain selected.
   



-------

.. _no-28978:

.. function:: dabo.ui.uiwx.dListControl.dListControl.unselectAll(self)

   De-selects all rows.



-------


Methods - inherited
=====================

.. _no-28852:

.. function:: dabo.ui.uiwx.dListControl.dListControl.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28855:

.. function:: dabo.ui.uiwx.dListControl.dListControl.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-28856:

.. function:: dabo.ui.uiwx.dListControl.dListControl.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28857:

.. function:: dabo.ui.uiwx.dListControl.dListControl.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28858:

.. function:: dabo.ui.uiwx.dListControl.dListControl.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28860:

.. function:: dabo.ui.uiwx.dListControl.dListControl.appendItem(self, txt, select=False)
   :noindex:


   Adds a new item to the end of the list


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28862:

.. function:: dabo.ui.uiwx.dListControl.dListControl.autoBindEvents(self, force=True)
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

.. _no-28865:

.. function:: dabo.ui.uiwx.dListControl.dListControl.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28866:

.. function:: dabo.ui.uiwx.dListControl.dListControl.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28867:

.. function:: dabo.ui.uiwx.dListControl.dListControl.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28868:

.. function:: dabo.ui.uiwx.dListControl.dListControl.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28869:

.. function:: dabo.ui.uiwx.dListControl.dListControl.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-28870:

.. function:: dabo.ui.uiwx.dListControl.dListControl.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28872:

.. function:: dabo.ui.uiwx.dListControl.dListControl.clearSelections(self)
   :noindex:


   
   Stub method. Only used in the list box, where there
   can be multiple selections.
   


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28873:

.. function:: dabo.ui.uiwx.dListControl.dListControl.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28874:

.. function:: dabo.ui.uiwx.dListControl.dListControl.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28875:

.. function:: dabo.ui.uiwx.dListControl.dListControl.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28876:

.. function:: dabo.ui.uiwx.dListControl.dListControl.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28877:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28878:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28879:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-28880:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28881:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28882:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28883:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28884:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28885:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28886:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28887:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28888:

.. function:: dabo.ui.uiwx.dListControl.dListControl.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28889:

.. function:: dabo.ui.uiwx.dListControl.dListControl.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28890:

.. function:: dabo.ui.uiwx.dListControl.dListControl.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28891:

.. function:: dabo.ui.uiwx.dListControl.dListControl.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28892:

.. function:: dabo.ui.uiwx.dListControl.dListControl.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28893:

.. function:: dabo.ui.uiwx.dListControl.dListControl.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28894:

.. function:: dabo.ui.uiwx.dListControl.dListControl.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28895:

.. function:: dabo.ui.uiwx.dListControl.dListControl.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28896:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28897:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28899:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28901:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28902:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28907:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28908:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28909:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-28910:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28911:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28912:

.. function:: dabo.ui.uiwx.dListControl.dListControl.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28913:

.. function:: dabo.ui.uiwx.dListControl.dListControl.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28914:

.. function:: dabo.ui.uiwx.dListControl.dListControl.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28915:

.. function:: dabo.ui.uiwx.dListControl.dListControl.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28918:

.. function:: dabo.ui.uiwx.dListControl.dListControl.insertItem(self, pos, txt, select=False)
   :noindex:


   Inserts a new item into the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28920:

.. function:: dabo.ui.uiwx.dListControl.dListControl.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28921:

.. function:: dabo.ui.uiwx.dListControl.dListControl.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28922:

.. function:: dabo.ui.uiwx.dListControl.dListControl.lockDisplay(self)
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

.. _no-28923:

.. function:: dabo.ui.uiwx.dListControl.dListControl.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28924:

.. function:: dabo.ui.uiwx.dListControl.dListControl.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28925:

.. function:: dabo.ui.uiwx.dListControl.dListControl.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28926:

.. function:: dabo.ui.uiwx.dListControl.dListControl.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28927:

.. function:: dabo.ui.uiwx.dListControl.dListControl.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28928:

.. function:: dabo.ui.uiwx.dListControl.dListControl.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28929:

.. function:: dabo.ui.uiwx.dListControl.dListControl.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28930:

.. function:: dabo.ui.uiwx.dListControl.dListControl.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28931:

.. function:: dabo.ui.uiwx.dListControl.dListControl.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28932:

.. function:: dabo.ui.uiwx.dListControl.dListControl.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28933:

.. function:: dabo.ui.uiwx.dListControl.dListControl.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28934:

.. function:: dabo.ui.uiwx.dListControl.dListControl.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28935:

.. function:: dabo.ui.uiwx.dListControl.dListControl.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28936:

.. function:: dabo.ui.uiwx.dListControl.dListControl.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28937:

.. function:: dabo.ui.uiwx.dListControl.dListControl.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28940:

.. function:: dabo.ui.uiwx.dListControl.dListControl.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28941:

.. function:: dabo.ui.uiwx.dListControl.dListControl.removeItem(self, pos)
   :noindex:


   Removes the item at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28943:

.. function:: dabo.ui.uiwx.dListControl.dListControl.resizeColumn(self, minWidth)
   :noindex:



Inherited from: 'wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin - can not provide a link

-------

.. _no-28944:

.. function:: dabo.ui.uiwx.dListControl.dListControl.resizeLastColumn(self, minWidth)
   :noindex:


    Resize the last column appropriately.
   
               If the list's columns are too wide to fit within the window, we use
               a horizontal scrollbar.  Otherwise, we expand the right-most column
               to take up the remaining free space in the list.
   
               This method is called automatically when the wx.ListCtrl is resized;
               you can also call it yourself whenever you want the last column to
               be resized appropriately (eg, when adding, removing or resizing
               columns).
   
               'minWidth' is the preferred minimum width for the last column.
           


Inherited from: 'wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin - can not provide a link

-------

.. _no-28945:

.. function:: dabo.ui.uiwx.dListControl.dListControl.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28946:

.. function:: dabo.ui.uiwx.dListControl.dListControl.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28951:

.. function:: dabo.ui.uiwx.dListControl.dListControl.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28952:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-28956:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28961:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28962:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-28963:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-28964:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setResizeColumn(self, col)
   :noindex:


   
           Specify which column that should be autosized.  Pass either
           'LAST' or the column number.  Default is 'LAST'.
           


Inherited from: 'wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin - can not provide a link

-------

.. _no-28965:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setSelection(self, index)
   :noindex:


   Same as setting property PositionValue.


Inherited from: :ref:`dabo.ui.uiwx.dControlItemMixin.dControlItemMixin`

-------

.. _no-28966:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28967:

.. function:: dabo.ui.uiwx.dListControl.dListControl.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28968:

.. function:: dabo.ui.uiwx.dListControl.dListControl.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28969:

.. function:: dabo.ui.uiwx.dListControl.dListControl.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28970:

.. function:: dabo.ui.uiwx.dListControl.dListControl.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28972:

.. function:: dabo.ui.uiwx.dListControl.dListControl.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28973:

.. function:: dabo.ui.uiwx.dListControl.dListControl.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28974:

.. function:: dabo.ui.uiwx.dListControl.dListControl.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28975:

.. function:: dabo.ui.uiwx.dListControl.dListControl.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28976:

.. function:: dabo.ui.uiwx.dListControl.dListControl.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28979:

.. function:: dabo.ui.uiwx.dListControl.dListControl.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
