
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDialog

.. _dabo.ui.uiwx.dDialog.dStandardButtonDialog:

======================================================
|doc_title|  **dDialog.dStandardButtonDialog** - class
======================================================


Creates a dialog with standard buttons and associated functionality. You can
choose the buttons that display by passing True for any of the following
properties:

OK
Cancel
Yes
No
Help

If you don't specify buttons, only the OK will be included; if you do specify buttons,
you must specify them all; in other words, OK is only assumed if nothing is specified.
Then add your custom controls in the addControls() hook method, and respond to
the pressing of the standard buttons in the run*() handlers, where * is the name of the
associated property (e.g., runOK(), runNo(), etc.). You can query the Accepted property
to find out if the user pressed "OK" or "Yes"; if neither of these was pressed,
Accepted will be False.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dStandardButtonDialog**

.. inheritance-diagram:: dStandardButtonDialog


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dDialog`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.dialogs.infoMessage.DlgInfoMessage`
* :ref:`dabo.ui.uiwx.dDialog.dOkCancelDialog`
* :ref:`dabo.ui.uiwx.dDialog.dYesNoDialog`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDialog.dStandardButtonDialog

   .. automethod:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`Accepted <no-15030>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-15031>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-15032>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-15033>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-15034>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-15035>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-15036>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-15037>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-15038>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-15039>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-15040>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-15041>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-15042>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-15043>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-15044>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-15045>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-15046>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-15047>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-15048>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-15049>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-15050>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-15051>`                    Returns a list of object references to the children of
:ref:`Class <no-15052>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-15053>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-15054>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-15055>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-15056>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-15057>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-15058>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-15059>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-15060>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-15061>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-15062>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-15063>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-15064>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-15065>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-15066>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-15067>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-15068>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-15069>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-15070>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-15071>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-15072>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-15073>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-15074>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-15075>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-15076>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-15077>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-15078>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-15079>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-15080>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-15081>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-15082>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-15083>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-15084>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-15085>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-15086>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-15087>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-15088>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-15089>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-15090>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-15091>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-15092>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-15093>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-15094>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-15095>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-15096>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-15097>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-15098>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-15099>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-15100>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-15101>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-15102>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-15103>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-15104>`                    Specifies the font face. (str)
:ref:`FontInfo <no-15105>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-15106>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-15107>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-15108>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-15109>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-15110>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-15111>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-15112>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-15113>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-15114>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-15115>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-15116>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-15117>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-15118>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-15119>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-15120>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-15121>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-15122>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-15123>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-15124>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-15125>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-15126>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-15127>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-15128>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-15129>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-15130>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-15131>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-15132>`                    Specifies the base name of the object.
:ref:`NoButton <no-15133>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-15134>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-15135>`                      The containing object. (obj)
:ref:`Position <no-15136>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-15137>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-15138>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-15139>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-15140>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-15141>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-15142>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-15143>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-15144>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-15145>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-15146>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-15147>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-15148>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-15149>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-15150>`                        The size of the object. (tuple)
:ref:`Sizer <no-15151>`                       The sizer for the object.
:ref:`SizersToOutline <no-15152>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-15153>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-15154>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-15155>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-15156>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-15157>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-15158>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-15159>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-15160>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-15161>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-15162>`                         The top position of the object. (int)
:ref:`Transparency <no-15163>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-15164>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-15165>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-15166>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-15167>`                       The width of the object. (int)
:ref:`WindowHandle <no-15168>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-15169>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-15170>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================= ========================


Properties
==========

.. _no-15030:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)



-------

.. _no-15045:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)



-------

.. _no-15046:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)



-------

.. _no-15047:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).



-------

.. _no-15048:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)



-------

.. _no-15112:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).



-------

.. _no-15133:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).



-------

.. _no-15134:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).



-------

.. _no-15170:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).



-------


Properties - inherited
========================

.. _no-15031:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15032:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15033:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15034:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15035:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15036:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15037:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15038:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15039:

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

.. _no-15040:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15041:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15042:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15043:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15044:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15049:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15050:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15051:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15052:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15053:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15054:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15055:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15056:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15057:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15058:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15059:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15060:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15061:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15062:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15063:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15064:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15065:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15066:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15067:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15068:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15069:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15070:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15071:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15072:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15073:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15074:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15075:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15076:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15077:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15078:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15079:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15080:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15081:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15082:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15083:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15084:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15085:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15086:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15087:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15088:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15089:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15090:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15091:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15092:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15093:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15094:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15095:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15096:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15097:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15098:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15099:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15100:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15101:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15102:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15103:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15104:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15105:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15106:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15107:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15108:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15109:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15110:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15111:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15113:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15114:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15115:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-15116:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15117:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15118:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15119:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15120:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15121:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15122:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15123:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15124:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15125:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15126:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15127:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15128:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15129:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15130:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15131:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15132:

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

.. _no-15135:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15136:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15137:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15138:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15139:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15140:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15141:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15142:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15143:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15144:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15145:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15146:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15147:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15148:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15149:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15150:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15151:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15152:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15153:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15154:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15155:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15156:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15157:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15158:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15159:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15160:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15161:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15162:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15163:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15164:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15165:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15166:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15167:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15168:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15169:

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
:ref:`Activate <no-15171>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-15172>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-15173>`              Occurs when a child control is created.
:ref:`Close <no-15174>`                  Occurs when the user closes the form.
:ref:`Create <no-15175>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-15176>`             Occurs when another form becomes active.
:ref:`Destroy <no-15177>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-15178>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-15179>`               Occurs when the control gets the focus.
:ref:`Idle <no-15180>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-15181>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-15182>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-15183>`               
:ref:`KeyUp <no-15184>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-15185>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-15186>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-15187>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-15188>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-15189>`             
:ref:`MouseLeave <no-15190>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-15191>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-15192>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-15193>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-15194>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-15195>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-15196>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-15197>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-15198>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-15199>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-15200>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-15201>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-15202>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-15203>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-15204>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-15205>`                   Occurs when the control's position changes.
:ref:`Paint <no-15206>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-15207>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-15208>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-15209>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-15210>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-15171:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-15172:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-15173:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-15174:

