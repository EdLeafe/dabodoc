
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.HotKeyEditor

.. _dabo.ui.dialogs.HotKeyEditor.HotKeyEditor:

==================================================
|doc_title|  **HotKeyEditor.HotKeyEditor** - class
==================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **HotKeyEditor**

.. inheritance-diagram:: HotKeyEditor


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dOkCancelDialog`



|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor


|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Accepted <no-7308>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-7309>`               Contains a reference to the active control on the form, or None.
:ref:`Alt <no-7310>`                         Reflects the presence of the Alt key in the selected key combo. Default=False.  (bool)
:ref:`Application <no-7311>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-7312>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-7313>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-7314>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-7315>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-7316>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-7317>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-7318>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-7319>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-7320>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-7321>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-7322>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-7323>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-7324>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-7325>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-7326>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-7327>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-7328>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-7329>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Changed <no-7330>`                     Returns True only if the current key is different than the starting value. (read-only) (bool)
:ref:`Children <no-7331>`                    Returns a list of object references to the children of
:ref:`Class <no-7332>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-7333>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-7334>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-7335>`        Reference to the sizer item that control's this control's layout.
:ref:`Ctrl <no-7336>`                        Reflects the presence of the Ctrl key in the selected key combo. Default=False. (read-only) (bool)
:ref:`CxnName <no-7337>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-7338>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-7339>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-7340>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-7341>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-7342>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-7343>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-7344>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-7345>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-7346>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-7347>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-7348>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-7349>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-7350>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-7351>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-7352>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-7353>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-7354>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-7355>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-7356>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-7357>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-7358>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-7359>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-7360>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-7361>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-7362>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-7363>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-7364>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-7365>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-7366>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-7367>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-7368>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-7369>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-7370>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-7371>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-7372>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-7373>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-7374>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-7375>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-7376>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-7377>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-7378>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-7379>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-7380>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-7381>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-7382>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-7383>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-7384>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-7385>`                    Specifies the font face. (str)
:ref:`FontInfo <no-7386>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-7387>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-7388>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-7389>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-7390>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-7391>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-7392>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-7393>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-7394>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-7395>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-7396>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-7397>`         Controls how often the form is refreshed when idle.
:ref:`KeyChar <no-7398>`                     The non-modifier key in the selected key combo. Default=. (read-only) (str)
:ref:`KeyCode <no-7399>`                     Underlying key code of the key/modifier combo. Default=-1 (read-only) (int)
:ref:`KeyText <no-7400>`                     The displayed text for the key/modifier combo. Default= (read-only) (str)
:ref:`Left <no-7401>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-7402>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-7403>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-7404>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-7405>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-7406>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-7407>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-7408>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-7409>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-7410>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-7411>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-7412>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-7413>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-7414>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-7415>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-7416>`                    Specifies the base name of the object.
:ref:`NoButton <no-7417>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-7418>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-7419>`                      The containing object. (obj)
:ref:`Position <no-7420>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-7421>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-7422>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-7423>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-7424>`         Specifies whether the form's position and size as set by the user
:ref:`Shift <no-7425>`                       Reflects the presence of the Alt key in the selected key combo. Default=False. (read-only) (bool)
:ref:`ShowCaption <no-7426>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-7427>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-7428>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-7429>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-7430>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-7431>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-7432>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-7433>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-7434>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-7435>`                        The size of the object. (tuple)
:ref:`Sizer <no-7436>`                       The sizer for the object.
:ref:`SizersToOutline <no-7437>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-7438>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-7439>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-7440>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-7441>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-7442>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-7443>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-7444>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-7445>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-7446>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-7447>`                         The top position of the object. (int)
:ref:`Transparency <no-7448>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-7449>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-7450>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-7451>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-7452>`                       The width of the object. (int)
:ref:`WindowHandle <no-7453>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-7454>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-7455>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================ ========================


Properties
==========

.. _no-7310:

**Alt** 

Reflects the presence of the Alt key in the selected key combo. Default=False.  (bool)



-------

.. _no-7330:

**Changed** 

Returns True only if the current key is different than the starting value. (read-only) (bool)



-------

.. _no-7336:

**Ctrl** 

Reflects the presence of the Ctrl key in the selected key combo. Default=False. (read-only) (bool)



-------

.. _no-7398:

**KeyChar** 

The non-modifier key in the selected key combo. Default=. (read-only) (str)



-------

.. _no-7399:

**KeyCode** 

Underlying key code of the key/modifier combo. Default=-1 (read-only) (int)



-------

.. _no-7400:

**KeyText** 

The displayed text for the key/modifier combo. Default= (read-only) (str)



-------

.. _no-7425:

**Shift** 

Reflects the presence of the Alt key in the selected key combo. Default=False. (read-only) (bool)



-------


Properties - inherited
========================

.. _no-7308:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7309:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7311:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7312:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7313:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7314:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7315:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7316:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7317:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7318:

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

.. _no-7319:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7320:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7321:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7322:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7323:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7324:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7325:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7326:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7327:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7328:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7329:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7331:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7332:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7333:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7334:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7335:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7337:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7338:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7339:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7340:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7341:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7342:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7343:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7344:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7345:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7346:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7347:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7348:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7349:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7350:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7351:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7352:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7353:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7354:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7355:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7356:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7357:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7358:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7359:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7360:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7361:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7362:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7363:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7364:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7365:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7366:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7367:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7368:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7369:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7370:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7371:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7372:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7373:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7374:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7375:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7376:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7377:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7378:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7379:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7380:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7381:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7382:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7383:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7384:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7385:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7386:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7387:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7388:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7389:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7390:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7391:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7392:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7393:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7394:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7395:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7396:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-7397:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7401:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7402:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7403:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7404:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7405:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7406:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7407:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7408:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7409:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7410:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7411:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7412:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7413:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7414:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7415:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7416:

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

.. _no-7417:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7418:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7419:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7420:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7421:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7422:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7423:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7424:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7426:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7427:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7428:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7429:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7430:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7431:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7432:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7433:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7434:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7435:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7436:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-7437:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7438:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7439:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7440:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7441:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7442:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7443:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7444:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7445:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7446:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7447:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7448:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7449:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7450:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7451:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7452:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7453:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7454:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7455:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`Activate <no-7456>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-7457>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-7458>`              Occurs when a child control is created.
:ref:`Close <no-7459>`                  Occurs when the user closes the form.
:ref:`Create <no-7460>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-7461>`             Occurs when another form becomes active.
:ref:`Destroy <no-7462>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-7463>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-7464>`               Occurs when the control gets the focus.
:ref:`Idle <no-7465>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-7466>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-7467>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-7468>`               
:ref:`KeyUp <no-7469>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-7470>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-7471>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-7472>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-7473>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-7474>`             
:ref:`MouseLeave <no-7475>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-7476>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-7477>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-7478>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-7479>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-7480>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-7481>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-7482>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-7483>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-7484>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-7485>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-7486>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-7487>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-7488>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-7489>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-7490>`                   Occurs when the control's position changes.
:ref:`Paint <no-7491>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-7492>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-7493>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-7494>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-7495>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-7456:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-7457:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-7458:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-7459:

