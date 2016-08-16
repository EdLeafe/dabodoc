
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.PreferenceDialog

.. _dabo.ui.dialogs.PreferenceDialog.PreferenceDialog:

==========================================================
|doc_title|  **PreferenceDialog.PreferenceDialog** - class
==========================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **PreferenceDialog**

.. inheritance-diagram:: PreferenceDialog


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dOkCancelDialog`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/PreferenceDialog.png
          :scale: 75 %
          :target: _static/macWidgets/PreferenceDialog.png
          :alt: PreferenceDialog



     - .. image:: _static/winWidgets/PreferenceDialog.png
          :scale: 75 %
          :target: _static/winWidgets/PreferenceDialog.png
          :alt: PreferenceDialog



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog


|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`Accepted <no-10252>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-10253>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-10254>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-10255>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-10256>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-10257>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-10258>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-10259>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-10260>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-10261>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-10262>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-10263>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-10264>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-10265>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-10266>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-10267>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-10268>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-10269>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-10270>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-10271>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-10272>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-10273>`                    Returns a list of object references to the children of
:ref:`Class <no-10274>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-10275>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-10276>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-10277>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-10278>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-10279>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-10280>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-10281>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-10282>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-10283>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-10284>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-10285>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-10286>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-10287>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-10288>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-10289>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-10290>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-10291>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-10292>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-10293>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-10294>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-10295>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-10296>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-10297>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-10298>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-10299>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-10300>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-10301>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-10302>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-10303>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-10304>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-10305>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-10306>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-10307>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-10308>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-10309>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-10310>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-10311>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-10312>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-10313>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-10314>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-10315>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-10316>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-10317>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-10318>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-10319>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-10320>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-10321>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-10322>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-10323>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-10324>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-10325>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-10326>`                    Specifies the font face. (str)
:ref:`FontInfo <no-10327>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-10328>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-10329>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-10330>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-10331>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-10332>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-10333>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-10334>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-10335>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-10336>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-10337>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-10338>`         Controls how often the form is refreshed when idle.
:ref:`IncludeDefaultPages <no-10339>`         When True, the _addDefaultPages() method is called to add the common
:ref:`IncludeFrameworkPages <no-10340>`       When True, the _addFrameworkPages() method is called to add the common
:ref:`Left <no-10341>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-10342>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-10343>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-10344>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-10345>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-10346>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-10347>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-10348>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-10349>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-10350>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-10351>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-10352>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-10353>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-10354>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-10355>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-10356>`                    Specifies the base name of the object.
:ref:`NoButton <no-10357>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-10358>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-10359>`                      The containing object. (obj)
:ref:`Position <no-10360>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-10361>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-10362>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-10363>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-10364>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-10365>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-10366>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-10367>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-10368>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-10369>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-10370>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-10371>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-10372>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-10373>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-10374>`                        The size of the object. (tuple)
:ref:`Sizer <no-10375>`                       The sizer for the object.
:ref:`SizersToOutline <no-10376>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-10377>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-10378>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-10379>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-10380>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-10381>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-10382>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-10383>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-10384>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-10385>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-10386>`                         The top position of the object. (int)
:ref:`Transparency <no-10387>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-10388>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-10389>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-10390>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-10391>`                       The width of the object. (int)
:ref:`WindowHandle <no-10392>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-10393>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-10394>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================= ========================


Properties
==========

.. _no-10339:

**IncludeDefaultPages** 

When True, the _addDefaultPages() method is called to add the common
    Dabo settings. Default=True  (bool)



-------

.. _no-10340:

**IncludeFrameworkPages** 

When True, the _addFrameworkPages() method is called to add the common
    Dabo settings. Default=False  (bool)



-------


Properties - inherited
========================

.. _no-10252:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10253:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10254:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10255:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10256:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10257:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10258:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10259:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10260:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10261:

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

.. _no-10262:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10263:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10264:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10265:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10266:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10267:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10268:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10269:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10270:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10271:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10272:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10273:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10274:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10275:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10276:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10277:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10278:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10279:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10280:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10281:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10282:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10283:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10284:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10285:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10286:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10287:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10288:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10289:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10290:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10291:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10292:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10293:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10294:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10295:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10296:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10297:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10298:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10299:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10300:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10301:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10302:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10303:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10304:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10305:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10306:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10307:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10308:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10309:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10310:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10311:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10312:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10313:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10314:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10315:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10316:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10317:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10318:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10319:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10320:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10321:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10322:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10323:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10324:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10325:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10326:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10327:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10328:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10329:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10330:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10331:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10332:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10333:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10334:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10335:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10336:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10337:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-10338:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10341:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10342:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10343:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10344:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10345:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10346:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10347:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10348:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10349:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10350:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10351:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10352:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10353:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10354:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10355:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10356:

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

