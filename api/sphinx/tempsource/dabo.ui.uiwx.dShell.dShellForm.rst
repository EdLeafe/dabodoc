
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dShell

.. _dabo.ui.uiwx.dShell.dShellForm:

==========================================
|doc_title|  **dShell.dShellForm** - class
==========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dShellForm**

.. inheritance-diagram:: dShellForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dShell.dShellForm


|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-32295>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-32296>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-32297>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-32298>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-32299>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-32300>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-32301>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-32302>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-32303>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-32304>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-32305>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-32306>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-32307>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-32308>`                     The caption of the object. (str)
:ref:`Centered <no-32309>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-32310>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-32311>`                    Returns a list of object references to the children of
:ref:`Class <no-32312>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-32313>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-32314>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-32315>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-32316>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-32317>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-32318>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-32319>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-32320>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-32321>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-32322>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-32323>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-32324>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-32325>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-32326>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-32327>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-32328>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-32329>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-32330>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-32331>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-32332>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-32333>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-32334>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-32335>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-32336>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-32337>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-32338>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-32339>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-32340>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-32341>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-32342>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMinPanelSize <no-32343>`         Dynamically determine the value of the MinPanelSize property.
:ref:`DynamicMousePointer <no-32344>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicOrientation <no-32345>`          Dynamically determine the value of the Orientation property.
:ref:`DynamicPosition <no-32346>`             Dynamically determine the value of the Position property.
:ref:`DynamicSashPosition <no-32347>`         Dynamically determine the value of the SashPosition property.
:ref:`DynamicShowCaption <no-32348>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-32349>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-32350>`                 Dynamically determine the value of the Size property.
:ref:`DynamicSplitState <no-32351>`           Dynamically determine the value of the SplitState property.
:ref:`DynamicStatusBar <no-32352>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-32353>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-32354>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-32355>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-32356>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-32357>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-32358>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-32359>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-32360>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-32361>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-32362>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-32363>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-32364>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-32365>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-32366>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-32367>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-32368>`                    Name of the font face used in the shell  (str)
:ref:`FontInfo <no-32369>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-32370>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-32371>`                    Size of the font used in the shell  (int)
:ref:`FontUnderline <no-32372>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-32373>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-32374>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-32375>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-32376>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-32377>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-32378>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-32379>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-32380>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-32381>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-32382>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-32383>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-32384>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-32385>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-32386>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-32387>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-32388>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinPanelSize <no-32389>`                Controls the minimum width/height of the panels.  (int)
:ref:`MinimumHeight <no-32390>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-32391>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-32392>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-32393>`                       Specifies whether this dForm is modal or not  (bool)
:ref:`MousePointer <no-32394>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-32395>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-32396>`                    Specifies the base name of the object.
:ref:`Orientation <no-32397>`                 Determines if the window splits Horizontally or Vertically.  (str)
:ref:`Panel1 <no-32398>`                      Returns the Top/Left panel.  (SplitterPanel)
:ref:`Panel2 <no-32399>`                      Returns the Bottom/Right panel.  (SplitterPanel)
:ref:`Parent <no-32400>`                      The containing object. (obj)
:ref:`Position <no-32401>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-32402>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-32403>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-32404>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-32405>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-32406>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-32407>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SashPosition <no-32408>`                Position of the sash when the window is split.  (int)
:ref:`SaveAllRows <no-32409>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-32410>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-32411>`         Specifies whether the form's position and size as set by the user
:ref:`ShellClass <no-32412>`                  Class to use for the interactive shell  (dShell)
:ref:`ShowCaption <no-32413>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-32414>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-32415>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-32416>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-32417>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-32418>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-32419>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-32420>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-32421>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-32422>`                        The size of the object. (tuple)
:ref:`Sizer <no-32423>`                       The sizer for the object.
:ref:`SizersToOutline <no-32424>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`SplitState <no-32425>`                  Controls whether the output is in a separate pane (default)
:ref:`Splitter <no-32426>`                    Reference to the main splitter in the form  (dSplitter
:ref:`StatusBar <no-32427>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-32428>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-32429>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-32430>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-32431>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-32432>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-32433>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-32434>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-32435>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-32436>`                         The top position of the object. (int)
:ref:`Transparency <no-32437>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-32438>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-32439>`                     Specifies whether the form is shown or hidden.  (bool)
:ref:`VisibleOnScreen <no-32440>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-32441>`                       The width of the object. (int)
:ref:`WindowHandle <no-32442>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-32443>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties
==========

.. _no-32351:

**DynamicSplitState** 

Dynamically determine the value of the SplitState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SplitState property. If DynamicSplitState is set to None (the default), SplitState
will not be dynamically evaluated.



-------

.. _no-32412:

**ShellClass** 

Class to use for the interactive shell  (dShell)



-------

.. _no-32425:

**SplitState** 

Controls whether the output is in a separate pane (default)
    or intermixed with the commands.  (bool)



-------


Properties - inherited
========================

.. _no-32295:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32296:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32297:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32298:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32299:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32300:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32301:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32302:

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

.. _no-32303:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32304:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32305:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32306:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32307:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32308:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32309:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32310:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32311:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32312:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32313:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32314:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32315:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32316:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32317:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32318:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32319:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32320:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32321:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32322:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32323:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32324:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32325:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32326:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32327:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32328:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32329:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32330:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32331:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32332:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32333:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32334:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32335:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32336:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32337:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32338:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32339:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32340:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32341:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32342:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32343:

**DynamicMinPanelSize** 

Dynamically determine the value of the MinPanelSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MinPanelSize property. If DynamicMinPanelSize is set to None (the default), MinPanelSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32344:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32345:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32346:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32347:

**DynamicSashPosition** 

Dynamically determine the value of the SashPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SashPosition property. If DynamicSashPosition is set to None (the default), SashPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32348:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32349:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32350:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32352:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32353:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32354:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32355:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32356:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32357:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32358:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32359:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32360:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32361:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32362:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32363:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32364:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32365:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32366:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32367:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32368:

**FontFace** 

Name of the font face used in the shell  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32369:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32370:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32371:

**FontSize** 

Size of the font used in the shell  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32372:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32373:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32374:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32375:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32376:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32377:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32378:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-32379:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32380:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32381:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32382:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32383:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32384:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32385:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32386:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-32387:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32388:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32389:

**MinPanelSize** 

Controls the minimum width/height of the panels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32390:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32391:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32392:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32393:

**Modal** 

Specifies whether this dForm is modal or not  (bool)

    A modal dForm runs its own event loop, blocking program flow until the
    form is hidden or closed, exactly like a dDialog does it. This property
    may only be sent to the constructor, and once instantiated you may not
    change the modality of a form. For example::

            frm = dabo.ui.dForm(Modal=True)

    will create a modal form.

    .. note::

        That a modal dForm is actually a dDialog, and as such does not
        have the ability to contain MenuBars, StatusBars, or ToolBars.

    


Inherited from: :ref:`dabo.ui.uiwx.dForm.dForm`

-------

.. _no-32394:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32395:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32396:

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

.. _no-32397:

**Orientation** 

Determines if the window splits Horizontally or Vertically.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32398:

**Panel1** 

Returns the Top/Left panel.  (SplitterPanel)


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32399:

**Panel2** 

Returns the Bottom/Right panel.  (SplitterPanel)


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32400:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32401:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32402:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32403:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32404:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32405:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32406:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32407:

**RowNavigationDelay** 

Specifies optional delay to wait for updating the entire form when the user
    is navigating the records. (int; default=0 [ms])

    Set to 0 or None to ensure that all controls reflect immediately to the data changes.
    Setting to a positive non-zero value will result in the following behavior:

    As the row number changes, dEvents.RowNavigation events will fire and the
    afterRowNavigation() hook method will be called, allowing your form code to update a
    specific set of controls so the user knows the records are being navigated. The
    default behavior will reflect the current row number in the form's status bar as
    row navigation is occurring.

    After a navigation and the RowNavigationDelay has passed, the form will be
    completely updated and refreshed. dEvents.RowNumChanged will be fired, and the
    hook afterPointerMove() will be called.

    Recommended setting if non-zero: 250 [ms]. Values under that result in the timer
    firing before the user can navigate again, although this will be dependent on your
    specific situation.
    


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32408:

**SashPosition** 

Position of the sash when the window is split.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32409:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32410:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32411:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32413:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32414:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32415:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32416:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32417:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32418:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32419:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32420:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32421:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32422:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32423:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32424:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32426:

**Splitter** 

Reference to the main splitter in the form  (dSplitter


Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32427:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-32428:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32429:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32430:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32431:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32432:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32433:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32434:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-32435:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32436:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32437:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32438:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32439:

**Visible** 

Specifies whether the form is shown or hidden.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32440:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32441:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32442:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32443:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`Activate <no-32444>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-32445>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-32446>`              Occurs when a child control is created.
:ref:`Close <no-32447>`                  Occurs when the user closes the form.
:ref:`ControlNavigationEvent <no-32448>` 
:ref:`Create <no-32449>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-32450>`             Occurs when another form becomes active.
:ref:`Destroy <no-32451>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-32452>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-32453>`               Occurs when the control gets the focus.
:ref:`Idle <no-32454>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-32455>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-32456>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-32457>`               
:ref:`KeyUp <no-32458>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-32459>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-32460>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-32461>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-32462>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-32463>`             
:ref:`MouseLeave <no-32464>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-32465>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-32466>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-32467>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-32468>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-32469>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-32470>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-32471>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-32472>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-32473>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-32474>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-32475>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-32476>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-32477>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-32478>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-32479>`                   Occurs when the control's position changes.
:ref:`Paint <no-32480>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-32481>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-32482>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-32483>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-32484>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-32444:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-32445:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-32446:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-32447:

**Close** 

Occurs when the user closes the form.



-------

.. _no-32448:

**ControlNavigationEvent** 



-------

.. _no-32449:

**Create** 

Occurs after the control or form is created.



-------

.. _no-32450:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-32451:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-32452:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-32453:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-32454:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-32455:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-32456:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-32457:

**KeyEvent** 



-------

.. _no-32458:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-32459:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-32460:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-32461:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-32462:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-32463:

**MouseEvent** 



-------

.. _no-32464:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-32465:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-32466:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-32467:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-32468:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-32469:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-32470:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-32471:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-32472:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-32473:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-32474:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-32475:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-32476:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-32477:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-32478:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-32479:

**Move** 

Occurs when the control's position changes.



-------

.. _no-32480:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-32481:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-32482:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-32483:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-32484:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-32485>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-32486>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-32487>`                      Add a bizobj to this form.
:ref:`addObject <no-32488>`                      Instantiate object as a child of self.
:ref:`addToHistory <no-32489>`                   
:ref:`addToOutlinedSizers <no-32490>`            
:ref:`afterCancel <no-32491>`                    
:ref:`afterDelete <no-32492>`                    
:ref:`afterDeleteAll <no-32493>`                 
:ref:`afterFilter <no-32494>`                    
:ref:`afterFirst <no-32495>`                     
:ref:`afterInit <no-32496>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-32497>`                   
:ref:`afterLast <no-32498>`                      
:ref:`afterNew <no-32499>`                       
:ref:`afterNext <no-32500>`                      
:ref:`afterPointerMove <no-32501>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-32502>`                     
:ref:`afterRequery <no-32503>`                   
:ref:`afterRowNavigation <no-32504>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-32505>`                      
:ref:`afterSetMenuBar <no-32506>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-32507>`          Subclass hook.
:ref:`afterSetProperties <no-32508>`             
:ref:`appendOut <no-32509>`                      
:ref:`appendToolBarButton <no-32510>`            
:ref:`autoBindEvents <no-32511>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-32512>`                   
:ref:`beforeClose <no-32513>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-32514>`                   
:ref:`beforeDeleteAll <no-32515>`                
:ref:`beforeFilter <no-32516>`                   
:ref:`beforeFirst <no-32517>`                    
:ref:`beforeInit <no-32518>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-32519>`                     
:ref:`beforeNew <no-32520>`                      
:ref:`beforeNext <no-32521>`                     
:ref:`beforePointerMove <no-32522>`              
:ref:`beforePrior <no-32523>`                    
:ref:`beforeRequery <no-32524>`                  
:ref:`beforeSave <no-32525>`                     
:ref:`beforeSetProperties <no-32526>`            
:ref:`bindEvent <no-32527>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-32528>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-32529>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-32530>`                   Makes this object topmost
:ref:`cancel <no-32531>`                         Ask the bizobj to cancel its changes.
:ref:`clear <no-32532>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-32533>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-32534>`                          This method will close the form. If force = False (default)
:ref:`closing <no-32535>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-32536>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-32537>`           Given a position relative to this control, return a position relative
:ref:`copy <no-32538>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-32539>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-32540>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-32541>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-32542>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-32543>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-32544>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-32545>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-32546>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-32547>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-32548>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-32549>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-32550>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-32551>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-32552>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-32553>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-32554>`                       Draws text on the object at the specified position
:ref:`endHover <no-32555>`                       
:ref:`fillMenu <no-32556>`                       
:ref:`fillPreferenceDialog <no-32557>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-32558>`                         Apply a filter to the bizobj's data.
:ref:`first <no-32559>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-32560>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-32561>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-32562>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-32563>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-32564>`              
:ref:`formCoordinates <no-32565>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-32566>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-32567>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-32568>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-32569>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-32570>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-32571>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-32572>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-32573>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-32574>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-32575>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-32576>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-32577>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-32578>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-32579>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-32580>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-32581>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-32582>`                           Make the object invisible.
:ref:`initEvents <no-32583>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-32584>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-32585>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-32586>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-32587>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-32588>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-32589>`                    Locks the visual updates to the control.
:ref:`moveCodeStack <no-32590>`                  
:ref:`moveTabOrderAfter <no-32591>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-32592>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-32593>`                Move the record pointer to the specified row.
:ref:`new <no-32594>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-32595>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-32596>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-32597>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-32598>`                       
:ref:`onClearOutput <no-32599>`                  
:ref:`onCodeKeyDown <no-32600>`                  
:ref:`onCodeRightDown <no-32601>`                
:ref:`onDelete <no-32602>`                       
:ref:`onEditRedo <no-32603>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-32604>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-32605>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-32606>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-32607>`                        
:ref:`onHistoryPop <no-32608>`                   Let the user type in part of a command, and retrieve the matching commands
:ref:`onHover <no-32609>`                        
:ref:`onLast <no-32610>`                         
:ref:`onNew <no-32611>`                          
:ref:`onNext <no-32612>`                         
:ref:`onOutputRightDown <no-32613>`              
:ref:`onPrior <no-32614>`                        
:ref:`onRequery <no-32615>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onResize <no-32616>`                       
:ref:`onRunCode <no-32617>`                      
:ref:`onSave <no-32618>`                         
:ref:`onShellContext <no-32619>`                 
:ref:`onShellRight <no-32620>`                   
:ref:`onSplitContext <no-32621>`                 
:ref:`onToggleCodePane <no-32622>`               Toggle between the Code Pane and the Output Pane
:ref:`onViewZoomIn <no-32623>`                   
:ref:`onViewZoomNormal <no-32624>`               
:ref:`onViewZoomOut <no-32625>`                  
:ref:`paste <no-32626>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-32627>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-32628>`                    
:ref:`prior <no-32629>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-32630>`            This will fire if files are dropped on the code editor. If more than one
:ref:`processDroppedText <no-32631>`             Add the text to the code editor.
:ref:`pushStatusText <no-32632>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-32633>`                     Raise the passed Dabo event.
:ref:`reCreate <no-32634>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-32635>`                       Recreate the object.
:ref:`redraw <no-32636>`                         Called when the object is (re)drawn.
:ref:`refresh <no-32637>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-32638>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-32639>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-32640>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-32641>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-32642>`              
:ref:`removeFilter <no-32643>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-32644>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-32645>`       
:ref:`requery <no-32646>`                        Ask the bizobj to requery.
:ref:`restoreHistory <no-32647>`                 Get the stored history from previous sessions, and set the shell's
:ref:`restoreSizeAndPosition <no-32648>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-32649>` 
:ref:`safeDestroy <no-32650>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`sashDoubleClick <no-32651>`                
:ref:`sashPosChanged <no-32652>`                 
:ref:`save <no-32653>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-32654>`            Save the current size and position of this form.
:ref:`sendToBack <no-32655>`                     Places this object behind all others.
:ref:`setAll <no-32656>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-32657>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-32658>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-32659>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-32660>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-32661>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-32662>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-32663>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-32664>`                  Set the status text to val.
:ref:`show <no-32665>`                           Make the object visible.
:ref:`showContainingPage <no-32666>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-32667>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-32668>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`split <no-32669>`                          
:ref:`super <no-32670>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-32671>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-32672>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-32673>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-32674>`               Immediately unlocks the display, no matter how many previous
:ref:`unsplit <no-32675>`                        
:ref:`update <no-32676>`                         Updates the contained controls with current values from the source.
:ref:`validateField <no-32677>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods
=======

.. _no-32489:

.. function:: dabo.ui.uiwx.dShell.dShellForm.addToHistory(self, cmd=None)



-------

.. _no-32509:

.. function:: dabo.ui.uiwx.dShell.dShellForm.appendOut(self, tx)



-------

.. _no-32556:

.. function:: dabo.ui.uiwx.dShell.dShellForm.fillMenu(self)



-------

.. _no-32590:

.. function:: dabo.ui.uiwx.dShell.dShellForm.moveCodeStack(self, direction)



-------

.. _no-32599:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onClearOutput(self, evt)



-------

.. _no-32600:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onCodeKeyDown(self, evt)



-------

.. _no-32601:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onCodeRightDown(self, evt)



-------

.. _no-32608:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onHistoryPop(self, evt)

   
   Let the user type in part of a command, and retrieve the matching commands
   from their history.
   



-------

.. _no-32613:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onOutputRightDown(self, evt)



-------

.. _no-32616:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onResize(self, evt)



-------

.. _no-32617:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onRunCode(self, evt, addReturn=True)



-------

.. _no-32619:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onShellContext(self, evt)



-------

.. _no-32620:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onShellRight(self, evt)



-------

.. _no-32621:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onSplitContext(self, evt)



-------

.. _no-32622:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onToggleCodePane(self, evt)

   Toggle between the Code Pane and the Output Pane



-------

.. _no-32623:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onViewZoomIn(self, evt)



-------

.. _no-32624:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onViewZoomNormal(self, evt)



-------

.. _no-32625:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onViewZoomOut(self, evt)



-------

.. _no-32630:

.. function:: dabo.ui.uiwx.dShell.dShellForm.processDroppedFiles(self, filelist)

   
   This will fire if files are dropped on the code editor. If more than one
   file is dropped, only open the first, and warn the user.
   



-------

.. _no-32631:

.. function:: dabo.ui.uiwx.dShell.dShellForm.processDroppedText(self, txt)

   Add the text to the code editor.



-------

.. _no-32647:

.. function:: dabo.ui.uiwx.dShell.dShellForm.restoreHistory(self)

   
   Get the stored history from previous sessions, and set the shell's
   internal command history list to it.
   



-------

.. _no-32651:

.. function:: dabo.ui.uiwx.dShell.dShellForm.sashDoubleClick(self, evt)



-------

.. _no-32652:

.. function:: dabo.ui.uiwx.dShell.dShellForm.sashPosChanged(self, evt)



-------


Methods - inherited
=====================

.. _no-32485:

.. function:: dabo.ui.uiwx.dShell.dShellForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32486:

.. function:: dabo.ui.uiwx.dShell.dShellForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32487:

.. function:: dabo.ui.uiwx.dShell.dShellForm.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32488:

.. function:: dabo.ui.uiwx.dShell.dShellForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-32490:

.. function:: dabo.ui.uiwx.dShell.dShellForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32491:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32492:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32493:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32494:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32495:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32496:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32497:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32498:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32499:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32500:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32501:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32502:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32503:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32504:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32505:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32506:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32507:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32508:

.. function:: dabo.ui.uiwx.dShell.dShellForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32510:

.. function:: dabo.ui.uiwx.dShell.dShellForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32511:

.. function:: dabo.ui.uiwx.dShell.dShellForm.autoBindEvents(self, force=True)
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

.. _no-32512:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32513:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32514:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32515:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32516:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32517:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32518:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32519:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32520:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32521:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32522:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32523:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32524:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32525:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32526:

.. function:: dabo.ui.uiwx.dShell.dShellForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32527:

.. function:: dabo.ui.uiwx.dShell.dShellForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32528:

.. function:: dabo.ui.uiwx.dShell.dShellForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32529:

.. function:: dabo.ui.uiwx.dShell.dShellForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-32530:

.. function:: dabo.ui.uiwx.dShell.dShellForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32531:

.. function:: dabo.ui.uiwx.dShell.dShellForm.cancel(self, dataSource=None, ignoreNoRecords=None)
   :noindex:


   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32532:

.. function:: dabo.ui.uiwx.dShell.dShellForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32533:

.. function:: dabo.ui.uiwx.dShell.dShellForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32534:

.. function:: dabo.ui.uiwx.dShell.dShellForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32535:

.. function:: dabo.ui.uiwx.dShell.dShellForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32536:

.. function:: dabo.ui.uiwx.dShell.dShellForm.confirmChanges(self, bizobjs=None)
   :noindex:


   
   Ask the user if they want to save changes, discard changes, or cancel.
   
   The user will be queried if the form's CheckForChanges property is True, and
   if there are any pending changes on the form's bizobjs as specified in either
   the 'bizobjs' parameter, or, if no parameter is sent, the return value of
   getBizobjsToCheck().
   
   If all the above are True, the dialog will be presented. "Yes" will cause
   all changes to be saved. "No" will discard any changes before proceeding
   with the operation that caused confirmChanges() to be called in the first
   place (e.g. a requery() or the form being closed). "Cancel" will not save
   any changes, but also cancel the requery or form close.
   
   See also: getBizobjsToCheck() method, CheckForChanges property.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32537:

.. function:: dabo.ui.uiwx.dShell.dShellForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32538:

.. function:: dabo.ui.uiwx.dShell.dShellForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32539:

.. function:: dabo.ui.uiwx.dShell.dShellForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32540:

.. function:: dabo.ui.uiwx.dShell.dShellForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32541:

.. function:: dabo.ui.uiwx.dShell.dShellForm.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32542:

.. function:: dabo.ui.uiwx.dShell.dShellForm.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32543:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32544:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32545:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-32546:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32547:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32548:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32549:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32550:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32551:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32552:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32553:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32554:

.. function:: dabo.ui.uiwx.dShell.dShellForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32555:

.. function:: dabo.ui.uiwx.dShell.dShellForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32557:

.. function:: dabo.ui.uiwx.dShell.dShellForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32558:

.. function:: dabo.ui.uiwx.dShell.dShellForm.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32559:

.. function:: dabo.ui.uiwx.dShell.dShellForm.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32560:

.. function:: dabo.ui.uiwx.dShell.dShellForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32561:

.. function:: dabo.ui.uiwx.dShell.dShellForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32562:

.. function:: dabo.ui.uiwx.dShell.dShellForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32563:

.. function:: dabo.ui.uiwx.dShell.dShellForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32564:

.. function:: dabo.ui.uiwx.dShell.dShellForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32565:

.. function:: dabo.ui.uiwx.dShell.dShellForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32566:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32567:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32568:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getBizobjsToCheck(self)
   :noindex:


   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32569:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32570:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32571:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32572:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32573:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32574:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32575:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32576:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32577:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32578:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-32579:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32580:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32581:

.. function:: dabo.ui.uiwx.dShell.dShellForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32582:

.. function:: dabo.ui.uiwx.dShell.dShellForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32583:

.. function:: dabo.ui.uiwx.dShell.dShellForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32584:

.. function:: dabo.ui.uiwx.dShell.dShellForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32585:

.. function:: dabo.ui.uiwx.dShell.dShellForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32586:

.. function:: dabo.ui.uiwx.dShell.dShellForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32587:

.. function:: dabo.ui.uiwx.dShell.dShellForm.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32588:

.. function:: dabo.ui.uiwx.dShell.dShellForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32589:

.. function:: dabo.ui.uiwx.dShell.dShellForm.lockDisplay(self)
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

.. _no-32591:

.. function:: dabo.ui.uiwx.dShell.dShellForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32592:

.. function:: dabo.ui.uiwx.dShell.dShellForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32593:

.. function:: dabo.ui.uiwx.dShell.dShellForm.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32594:

.. function:: dabo.ui.uiwx.dShell.dShellForm.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32595:

.. function:: dabo.ui.uiwx.dShell.dShellForm.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32596:

.. function:: dabo.ui.uiwx.dShell.dShellForm.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32597:

.. function:: dabo.ui.uiwx.dShell.dShellForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32598:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onCancel(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32602:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onDelete(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32603:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32604:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32605:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32606:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32607:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32609:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32610:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32611:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onNew(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32612:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32614:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32615:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onRequery(self, evt)
   :noindex:


   Occurs when an EVT_MENU event is received by this form.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32618:

.. function:: dabo.ui.uiwx.dShell.dShellForm.onSave(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32626:

.. function:: dabo.ui.uiwx.dShell.dShellForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32627:

.. function:: dabo.ui.uiwx.dShell.dShellForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32628:

.. function:: dabo.ui.uiwx.dShell.dShellForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32629:

.. function:: dabo.ui.uiwx.dShell.dShellForm.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32632:

.. function:: dabo.ui.uiwx.dShell.dShellForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32633:

.. function:: dabo.ui.uiwx.dShell.dShellForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32634:

.. function:: dabo.ui.uiwx.dShell.dShellForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32635:

.. function:: dabo.ui.uiwx.dShell.dShellForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32636:

.. function:: dabo.ui.uiwx.dShell.dShellForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32637:

.. function:: dabo.ui.uiwx.dShell.dShellForm.refresh(self, interval=None)
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

.. _no-32638:

.. function:: dabo.ui.uiwx.dShell.dShellForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32639:

.. function:: dabo.ui.uiwx.dShell.dShellForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32640:

.. function:: dabo.ui.uiwx.dShell.dShellForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32641:

.. function:: dabo.ui.uiwx.dShell.dShellForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32642:

.. function:: dabo.ui.uiwx.dShell.dShellForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32643:

.. function:: dabo.ui.uiwx.dShell.dShellForm.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32644:

.. function:: dabo.ui.uiwx.dShell.dShellForm.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32645:

.. function:: dabo.ui.uiwx.dShell.dShellForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32646:

.. function:: dabo.ui.uiwx.dShell.dShellForm.requery(self, dataSource=None)
   :noindex:


   Ask the bizobj to requery.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32648:

.. function:: dabo.ui.uiwx.dShell.dShellForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32649:

.. function:: dabo.ui.uiwx.dShell.dShellForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32650:

.. function:: dabo.ui.uiwx.dShell.dShellForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32653:

.. function:: dabo.ui.uiwx.dShell.dShellForm.save(self, dataSource=None)
   :noindex:


   Ask the bizobj to commit its changes to the backend.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32654:

.. function:: dabo.ui.uiwx.dShell.dShellForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32655:

.. function:: dabo.ui.uiwx.dShell.dShellForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32656:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-32657:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32658:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32659:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-32660:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-32661:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32662:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32663:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32664:

.. function:: dabo.ui.uiwx.dShell.dShellForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32665:

.. function:: dabo.ui.uiwx.dShell.dShellForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32666:

.. function:: dabo.ui.uiwx.dShell.dShellForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32667:

.. function:: dabo.ui.uiwx.dShell.dShellForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32668:

.. function:: dabo.ui.uiwx.dShell.dShellForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-32669:

.. function:: dabo.ui.uiwx.dShell.dShellForm.split(self, dir=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32670:

.. function:: dabo.ui.uiwx.dShell.dShellForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32671:

.. function:: dabo.ui.uiwx.dShell.dShellForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32672:

.. function:: dabo.ui.uiwx.dShell.dShellForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32673:

.. function:: dabo.ui.uiwx.dShell.dShellForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32674:

.. function:: dabo.ui.uiwx.dShell.dShellForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32675:

.. function:: dabo.ui.uiwx.dShell.dShellForm.unsplit(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`

-------

.. _no-32676:

.. function:: dabo.ui.uiwx.dShell.dShellForm.update(self, interval=None)
   :noindex:


   
   Updates the contained controls with current values from the source.
   
   This method is called repeatedly from many different places during
   a single change in the UI, so by default the actual execution is cached
   using callAfterInterval(). The default interval is the value of the
   DataUpdateDelay property, which in turn defaults to 100 milliseconds. You
   can change that to suit your app needs by passing a different interval
   in milliseconds.
   
   Sometimes, though, you want to force immediate execution of the
   update. In these cases, pass an interval of 0 to this method, which
   means don't wait; execute now.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-32677:

.. function:: dabo.ui.uiwx.dShell.dShellForm.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
