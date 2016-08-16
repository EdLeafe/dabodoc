
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dGrid

.. _dabo.ui.uiwx.dGrid.dGrid:

====================================
|doc_title|  **dGrid.dGrid** - class
====================================


Creates a grid, with rows and columns to represent records and fields.

Grids are powerful controls for allowing reading and writing of data. A
grid can have any number of dColumns, which themselves have lots of properties
to manipulate. The grid is virtual, meaning that large amounts of data can
be accessed efficiently: only the data that needs to be shown on the current
screen is copied and displayed.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dGrid**

.. inheritance-diagram:: dGrid


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.grid.Grid - can not provide a link



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Grid.Grid`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dGrid.png
          :scale: 75 %
          :target: _static/macWidgets/dGrid.png
          :alt: dGrid



     - .. image:: _static/winWidgets/dGrid.png
          :scale: 75 %
          :target: _static/winWidgets/dGrid.png
          :alt: dGrid



     - .. image:: _static/nixWidgets/dGrid.png
          :scale: 75 %
          :target: _static/nixWidgets/dGrid.png
          :alt: dGrid


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dGrid.dGrid

   .. automethod:: dabo.ui.uiwx.dGrid.dGrid.__init__

|method_summary| Properties Summary
===================================


================================================== ========================
:ref:`ActivateEditorOnSelect <no-12623>`           Specifies whether the cell editor, if any, is activated upon cell selection.
:ref:`AlternateRowColoring <no-12624>`             When True, alternate rows of the grid are colored according to
:ref:`Application <no-12625>`                      Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoAdjustHeaderHeight <no-12626>`           When True, changing the VerticalHeaders property will adjust the HeaderHeight
:ref:`BackColor <no-12627>`                        Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-12628>`                        The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-12629>`                      Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-12630>`                      Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-12631>`                  Style of line for the border drawn around the control.
:ref:`BorderStyle <no-12632>`                      Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-12633>`                      Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-12634>`                           The position of the bottom side of the object. This is a
:ref:`Caption <no-12635>`                          The caption of the object. (str)
:ref:`CellHighlightWidth <no-12636>`               Specifies the width of the cell highlight box.
:ref:`Children <no-12637>`                         List of dColumns, same as self.Columns.(list)
:ref:`Class <no-12638>`                            The class the object is based on. Read-only.  (class)
:ref:`ColumnClass <no-12639>`                      Class to instantiate when a change to ColumnCount requires
:ref:`ColumnCount <no-12640>`                      Number of columns in the grid.  (int)
:ref:`Columns <no-12641>`                          List of dColumns.  (list)
:ref:`ControllingSizer <no-12642>`                 Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-12643>`             Reference to the sizer item that control's this control's layout.
:ref:`CurrentCellValue <no-12644>`                 Value of the currently selected grid cell  (varies)
:ref:`CurrentColumn <no-12645>`                    Currently selected column index. (int)
:ref:`CurrentField <no-12646>`                     Field for the currently selected column(str)
:ref:`CurrentRow <no-12647>`                       Currently selected row  (int)
:ref:`DataSet <no-12648>`                          The set of data displayed in the grid. (set of dicts)
:ref:`DataSource <no-12649>`                       The source of the data to display in the grid. (str)
:ref:`DroppedFileHandler <no-12650>`               Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-12651>`               Reference to the object that will handle text dropped on this control.
:ref:`DynamicActivateEditorOnSelect <no-12652>`    Dynamically determine the value of the ActivateEditorOnSelect property.
:ref:`DynamicAlternateRowColoring <no-12653>`      Dynamically determine the value of the AlternateRowColoring property.
:ref:`DynamicBackColor <no-12654>`                 Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-12655>`               Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-12656>`           Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-12657>`               Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-12658>`               Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-12659>`                   Dynamically determine the value of the Caption property.
:ref:`DynamicCellHighlightWidth <no-12660>`        Dynamically determine the value of the CellHighlightWidth property.
:ref:`DynamicColumnClass <no-12661>`               Dynamically determine the value of the ColumnClass property.
:ref:`DynamicColumnCount <no-12662>`               Dynamically determine the value of the ColumnCount property.
:ref:`DynamicCurrentColumn <no-12663>`             Dynamically determine the value of the CurrentColumn property.
:ref:`DynamicCurrentField <no-12664>`              Dynamically determine the value of the CurrentField property.
:ref:`DynamicCurrentRow <no-12665>`                Dynamically determine the value of the CurrentRow property.
:ref:`DynamicDataSet <no-12666>`                   Dynamically determine the value of the DataSet property.
:ref:`DynamicDataSource <no-12667>`                Dynamically determine the value of the DataSource property.
:ref:`DynamicEditable <no-12668>`                  Dynamically determine the value of the Editable property.
:ref:`DynamicEnabled <no-12669>`                   Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-12670>`                      Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-12671>`                  Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-12672>`                  Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-12673>`                Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-12674>`                  Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-12675>`             Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-12676>`                 Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeaderBackColor <no-12677>`           Dynamically determine the value of the HeaderBackColor property.
:ref:`DynamicHeaderForeColor <no-12678>`           Dynamically determine the value of the HeaderForeColor property.
:ref:`DynamicHeaderHeight <no-12679>`              Dynamically determine the value of the HeaderHeight property.
:ref:`DynamicHeaderHorizontalAlignment <no-12680>` Dynamically determine the value of the HeaderHorizontalAlignment property.
:ref:`DynamicHeaderVerticalAlignment <no-12681>`   Dynamically determine the value of the HeaderVerticalAlignment property.
:ref:`DynamicHeight <no-12682>`                    Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScrolling <no-12683>`       Dynamically determine the value of the HorizontalScrolling property.
:ref:`DynamicLeft <no-12684>`                      Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-12685>`              Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-12686>`                  Dynamically determine the value of the Position property.
:ref:`DynamicRowColorEven <no-12687>`              Dynamically determine the value of the RowColorEven property.
:ref:`DynamicRowColorOdd <no-12688>`               Dynamically determine the value of the RowColorOdd property.
:ref:`DynamicRowHeight <no-12689>`                 Dynamically determine the value of the RowHeight property.
:ref:`DynamicRowLabelWidth <no-12690>`             Dynamically determine the value of the RowLabelWidth property.
:ref:`DynamicRowLabels <no-12691>`                 Dynamically determine the value of the RowLabels property.
:ref:`DynamicSameSizeRows <no-12692>`              Dynamically determine the value of the SameSizeRows property.
:ref:`DynamicSearchDelay <no-12693>`               Dynamically determine the value of the SearchDelay property.
:ref:`DynamicSearchable <no-12694>`                Dynamically determine the value of the Searchable property.
:ref:`DynamicSelectionBackColor <no-12695>`        Dynamically determine the value of the SelectionBackColor property.
:ref:`DynamicSelectionForeColor <no-12696>`        Dynamically determine the value of the SelectionForeColor property.
:ref:`DynamicSelectionMode <no-12697>`             Dynamically determine the value of the SelectionMode property.
:ref:`DynamicShowCellBorders <no-12698>`           Dynamically determine the value of the ShowCellBorders property.
:ref:`DynamicShowColumnLabels <no-12699>`          Dynamically determine the value of the ShowColumnLabels property.
:ref:`DynamicShowHeaders <no-12700>`               Dynamically determine the value of the ShowHeaders property.
:ref:`DynamicShowRowLabels <no-12701>`             Dynamically determine the value of the ShowRowLabels property.
:ref:`DynamicSize <no-12702>`                      Dynamically determine the value of the Size property.
:ref:`DynamicSortable <no-12703>`                  Dynamically determine the value of the Sortable property.
:ref:`DynamicStatusText <no-12704>`                Dynamically determine the value of the StatusText property.
:ref:`DynamicTabNavigates <no-12705>`              Dynamically determine the value of the TabNavigates property.
:ref:`DynamicTag <no-12706>`                       Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-12707>`               Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-12708>`                       Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-12709>`              Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalHeaders <no-12710>`           Dynamically determine the value of the VerticalHeaders property.
:ref:`DynamicVerticalScrolling <no-12711>`         Dynamically determine the value of the VerticalScrolling property.
:ref:`DynamicVisible <no-12712>`                   Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-12713>`                     Dynamically determine the value of the Width property.
:ref:`Editable <no-12714>`                         This setting enables/disables cell editing globally.  (bool)
:ref:`Enabled <no-12715>`                          Specifies whether the object and children can get user input. (bool)
:ref:`Encoding <no-12716>`                         Name of encoding to use for unicode(str)
:ref:`Font <no-12717>`                             Specifies font object for this control. (dFont)
:ref:`FontBold <no-12718>`                         Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-12719>`                  Human-readable description of the current font settings. (str)
:ref:`FontFace <no-12720>`                         Specifies the font face. (str)
:ref:`FontInfo <no-12721>`                         Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-12722>`                       Specifies whether font is italicized. (bool)
:ref:`FontSize <no-12723>`                         Specifies the point size of the font. (int)
:ref:`FontUnderline <no-12724>`                    Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-12725>`                        Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-12726>`                             Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`HeaderBackColor <no-12727>`                  Optional color for the background of the column headers.  (str or None)
:ref:`HeaderForeColor <no-12728>`                  Optional color for the foreground (text) of the column headers.  (str or None)
:ref:`HeaderHeight <no-12729>`                     Height of the column headers.  (int)
:ref:`HeaderHorizontalAlignment <no-12730>`        The horizontal alignment of the header captions. ('Left', 'Center', 'Right')
:ref:`HeaderVerticalAlignment <no-12731>`          The vertical alignment of the header captions. ('Top', 'Center', 'Bottom')
:ref:`Height <no-12732>`                           Specifies the height of the object. (int)
:ref:`HelpContextText <no-12733>`                  Specifies the context-sensitive help text associated with this
:ref:`HorizontalScrolling <no-12734>`              Is scrolling enabled in the horizontal direction?  (bool)
:ref:`Hover <no-12735>`                            When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-12736>`                             Specifies the left position of the object. (int)
:ref:`LogEvents <no-12737>`                        Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-12738>`                    Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-12739>`                      Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-12740>`                     Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-12741>`                    Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-12742>`                      Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-12743>`                     Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-12744>`                     Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`MovableColumns <no-12745>`                   When False, the user cannot re-order the columns by dragging the headers (bool)
:ref:`MultipleSelection <no-12746>`                When True (default), more than one cell/row/col can be selected at once(bool)
:ref:`Name <no-12747>`                             Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-12748>`                         Specifies the base name of the object.
:ref:`NoneDisplay <no-12749>`                      Text to display for null (None) values.(str)
:ref:`Parent <no-12750>`                           The containing object. (obj)
:ref:`Position <no-12751>`                         The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-12752>`                Reference to the Preference Management object  (dPref)
:ref:`RegID <no-12753>`                            A unique identifier used for referencing by other objects. (str)
:ref:`ResizableColumns <no-12754>`                 When False, the user cannot resize the columns  (bool)
:ref:`ResizableRows <no-12755>`                    When False, the user cannot resize the rows(bool)
:ref:`Right <no-12756>`                            The position of the right side of the object. This is a
:ref:`RowColorEven <no-12757>`                     When alternate row coloring is active, controls the color
:ref:`RowColorOdd <no-12758>`                      When alternate row coloring is active, controls the color
:ref:`RowCount <no-12759>`                         Number of rows in the grid.(int)
:ref:`RowHeight <no-12760>`                        Row Height for all rows of the grid(int)
:ref:`RowLabelWidth <no-12761>`                    Width of the label on the left side of the rows. This only changes
:ref:`RowLabels <no-12762>`                        List of the row labels.(list)
:ref:`SameSizeRows <no-12763>`                     Is every row the same height?(bool)
:ref:`SaveRestoreDataSet <no-12764>`               Specifies whether the DataSet is persisted to preferences (bool).
:ref:`SearchDelay <no-12765>`                      Specifies the delay before incrementeal searching begins.(int or None)
:ref:`Searchable <no-12766>`                       Specifies whether the columns can be searched.  (bool)
:ref:`Selection <no-12767>`                        Returns either a list of row/column numbers if SelectionMode is set to
:ref:`SelectionBackColor <no-12768>`               BackColor of selected cells(str or RGB tuple)
:ref:`SelectionForeColor <no-12769>`               ForeColor of selected cells(str or RGB tuple)
:ref:`SelectionMode <no-12770>`                    Determines how the grid displays selections.  (str)
:ref:`ShowCellBorders <no-12771>`                  Are borders around cells shown?(bool)
:ref:`ShowColumnLabels <no-12772>`                 Are column labels shown?  (bool)
:ref:`ShowHeaders <no-12773>`                      Are grid column headers shown? (bool)
:ref:`ShowRowLabels <no-12774>`                    Are row labels shown?  (bool)
:ref:`Size <no-12775>`                             The size of the object. (tuple)
:ref:`Sizer <no-12776>`                            The sizer for the object.
:ref:`SortIndicatorColor <no-12777>`               Color of the icon is that identifies a column as being sorted.
:ref:`SortIndicatorSize <no-12778>`                Determines how large the icon is that identifies a column as
:ref:`Sortable <no-12779>`                         Specifies whether the columns can be sorted. If True,
:ref:`StatusText <no-12780>`                       Specifies the text that displays in the form's status bar, if any.
:ref:`TabNavigates <no-12781>`                     Specifies whether Tab navigates to the next control (True, the default),
:ref:`TabStop <no-12782>`                          Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-12783>`                              A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-12784>`                      Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-12785>`                              The top position of the object. (int)
:ref:`Transparency <no-12786>`                     Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-12787>`                Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`VerticalHeaders <no-12788>`                  When True, the column headers' Captions are written vertically.
:ref:`VerticalScrolling <no-12789>`                Is scrolling enabled in the vertical direction?(bool)
:ref:`Visible <no-12790>`                          Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-12791>`                  Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-12792>`                            The width of the object. (int)
:ref:`WindowHandle <no-12793>`                     The platform-specific handle for the window. Read-only. (long)

================================================== ========================


Properties
==========

.. _no-12623:

**ActivateEditorOnSelect** 

Specifies whether the cell editor, if any, is activated upon cell selection.



-------

.. _no-12624:

**AlternateRowColoring** 

When True, alternate rows of the grid are colored according to
    the RowColorOdd and RowColorEven properties     (bool)



-------

.. _no-12626:

**AutoAdjustHeaderHeight** 

When True, changing the VerticalHeaders property will adjust the HeaderHeight
    to accommodate the rotated labels. Default=False.  (bool)



-------

.. _no-12636:

**CellHighlightWidth** 

Specifies the width of the cell highlight box.



-------

.. _no-12639:

**ColumnClass** 

Class to instantiate when a change to ColumnCount requires
    additional columns to be created. Default=dColumn.    (dColumn subclass)



-------

.. _no-12640:

**ColumnCount** 

Number of columns in the grid.  (int)



-------

.. _no-12641:

**Columns** 

List of dColumns.  (list)



-------

.. _no-12644:

**CurrentCellValue** 

Value of the currently selected grid cell  (varies)



-------

.. _no-12645:

**CurrentColumn** 

Currently selected column index. (int)



-------

.. _no-12646:

**CurrentField** 

Field for the currently selected column(str)



-------

.. _no-12647:

**CurrentRow** 

Currently selected row  (int)



-------

.. _no-12648:

**DataSet** 

The set of data displayed in the grid. (set of dicts)

        When DataSource isn't defined, setting DataSet to a set of dicts,
        such as what you get from calling dBizobj.getDataSet(), will
        define the source of the data that the grid displays.

        If DataSource is defined, DataSet is read-only and returns the dataSet
        from the bizobj.



-------

.. _no-12649:

**DataSource** 

The source of the data to display in the grid. (str)

        This corresponds to a bizobj with a matching DataSource on the form,
        and setting this makes it impossible to set DataSet.



-------

.. _no-12652:

**DynamicActivateEditorOnSelect** 

Dynamically determine the value of the ActivateEditorOnSelect property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ActivateEditorOnSelect property. If DynamicActivateEditorOnSelect is set to None (the default), ActivateEditorOnSelect
will not be dynamically evaluated.



-------

.. _no-12653:

**DynamicAlternateRowColoring** 

Dynamically determine the value of the AlternateRowColoring property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AlternateRowColoring property. If DynamicAlternateRowColoring is set to None (the default), AlternateRowColoring
will not be dynamically evaluated.



-------

.. _no-12660:

**DynamicCellHighlightWidth** 

Dynamically determine the value of the CellHighlightWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CellHighlightWidth property. If DynamicCellHighlightWidth is set to None (the default), CellHighlightWidth
will not be dynamically evaluated.



-------

.. _no-12661:

**DynamicColumnClass** 

Dynamically determine the value of the ColumnClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ColumnClass property. If DynamicColumnClass is set to None (the default), ColumnClass
will not be dynamically evaluated.



-------

.. _no-12662:

**DynamicColumnCount** 

Dynamically determine the value of the ColumnCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ColumnCount property. If DynamicColumnCount is set to None (the default), ColumnCount
will not be dynamically evaluated.



-------

.. _no-12663:

**DynamicCurrentColumn** 

Dynamically determine the value of the CurrentColumn property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CurrentColumn property. If DynamicCurrentColumn is set to None (the default), CurrentColumn
will not be dynamically evaluated.



-------

.. _no-12664:

**DynamicCurrentField** 

Dynamically determine the value of the CurrentField property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CurrentField property. If DynamicCurrentField is set to None (the default), CurrentField
will not be dynamically evaluated.



-------

.. _no-12665:

**DynamicCurrentRow** 

Dynamically determine the value of the CurrentRow property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CurrentRow property. If DynamicCurrentRow is set to None (the default), CurrentRow
will not be dynamically evaluated.



-------

.. _no-12666:

**DynamicDataSet** 

Dynamically determine the value of the DataSet property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DataSet property. If DynamicDataSet is set to None (the default), DataSet
will not be dynamically evaluated.



-------

.. _no-12667:

**DynamicDataSource** 

Dynamically determine the value of the DataSource property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DataSource property. If DynamicDataSource is set to None (the default), DataSource
will not be dynamically evaluated.



-------

.. _no-12668:

**DynamicEditable** 

Dynamically determine the value of the Editable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Editable property. If DynamicEditable is set to None (the default), Editable
will not be dynamically evaluated.



-------

.. _no-12677:

**DynamicHeaderBackColor** 

Dynamically determine the value of the HeaderBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderBackColor property. If DynamicHeaderBackColor is set to None (the default), HeaderBackColor
will not be dynamically evaluated.



-------

.. _no-12678:

**DynamicHeaderForeColor** 

Dynamically determine the value of the HeaderForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderForeColor property. If DynamicHeaderForeColor is set to None (the default), HeaderForeColor
will not be dynamically evaluated.



-------

.. _no-12679:

**DynamicHeaderHeight** 

Dynamically determine the value of the HeaderHeight property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderHeight property. If DynamicHeaderHeight is set to None (the default), HeaderHeight
will not be dynamically evaluated.



-------

.. _no-12680:

**DynamicHeaderHorizontalAlignment** 

Dynamically determine the value of the HeaderHorizontalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderHorizontalAlignment property. If DynamicHeaderHorizontalAlignment is set to None (the default), HeaderHorizontalAlignment
will not be dynamically evaluated.



-------

.. _no-12681:

**DynamicHeaderVerticalAlignment** 

Dynamically determine the value of the HeaderVerticalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderVerticalAlignment property. If DynamicHeaderVerticalAlignment is set to None (the default), HeaderVerticalAlignment
will not be dynamically evaluated.



-------

.. _no-12683:

**DynamicHorizontalScrolling** 

Dynamically determine the value of the HorizontalScrolling property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScrolling property. If DynamicHorizontalScrolling is set to None (the default), HorizontalScrolling
will not be dynamically evaluated.



-------

.. _no-12687:

**DynamicRowColorEven** 

Dynamically determine the value of the RowColorEven property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowColorEven property. If DynamicRowColorEven is set to None (the default), RowColorEven
will not be dynamically evaluated.



-------

.. _no-12688:

**DynamicRowColorOdd** 

Dynamically determine the value of the RowColorOdd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowColorOdd property. If DynamicRowColorOdd is set to None (the default), RowColorOdd
will not be dynamically evaluated.



-------

.. _no-12689:

**DynamicRowHeight** 

Dynamically determine the value of the RowHeight property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowHeight property. If DynamicRowHeight is set to None (the default), RowHeight
will not be dynamically evaluated.



-------

.. _no-12690:

**DynamicRowLabelWidth** 

Dynamically determine the value of the RowLabelWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowLabelWidth property. If DynamicRowLabelWidth is set to None (the default), RowLabelWidth
will not be dynamically evaluated.



-------

.. _no-12691:

**DynamicRowLabels** 

Dynamically determine the value of the RowLabels property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowLabels property. If DynamicRowLabels is set to None (the default), RowLabels
will not be dynamically evaluated.



-------

.. _no-12692:

**DynamicSameSizeRows** 

Dynamically determine the value of the SameSizeRows property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SameSizeRows property. If DynamicSameSizeRows is set to None (the default), SameSizeRows
will not be dynamically evaluated.



-------

.. _no-12693:

**DynamicSearchDelay** 

Dynamically determine the value of the SearchDelay property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SearchDelay property. If DynamicSearchDelay is set to None (the default), SearchDelay
will not be dynamically evaluated.



-------

.. _no-12694:

**DynamicSearchable** 

Dynamically determine the value of the Searchable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Searchable property. If DynamicSearchable is set to None (the default), Searchable
will not be dynamically evaluated.



-------

.. _no-12695:

**DynamicSelectionBackColor** 

Dynamically determine the value of the SelectionBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionBackColor property. If DynamicSelectionBackColor is set to None (the default), SelectionBackColor
will not be dynamically evaluated.



-------

.. _no-12696:

**DynamicSelectionForeColor** 

Dynamically determine the value of the SelectionForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionForeColor property. If DynamicSelectionForeColor is set to None (the default), SelectionForeColor
will not be dynamically evaluated.



-------

.. _no-12697:

**DynamicSelectionMode** 

Dynamically determine the value of the SelectionMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionMode property. If DynamicSelectionMode is set to None (the default), SelectionMode
will not be dynamically evaluated.



-------

.. _no-12698:

**DynamicShowCellBorders** 

Dynamically determine the value of the ShowCellBorders property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCellBorders property. If DynamicShowCellBorders is set to None (the default), ShowCellBorders
will not be dynamically evaluated.



-------

.. _no-12699:

**DynamicShowColumnLabels** 

Dynamically determine the value of the ShowColumnLabels property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowColumnLabels property. If DynamicShowColumnLabels is set to None (the default), ShowColumnLabels
will not be dynamically evaluated.



-------

.. _no-12700:

**DynamicShowHeaders** 

Dynamically determine the value of the ShowHeaders property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowHeaders property. If DynamicShowHeaders is set to None (the default), ShowHeaders
will not be dynamically evaluated.



-------

.. _no-12701:

**DynamicShowRowLabels** 

Dynamically determine the value of the ShowRowLabels property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowRowLabels property. If DynamicShowRowLabels is set to None (the default), ShowRowLabels
will not be dynamically evaluated.



-------

.. _no-12703:

**DynamicSortable** 

Dynamically determine the value of the Sortable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Sortable property. If DynamicSortable is set to None (the default), Sortable
will not be dynamically evaluated.



-------

.. _no-12705:

**DynamicTabNavigates** 

Dynamically determine the value of the TabNavigates property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabNavigates property. If DynamicTabNavigates is set to None (the default), TabNavigates
will not be dynamically evaluated.



-------

.. _no-12710:

**DynamicVerticalHeaders** 

Dynamically determine the value of the VerticalHeaders property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalHeaders property. If DynamicVerticalHeaders is set to None (the default), VerticalHeaders
will not be dynamically evaluated.



-------

.. _no-12711:

**DynamicVerticalScrolling** 

Dynamically determine the value of the VerticalScrolling property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScrolling property. If DynamicVerticalScrolling is set to None (the default), VerticalScrolling
will not be dynamically evaluated.



-------

.. _no-12714:

**Editable** 

This setting enables/disables cell editing globally.  (bool)

    When False, no cells will be editable by the user. When True, cells in
    columns set as Editable will be editable by the user. Note that grids
    and columns are both set with Editable=False by default, so to enable
    cell editing you need to turn    it on in the appropriate column as well
    as in the grid.



-------

.. _no-12716:

**Encoding** 

Name of encoding to use for unicode(str)



-------

.. _no-12727:

**HeaderBackColor** 

Optional color for the background of the column headers.  (str or None)

    This is only the default: setting the corresponding dColumn property will
    override.



-------

.. _no-12728:

**HeaderForeColor** 

Optional color for the foreground (text) of the column headers.  (str or None)

    This is only the default: setting the corresponding dColumn property will
    override.



-------

.. _no-12729:

**HeaderHeight** 

Height of the column headers.  (int)



-------

.. _no-12730:

**HeaderHorizontalAlignment** 

The horizontal alignment of the header captions. ('Left', 'Center', 'Right')

    This is only the default: setting the corresponding dColumn property will
    override.



-------

.. _no-12731:

**HeaderVerticalAlignment** 

The vertical alignment of the header captions. ('Top', 'Center', 'Bottom')

    This is only the default: setting the corresponding dColumn property will
    override.



-------

.. _no-12734:

**HorizontalScrolling** 

Is scrolling enabled in the horizontal direction?  (bool)



-------

.. _no-12745:

**MovableColumns** 

When False, the user cannot re-order the columns by dragging the headers (bool)



-------

.. _no-12746:

**MultipleSelection** 

When True (default), more than one cell/row/col can be selected at once(bool)



-------

.. _no-12749:

**NoneDisplay** 

Text to display for null (None) values.(str)



-------

.. _no-12754:

**ResizableColumns** 

When False, the user cannot resize the columns  (bool)



-------

.. _no-12755:

**ResizableRows** 

When False, the user cannot resize the rows(bool)



-------

.. _no-12757:

**RowColorEven** 

When alternate row coloring is active, controls the color
    of the even rows  (str or tuple)



-------

.. _no-12758:

**RowColorOdd** 

When alternate row coloring is active, controls the color
    of the odd rows     (str or tuple)



-------

.. _no-12759:

**RowCount** 

Number of rows in the grid.(int)



-------

.. _no-12760:

**RowHeight** 

Row Height for all rows of the grid(int)



-------

.. _no-12761:

**RowLabelWidth** 

Width of the label on the left side of the rows. This only changes
    the grid if ShowRowLabels is True.    (int)



-------

.. _no-12762:

**RowLabels** 

List of the row labels.(list)



-------

.. _no-12763:

**SameSizeRows** 

Is every row the same height?(bool)



-------

.. _no-12764:

**SaveRestoreDataSet** 

Specifies whether the DataSet is persisted to preferences (bool).

        This allows you to build a grid to capture user input of some form, and
        instead of saving the row and field values to a database, to save the
        entire dataset to a single key in the prefs table.

        Use this sparingly for grids that won't grow too large.

        The default is False.



-------

.. _no-12765:

**SearchDelay** 

Specifies the delay before incrementeal searching begins.(int or None)

        As the user types, the search string is modified. If the time between
        keystrokes exceeds SearchDelay (milliseconds), the search will run and
        the search string    will be cleared.

        If SearchDelay is set to None (the default), Application.SearchDelay will
        be used.



-------

.. _no-12766:

**Searchable** 

Specifies whether the columns can be searched.  (bool)

        If True, columns that have their Searchable properties set to True
        will be searchable.

        Default: True



-------

.. _no-12767:

**Selection** 

Returns either a list of row/column numbers if SelectionMode is set to
    either 'Row' or 'Column'. If SelectionMode is 'Cell', returns a list of 2-tuples,
    where each 2-tuple represents a selected range of cells: the top-left and
    bottom-right coordinates for a given range. If only a single cell is selected,
    there will be only one 2-tuple in the list, with both values being the same.
    If a continuous block of cells is selected, there will be only one 2-tuple in the
    list, but the values will differ. If more than one discontinuous range is selected,
    there will be as many 2-tuples as there are range blocks.  (list)



-------

.. _no-12768:

**SelectionBackColor** 

BackColor of selected cells(str or RGB tuple)



-------

.. _no-12769:

**SelectionForeColor** 

ForeColor of selected cells(str or RGB tuple)



-------

.. _no-12771:

**ShowCellBorders** 

Are borders around cells shown?(bool)



-------

.. _no-12772:

**ShowColumnLabels** 

Are column labels shown?  (bool)

    DEPRECATED: Use ShowHeaders instead.



-------

.. _no-12773:

**ShowHeaders** 

Are grid column headers shown? (bool)



-------

.. _no-12774:

**ShowRowLabels** 

Are row labels shown?  (bool)



-------

.. _no-12777:

**SortIndicatorColor** 

Color of the icon is that identifies a column as being sorted.
    Default="yellow".  (str or color tuple)



-------

.. _no-12778:

**SortIndicatorSize** 

Determines how large the icon is that identifies a column as
    being sorted. Default=8.  (int)



-------

.. _no-12779:

**Sortable** 

Specifies whether the columns can be sorted. If True,
    and if the column's Sortable property is True, the column
    will be sortable. Default: True     (bool)



-------

.. _no-12781:

**TabNavigates** 

Specifies whether Tab navigates to the next control (True, the default),
    or if Tab moves to the next column in the grid (False).



-------

.. _no-12788:

**VerticalHeaders** 

When True, the column headers' Captions are written vertically.
    Default=False.    (bool)



-------

.. _no-12789:

**VerticalScrolling** 

Is scrolling enabled in the vertical direction?(bool)



-------


Properties - inherited
========================

.. _no-12625:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12627:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12628:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12629:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12630:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12631:

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

.. _no-12632:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12633:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12634:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12635:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12637:

**Children** 

List of dColumns, same as self.Columns.(list)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12638:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12642:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12643:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12650:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12651:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12654:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12655:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12656:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12657:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12658:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12659:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12669:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12670:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12671:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12672:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12673:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12674:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12675:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12676:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12682:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12684:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12685:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12686:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12702:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12704:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12706:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12707:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12708:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12709:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12712:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12713:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12715:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12717:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12718:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12719:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12720:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12721:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12722:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12723:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12724:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12725:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12726:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12732:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12733:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12735:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12736:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12737:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12738:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12739:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12740:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12741:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12742:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12743:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12744:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12747:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12748:

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

.. _no-12750:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12751:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12752:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12753:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12756:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12770:

**SelectionMode** 

Determines how the grid displays selections.  (str)
    Options are:
        Cells/Plain/None - no row/col highlighting    (default)
        Row - the row of the selected cell is highlighted
        Column - the column of the selected cell is highlighted

    The highlight color is determined by the SelectionBackColor and
    SelectionForeColor properties.
    


Inherited from: 'wx.grid.Grid - can not provide a link

-------

.. _no-12775:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12776:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12780:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12782:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-12783:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12784:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12785:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12786:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12787:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12790:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12791:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12792:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12793:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


================================================ ========================
:ref:`BackgroundErased <no-12794>`               Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-12795>`                         Occurs after the control or form is created.
:ref:`Destroy <no-12796>`                        Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-12797>`          Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-12798>`                       Occurs when the control gets the focus.
:ref:`GridAfterSort <no-12799>`                  Occurs after the grid is sorted
:ref:`GridBeforeSort <no-12800>`                 Occurs before the grid is sorted
:ref:`GridCellEditBegin <no-12801>`              Occurs when the editor for a grid cell is shown, allowing the user to edit.
:ref:`GridCellEditEnd <no-12802>`                Occurs when the editor for a grid cell is hidden.
:ref:`GridCellEdited <no-12803>`                 Occurs when the user edits the content of a grid cell.
:ref:`GridCellEditorHit <no-12804>`              Occurs when the user changes the value in the grid cell editor.
:ref:`GridCellSelected <no-12805>`               Occurs when the a new cell is selected in the grid.
:ref:`GridColSize <no-12806>`                    Occurs when the grid's columns are resized.
:ref:`GridContextMenu <no-12807>`                Occurs when the context menu is requested in the grid region.
:ref:`GridEvent <no-12808>`                      
:ref:`GridHeaderContextMenu <no-12809>`          Occurs when the context menu is requested in the grid header region.
:ref:`GridHeaderIdle <no-12810>`                 Occurs when an idle cycle happens in the grid header.
:ref:`GridHeaderMouseEnter <no-12811>`           Occurs when the mouse pointer enters the grid's header region.
:ref:`GridHeaderMouseLeave <no-12812>`           Occurs when the mouse pointer leaves the grid's header region.
:ref:`GridHeaderMouseLeftClick <no-12813>`       Occurs when the left mouse button is clicked in the header region.
:ref:`GridHeaderMouseLeftDoubleClick <no-12814>` Occurs when the left mouse button is double-clicked in the header region.
:ref:`GridHeaderMouseLeftDown <no-12815>`        Occurs when the left mouse button goes down in the header region.
:ref:`GridHeaderMouseLeftUp <no-12816>`          Occurs when the left mouse button goes up in the header region.
:ref:`GridHeaderMouseMove <no-12817>`            Occurs when the mouse moves in the grid header region.
:ref:`GridHeaderMouseRightClick <no-12818>`      Occurs when the right mouse button is clicked in the header region.
:ref:`GridHeaderMouseRightDown <no-12819>`       Occurs when the left mouse button goes down in the header region.
:ref:`GridHeaderMouseRightUp <no-12820>`         Occurs when the left mouse button goes up in the header region.
:ref:`GridMouseLeftClick <no-12821>`             Occurs when the left mouse button is clicked in the grid region.
:ref:`GridMouseLeftDoubleClick <no-12822>`       Occurs when the left mouse button is double-clicked in the grid region.
:ref:`GridMouseLeftDown <no-12823>`              Occurs when the left mouse button goes down in the grid region.
:ref:`GridMouseLeftUp <no-12824>`                Occurs when the left mouse button goes up in the grid region.
:ref:`GridMouseMove <no-12825>`                  Occurs when the mouse moves in the grid region (not the headers).
:ref:`GridMouseRightClick <no-12826>`            Occurs when the right mouse button is clicked in the header region.
:ref:`GridMouseRightDown <no-12827>`             Occurs when the right mouse button goes down in the grid region.
:ref:`GridMouseRightUp <no-12828>`               Occurs when the right mouse button goes up in the grid region.
:ref:`GridRangeSelected <no-12829>`              Occurs when the a new cell is selected in the grid.
:ref:`GridRowSize <no-12830>`                    Occurs when the grid's rows are resized.
:ref:`Idle <no-12831>`                           Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-12832>`                        Occurs when a key is depressed and released on the
:ref:`KeyDown <no-12833>`                        Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-12834>`                       
:ref:`KeyUp <no-12835>`                          Occurs when any key is released on the focused control or form.
:ref:`ListColumnResize <no-12836>`               Occurs when the user manually resizes a column of dListControl.
:ref:`ListHeaderMouseLeftClick <no-12837>`       Occurs when the left mouse button is clicked in the header region of dListControl.
:ref:`ListHeaderMouseRightClick <no-12838>`      Occurs when the right mouse button is clicked in the header region of dListControl.
:ref:`LostFocus <no-12839>`                      Occurs when the control loses the focus.
:ref:`MenuClose <no-12840>`                      Occurs when a menu has just been closed.
:ref:`MenuOpen <no-12841>`                       Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-12842>`                     Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-12843>`                     
:ref:`MouseLeave <no-12844>`                     Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-12845>`                 Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-12846>`           Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-12847>`                  Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-12848>`                    Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-12849>`               Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-12850>`         Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-12851>`                Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-12852>`                  Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-12853>`                      Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-12854>`                Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-12855>`          Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-12856>`                 Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-12857>`                   Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-12858>`                     Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-12859>`                           Occurs when the control's position changes.
:ref:`Paint <no-12860>`                          Occurs when it is time to paint the control.
:ref:`Resize <no-12861>`                         Occurs when the control or form is resized.
:ref:`ScrollBottom <no-12862>`                   Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-12863>`                    
:ref:`ScrollLineDown <no-12864>`                 Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-12865>`                   Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-12866>`                 Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-12867>`                   Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-12868>`                Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-12869>`             Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-12870>`                      Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-12871>`                  Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-12872>`                    Occurs when a drag operation ends in a tree.
:ref:`Update <no-12873>`                         Occurs when a container wants its controls to update

