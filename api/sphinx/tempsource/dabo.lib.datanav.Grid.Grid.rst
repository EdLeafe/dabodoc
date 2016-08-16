
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Grid

.. _dabo.lib.datanav.Grid.Grid:

==================================
|doc_title|  **Grid.Grid** - class
==================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Grid**

.. inheritance-diagram:: Grid


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dGrid.dGrid`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Grid.Grid


|method_summary| Properties Summary
===================================


================================================= ========================
:ref:`ActivateEditorOnSelect <no-5324>`           Specifies whether the cell editor, if any, is activated upon cell selection.
:ref:`AlternateRowColoring <no-5325>`             When True, alternate rows of the grid are colored according to
:ref:`Application <no-5326>`                      Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoAdjustHeaderHeight <no-5327>`           When True, changing the VerticalHeaders property will adjust the HeaderHeight
:ref:`BackColor <no-5328>`                        Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-5329>`                        The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-5330>`                      Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-5331>`                      Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-5332>`                  Style of line for the border drawn around the control.
:ref:`BorderStyle <no-5333>`                      Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-5334>`                      Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-5335>`                           The position of the bottom side of the object. This is a
:ref:`Caption <no-5336>`                          The caption of the object. (str)
:ref:`CellHighlightWidth <no-5337>`               Specifies the width of the cell highlight box.
:ref:`Children <no-5338>`                         List of dColumns, same as self.Columns.(list)
:ref:`Class <no-5339>`                            The class the object is based on. Read-only.  (class)
:ref:`ColumnClass <no-5340>`                      Class to instantiate when a change to ColumnCount requires
:ref:`ColumnCount <no-5341>`                      Number of columns in the grid.  (int)
:ref:`Columns <no-5342>`                          List of dColumns.  (list)
:ref:`ControllingSizer <no-5343>`                 Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-5344>`             Reference to the sizer item that control's this control's layout.
:ref:`CurrentCellValue <no-5345>`                 Value of the currently selected grid cell  (varies)
:ref:`CurrentColumn <no-5346>`                    Currently selected column index. (int)
:ref:`CurrentField <no-5347>`                     Field for the currently selected column(str)
:ref:`CurrentRow <no-5348>`                       Currently selected row  (int)
:ref:`DataSet <no-5349>`                          The set of data displayed in the grid. (set of dicts)
:ref:`DataSource <no-5350>`                       The source of the data to display in the grid. (str)
:ref:`DroppedFileHandler <no-5351>`               Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-5352>`               Reference to the object that will handle text dropped on this control.
:ref:`DynamicActivateEditorOnSelect <no-5353>`    Dynamically determine the value of the ActivateEditorOnSelect property.
:ref:`DynamicAlternateRowColoring <no-5354>`      Dynamically determine the value of the AlternateRowColoring property.
:ref:`DynamicBackColor <no-5355>`                 Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-5356>`               Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-5357>`           Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-5358>`               Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-5359>`               Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-5360>`                   Dynamically determine the value of the Caption property.
:ref:`DynamicCellHighlightWidth <no-5361>`        Dynamically determine the value of the CellHighlightWidth property.
:ref:`DynamicColumnClass <no-5362>`               Dynamically determine the value of the ColumnClass property.
:ref:`DynamicColumnCount <no-5363>`               Dynamically determine the value of the ColumnCount property.
:ref:`DynamicCurrentColumn <no-5364>`             Dynamically determine the value of the CurrentColumn property.
:ref:`DynamicCurrentField <no-5365>`              Dynamically determine the value of the CurrentField property.
:ref:`DynamicCurrentRow <no-5366>`                Dynamically determine the value of the CurrentRow property.
:ref:`DynamicDataSet <no-5367>`                   Dynamically determine the value of the DataSet property.
:ref:`DynamicDataSource <no-5368>`                Dynamically determine the value of the DataSource property.
:ref:`DynamicEditable <no-5369>`                  Dynamically determine the value of the Editable property.
:ref:`DynamicEnabled <no-5370>`                   Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-5371>`                      Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-5372>`                  Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-5373>`                  Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-5374>`                Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-5375>`                  Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-5376>`             Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-5377>`                 Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeaderBackColor <no-5378>`           Dynamically determine the value of the HeaderBackColor property.
:ref:`DynamicHeaderForeColor <no-5379>`           Dynamically determine the value of the HeaderForeColor property.
:ref:`DynamicHeaderHeight <no-5380>`              Dynamically determine the value of the HeaderHeight property.
:ref:`DynamicHeaderHorizontalAlignment <no-5381>` Dynamically determine the value of the HeaderHorizontalAlignment property.
:ref:`DynamicHeaderVerticalAlignment <no-5382>`   Dynamically determine the value of the HeaderVerticalAlignment property.
:ref:`DynamicHeight <no-5383>`                    Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScrolling <no-5384>`       Dynamically determine the value of the HorizontalScrolling property.
:ref:`DynamicLeft <no-5385>`                      Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-5386>`              Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-5387>`                  Dynamically determine the value of the Position property.
:ref:`DynamicRowColorEven <no-5388>`              Dynamically determine the value of the RowColorEven property.
:ref:`DynamicRowColorOdd <no-5389>`               Dynamically determine the value of the RowColorOdd property.
:ref:`DynamicRowHeight <no-5390>`                 Dynamically determine the value of the RowHeight property.
:ref:`DynamicRowLabelWidth <no-5391>`             Dynamically determine the value of the RowLabelWidth property.
:ref:`DynamicRowLabels <no-5392>`                 Dynamically determine the value of the RowLabels property.
:ref:`DynamicSameSizeRows <no-5393>`              Dynamically determine the value of the SameSizeRows property.
:ref:`DynamicSearchDelay <no-5394>`               Dynamically determine the value of the SearchDelay property.
:ref:`DynamicSearchable <no-5395>`                Dynamically determine the value of the Searchable property.
:ref:`DynamicSelectionBackColor <no-5396>`        Dynamically determine the value of the SelectionBackColor property.
:ref:`DynamicSelectionForeColor <no-5397>`        Dynamically determine the value of the SelectionForeColor property.
:ref:`DynamicSelectionMode <no-5398>`             Dynamically determine the value of the SelectionMode property.
:ref:`DynamicShowCellBorders <no-5399>`           Dynamically determine the value of the ShowCellBorders property.
:ref:`DynamicShowColumnLabels <no-5400>`          Dynamically determine the value of the ShowColumnLabels property.
:ref:`DynamicShowHeaders <no-5401>`               Dynamically determine the value of the ShowHeaders property.
:ref:`DynamicShowRowLabels <no-5402>`             Dynamically determine the value of the ShowRowLabels property.
:ref:`DynamicSize <no-5403>`                      Dynamically determine the value of the Size property.
:ref:`DynamicSortable <no-5404>`                  Dynamically determine the value of the Sortable property.
:ref:`DynamicStatusText <no-5405>`                Dynamically determine the value of the StatusText property.
:ref:`DynamicTabNavigates <no-5406>`              Dynamically determine the value of the TabNavigates property.
:ref:`DynamicTag <no-5407>`                       Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-5408>`               Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-5409>`                       Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-5410>`              Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalHeaders <no-5411>`           Dynamically determine the value of the VerticalHeaders property.
:ref:`DynamicVerticalScrolling <no-5412>`         Dynamically determine the value of the VerticalScrolling property.
:ref:`DynamicVisible <no-5413>`                   Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-5414>`                     Dynamically determine the value of the Width property.
:ref:`Editable <no-5415>`                         This setting enables/disables cell editing globally.  (bool)
:ref:`Enabled <no-5416>`                          Specifies whether the object and children can get user input. (bool)
:ref:`Encoding <no-5417>`                         Name of encoding to use for unicode(str)
:ref:`Font <no-5418>`                             Specifies font object for this control. (dFont)
:ref:`FontBold <no-5419>`                         Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-5420>`                  Human-readable description of the current font settings. (str)
:ref:`FontFace <no-5421>`                         Specifies the font face. (str)
:ref:`FontInfo <no-5422>`                         Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-5423>`                       Specifies whether font is italicized. (bool)
:ref:`FontSize <no-5424>`                         Specifies the point size of the font. (int)
:ref:`FontUnderline <no-5425>`                    Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-5426>`                        Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-5427>`                             Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`HeaderBackColor <no-5428>`                  Optional color for the background of the column headers.  (str or None)
:ref:`HeaderForeColor <no-5429>`                  Optional color for the foreground (text) of the column headers.  (str or None)
:ref:`HeaderHeight <no-5430>`                     Height of the column headers.  (int)
:ref:`HeaderHorizontalAlignment <no-5431>`        The horizontal alignment of the header captions. ('Left', 'Center', 'Right')
:ref:`HeaderVerticalAlignment <no-5432>`          The vertical alignment of the header captions. ('Top', 'Center', 'Bottom')
:ref:`Height <no-5433>`                           Specifies the height of the object. (int)
:ref:`HelpContextText <no-5434>`                  Specifies the context-sensitive help text associated with this
:ref:`HorizontalScrolling <no-5435>`              Is scrolling enabled in the horizontal direction?  (bool)
:ref:`Hover <no-5436>`                            When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-5437>`                             Specifies the left position of the object. (int)
:ref:`LogEvents <no-5438>`                        Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-5439>`                    Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-5440>`                      Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-5441>`                     Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-5442>`                    Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-5443>`                      Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-5444>`                     Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-5445>`                     Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`MovableColumns <no-5446>`                   When False, the user cannot re-order the columns by dragging the headers (bool)
:ref:`MultipleSelection <no-5447>`                When True (default), more than one cell/row/col can be selected at once(bool)
:ref:`Name <no-5448>`                             Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-5449>`                         Specifies the base name of the object.
:ref:`NoneDisplay <no-5450>`                      Text to display for null (None) values.(str)
:ref:`Parent <no-5451>`                           The containing object. (obj)
:ref:`Position <no-5452>`                         The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-5453>`                Reference to the Preference Management object  (dPref)
:ref:`RegID <no-5454>`                            A unique identifier used for referencing by other objects. (str)
:ref:`ResizableColumns <no-5455>`                 When False, the user cannot resize the columns  (bool)
:ref:`ResizableRows <no-5456>`                    When False, the user cannot resize the rows(bool)
:ref:`Right <no-5457>`                            The position of the right side of the object. This is a
:ref:`RowColorEven <no-5458>`                     When alternate row coloring is active, controls the color
:ref:`RowColorOdd <no-5459>`                      When alternate row coloring is active, controls the color
:ref:`RowCount <no-5460>`                         Number of rows in the grid.(int)
:ref:`RowHeight <no-5461>`                        Row Height for all rows of the grid(int)
:ref:`RowLabelWidth <no-5462>`                    Width of the label on the left side of the rows. This only changes
:ref:`RowLabels <no-5463>`                        List of the row labels.(list)
:ref:`SameSizeRows <no-5464>`                     Is every row the same height?(bool)
:ref:`SaveRestoreDataSet <no-5465>`               Specifies whether the DataSet is persisted to preferences (bool).
:ref:`SearchDelay <no-5466>`                      Specifies the delay before incrementeal searching begins.(int or None)
:ref:`Searchable <no-5467>`                       Specifies whether the columns can be searched.  (bool)
:ref:`Selection <no-5468>`                        Returns either a list of row/column numbers if SelectionMode is set to
:ref:`SelectionBackColor <no-5469>`               BackColor of selected cells(str or RGB tuple)
:ref:`SelectionForeColor <no-5470>`               ForeColor of selected cells(str or RGB tuple)
:ref:`SelectionMode <no-5471>`                    Determines how the grid displays selections.  (str)
:ref:`ShowCellBorders <no-5472>`                  Are borders around cells shown?(bool)
:ref:`ShowColumnLabels <no-5473>`                 Are column labels shown?  (bool)
:ref:`ShowHeaders <no-5474>`                      Are grid column headers shown? (bool)
:ref:`ShowRowLabels <no-5475>`                    Are row labels shown?  (bool)
:ref:`Size <no-5476>`                             The size of the object. (tuple)
:ref:`Sizer <no-5477>`                            The sizer for the object.
:ref:`SortIndicatorColor <no-5478>`               Color of the icon is that identifies a column as being sorted.
:ref:`SortIndicatorSize <no-5479>`                Determines how large the icon is that identifies a column as
:ref:`Sortable <no-5480>`                         Specifies whether the columns can be sorted. If True,
:ref:`StatusText <no-5481>`                       Specifies the text that displays in the form's status bar, if any.
:ref:`TabNavigates <no-5482>`                     Specifies whether Tab navigates to the next control (True, the default),
:ref:`TabStop <no-5483>`                          Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-5484>`                              A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-5485>`                      Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-5486>`                              The top position of the object. (int)
:ref:`Transparency <no-5487>`                     Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-5488>`                Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`VerticalHeaders <no-5489>`                  When True, the column headers' Captions are written vertically.
:ref:`VerticalScrolling <no-5490>`                Is scrolling enabled in the vertical direction?(bool)
:ref:`Visible <no-5491>`                          Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-5492>`                  Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-5493>`                            The width of the object. (int)
:ref:`WindowHandle <no-5494>`                     The platform-specific handle for the window. Read-only. (long)

================================================= ========================


Properties - inherited
========================

.. _no-5324:

**ActivateEditorOnSelect** 

Specifies whether the cell editor, if any, is activated upon cell selection.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5325:

**AlternateRowColoring** 

When True, alternate rows of the grid are colored according to
    the RowColorOdd and RowColorEven properties     (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5326:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5327:

**AutoAdjustHeaderHeight** 

When True, changing the VerticalHeaders property will adjust the HeaderHeight
    to accommodate the rotated labels. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5328:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5329:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5330:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5331:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5332:

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

.. _no-5333:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5334:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5335:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5336:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5337:

**CellHighlightWidth** 

Specifies the width of the cell highlight box.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5338:

**Children** 

List of dColumns, same as self.Columns.(list)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5339:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5340:

**ColumnClass** 

Class to instantiate when a change to ColumnCount requires
    additional columns to be created. Default=dColumn.    (dColumn subclass)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5341:

**ColumnCount** 

Number of columns in the grid.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5342:

**Columns** 

List of dColumns.  (list)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5343:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5344:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5345:

**CurrentCellValue** 

Value of the currently selected grid cell  (varies)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5346:

**CurrentColumn** 

Currently selected column index. (int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5347:

**CurrentField** 

Field for the currently selected column(str)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5348:

**CurrentRow** 

Currently selected row  (int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5349:

**DataSet** 

The set of data displayed in the grid. (set of dicts)

        When DataSource isn't defined, setting DataSet to a set of dicts,
        such as what you get from calling dBizobj.getDataSet(), will
        define the source of the data that the grid displays.

        If DataSource is defined, DataSet is read-only and returns the dataSet
        from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5350:

**DataSource** 

The source of the data to display in the grid. (str)

        This corresponds to a bizobj with a matching DataSource on the form,
        and setting this makes it impossible to set DataSet.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5351:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5352:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5353:

**DynamicActivateEditorOnSelect** 

Dynamically determine the value of the ActivateEditorOnSelect property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ActivateEditorOnSelect property. If DynamicActivateEditorOnSelect is set to None (the default), ActivateEditorOnSelect
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5354:

**DynamicAlternateRowColoring** 

Dynamically determine the value of the AlternateRowColoring property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AlternateRowColoring property. If DynamicAlternateRowColoring is set to None (the default), AlternateRowColoring
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5355:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5356:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5357:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5358:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5359:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5360:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5361:

**DynamicCellHighlightWidth** 

Dynamically determine the value of the CellHighlightWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CellHighlightWidth property. If DynamicCellHighlightWidth is set to None (the default), CellHighlightWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5362:

**DynamicColumnClass** 

Dynamically determine the value of the ColumnClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ColumnClass property. If DynamicColumnClass is set to None (the default), ColumnClass
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5363:

**DynamicColumnCount** 

Dynamically determine the value of the ColumnCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ColumnCount property. If DynamicColumnCount is set to None (the default), ColumnCount
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5364:

**DynamicCurrentColumn** 

Dynamically determine the value of the CurrentColumn property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CurrentColumn property. If DynamicCurrentColumn is set to None (the default), CurrentColumn
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5365:

**DynamicCurrentField** 

Dynamically determine the value of the CurrentField property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CurrentField property. If DynamicCurrentField is set to None (the default), CurrentField
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5366:

**DynamicCurrentRow** 

Dynamically determine the value of the CurrentRow property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CurrentRow property. If DynamicCurrentRow is set to None (the default), CurrentRow
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5367:

**DynamicDataSet** 

Dynamically determine the value of the DataSet property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DataSet property. If DynamicDataSet is set to None (the default), DataSet
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5368:

**DynamicDataSource** 

Dynamically determine the value of the DataSource property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DataSource property. If DynamicDataSource is set to None (the default), DataSource
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5369:

**DynamicEditable** 

Dynamically determine the value of the Editable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Editable property. If DynamicEditable is set to None (the default), Editable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5370:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5371:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5372:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5373:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5374:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5375:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5376:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5377:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5378:

**DynamicHeaderBackColor** 

Dynamically determine the value of the HeaderBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderBackColor property. If DynamicHeaderBackColor is set to None (the default), HeaderBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5379:

**DynamicHeaderForeColor** 

Dynamically determine the value of the HeaderForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderForeColor property. If DynamicHeaderForeColor is set to None (the default), HeaderForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5380:

**DynamicHeaderHeight** 

Dynamically determine the value of the HeaderHeight property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderHeight property. If DynamicHeaderHeight is set to None (the default), HeaderHeight
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5381:

**DynamicHeaderHorizontalAlignment** 

Dynamically determine the value of the HeaderHorizontalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderHorizontalAlignment property. If DynamicHeaderHorizontalAlignment is set to None (the default), HeaderHorizontalAlignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5382:

**DynamicHeaderVerticalAlignment** 

Dynamically determine the value of the HeaderVerticalAlignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderVerticalAlignment property. If DynamicHeaderVerticalAlignment is set to None (the default), HeaderVerticalAlignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5383:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5384:

**DynamicHorizontalScrolling** 

Dynamically determine the value of the HorizontalScrolling property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScrolling property. If DynamicHorizontalScrolling is set to None (the default), HorizontalScrolling
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5385:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5386:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5387:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5388:

**DynamicRowColorEven** 

Dynamically determine the value of the RowColorEven property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowColorEven property. If DynamicRowColorEven is set to None (the default), RowColorEven
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5389:

**DynamicRowColorOdd** 

Dynamically determine the value of the RowColorOdd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowColorOdd property. If DynamicRowColorOdd is set to None (the default), RowColorOdd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5390:

**DynamicRowHeight** 

Dynamically determine the value of the RowHeight property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowHeight property. If DynamicRowHeight is set to None (the default), RowHeight
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5391:

**DynamicRowLabelWidth** 

Dynamically determine the value of the RowLabelWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowLabelWidth property. If DynamicRowLabelWidth is set to None (the default), RowLabelWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5392:

**DynamicRowLabels** 

Dynamically determine the value of the RowLabels property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
RowLabels property. If DynamicRowLabels is set to None (the default), RowLabels
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5393:

**DynamicSameSizeRows** 

Dynamically determine the value of the SameSizeRows property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SameSizeRows property. If DynamicSameSizeRows is set to None (the default), SameSizeRows
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5394:

**DynamicSearchDelay** 

Dynamically determine the value of the SearchDelay property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SearchDelay property. If DynamicSearchDelay is set to None (the default), SearchDelay
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5395:

**DynamicSearchable** 

Dynamically determine the value of the Searchable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Searchable property. If DynamicSearchable is set to None (the default), Searchable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5396:

**DynamicSelectionBackColor** 

Dynamically determine the value of the SelectionBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionBackColor property. If DynamicSelectionBackColor is set to None (the default), SelectionBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5397:

**DynamicSelectionForeColor** 

Dynamically determine the value of the SelectionForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionForeColor property. If DynamicSelectionForeColor is set to None (the default), SelectionForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5398:

**DynamicSelectionMode** 

Dynamically determine the value of the SelectionMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionMode property. If DynamicSelectionMode is set to None (the default), SelectionMode
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5399:

**DynamicShowCellBorders** 

Dynamically determine the value of the ShowCellBorders property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCellBorders property. If DynamicShowCellBorders is set to None (the default), ShowCellBorders
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5400:

**DynamicShowColumnLabels** 

Dynamically determine the value of the ShowColumnLabels property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowColumnLabels property. If DynamicShowColumnLabels is set to None (the default), ShowColumnLabels
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5401:

**DynamicShowHeaders** 

Dynamically determine the value of the ShowHeaders property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowHeaders property. If DynamicShowHeaders is set to None (the default), ShowHeaders
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5402:

**DynamicShowRowLabels** 

Dynamically determine the value of the ShowRowLabels property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowRowLabels property. If DynamicShowRowLabels is set to None (the default), ShowRowLabels
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5403:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5404:

**DynamicSortable** 

Dynamically determine the value of the Sortable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Sortable property. If DynamicSortable is set to None (the default), Sortable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5405:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5406:

**DynamicTabNavigates** 

Dynamically determine the value of the TabNavigates property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabNavigates property. If DynamicTabNavigates is set to None (the default), TabNavigates
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5407:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5408:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5409:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5410:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5411:

**DynamicVerticalHeaders** 

Dynamically determine the value of the VerticalHeaders property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalHeaders property. If DynamicVerticalHeaders is set to None (the default), VerticalHeaders
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5412:

**DynamicVerticalScrolling** 

Dynamically determine the value of the VerticalScrolling property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScrolling property. If DynamicVerticalScrolling is set to None (the default), VerticalScrolling
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5413:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5414:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5415:

**Editable** 

This setting enables/disables cell editing globally.  (bool)

    When False, no cells will be editable by the user. When True, cells in
    columns set as Editable will be editable by the user. Note that grids
    and columns are both set with Editable=False by default, so to enable
    cell editing you need to turn    it on in the appropriate column as well
    as in the grid.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5416:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5417:

**Encoding** 

Name of encoding to use for unicode(str)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5418:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5419:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5420:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5421:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5422:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5423:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5424:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5425:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5426:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5427:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5428:

**HeaderBackColor** 

Optional color for the background of the column headers.  (str or None)

    This is only the default: setting the corresponding dColumn property will
    override.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5429:

**HeaderForeColor** 

Optional color for the foreground (text) of the column headers.  (str or None)

    This is only the default: setting the corresponding dColumn property will
    override.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5430:

**HeaderHeight** 

Height of the column headers.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5431:

**HeaderHorizontalAlignment** 

The horizontal alignment of the header captions. ('Left', 'Center', 'Right')

    This is only the default: setting the corresponding dColumn property will
    override.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5432:

**HeaderVerticalAlignment** 

The vertical alignment of the header captions. ('Top', 'Center', 'Bottom')

    This is only the default: setting the corresponding dColumn property will
    override.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5433:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5434:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5435:

**HorizontalScrolling** 

Is scrolling enabled in the horizontal direction?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5436:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5437:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5438:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5439:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5440:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5441:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5442:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5443:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5444:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5445:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5446:

**MovableColumns** 

When False, the user cannot re-order the columns by dragging the headers (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5447:

**MultipleSelection** 

When True (default), more than one cell/row/col can be selected at once(bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5448:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5449:

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

.. _no-5450:

**NoneDisplay** 

Text to display for null (None) values.(str)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5451:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5452:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5453:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5454:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5455:

**ResizableColumns** 

When False, the user cannot resize the columns  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5456:

**ResizableRows** 

When False, the user cannot resize the rows(bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5457:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5458:

**RowColorEven** 

When alternate row coloring is active, controls the color
    of the even rows  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5459:

**RowColorOdd** 

When alternate row coloring is active, controls the color
    of the odd rows     (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5460:

**RowCount** 

Number of rows in the grid.(int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5461:

**RowHeight** 

Row Height for all rows of the grid(int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5462:

**RowLabelWidth** 

Width of the label on the left side of the rows. This only changes
    the grid if ShowRowLabels is True.    (int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5463:

**RowLabels** 

List of the row labels.(list)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5464:

**SameSizeRows** 

Is every row the same height?(bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5465:

**SaveRestoreDataSet** 

Specifies whether the DataSet is persisted to preferences (bool).

        This allows you to build a grid to capture user input of some form, and
        instead of saving the row and field values to a database, to save the
        entire dataset to a single key in the prefs table.

        Use this sparingly for grids that won't grow too large.

        The default is False.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5466:

**SearchDelay** 

Specifies the delay before incrementeal searching begins.(int or None)

        As the user types, the search string is modified. If the time between
        keystrokes exceeds SearchDelay (milliseconds), the search will run and
        the search string    will be cleared.

        If SearchDelay is set to None (the default), Application.SearchDelay will
        be used.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5467:

**Searchable** 

Specifies whether the columns can be searched.  (bool)

        If True, columns that have their Searchable properties set to True
        will be searchable.

        Default: True


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5468:

**Selection** 

Returns either a list of row/column numbers if SelectionMode is set to
    either 'Row' or 'Column'. If SelectionMode is 'Cell', returns a list of 2-tuples,
    where each 2-tuple represents a selected range of cells: the top-left and
    bottom-right coordinates for a given range. If only a single cell is selected,
    there will be only one 2-tuple in the list, with both values being the same.
    If a continuous block of cells is selected, there will be only one 2-tuple in the
    list, but the values will differ. If more than one discontinuous range is selected,
    there will be as many 2-tuples as there are range blocks.  (list)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5469:

**SelectionBackColor** 

BackColor of selected cells(str or RGB tuple)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5470:

**SelectionForeColor** 

ForeColor of selected cells(str or RGB tuple)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5471:

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

.. _no-5472:

**ShowCellBorders** 

Are borders around cells shown?(bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5473:

**ShowColumnLabels** 

Are column labels shown?  (bool)

    DEPRECATED: Use ShowHeaders instead.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5474:

**ShowHeaders** 

Are grid column headers shown? (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5475:

**ShowRowLabels** 

Are row labels shown?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5476:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5477:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5478:

**SortIndicatorColor** 

Color of the icon is that identifies a column as being sorted.
    Default="yellow".  (str or color tuple)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5479:

**SortIndicatorSize** 

Determines how large the icon is that identifies a column as
    being sorted. Default=8.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5480:

**Sortable** 

Specifies whether the columns can be sorted. If True,
    and if the column's Sortable property is True, the column
    will be sortable. Default: True     (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5481:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5482:

**TabNavigates** 

Specifies whether Tab navigates to the next control (True, the default),
    or if Tab moves to the next column in the grid (False).


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5483:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-5484:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5485:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5486:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5487:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5488:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5489:

**VerticalHeaders** 

When True, the column headers' Captions are written vertically.
    Default=False.    (bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5490:

**VerticalScrolling** 

Is scrolling enabled in the vertical direction?(bool)


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5491:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5492:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5493:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5494:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


=============================================== ========================
:ref:`BackgroundErased <no-5495>`               Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-5496>`                         Occurs after the control or form is created.
:ref:`Destroy <no-5497>`                        Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-5498>`          Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-5499>`                       Occurs when the control gets the focus.
:ref:`GridAfterSort <no-5500>`                  Occurs after the grid is sorted
:ref:`GridBeforeSort <no-5501>`                 Occurs before the grid is sorted
:ref:`GridCellEditBegin <no-5502>`              Occurs when the editor for a grid cell is shown, allowing the user to edit.
:ref:`GridCellEditEnd <no-5503>`                Occurs when the editor for a grid cell is hidden.
:ref:`GridCellEdited <no-5504>`                 Occurs when the user edits the content of a grid cell.
:ref:`GridCellEditorHit <no-5505>`              Occurs when the user changes the value in the grid cell editor.
:ref:`GridCellSelected <no-5506>`               Occurs when the a new cell is selected in the grid.
:ref:`GridColSize <no-5507>`                    Occurs when the grid's columns are resized.
:ref:`GridContextMenu <no-5508>`                Occurs when the context menu is requested in the grid region.
:ref:`GridEvent <no-5509>`                      
:ref:`GridHeaderContextMenu <no-5510>`          Occurs when the context menu is requested in the grid header region.
:ref:`GridHeaderIdle <no-5511>`                 Occurs when an idle cycle happens in the grid header.
:ref:`GridHeaderMouseEnter <no-5512>`           Occurs when the mouse pointer enters the grid's header region.
:ref:`GridHeaderMouseLeave <no-5513>`           Occurs when the mouse pointer leaves the grid's header region.
:ref:`GridHeaderMouseLeftClick <no-5514>`       Occurs when the left mouse button is clicked in the header region.
:ref:`GridHeaderMouseLeftDoubleClick <no-5515>` Occurs when the left mouse button is double-clicked in the header region.
:ref:`GridHeaderMouseLeftDown <no-5516>`        Occurs when the left mouse button goes down in the header region.
:ref:`GridHeaderMouseLeftUp <no-5517>`          Occurs when the left mouse button goes up in the header region.
:ref:`GridHeaderMouseMove <no-5518>`            Occurs when the mouse moves in the grid header region.
:ref:`GridHeaderMouseRightClick <no-5519>`      Occurs when the right mouse button is clicked in the header region.
:ref:`GridHeaderMouseRightDown <no-5520>`       Occurs when the left mouse button goes down in the header region.
:ref:`GridHeaderMouseRightUp <no-5521>`         Occurs when the left mouse button goes up in the header region.
:ref:`GridMouseLeftClick <no-5522>`             Occurs when the left mouse button is clicked in the grid region.
:ref:`GridMouseLeftDoubleClick <no-5523>`       Occurs when the left mouse button is double-clicked in the grid region.
:ref:`GridMouseLeftDown <no-5524>`              Occurs when the left mouse button goes down in the grid region.
:ref:`GridMouseLeftUp <no-5525>`                Occurs when the left mouse button goes up in the grid region.
:ref:`GridMouseMove <no-5526>`                  Occurs when the mouse moves in the grid region (not the headers).
:ref:`GridMouseRightClick <no-5527>`            Occurs when the right mouse button is clicked in the header region.
:ref:`GridMouseRightDown <no-5528>`             Occurs when the right mouse button goes down in the grid region.
:ref:`GridMouseRightUp <no-5529>`               Occurs when the right mouse button goes up in the grid region.
:ref:`GridRangeSelected <no-5530>`              Occurs when the a new cell is selected in the grid.
:ref:`GridRowSize <no-5531>`                    Occurs when the grid's rows are resized.
:ref:`Idle <no-5532>`                           Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-5533>`                        Occurs when a key is depressed and released on the
:ref:`KeyDown <no-5534>`                        Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-5535>`                       
:ref:`KeyUp <no-5536>`                          Occurs when any key is released on the focused control or form.
:ref:`ListColumnResize <no-5537>`               Occurs when the user manually resizes a column of dListControl.
:ref:`ListHeaderMouseLeftClick <no-5538>`       Occurs when the left mouse button is clicked in the header region of dListControl.
:ref:`ListHeaderMouseRightClick <no-5539>`      Occurs when the right mouse button is clicked in the header region of dListControl.
:ref:`LostFocus <no-5540>`                      Occurs when the control loses the focus.
:ref:`MenuClose <no-5541>`                      Occurs when a menu has just been closed.
:ref:`MenuOpen <no-5542>`                       Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-5543>`                     Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-5544>`                     
:ref:`MouseLeave <no-5545>`                     Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-5546>`                 Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-5547>`           Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-5548>`                  Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-5549>`                    Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-5550>`               Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-5551>`         Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-5552>`                Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-5553>`                  Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-5554>`                      Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-5555>`                Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-5556>`          Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-5557>`                 Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-5558>`                   Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-5559>`                     Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-5560>`                           Occurs when the control's position changes.
:ref:`Paint <no-5561>`                          Occurs when it is time to paint the control.
:ref:`Resize <no-5562>`                         Occurs when the control or form is resized.
:ref:`ScrollBottom <no-5563>`                   Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-5564>`                    
:ref:`ScrollLineDown <no-5565>`                 Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-5566>`                   Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-5567>`                 Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-5568>`                   Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-5569>`                Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-5570>`             Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-5571>`                      Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-5572>`                  Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-5573>`                    Occurs when a drag operation ends in a tree.
:ref:`Update <no-5574>`                         Occurs when a container wants its controls to update

