
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDialog

.. _dabo.ui.uiwx.dDialog.dYesNoDialog:

=============================================
|doc_title|  **dDialog.dYesNoDialog** - class
=============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dYesNoDialog**

.. inheritance-diagram:: dYesNoDialog


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dYesNoDialog.png
          :scale: 75 %
          :target: _static/macWidgets/dYesNoDialog.png
          :alt: dYesNoDialog



     - no image available



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDialog.dYesNoDialog

   .. automethod:: dabo.ui.uiwx.dDialog.dYesNoDialog.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`Accepted <no-15332>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-15333>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-15334>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-15335>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-15336>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-15337>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-15338>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-15339>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-15340>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-15341>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-15342>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-15343>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-15344>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-15345>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-15346>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-15347>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-15348>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-15349>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-15350>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-15351>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-15352>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-15353>`                    Returns a list of object references to the children of
:ref:`Class <no-15354>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-15355>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-15356>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-15357>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-15358>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-15359>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-15360>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-15361>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-15362>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-15363>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-15364>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-15365>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-15366>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-15367>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-15368>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-15369>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-15370>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-15371>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-15372>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-15373>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-15374>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-15375>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-15376>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-15377>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-15378>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-15379>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-15380>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-15381>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-15382>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-15383>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-15384>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-15385>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-15386>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-15387>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-15388>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-15389>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-15390>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-15391>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-15392>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-15393>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-15394>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-15395>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-15396>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-15397>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-15398>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-15399>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-15400>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-15401>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-15402>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-15403>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-15404>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-15405>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-15406>`                    Specifies the font face. (str)
:ref:`FontInfo <no-15407>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-15408>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-15409>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-15410>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-15411>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-15412>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-15413>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-15414>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-15415>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-15416>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-15417>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-15418>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-15419>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-15420>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-15421>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-15422>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-15423>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-15424>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-15425>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-15426>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-15427>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-15428>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-15429>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-15430>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-15431>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-15432>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-15433>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-15434>`                    Specifies the base name of the object.
:ref:`NoButton <no-15435>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-15436>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-15437>`                      The containing object. (obj)
:ref:`Position <no-15438>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-15439>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-15440>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-15441>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-15442>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-15443>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-15444>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-15445>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-15446>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-15447>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-15448>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-15449>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-15450>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-15451>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-15452>`                        The size of the object. (tuple)
:ref:`Sizer <no-15453>`                       The sizer for the object.
:ref:`SizersToOutline <no-15454>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-15455>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-15456>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-15457>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-15458>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-15459>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-15460>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-15461>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-15462>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-15463>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-15464>`                         The top position of the object. (int)
:ref:`Transparency <no-15465>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-15466>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-15467>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-15468>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-15469>`                       The width of the object. (int)
:ref:`WindowHandle <no-15470>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-15471>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-15472>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================= ========================


Properties - inherited
========================

.. _no-15332:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15333:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15334:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15335:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15336:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15337:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15338:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15339:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15340:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15341:

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

.. _no-15342:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15343:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15344:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15345:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15346:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15347:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15348:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15349:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15350:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15351:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15352:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15353:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15354:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15355:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15356:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15357:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15358:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15359:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15360:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15361:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15362:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15363:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15364:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15365:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15366:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15367:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15368:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15369:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15370:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15371:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15372:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15373:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15374:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15375:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15376:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15377:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15378:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15379:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15380:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15381:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15382:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15383:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15384:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15385:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15386:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15387:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15388:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15389:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15390:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15391:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15392:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15393:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15394:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15395:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15396:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15397:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15398:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15399:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15400:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15401:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15402:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15403:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15404:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15405:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15406:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15407:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15408:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15409:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15410:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15411:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15412:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15413:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15414:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15415:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15416:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15417:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-15418:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15419:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15420:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15421:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15422:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15423:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15424:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15425:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15426:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15427:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15428:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15429:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15430:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15431:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15432:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15433:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15434:

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

.. _no-15435:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15436:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15437:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15438:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15439:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15440:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15441:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15442:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15443:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15444:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15445:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15446:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15447:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15448:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15449:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15450:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15451:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15452:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15453:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15454:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15455:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15456:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15457:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15458:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15459:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15460:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15461:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15462:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15463:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15464:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15465:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15466:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15467:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15468:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15469:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15470:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15471:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15472:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`Activate <no-15473>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-15474>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-15475>`              Occurs when a child control is created.
:ref:`Close <no-15476>`                  Occurs when the user closes the form.
:ref:`Create <no-15477>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-15478>`             Occurs when another form becomes active.
:ref:`Destroy <no-15479>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-15480>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-15481>`               Occurs when the control gets the focus.
:ref:`Idle <no-15482>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-15483>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-15484>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-15485>`               
:ref:`KeyUp <no-15486>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-15487>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-15488>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-15489>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-15490>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-15491>`             
:ref:`MouseLeave <no-15492>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-15493>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-15494>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-15495>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-15496>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-15497>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-15498>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-15499>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-15500>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-15501>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-15502>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-15503>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-15504>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-15505>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-15506>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-15507>`                   Occurs when the control's position changes.
:ref:`Paint <no-15508>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-15509>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-15510>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-15511>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-15512>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-15473:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-15474:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-15475:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-15476:

**Close** 

Occurs when the user closes the form.



-------

.. _no-15477:

**Create** 

Occurs after the control or form is created.



-------

.. _no-15478:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-15479:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-15480:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-15481:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-15482:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-15483:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-15484:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-15485:

**KeyEvent** 



-------

.. _no-15486:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-15487:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-15488:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-15489:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-15490:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-15491:

**MouseEvent** 



-------

