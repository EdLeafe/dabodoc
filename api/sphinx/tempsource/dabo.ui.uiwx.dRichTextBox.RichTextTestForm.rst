
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dRichTextBox

.. _dabo.ui.uiwx.dRichTextBox.RichTextTestForm:

======================================================
|doc_title|  **dRichTextBox.RichTextTestForm** - class
======================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **RichTextTestForm**

.. inheritance-diagram:: RichTextTestForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dForm.dForm`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm


|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-18584>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-18585>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-18586>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-18587>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-18588>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-18589>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-18590>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-18591>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-18592>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-18593>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-18594>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-18595>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-18596>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-18597>`                     The caption of the object. (str)
:ref:`Centered <no-18598>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-18599>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-18600>`                    Returns a list of object references to the children of
:ref:`Class <no-18601>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-18602>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-18603>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-18604>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-18605>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-18606>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-18607>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-18608>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-18609>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-18610>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-18611>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-18612>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-18613>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-18614>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-18615>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-18616>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-18617>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-18618>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-18619>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-18620>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-18621>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-18622>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-18623>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-18624>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-18625>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-18626>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-18627>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-18628>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-18629>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-18630>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-18631>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-18632>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-18633>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-18634>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-18635>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-18636>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-18637>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-18638>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-18639>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-18640>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-18641>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-18642>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-18643>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-18644>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-18645>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-18646>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-18647>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-18648>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-18649>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-18650>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-18651>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-18652>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-18653>`                    Specifies the font face. (str)
:ref:`FontInfo <no-18654>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-18655>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-18656>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-18657>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-18658>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-18659>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-18660>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-18661>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-18662>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-18663>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-18664>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-18665>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-18666>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-18667>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-18668>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-18669>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-18670>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-18671>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-18672>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-18673>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-18674>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-18675>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-18676>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-18677>`                       Specifies whether this dForm is modal or not  (bool)
:ref:`MousePointer <no-18678>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-18679>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-18680>`                    Specifies the base name of the object.
:ref:`Parent <no-18681>`                      The containing object. (obj)
:ref:`Position <no-18682>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-18683>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-18684>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-18685>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-18686>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-18687>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-18688>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SaveAllRows <no-18689>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-18690>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-18691>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-18692>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-18693>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-18694>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-18695>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-18696>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-18697>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-18698>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-18699>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-18700>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-18701>`                        The size of the object. (tuple)
:ref:`Sizer <no-18702>`                       The sizer for the object.
:ref:`SizersToOutline <no-18703>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-18704>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-18705>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-18706>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-18707>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-18708>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-18709>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-18710>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-18711>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-18712>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-18713>`                         The top position of the object. (int)
:ref:`Transparency <no-18714>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-18715>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-18716>`                     Specifies whether the form is shown or hidden.  (bool)
:ref:`VisibleOnScreen <no-18717>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-18718>`                       The width of the object. (int)
:ref:`WindowHandle <no-18719>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-18720>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties - inherited
========================

.. _no-18584:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18585:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18586:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18587:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18588:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18589:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18590:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18591:

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

.. _no-18592:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18593:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18594:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18595:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18596:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18597:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18598:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18599:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18600:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18601:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18602:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18603:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18604:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18605:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18606:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18607:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18608:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18609:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18610:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18611:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18612:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18613:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18614:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18615:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18616:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18617:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18618:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18619:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18620:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18621:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18622:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18623:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18624:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18625:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18626:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18627:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18628:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18629:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18630:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18631:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18632:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18633:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18634:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18635:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18636:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18637:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18638:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18639:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18640:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18641:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18642:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18643:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18644:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18645:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18646:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18647:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18648:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18649:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18650:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18651:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18652:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18653:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18654:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18655:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18656:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18657:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18658:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18659:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18660:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18661:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18662:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18663:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-18664:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18665:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18666:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18667:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18668:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18669:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18670:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18671:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-18672:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18673:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18674:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18675:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18676:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18677:

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

.. _no-18678:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18679:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18680:

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

.. _no-18681:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18682:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18683:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18684:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18685:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18686:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18687:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18688:

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

.. _no-18689:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18690:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18691:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18692:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18693:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18694:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18695:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18696:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18697:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18698:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18699:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18700:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18701:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18702:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18703:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18704:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-18705:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18706:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18707:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18708:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18709:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18710:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18711:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-18712:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18713:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18714:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18715:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18716:

**Visible** 

Specifies whether the form is shown or hidden.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18717:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18718:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18719:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18720:

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
:ref:`Activate <no-18721>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-18722>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-18723>`              Occurs when a child control is created.
:ref:`Close <no-18724>`                  Occurs when the user closes the form.
:ref:`ControlNavigationEvent <no-18725>` 
:ref:`Create <no-18726>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-18727>`             Occurs when another form becomes active.
:ref:`Destroy <no-18728>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-18729>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-18730>`               Occurs when the control gets the focus.
:ref:`Idle <no-18731>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-18732>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-18733>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-18734>`               
:ref:`KeyUp <no-18735>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-18736>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-18737>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-18738>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-18739>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-18740>`             
:ref:`MouseLeave <no-18741>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-18742>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-18743>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-18744>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-18745>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-18746>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-18747>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-18748>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-18749>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-18750>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-18751>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-18752>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-18753>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-18754>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-18755>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-18756>`                   Occurs when the control's position changes.
:ref:`Paint <no-18757>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-18758>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-18759>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-18760>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-18761>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-18721:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-18722:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-18723:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-18724:

**Close** 

Occurs when the user closes the form.



-------

.. _no-18725:

**ControlNavigationEvent** 



-------

.. _no-18726:

**Create** 

Occurs after the control or form is created.



-------

.. _no-18727:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-18728:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-18729:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-18730:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-18731:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-18732:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-18733:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-18734:

**KeyEvent** 



-------

.. _no-18735:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-18736:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-18737:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-18738:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-18739:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-18740:

**MouseEvent** 



-------

.. _no-18741:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-18742:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-18743:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-18744:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-18745:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-18746:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-18747:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-18748:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-18749:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-18750:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-18751:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-18752:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-18753:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-18754:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-18755:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-18756:

**Move** 

Occurs when the control's position changes.



-------

.. _no-18757:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-18758:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-18759:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-18760:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-18761:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-18762>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-18763>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-18764>`                      Add a bizobj to this form.
:ref:`addObject <no-18765>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-18766>`            
:ref:`afterCancel <no-18767>`                    
:ref:`afterDelete <no-18768>`                    
:ref:`afterDeleteAll <no-18769>`                 
:ref:`afterFilter <no-18770>`                    
:ref:`afterFirst <no-18771>`                     
:ref:`afterInit <no-18772>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-18773>`                   
:ref:`afterLast <no-18774>`                      
:ref:`afterNew <no-18775>`                       
:ref:`afterNext <no-18776>`                      
:ref:`afterPointerMove <no-18777>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-18778>`                     
:ref:`afterRequery <no-18779>`                   
:ref:`afterRowNavigation <no-18780>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-18781>`                      
:ref:`afterSetMenuBar <no-18782>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-18783>`          Subclass hook.
:ref:`afterSetProperties <no-18784>`             
:ref:`appendToolBarButton <no-18785>`            
:ref:`autoBindEvents <no-18786>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-18787>`                   
:ref:`beforeClose <no-18788>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-18789>`                   
:ref:`beforeDeleteAll <no-18790>`                
:ref:`beforeFilter <no-18791>`                   
:ref:`beforeFirst <no-18792>`                    
:ref:`beforeInit <no-18793>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-18794>`                     
:ref:`beforeNew <no-18795>`                      
:ref:`beforeNext <no-18796>`                     
:ref:`beforePointerMove <no-18797>`              
:ref:`beforePrior <no-18798>`                    
:ref:`beforeRequery <no-18799>`                  
:ref:`beforeSave <no-18800>`                     
:ref:`beforeSetProperties <no-18801>`            
:ref:`bindEvent <no-18802>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-18803>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-18804>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-18805>`                   Makes this object topmost
:ref:`cancel <no-18806>`                         Ask the bizobj to cancel its changes.
:ref:`checkForUpdate <no-18807>`                 
:ref:`clear <no-18808>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-18809>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-18810>`                          This method will close the form. If force = False (default)
:ref:`closing <no-18811>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-18812>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-18813>`           Given a position relative to this control, return a position relative
:ref:`copy <no-18814>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-18815>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-18816>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-18817>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-18818>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-18819>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-18820>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-18821>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-18822>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-18823>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-18824>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-18825>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-18826>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-18827>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-18828>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-18829>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-18830>`                       Draws text on the object at the specified position
:ref:`endHover <no-18831>`                       
:ref:`fillPreferenceDialog <no-18832>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-18833>`                         Apply a filter to the bizobj's data.
:ref:`first <no-18834>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-18835>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-18836>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-18837>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-18838>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-18839>`              
:ref:`formCoordinates <no-18840>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-18841>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-18842>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-18843>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-18844>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-18845>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-18846>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-18847>`           Get the text to describe which record is current.
:ref:`getCurrentStyle <no-18848>`                
:ref:`getDisplayLocker <no-18849>`               Returns an object that locks the current display when created, and
:ref:`getDummyText <no-18850>`                   
:ref:`getMenu <no-18851>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-18852>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-18853>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-18854>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-18855>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-18856>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-18857>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-18858>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-18859>`                           Make the object invisible.
:ref:`initEvents <no-18860>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-18861>`                 
:ref:`isContainedBy <no-18862>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-18863>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-18864>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-18865>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-18866>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-18867>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-18868>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-18869>`                Move the record pointer to the specified row.
:ref:`new <no-18870>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-18871>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-18872>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-18873>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-18874>`                       
:ref:`onDelete <no-18875>`                       
:ref:`onEditRedo <no-18876>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-18877>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-18878>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-18879>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-18880>`                        
:ref:`onHover <no-18881>`                        
:ref:`onLast <no-18882>`                         
:ref:`onNew <no-18883>`                          
:ref:`onNext <no-18884>`                         
:ref:`onOpen <no-18885>`                         
:ref:`onPrior <no-18886>`                        
:ref:`onRequery <no-18887>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onSave <no-18888>`                         
:ref:`onSetBackColor <no-18889>`                 
:ref:`onSetFontFace <no-18890>`                  
:ref:`onSetFontSize <no-18891>`                  
:ref:`onSetForeColor <no-18892>`                 
:ref:`onTest <no-18893>`                         
:ref:`paste <no-18894>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-18895>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-18896>`                    
:ref:`prior <no-18897>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-18898>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-18899>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-18900>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-18901>`                     Raise the passed Dabo event.
:ref:`reCreate <no-18902>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-18903>`                       Recreate the object.
:ref:`redraw <no-18904>`                         Called when the object is (re)drawn.
:ref:`refresh <no-18905>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-18906>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-18907>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-18908>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-18909>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-18910>`              
:ref:`removeFilter <no-18911>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-18912>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-18913>`       
:ref:`requery <no-18914>`                        Ask the bizobj to requery.
:ref:`restoreSizeAndPosition <no-18915>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-18916>` 
:ref:`safeDestroy <no-18917>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-18918>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-18919>`            Save the current size and position of this form.
:ref:`sendToBack <no-18920>`                     Places this object behind all others.
:ref:`setAll <no-18921>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-18922>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-18923>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-18924>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-18925>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-18926>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-18927>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-18928>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-18929>`                  Set the status text to val.
:ref:`show <no-18930>`                           Make the object visible.
:ref:`showContainingPage <no-18931>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-18932>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-18933>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-18934>`                          This method used to call superclass code, but it's been removed.
:ref:`toggleStyle <no-18935>`                    
:ref:`unbindEvent <no-18936>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-18937>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-18938>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-18939>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-18940>`                         Updates the contained controls with current values from the source.
:ref:`updateSelection <no-18941>`                
:ref:`validateField <no-18942>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods
=======