**Close** 

Occurs when the user closes the form.



-------

.. _no-7460:

**Create** 

Occurs after the control or form is created.



-------

.. _no-7461:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-7462:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-7463:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-7464:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-7465:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-7466:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-7467:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-7468:

**KeyEvent** 



-------

.. _no-7469:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-7470:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-7471:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-7472:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-7473:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-7474:

**MouseEvent** 



-------

.. _no-7475:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-7476:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-7477:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-7478:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-7479:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-7480:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-7481:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-7482:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-7483:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-7484:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-7485:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-7486:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-7487:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-7488:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-7489:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-7490:

**Move** 

Occurs when the control's position changes.



-------

.. _no-7491:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-7492:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-7493:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-7494:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-7495:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-7496>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-7497>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControlSequence <no-7498>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-7499>`                    
:ref:`addObject <no-7500>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-7501>`            
:ref:`afterAddControls <no-7502>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-7503>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-7504>`                   
:ref:`afterSetMenuBar <no-7505>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-7506>`             
:ref:`appendToolBarButton <no-7507>`            
:ref:`autoBindEvents <no-7508>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-7509>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-7510>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-7511>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-7512>`            
:ref:`bindEvent <no-7513>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-7514>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-7515>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-7516>`                   Makes this object topmost
:ref:`clear <no-7517>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-7518>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-7519>`                          This method will close the form. If force = False (default)
:ref:`closing <no-7520>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-7521>`           Given a position relative to this control, return a position relative
:ref:`copy <no-7522>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-7523>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-7524>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-7525>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-7526>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-7527>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-7528>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-7529>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-7530>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-7531>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-7532>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-7533>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-7534>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-7535>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-7536>`                       Draws text on the object at the specified position
:ref:`endHover <no-7537>`                       
:ref:`fillPreferenceDialog <no-7538>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-7539>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-7540>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-7541>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-7542>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-7543>`              
:ref:`formCoordinates <no-7544>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-7545>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-7546>`                      
:ref:`getCaptureBitmap <no-7547>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-7548>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-7549>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-7550>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-7551>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-7552>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-7553>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-7554>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-7555>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-7556>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-7557>`                           Make the object invisible.
:ref:`initEvents <no-7558>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-7559>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-7560>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-7561>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-7562>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-7563>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-7564>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-7565>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-7566>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-7567>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-7568>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-7569>`                        
:ref:`onKeyUp <no-7570>`                        
:ref:`paste <no-7571>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-7572>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-7573>`                    
:ref:`processDroppedFiles <no-7574>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-7575>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-7576>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-7577>`                     Raise the passed Dabo event.
:ref:`reCreate <no-7578>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-7579>`                       Recreate the object.
:ref:`redraw <no-7580>`                         Called when the object is (re)drawn.
:ref:`refresh <no-7581>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-7582>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-7583>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-7584>`                        Need to augment this to make sure the dialog
:ref:`reload <no-7585>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-7586>`              
:ref:`removeFromOutlinedSizers <no-7587>`       
:ref:`restoreSizeAndPosition <no-7588>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-7589>` 
:ref:`runCancel <no-7590>`                      
:ref:`runHelp <no-7591>`                        
:ref:`runNo <no-7592>`                          
:ref:`runOK <no-7593>`                          
:ref:`runYes <no-7594>`                         
:ref:`safeDestroy <no-7595>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-7596>`            Save the current size and position of this form.
:ref:`sendToBack <no-7597>`                     Places this object behind all others.
:ref:`setAll <no-7598>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-7599>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-7600>`                       Sets focus to the object.
:ref:`setKey <no-7601>`                         
:ref:`setPositionInSizer <no-7602>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-7603>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-7604>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-7605>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-7606>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-7607>`                  Set the status text to val.
:ref:`show <no-7608>`                           
:ref:`showContainingPage <no-7609>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-7610>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-7611>`                      Show the dialog modally.
:ref:`showModeless <no-7612>`                   Show the dialog non-modally.
:ref:`super <no-7613>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-7614>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-7615>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-7616>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-7617>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-7618>`                         Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-7499:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.addControls(self)



-------

.. _no-7570:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.onKeyUp(self, evt)



-------

.. _no-7601:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setKey(self, key)



-------


Methods - inherited
=====================

.. _no-7496:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7497:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7498:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.addControlSequence(self, seq)
   :noindex:


   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7500:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-7501:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7502:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7503:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7504:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7505:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7506:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7507:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7508:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.autoBindEvents(self, force=True)
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

.. _no-7509:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7510:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7511:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7512:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7513:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-7514:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-7515:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-7516:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7517:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7518:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7519:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7520:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7521:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7522:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7523:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7524:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7525:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7526:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7527:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-7528:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7529:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7530:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7531:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7532:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7533:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7534:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7535:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7536:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7537:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7538:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7539:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7540:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7541:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7542:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7543:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7544:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7545:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7546:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7547:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7548:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7549:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7550:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7551:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7552:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7553:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7554:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-7555:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7556:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7557:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7558:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7559:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7560:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7561:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7562:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7563:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.lockDisplay(self)
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

.. _no-7564:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7565:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7566:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7567:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7568:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7569:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7571:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7572:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7573:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7574:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7575:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7576:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7577:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7578:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-7579:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7580:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7581:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.refresh(self, interval=None)
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

.. _no-7582:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7583:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7584:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7585:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7586:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7587:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7588:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7589:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7590:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.runCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7591:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.runHelp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7592:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.runNo(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7593:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.runOK(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7594:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.runYes(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7595:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7596:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7597:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7598:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-7599:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setEscapeButton(self, btn=None)
   :noindex:


   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-7600:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7602:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7603:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-7604:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-7605:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7606:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7607:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-7608:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7609:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7610:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7611:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7612:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-7613:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-7614:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-7615:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7616:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7617:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-7618:

.. function:: dabo.ui.dialogs.HotKeyEditor.HotKeyEditor.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
