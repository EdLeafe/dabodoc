
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSearchBox

.. _dabo.ui.uiwx.dSearchBox.dSearchBox:

==============================================
|doc_title|  **dSearchBox.dSearchBox** - class
==============================================

Creates a text box for editing one line of string data.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSearchBox**

.. inheritance-diagram:: dSearchBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dSearchBox.png
          :scale: 75 %
          :target: _static/winWidgets/dSearchBox.png
          :alt: dSearchBox



     - .. image:: _static/nixWidgets/dSearchBox.png
          :scale: 75 %
          :target: _static/nixWidgets/dSearchBox.png
          :alt: dSearchBox


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSearchBox.dSearchBox

   .. automethod:: dabo.ui.uiwx.dSearchBox.dSearchBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-28423>`                Specifies the alignment of the text. (str)
:ref:`Application <no-28424>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-28425>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-28426>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-28427>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-28428>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-28429>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-28430>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-28431>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-28432>`                   The position of the bottom side of the object. This is a
:ref:`CancelButtonVisible <no-28433>`      Tells whether or not the cancel button is visible (bool)
:ref:`Caption <no-28434>`                  The caption of the object. (str)
:ref:`Children <no-28435>`                 Returns a list of object references to the children of
:ref:`Class <no-28436>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-28437>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-28438>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-28439>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-28440>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-28441>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-28442>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-28443>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-28444>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-28445>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-28446>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-28447>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-28448>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-28449>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-28450>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-28451>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-28452>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-28453>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-28454>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-28455>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-28456>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-28457>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-28458>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-28459>`            Dynamically determine the value of the Height property.
:ref:`DynamicInsertionPosition <no-28460>` Dynamically determine the value of the InsertionPosition property.
:ref:`DynamicLeft <no-28461>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-28462>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPasswordEntry <no-28463>`     Dynamically determine the value of the PasswordEntry property.
:ref:`DynamicPosition <no-28464>`          Dynamically determine the value of the Position property.
:ref:`DynamicReadOnly <no-28465>`          Dynamically determine the value of the ReadOnly property.
:ref:`DynamicSelectOnEntry <no-28466>`     Dynamically determine the value of the SelectOnEntry property.
:ref:`DynamicSelectionEnd <no-28467>`      Dynamically determine the value of the SelectionEnd property.
:ref:`DynamicSelectionLength <no-28468>`   Dynamically determine the value of the SelectionLength property.
:ref:`DynamicSelectionStart <no-28469>`    Dynamically determine the value of the SelectionStart property.
:ref:`DynamicSize <no-28470>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-28471>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicStrictDateEntry <no-28472>`   Dynamically determine the value of the StrictDateEntry property.
:ref:`DynamicTag <no-28473>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-28474>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-28475>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-28476>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-28477>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-28478>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-28479>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-28480>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-28481>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-28482>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-28483>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-28484>`                 Specifies the font face. (str)
:ref:`FontInfo <no-28485>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-28486>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-28487>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-28488>`            Specifies whether text is underlined. (bool)
:ref:`ForceCase <no-28489>`                Determines if we change the case of entered text. Possible values are:
:ref:`ForeColor <no-28490>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-28491>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-28492>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-28493>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-28494>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`InsertionPosition <no-28495>`        Position of the insertion point within the control  (int)
:ref:`IsSecret <no-28496>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-28497>`                     Specifies the left position of the object. (int)
:ref:`List <no-28498>`                     A dropdown list that appears right below the search button (list)
:ref:`LogEvents <no-28499>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-28500>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-28501>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-28502>`             Maximum allowable width for the control in pixels.  (int)
:ref:`Menu <no-28503>`                     Menu used to display the controls.  Generated by List (dMenu)
:ref:`MinimumHeight <no-28504>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-28505>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-28506>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-28507>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-28508>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-28509>`                 Specifies the base name of the object.
:ref:`NoneDisplay <no-28510>`              Specifies the string displayed if Value is None  (str or None)
:ref:`NumericBlankToZero <no-28511>`       Specifies whether a blank textbox gets interpreted as 0.
:ref:`Parent <no-28512>`                   The containing object. (obj)
:ref:`PasswordEntry <no-28513>`            Specifies whether plain-text or asterisks are echoed. (bool)
:ref:`PersistSecretData <no-28514>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-28515>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-28516>`        Reference to the Preference Management object  (dPref)
:ref:`ReadOnly <no-28517>`                 Specifies whether or not the text can be edited. (bool)
:ref:`RegID <no-28518>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-28519>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-28520>`         Specifies whether the Value of the control gets saved when
:ref:`SearchButtonVisible <no-28521>`      Tells whether or not the search button is visible (bool)
:ref:`SelectOnEntry <no-28522>`            Specifies whether all text gets selected upon receiving focus. (bool)
:ref:`SelectedText <no-28523>`             Currently selected text. Returns the empty string if nothing is selected  (str)
:ref:`SelectionEnd <no-28524>`             Position of the end of the selected text. If no text is
:ref:`SelectionLength <no-28525>`          Length of the selected text, or 0 if nothing is selected.  (int)
:ref:`SelectionStart <no-28526>`           Position of the beginning of the selected text. If no text is
:ref:`Size <no-28527>`                     The size of the object. (tuple)
:ref:`Sizer <no-28528>`                    The sizer for the object.
:ref:`Source <no-28529>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-28530>`               Specifies the text that displays in the form's status bar, if any.
:ref:`StrictDateEntry <no-28531>`          Specifies whether date values must be entered in strict ISO8601 format. Default=False.
:ref:`StrictNumericEntry <no-28532>`       When True, the DataType will be preserved across numeric types. When False, the
:ref:`TabStop <no-28533>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-28534>`                      A property that user code can safely use for specific purposes.
:ref:`TextLength <no-28535>`               The maximum length the entered text can be. (int)
:ref:`ToolTipText <no-28536>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-28537>`                      The top position of the object. (int)
:ref:`Transparency <no-28538>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-28539>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-28540>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-28541>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-28542>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-28543>`                    The width of the object. (int)
:ref:`WindowHandle <no-28544>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-28498:

**List** 

A dropdown list that appears right below the search button (list)



-------


Properties - inherited
========================

.. _no-28423:

**Alignment** 

Specifies the alignment of the text. (str)
       Left (default)
       Center
       Right


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-28424:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28425:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28426:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28427:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28428:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28429:

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

.. _no-28430:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28431:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28432:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28433:

**CancelButtonVisible** 

Tells whether or not the cancel button is visible (bool)


Inherited from: 'wx._controls.SearchCtrl - can not provide a link

-------

.. _no-28434:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28435:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28436:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28437:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28438:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28439:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28440:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28441:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28442:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28443:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28444:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28445:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28446:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28447:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28448:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28449:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28450:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28451:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28452:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28453:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28454:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28455:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28456:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28457:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28458:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28459:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28460:

**DynamicInsertionPosition** 

Dynamically determine the value of the InsertionPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
InsertionPosition property. If DynamicInsertionPosition is set to None (the default), InsertionPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28461:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28462:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28463:

**DynamicPasswordEntry** 

Dynamically determine the value of the PasswordEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PasswordEntry property. If DynamicPasswordEntry is set to None (the default), PasswordEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28464:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28465:

**DynamicReadOnly** 

Dynamically determine the value of the ReadOnly property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ReadOnly property. If DynamicReadOnly is set to None (the default), ReadOnly
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28466:

**DynamicSelectOnEntry** 

Dynamically determine the value of the SelectOnEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectOnEntry property. If DynamicSelectOnEntry is set to None (the default), SelectOnEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28467:

**DynamicSelectionEnd** 

Dynamically determine the value of the SelectionEnd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionEnd property. If DynamicSelectionEnd is set to None (the default), SelectionEnd
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28468:

**DynamicSelectionLength** 

Dynamically determine the value of the SelectionLength property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionLength property. If DynamicSelectionLength is set to None (the default), SelectionLength
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28469:

**DynamicSelectionStart** 

Dynamically determine the value of the SelectionStart property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectionStart property. If DynamicSelectionStart is set to None (the default), SelectionStart
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28470:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28471:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28472:

**DynamicStrictDateEntry** 

Dynamically determine the value of the StrictDateEntry property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StrictDateEntry property. If DynamicStrictDateEntry is set to None (the default), StrictDateEntry
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28473:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28474:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28475:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28476:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28477:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-28478:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28479:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28480:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28481:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28482:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28483:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28484:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28485:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28486:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28487:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28488:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28489:

**ForceCase** 

Determines if we change the case of entered text. Possible values are:

        ===========  =====================
        None or ""   No changes made (default)
        "Upper"      FORCE TO UPPER CASE
        "Lower"      Force to lower case
        "Title"      Force To Title Case
        ===========  =====================

    These can be abbreviated to "u", "l" or "t"  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28490:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28491:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28492:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28493:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28494:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28495:

**InsertionPosition** 

Position of the insertion point within the control  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28496:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28497:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28499:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28500:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28501:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28502:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28503:

**Menu** 

Menu used to display the controls.  Generated by List (dMenu)


Inherited from: 'wx._controls.SearchCtrl - can not provide a link

-------

.. _no-28504:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28505:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28506:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28507:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28508:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28509:

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

.. _no-28510:

**NoneDisplay** 

Specifies the string displayed if Value is None  (str or None)

        If None, self.Application.NoneDisplay will be used.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28511:

**NumericBlankToZero** 

Specifies whether a blank textbox gets interpreted as 0.

    When True, if the user clears the textbox value, such as by selecting all
    and pressing the space bar or delete, the value will become 0 when the
    control loses focus.

    When False, the value will revert back to the last numeric value when the
    control loses focus.

    The default comes from dabo.dTextBox_NumericBlankToZero, which defaults to
    False.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28512:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28513:

**PasswordEntry** 

Specifies whether plain-text or asterisks are echoed. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28514:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28515:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28516:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28517:

**ReadOnly** 

Specifies whether or not the text can be edited. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28518:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28519:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28520:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28521:

**SearchButtonVisible** 

Tells whether or not the search button is visible (bool)


Inherited from: 'wx._controls.SearchCtrl - can not provide a link

-------

.. _no-28522:

**SelectOnEntry** 

Specifies whether all text gets selected upon receiving focus. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28523:

**SelectedText** 

Currently selected text. Returns the empty string if nothing is selected  (str)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28524:

**SelectionEnd** 

Position of the end of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28525:

**SelectionLength** 

Length of the selected text, or 0 if nothing is selected.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28526:

**SelectionStart** 

Position of the beginning of the selected text. If no text is
    selected, returns the Position of the insertion cursor.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28527:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28528:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28529:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28530:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28531:

**StrictDateEntry** 

Specifies whether date values must be entered in strict ISO8601 format. Default=False.

    If not strict, dates can be accepted in YYYYMMDD, YYMMDD, and MMDD format,
    which will be coerced into sensible date values automatically.


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28532:

**StrictNumericEntry** 

When True, the DataType will be preserved across numeric types. When False, the
    DataType will respond to user input to convert to the 'obvious' numeric type.
    Default=True. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28533:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-28534:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28535:

**TextLength** 

The maximum length the entered text can be. (int)


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28536:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28537:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28538:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28539:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28540:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------

.. _no-28541:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28542:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28543:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28544:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


=========================================== ========================
:ref:`BackgroundErased <no-28545>`          Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-28546>`                    Occurs after the control or form is created.
:ref:`Destroy <no-28547>`                   Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-28548>`     Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-28549>`                  Occurs when the control gets the focus.
:ref:`Idle <no-28550>`                      Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-28551>`         Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-28552>`                   Occurs when a key is depressed and released on the
:ref:`KeyDown <no-28553>`                   Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-28554>`                  
:ref:`KeyUp <no-28555>`                     Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-28556>`                 Occurs when the control loses the focus.
:ref:`MenuClose <no-28557>`                 Occurs when a menu has just been closed.
:ref:`MenuOpen <no-28558>`                  Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-28559>`                Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-28560>`                
:ref:`MouseLeave <no-28561>`                Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-28562>`            Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-28563>`      Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-28564>`             Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-28565>`               Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-28566>`          Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-28567>`    Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-28568>`           Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-28569>`             Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-28570>`                 Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-28571>`           Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-28572>`     Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-28573>`            Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-28574>`              Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-28575>`                Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-28576>`                      Occurs when the control's position changes.
:ref:`Paint <no-28577>`                     Occurs when it is time to paint the control.
:ref:`Resize <no-28578>`                    Occurs when the control or form is resized.
:ref:`SearchButtonClicked <no-28579>`       Occurs when the user clicks the search button in a dSearchBox.
:ref:`SearchCancelButtonClicked <no-28580>` Occurs when the user clicks the cancel button in a dSearchBox.
:ref:`TreeBeginDrag <no-28581>`             Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-28582>`               Occurs when a drag operation ends in a tree.
:ref:`Update <no-28583>`                    Occurs when a container wants its controls to update
:ref:`ValueChanged <no-28584>`              Occurs when the control's value has changed, whether

