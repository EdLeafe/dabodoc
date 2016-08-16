
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dGrid

.. _dabo.ui.uiwx.dGrid.dColumn:

======================================
|doc_title|  **dGrid.dColumn** - class
======================================


These aren't the actual columns that appear in the grid; rather,
they provide a way to interact with the underlying grid table in a more
straightforward manner.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dColumn**

.. inheritance-diagram:: dColumn


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dGrid.dColumn

   .. automethod:: dabo.ui.uiwx.dGrid.dColumn.__init__

|method_summary| Properties Summary
===================================


================================================== ========================
:ref:`Application <no-12495>`                      Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-12496>`                        Color for the background of each cell in the column.
:ref:`BaseClass <no-12497>`                        The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-12498>`                      Base key used when saving/restoring preferences  (str)
:ref:`Bottom <no-12499>`                           The position of the bottom side of the object. This is a
:ref:`Caption <no-12500>`                          Specifies the caption displayed in this column's header.
:ref:`CellBackColor <no-12501>`                    Color for the background of the current cell in the column.
:ref:`CellFontBold <no-12502>`                     Specifies whether the current cell's font is bold-faced.
:ref:`CellForeColor <no-12503>`                    Color for the foreground (text) of the current cell in the column.
:ref:`Children <no-12504>`                         List of child objects.
:ref:`Class <no-12505>`                            The class the object is based on. Read-only.  (class)
:ref:`ColumnIndex <no-12506>`                      Return our column index in the grid, or -1.
:ref:`CustomEditorClass <no-12507>`                Custom Editor class for this column. Default: None.
:ref:`CustomEditors <no-12508>`                    Dictionary of custom editors for this column. Default: {}.
:ref:`CustomListEditorChoices <no-12509>`          Dictionary of custom list choices for this column. Default: {}.
:ref:`CustomRendererClass <no-12510>`              Custom Renderer class for this column. Default: None.
:ref:`CustomRenderers <no-12511>`                  Dictionary of custom renderers for this column. Default: {}.
:ref:`DataField <no-12512>`                        Field key in the data set to which this column is bound. (str)
:ref:`DataType <no-12513>`                         Description of the data type for this column (str)
:ref:`DynamicBackColor <no-12514>`                 Dynamically determine the value of the BackColor property.
:ref:`DynamicCaption <no-12515>`                   Dynamically determine the value of the Caption property.
:ref:`DynamicCellBackColor <no-12516>`             Dynamically determine the value of the CellBackColor property.
:ref:`DynamicCellFontBold <no-12517>`              Dynamically determine the value of the CellFontBold property.
:ref:`DynamicCellForeColor <no-12518>`             Dynamically determine the value of the CellForeColor property.
:ref:`DynamicCustomEditorClass <no-12519>`         Dynamically determine the value of the CustomEditorClass property.
:ref:`DynamicCustomEditors <no-12520>`             Dynamically determine the value of the CustomEditors property.
:ref:`DynamicCustomListEditorChoices <no-12521>`   Dynamically determine the value of the CustomListEditorChoices property.
:ref:`DynamicCustomRendererClass <no-12522>`       Dynamically determine the value of the CustomRendererClass property.
:ref:`DynamicCustomRenderers <no-12523>`           Dynamically determine the value of the CustomRenderers property.
:ref:`DynamicDataField <no-12524>`                 Dynamically determine the value of the DataField property.
:ref:`DynamicDataType <no-12525>`                  Dynamically determine the value of the DataType property.
:ref:`DynamicEditable <no-12526>`                  Dynamically determine the value of the Editable property.
:ref:`DynamicFont <no-12527>`                      Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-12528>`                  Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-12529>`                  Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-12530>`                Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-12531>`                  Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-12532>`             Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-12533>`                 Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeaderBackColor <no-12534>`           Dynamically determine the value of the HeaderBackColor property.
:ref:`DynamicHeaderFont <no-12535>`                Dynamically determine the value of the HeaderFont property.
:ref:`DynamicHeaderFontBold <no-12536>`            Dynamically determine the value of the HeaderFontBold property.
:ref:`DynamicHeaderFontFace <no-12537>`            Dynamically determine the value of the HeaderFontFace property.
:ref:`DynamicHeaderFontItalic <no-12538>`          Dynamically determine the value of the HeaderFontItalic property.
:ref:`DynamicHeaderFontSize <no-12539>`            Dynamically determine the value of the HeaderFontSize property.
:ref:`DynamicHeaderFontUnderline <no-12540>`       Dynamically determine the value of the HeaderFontUnderline property.
:ref:`DynamicHeaderForeColor <no-12541>`           Dynamically determine the value of the HeaderForeColor property.
:ref:`DynamicHeaderHorizontalAlignment <no-12542>` Dynamically determine the value of the HeaderHorizontalAlignment property.
:ref:`DynamicHeaderVerticalAlignment <no-12543>`   Dynamically determine the value of the HeaderVerticalAlignment property.
:ref:`DynamicHorizontalAlignment <no-12544>`       Dynamically determine the value of the HorizontalAlignment property.
:ref:`DynamicListEditorChoices <no-12545>`         Dynamically determine the value of the ListEditorChoices property.
:ref:`DynamicOrder <no-12546>`                     Dynamically determine the value of the Order property.
:ref:`DynamicSearchable <no-12547>`                Dynamically determine the value of the Searchable property.
:ref:`DynamicSortable <no-12548>`                  Dynamically determine the value of the Sortable property.
:ref:`DynamicVerticalAlignment <no-12549>`         Dynamically determine the value of the VerticalAlignment property.
:ref:`DynamicVisible <no-12550>`                   Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-12551>`                     Dynamically determine the value of the Width property.
:ref:`Editable <no-12552>`                         If True, and if the grid is set as Editable, the cell values in this
:ref:`EditorClass <no-12553>`                      Returns the editor class used for cells in the column. This
:ref:`Expand <no-12554>`                           Does this column expand/shrink as the grid width changes?
:ref:`Font <no-12555>`                             The font properties of the column's cells. (dFont)
:ref:`FontBold <no-12556>`                         Specifies if the cell font (for all cells in the column) is bold-faced. (bool)
:ref:`FontDescription <no-12557>`                  Human-readable description of the column's cell font settings. (str)
:ref:`FontFace <no-12558>`                         Specifies the font face for the column cells. (str)
:ref:`FontInfo <no-12559>`                         Specifies the platform-native font info string for the column cells. Read-only. (str)
:ref:`FontItalic <no-12560>`                       Specifies whether the column's cell font is italicized. (bool)
:ref:`FontSize <no-12561>`                         Specifies the point size of the column's cell font. (int)
:ref:`FontUnderline <no-12562>`                    Specifies whether cell text is underlined. (bool)
:ref:`ForeColor <no-12563>`                        Color for the foreground (text) of each cell in the column.
:ref:`Form <no-12564>`                             Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`HeaderBackColor <no-12565>`                  Optional color for the background of the column header  (str)
:ref:`HeaderFont <no-12566>`                       The font properties of the column's header. (dFont)
:ref:`HeaderFontBold <no-12567>`                   Specifies if the header font is bold-faced. (bool)
:ref:`HeaderFontDescription <no-12568>`            Human-readable description of the current header font settings. (str)
:ref:`HeaderFontFace <no-12569>`                   Specifies the font face for the column header. (str)
:ref:`HeaderFontInfo <no-12570>`                   Specifies the platform-native font info string for the column header. Read-only. (str)
:ref:`HeaderFontItalic <no-12571>`                 Specifies whether the header font is italicized. (bool)
:ref:`HeaderFontSize <no-12572>`                   Specifies the point size of the header font. (int)
:ref:`HeaderFontUnderline <no-12573>`              Specifies whether column header text is underlined. (bool)
:ref:`HeaderForeColor <no-12574>`                  Optional color for the foreground (text) of the column header  (str)
:ref:`HeaderHorizontalAlignment <no-12575>`        Specifies the horizontal alignment of the header caption. ('Left', 'Center', 'Right')
:ref:`HeaderVerticalAlignment <no-12576>`          Specifies the vertical alignment of the header caption. ('Top', 'Center', 'Bottom')
:ref:`HorizontalAlignment <no-12577>`              Horizontal alignment for all cells in this column. (str)
:ref:`ListEditorChoices <no-12578>`                Specifies the list of choices that will appear in the list. Only applies
:ref:`LogEvents <no-12579>`                        Specifies which events to log.  (list of strings)
:ref:`Movable <no-12580>`                          Specifies whether this column is movable by the user.
:ref:`Name <no-12581>`                             The name of the object.  (str)
:ref:`Order <no-12582>`                            Order of this column. Columns in the grid are arranged according
:ref:`Parent <no-12583>`                           The containing object.  (obj)
:ref:`Precision <no-12584>`                        Number of decimal places to display for float and decimal values (int)
:ref:`PreferenceManager <no-12585>`                Reference to the Preference Management object  (dPref)
:ref:`RendererClass <no-12586>`                    Returns the renderer class used for cells in the column. This will be
:ref:`Resizable <no-12587>`                        Specifies whether this column is resizable by the user.
:ref:`Right <no-12588>`                            The position of the right side of the object. This is a
:ref:`Searchable <no-12589>`                       Specifies whether this column's incremental search is enabled.
:ref:`Sortable <no-12590>`                         Specifies whether this column can be sorted. Default: True. The grid's
:ref:`Value <no-12591>`                            Returns the current value of the column from the underlying dataset or bizobj.
:ref:`VerticalAlignment <no-12592>`                Vertical alignment for all cells in this column. Acceptable values
:ref:`Visible <no-12593>`                          Controls whether the column is shown or not(bool)
:ref:`Width <no-12594>`                            Width of this column (int)
:ref:`WordWrap <no-12595>`                         When True, text longer than the column width will wrap to the next line(bool)

