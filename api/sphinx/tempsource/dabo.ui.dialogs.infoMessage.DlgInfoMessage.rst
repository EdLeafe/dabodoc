
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.infoMessage

.. _dabo.ui.dialogs.infoMessage.DlgInfoMessage:

===================================================
|doc_title|  **infoMessage.DlgInfoMessage** - class
===================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **DlgInfoMessage**

.. inheritance-diagram:: DlgInfoMessage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`



|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.infoMessage.DlgInfoMessage


|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Accepted <no-7923>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-7924>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-7925>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-7926>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-7927>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-7928>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-7929>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-7930>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-7931>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-7932>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-7933>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-7934>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-7935>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-7936>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-7937>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-7938>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-7939>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-7940>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-7941>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-7942>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-7943>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-7944>`                    Returns a list of object references to the children of
:ref:`Class <no-7945>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-7946>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-7947>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-7948>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-7949>`                     Name of the connection used for data access  (str)
:ref:`DefaultShowInFuture <no-7950>`         Specifies whether the 'show in future' checkbox is checked by default.
:ref:`DroppedFileHandler <no-7951>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-7952>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-7953>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-7954>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-7955>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-7956>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-7957>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-7958>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-7959>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-7960>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-7961>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-7962>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-7963>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-7964>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-7965>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-7966>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-7967>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-7968>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-7969>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-7970>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-7971>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-7972>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-7973>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-7974>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-7975>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-7976>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-7977>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-7978>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-7979>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-7980>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-7981>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-7982>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-7983>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-7984>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-7985>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-7986>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-7987>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-7988>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-7989>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-7990>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-7991>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-7992>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-7993>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-7994>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-7995>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-7996>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-7997>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-7998>`                    Specifies the font face. (str)
:ref:`FontInfo <no-7999>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-8000>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-8001>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-8002>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-8003>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-8004>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-8005>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-8006>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-8007>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-8008>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-8009>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-8010>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-8011>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-8012>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-8013>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-8014>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-8015>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-8016>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-8017>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-8018>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-8019>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`Message <no-8020>`                     Specifies the message to display.
:ref:`MinimumHeight <no-8021>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-8022>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-8023>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-8024>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-8025>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-8026>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-8027>`                    Specifies the base name of the object.
:ref:`NoButton <no-8028>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-8029>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-8030>`                      The containing object. (obj)
:ref:`Position <no-8031>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-8032>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-8033>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-8034>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-8035>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-8036>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-8037>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-8038>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-8039>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-8040>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-8041>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-8042>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-8043>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-8044>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-8045>`                        The size of the object. (tuple)
:ref:`Sizer <no-8046>`                       The sizer for the object.
:ref:`SizersToOutline <no-8047>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-8048>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-8049>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-8050>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-8051>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-8052>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-8053>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-8054>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-8055>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-8056>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-8057>`                         The top position of the object. (int)
:ref:`Transparency <no-8058>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-8059>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-8060>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-8061>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-8062>`                       The width of the object. (int)
:ref:`WindowHandle <no-8063>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-8064>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-8065>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================ ========================


Properties
==========

.. _no-7950:

**DefaultShowInFuture** 

Specifies whether the 'show in future' checkbox is checked by default.



-------

.. _no-8020:

**Message** 

Specifies the message to display.



-------


Properties - inherited
========================

.. _no-7923:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7924:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7925:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7926:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7927:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7928:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7929:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7930:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7931:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7932:

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

.. _no-7933:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7934:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7935:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7936:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7937:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7938:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7939:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7940:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7941:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7942:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7943:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7944:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7945:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7946:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7947:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7948:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7949:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7951:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7952:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7953:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7954:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7955:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7956:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7957:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7958:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7959:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7960:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7961:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7962:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7963:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7964:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7965:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7966:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7967:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7968:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7969:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7970:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7971:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7972:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7973:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7974:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7975:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7976:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7977:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7978:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7979:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7980:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7981:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7982:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7983:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7984:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7985:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7986:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7987:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7988:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7989:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7990:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7991:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7992:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7993:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7994:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7995:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7996:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7997:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7998:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7999:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8000:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8001:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8002:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8003:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8004:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8005:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8006:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8007:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8008:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8009:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-8010:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8011:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8012:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8013:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8014:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8015:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8016:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8017:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8018:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8019:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8021:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8022:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8023:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8024:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8025:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8026:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8027:

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