.. _no-18773:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterInitAll(self)



-------

.. _no-18807:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.checkForUpdate(self, evt)



-------

.. _no-18848:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getCurrentStyle(self)



-------

.. _no-18850:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getDummyText(self)



-------

.. _no-18861:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.initProperties(self)



-------

.. _no-18885:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onOpen(self, evt)



-------

.. _no-18888:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onSave(self, evt)



-------

.. _no-18889:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onSetBackColor(self, evt)



-------

.. _no-18890:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onSetFontFace(self, evt)



-------

.. _no-18891:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onSetFontSize(self, evt)



-------

.. _no-18892:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onSetForeColor(self, evt)



-------

.. _no-18893:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onTest(self, evt)



-------

.. _no-18935:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.toggleStyle(self, evt)



-------

.. _no-18941:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.updateSelection(self, style=None)



-------


Methods - inherited
=====================

.. _no-18762:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18763:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18764:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18765:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-18766:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18767:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18768:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18769:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18770:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18771:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18772:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18774:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18775:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18776:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18777:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18778:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18779:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18780:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18781:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18782:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18783:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18784:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18785:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18786:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.autoBindEvents(self, force=True)
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

.. _no-18787:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18788:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18789:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18790:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18791:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18792:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18793:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18794:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18795:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18796:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18797:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18798:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18799:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18800:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18801:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18802:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18803:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18804:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-18805:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18806:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.cancel(self, dataSource=None, ignoreNoRecords=None)
   :noindex:


   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18808:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18809:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18810:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18811:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18812:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.confirmChanges(self, bizobjs=None)
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