================================================== ========================


Properties
==========

.. _no-12496:

**BackColor** 

Color for the background of each cell in the column.



-------

.. _no-12500:

**Caption** 

Specifies the caption displayed in this column's header.



-------

.. _no-12501:

**CellBackColor** 

Color for the background of the current cell in the column.



-------

.. _no-12502:

**CellFontBold** 

Specifies whether the current cell's font is bold-faced.



-------

.. _no-12503:

**CellForeColor** 

Color for the foreground (text) of the current cell in the column.



-------

.. _no-12506:

**ColumnIndex** 

Return our column index in the grid, or -1.



-------

.. _no-12507:

**CustomEditorClass** 

Custom Editor class for this column. Default: None.

    Set this to override the default editor class, which Dabo will
    select based on the data type of the field.



-------

.. _no-12508:

**CustomEditors** 

Dictionary of custom editors for this column. Default: {}.

    Set this to override the default editor class on a row-by-row basis.
    If there is no custom editor class for a given row in CustomEditors,
    the CustomEditor property setting will apply.



-------

.. _no-12509:

**CustomListEditorChoices** 

Dictionary of custom list choices for this column. Default: {}.

    Set this to override the default list choices on a row-by-row basis.
    If there is no custom entry for a given row in CustomListEditorChoices,
    the ListEditorChoices property setting will apply.