=============================================== ========================


Events
=======

.. _no-5495:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-5496:

**Create** 

Occurs after the control or form is created.



-------

.. _no-5497:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-5498:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-5499:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-5500:

**GridAfterSort** 

Occurs after the grid is sorted



-------

.. _no-5501:

**GridBeforeSort** 

Occurs before the grid is sorted



-------

.. _no-5502:

**GridCellEditBegin** 

Occurs when the editor for a grid cell is shown, allowing the user to edit.



-------

.. _no-5503:

**GridCellEditEnd** 

Occurs when the editor for a grid cell is hidden.



-------

.. _no-5504:

**GridCellEdited** 

Occurs when the user edits the content of a grid cell.



-------

.. _no-5505:

**GridCellEditorHit** 

Occurs when the user changes the value in the grid cell editor.

For a checkbox, this occurs when the user toggles the checkmark.
This event is not implemented for other grid cell editors, yet.




-------

.. _no-5506:

**GridCellSelected** 

Occurs when the a new cell is selected in the grid.



-------

.. _no-5507:

**GridColSize** 

Occurs when the grid's columns are resized.



-------

.. _no-5508:

**GridContextMenu** 

Occurs when the context menu is requested in the grid region.



-------

.. _no-5509:

**GridEvent** 



-------

.. _no-5510:

**GridHeaderContextMenu** 

Occurs when the context menu is requested in the grid header region.



-------

.. _no-5511:

**GridHeaderIdle** 

Occurs when an idle cycle happens in the grid header.



-------

.. _no-5512:

**GridHeaderMouseEnter** 

Occurs when the mouse pointer enters the grid's header region.



-------

.. _no-5513:

**GridHeaderMouseLeave** 

Occurs when the mouse pointer leaves the grid's header region.



-------

.. _no-5514:

**GridHeaderMouseLeftClick** 

Occurs when the left mouse button is clicked in the header region.



-------

.. _no-5515:

**GridHeaderMouseLeftDoubleClick** 

Occurs when the left mouse button is double-clicked in the header region.



-------

.. _no-5516:

**GridHeaderMouseLeftDown** 

Occurs when the left mouse button goes down in the header region.



-------

.. _no-5517:

**GridHeaderMouseLeftUp** 

Occurs when the left mouse button goes up in the header region.



-------

.. _no-5518:

**GridHeaderMouseMove** 

Occurs when the mouse moves in the grid header region.



-------

.. _no-5519:

**GridHeaderMouseRightClick** 

Occurs when the right mouse button is clicked in the header region.



-------

.. _no-5520:

**GridHeaderMouseRightDown** 

