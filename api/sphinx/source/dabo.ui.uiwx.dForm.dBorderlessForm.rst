
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dForm

.. _dabo.ui.uiwx.dForm.dBorderlessForm:

==============================================
|doc_title|  **dForm.dBorderlessForm** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBorderlessForm**

.. inheritance-diagram:: dBorderlessForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dForm.BaseForm`



|subclasses| Known Subclasses
=============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dForm.dBorderlessForm

   .. automethod:: dabo.ui.uiwx.dForm.dBorderlessForm.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-27185>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-27186>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-27187>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-27188>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-27189>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-27190>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-27191>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-27192>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-27193>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-27194>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-27195>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-27196>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-27197>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-27198>`                     The caption of the object. (str)
:ref:`Centered <no-27199>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-27200>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-27201>`                    Returns a list of object references to the children of
:ref:`Class <no-27202>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-27203>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-27204>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-27205>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-27206>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-27207>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-27208>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-27209>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-27210>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-27211>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-27212>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-27213>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-27214>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-27215>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-27216>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-27217>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-27218>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-27219>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-27220>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-27221>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-27222>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-27223>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-27224>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-27225>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-27226>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-27227>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-27228>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-27229>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-27230>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-27231>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-27232>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-27233>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-27234>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-27235>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-27236>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-27237>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-27238>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-27239>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-27240>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-27241>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-27242>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-27243>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-27244>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-27245>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-27246>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-27247>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-27248>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-27249>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-27250>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-27251>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-27252>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-27253>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-27254>`                    Specifies the font face. (str)
:ref:`FontInfo <no-27255>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-27256>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-27257>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-27258>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-27259>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-27260>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-27261>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-27262>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-27263>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-27264>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-27265>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-27266>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-27267>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-27268>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-27269>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-27270>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-27271>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-27272>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-27273>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-27274>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-27275>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-27276>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-27277>`                Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-27278>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-27279>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-27280>`                    Specifies the base name of the object.
:ref:`Parent <no-27281>`                      The containing object. (obj)
:ref:`Position <no-27282>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-27283>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-27284>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-27285>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-27286>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-27287>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-27288>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SaveAllRows <no-27289>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-27290>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-27291>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-27292>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-27293>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-27294>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-27295>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-27296>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-27297>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-27298>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-27299>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-27300>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-27301>`                        The size of the object. (tuple)
:ref:`Sizer <no-27302>`                       The sizer for the object.
:ref:`SizersToOutline <no-27303>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-27304>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-27305>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-27306>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-27307>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-27308>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-27309>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-27310>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-27311>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-27312>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-27313>`                         The top position of the object. (int)
:ref:`Transparency <no-27314>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-27315>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-27316>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-27317>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-27318>`                       The width of the object. (int)
:ref:`WindowHandle <no-27319>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-27320>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties - inherited
========================

.. _no-27185:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27186:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27187:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27188:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27189:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27190:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27191:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27192:

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

.. _no-27193:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27194:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27195:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27196:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27197:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27198:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27199:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27200:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27201:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27202:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27203:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27204:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27205:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27206:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27207:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27208:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27209:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27210:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27211:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27212:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27213:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27214:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27215:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27216:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27217:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27218:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27219:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27220:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27221:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27222:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27223:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27224:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27225:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27226:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27227:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27228:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27229:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27230:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27231:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27232:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27233:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27234:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27235:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27236:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27237:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27238:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27239:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27240:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27241:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27242:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27243:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27244:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27245:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27246:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27247:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27248:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27249:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27250:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27251:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27252:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27253:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27254:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27255:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27256:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27257:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27258:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27259:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27260:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27261:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27262:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27263:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27264:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-27265:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27266:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27267:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27268:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27269:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27270:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27271:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27272:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27273:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27274:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27275:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27276:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27277:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27278:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27279:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27280:

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

.. _no-27281:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27282:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27283:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27284:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27285:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27286:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27287:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27288:

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