-------

.. _no-12510:

**CustomRendererClass** 

Custom Renderer class for this column. Default: None.

    Set this to override the default renderer class, which Dabo will select based
    on the data type of the field.



-------

.. _no-12511:

**CustomRenderers** 

Dictionary of custom renderers for this column. Default: {}.

    Set this to override the default renderer class on a row-by-row basis.
    If there is no custom renderer for a given row in CustomRenderers, the
    CustomRendererClass property setting will apply.



-------

.. _no-12512:

**DataField** 

Field key in the data set to which this column is bound. (str)



-------

.. _no-12513:

**DataType** 

Description of the data type for this column (str)



-------

.. _no-12514:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.



-------

.. _no-12515:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.



-------

.. _no-12516:

**DynamicCellBackColor** 

Dynamically determine the value of the CellBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CellBackColor property. If DynamicCellBackColor is set to None (the default), CellBackColor
will not be dynamically evaluated.



-------

.. _no-12517:

**DynamicCellFontBold** 

Dynamically determine the value of the CellFontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CellFontBold property. If DynamicCellFontBold is set to None (the default), CellFontBold
will not be dynamically evaluated.



-------

.. _no-12518:

**DynamicCellForeColor** 

Dynamically determine the value of the CellForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CellForeColor property. If DynamicCellForeColor is set to None (the default), CellForeColor
will not be dynamically evaluated.



-------

.. _no-12519:

**DynamicCustomEditorClass** 

Dynamically determine the value of the CustomEditorClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CustomEditorClass property. If DynamicCustomEditorClass is set to None (the default), CustomEditorClass
will not be dynamically evaluated.



-------

.. _no-12520:

**DynamicCustomEditors** 

Dynamically determine the value of the CustomEditors property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CustomEditors property. If DynamicCustomEditors is set to None (the default), CustomEditors
will not be dynamically evaluated.



-------

.. _no-12521:

**DynamicCustomListEditorChoices** 

Dynamically determine the value of the CustomListEditorChoices property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CustomListEditorChoices property. If DynamicCustomListEditorChoices is set to None (the default), CustomListEditorChoices
will not be dynamically evaluated.



-------

.. _no-12522:

**DynamicCustomRendererClass** 

Dynamically determine the value of the CustomRendererClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CustomRendererClass property. If DynamicCustomRendererClass is set to None (the default), CustomRendererClass
will not be dynamically evaluated.



-------

.. _no-12523:

**DynamicCustomRenderers** 

Dynamically determine the value of the CustomRenderers property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CustomRenderers property. If DynamicCustomRenderers is set to None (the default), CustomRenderers
will not be dynamically evaluated.



-------

.. _no-12524:

**DynamicDataField** 

Dynamically determine the value of the DataField property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DataField property. If DynamicDataField is set to None (the default), DataField
will not be dynamically evaluated.



-------

.. _no-12525:

**DynamicDataType** 

Dynamically determine the value of the DataType property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DataType property. If DynamicDataType is set to None (the default), DataType
will not be dynamically evaluated.



-------

.. _no-12526:

**DynamicEditable** 

Dynamically determine the value of the Editable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Editable property. If DynamicEditable is set to None (the default), Editable
will not be dynamically evaluated.



-------

.. _no-12527:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.



-------

.. _no-12528:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.



-------

.. _no-12529:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.



-------

.. _no-12530:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.



-------

.. _no-12531:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.



-------

.. _no-12532:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.



-------

.. _no-12533:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.



-------

.. _no-12534:

**DynamicHeaderBackColor** 

Dynamically determine the value of the HeaderBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderBackColor property. If DynamicHeaderBackColor is set to None (the default), HeaderBackColor
will not be dynamically evaluated.



-------

.. _no-12535:

**DynamicHeaderFont** 

Dynamically determine the value of the HeaderFont property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderFont property. If DynamicHeaderFont is set to None (the default), HeaderFont
will not be dynamically evaluated.



-------

.. _no-12536:

**DynamicHeaderFontBold** 

Dynamically determine the value of the HeaderFontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderFontBold property. If DynamicHeaderFontBold is set to None (the default), HeaderFontBold
will not be dynamically evaluated.



-------

.. _no-12537:

**DynamicHeaderFontFace** 

Dynamically determine the value of the HeaderFontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderFontFace property. If DynamicHeaderFontFace is set to None (the default), HeaderFontFace
will not be dynamically evaluated.



-------

.. _no-12538:

**DynamicHeaderFontItalic** 

Dynamically determine the value of the HeaderFontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderFontItalic property. If DynamicHeaderFontItalic is set to None (the default), HeaderFontItalic
will not be dynamically evaluated.



-------

.. _no-12539:

**DynamicHeaderFontSize** 

Dynamically determine the value of the HeaderFontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderFontSize property. If DynamicHeaderFontSize is set to None (the default), HeaderFontSize
will not be dynamically evaluated.



-------

.. _no-12540:

**DynamicHeaderFontUnderline** 

Dynamically determine the value of the HeaderFontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderFontUnderline property. If DynamicHeaderFontUnderline is set to None (the default), HeaderFontUnderline
will not be dynamically evaluated.



-------

.. _no-12541:

**DynamicHeaderForeColor** 

Dynamically determine the value of the HeaderForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderForeColor property. If DynamicHeaderForeColor is set to None (the default), HeaderForeColor
will not be dynamically evaluated.



-------

.. _no-12542:

**DynamicHeaderHorizontalAlignment** 

Dynamically determine the value of the HeaderHorizontalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderHorizontalAlignment property. If DynamicHeaderHorizontalAlignment is set to None (the default), HeaderHorizontalAlignment
will not be dynamically evaluated.