.. _no-10357:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10358:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10359:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10360:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10361:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10362:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10363:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10364:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10365:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10366:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10367:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10368:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10369:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10370:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10371:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10372:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10373:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10374:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10375:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10376:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10377:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10378:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10379:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10380:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10381:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10382:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10383:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10384:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10385:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10386:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10387:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10388:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10389:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10390:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10391:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10392:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10393:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10394:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`Activate <no-10395>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-10396>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-10397>`              Occurs when a child control is created.
:ref:`Close <no-10398>`                  Occurs when the user closes the form.
:ref:`Create <no-10399>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-10400>`             Occurs when another form becomes active.
:ref:`Destroy <no-10401>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-10402>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-10403>`               Occurs when the control gets the focus.
:ref:`Idle <no-10404>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-10405>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-10406>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-10407>`               
:ref:`KeyUp <no-10408>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-10409>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-10410>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-10411>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-10412>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-10413>`             
:ref:`MouseLeave <no-10414>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-10415>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-10416>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-10417>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-10418>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-10419>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-10420>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-10421>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-10422>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-10423>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-10424>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-10425>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-10426>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-10427>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-10428>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-10429>`                   Occurs when the control's position changes.
:ref:`Paint <no-10430>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-10431>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-10432>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-10433>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-10434>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-10395:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-10396:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-10397:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-10398:

**Close** 

Occurs when the user closes the form.



-------

.. _no-10399:

**Create** 

Occurs after the control or form is created.



-------

.. _no-10400:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-10401:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-10402:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-10403:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-10404:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-10405:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-10406:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-10407:

**KeyEvent** 



-------

.. _no-10408:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-10409:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-10410:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-10411:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-10412:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-10413:

**MouseEvent** 



-------

.. _no-10414:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-10415:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-10416:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-10417:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-10418:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-10419:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-10420:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-10421:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-10422:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-10423:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-10424:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-10425:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-10426:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-10427:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-10428:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-10429:

**Move** 

Occurs when the control's position changes.



-------

.. _no-10430:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-10431:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-10432:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-10433:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-10434:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-10435>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-10436>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addCategory <no-10437>`                    Adds a page to the main PageList control, sets the caption to the
:ref:`addControlSequence <no-10438>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-10439>`                    Add the base PageList, and then delete this method from the
:ref:`addObject <no-10440>`                      Instantiate object as a child of self.
:ref:`addPages <no-10441>`                       
:ref:`addToOutlinedSizers <no-10442>`            
:ref:`afterAddControls <no-10443>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-10444>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-10445>`                   
:ref:`afterSetMenuBar <no-10446>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-10447>`             
:ref:`appendPage <no-10448>`                     Pass-through method to the internal paged control
:ref:`appendToolBarButton <no-10449>`            
:ref:`autoBindEvents <no-10450>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-10451>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-10452>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-10453>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-10454>`            
:ref:`bindEvent <no-10455>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-10456>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-10457>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-10458>`                   Makes this object topmost
:ref:`clear <no-10459>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-10460>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-10461>`                          This method will close the form. If force = False (default)
:ref:`closing <no-10462>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-10463>`           Given a position relative to this control, return a position relative
:ref:`copy <no-10464>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-10465>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-10466>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-10467>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-10468>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-10469>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-10470>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-10471>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-10472>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-10473>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-10474>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-10475>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-10476>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-10477>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-10478>`                       Draws text on the object at the specified position
:ref:`endHover <no-10479>`                       
:ref:`fillPreferenceDialog <no-10480>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-10481>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-10482>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-10483>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-10484>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-10485>`              
:ref:`formCoordinates <no-10486>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-10487>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-10488>`                      
:ref:`getCaptureBitmap <no-10489>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-10490>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-10491>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-10492>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-10493>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-10494>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-10495>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-10496>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-10497>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-10498>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-10499>`                           Make the object invisible.
:ref:`initEvents <no-10500>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-10501>`                 Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-10502>`                     Pass-through method to the internal paged control
:ref:`isContainedBy <no-10503>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-10504>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-10505>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-10506>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-10507>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-10508>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-10509>`              Given a position relative to the form, return a position relative
:ref:`onAcceptPref <no-10510>`                   Override this for subclasses where you need separate OK processing.
:ref:`onCancelPref <no-10511>`                   Override this for subclasses where you need separate Cancel processing.
:ref:`onCheckNow <no-10512>`                     
:ref:`onChkUpdate <no-10513>`                    
:ref:`onEditRedo <no-10514>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-10515>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-10516>`                        
:ref:`onRollbackMenuChanges <no-10517>`          
:ref:`paste <no-10518>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-10519>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-10520>`                    
:ref:`processDroppedFiles <no-10521>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-10522>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-10523>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-10524>`                     Raise the passed Dabo event.
:ref:`reCreate <no-10525>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-10526>`                       Recreate the object.
:ref:`redraw <no-10527>`                         Called when the object is (re)drawn.
:ref:`refresh <no-10528>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-10529>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-10530>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-10531>`                        Need to augment this to make sure the dialog
:ref:`reload <no-10532>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-10533>`              
:ref:`removeFromOutlinedSizers <no-10534>`       
:ref:`restoreSizeAndPosition <no-10535>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-10536>` 
:ref:`runCancel <no-10537>`                      
:ref:`runHelp <no-10538>`                        
:ref:`runNo <no-10539>`                          
:ref:`runOK <no-10540>`                          
:ref:`runYes <no-10541>`                         
:ref:`safeDestroy <no-10542>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-10543>`            Save the current size and position of this form.
:ref:`sendToBack <no-10544>`                     Places this object behind all others.
:ref:`setAll <no-10545>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-10546>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-10547>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-10548>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-10549>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-10550>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-10551>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-10552>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-10553>`                  Set the status text to val.
:ref:`show <no-10554>`                           
:ref:`showContainingPage <no-10555>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-10556>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-10557>`                      Show the dialog modally.
:ref:`showModeless <no-10558>`                   Show the dialog non-modally.
:ref:`super <no-10559>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-10560>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-10561>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-10562>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-10563>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-10564>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods
=======