================================================ ========================


Events
=======

.. _no-12794:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-12795:

**Create** 

Occurs after the control or form is created.



-------

.. _no-12796:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-12797:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-12798:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-12799:

**GridAfterSort** 

Occurs after the grid is sorted



-------

.. _no-12800:

**GridBeforeSort** 

Occurs before the grid is sorted



-------

.. _no-12801:

**GridCellEditBegin** 

Occurs when the editor for a grid cell is shown, allowing the user to edit.



-------

.. _no-12802:

**GridCellEditEnd** 

Occurs when the editor for a grid cell is hidden.



-------

.. _no-12803:

**GridCellEdited** 

Occurs when the user edits the content of a grid cell.



-------

.. _no-12804:

**GridCellEditorHit** 

Occurs when the user changes the value in the grid cell editor.

For a checkbox, this occurs when the user toggles the checkmark.
This event is not implemented for other grid cell editors, yet.




-------

.. _no-12805:

**GridCellSelected** 

Occurs when the a new cell is selected in the grid.



-------

.. _no-12806:

**GridColSize** 

Occurs when the grid's columns are resized.



-------

.. _no-12807:

**GridContextMenu** 

Occurs when the context menu is requested in the grid region.



-------

.. _no-12808:

**GridEvent** 



-------

.. _no-12809:

**GridHeaderContextMenu** 

Occurs when the context menu is requested in the grid header region.



-------

.. _no-12810:

**GridHeaderIdle** 

Occurs when an idle cycle happens in the grid header.



-------

.. _no-12811:

**GridHeaderMouseEnter** 

Occurs when the mouse pointer enters the grid's header region.



-------

.. _no-12812:

**GridHeaderMouseLeave** 

Occurs when the mouse pointer leaves the grid's header region.



-------

.. _no-12813:

**GridHeaderMouseLeftClick** 

Occurs when the left mouse button is clicked in the header region.



-------

.. _no-12814:

**GridHeaderMouseLeftDoubleClick** 

Occurs when the left mouse button is double-clicked in the header region.



-------

.. _no-12815:

**GridHeaderMouseLeftDown** 

Occurs when the left mouse button goes down in the header region.



-------

.. _no-12816:

**GridHeaderMouseLeftUp** 

Occurs when the left mouse button goes up in the header region.



-------

.. _no-12817:

**GridHeaderMouseMove** 

Occurs when the mouse moves in the grid header region.



-------

.. _no-12818:

**GridHeaderMouseRightClick** 

Occurs when the right mouse button is clicked in the header region.



-------

.. _no-12819:

**GridHeaderMouseRightDown** 