-------

.. _no-12543:

**DynamicHeaderVerticalAlignment** 

Dynamically determine the value of the HeaderVerticalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderVerticalAlignment property. If DynamicHeaderVerticalAlignment is set to None (the default), HeaderVerticalAlignment
will not be dynamically evaluated.



-------

.. _no-12544:

**DynamicHorizontalAlignment** 

Dynamically determine the value of the HorizontalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalAlignment property. If DynamicHorizontalAlignment is set to None (the default), HorizontalAlignment
will not be dynamically evaluated.



-------

.. _no-12545:

**DynamicListEditorChoices** 

Dynamically determine the value of the ListEditorChoices property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ListEditorChoices property. If DynamicListEditorChoices is set to None (the default), ListEditorChoices
will not be dynamically evaluated.



-------

.. _no-12546:

**DynamicOrder** 

Dynamically determine the value of the Order property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Order property. If DynamicOrder is set to None (the default), Order
will not be dynamically evaluated.



-------

.. _no-12547:

**DynamicSearchable** 

Dynamically determine the value of the Searchable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Searchable property. If DynamicSearchable is set to None (the default), Searchable
will not be dynamically evaluated.



-------

.. _no-12548:

**DynamicSortable** 

Dynamically determine the value of the Sortable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Sortable property. If DynamicSortable is set to None (the default), Sortable
will not be dynamically evaluated.



-------

.. _no-12549:

**DynamicVerticalAlignment** 

Dynamically determine the value of the VerticalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalAlignment property. If DynamicVerticalAlignment is set to None (the default), VerticalAlignment
will not be dynamically evaluated.



-------

.. _no-12550:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.



-------

.. _no-12551:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.



-------

.. _no-12552:

**Editable** 

If True, and if the grid is set as Editable, the cell values in this
        column are editable by the user. If False, the cells in this column
        cannot be edited no matter what the grid setting is. When editable,
        incremental searching will not be enabled, regardless of the
        Searchable property setting.  (bool)



-------

.. _no-12553:

**EditorClass** 

Returns the editor class used for cells in the column. This
        will be self.CustomEditorClass if set, or the default editor for the
        datatype of the field.    (varies)



-------

.. _no-12554:

**Expand** 

Does this column expand/shrink as the grid width changes?
    Default=False  (bool)



-------

.. _no-12555:

**Font** 

The font properties of the column's cells. (dFont)



-------

.. _no-12556:

**FontBold** 

Specifies if the cell font (for all cells in the column) is bold-faced. (bool)



-------

.. _no-12557:

**FontDescription** 

Human-readable description of the column's cell font settings. (str)



-------

.. _no-12558:

**FontFace** 

Specifies the font face for the column cells. (str)



-------

.. _no-12559:

**FontInfo** 

Specifies the platform-native font info string for the column cells. Read-only. (str)



-------

.. _no-12560:

**FontItalic** 

Specifies whether the column's cell font is italicized. (bool)



-------

.. _no-12561:

**FontSize** 

Specifies the point size of the column's cell font. (int)



-------

.. _no-12562:

**FontUnderline** 

Specifies whether cell text is underlined. (bool)



-------

.. _no-12563:

**ForeColor** 

Color for the foreground (text) of each cell in the column.



-------

.. _no-12565:

**HeaderBackColor** 

Optional color for the background of the column header  (str)



-------

.. _no-12566:

**HeaderFont** 

The font properties of the column's header. (dFont)



-------

.. _no-12567:

**HeaderFontBold** 

Specifies if the header font is bold-faced. (bool)



-------

.. _no-12568:

**HeaderFontDescription** 

Human-readable description of the current header font settings. (str)



-------

.. _no-12569:

**HeaderFontFace** 

Specifies the font face for the column header. (str)



-------

.. _no-12570:

**HeaderFontInfo** 

Specifies the platform-native font info string for the column header. Read-only. (str)



-------

.. _no-12571:

**HeaderFontItalic** 

Specifies whether the header font is italicized. (bool)



-------

.. _no-12572:

**HeaderFontSize** 

Specifies the point size of the header font. (int)



-------

.. _no-12573:

**HeaderFontUnderline** 