.. _no-10437:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.addCategory(self, category, pos=None)

   
   Adds a page to the main PageList control, sets the caption to the
   passed string, and returns a reference to the page. If the optional 'pos'
   parameter is passed, the page is inserted in that position; otherwise, it
   is appended after any existing pages.
   



-------

.. _no-10439:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.addControls(self)

   
   Add the base PageList, and then delete this method from the
   namespace. Users will customize with addCategory() and then
   adding controls to the category page.
   



-------

.. _no-10441:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.addPages(self)



-------

.. _no-10448:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.appendPage(self, pgCls=None, \*args, \**kwargs)

   Pass-through method to the internal paged control



-------

.. _no-10502:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.insertPage(self, pos, pgCls=None, \*args, \**kwargs)

   Pass-through method to the internal paged control



-------

.. _no-10510:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onAcceptPref(self)

   Override this for subclasses where you need separate OK processing.



-------

.. _no-10511:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onCancelPref(self)

   Override this for subclasses where you need separate Cancel processing.



-------

.. _no-10512:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onCheckNow(self, evt)



-------

.. _no-10513:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onChkUpdate(self, evt)



-------

.. _no-10517:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onRollbackMenuChanges(self)



-------


Methods - inherited
=====================

.. _no-10435:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10436:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10438:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.addControlSequence(self, seq)
   :noindex:


   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10440:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-10442:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10443:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10444:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10445:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10446:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10447:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10449:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10450:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.autoBindEvents(self, force=True)
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

.. _no-10451:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10452:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10453:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10454:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10455:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10456:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10457:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-10458:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10459:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10460:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10461:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10462:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10463:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10464:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10465:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10466:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10467:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10468:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10469:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-10470:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10471:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10472:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10473:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10474:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10475:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10476:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10477:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10478:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10479:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10480:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10481:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10482:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10483:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10484:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10485:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10486:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10487:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10488:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10489:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10490:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10491:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10492:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10493:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10494:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10495:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10496:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-10497:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10498:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10499:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10500:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10501:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10503:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10504:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10505:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10506:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.lockDisplay(self)
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

.. _no-10507:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10508:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10509:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10514:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10515:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10516:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10518:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10519:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10520:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10521:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10522:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10523:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10524:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10525:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10526:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10527:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10528:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.refresh(self, interval=None)
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

.. _no-10529:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10530:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10531:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10532:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10533:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10534:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10535:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10536:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10537:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.runCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10538:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.runHelp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10539:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.runNo(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10540:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.runOK(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10541:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.runYes(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10542:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10543:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10544:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10545:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-10546:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setEscapeButton(self, btn=None)
   :noindex:


   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-10547:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10548:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10549:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-10550:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-10551:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10552:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10553:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10554:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10555:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10556:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10557:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10558:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10559:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10560:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10561:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10562:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10563:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10564:

.. function:: dabo.ui.dialogs.PreferenceDialog.PreferenceDialog.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