Occurs when the left mouse button goes down in the header region.



-------

.. _no-12820:

**GridHeaderMouseRightUp** 

Occurs when the left mouse button goes up in the header region.



-------

.. _no-12821:

**GridMouseLeftClick** 

Occurs when the left mouse button is clicked in the grid region.



-------

.. _no-12822:

**GridMouseLeftDoubleClick** 

Occurs when the left mouse button is double-clicked in the grid region.



-------

.. _no-12823:

**GridMouseLeftDown** 

Occurs when the left mouse button goes down in the grid region.



-------

.. _no-12824:

**GridMouseLeftUp** 

Occurs when the left mouse button goes up in the grid region.



-------

.. _no-12825:

**GridMouseMove** 

Occurs when the mouse moves in the grid region (not the headers).



-------

.. _no-12826:

**GridMouseRightClick** 

Occurs when the right mouse button is clicked in the header region.



-------

.. _no-12827:

**GridMouseRightDown** 

Occurs when the right mouse button goes down in the grid region.



-------

.. _no-12828:

**GridMouseRightUp** 

Occurs when the right mouse button goes up in the grid region.



-------

.. _no-12829:

**GridRangeSelected** 

Occurs when the a new cell is selected in the grid.



-------

.. _no-12830:

**GridRowSize** 

