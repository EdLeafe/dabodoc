
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.htmlAbout

.. _dabo.ui.dialogs.htmlAbout.HtmlAbout:

============================================
|doc_title|  **htmlAbout.HtmlAbout** - class
============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **HtmlAbout**

.. inheritance-diagram:: HtmlAbout


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dDialog`



|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.htmlAbout.HtmlAbout


|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`ActiveControl <no-7017>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-7018>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-7019>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-7020>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-7021>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-7022>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-7023>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-7024>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-7025>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-7026>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-7027>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-7028>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-7029>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-7030>`                      The position of the bottom side of the object. This is a
:ref:`Caption <no-7031>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-7032>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-7033>`                    Returns a list of object references to the children of
:ref:`Class <no-7034>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-7035>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-7036>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-7037>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-7038>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-7039>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-7040>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-7041>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-7042>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-7043>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-7044>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-7045>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-7046>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-7047>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-7048>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-7049>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-7050>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-7051>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-7052>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-7053>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-7054>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-7055>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-7056>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-7057>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-7058>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-7059>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-7060>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-7061>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-7062>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-7063>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-7064>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-7065>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-7066>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-7067>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-7068>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-7069>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-7070>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-7071>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-7072>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-7073>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-7074>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-7075>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-7076>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-7077>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-7078>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-7079>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-7080>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-7081>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-7082>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-7083>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-7084>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-7085>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-7086>`                    Specifies the font face. (str)
:ref:`FontInfo <no-7087>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-7088>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-7089>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-7090>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-7091>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-7092>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-7093>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-7094>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-7095>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-7096>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-7097>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-7098>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-7099>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-7100>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-7101>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-7102>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-7103>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-7104>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-7105>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-7106>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-7107>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-7108>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-7109>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-7110>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-7111>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-7112>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-7113>`                    Specifies the base name of the object.
:ref:`Parent <no-7114>`                      The containing object. (obj)
:ref:`Position <no-7115>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-7116>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-7117>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-7118>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-7119>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-7120>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-7121>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-7122>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-7123>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-7124>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-7125>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-7126>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-7127>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-7128>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-7129>`                        The size of the object. (tuple)
:ref:`Sizer <no-7130>`                       The sizer for the object.
:ref:`SizersToOutline <no-7131>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-7132>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-7133>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-7134>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-7135>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-7136>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-7137>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-7138>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-7139>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-7140>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-7141>`                         The top position of the object. (int)
:ref:`Transparency <no-7142>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-7143>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-7144>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-7145>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-7146>`                       The width of the object. (int)
:ref:`WindowHandle <no-7147>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-7148>`                 Specifies the current state of the form. (int)

============================================ ========================


Properties - inherited
========================

.. _no-7017:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7018:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7019:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7020:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7021:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7022:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7023:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7024:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7025:

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

.. _no-7026:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7027:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7028:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7029:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7030:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7031:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7032:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7033:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7034:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7035:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7036:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7037:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7038:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7039:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7040:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7041:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7042:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7043:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7044:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7045:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7046:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7047:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7048:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7049:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7050:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7051:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7052:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7053:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7054:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7055:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7056:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7057:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7058:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7059:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7060:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7061:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7062:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7063:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7064:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7065:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7066:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7067:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7068:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7069:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7070:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7071:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7072:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7073:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7074:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7075:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7076:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7077:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7078:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7079:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7080:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7081:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7082:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7083:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7084:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7085:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7086:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7087:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7088:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7089:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7090:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7091:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7092:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7093:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7094:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7095:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7096:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-7097:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7098:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7099:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7100:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7101:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7102:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7103:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7104:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7105:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7106:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7107:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7108:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7109:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7110:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7111:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7112:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7113:

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

.. _no-7114:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7115:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7116:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7117:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7118:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7119:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7120:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7121:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7122:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7123:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7124:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7125:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7126:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7127:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7128:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7129:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7130:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7131:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7132:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7133:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7134:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7135:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7136:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7137:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7138:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7139:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7140:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7141:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7142:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7143:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7144:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7145:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7146:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7147:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7148:

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


======================================= ========================
:ref:`Activate <no-7149>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-7150>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-7151>`              Occurs when a child control is created.
:ref:`Close <no-7152>`                  Occurs when the user closes the form.
:ref:`Create <no-7153>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-7154>`             Occurs when another form becomes active.
:ref:`Destroy <no-7155>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-7156>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-7157>`               Occurs when the control gets the focus.
:ref:`Idle <no-7158>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-7159>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-7160>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-7161>`               
:ref:`KeyUp <no-7162>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-7163>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-7164>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-7165>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-7166>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-7167>`             
:ref:`MouseLeave <no-7168>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-7169>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-7170>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-7171>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-7172>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-7173>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-7174>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-7175>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-7176>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-7177>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-7178>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-7179>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-7180>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-7181>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-7182>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-7183>`                   Occurs when the control's position changes.
:ref:`Paint <no-7184>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-7185>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-7186>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-7187>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-7188>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-7149:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-7150:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-7151:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-7152:

**Close** 

Occurs when the user closes the form.



-------

.. _no-7153:

**Create** 

Occurs after the control or form is created.



-------

.. _no-7154:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-7155:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-7156:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-7157:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-7158:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-7159:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-7160:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-7161:

**KeyEvent** 



-------

.. _no-7162:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-7163:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-7164:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-7165:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-7166:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-7167:

**MouseEvent** 



-------

.. _no-7168:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-7169:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-7170:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-7171:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-7172:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-7173:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-7174:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-7175:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-7176:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-7177:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-7178:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-7179:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-7180:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-7181:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-7182:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-7183:

**Move** 