**Close** 

Occurs when the user closes the form.



-------

.. _no-15175:

**Create** 

Occurs after the control or form is created.



-------

.. _no-15176:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-15177:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-15178:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-15179:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-15180:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-15181:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-15182:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-15183:

**KeyEvent** 



-------

.. _no-15184:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-15185:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-15186:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-15187:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-15188:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-15189:

**MouseEvent** 



-------

.. _no-15190:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-15191:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-15192:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-15193:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-15194:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-15195:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-15196:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-15197:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-15198:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-15199:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-15200:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-15201:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-15202:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-15203:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-15204:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-15205:

**Move** 

Occurs when the control's position changes.



-------

.. _no-15206:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-15207:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-15208:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-15209:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-15210:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-15211>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-15212>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControlSequence <no-15213>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-15214>`                    Use this method to add controls to the dialog. The standard buttons will be added
:ref:`addObject <no-15215>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-15216>`            
:ref:`afterAddControls <no-15217>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-15218>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-15219>`                   
:ref:`afterSetMenuBar <no-15220>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-15221>`             
:ref:`appendToolBarButton <no-15222>`            
:ref:`autoBindEvents <no-15223>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-15224>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-15225>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-15226>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-15227>`            
:ref:`bindEvent <no-15228>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-15229>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-15230>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-15231>`                   Makes this object topmost
:ref:`clear <no-15232>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-15233>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-15234>`                          This method will close the form. If force = False (default)
:ref:`closing <no-15235>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-15236>`           Given a position relative to this control, return a position relative
:ref:`copy <no-15237>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-15238>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-15239>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-15240>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-15241>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-15242>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-15243>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-15244>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-15245>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-15246>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-15247>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-15248>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-15249>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-15250>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-15251>`                       Draws text on the object at the specified position
:ref:`endHover <no-15252>`                       
:ref:`fillPreferenceDialog <no-15253>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-15254>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-15255>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-15256>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-15257>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-15258>`              
:ref:`formCoordinates <no-15259>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-15260>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-15261>`                      
:ref:`getCaptureBitmap <no-15262>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-15263>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-15264>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-15265>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-15266>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-15267>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-15268>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-15269>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-15270>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-15271>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-15272>`                           Make the object invisible.
:ref:`initEvents <no-15273>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-15274>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-15275>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-15276>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-15277>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-15278>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-15279>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-15280>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-15281>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-15282>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-15283>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-15284>`                        
:ref:`paste <no-15285>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-15286>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-15287>`                    
:ref:`processDroppedFiles <no-15288>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-15289>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-15290>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-15291>`                     Raise the passed Dabo event.
:ref:`reCreate <no-15292>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-15293>`                       Recreate the object.
:ref:`redraw <no-15294>`                         Called when the object is (re)drawn.
:ref:`refresh <no-15295>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-15296>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-15297>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-15298>`                        Need to augment this to make sure the dialog
:ref:`reload <no-15299>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-15300>`              
:ref:`removeFromOutlinedSizers <no-15301>`       
:ref:`restoreSizeAndPosition <no-15302>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-15303>` 
:ref:`runCancel <no-15304>`                      
:ref:`runHelp <no-15305>`                        
:ref:`runNo <no-15306>`                          
:ref:`runOK <no-15307>`                          
:ref:`runYes <no-15308>`                         
:ref:`safeDestroy <no-15309>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-15310>`            Save the current size and position of this form.
:ref:`sendToBack <no-15311>`                     Places this object behind all others.
:ref:`setAll <no-15312>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-15313>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-15314>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-15315>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-15316>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-15317>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-15318>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-15319>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-15320>`                  Set the status text to val.
:ref:`show <no-15321>`                           
:ref:`showContainingPage <no-15322>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-15323>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-15324>`                      Show the dialog modally.
:ref:`showModeless <no-15325>`                   Show the dialog non-modally.
:ref:`super <no-15326>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-15327>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-15328>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-15329>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-15330>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-15331>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods
=======