Occurs when the left mouse button goes down in the header region.



-------

.. _no-5521:

**GridHeaderMouseRightUp** 

Occurs when the left mouse button goes up in the header region.



-------

.. _no-5522:

**GridMouseLeftClick** 

Occurs when the left mouse button is clicked in the grid region.



-------

.. _no-5523:

**GridMouseLeftDoubleClick** 

Occurs when the left mouse button is double-clicked in the grid region.



-------

.. _no-5524:

**GridMouseLeftDown** 

Occurs when the left mouse button goes down in the grid region.



-------

.. _no-5525:

**GridMouseLeftUp** 

Occurs when the left mouse button goes up in the grid region.



-------

.. _no-5526:

**GridMouseMove** 

Occurs when the mouse moves in the grid region (not the headers).



-------

.. _no-5527:

**GridMouseRightClick** 

Occurs when the right mouse button is clicked in the header region.



-------

.. _no-5528:

**GridMouseRightDown** 

Occurs when the right mouse button goes down in the grid region.



-------

.. _no-5529:

**GridMouseRightUp** 

Occurs when the right mouse button goes up in the grid region.



-------

.. _no-5530:

**GridRangeSelected** 

Occurs when the a new cell is selected in the grid.



-------

.. _no-5531:

**GridRowSize** 