Specifies whether column header text is underlined. (bool)



-------

.. _no-12574:

**HeaderForeColor** 

Optional color for the foreground (text) of the column header  (str)



-------

.. _no-12575:

**HeaderHorizontalAlignment** 

Specifies the horizontal alignment of the header caption. ('Left', 'Center', 'Right')



-------

.. _no-12576:

**HeaderVerticalAlignment** 

Specifies the vertical alignment of the header caption. ('Top', 'Center', 'Bottom')



-------

.. _no-12577:

**HorizontalAlignment** 

Horizontal alignment for all cells in this column. (str)
        Acceptable values are:
            'Automatic': The cell's contents will align right for numeric data, left for text. (default)
            'Left'
            'Center'
            'Right' 



-------

.. _no-12578:

**ListEditorChoices** 

Specifies the list of choices that will appear in the list. Only applies
if the DataType is set as "list".  (list)



-------

.. _no-12580:

**Movable** 

Specifies whether this column is movable by the user.

    Note also the dGrid.MovableColumns property - if that is set
    to False, columns will not be movable even if their Movable
    property is set to True.



-------

.. _no-12582:

**Order** 

Order of this column. Columns in the grid are arranged according
    to their relative Order. (int)



-------

.. _no-12584:

**Precision** 

Number of decimal places to display for float and decimal values (int)



-------

.. _no-12586:

**RendererClass** 

Returns the renderer class used for cells in the column. This will be
    self.CustomRendererClass if set, or the default renderer class for the
    datatype of the field.    (varies)



-------

.. _no-12587:

**Resizable** 

Specifies whether this column is resizable by the user.

    Note also the dGrid.ResizableColumns property - if that is set
    to False, columns will not be resizable even if their Resizable
    property is set to True.



-------

.. _no-12589:

**Searchable** 

Specifies whether this column's incremental search is enabled.
    Default: True. The grid's Searchable property will override this setting.
    (bool)



-------

.. _no-12590:

**Sortable** 

Specifies whether this column can be sorted. Default: True. The grid's
    Sortable property will override this setting.  (bool)



-------

.. _no-12591:

**Value** 

Returns the current value of the column from the underlying dataset or bizobj.



-------

.. _no-12592:

**VerticalAlignment** 

Vertical alignment for all cells in this column. Acceptable values
    are 'Top', 'Center', and 'Bottom'.    (str)



-------

.. _no-12593:

**Visible** 

Controls whether the column is shown or not(bool)



-------

.. _no-12594:

**Width** 

Width of this column (int)



-------

.. _no-12595:

**WordWrap** 

When True, text longer than the column width will wrap to the next line(bool)



-------


Properties - inherited
========================

.. _no-12495:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12497:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12498:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12499:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12504:

**Children** 

List of child objects.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12505:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12564:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12579:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12581:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12583:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12585:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12588:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------


|method_summary| Events Summary
===============================


========== ========================

========== ========================


|method_summary| Methods Summary
================================