.. _no-8028:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8029:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8030:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8031:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8032:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8033:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8034:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8035:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8036:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8037:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8038:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8039:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8040:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8041:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8042:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8043:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8044:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8045:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8046:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8047:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8048:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8049:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8050:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8051:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8052:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8053:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8054:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8055:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8056:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8057:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8058:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8059:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8060:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8061:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8062:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8063:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8064:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8065:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`Activate <no-8066>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-8067>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-8068>`              Occurs when a child control is created.
:ref:`Close <no-8069>`                  Occurs when the user closes the form.
:ref:`Create <no-8070>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-8071>`             Occurs when another form becomes active.
:ref:`Destroy <no-8072>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-8073>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-8074>`               Occurs when the control gets the focus.
:ref:`Idle <no-8075>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-8076>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-8077>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-8078>`               
:ref:`KeyUp <no-8079>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-8080>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-8081>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-8082>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-8083>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-8084>`             
:ref:`MouseLeave <no-8085>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-8086>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-8087>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-8088>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-8089>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-8090>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-8091>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-8092>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-8093>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-8094>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-8095>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-8096>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-8097>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-8098>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-8099>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-8100>`                   Occurs when the control's position changes.
:ref:`Paint <no-8101>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-8102>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-8103>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-8104>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-8105>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-8066:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-8067:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-8068:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-8069:

**Close** 

Occurs when the user closes the form.



-------

.. _no-8070:

**Create** 

Occurs after the control or form is created.



-------

.. _no-8071:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-8072:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-8073:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-8074:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-8075:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-8076:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-8077:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-8078:

**KeyEvent** 



-------

.. _no-8079:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-8080:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-8081:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-8082:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-8083:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-8084:

**MouseEvent** 



-------

.. _no-8085:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-8086:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-8087:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-8088:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-8089:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-8090:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-8091:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-8092:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-8093:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-8094:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-8095:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-8096:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-8097:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-8098:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-8099:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-8100:

**Move** 

Occurs when the control's position changes.



-------

.. _no-8101:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-8102:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-8103:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-8104:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-8105:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-8106>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-8107>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControlSequence <no-8108>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-8109>`                    
:ref:`addObject <no-8110>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-8111>`            
:ref:`afterAddControls <no-8112>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-8113>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-8114>`                   
:ref:`afterSetMenuBar <no-8115>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-8116>`             
:ref:`appendToolBarButton <no-8117>`            
:ref:`autoBindEvents <no-8118>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-8119>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-8120>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-8121>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-8122>`            
:ref:`bindEvent <no-8123>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-8124>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-8125>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-8126>`                   Makes this object topmost
:ref:`clear <no-8127>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-8128>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-8129>`                          This method will close the form. If force = False (default)
:ref:`closing <no-8130>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-8131>`           Given a position relative to this control, return a position relative
:ref:`copy <no-8132>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-8133>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-8134>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-8135>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-8136>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-8137>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-8138>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-8139>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-8140>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-8141>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-8142>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-8143>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-8144>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-8145>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-8146>`                       Draws text on the object at the specified position
:ref:`endHover <no-8147>`                       
:ref:`fillPreferenceDialog <no-8148>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-8149>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-8150>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-8151>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-8152>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-8153>`              
:ref:`formCoordinates <no-8154>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-8155>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-8156>`                      
:ref:`getCaptureBitmap <no-8157>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-8158>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-8159>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-8160>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-8161>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-8162>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-8163>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-8164>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-8165>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-8166>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-8167>`                           Make the object invisible.
:ref:`initEvents <no-8168>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-8169>`                 
:ref:`isContainedBy <no-8170>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-8171>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-8172>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-8173>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-8174>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-8175>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-8176>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-8177>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-8178>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-8179>`                        
:ref:`paste <no-8180>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-8181>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-8182>`                    
:ref:`processDroppedFiles <no-8183>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-8184>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-8185>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-8186>`                     Raise the passed Dabo event.
:ref:`reCreate <no-8187>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-8188>`                       Recreate the object.
:ref:`redraw <no-8189>`                         Called when the object is (re)drawn.
:ref:`refresh <no-8190>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-8191>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-8192>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-8193>`                        Need to augment this to make sure the dialog
:ref:`reload <no-8194>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-8195>`              
:ref:`removeFromOutlinedSizers <no-8196>`       
:ref:`restoreSizeAndPosition <no-8197>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-8198>` 
:ref:`runCancel <no-8199>`                      
:ref:`runHelp <no-8200>`                        
:ref:`runNo <no-8201>`                          
:ref:`runOK <no-8202>`                          
:ref:`runYes <no-8203>`                         
:ref:`safeDestroy <no-8204>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-8205>`            Save the current size and position of this form.
:ref:`sendToBack <no-8206>`                     Places this object behind all others.
:ref:`setAll <no-8207>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-8208>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-8209>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-8210>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-8211>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-8212>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-8213>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-8214>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-8215>`                  Set the status text to val.
:ref:`show <no-8216>`                           
:ref:`showContainingPage <no-8217>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-8218>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-8219>`                      Show the dialog modally.
:ref:`showModeless <no-8220>`                   Show the dialog non-modally.
:ref:`super <no-8221>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-8222>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-8223>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-8224>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-8225>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-8226>`                         Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-8109:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.addControls(self)



-------

.. _no-8169:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.initProperties(self)



-------


Methods - inherited
=====================

.. _no-8106:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8107:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8108:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.addControlSequence(self, seq)
   :noindex:


   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8110:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-8111:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8112:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8113:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8114:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8115:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8116:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8117:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8118:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.autoBindEvents(self, force=True)
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

.. _no-8119:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8120:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8121:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8122:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8123:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-8124:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-8125:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-8126:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8127:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8128:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8129:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8130:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8131:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8132:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8133:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8134:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8135:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8136:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8137:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-8138:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8139:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8140:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8141:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8142:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8143:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8144:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8145:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8146:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8147:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8148:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8149:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8150:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8151:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8152:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8153:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8154:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8155:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8156:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8157:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8158:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8159:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8160:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8161:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8162:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8163:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8164:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-8165:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8166:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8167:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8168:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8170:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8171:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8172:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8173:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.lockDisplay(self)
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

.. _no-8174:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8175:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8176:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8177:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8178:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8179:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8180:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8181:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8182:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8183:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8184:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8185:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8186:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8187:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8188:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8189:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8190:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.refresh(self, interval=None)
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

.. _no-8191:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8192:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8193:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8194:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8195:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8196:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8197:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8198:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8199:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.runCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8200:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.runHelp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8201:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.runNo(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8202:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.runOK(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8203:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.runYes(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8204:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8205:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8206:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8207:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-8208:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setEscapeButton(self, btn=None)
   :noindex:


   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8209:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8210:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8211:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-8212:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-8213:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8214:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8215:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8216:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8217:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8218:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8219:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8220:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8221:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8222:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-8223:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8224:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8225:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8226:

.. function:: dabo.ui.dialogs.infoMessage.DlgInfoMessage.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