Occurs when the control's position changes.



-------

.. _no-7184:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-7185:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-7186:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-7187:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-7188:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-7189>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-7190>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControls <no-7191>`                    
:ref:`addObject <no-7192>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-7193>`            
:ref:`afterAddControls <no-7194>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-7195>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-7196>`                   
:ref:`afterSetMenuBar <no-7197>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-7198>`             
:ref:`appendToolBarButton <no-7199>`            
:ref:`autoBindEvents <no-7200>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-7201>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-7202>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-7203>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-7204>`            
:ref:`bindEvent <no-7205>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-7206>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-7207>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-7208>`                   Makes this object topmost
:ref:`clear <no-7209>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-7210>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-7211>`                          This method will close the form. If force = False (default)
:ref:`closing <no-7212>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-7213>`           Given a position relative to this control, return a position relative
:ref:`copy <no-7214>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-7215>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-7216>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-7217>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-7218>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-7219>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-7220>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-7221>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-7222>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-7223>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-7224>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-7225>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-7226>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-7227>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-7228>`                       Draws text on the object at the specified position
:ref:`endHover <no-7229>`                       
:ref:`fillPreferenceDialog <no-7230>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-7231>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-7232>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-7233>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-7234>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-7235>`              
:ref:`formCoordinates <no-7236>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-7237>`                Return the fully qualified name of the object.
:ref:`getAppSpecificString <no-7238>`           
:ref:`getBizobj <no-7239>`                      
:ref:`getCaptureBitmap <no-7240>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-7241>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-7242>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-7243>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-7244>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-7245>`               Given a RegID value, this will return a reference to the
:ref:`getPageData <no-7246>`                    Basic Template structure of the About box.
:ref:`getPositionInSizer <no-7247>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-7248>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-7249>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-7250>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-7251>`                           Make the object invisible.
:ref:`initEvents <no-7252>`                     
:ref:`initProperties <no-7253>`                 
:ref:`isContainedBy <no-7254>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-7255>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-7256>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-7257>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-7258>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-7259>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-7260>`              Given a position relative to the form, return a position relative
:ref:`onClear <no-7261>`                        
:ref:`onCopyInfo <no-7262>`                     Copy the system information to the Clipboard
:ref:`onEditRedo <no-7263>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-7264>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-7265>`                        
:ref:`paste <no-7266>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-7267>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-7268>`                    
:ref:`processDroppedFiles <no-7269>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-7270>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-7271>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-7272>`                     Raise the passed Dabo event.
:ref:`reCreate <no-7273>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-7274>`                       Recreate the object.
:ref:`redraw <no-7275>`                         Called when the object is (re)drawn.
:ref:`refresh <no-7276>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-7277>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-7278>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-7279>`                        Need to augment this to make sure the dialog
:ref:`reload <no-7280>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-7281>`              
:ref:`removeFromOutlinedSizers <no-7282>`       
:ref:`restoreSizeAndPosition <no-7283>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-7284>` 
:ref:`safeDestroy <no-7285>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-7286>`            Save the current size and position of this form.
:ref:`sendToBack <no-7287>`                     Places this object behind all others.
:ref:`setAll <no-7288>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-7289>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-7290>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-7291>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-7292>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-7293>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-7294>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-7295>`                  Set the status text to val.
:ref:`show <no-7296>`                           
:ref:`showContainingPage <no-7297>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-7298>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-7299>`                      Show the dialog modally.
:ref:`showModeless <no-7300>`                   Show the dialog non-modally.
:ref:`super <no-7301>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-7302>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-7303>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-7304>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-7305>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-7306>`                         Update the properties of this object and all contained objects.
:ref:`writeHtmlPage <no-7307>`                  

=============================================== ========================


Methods
=======

.. _no-7191:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.addControls(self)



-------

.. _no-7238:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getAppSpecificString(self)



-------

.. _no-7246:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getPageData(self)

   Basic Template structure of the About box.



-------

.. _no-7252:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.initEvents(self)



-------

.. _no-7253:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.initProperties(self)



-------

.. _no-7261:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.onClear(self, evt)



-------

.. _no-7262:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.onCopyInfo(self, evt)

   Copy the system information to the Clipboard



-------

.. _no-7307:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.writeHtmlPage(self)



-------


Methods - inherited
=====================

.. _no-7189:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7190:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7192:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-7193:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7194:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7195:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7196:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7197:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7198:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7199:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7200:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.autoBindEvents(self, force=True)
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

.. _no-7201:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7202:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7203:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7204:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7205:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-7206:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-7207:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-7208:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7209:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7210:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7211:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7212:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7213:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7214:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7215:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7216:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7217:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7218:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7219:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-7220:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7221:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7222:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7223:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7224:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7225:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7226:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7227:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7228:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7229:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7230:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7231:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7232:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7233:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7234:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7235:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7236:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7237:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7239:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7240:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7241:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7242:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7243:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7244:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7245:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7247:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7248:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-7249:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7250:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7251:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7254:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7255:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7256:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7257:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.lockDisplay(self)
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

.. _no-7258:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7259:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7260:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7263:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7264:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7265:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7266:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7267:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7268:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7269:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7270:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7271:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7272:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7273:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7274:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7275:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7276:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.refresh(self, interval=None)
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

.. _no-7277:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7278:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7279:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7280:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7281:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7282:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7283:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7284:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7285:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7286:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7287:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7288:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-7289:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7290:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7291:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-7292:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-7293:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7294:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7295:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7296:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7297:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7298:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7299:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7300:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7301:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7302:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-7303:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7304:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7305:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7306:

.. function:: dabo.ui.dialogs.htmlAbout.HtmlAbout.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