============================================ ========================
:ref:`addObject <no-12596>`                  Create an instance of classRef, and make it a child of self.
:ref:`afterInit <no-12597>`                  Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-12598>`             Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-12599>`                 Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-12600>`                  Bind a dEvent to a callback function.
:ref:`bindEvents <no-12601>`                 Bind a sequence of [dEvent, callback] lists.
:ref:`clone <no-12602>`                      Abstract method: subclasses MUST override for UI-specifics.
:ref:`fontZoomIn <no-12603>`                 Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-12604>`             Reset the font zoom back to zero.
:ref:`fontZoomOut <no-12605>`                Zoom out on the font, by setting a lower point size.
:ref:`getAbsoluteName <no-12606>`            Return the fully qualified name of the object.
:ref:`getDataTypeForColumn <no-12607>`       
:ref:`getEditorClassForRow <no-12608>`       Return the cell editor class for the passed row.
:ref:`getListEditorChoicesForRow <no-12609>` Return the list of choices for the list editor for the given row.
:ref:`getProperties <no-12610>`              Returns a dictionary of property name/value pairs.
:ref:`getRendererClassForRow <no-12611>`     Return the cell renderer class for the passed row.
:ref:`initEvents <no-12612>`                 Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-12613>`             Hook for subclasses. User subclasses should set properties
:ref:`iterateCall <no-12614>`                Call the given function on this object and all of its Children. If
:ref:`raiseEvent <no-12615>`                 Send the event to all registered listeners.
:ref:`reCreate <no-12616>`                   Abstract method: subclasses MUST override for UI-specifics.
:ref:`refresh <no-12617>`                    Abstract method.
:ref:`release <no-12618>`                    Usually don't need this, but it helps to keep this in
:ref:`setProperties <no-12619>`              Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-12620>`      Sets a group of properties on the object all at once. This
:ref:`super <no-12621>`                      This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-12622>`                Remove a previously registered event binding.

============================================ ========================


Methods
=======

.. _no-12607:

.. function:: dabo.ui.uiwx.dGrid.dColumn.getDataTypeForColumn(self)



-------

.. _no-12608:

.. function:: dabo.ui.uiwx.dGrid.dColumn.getEditorClassForRow(self, row)

   Return the cell editor class for the passed row.



-------

.. _no-12609:

.. function:: dabo.ui.uiwx.dGrid.dColumn.getListEditorChoicesForRow(self, row)

   Return the list of choices for the list editor for the given row.



-------

.. _no-12611:

.. function:: dabo.ui.uiwx.dGrid.dColumn.getRendererClassForRow(self, row)

   Return the cell renderer class for the passed row.



-------

.. _no-12618:

.. function:: dabo.ui.uiwx.dGrid.dColumn.release(self)

   
   Usually don't need this, but it helps to keep this in
   line with other Dabo objects.
   



-------


Methods - inherited
=====================

.. _no-12596:

.. function:: dabo.ui.uiwx.dGrid.dColumn.addObject(self, classRef, Name=None, \*args, \**kwargs)
   :noindex:


   
   Create an instance of classRef, and make it a child of self.
   
   Abstract method: subclasses MUST override for UI-specifics.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12597:

.. function:: dabo.ui.uiwx.dGrid.dColumn.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12598:

.. function:: dabo.ui.uiwx.dGrid.dColumn.autoBindEvents(self, force=True)
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

.. _no-12599:

.. function:: dabo.ui.uiwx.dGrid.dColumn.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12600:

.. function:: dabo.ui.uiwx.dGrid.dColumn.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12601:

.. function:: dabo.ui.uiwx.dGrid.dColumn.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12602:

.. function:: dabo.ui.uiwx.dGrid.dColumn.clone(self, obj, name=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12603:

.. function:: dabo.ui.uiwx.dGrid.dColumn.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12604:

.. function:: dabo.ui.uiwx.dGrid.dColumn.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12605:

.. function:: dabo.ui.uiwx.dGrid.dColumn.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12606:

.. function:: dabo.ui.uiwx.dGrid.dColumn.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12610:

.. function:: dabo.ui.uiwx.dGrid.dColumn.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-12612:

.. function:: dabo.ui.uiwx.dGrid.dColumn.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12613:

.. function:: dabo.ui.uiwx.dGrid.dColumn.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12614:

.. function:: dabo.ui.uiwx.dGrid.dColumn.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12615:

.. function:: dabo.ui.uiwx.dGrid.dColumn.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
   :noindex:


   
   Send the event to all registered listeners.
   
   If uiEvent is sent, dEvents.Event will be able to parse it for useful
   information to send along to the callback.
   
   Additional arguments, if any, are sent along to the constructor    of the
   event. While this feature exists so that UI-lib event handlers can pass
   along information (such as the keystroke information in a key event), user
   code may pass along additional arguments as well, which    will exist in the
   event.EventData dictionary property.
   
   In most cases, user code should call raiseEvent() with
   the event class (dEvents.Hit, for example) as the only parameter.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12616:

.. function:: dabo.ui.uiwx.dGrid.dColumn.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12617:

.. function:: dabo.ui.uiwx.dGrid.dColumn.refresh(self)
   :noindex:


   Abstract method.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12619:

.. function:: dabo.ui.uiwx.dGrid.dColumn.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-12620:

.. function:: dabo.ui.uiwx.dGrid.dColumn.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-12621:

.. function:: dabo.ui.uiwx.dGrid.dColumn.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12622:

.. function:: dabo.ui.uiwx.dGrid.dColumn.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------


|