Occurs when the grid's rows are resized.



-------

.. _no-12831:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-12832:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-12833:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-12834:

**KeyEvent** 



-------

.. _no-12835:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-12836:

**ListColumnResize** 

Occurs when the user manually resizes a column of dListControl.



-------

.. _no-12837:

**ListHeaderMouseLeftClick** 

Occurs when the left mouse button is clicked in the header region of dListControl.



-------

.. _no-12838:

**ListHeaderMouseRightClick** 

Occurs when the right mouse button is clicked in the header region of dListControl.



-------

.. _no-12839:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-12840:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-12841:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-12842:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-12843:

**MouseEvent** 



-------

.. _no-12844:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-12845:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-12846:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-12847:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-12848:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-12849:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-12850:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-12851:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-12852:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-12853:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-12854:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-12855:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-12856:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-12857:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-12858:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-12859:

**Move** 

Occurs when the control's position changes.



-------

.. _no-12860:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-12861:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-12862:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-12863:

**ScrollEvent** 



-------

.. _no-12864:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-12865:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-12866:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-12867:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-12868:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-12869:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-12870:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-12871:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-12872:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-12873:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================== ========================
:ref:`absoluteCoordinates <no-12874>`    Translates a position value for a control to absolute screen position.
:ref:`addColumn <no-12875>`              Adds a column to the grid.
:ref:`addColumns <no-12876>`             Adds a set of columns to the grid.
:ref:`addObject <no-12877>`              Instantiate object as a child of self.
:ref:`addToSearchStr <no-12878>`         Add a character to the current incremental search.
:ref:`afterCellEdit <no-12879>`          Called after a cell has been edited by the user.
:ref:`afterInit <no-12880>`              Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-12881>`           
:ref:`afterSetProperties <no-12882>`     
:ref:`autoBindEvents <no-12883>`         Automatically bind any on*() methods to the associated event.
:ref:`autoSizeCol <no-12884>`            Set the column to the minimum width necessary to display its data.
:ref:`beforeInit <no-12885>`             Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-12886>`    
:ref:`bindEvent <no-12887>`              Bind a dEvent to a callback function.
:ref:`bindEvents <no-12888>`             Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-12889>`                Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-12890>`           Makes this object topmost
:ref:`buildFromDataSet <no-12891>`       Add columns with properties set based on the passed dataset.
:ref:`cell <no-12892>`                   
:ref:`clear <no-12893>`                  Clears the background of custom-drawn objects.
:ref:`clone <no-12894>`                  Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-12895>`   Given a position relative to this control, return a position relative
:ref:`copy <no-12896>`                   
:ref:`customCanGetValueAs <no-12897>`    
:ref:`customCanSetValueAs <no-12898>`    
:ref:`cut <no-12899>`                    Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-12900>`                Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-12901>`             Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-12902>`             Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-12903>`            Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-12904>`        Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-12905>`           Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-12906>`               Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-12907>`          Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-12908>`            Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-12909>`          Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-12910>`   Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-12911>`               Draws text on the object at the specified position
:ref:`endHover <no-12912>`               
:ref:`fillContextMenu <no-12913>`        User hook called just before showing the context menu.
:ref:`fillGrid <no-12914>`               Refresh the grid to match the data in the data set.
:ref:`fillHeaderContextMenu <no-12915>`  User hook called just before showing the context menu for the header.
:ref:`findReplace <no-12916>`            Called from the 'Find' dialog.
:ref:`fitHeaderHeight <no-12917>`        Sizes the HeaderHeight to comfortably fit the captions. Primarily used for
:ref:`fitToSizer <no-12918>`             Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-12919>`             Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-12920>`         Reset the font zoom back to zero.
:ref:`fontZoomOut <no-12921>`            Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-12922>`        Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-12923>`        Return the fully qualified name of the object.
:ref:`getBizobj <no-12924>`              Get the bizobj that is controlling this grid.
:ref:`getCaptureBitmap <no-12925>`       Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getColByDataField <no-12926>`      Given a DataField value, return the corresponding column.
:ref:`getColByX <no-12927>`              Given the x-coordinate, return the column object.
:ref:`getColNumByX <no-12928>`           Given the x-coordinate, return the column index in self.Columns.
:ref:`getColumnValueByRow <no-12929>`    Returns the value in the given column and row.
:ref:`getContainingPage <no-12930>`      Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-12931>`       Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-12932>`       Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-12933>`     Convenience method to let you call this directly on the object.
:ref:`getProperties <no-12934>`          Returns a dictionary of property name/value pairs.
:ref:`getRowNumByY <no-12935>`           Given the y-coordinate, return the row number.
:ref:`getSizerProp <no-12936>`           Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-12937>`          Returns a dict containing the object's sizer property info. The
:ref:`getValue <no-12938>`               Returns the value of the specified row and column.
:ref:`hide <no-12939>`                   Make the object invisible.
:ref:`initEvents <no-12940>`             Hook for subclasses. User code should do custom event binding
:ref:`initHeader <no-12941>`             Initialize behavior for the grid header region.
:ref:`initProperties <no-12942>`         Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-12943>`          Returns True if the containership hierarchy for this control
:ref:`isScrollBarVisible <no-12944>`     
:ref:`iterateCall <no-12945>`            Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-12946>`            Locks the visual updates to the control.
:ref:`maxColOrder <no-12947>`            Returns the highest value of Order for all columns.
:ref:`moveColumn <no-12948>`             Move the column to a new position.
:ref:`moveTabOrderAfter <no-12949>`      Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-12950>`     Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-12951>`      Given a position relative to the form, return a position relative
:ref:`onHover <no-12952>`                
:ref:`onIncSearchTimer <no-12953>`       Occurs when the incremental search timer reaches its interval.
:ref:`paste <no-12954>`                  Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-12955>`            
:ref:`precisionFromDataField <no-12956>` Return the decimal precision for the passed data field, or the default
:ref:`processDroppedFiles <no-12957>`    Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-12958>`     Handler for text dropped on the control. Override in your
:ref:`processSort <no-12959>`            Sort the grid column.
:ref:`raiseEvent <no-12960>`             Raise the passed Dabo event.
:ref:`reCreate <no-12961>`               Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-12962>`               Recreate the object.
:ref:`redraw <no-12963>`                 Called when the object is (re)drawn.
:ref:`refresh <no-12964>`                Repaint the grid.
:ref:`relativeCoordinates <no-12965>`    Translates an absolute screen position to position value for a control.
:ref:`release <no-12966>`                Destroys the object.
:ref:`removeColumn <no-12967>`           Removes a column from the grid.
:ref:`removeColumns <no-12968>`          Removes a set of columns from the grid.
:ref:`removeDrawnObject <no-12969>`      
:ref:`restoreDataSet <no-12970>`         
:ref:`runIncSearch <no-12971>`           Run the incremental search.
:ref:`saveDataSet <no-12972>`            
:ref:`sendToBack <no-12973>`             Places this object behind all others.
:ref:`setAll <no-12974>`                 Set all child object properties to the passed value.
:ref:`setEditorForCell <no-12975>`       
:ref:`setFocus <no-12976>`               Sets focus to the object.
:ref:`setPositionInSizer <no-12977>`     Convenience method to let you call this directly on the object.
:ref:`setProperties <no-12978>`          Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-12979>`  Sets a group of properties on the object all at once. This
:ref:`setRendererForCell <no-12980>`     
:ref:`setRowHeight <no-12981>`           Explicitly set the height of a specific row in the grid. If
:ref:`setSizerProp <no-12982>`           Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-12983>`          Convenience method for setting multiple sizer item properties at once. The
:ref:`setTableAttributes <no-12984>`     Set the attributes for table display
:ref:`setValue <no-12985>`               
:ref:`show <no-12986>`                   Make the object visible.
:ref:`showColumn <no-12987>`             If the column is not shown and visible=True, show it. Likewise
:ref:`showContainingPage <no-12988>`     If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-12989>`        Display a context menu (popup) at the specified position.
:ref:`sizeToColumns <no-12990>`          Set the width of the grid equal to the sum of the widthsof the columns.
:ref:`sizeToRows <no-12991>`             Set the height of the grid equal to the sum of the heights of the rows.
:ref:`sort <no-12992>`                   Hook method used in subclasses for custom sorting.
:ref:`super <no-12993>`                  This method used to call superclass code, but it's been removed.
:ref:`typeFromDataField <no-12994>`      When the DataField is set for a column, it needs to set the corresponding
:ref:`unbindEvent <no-12995>`            Remove a previously registered event binding.
:ref:`unbindKey <no-12996>`              Unbind a previously bound key combination.
:ref:`unlockDisplay <no-12997>`          Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-12998>`       Immediately unlocks the display, no matter how many previous
:ref:`update <no-12999>`                 Call this when your datasource or dataset has changed to get the grid showing

======================================== ========================


Methods
=======

.. _no-12875:

.. function:: dabo.ui.uiwx.dGrid.dGrid.addColumn(self, col=None, inBatch=False, \*args, \**kwargs)

   Adds a column to the grid.
   
   If no col (class or instance) is passed, a blank dColumn is added, which
   can be customized later. Any extra keyword arguments are passed to the
   constructor of the new dColumn.
   



-------

.. _no-12876:

.. function:: dabo.ui.uiwx.dGrid.dGrid.addColumns(self, \*columns)

   
   Adds a set of columns to the grid.
   
   Each column in the set should be a dColumn instance.
   



-------

.. _no-12878:

.. function:: dabo.ui.uiwx.dGrid.dGrid.addToSearchStr(self, key)

   
   Add a character to the current incremental search.
   
   Called by KeyDown when the user pressed an alphanumeric key. Add the
   key to the current search and start the timer.
   



-------

.. _no-12879:

.. function:: dabo.ui.uiwx.dGrid.dGrid.afterCellEdit(self, row, col)

   Called after a cell has been edited by the user.



-------

.. _no-12884:

.. function:: dabo.ui.uiwx.dGrid.dGrid.autoSizeCol(self, colNum, persist=False)

   
   Set the column to the minimum width necessary to display its data.
   
   Set colNum='all' to auto-size all columns. Set persist=True to persist the
   new width to the user settings table.
   



-------

.. _no-12891:

.. function:: dabo.ui.uiwx.dGrid.dGrid.buildFromDataSet(self, ds, keyCaption=None, includeFields=None, colOrder=None, colWidths=None, colTypes=None, autoSizeCols=True)

   
   Add columns with properties set based on the passed dataset.
   
   A dataset is defined as one of:
   
       + a sequence of dicts, containing fieldname/fieldvalue pairs.
       + a string, which maps to a bizobj on the form.
   
   The columns will be taken from the first record of the dataset, with each
   column header caption being set to the field name, unless    the optional
   keyCaption parameter is passed. This parameter is a 1:1 dict containing
   the data set keys as its keys, and the desired caption as the
   corresponding value.
   
   If the includeFields parameter is a sequence, the only columns added will
   be the fieldnames included in the includeFields sequence. If the
   includeFields    parameter is None, all fields will be added to the grid.
   
   The columns will be in the order returned by ds.keys(), unless the
   optional colOrder parameter is passed. Like the keyCaption property,
   this is a 1:1 dict containing key:order.
   



-------

.. _no-12892:

.. function:: dabo.ui.uiwx.dGrid.dGrid.cell(self, row, col)



-------

.. _no-12896:

.. function:: dabo.ui.uiwx.dGrid.dGrid.copy(self)



-------

.. _no-12897:

.. function:: dabo.ui.uiwx.dGrid.dGrid.customCanGetValueAs(self, row, col, typ)



-------

.. _no-12898:

.. function:: dabo.ui.uiwx.dGrid.dGrid.customCanSetValueAs(self, row, col, typ)



-------

.. _no-12913:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fillContextMenu(self, menu)

   
   User hook called just before showing the context menu.
   
   User code can append menu items, or replace/remove the menu entirely.
   Return a dMenu or None from this hook. Default: no context menu.
   



-------

.. _no-12914:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fillGrid(self, force=False)

   Refresh the grid to match the data in the data set.



-------

.. _no-12915:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fillHeaderContextMenu(self, menu)

   
   User hook called just before showing the context menu for the header.
   
   User code can append menu items, or replace/remove the menu entirely.
   Return a dMenu or None from this hook. The default menu includes an
   option to autosize the column.
   



-------

.. _no-12916:

.. function:: dabo.ui.uiwx.dGrid.dGrid.findReplace(self, action, findString, replaceString, downwardSearch, wholeWord, matchCase)

   Called from the 'Find' dialog.



-------

.. _no-12917:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fitHeaderHeight(self)

   
   Sizes the HeaderHeight to comfortably fit the captions. Primarily used for
   vertical captions or multi-line captions.
   



-------

.. _no-12924:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getBizobj(self)

   
   Get the bizobj that is controlling this grid.
   
   Either there was an explicitly-set bizobj reference in
   self.DataSource, in which case that is returned, or self.DataSource
   is a string, in which case the form hierarchy is walked finding the
   first bizobj with the correct DataSource.
   
   Return None if no bizobj can be located.
   



-------

.. _no-12926:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getColByDataField(self, df)

   Given a DataField value, return the corresponding column.



-------

.. _no-12927:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getColByX(self, x)

   Given the x-coordinate, return the column object.



-------

.. _no-12928:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getColNumByX(self, x)

   Given the x-coordinate, return the column index in self.Columns.



-------

.. _no-12929:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getColumnValueByRow(self, col, row)

   Returns the value in the given column and row.



-------

.. _no-12935:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getRowNumByY(self, y)

   Given the y-coordinate, return the row number.



-------

.. _no-12938:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getValue(self, row=None, col=None)

   
   Returns the value of the specified row and column.
   
   If no row/col is specified, the current row/col will be used.
   



-------

.. _no-12941:

.. function:: dabo.ui.uiwx.dGrid.dGrid.initHeader(self)

   Initialize behavior for the grid header region.



-------

.. _no-12944:

.. function:: dabo.ui.uiwx.dGrid.dGrid.isScrollBarVisible(self, which)



-------

.. _no-12947:

.. function:: dabo.ui.uiwx.dGrid.dGrid.maxColOrder(self)

   Returns the highest value of Order for all columns.



-------

.. _no-12948:

.. function:: dabo.ui.uiwx.dGrid.dGrid.moveColumn(self, colNum, toNum)

   Move the column to a new position.



-------

.. _no-12953:

.. function:: dabo.ui.uiwx.dGrid.dGrid.onIncSearchTimer(self, evt)

   
   Occurs when the incremental search timer reaches its interval.
   It is time to run the search, if there is any search in the buffer.
   



-------

.. _no-12956:

.. function:: dabo.ui.uiwx.dGrid.dGrid.precisionFromDataField(self, df)

   
   Return the decimal precision for the passed data field, or the default
   precision if this isn't a decimal field or it isn't specified in the
   bizobj.
   



-------

.. _no-12959:

.. function:: dabo.ui.uiwx.dGrid.dGrid.processSort(self, gridCol=None, toggleSort=True)

   
   Sort the grid column.
   
   Toggle between ascending and descending. If the grid column index isn't
   passed, the currently active grid column will be sorted.
   



-------

.. _no-12964:

.. function:: dabo.ui.uiwx.dGrid.dGrid.refresh(self)

   Repaint the grid.



-------

.. _no-12967:

.. function:: dabo.ui.uiwx.dGrid.dGrid.removeColumn(self, col=None, inBatch=False)

   
   Removes a column from the grid.
   
   If no column is passed, the last column is removed. The col argument can
   be either a column index or a dColumn instance.
   



-------

.. _no-12968:

.. function:: dabo.ui.uiwx.dGrid.dGrid.removeColumns(self, \*columns)

   
   Removes a set of columns from the grid.
   
   The passed columns can be indexes or dColumn instances, or both.
   



-------

.. _no-12970:

.. function:: dabo.ui.uiwx.dGrid.dGrid.restoreDataSet(self)



-------

.. _no-12971:

.. function:: dabo.ui.uiwx.dGrid.dGrid.runIncSearch(self)

   Run the incremental search.



-------

.. _no-12972:

.. function:: dabo.ui.uiwx.dGrid.dGrid.saveDataSet(self)



-------

.. _no-12975:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setEditorForCell(self, row, col, edt)



-------

.. _no-12980:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setRendererForCell(self, row, col, rnd)



-------

.. _no-12981:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setRowHeight(self, row, ht)

   Explicitly set the height of a specific row in the grid. If
   SameSizeRows is True, all rows will be affected.
   



-------

.. _no-12984:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setTableAttributes(self, tbl=None)

   Set the attributes for table display



-------

.. _no-12985:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setValue(self, row, col, val)



-------

.. _no-12987:

.. function:: dabo.ui.uiwx.dGrid.dGrid.showColumn(self, col, visible)

   
   If the column is not shown and visible=True, show it. Likewise
   but opposite if visible=False.
   



-------

.. _no-12990:

.. function:: dabo.ui.uiwx.dGrid.dGrid.sizeToColumns(self, scrollBarFudge=True)

   
   Set the width of the grid equal to the sum of the widths    of the columns.
   
   If scrollBarFudge is True, additional space will be added to account for
   the width of the vertical scrollbar.
   



-------

.. _no-12991:

.. function:: dabo.ui.uiwx.dGrid.dGrid.sizeToRows(self, maxHeight=500, scrollBarFudge=True)

   
   Set the height of the grid equal to the sum of the heights of the rows.
   
   This is intended to be used only when the number of rows is expected to be
   low. Set maxHeight to whatever you want the maximum height to be.
   



-------

.. _no-12992:

.. function:: dabo.ui.uiwx.dGrid.dGrid.sort(self)

   Hook method used in subclasses for custom sorting.



-------

.. _no-12994:

.. function:: dabo.ui.uiwx.dGrid.dGrid.typeFromDataField(self, df, col=None)

   
   When the DataField is set for a column, it needs to set the corresponding
   value of its DataType property. Will return the Python data type, or None if
   there is no bizobj, or no DataStructure info available in the bizobj.
   



-------

.. _no-12999:

.. function:: dabo.ui.uiwx.dGrid.dGrid.update(self)

   
   Call this when your datasource or dataset has changed to get the grid showing
   the proper number of rows with current data.
   



-------


Methods - inherited
=====================

.. _no-12874:

.. function:: dabo.ui.uiwx.dGrid.dGrid.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12877:

.. function:: dabo.ui.uiwx.dGrid.dGrid.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-12880:

.. function:: dabo.ui.uiwx.dGrid.dGrid.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12881:

.. function:: dabo.ui.uiwx.dGrid.dGrid.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12882:

.. function:: dabo.ui.uiwx.dGrid.dGrid.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12883:

.. function:: dabo.ui.uiwx.dGrid.dGrid.autoBindEvents(self, force=True)
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

.. _no-12885:

.. function:: dabo.ui.uiwx.dGrid.dGrid.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12886:

.. function:: dabo.ui.uiwx.dGrid.dGrid.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12887:

.. function:: dabo.ui.uiwx.dGrid.dGrid.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12888:

.. function:: dabo.ui.uiwx.dGrid.dGrid.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12889:

.. function:: dabo.ui.uiwx.dGrid.dGrid.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-12890:

.. function:: dabo.ui.uiwx.dGrid.dGrid.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12893:

.. function:: dabo.ui.uiwx.dGrid.dGrid.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12894:

.. function:: dabo.ui.uiwx.dGrid.dGrid.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12895:

.. function:: dabo.ui.uiwx.dGrid.dGrid.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12899:

.. function:: dabo.ui.uiwx.dGrid.dGrid.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12900:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12901:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12902:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-12903:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12904:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12905:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12906:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12907:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12908:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12909:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12910:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12911:

.. function:: dabo.ui.uiwx.dGrid.dGrid.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12912:

.. function:: dabo.ui.uiwx.dGrid.dGrid.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12918:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12919:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12920:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12921:

.. function:: dabo.ui.uiwx.dGrid.dGrid.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12922:

.. function:: dabo.ui.uiwx.dGrid.dGrid.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12923:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12925:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12930:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12931:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12932:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12933:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12934:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-12936:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12937:

.. function:: dabo.ui.uiwx.dGrid.dGrid.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12939:

.. function:: dabo.ui.uiwx.dGrid.dGrid.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12940:

.. function:: dabo.ui.uiwx.dGrid.dGrid.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12942:

.. function:: dabo.ui.uiwx.dGrid.dGrid.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12943:

.. function:: dabo.ui.uiwx.dGrid.dGrid.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12945:

.. function:: dabo.ui.uiwx.dGrid.dGrid.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12946:

.. function:: dabo.ui.uiwx.dGrid.dGrid.lockDisplay(self)
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

.. _no-12949:

.. function:: dabo.ui.uiwx.dGrid.dGrid.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12950:

.. function:: dabo.ui.uiwx.dGrid.dGrid.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12951:

.. function:: dabo.ui.uiwx.dGrid.dGrid.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12952:

.. function:: dabo.ui.uiwx.dGrid.dGrid.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12954:

.. function:: dabo.ui.uiwx.dGrid.dGrid.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12955:

.. function:: dabo.ui.uiwx.dGrid.dGrid.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12957:

.. function:: dabo.ui.uiwx.dGrid.dGrid.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12958:

.. function:: dabo.ui.uiwx.dGrid.dGrid.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12960:

.. function:: dabo.ui.uiwx.dGrid.dGrid.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12961:

.. function:: dabo.ui.uiwx.dGrid.dGrid.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12962:

.. function:: dabo.ui.uiwx.dGrid.dGrid.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12963:

.. function:: dabo.ui.uiwx.dGrid.dGrid.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12965:

.. function:: dabo.ui.uiwx.dGrid.dGrid.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12966:

.. function:: dabo.ui.uiwx.dGrid.dGrid.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12969:

.. function:: dabo.ui.uiwx.dGrid.dGrid.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12973:

.. function:: dabo.ui.uiwx.dGrid.dGrid.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12974:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-12976:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12977:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12978:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-12979:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-12982:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12983:

.. function:: dabo.ui.uiwx.dGrid.dGrid.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12986:

.. function:: dabo.ui.uiwx.dGrid.dGrid.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12988:

.. function:: dabo.ui.uiwx.dGrid.dGrid.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12989:

.. function:: dabo.ui.uiwx.dGrid.dGrid.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12993:

.. function:: dabo.ui.uiwx.dGrid.dGrid.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12995:

.. function:: dabo.ui.uiwx.dGrid.dGrid.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12996:

.. function:: dabo.ui.uiwx.dGrid.dGrid.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12997:

.. function:: dabo.ui.uiwx.dGrid.dGrid.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12998:

.. function:: dabo.ui.uiwx.dGrid.dGrid.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