Occurs when the grid's rows are resized.



-------

.. _no-5532:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-5533:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-5534:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-5535:

**KeyEvent** 



-------

.. _no-5536:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-5537:

**ListColumnResize** 

Occurs when the user manually resizes a column of dListControl.



-------

.. _no-5538:

**ListHeaderMouseLeftClick** 

Occurs when the left mouse button is clicked in the header region of dListControl.



-------

.. _no-5539:

**ListHeaderMouseRightClick** 

Occurs when the right mouse button is clicked in the header region of dListControl.



-------

.. _no-5540:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-5541:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-5542:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-5543:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-5544:

**MouseEvent** 



-------

.. _no-5545:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-5546:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-5547:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-5548:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-5549:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-5550:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-5551:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-5552:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-5553:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-5554:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-5555:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-5556:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-5557:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-5558:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-5559:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-5560:

**Move** 

Occurs when the control's position changes.



-------

.. _no-5561:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-5562:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-5563:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-5564:

**ScrollEvent** 



-------

.. _no-5565:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-5566:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-5567:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-5568:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-5569:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-5570:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-5571:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-5572:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-5573:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-5574:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-5575>`    Translates a position value for a control to absolute screen position.
:ref:`addColumn <no-5576>`              Adds a column to the grid.
:ref:`addColumns <no-5577>`             Adds a set of columns to the grid.
:ref:`addObject <no-5578>`              Instantiate object as a child of self.
:ref:`addToSearchStr <no-5579>`         Add a character to the current incremental search.
:ref:`afterCellEdit <no-5580>`          Called after a cell has been edited by the user.
:ref:`afterInit <no-5581>`              Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-5582>`           
:ref:`afterSetProperties <no-5583>`     
:ref:`autoBindEvents <no-5584>`         Automatically bind any on*() methods to the associated event.
:ref:`autoSizeCol <no-5585>`            Set the column to the minimum width necessary to display its data.
:ref:`beforeInit <no-5586>`             Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-5587>`    
:ref:`bindEvent <no-5588>`              Bind a dEvent to a callback function.
:ref:`bindEvents <no-5589>`             Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-5590>`                Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-5591>`           Makes this object topmost
:ref:`buildFromDataSet <no-5592>`       Add columns with properties set based on the passed dataset.
:ref:`cell <no-5593>`                   
:ref:`clear <no-5594>`                  Clears the background of custom-drawn objects.
:ref:`clone <no-5595>`                  Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-5596>`   Given a position relative to this control, return a position relative
:ref:`copy <no-5597>`                   
:ref:`customCanGetValueAs <no-5598>`    
:ref:`customCanSetValueAs <no-5599>`    
:ref:`cut <no-5600>`                    Called by uiApp when the user requests a cut operation.
:ref:`deleteRecord <no-5601>`           Request that the current row be deleted.
:ref:`drawArc <no-5602>`                Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-5603>`             Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-5604>`             Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-5605>`            Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-5606>`        Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-5607>`           Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-5608>`               Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-5609>`          Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-5610>`            Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-5611>`          Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-5612>`   Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-5613>`               Draws text on the object at the specified position
:ref:`editRecord <no-5614>`             Request that the current row be edited.
:ref:`endHover <no-5615>`               
:ref:`fillContextMenu <no-5616>`        Display a context menu of relevant choices.
:ref:`fillGrid <no-5617>`               Refresh the grid to match the data in the data set.
:ref:`fillHeaderContextMenu <no-5618>`  User hook called just before showing the context menu for the header.
:ref:`findReplace <no-5619>`            Called from the 'Find' dialog.
:ref:`fitHeaderHeight <no-5620>`        Sizes the HeaderHeight to comfortably fit the captions. Primarily used for
:ref:`fitToSizer <no-5621>`             Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-5622>`             Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-5623>`         Reset the font zoom back to zero.
:ref:`fontZoomOut <no-5624>`            Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-5625>`        Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-5626>`        Return the fully qualified name of the object.
:ref:`getBizobj <no-5627>`              Get the bizobj that is controlling this grid.
:ref:`getCaptureBitmap <no-5628>`       Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getColByDataField <no-5629>`      Given a DataField value, return the corresponding column.
:ref:`getColByX <no-5630>`              Given the x-coordinate, return the column object.
:ref:`getColNumByX <no-5631>`           Given the x-coordinate, return the column index in self.Columns.
:ref:`getColumnValueByRow <no-5632>`    Returns the value in the given column and row.
:ref:`getContainingPage <no-5633>`      Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-5634>`       Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-5635>`       Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-5636>`     Convenience method to let you call this directly on the object.
:ref:`getProperties <no-5637>`          Returns a dictionary of property name/value pairs.
:ref:`getRowNumByY <no-5638>`           Given the y-coordinate, return the row number.
:ref:`getSizerProp <no-5639>`           Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-5640>`          Returns a dict containing the object's sizer property info. The
:ref:`getValue <no-5641>`               Returns the value of the specified row and column.
:ref:`hide <no-5642>`                   Make the object invisible.
:ref:`initEvents <no-5643>`             Hook for subclasses. User code should do custom event binding
:ref:`initHeader <no-5644>`             Initialize behavior for the grid header region.
:ref:`initProperties <no-5645>`         Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-5646>`          Returns True if the containership hierarchy for this control
:ref:`isScrollBarVisible <no-5647>`     
:ref:`iterateCall <no-5648>`            Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-5649>`            Locks the visual updates to the control.
:ref:`maxColOrder <no-5650>`            Returns the highest value of Order for all columns.
:ref:`moveColumn <no-5651>`             Move the column to a new position.
:ref:`moveTabOrderAfter <no-5652>`      Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-5653>`     Moves this object's tab order before the passed obj.
:ref:`newRecord <no-5654>`              Request that a new row be added.
:ref:`objectCoordinates <no-5655>`      Given a position relative to the form, return a position relative
:ref:`onGridLeftDClick <no-5656>`       Occurs when the user double-clicks a cell in the grid.
:ref:`onHover <no-5657>`                
:ref:`onIncSearchTimer <no-5658>`       Occurs when the incremental search timer reaches its interval.
:ref:`paste <no-5659>`                  Called by uiApp when the user requests a paste operation.
:ref:`pickRecord <no-5660>`             The form is a picklist, and the user picked a record.
:ref:`populate <no-5661>`               
:ref:`posIsWithin <no-5662>`            
:ref:`precisionFromDataField <no-5663>` Return the decimal precision for the passed data field, or the default
:ref:`processDroppedFiles <no-5664>`    Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-5665>`     Handler for text dropped on the control. Override in your
:ref:`processEditRecord <no-5666>`      
:ref:`processEsc <no-5667>`             
:ref:`processSort <no-5668>`            Sort the grid column.
:ref:`raiseEvent <no-5669>`             Raise the passed Dabo event.
:ref:`reCreate <no-5670>`               Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-5671>`               Recreate the object.
:ref:`redraw <no-5672>`                 Called when the object is (re)drawn.
:ref:`refresh <no-5673>`                Repaint the grid.
:ref:`relativeCoordinates <no-5674>`    Translates an absolute screen position to position value for a control.
:ref:`release <no-5675>`                Destroys the object.
:ref:`removeColumn <no-5676>`           Removes a column from the grid.
:ref:`removeColumns <no-5677>`          Removes a set of columns from the grid.
:ref:`removeDrawnObject <no-5678>`      
:ref:`restoreDataSet <no-5679>`         
:ref:`runIncSearch <no-5680>`           Run the incremental search.
:ref:`saveDataSet <no-5681>`            
:ref:`sendToBack <no-5682>`             Places this object behind all others.
:ref:`setAll <no-5683>`                 Set all child object properties to the passed value.
:ref:`setEditorForCell <no-5684>`       
:ref:`setFocus <no-5685>`               Sets focus to the object.
:ref:`setPositionInSizer <no-5686>`     Convenience method to let you call this directly on the object.
:ref:`setProperties <no-5687>`          Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-5688>`  Sets a group of properties on the object all at once. This
:ref:`setRendererForCell <no-5689>`     
:ref:`setRowHeight <no-5690>`           Explicitly set the height of a specific row in the grid. If
:ref:`setSizerProp <no-5691>`           Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-5692>`          Convenience method for setting multiple sizer item properties at once. The
:ref:`setTableAttributes <no-5693>`     Set the attributes for table display
:ref:`setValue <no-5694>`               
:ref:`show <no-5695>`                   Make the object visible.
:ref:`showColumn <no-5696>`             If the column is not shown and visible=True, show it. Likewise
:ref:`showContainingPage <no-5697>`     If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-5698>`        Display a context menu (popup) at the specified position.
:ref:`sizeToColumns <no-5699>`          Set the width of the grid equal to the sum of the widthsof the columns.
:ref:`sizeToRows <no-5700>`             Set the height of the grid equal to the sum of the heights of the rows.
:ref:`sort <no-5701>`                   
:ref:`super <no-5702>`                  This method used to call superclass code, but it's been removed.
:ref:`typeFromDataField <no-5703>`      When the DataField is set for a column, it needs to set the corresponding
:ref:`unbindEvent <no-5704>`            Remove a previously registered event binding.
:ref:`unbindKey <no-5705>`              Unbind a previously bound key combination.
:ref:`unlockDisplay <no-5706>`          Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-5707>`       Immediately unlocks the display, no matter how many previous
:ref:`update <no-5708>`                 Call this when your datasource or dataset has changed to get the grid showing

======================================= ========================


Methods
=======

.. _no-5601:

.. function:: dabo.lib.datanav.Grid.Grid.deleteRecord(self)

   Request that the current row be deleted.



-------

.. _no-5614:

.. function:: dabo.lib.datanav.Grid.Grid.editRecord(self)

   Request that the current row be edited.



-------

.. _no-5616:

.. function:: dabo.lib.datanav.Grid.Grid.fillContextMenu(self, menu)

   
   Display a context menu of relevant choices.
   
   By default, the choices are 'New', 'Edit', and 'Delete'.
   



-------

.. _no-5654:

.. function:: dabo.lib.datanav.Grid.Grid.newRecord(self)

   Request that a new row be added.



-------

.. _no-5656:

.. function:: dabo.lib.datanav.Grid.Grid.onGridLeftDClick(self, evt)

   
   Occurs when the user double-clicks a cell in the grid.
   By default, this is interpreted as a request to edit the record.
   



-------

.. _no-5660:

.. function:: dabo.lib.datanav.Grid.Grid.pickRecord(self)

   The form is a picklist, and the user picked a record.



-------

.. _no-5661:

.. function:: dabo.lib.datanav.Grid.Grid.populate(self)



-------

.. _no-5666:

.. function:: dabo.lib.datanav.Grid.Grid.processEditRecord(self)



-------

.. _no-5667:

.. function:: dabo.lib.datanav.Grid.Grid.processEsc(self)



-------

.. _no-5701:

.. function:: dabo.lib.datanav.Grid.Grid.sort(self)



-------


Methods - inherited
=====================

.. _no-5575:

.. function:: dabo.lib.datanav.Grid.Grid.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5576:

.. function:: dabo.lib.datanav.Grid.Grid.addColumn(self, col=None, inBatch=False, \*args, \**kwargs)
   :noindex:


   Adds a column to the grid.
   
   If no col (class or instance) is passed, a blank dColumn is added, which
   can be customized later. Any extra keyword arguments are passed to the
   constructor of the new dColumn.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5577:

.. function:: dabo.lib.datanav.Grid.Grid.addColumns(self, \*columns)
   :noindex:


   
   Adds a set of columns to the grid.
   
   Each column in the set should be a dColumn instance.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5578:

.. function:: dabo.lib.datanav.Grid.Grid.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-5579:

.. function:: dabo.lib.datanav.Grid.Grid.addToSearchStr(self, key)
   :noindex:


   
   Add a character to the current incremental search.
   
   Called by KeyDown when the user pressed an alphanumeric key. Add the
   key to the current search and start the timer.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5580:

.. function:: dabo.lib.datanav.Grid.Grid.afterCellEdit(self, row, col)
   :noindex:


   Called after a cell has been edited by the user.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5581:

.. function:: dabo.lib.datanav.Grid.Grid.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5582:

.. function:: dabo.lib.datanav.Grid.Grid.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5583:

.. function:: dabo.lib.datanav.Grid.Grid.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5584:

.. function:: dabo.lib.datanav.Grid.Grid.autoBindEvents(self, force=True)
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

.. _no-5585:

.. function:: dabo.lib.datanav.Grid.Grid.autoSizeCol(self, colNum, persist=False)
   :noindex:


   
   Set the column to the minimum width necessary to display its data.
   
   Set colNum='all' to auto-size all columns. Set persist=True to persist the
   new width to the user settings table.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5586:

.. function:: dabo.lib.datanav.Grid.Grid.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5587:

.. function:: dabo.lib.datanav.Grid.Grid.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5588:

.. function:: dabo.lib.datanav.Grid.Grid.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5589:

.. function:: dabo.lib.datanav.Grid.Grid.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5590:

.. function:: dabo.lib.datanav.Grid.Grid.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-5591:

.. function:: dabo.lib.datanav.Grid.Grid.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5592:

.. function:: dabo.lib.datanav.Grid.Grid.buildFromDataSet(self, ds, keyCaption=None, includeFields=None, colOrder=None, colWidths=None, colTypes=None, autoSizeCols=True)
   :noindex:


   
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
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5593:

.. function:: dabo.lib.datanav.Grid.Grid.cell(self, row, col)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5594:

.. function:: dabo.lib.datanav.Grid.Grid.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5595:

.. function:: dabo.lib.datanav.Grid.Grid.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5596:

.. function:: dabo.lib.datanav.Grid.Grid.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5597:

.. function:: dabo.lib.datanav.Grid.Grid.copy(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5598:

.. function:: dabo.lib.datanav.Grid.Grid.customCanGetValueAs(self, row, col, typ)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5599:

.. function:: dabo.lib.datanav.Grid.Grid.customCanSetValueAs(self, row, col, typ)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5600:

.. function:: dabo.lib.datanav.Grid.Grid.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5602:

.. function:: dabo.lib.datanav.Grid.Grid.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5603:

.. function:: dabo.lib.datanav.Grid.Grid.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5604:

.. function:: dabo.lib.datanav.Grid.Grid.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-5605:

.. function:: dabo.lib.datanav.Grid.Grid.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5606:

.. function:: dabo.lib.datanav.Grid.Grid.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5607:

.. function:: dabo.lib.datanav.Grid.Grid.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5608:

.. function:: dabo.lib.datanav.Grid.Grid.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5609:

.. function:: dabo.lib.datanav.Grid.Grid.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5610:

.. function:: dabo.lib.datanav.Grid.Grid.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5611:

.. function:: dabo.lib.datanav.Grid.Grid.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5612:

.. function:: dabo.lib.datanav.Grid.Grid.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5613:

.. function:: dabo.lib.datanav.Grid.Grid.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5615:

.. function:: dabo.lib.datanav.Grid.Grid.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5617:

.. function:: dabo.lib.datanav.Grid.Grid.fillGrid(self, force=False)
   :noindex:


   Refresh the grid to match the data in the data set.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5618:

.. function:: dabo.lib.datanav.Grid.Grid.fillHeaderContextMenu(self, menu)
   :noindex:


   
   User hook called just before showing the context menu for the header.
   
   User code can append menu items, or replace/remove the menu entirely.
   Return a dMenu or None from this hook. The default menu includes an
   option to autosize the column.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5619:

.. function:: dabo.lib.datanav.Grid.Grid.findReplace(self, action, findString, replaceString, downwardSearch, wholeWord, matchCase)
   :noindex:


   Called from the 'Find' dialog.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5620:

.. function:: dabo.lib.datanav.Grid.Grid.fitHeaderHeight(self)
   :noindex:


   
   Sizes the HeaderHeight to comfortably fit the captions. Primarily used for
   vertical captions or multi-line captions.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5621:

.. function:: dabo.lib.datanav.Grid.Grid.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5622:

.. function:: dabo.lib.datanav.Grid.Grid.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5623:

.. function:: dabo.lib.datanav.Grid.Grid.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5624:

.. function:: dabo.lib.datanav.Grid.Grid.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5625:

.. function:: dabo.lib.datanav.Grid.Grid.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5626:

.. function:: dabo.lib.datanav.Grid.Grid.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5627:

.. function:: dabo.lib.datanav.Grid.Grid.getBizobj(self)
   :noindex:


   
   Get the bizobj that is controlling this grid.
   
   Either there was an explicitly-set bizobj reference in
   self.DataSource, in which case that is returned, or self.DataSource
   is a string, in which case the form hierarchy is walked finding the
   first bizobj with the correct DataSource.
   
   Return None if no bizobj can be located.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5628:

.. function:: dabo.lib.datanav.Grid.Grid.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5629:

.. function:: dabo.lib.datanav.Grid.Grid.getColByDataField(self, df)
   :noindex:


   Given a DataField value, return the corresponding column.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5630:

.. function:: dabo.lib.datanav.Grid.Grid.getColByX(self, x)
   :noindex:


   Given the x-coordinate, return the column object.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5631:

.. function:: dabo.lib.datanav.Grid.Grid.getColNumByX(self, x)
   :noindex:


   Given the x-coordinate, return the column index in self.Columns.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5632:

.. function:: dabo.lib.datanav.Grid.Grid.getColumnValueByRow(self, col, row)
   :noindex:


   Returns the value in the given column and row.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5633:

.. function:: dabo.lib.datanav.Grid.Grid.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5634:

.. function:: dabo.lib.datanav.Grid.Grid.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5635:

.. function:: dabo.lib.datanav.Grid.Grid.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5636:

.. function:: dabo.lib.datanav.Grid.Grid.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5637:

.. function:: dabo.lib.datanav.Grid.Grid.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-5638:

.. function:: dabo.lib.datanav.Grid.Grid.getRowNumByY(self, y)
   :noindex:


   Given the y-coordinate, return the row number.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5639:

.. function:: dabo.lib.datanav.Grid.Grid.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5640:

.. function:: dabo.lib.datanav.Grid.Grid.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5641:

.. function:: dabo.lib.datanav.Grid.Grid.getValue(self, row=None, col=None)
   :noindex:


   
   Returns the value of the specified row and column.
   
   If no row/col is specified, the current row/col will be used.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5642:

.. function:: dabo.lib.datanav.Grid.Grid.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5643:

.. function:: dabo.lib.datanav.Grid.Grid.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5644:

.. function:: dabo.lib.datanav.Grid.Grid.initHeader(self)
   :noindex:


   Initialize behavior for the grid header region.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5645:

.. function:: dabo.lib.datanav.Grid.Grid.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5646:

.. function:: dabo.lib.datanav.Grid.Grid.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5647:

.. function:: dabo.lib.datanav.Grid.Grid.isScrollBarVisible(self, which)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5648:

.. function:: dabo.lib.datanav.Grid.Grid.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5649:

.. function:: dabo.lib.datanav.Grid.Grid.lockDisplay(self)
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

.. _no-5650:

.. function:: dabo.lib.datanav.Grid.Grid.maxColOrder(self)
   :noindex:


   Returns the highest value of Order for all columns.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5651:

.. function:: dabo.lib.datanav.Grid.Grid.moveColumn(self, colNum, toNum)
   :noindex:


   Move the column to a new position.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5652:

.. function:: dabo.lib.datanav.Grid.Grid.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5653:

.. function:: dabo.lib.datanav.Grid.Grid.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5655:

.. function:: dabo.lib.datanav.Grid.Grid.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5657:

.. function:: dabo.lib.datanav.Grid.Grid.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5658:

.. function:: dabo.lib.datanav.Grid.Grid.onIncSearchTimer(self, evt)
   :noindex:


   
   Occurs when the incremental search timer reaches its interval.
   It is time to run the search, if there is any search in the buffer.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5659:

.. function:: dabo.lib.datanav.Grid.Grid.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5662:

.. function:: dabo.lib.datanav.Grid.Grid.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5663:

.. function:: dabo.lib.datanav.Grid.Grid.precisionFromDataField(self, df)
   :noindex:


   
   Return the decimal precision for the passed data field, or the default
   precision if this isn't a decimal field or it isn't specified in the
   bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5664:

.. function:: dabo.lib.datanav.Grid.Grid.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5665:

.. function:: dabo.lib.datanav.Grid.Grid.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5668:

.. function:: dabo.lib.datanav.Grid.Grid.processSort(self, gridCol=None, toggleSort=True)
   :noindex:


   
   Sort the grid column.
   
   Toggle between ascending and descending. If the grid column index isn't
   passed, the currently active grid column will be sorted.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5669:

.. function:: dabo.lib.datanav.Grid.Grid.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5670:

.. function:: dabo.lib.datanav.Grid.Grid.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5671:

.. function:: dabo.lib.datanav.Grid.Grid.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5672:

.. function:: dabo.lib.datanav.Grid.Grid.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5673:

.. function:: dabo.lib.datanav.Grid.Grid.refresh(self)
   :noindex:


   Repaint the grid.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5674:

.. function:: dabo.lib.datanav.Grid.Grid.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5675:

.. function:: dabo.lib.datanav.Grid.Grid.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5676:

.. function:: dabo.lib.datanav.Grid.Grid.removeColumn(self, col=None, inBatch=False)
   :noindex:


   
   Removes a column from the grid.
   
   If no column is passed, the last column is removed. The col argument can
   be either a column index or a dColumn instance.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5677:

.. function:: dabo.lib.datanav.Grid.Grid.removeColumns(self, \*columns)
   :noindex:


   
   Removes a set of columns from the grid.
   
   The passed columns can be indexes or dColumn instances, or both.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5678:

.. function:: dabo.lib.datanav.Grid.Grid.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5679:

.. function:: dabo.lib.datanav.Grid.Grid.restoreDataSet(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5680:

.. function:: dabo.lib.datanav.Grid.Grid.runIncSearch(self)
   :noindex:


   Run the incremental search.


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5681:

.. function:: dabo.lib.datanav.Grid.Grid.saveDataSet(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5682:

.. function:: dabo.lib.datanav.Grid.Grid.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5683:

.. function:: dabo.lib.datanav.Grid.Grid.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-5684:

.. function:: dabo.lib.datanav.Grid.Grid.setEditorForCell(self, row, col, edt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5685:

.. function:: dabo.lib.datanav.Grid.Grid.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5686:

.. function:: dabo.lib.datanav.Grid.Grid.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5687:

.. function:: dabo.lib.datanav.Grid.Grid.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-5688:

.. function:: dabo.lib.datanav.Grid.Grid.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-5689:

.. function:: dabo.lib.datanav.Grid.Grid.setRendererForCell(self, row, col, rnd)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5690:

.. function:: dabo.lib.datanav.Grid.Grid.setRowHeight(self, row, ht)
   :noindex:


   Explicitly set the height of a specific row in the grid. If
   SameSizeRows is True, all rows will be affected.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5691:

.. function:: dabo.lib.datanav.Grid.Grid.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5692:

.. function:: dabo.lib.datanav.Grid.Grid.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5693:

.. function:: dabo.lib.datanav.Grid.Grid.setTableAttributes(self, tbl=None)
   :noindex:


   Set the attributes for table display


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5694:

.. function:: dabo.lib.datanav.Grid.Grid.setValue(self, row, col, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5695:

.. function:: dabo.lib.datanav.Grid.Grid.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5696:

.. function:: dabo.lib.datanav.Grid.Grid.showColumn(self, col, visible)
   :noindex:


   
   If the column is not shown and visible=True, show it. Likewise
   but opposite if visible=False.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5697:

.. function:: dabo.lib.datanav.Grid.Grid.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5698:

.. function:: dabo.lib.datanav.Grid.Grid.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5699:

.. function:: dabo.lib.datanav.Grid.Grid.sizeToColumns(self, scrollBarFudge=True)
   :noindex:


   
   Set the width of the grid equal to the sum of the widths    of the columns.
   
   If scrollBarFudge is True, additional space will be added to account for
   the width of the vertical scrollbar.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5700:

.. function:: dabo.lib.datanav.Grid.Grid.sizeToRows(self, maxHeight=500, scrollBarFudge=True)
   :noindex:


   
   Set the height of the grid equal to the sum of the heights of the rows.
   
   This is intended to be used only when the number of rows is expected to be
   low. Set maxHeight to whatever you want the maximum height to be.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5702:

.. function:: dabo.lib.datanav.Grid.Grid.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5703:

.. function:: dabo.lib.datanav.Grid.Grid.typeFromDataField(self, df, col=None)
   :noindex:


   
   When the DataField is set for a column, it needs to set the corresponding
   value of its DataType property. Will return the Python data type, or None if
   there is no bizobj, or no DataStructure info available in the bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------

.. _no-5704:

.. function:: dabo.lib.datanav.Grid.Grid.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5705:

.. function:: dabo.lib.datanav.Grid.Grid.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5706:

.. function:: dabo.lib.datanav.Grid.Grid.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5707:

.. function:: dabo.lib.datanav.Grid.Grid.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5708:

.. function:: dabo.lib.datanav.Grid.Grid.update(self)
   :noindex:


   
   Call this when your datasource or dataset has changed to get the grid showing
   the proper number of rows with current data.
   


Inherited from: :ref:`dabo.ui.uiwx.dGrid.dGrid`

-------


|