=========================================== ========================


Events
=======

.. _no-28545:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-28546:

**Create** 

Occurs after the control or form is created.



-------

.. _no-28547:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-28548:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-28549:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-28550:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-28551:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-28552:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-28553:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-28554:

**KeyEvent** 



-------

.. _no-28555:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-28556:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-28557:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-28558:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-28559:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-28560:

**MouseEvent** 



-------

.. _no-28561:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-28562:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-28563:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-28564:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-28565:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-28566:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-28567:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-28568:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-28569:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-28570:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-28571:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-28572:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-28573:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-28574:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-28575:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-28576:

**Move** 

Occurs when the control's position changes.



-------

.. _no-28577:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-28578:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-28579:

**SearchButtonClicked** 

Occurs when the user clicks the search button in a dSearchBox.



-------

.. _no-28580:

**SearchCancelButtonClicked** 

Occurs when the user clicks the cancel button in a dSearchBox.



-------

.. _no-28581:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-28582:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-28583:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-28584:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


============================================== ========================
:ref:`absoluteCoordinates <no-28585>`          Translates a position value for a control to absolute screen position.
:ref:`addObject <no-28586>`                    Instantiate object as a child of self.
:ref:`afterInit <no-28587>`                    Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-28588>`                 
:ref:`afterSetProperties <no-28589>`           
:ref:`autoBindEvents <no-28590>`               Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-28591>`                   Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-28592>`          
:ref:`bindEvent <no-28593>`                    Bind a dEvent to a callback function.
:ref:`bindEvents <no-28594>`                   Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-28595>`                      Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-28596>`                 Makes this object topmost
:ref:`charsAfterCursor <no-28597>`             Returns the characters immediately after the current InsertionPoint,
:ref:`charsBeforeCursor <no-28598>`            Returns the characters immediately before the current InsertionPoint,
:ref:`clear <no-28599>`                        Clears the background of custom-drawn objects.
:ref:`clone <no-28600>`                        Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-28601>`         Given a position relative to this control, return a position relative
:ref:`convertStringValueToDataType <no-28602>` Given a string value and a type, return an appropriate value of that type.
:ref:`copy <no-28603>`                         Called by uiApp when the user requests a copy operation.
:ref:`cut <no-28604>`                          Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-28605>`                      Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-28606>`                   Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-28607>`                   Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-28608>`                  Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-28609>`              Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-28610>`                 Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-28611>`                     Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-28612>`                Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-28613>`                  Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-28614>`                Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-28615>`         Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-28616>`                     Draws text on the object at the specified position
:ref:`endHover <no-28617>`                     
:ref:`fitToSizer <no-28618>`                   Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-28619>`                   
:ref:`fontZoomIn <no-28620>`                   Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-28621>`               Reset the font zoom back to zero.
:ref:`fontZoomOut <no-28622>`                  Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-28623>`              Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-28624>`              Return the fully qualified name of the object.
:ref:`getBlankValue <no-28625>`                
:ref:`getCaptureBitmap <no-28626>`             Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-28627>`            Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-28628>`             Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-28629>`             Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-28630>`           Convenience method to let you call this directly on the object.
:ref:`getProperties <no-28631>`                Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-28632>`             
:ref:`getSizerProp <no-28633>`                 Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-28634>`                Returns a dict containing the object's sizer property info. The
:ref:`getStringValue <no-28635>`               Given a value of any data type, return a string rendition.
:ref:`hide <no-28636>`                         Make the object invisible.
:ref:`initEvents <no-28637>`                   Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-28638>`               Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-28639>`                Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-28640>`                  Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-28641>`                  Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-28642>`            Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-28643>`           Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-28644>`            Given a position relative to the form, return a position relative
:ref:`onHover <no-28645>`                      
:ref:`paste <no-28646>`                        Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-28647>`                  
:ref:`processDroppedFiles <no-28648>`          Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-28649>`           Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-28650>`                   Raise the passed Dabo event.
:ref:`reCreate <no-28651>`                     Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-28652>`                     Recreate the object.
:ref:`redraw <no-28653>`                       Called when the object is (re)drawn.
:ref:`refresh <no-28654>`                      Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-28655>`          Translates an absolute screen position to position value for a control.
:ref:`release <no-28656>`                      Destroys the object.
:ref:`removeDrawnObject <no-28657>`            
:ref:`restoreValue <no-28658>`                 Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-28659>`                    Save control's value to dApp's user settings table.
:ref:`select <no-28660>`                       Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-28661>`                    Each subclass must define their own selectAll method. This will
:ref:`selectNone <no-28662>`                   Select no text in the control.
:ref:`sendToBack <no-28663>`                   Places this object behind all others.
:ref:`setAll <no-28664>`                       Set all child object properties to the passed value.
:ref:`setFocus <no-28665>`                     Sets focus to the object.
:ref:`setPositionInSizer <no-28666>`           Convenience method to let you call this directly on the object.
:ref:`setProperties <no-28667>`                Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-28668>`        Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-28669>`                 Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-28670>`                Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-28671>`                         Make the object visible.
:ref:`showContainingPage <no-28672>`           If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-28673>`              Display a context menu (popup) at the specified position.
:ref:`super <no-28674>`                        This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-28675>`                  Remove a previously registered event binding.
:ref:`unbindKey <no-28676>`                    Unbind a previously bound key combination.
:ref:`unlockDisplay <no-28677>`                Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-28678>`             Immediately unlocks the display, no matter how many previous
:ref:`update <no-28679>`                       Update control's value to match the current value from the source.
:ref:`write <no-28680>`                        write(self, String text)

============================================== ========================


Methods - inherited
=====================

.. _no-28585:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28586:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-28587:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28588:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28589:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28590:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.autoBindEvents(self, force=True)
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

.. _no-28591:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28592:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28593:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28594:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28595:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-28596:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28597:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.charsAfterCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately after the current InsertionPoint,
   or, if there is selected text, before the end of the current selection.
   By default, it will return one character, but you can specify a greater
   number to be returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28598:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.charsBeforeCursor(self, num=None, includeSelectedText=False)
   :noindex:


   
   Returns the characters immediately before the current InsertionPoint,
   or, if there is selected text, before the beginning of the current
   selection. By default, it will return one character, but you can specify
   a greater number to be returned. If there is selected text, and
   includeSelectedText is True, this will return the string consisting of
   the characters before plus the selected text.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28599:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28600:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28601:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28602:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.convertStringValueToDataType(self, strVal, dataType)
   :noindex:


   
   Given a string value and a type, return an appropriate value of that type.
   If the value can't be converted, a ValueError will be raised.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28603:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28604:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28605:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28606:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28607:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-28608:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28609:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28610:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28611:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28612:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28613:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28614:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28615:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28616:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28617:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28618:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28619:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.flushValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28620:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28621:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28622:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28623:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28624:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28625:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getBlankValue(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28626:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28627:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28628:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28629:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28630:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28631:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-28632:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28633:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28634:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28635:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.getStringValue(self, value)
   :noindex:


   
   Given a value of any data type, return a string rendition.
   
   Used internally by _setValue and flushValue, but also exposed to subclasses
   in case they need specialized behavior. The value returned from this
   function will be what is displayed in the UI textbox.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixin`

-------

.. _no-28636:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28637:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28638:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28639:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28640:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28641:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.lockDisplay(self)
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

.. _no-28642:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28643:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28644:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28645:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28646:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28647:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28648:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28649:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28650:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28651:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28652:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28653:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28654:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28655:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28656:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28657:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28658:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28659:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28660:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-28661:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.selectAll(self)
   :noindex:


   
   Each subclass must define their own selectAll method. This will
   be called if SelectOnEntry is True when the control gets focus.
   


Inherited from: :ref:`dabo.ui.uiwx.dTextBoxMixin.dTextBoxMixinBase`

-------

.. _no-28662:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-28663:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28664:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-28665:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28666:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28667:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-28668:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-28669:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28670:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28671:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28672:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28673:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28674:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28675:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28676:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28677:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28678:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28679:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28680:

.. function:: dabo.ui.uiwx.dSearchBox.dSearchBox.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