.. _no-18813:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18814:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18815:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18816:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18817:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18818:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18819:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18820:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18821:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-18822:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18823:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18824:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18825:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18826:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18827:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18828:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18829:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18830:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18831:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18832:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18833:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18834:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18835:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18836:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18837:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18838:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18839:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18840:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18841:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18842:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18843:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getBizobjsToCheck(self)
   :noindex:


   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18844:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18845:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18846:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18847:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18849:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18851:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18852:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18853:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18854:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18855:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-18856:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18857:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18858:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18859:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18860:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18862:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18863:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18864:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18865:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18866:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.lockDisplay(self)
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

.. _no-18867:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18868:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18869:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18870:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18871:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18872:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18873:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18874:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onCancel(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18875:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onDelete(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18876:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18877:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18878:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18879:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18880:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18881:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18882:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18883:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onNew(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18884:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18886:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18887:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.onRequery(self, evt)
   :noindex:


   Occurs when an EVT_MENU event is received by this form.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18894:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18895:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18896:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18897:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18898:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18899:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18900:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18901:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18902:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18903:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18904:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18905:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.refresh(self, interval=None)
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

.. _no-18906:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18907:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18908:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18909:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18910:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18911:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18912:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18913:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18914:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.requery(self, dataSource=None)
   :noindex:


   Ask the bizobj to requery.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18915:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18916:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18917:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18918:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.save(self, dataSource=None)
   :noindex:


   Ask the bizobj to commit its changes to the backend.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18919:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18920:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18921:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-18922:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18923:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18924:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-18925:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-18926:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-18927:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18928:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18929:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18930:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18931:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18932:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18933:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-18934:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18936:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18937:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18938:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18939:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18940:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.update(self, interval=None)
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

.. _no-18942:

.. function:: dabo.ui.uiwx.dRichTextBox.RichTextTestForm.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