.. _no-15492:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-15493:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-15494:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-15495:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-15496:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-15497:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-15498:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-15499:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-15500:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-15501:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-15502:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-15503:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-15504:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-15505:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-15506:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-15507:

**Move** 

Occurs when the control's position changes.



-------

.. _no-15508:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-15509:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-15510:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-15511:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-15512:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-15513>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-15514>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControlSequence <no-15515>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-15516>`                    Use this method to add controls to the dialog. The standard buttons will be added
:ref:`addObject <no-15517>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-15518>`            
:ref:`afterAddControls <no-15519>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-15520>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-15521>`                   
:ref:`afterSetMenuBar <no-15522>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-15523>`             
:ref:`appendToolBarButton <no-15524>`            
:ref:`autoBindEvents <no-15525>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-15526>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-15527>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-15528>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-15529>`            
:ref:`bindEvent <no-15530>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-15531>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-15532>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-15533>`                   Makes this object topmost
:ref:`clear <no-15534>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-15535>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-15536>`                          This method will close the form. If force = False (default)
:ref:`closing <no-15537>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-15538>`           Given a position relative to this control, return a position relative
:ref:`copy <no-15539>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-15540>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-15541>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-15542>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-15543>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-15544>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-15545>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-15546>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-15547>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-15548>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-15549>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-15550>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-15551>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-15552>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-15553>`                       Draws text on the object at the specified position
:ref:`endHover <no-15554>`                       
:ref:`fillPreferenceDialog <no-15555>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-15556>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-15557>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-15558>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-15559>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-15560>`              
:ref:`formCoordinates <no-15561>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-15562>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-15563>`                      
:ref:`getCaptureBitmap <no-15564>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-15565>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-15566>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-15567>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-15568>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-15569>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-15570>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-15571>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-15572>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-15573>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-15574>`                           Make the object invisible.
:ref:`initEvents <no-15575>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-15576>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-15577>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-15578>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-15579>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-15580>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-15581>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-15582>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-15583>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-15584>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-15585>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-15586>`                        
:ref:`paste <no-15587>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-15588>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-15589>`                    
:ref:`processDroppedFiles <no-15590>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-15591>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-15592>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-15593>`                     Raise the passed Dabo event.
:ref:`reCreate <no-15594>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-15595>`                       Recreate the object.
:ref:`redraw <no-15596>`                         Called when the object is (re)drawn.
:ref:`refresh <no-15597>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-15598>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-15599>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-15600>`                        Need to augment this to make sure the dialog
:ref:`reload <no-15601>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-15602>`              
:ref:`removeFromOutlinedSizers <no-15603>`       
:ref:`restoreSizeAndPosition <no-15604>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-15605>` 
:ref:`runCancel <no-15606>`                      
:ref:`runHelp <no-15607>`                        
:ref:`runNo <no-15608>`                          
:ref:`runOK <no-15609>`                          
:ref:`runYes <no-15610>`                         
:ref:`safeDestroy <no-15611>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-15612>`            Save the current size and position of this form.
:ref:`sendToBack <no-15613>`                     Places this object behind all others.
:ref:`setAll <no-15614>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-15615>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-15616>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-15617>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-15618>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-15619>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-15620>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-15621>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-15622>`                  Set the status text to val.
:ref:`show <no-15623>`                           
:ref:`showContainingPage <no-15624>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-15625>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-15626>`                      Show the dialog modally.
:ref:`showModeless <no-15627>`                   Show the dialog non-modally.
:ref:`super <no-15628>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-15629>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-15630>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-15631>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-15632>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-15633>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods - inherited
=====================

.. _no-15513:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15514:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15515:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.addControlSequence(self, seq)
   :noindex:


   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15516:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.addControls(self)
   :noindex:


   
   Use this method to add controls to the dialog. The standard buttons will be added
   after this method runs, so that they appear at the bottom of the dialog.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15517:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-15518:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15519:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15520:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15521:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15522:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15523:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15524:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15525:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.autoBindEvents(self, force=True)
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

.. _no-15526:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15527:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15528:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15529:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15530:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15531:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15532:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-15533:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15534:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15535:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15536:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15537:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15538:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15539:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15540:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15541:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15542:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15543:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15544:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-15545:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15546:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15547:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15548:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15549:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15550:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15551:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15552:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15553:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15554:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15555:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15556:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15557:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15558:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15559:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15560:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15561:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15562:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15563:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15564:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15565:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15566:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15567:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15568:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15569:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15570:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15571:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-15572:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15573:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15574:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15575:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15576:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15577:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15578:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15579:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15580:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.lockDisplay(self)
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

.. _no-15581:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15582:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15583:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15584:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15585:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15586:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15587:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15588:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15589:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15590:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15591:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15592:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15593:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15594:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15595:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15596:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15597:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.refresh(self, interval=None)
   :noindex:


   
   Repaints the form and all contained objects.
   
   This method is called repeatedly from many different places during
   a single change in the UI, so by default the actual execution is cached
   using callAfterInterval(). The default interval is 100 milliseconds. You
   can change that to suit your app needs by passing a different interval
   in milliseconds.
   
   Sometimes, though, you want to force immediate execution of the
   refresh. In these cases, pass an interval of 0 to this method, which
   means don't wait; execute now.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15598:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15599:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15600:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15601:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15602:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15603:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15604:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15605:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15606:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.runCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15607:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.runHelp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15608:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.runNo(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15609:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.runOK(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15610:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.runYes(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15611:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15612:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15613:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15614:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-15615:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setEscapeButton(self, btn=None)
   :noindex:


   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15616:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15617:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15618:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-15619:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-15620:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15621:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15622:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15623:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15624:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15625:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15626:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15627:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15628:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15629:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15630:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15631:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15632:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15633:

.. function:: dabo.ui.uiwx.dDialog.dYesNoDialog.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