.. _no-27289:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27290:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27291:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27292:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27293:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27294:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27295:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27296:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27297:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27298:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27299:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27300:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27301:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27302:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27303:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27304:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27305:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27306:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27307:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27308:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27309:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27310:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27311:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27312:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27313:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27314:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27315:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27316:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27317:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27318:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27319:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27320:

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
:ref:`BackgroundErased <no-27321>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-27322>`                 Occurs after the control or form is created.
:ref:`Destroy <no-27323>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-27324>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-27325>`               Occurs when the control gets the focus.
:ref:`Idle <no-27326>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-27327>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-27328>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-27329>`               
:ref:`KeyUp <no-27330>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-27331>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-27332>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-27333>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-27334>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-27335>`             
:ref:`MouseLeave <no-27336>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-27337>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-27338>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-27339>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-27340>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-27341>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-27342>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-27343>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-27344>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-27345>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-27346>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-27347>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-27348>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-27349>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-27350>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-27351>`                   Occurs when the control's position changes.
:ref:`Paint <no-27352>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-27353>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-27354>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-27355>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-27356>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-27321:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-27322:

**Create** 

Occurs after the control or form is created.



-------

.. _no-27323:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-27324:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-27325:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-27326:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-27327:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-27328:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-27329:

**KeyEvent** 



-------

.. _no-27330:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-27331:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-27332:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-27333:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-27334:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-27335:

**MouseEvent** 



-------

.. _no-27336:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-27337:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-27338:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-27339:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-27340:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-27341:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-27342:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-27343:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-27344:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-27345:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-27346:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-27347:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-27348:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-27349:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-27350:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-27351:

**Move** 

Occurs when the control's position changes.



-------

.. _no-27352:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-27353:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-27354:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-27355:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-27356:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-27357>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-27358>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-27359>`                      Add a bizobj to this form.
:ref:`addObject <no-27360>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-27361>`            
:ref:`afterCancel <no-27362>`                    
:ref:`afterDelete <no-27363>`                    
:ref:`afterDeleteAll <no-27364>`                 
:ref:`afterFilter <no-27365>`                    
:ref:`afterFirst <no-27366>`                     
:ref:`afterInit <no-27367>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-27368>`                   
:ref:`afterLast <no-27369>`                      
:ref:`afterNew <no-27370>`                       
:ref:`afterNext <no-27371>`                      
:ref:`afterPointerMove <no-27372>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-27373>`                     
:ref:`afterRequery <no-27374>`                   
:ref:`afterRowNavigation <no-27375>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-27376>`                      
:ref:`afterSetMenuBar <no-27377>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-27378>`          Subclass hook.
:ref:`afterSetProperties <no-27379>`             
:ref:`appendToolBarButton <no-27380>`            
:ref:`autoBindEvents <no-27381>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-27382>`                   
:ref:`beforeClose <no-27383>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-27384>`                   
:ref:`beforeDeleteAll <no-27385>`                
:ref:`beforeFilter <no-27386>`                   
:ref:`beforeFirst <no-27387>`                    
:ref:`beforeInit <no-27388>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-27389>`                     
:ref:`beforeNew <no-27390>`                      
:ref:`beforeNext <no-27391>`                     
:ref:`beforePointerMove <no-27392>`              
:ref:`beforePrior <no-27393>`                    
:ref:`beforeRequery <no-27394>`                  
:ref:`beforeSave <no-27395>`                     
:ref:`beforeSetProperties <no-27396>`            
:ref:`bindEvent <no-27397>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-27398>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-27399>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-27400>`                   Makes this object topmost
:ref:`cancel <no-27401>`                         Ask the bizobj to cancel its changes.
:ref:`clear <no-27402>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-27403>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-27404>`                          This method will close the form. If force = False (default)
:ref:`closing <no-27405>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-27406>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-27407>`           Given a position relative to this control, return a position relative
:ref:`copy <no-27408>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-27409>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-27410>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-27411>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-27412>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-27413>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-27414>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-27415>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-27416>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-27417>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-27418>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-27419>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-27420>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-27421>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-27422>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-27423>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-27424>`                       Draws text on the object at the specified position
:ref:`endHover <no-27425>`                       
:ref:`fillPreferenceDialog <no-27426>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-27427>`                         Apply a filter to the bizobj's data.
:ref:`first <no-27428>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-27429>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-27430>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-27431>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-27432>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-27433>`              
:ref:`formCoordinates <no-27434>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-27435>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-27436>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-27437>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-27438>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-27439>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-27440>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-27441>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-27442>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-27443>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-27444>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-27445>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-27446>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-27447>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-27448>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-27449>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-27450>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-27451>`                           Make the object invisible.
:ref:`initEvents <no-27452>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-27453>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-27454>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-27455>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-27456>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-27457>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-27458>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-27459>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-27460>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-27461>`                Move the record pointer to the specified row.
:ref:`new <no-27462>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-27463>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-27464>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-27465>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-27466>`                       
:ref:`onDelete <no-27467>`                       
:ref:`onEditRedo <no-27468>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-27469>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-27470>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-27471>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-27472>`                        
:ref:`onHover <no-27473>`                        
:ref:`onLast <no-27474>`                         
:ref:`onNew <no-27475>`                          
:ref:`onNext <no-27476>`                         
:ref:`onPrior <no-27477>`                        
:ref:`onRequery <no-27478>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onSave <no-27479>`                         
:ref:`paste <no-27480>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-27481>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-27482>`                    
:ref:`prior <no-27483>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-27484>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-27485>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-27486>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-27487>`                     Raise the passed Dabo event.
:ref:`reCreate <no-27488>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-27489>`                       Recreate the object.
:ref:`redraw <no-27490>`                         Called when the object is (re)drawn.
:ref:`refresh <no-27491>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-27492>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-27493>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-27494>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-27495>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-27496>`              
:ref:`removeFilter <no-27497>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-27498>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-27499>`       
:ref:`requery <no-27500>`                        Ask the bizobj to requery.
:ref:`restoreSizeAndPosition <no-27501>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-27502>` 
:ref:`safeDestroy <no-27503>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-27504>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-27505>`            Save the current size and position of this form.
:ref:`sendToBack <no-27506>`                     Places this object behind all others.
:ref:`setAll <no-27507>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-27508>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-27509>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-27510>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-27511>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-27512>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-27513>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-27514>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-27515>`                  Set the status text to val.
:ref:`show <no-27516>`                           Make the object visible.
:ref:`showContainingPage <no-27517>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-27518>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-27519>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-27520>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-27521>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-27522>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-27523>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-27524>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-27525>`                         Updates the contained controls with current values from the source.
:ref:`validateField <no-27526>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods - inherited
=====================

.. _no-27357:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27358:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27359:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27360:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-27361:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27362:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27363:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27364:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27365:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27366:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27367:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27368:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27369:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27370:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27371:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27372:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27373:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27374:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27375:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27376:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27377:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27378:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27379:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27380:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27381:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.autoBindEvents(self, force=True)
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

.. _no-27382:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27383:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27384:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27385:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27386:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27387:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27388:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27389:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27390:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27391:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27392:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27393:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27394:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27395:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27396:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27397:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27398:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27399:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-27400:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27401:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.cancel(self, dataSource=None, ignoreNoRecords=None)
   :noindex:


   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27402:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27403:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27404:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27405:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27406:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.confirmChanges(self, bizobjs=None)
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

.. _no-27407:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27408:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27409:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27410:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27411:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27412:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27413:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27414:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27415:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-27416:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27417:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27418:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27419:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27420:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27421:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27422:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27423:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27424:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27425:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27426:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27427:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27428:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27429:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27430:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27431:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27432:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27433:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27434:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27435:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27436:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27437:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getBizobjsToCheck(self)
   :noindex:


   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27438:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27439:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27440:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27441:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27442:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27443:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27444:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27445:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27446:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27447:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-27448:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27449:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27450:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27451:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27452:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27453:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27454:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27455:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27456:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27457:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27458:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.lockDisplay(self)
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

.. _no-27459:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27460:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27461:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27462:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27463:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27464:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27465:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27466:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onCancel(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27467:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onDelete(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27468:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27469:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27470:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27471:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27472:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27473:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27474:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27475:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onNew(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27476:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27477:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27478:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onRequery(self, evt)
   :noindex:


   Occurs when an EVT_MENU event is received by this form.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27479:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.onSave(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27480:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27481:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27482:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27483:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27484:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27485:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27486:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27487:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27488:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27489:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27490:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27491:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.refresh(self, interval=None)
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

.. _no-27492:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27493:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27494:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27495:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27496:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27497:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27498:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27499:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27500:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.requery(self, dataSource=None)
   :noindex:


   Ask the bizobj to requery.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27501:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27502:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27503:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27504:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.save(self, dataSource=None)
   :noindex:


   Ask the bizobj to commit its changes to the backend.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27505:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27506:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27507:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-27508:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27509:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27510:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-27511:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-27512:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27513:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27514:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27515:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27516:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27517:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27518:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27519:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27520:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27521:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27522:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27523:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27524:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27525:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.update(self, interval=None)
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

.. _no-27526:

.. function:: dabo.ui.uiwx.dForm.dBorderlessForm.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