.. _no-15213:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.addControlSequence(self, seq)

   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   



-------

.. _no-15214:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.addControls(self)

   
   Use this method to add controls to the dialog. The standard buttons will be added
   after this method runs, so that they appear at the bottom of the dialog.
   



-------

.. _no-15304:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.runCancel(self)



-------

.. _no-15305:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.runHelp(self)



-------

.. _no-15306:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.runNo(self)



-------

.. _no-15307:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.runOK(self)



-------

.. _no-15308:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.runYes(self)



-------

.. _no-15313:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setEscapeButton(self, btn=None)

   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   



-------


Methods - inherited
=====================

.. _no-15211:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15212:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15215:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-15216:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15217:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15218:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15219:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15220:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15221:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15222:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15223:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.autoBindEvents(self, force=True)
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

.. _no-15224:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15225:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15226:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15227:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15228:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15229:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15230:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-15231:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15232:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15233:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15234:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15235:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15236:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15237:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15238:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15239:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15240:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15241:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15242:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-15243:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15244:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15245:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15246:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15247:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15248:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15249:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15250:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15251:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15252:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15253:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15254:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15255:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15256:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15257:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15258:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15259:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15260:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15261:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15262:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15263:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15264:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15265:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15266:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15267:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15268:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15269:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-15270:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15271:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15272:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15273:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15274:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15275:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15276:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15277:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15278:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.lockDisplay(self)
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

.. _no-15279:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15280:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15281:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15282:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15283:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15284:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15285:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15286:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15287:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15288:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15289:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15290:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15291:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15292:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15293:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15294:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15295:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.refresh(self, interval=None)
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

.. _no-15296:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15297:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15298:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15299:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15300:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15301:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15302:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15303:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15309:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15310:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15311:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15312:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-15314:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15315:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15316:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-15317:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-15318:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15319:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15320:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15321:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15322:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15323:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15324:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15325:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15326:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15327:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15328:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15329:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15330:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15331:

.. function:: dabo.ui.uiwx.dDialog.dStandardButtonDialog.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
