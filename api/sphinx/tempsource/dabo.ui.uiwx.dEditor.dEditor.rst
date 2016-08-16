
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dEditor

.. _dabo.ui.uiwx.dEditor.dEditor:

========================================
|doc_title|  **dEditor.dEditor** - class
========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dEditor**

.. inheritance-diagram:: dEditor


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`
* wx.stc.StyledTextCtrl - can not provide a link



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



   * - .. image:: _static/macWidgets/dEditor.png
          :scale: 75 %
          :target: _static/macWidgets/dEditor.png
          :alt: dEditor



     - .. image:: _static/winWidgets/dEditor.png
          :scale: 75 %
          :target: _static/winWidgets/dEditor.png
          :alt: dEditor



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dEditor.dEditor

   .. automethod:: dabo.ui.uiwx.dEditor.dEditor.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-23270>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoAutoComplete <no-23271>`         Determines if auto-completion pops up without a special trigger key  (bool)
:ref:`AutoAutoCompleteMinLen <no-23272>`   When AutoAutoComplete is True, sets the minimum # of chars required
:ref:`AutoCompleteList <no-23273>`         Controls if the user has to press 'Enter/Tab' to accept
:ref:`AutoIndent <no-23274>`               Controls if a newline adds the previous line's indentation  (bool)
:ref:`BackColor <no-23275>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BackSpaceUnindents <no-23276>`       If set True then backspace, when in indentation, will go back
:ref:`BaseClass <no-23277>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-23278>`              Base key used when saving/restoring preferences  (str)
:ref:`BookmarkBackColor <no-23279>`        The color of the icon background Default=(0,255,255) (Tuple or String)
:ref:`BookmarkForeColor <no-23280>`        The color of the icon foreground Default=(128,128,128) (Tuple or String)
:ref:`BookmarkIcon <no-23281>`             The icon of bookmark that is show in the margin (default="circle") (string)
:ref:`BorderColor <no-23282>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-23283>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-23284>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-23285>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-23286>`                   The position of the bottom side of the object. This is a
:ref:`BufferedDrawing <no-23287>`          Setting to True (default) reduces display flicker  (bool)
:ref:`Caption <no-23288>`                  The caption of the object. (str)
:ref:`Children <no-23289>`                 Returns a list of object references to the children of
:ref:`Class <no-23290>`                    The class the object is based on. Read-only.  (class)
:ref:`CodeCompletion <no-23291>`           Determines if code completion is active (default=True)  (bool)
:ref:`Column <no-23292>`                   Returns the current column position of the cursor in the
:ref:`CommentString <no-23293>`            String used to prefix lines that are commented out  (str)
:ref:`ControllingSizer <no-23294>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-23295>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-23296>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-23297>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-23298>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-23299>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-23300>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-23301>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-23302>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-23303>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-23304>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-23305>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-23306>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-23307>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-23308>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-23309>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-23310>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-23311>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-23312>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-23313>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-23314>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-23315>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-23316>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-23317>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-23318>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-23319>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-23320>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-23321>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-23322>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-23323>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-23324>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-23325>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-23326>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-23327>`             Dynamically determine the value of the Width property.
:ref:`EOLMode <no-23328>`                  End of line characters. Allowed values are 'CRLF', 'LF' and 'CR'. (default=os dependent) (str)
:ref:`EdgeGuideColumn <no-23329>`          If self.EdgeGuide is set to True, specifies the column
:ref:`Enabled <no-23330>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Encoding <no-23331>`                 Type of encoding to use. Defaults to Dabo's encoding.  (str)
:ref:`FileName <no-23332>`                 Name of the file being edited (without path info)  (str)
:ref:`FilePath <no-23333>`                 Full path of the file being edited  (str)
:ref:`Font <no-23334>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-23335>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-23336>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-23337>`                 Name of the font face used in the editor  (str)
:ref:`FontInfo <no-23338>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-23339>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-23340>`                 Size of the font used in the editor  (int)
:ref:`FontUnderline <no-23341>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-23342>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-23343>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-23344>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-23345>`          Specifies the context-sensitive help text associated with this
:ref:`HiliteCharsBeyondLimit <no-23346>`   When True, characters beyond the column set it
:ref:`HiliteLimitColumn <no-23347>`        If self.HiliteCharsBeyondLimit is True, specifies
:ref:`Hover <no-23348>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-23349>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Language <no-23350>`                 Determines which language is used for the syntax coloring  (str)
:ref:`Left <no-23351>`                     Specifies the left position of the object. (int)
:ref:`LineCount <no-23352>`                Total number of lines in the document  (int)
:ref:`LineNumber <no-23353>`               Returns the current line number being edited  (int)
:ref:`LogEvents <no-23354>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-23355>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-23356>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-23357>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-23358>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-23359>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-23360>`             Minimum allowable width for the control in pixels.  (int)
:ref:`Modified <no-23361>`                 Has the content of this editor been modified?  (bool)
:ref:`MousePointer <no-23362>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-23363>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-23364>`                 Specifies the base name of the object.
:ref:`Parent <no-23365>`                   The containing object. (obj)
:ref:`PersistSecretData <no-23366>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-23367>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-23368>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-23369>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-23370>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-23371>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-23372>`         Specifies whether the Value of the control gets saved when
:ref:`Selection <no-23373>`                Selected text. (read-only) (str)
:ref:`SelectionBackColor <no-23374>`       Background color of selected text. Default=yellow  (str or tuple)
:ref:`SelectionEnd <no-23375>`             Position of the end of the selected text  (int)
:ref:`SelectionForeColor <no-23376>`       Forecolor of the selected text. Default=black  (str or tuple)
:ref:`SelectionPosition <no-23377>`        Tuple containing the start/end positions of the selected text.  (2-tuple of int)
:ref:`SelectionStart <no-23378>`           Position of the start of the selected text  (int)
:ref:`ShowCallTips <no-23379>`             Determines if call tips are shown (default=True)  (bool)
:ref:`ShowCodeFolding <no-23380>`          Determines if the code folding symbols are displayed
:ref:`ShowEOL <no-23381>`                  Determines if end-of-line markers are visible
:ref:`ShowEdgeGuide <no-23382>`            When True, will display a line at the column set by
:ref:`ShowIndentationGuides <no-23383>`    Deterimnes if indentation guides are displayed
:ref:`ShowLineNumbers <no-23384>`          Determines if line numbers are shown in the left
:ref:`ShowWhiteSpace <no-23385>`           Determines if white space characters are displayed
:ref:`Size <no-23386>`                     The size of the object. (tuple)
:ref:`Sizer <no-23387>`                    The sizer for the object.
:ref:`Source <no-23388>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-23389>`               Specifies the text that displays in the form's status bar, if any.
:ref:`SyntaxColoring <no-23390>`           Determines if syntax coloring is used (default=True)  (bool)
:ref:`TabStop <no-23391>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`TabWidth <no-23392>`                 Approximate number of spaces taken by each tab character
:ref:`Tag <no-23393>`                      A property that user code can safely use for specific purposes.
:ref:`Text <no-23394>`                     Current contents of the editor  (str)
:ref:`ToolTipText <no-23395>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-23396>`                      The top position of the object. (int)
:ref:`Transparency <no-23397>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-23398>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UseAntiAliasing <no-23399>`          Controls whether fonts are anti-aliased (default=True)  (bool)
:ref:`UseBookmarks <no-23400>`             Are we tracking bookmarks in the editor? Default=False  (bool)
:ref:`UseStyleTimer <no-23401>`            Syntax coloring can slow down sometimes. Set this to
:ref:`UseTabs <no-23402>`                  Indentation will only use space characters if useTabs
:ref:`Value <no-23403>`                    Specifies the current contents of the editor.  (basestring)
:ref:`Visible <no-23404>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-23405>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-23406>`                    The width of the object. (int)
:ref:`WindowHandle <no-23407>`             The platform-specific handle for the window. Read-only. (long)
:ref:`WordWrap <no-23408>`                 Controls whether text lines that are wider than the window
:ref:`ZoomLevel <no-23409>`                Point increase/decrease from normal viewing size  (int)

========================================== ========================


Properties
==========

.. _no-23271:

**AutoAutoComplete** 

Determines if auto-completion pops up without a special trigger key  (bool)



-------

.. _no-23272:

**AutoAutoCompleteMinLen** 

When AutoAutoComplete is True, sets the minimum # of chars required
    before the autocomplete popup appears. Default=3  (int)



-------

.. _no-23273:

**AutoCompleteList** 

Controls if the user has to press 'Enter/Tab' to accept
    the AutoComplete entry  (bool)



-------

.. _no-23274:

**AutoIndent** 

Controls if a newline adds the previous line's indentation  (bool)



-------

.. _no-23276:

**BackSpaceUnindents** 

If set True then backspace, when in indentation, will go back
    TabWidth positions; if set False then backspace will go back only one
    position. If UseTabs is True this should be set to False. (default=False)  (bool)



-------

.. _no-23279:

**BookmarkBackColor** 

The color of the icon background Default=(0,255,255) (Tuple or String)



-------

.. _no-23280:

**BookmarkForeColor** 

The color of the icon foreground Default=(128,128,128) (Tuple or String)



-------

.. _no-23281:

**BookmarkIcon** 

The icon of bookmark that is show in the margin (default="circle") (string)
    Available Values:
        - "circle"
        - "down arrow"
        - "arrow"
        - "arrows"
        - "rectangle"



-------

.. _no-23287:

**BufferedDrawing** 

Setting to True (default) reduces display flicker  (bool)



-------

.. _no-23291:

**CodeCompletion** 

Determines if code completion is active (default=True)  (bool)



-------

.. _no-23292:

**Column** 

Returns the current column position of the cursor in the
    file  (int)



-------

.. _no-23293:

**CommentString** 

String used to prefix lines that are commented out  (str)



-------

.. _no-23329:

**EdgeGuideColumn** 

If self.EdgeGuide is set to True, specifies the column
    position the guide is in(int)



-------

.. _no-23331:

**Encoding** 

Type of encoding to use. Defaults to Dabo's encoding.  (str)



-------

.. _no-23332:

**FileName** 

Name of the file being edited (without path info)  (str)



-------

.. _no-23333:

**FilePath** 

Full path of the file being edited  (str)



-------

.. _no-23346:

**HiliteCharsBeyondLimit** 

When True, characters beyond the column set it
    self.HiliteLimitColumn are visibly hilited  Note: When set to True,
    self.ShowEdgeGuide will be set to False. (bool)



-------

.. _no-23347:

**HiliteLimitColumn** 

If self.HiliteCharsBeyondLimit is True, specifies
    the limiting column  (int)



-------

.. _no-23350:

**Language** 

Determines which language is used for the syntax coloring  (str)



-------

.. _no-23353:

**LineNumber** 

Returns the current line number being edited  (int)



-------

.. _no-23361:

**Modified** 

Has the content of this editor been modified?  (bool)



-------

.. _no-23374:

**SelectionBackColor** 

Background color of selected text. Default=yellow  (str or tuple)



-------

.. _no-23376:

**SelectionForeColor** 

Forecolor of the selected text. Default=black  (str or tuple)



-------

.. _no-23377:

**SelectionPosition** 

Tuple containing the start/end positions of the selected text.  (2-tuple of int)



-------

.. _no-23379:

**ShowCallTips** 

Determines if call tips are shown (default=True)  (bool)



-------

.. _no-23380:

**ShowCodeFolding** 

Determines if the code folding symbols are displayed
    in the left margin (default=True)  (bool)



-------

.. _no-23381:

**ShowEOL** 

Determines if end-of-line markers are visible
    (default=False)  (bool)



-------

.. _no-23382:

**ShowEdgeGuide** 

When True, will display a line at the column set by
    self.EdgeGuideColumn.  Note: When set to True,
    self.HiliteCharsBeyondLimit will be set to False. (bool)



-------

.. _no-23383:

**ShowIndentationGuides** 

Deterimnes if indentation guides are displayed
    (default=False)  (bool)



-------

.. _no-23384:

**ShowLineNumbers** 

Determines if line numbers are shown in the left
    margin (default=True)  (bool)



-------

.. _no-23385:

**ShowWhiteSpace** 

Determines if white space characters are displayed
    (default=True)  (bool)



-------

.. _no-23390:

**SyntaxColoring** 

Determines if syntax coloring is used (default=True)  (bool)



-------

.. _no-23400:

**UseBookmarks** 

Are we tracking bookmarks in the editor? Default=False  (bool)



-------

.. _no-23401:

**UseStyleTimer** 

Syntax coloring can slow down sometimes. Set this to
    True to improve performance.  (bool)



-------

.. _no-23408:

**WordWrap** 

Controls whether text lines that are wider than the window
    are soft-wrapped or clipped. (bool)



-------

.. _no-23409:

**ZoomLevel** 

Point increase/decrease from normal viewing size  (int)



-------


Properties - inherited
========================

.. _no-23270:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23275:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23277:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23278:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23282:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23283:

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

.. _no-23284:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23285:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23286:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23288:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23289:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23290:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23294:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23295:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23296:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23297:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23298:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23299:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23300:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23301:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23302:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23303:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23304:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23305:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23306:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23307:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23308:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23309:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23310:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23311:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23312:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23313:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23314:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23315:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23316:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23317:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23318:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23319:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23320:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23321:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23322:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23323:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23324:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23325:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-23326:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23327:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23328:

**EOLMode** 

End of line characters. Allowed values are 'CRLF', 'LF' and 'CR'. (default=os dependent) (str)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23330:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23334:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23335:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23336:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23337:

**FontFace** 

Name of the font face used in the editor  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23338:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23339:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23340:

**FontSize** 

Size of the font used in the editor  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23341:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23342:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23343:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23344:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23345:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23348:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23349:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23351:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23352:

**LineCount** 

Total number of lines in the document  (int)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23354:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23355:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23356:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23357:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23358:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23359:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23360:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23362:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23363:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23364:

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

.. _no-23365:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23366:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23367:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23368:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23369:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23370:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23371:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23372:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23373:

**Selection** 

Selected text. (read-only) (str)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23375:

**SelectionEnd** 

Position of the end of the selected text  (int)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23378:

**SelectionStart** 

Position of the start of the selected text  (int)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23386:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23387:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-23388:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23389:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23391:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-23392:

**TabWidth** 

Approximate number of spaces taken by each tab character
    (default=4)  (int)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23393:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23394:

**Text** 

Current contents of the editor  (str)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23395:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23396:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23397:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23398:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23399:

**UseAntiAliasing** 

Controls whether fonts are anti-aliased (default=True)  (bool)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23402:

**UseTabs** 

Indentation will only use space characters if useTabs
    is False; if True, it will use a combination of tabs and
    spaces (default=True)  (bool)


Inherited from: 'wx.stc.StyledTextCtrl - can not provide a link

-------

.. _no-23403:

**Value** 

Specifies the current contents of the editor.  (basestring)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23404:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23405:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23406:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23407:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-23410>`       Occurs when a window background has been erased and needs repainting.
:ref:`ContentChanged <no-23411>`         Occurs when the contents of the Editor are modified.
:ref:`Create <no-23412>`                 Occurs after the control or form is created.
:ref:`Destroy <no-23413>`                Occurs when the control or form is destroyed.
:ref:`DocumentationHint <no-23414>`      Occurs when the editor wants documentation information to change.
:ref:`EditorEvent <no-23415>`            
:ref:`EditorStyleNeeded <no-23416>`      Occurs when the underlying editor control requires restyling.
:ref:`FontPropertiesChanged <no-23417>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-23418>`               Occurs when the control gets the focus.
:ref:`Idle <no-23419>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-23420>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-23421>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-23422>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-23423>`               
:ref:`KeyUp <no-23424>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-23425>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-23426>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-23427>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-23428>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-23429>`             
:ref:`MouseLeave <no-23430>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-23431>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-23432>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-23433>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-23434>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-23435>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-23436>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-23437>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-23438>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-23439>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-23440>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-23441>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-23442>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-23443>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-23444>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-23445>`                   Occurs when the control's position changes.
:ref:`Paint <no-23446>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-23447>`                 Occurs when the control or form is resized.
:ref:`TitleChanged <no-23448>`           Occurs when the editor's title changes.
:ref:`TreeBeginDrag <no-23449>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-23450>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-23451>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-23452>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-23410:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-23411:

**ContentChanged** 

Occurs when the contents of the Editor are modified.



-------

.. _no-23412:

**Create** 

Occurs after the control or form is created.



-------

.. _no-23413:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-23414:

**DocumentationHint** 

Occurs when the editor wants documentation information to change.

The IDE can bind to this to direct detailed documentation into a separate
window, likely replacing previous documentation. The user can choose how
to display that window, if at all.

Raise this event with three additional keyword arguments:
    + shortDoc: a one-liner call tip
    + longDoc: a multi-line call tip plus expanded documentation
    + object: a reference to the object to be documented, in case
        the listener wants to format additional information about
        the object.




-------

.. _no-23415:

**EditorEvent** 



-------

.. _no-23416:

**EditorStyleNeeded** 

Occurs when the underlying editor control requires restyling.



-------

.. _no-23417:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-23418:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-23419:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-23420:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-23421:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-23422:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-23423:

**KeyEvent** 



-------

.. _no-23424:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-23425:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-23426:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-23427:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-23428:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-23429:

**MouseEvent** 



-------

.. _no-23430:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-23431:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-23432:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-23433:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-23434:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-23435:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-23436:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-23437:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-23438:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-23439:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-23440:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-23441:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-23442:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-23443:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-23444:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-23445:

**Move** 

Occurs when the control's position changes.



-------

.. _no-23446:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-23447:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-23448:

**TitleChanged** 

Occurs when the editor's title changes.



-------

.. _no-23449:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-23450:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-23451:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-23452:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


========================================= ========================
:ref:`absoluteCoordinates <no-23453>`     Translates a position value for a control to absolute screen position.
:ref:`addObject <no-23454>`               Instantiate object as a child of self.
:ref:`afterInit <no-23455>`               Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-23456>`            
:ref:`afterSetProperties <no-23457>`      
:ref:`autoBindEvents <no-23458>`          Automatically bind any on*() methods to the associated event.
:ref:`autoComplete <no-23459>`            
:ref:`beforeInit <no-23460>`              Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-23461>`     
:ref:`bindEvent <no-23462>`               Bind a dEvent to a callback function.
:ref:`bindEvents <no-23463>`              Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-23464>`                 Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-23465>`            Makes this object topmost
:ref:`callTip <no-23466>`                 Present the call tip for the current object, if any.
:ref:`changeFontFace <no-23467>`          
:ref:`changeFontSize <no-23468>`          
:ref:`changeSelectedTextCase <no-23469>`  
:ref:`checkChangesAndContinue <no-23470>` Check to see if changes need to be saved, and if so prompt the user.
:ref:`checkForDiskUpdate <no-23471>`      Returns True or False depending on whether the file on disk has been modified
:ref:`clear <no-23472>`                   Clears the background of custom-drawn objects.
:ref:`clearAllBookmarks <no-23473>`       Removes all bookmarks.
:ref:`clearBookmark <no-23474>`           Clears the specified bookmark. If no such bookmark
:ref:`clone <no-23475>`                   Create another object just like the passed object. It assumes that the
:ref:`codeComplete <no-23476>`            Display the code completion list for the current object, if any.
:ref:`containerCoordinates <no-23477>`    Given a position relative to this control, return a position relative
:ref:`copy <no-23478>`                    Called by uiApp when the user requests a copy operation.
:ref:`cut <no-23479>`                     Called by uiApp when the user requests a cut operation.
:ref:`decreaseTextSize <no-23480>`        
:ref:`drawArc <no-23481>`                 Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-23482>`              Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-23483>`              Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-23484>`             Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-23485>`         Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-23486>`            Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-23487>`                Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-23488>`           Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-23489>`             Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-23490>`           Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-23491>`    Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-23492>`                Draws text on the object at the specified position
:ref:`endHover <no-23493>`                
:ref:`ensureLineVisible <no-23494>`       
:ref:`findBookmark <no-23495>`            Moves to the line for the specified bookmark. If no such
:ref:`fitToSizer <no-23496>`              Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-23497>`              Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-23498>`              Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-23499>`          Reset the font zoom back to zero.
:ref:`fontZoomOut <no-23500>`             Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-23501>`         Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-23502>`         Return the fully qualified name of the object.
:ref:`getBlankValue <no-23503>`           Return the empty value of the control.
:ref:`getBookmarkFromLine <no-23504>`     Returns the name of the bookmark for the passed
:ref:`getBookmarkList <no-23505>`         Returns a list of all current bookmark names.
:ref:`getCaptureBitmap <no-23506>`        Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-23507>`       Return the dPage or WizardPage that contains self.
:ref:`getCurrentLineBookmark <no-23508>`  Returns the name of the bookmark for the current
:ref:`getDisplayLocker <no-23509>`        Returns an object that locks the current display when created, and
:ref:`getFunctionList <no-23510>`         Returns a list of all 'class' and 'def' statements, along
:ref:`getLineFromPosition <no-23511>`     Given a position within the text, returns the corresponding line
:ref:`getLineText <no-23512>`             Returns the full text of the line containing specified position, or if
:ref:`getMarginWidth <no-23513>`          Returns the width of the non-editing area along the left side.
:ref:`getMousePosition <no-23514>`        Returns the current mouse position on the entire screen
:ref:`getPositionFromLine <no-23515>`     Given a line number, returns the position of the start of that line.
:ref:`getPositionFromXY <no-23516>`       Given an x,y position, returns the position in the text if that point
:ref:`getPositionInSizer <no-23517>`      Convenience method to let you call this directly on the object.
:ref:`getProperties <no-23518>`           Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-23519>`        
:ref:`getSizerProp <no-23520>`            Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-23521>`           Returns a dict containing the object's sizer property info. The
:ref:`getWord <no-23522>`                 
:ref:`getWordObject <no-23523>`           
:ref:`getWords <no-23524>`                
:ref:`goNextBookMark <no-23525>`          Moves to the next bookmark in the document. If the
:ref:`goPrevBookMark <no-23526>`          Moves to the previous bookmark in the document. If the
:ref:`hide <no-23527>`                    Make the object invisible.
:ref:`hiliteLine <no-23528>`              Selects the specified line. If the line number does not exist,
:ref:`increaseTextSize <no-23529>`        
:ref:`initEvents <no-23530>`              Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-23531>`          Hook for subclasses. User subclasses should set properties
:ref:`isChanged <no-23532>`               
:ref:`isContainedBy <no-23533>`           Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-23534>`             Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-23535>`             Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-23536>`       Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-23537>`      Moves this object's tab order before the passed obj.
:ref:`moveToBeginning <no-23538>`         
:ref:`moveToEnd <no-23539>`               
:ref:`newFile <no-23540>`                 Create a new file and edit it.
:ref:`objectCoordinates <no-23541>`       Given a position relative to the form, return a position relative
:ref:`onCommentLine <no-23542>`           
:ref:`onHover <no-23543>`                 
:ref:`onIdle <no-23544>`                  
:ref:`onListSelection <no-23545>`         
:ref:`onPrint <no-23546>`                 
:ref:`onPrintPreview <no-23547>`          
:ref:`onPrintSetup <no-23548>`            
:ref:`onUncommentLine <no-23549>`         
:ref:`openFile <no-23550>`                Open a new file and edit it.
:ref:`paste <no-23551>`                   Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-23552>`             
:ref:`processBookmarkClick <no-23553>`    Stub function to process a left click on the bookmark margin area.
:ref:`processDroppedFiles <no-23554>`     Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-23555>`      Handler for text dropped on the control. Override in your
:ref:`promptForFileName <no-23556>`       Prompt the user for a file name.
:ref:`promptForSaveAs <no-23557>`         Prompt user for the filename to save the file as.
:ref:`promptToSave <no-23558>`            
:ref:`raiseEvent <no-23559>`              Raise the passed Dabo event.
:ref:`reCreate <no-23560>`                Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-23561>`                Recreate the object.
:ref:`redraw <no-23562>`                  Called when the object is (re)drawn.
:ref:`refresh <no-23563>`                 Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-23564>`     Translates an absolute screen position to position value for a control.
:ref:`release <no-23565>`                 Destroys the object.
:ref:`removeDrawnObject <no-23566>`       
:ref:`restoreTextSize <no-23567>`         
:ref:`restoreValue <no-23568>`            Set the control's value to the value in dApp's user settings table.
:ref:`saveFile <no-23569>`                
:ref:`saveValue <no-23570>`               Save control's value to dApp's user settings table.
:ref:`select <no-23571>`                  Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-23572>`               Select all text in the control.
:ref:`selectLine <no-23573>`              
:ref:`selectNone <no-23574>`              Select no text in the control.
:ref:`selectWord <no-23575>`              
:ref:`sendToBack <no-23576>`              Places this object behind all others.
:ref:`setAll <no-23577>`                  Set all child object properties to the passed value.
:ref:`setBookmark <no-23578>`             Creates a bookmark that can be referenced by the
:ref:`setDefaultFont <no-23579>`          
:ref:`setDefaults <no-23580>`             
:ref:`setDocumentDefaults <no-23581>`     
:ref:`setFocus <no-23582>`                Sets focus to the object.
:ref:`setFormCallbacks <no-23583>`        
:ref:`setInactive <no-23584>`             Hides the auto-completion popup if one is open.
:ref:`setPositionInSizer <no-23585>`      Convenience method to let you call this directly on the object.
:ref:`setProperties <no-23586>`           Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-23587>`   Sets a group of properties on the object all at once. This
:ref:`setPyFont <no-23588>`               
:ref:`setSizerProp <no-23589>`            Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-23590>`           Convenience method for setting multiple sizer item properties at once. The
:ref:`setSyntaxColoring <no-23591>`       Sets the appropriate lexer for syntax coloring.
:ref:`setTitle <no-23592>`                Set the title of the editor
:ref:`show <no-23593>`                    Make the object visible.
:ref:`showContainingPage <no-23594>`      If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-23595>`         Display a context menu (popup) at the specified position.
:ref:`showCurrentLine <no-23596>`         Scrolls the editor so that the current position is visible.
:ref:`super <no-23597>`                   This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-23598>`             Remove a previously registered event binding.
:ref:`unbindKey <no-23599>`               Unbind a previously bound key combination.
:ref:`unlockDisplay <no-23600>`           Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-23601>`        Immediately unlocks the display, no matter how many previous
:ref:`update <no-23602>`                  Update control's value to match the current value from the source.

========================================= ========================


Methods
=======

.. _no-23459:

.. function:: dabo.ui.uiwx.dEditor.dEditor.autoComplete(self, obj=0, minWordLen=0)



-------

.. _no-23466:

.. function:: dabo.ui.uiwx.dEditor.dEditor.callTip(self)

   Present the call tip for the current object, if any.



-------

.. _no-23467:

.. function:: dabo.ui.uiwx.dEditor.dEditor.changeFontFace(self, fontFace)



-------

.. _no-23468:

.. function:: dabo.ui.uiwx.dEditor.dEditor.changeFontSize(self, fontSize)



-------

.. _no-23469:

.. function:: dabo.ui.uiwx.dEditor.dEditor.changeSelectedTextCase(self, newcase)



-------

.. _no-23470:

.. function:: dabo.ui.uiwx.dEditor.dEditor.checkChangesAndContinue(self)

   
   Check to see if changes need to be saved, and if so prompt the user.
   
   Return False if saves were needed but not made.
   



-------

.. _no-23471:

.. function:: dabo.ui.uiwx.dEditor.dEditor.checkForDiskUpdate(self)

   
   Returns True or False depending on whether the file on disk has been modified
   since it was opened. It is up to the calling code to decide what to do with this
   information.
   



-------

.. _no-23473:

.. function:: dabo.ui.uiwx.dEditor.dEditor.clearAllBookmarks(self)

   Removes all bookmarks.



-------

.. _no-23474:

.. function:: dabo.ui.uiwx.dEditor.dEditor.clearBookmark(self, nm)

   
   Clears the specified bookmark. If no such bookmark
   exists, does nothing.
   



-------

.. _no-23476:

.. function:: dabo.ui.uiwx.dEditor.dEditor.codeComplete(self)

   Display the code completion list for the current object, if any.



-------

.. _no-23480:

.. function:: dabo.ui.uiwx.dEditor.dEditor.decreaseTextSize(self, pts=1)



-------

.. _no-23494:

.. function:: dabo.ui.uiwx.dEditor.dEditor.ensureLineVisible(self, line)



-------

.. _no-23495:

.. function:: dabo.ui.uiwx.dEditor.dEditor.findBookmark(self, nm)

   
   Moves to the line for the specified bookmark. If no such
   bookmark exists, does nothing.
   



-------

.. _no-23504:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getBookmarkFromLine(self, line)

   
   Returns the name of the bookmark for the passed
   line, or None if the line is not bookmarked.
   



-------

.. _no-23505:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getBookmarkList(self)

   Returns a list of all current bookmark names.



-------

.. _no-23508:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getCurrentLineBookmark(self)

   
   Returns the name of the bookmark for the current
   line, or None if this line is not bookmarked.
   



-------

.. _no-23510:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getFunctionList(self)

   
   Returns a list of all 'class' and 'def' statements, along
   with their starting positions in the text.
   



-------

.. _no-23511:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getLineFromPosition(self, pos)

   
   Given a position within the text, returns the corresponding line
   number. If the position is invalid, returns -1.
   



-------

.. _no-23512:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getLineText(self, pos=None)

   
   Returns the full text of the line containing specified position, or if
   no position is passed, for the current insertion point.
   



-------

.. _no-23513:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getMarginWidth(self)

   Returns the width of the non-editing area along the left side.



-------

.. _no-23515:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getPositionFromLine(self, linenum)

   
   Given a line number, returns the position of the start of that line.
   If the line number is invalid, returns -1.



-------

.. _no-23516:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getPositionFromXY(self, x, y=None)

   
   Given an x,y position, returns the position in the text if that point
   is close to any text; if not, returns -1.
   



-------

.. _no-23522:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getWord(self, whole=None)



-------

.. _no-23523:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getWordObject(self, word=None, whole=None)



-------

.. _no-23524:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getWords(self, word=None, whole=None)



-------

.. _no-23525:

.. function:: dabo.ui.uiwx.dEditor.dEditor.goNextBookMark(self, line=None)

   
   Moves to the next bookmark in the document. If the
   line to start searching from is not specified, searches from
   the current line. If there are no more bookmarks, nothing
   happens.
   



-------

.. _no-23526:

.. function:: dabo.ui.uiwx.dEditor.dEditor.goPrevBookMark(self, line=None)

   
   Moves to the previous bookmark in the document. If the
   line to start searching from is not specified, searches from
   the current line. If there are no more bookmarks, nothing
   happens.
   



-------

.. _no-23528:

.. function:: dabo.ui.uiwx.dEditor.dEditor.hiliteLine(self, lineNum, extend=False)

   
   Selects the specified line. If the line number does not exist,
   a ValueError is raised.
   



-------

.. _no-23529:

.. function:: dabo.ui.uiwx.dEditor.dEditor.increaseTextSize(self, pts=1)



-------

.. _no-23532:

.. function:: dabo.ui.uiwx.dEditor.dEditor.isChanged(self)



-------

.. _no-23538:

.. function:: dabo.ui.uiwx.dEditor.dEditor.moveToBeginning(self)



-------

.. _no-23539:

.. function:: dabo.ui.uiwx.dEditor.dEditor.moveToEnd(self)



-------

.. _no-23540:

.. function:: dabo.ui.uiwx.dEditor.dEditor.newFile(self)

   Create a new file and edit it.



-------

.. _no-23542:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onCommentLine(self, evt)



-------

.. _no-23544:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onIdle(self, evt)



-------

.. _no-23545:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onListSelection(self, evt)



-------

.. _no-23546:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onPrint(self, evt=None)



-------

.. _no-23547:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onPrintPreview(self)



-------

.. _no-23548:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onPrintSetup(self)



-------

.. _no-23549:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onUncommentLine(self, evt)



-------

.. _no-23550:

.. function:: dabo.ui.uiwx.dEditor.dEditor.openFile(self, fileSpec=None, checkChanges=True)

   Open a new file and edit it.



-------

.. _no-23553:

.. function:: dabo.ui.uiwx.dEditor.dEditor.processBookmarkClick(self, lineNumber, bookmarkName)

   Stub function to process a left click on the bookmark margin area.



-------

.. _no-23556:

.. function:: dabo.ui.uiwx.dEditor.dEditor.promptForFileName(self, prompt=None, saveAs=False, path=None, \**kwargs)

   Prompt the user for a file name.



-------

.. _no-23557:

.. function:: dabo.ui.uiwx.dEditor.dEditor.promptForSaveAs(self)

   
   Prompt user for the filename to save the file as.
   
   If the file exists, confirm with the user that they really want to
   overwrite.
   



-------

.. _no-23558:

.. function:: dabo.ui.uiwx.dEditor.dEditor.promptToSave(self)



-------

.. _no-23567:

.. function:: dabo.ui.uiwx.dEditor.dEditor.restoreTextSize(self)



-------

.. _no-23569:

.. function:: dabo.ui.uiwx.dEditor.dEditor.saveFile(self, fname=None, force=False, isTmp=False)



-------

.. _no-23571:

.. function:: dabo.ui.uiwx.dEditor.dEditor.select(self, position, length)

   Select all text from <position> for <length> or end of string.



-------

.. _no-23573:

.. function:: dabo.ui.uiwx.dEditor.dEditor.selectLine(self)



-------

.. _no-23575:

.. function:: dabo.ui.uiwx.dEditor.dEditor.selectWord(self)



-------

.. _no-23578:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setBookmark(self, nm, line=None)

   
   Creates a bookmark that can be referenced by the
   identifying name that is passed. If a bookmark already
   exists for that name, the old one is deleted. The
   bookmark is set on the current line unless a specific
   line number is passed.
   



-------

.. _no-23579:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setDefaultFont(self, fontFace, fontSize)



-------

.. _no-23580:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setDefaults(self)



-------

.. _no-23581:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setDocumentDefaults(self)



-------

.. _no-23583:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setFormCallbacks(self, funcTuple)



-------

.. _no-23584:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setInactive(self)

   Hides the auto-completion popup if one is open.



-------

.. _no-23588:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setPyFont(self, fontFace, fontSize)



-------

.. _no-23591:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setSyntaxColoring(self, color=None)

   Sets the appropriate lexer for syntax coloring.



-------

.. _no-23592:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setTitle(self)

   Set the title of the editor



-------

.. _no-23596:

.. function:: dabo.ui.uiwx.dEditor.dEditor.showCurrentLine(self)

   Scrolls the editor so that the current position is visible.



-------


Methods - inherited
=====================

.. _no-23453:

.. function:: dabo.ui.uiwx.dEditor.dEditor.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23454:

.. function:: dabo.ui.uiwx.dEditor.dEditor.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-23455:

.. function:: dabo.ui.uiwx.dEditor.dEditor.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23456:

.. function:: dabo.ui.uiwx.dEditor.dEditor.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23457:

.. function:: dabo.ui.uiwx.dEditor.dEditor.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23458:

.. function:: dabo.ui.uiwx.dEditor.dEditor.autoBindEvents(self, force=True)
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

.. _no-23460:

.. function:: dabo.ui.uiwx.dEditor.dEditor.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23461:

.. function:: dabo.ui.uiwx.dEditor.dEditor.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23462:

.. function:: dabo.ui.uiwx.dEditor.dEditor.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23463:

.. function:: dabo.ui.uiwx.dEditor.dEditor.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23464:

.. function:: dabo.ui.uiwx.dEditor.dEditor.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-23465:

.. function:: dabo.ui.uiwx.dEditor.dEditor.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23472:

.. function:: dabo.ui.uiwx.dEditor.dEditor.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23475:

.. function:: dabo.ui.uiwx.dEditor.dEditor.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23477:

.. function:: dabo.ui.uiwx.dEditor.dEditor.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23478:

.. function:: dabo.ui.uiwx.dEditor.dEditor.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23479:

.. function:: dabo.ui.uiwx.dEditor.dEditor.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23481:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23482:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23483:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-23484:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23485:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23486:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23487:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23488:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23489:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23490:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23491:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23492:

.. function:: dabo.ui.uiwx.dEditor.dEditor.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23493:

.. function:: dabo.ui.uiwx.dEditor.dEditor.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23496:

.. function:: dabo.ui.uiwx.dEditor.dEditor.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23497:

.. function:: dabo.ui.uiwx.dEditor.dEditor.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23498:

.. function:: dabo.ui.uiwx.dEditor.dEditor.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23499:

.. function:: dabo.ui.uiwx.dEditor.dEditor.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23500:

.. function:: dabo.ui.uiwx.dEditor.dEditor.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23501:

.. function:: dabo.ui.uiwx.dEditor.dEditor.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23502:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23503:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getBlankValue(self)
   :noindex:


   Return the empty value of the control.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23506:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23507:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23509:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23514:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23517:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23518:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-23519:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23520:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23521:

.. function:: dabo.ui.uiwx.dEditor.dEditor.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23527:

.. function:: dabo.ui.uiwx.dEditor.dEditor.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23530:

.. function:: dabo.ui.uiwx.dEditor.dEditor.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23531:

.. function:: dabo.ui.uiwx.dEditor.dEditor.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23533:

.. function:: dabo.ui.uiwx.dEditor.dEditor.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23534:

.. function:: dabo.ui.uiwx.dEditor.dEditor.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23535:

.. function:: dabo.ui.uiwx.dEditor.dEditor.lockDisplay(self)
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

.. _no-23536:

.. function:: dabo.ui.uiwx.dEditor.dEditor.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23537:

.. function:: dabo.ui.uiwx.dEditor.dEditor.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23541:

.. function:: dabo.ui.uiwx.dEditor.dEditor.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23543:

.. function:: dabo.ui.uiwx.dEditor.dEditor.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23551:

.. function:: dabo.ui.uiwx.dEditor.dEditor.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23552:

.. function:: dabo.ui.uiwx.dEditor.dEditor.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23554:

.. function:: dabo.ui.uiwx.dEditor.dEditor.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23555:

.. function:: dabo.ui.uiwx.dEditor.dEditor.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23559:

.. function:: dabo.ui.uiwx.dEditor.dEditor.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23560:

.. function:: dabo.ui.uiwx.dEditor.dEditor.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23561:

.. function:: dabo.ui.uiwx.dEditor.dEditor.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23562:

.. function:: dabo.ui.uiwx.dEditor.dEditor.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23563:

.. function:: dabo.ui.uiwx.dEditor.dEditor.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23564:

.. function:: dabo.ui.uiwx.dEditor.dEditor.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23565:

.. function:: dabo.ui.uiwx.dEditor.dEditor.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23566:

.. function:: dabo.ui.uiwx.dEditor.dEditor.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23568:

.. function:: dabo.ui.uiwx.dEditor.dEditor.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23570:

.. function:: dabo.ui.uiwx.dEditor.dEditor.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-23572:

.. function:: dabo.ui.uiwx.dEditor.dEditor.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-23574:

.. function:: dabo.ui.uiwx.dEditor.dEditor.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-23576:

.. function:: dabo.ui.uiwx.dEditor.dEditor.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23577:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-23582:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23585:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23586:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-23587:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-23589:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23590:

.. function:: dabo.ui.uiwx.dEditor.dEditor.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23593:

.. function:: dabo.ui.uiwx.dEditor.dEditor.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23594:

.. function:: dabo.ui.uiwx.dEditor.dEditor.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23595:

.. function:: dabo.ui.uiwx.dEditor.dEditor.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23597:

.. function:: dabo.ui.uiwx.dEditor.dEditor.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23598:

.. function:: dabo.ui.uiwx.dEditor.dEditor.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23599:

.. function:: dabo.ui.uiwx.dEditor.dEditor.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23600:

.. function:: dabo.ui.uiwx.dEditor.dEditor.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23601:

.. function:: dabo.ui.uiwx.dEditor.dEditor.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23602:

.. function:: dabo.ui.uiwx.dEditor.dEditor.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
