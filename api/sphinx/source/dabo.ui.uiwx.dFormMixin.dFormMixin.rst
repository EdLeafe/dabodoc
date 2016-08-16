
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dFormMixin

.. _dabo.ui.uiwx.dFormMixin.dFormMixin:

==============================================
|doc_title|  **dFormMixin.dFormMixin** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dFormMixin**

.. inheritance-diagram:: dFormMixin


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dDialog.dDialog`
* :ref:`dabo.ui.uiwx.dForm.BaseForm`
* :ref:`dabo.ui.uiwx.dFormMain.dFormMainBase`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dFormMixin.dFormMixin

   .. automethod:: dabo.ui.uiwx.dFormMixin.dFormMixin.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-25027>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-25028>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-25029>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-25030>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-25031>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-25032>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-25033>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-25034>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-25035>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-25036>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-25037>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-25038>`                      The position of the bottom side of the object. This is a
:ref:`Caption <no-25039>`                     The caption of the object. (str)
:ref:`Centered <no-25040>`                    Centers the form on the screen when set to True.  (bool)
:ref:`Children <no-25041>`                    Returns a list of object references to the children of
:ref:`Class <no-25042>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-25043>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-25044>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-25045>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-25046>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-25047>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-25048>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-25049>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-25050>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-25051>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-25052>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-25053>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-25054>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-25055>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-25056>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-25057>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-25058>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-25059>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-25060>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-25061>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-25062>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-25063>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-25064>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-25065>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-25066>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-25067>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-25068>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-25069>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-25070>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-25071>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-25072>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-25073>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-25074>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-25075>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-25076>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-25077>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-25078>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-25079>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-25080>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-25081>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-25082>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-25083>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-25084>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-25085>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-25086>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-25087>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-25088>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-25089>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-25090>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-25091>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-25092>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-25093>`                    Specifies the font face. (str)
:ref:`FontInfo <no-25094>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-25095>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-25096>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-25097>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-25098>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-25099>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-25100>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-25101>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-25102>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-25103>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-25104>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-25105>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-25106>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-25107>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-25108>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-25109>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-25110>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-25111>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-25112>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-25113>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-25114>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-25115>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-25116>`                Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-25117>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-25118>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-25119>`                    Specifies the base name of the object.
:ref:`Parent <no-25120>`                      The containing object. (obj)
:ref:`Position <no-25121>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-25122>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-25123>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-25124>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-25125>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-25126>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-25127>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-25128>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-25129>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-25130>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-25131>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-25132>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-25133>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-25134>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-25135>`                        The size of the object. (tuple)
:ref:`Sizer <no-25136>`                       The sizer for the object.
:ref:`SizersToOutline <no-25137>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-25138>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-25139>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-25140>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-25141>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-25142>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-25143>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-25144>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-25145>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-25146>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-25147>`                         The top position of the object. (int)
:ref:`Transparency <no-25148>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-25149>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-25150>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-25151>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-25152>`                       The width of the object. (int)
:ref:`WindowHandle <no-25153>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-25154>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties
==========

.. _no-25027:

**ActiveControl** 

Contains a reference to the active control on the form, or None.



-------

.. _no-25029:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)



-------

.. _no-25035:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.



-------

.. _no-25040:

**Centered** 

Centers the form on the screen when set to True.  (bool)



-------

.. _no-25043:

**Connection** 

The connection to the database used by this form  (dConnection)



-------

.. _no-25046:

**CxnName** 

Name of the connection used for data access  (str)



-------

.. _no-25049:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.



-------

.. _no-25053:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.



-------

.. _no-25057:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.



-------

.. _no-25058:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.



-------

.. _no-25060:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.



-------

.. _no-25069:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.



-------

.. _no-25071:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.



-------

.. _no-25074:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.



-------

.. _no-25075:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.



-------

.. _no-25077:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.



-------

.. _no-25080:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.



-------

.. _no-25086:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.



-------

.. _no-25088:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.



-------

.. _no-25089:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)



-------

.. _no-25103:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.



-------

.. _no-25104:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)



-------

.. _no-25107:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)



-------

.. _no-25111:

**MenuBar** 

Specifies the menu bar instance for the form.



-------

.. _no-25112:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.



-------

.. _no-25113:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)



-------

.. _no-25125:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.



-------

.. _no-25126:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).



-------

.. _no-25127:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).



-------

.. _no-25128:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).



-------

.. _no-25129:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).



-------

.. _no-25130:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.



-------

.. _no-25131:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).



-------

.. _no-25132:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.



-------

.. _no-25133:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).



-------

.. _no-25134:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.



-------

.. _no-25137:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)



-------

.. _no-25138:

**StatusBar** 

Status bar for this form. (dStatusBar)



-------

.. _no-25139:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)



-------

.. _no-25141:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)



-------

.. _no-25143:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)



-------

.. _no-25144:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).



-------

.. _no-25145:

**ToolBar** 

Tool bar for this form. (dToolBar)



-------

.. _no-25154:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen



-------


Properties - inherited
========================

.. _no-25028:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25030:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25031:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25032:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25033:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25034:

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

.. _no-25036:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25037:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25038:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25039:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25041:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25042:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25044:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25045:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25047:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25048:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25050:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25051:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25052:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25054:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25055:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25056:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25059:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25061:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25062:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25063:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25064:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25065:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25066:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25067:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25068:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25070:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25072:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25073:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25076:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25078:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25079:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25081:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25082:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25083:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25084:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25085:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25087:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25090:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25091:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25092:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25093:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25094:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25095:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25096:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25097:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25098:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25099:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25100:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25101:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25102:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25105:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25106:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25108:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25109:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25110:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25114:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25115:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25116:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25117:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25118:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25119:

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

.. _no-25120:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25121:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25122:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25123:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25124:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25135:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25136:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25140:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25142:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25146:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25147:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25148:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25149:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25150:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25151:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25152:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25153:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-25155>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-25156>`                 Occurs after the control or form is created.
:ref:`Destroy <no-25157>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-25158>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-25159>`               Occurs when the control gets the focus.
:ref:`Idle <no-25160>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-25161>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-25162>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-25163>`               
:ref:`KeyUp <no-25164>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-25165>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-25166>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-25167>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-25168>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-25169>`             
:ref:`MouseLeave <no-25170>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-25171>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-25172>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-25173>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-25174>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-25175>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-25176>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-25177>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-25178>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-25179>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-25180>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-25181>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-25182>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-25183>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-25184>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-25185>`                   Occurs when the control's position changes.
:ref:`Paint <no-25186>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-25187>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-25188>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-25189>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-25190>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-25155:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-25156:

**Create** 

Occurs after the control or form is created.



-------

.. _no-25157:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-25158:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-25159:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-25160:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-25161:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-25162:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-25163:

**KeyEvent** 



-------

.. _no-25164:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-25165:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-25166:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-25167:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-25168:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-25169:

**MouseEvent** 



-------

.. _no-25170:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-25171:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-25172:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-25173:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-25174:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-25175:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-25176:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-25177:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-25178:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-25179:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-25180:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-25181:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-25182:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-25183:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-25184:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-25185:

**Move** 

Occurs when the control's position changes.



-------

.. _no-25186:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-25187:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-25188:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-25189:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-25190:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-25191>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-25192>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addObject <no-25193>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-25194>`            
:ref:`afterInit <no-25195>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-25196>`                   
:ref:`afterSetMenuBar <no-25197>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-25198>`             
:ref:`appendToolBarButton <no-25199>`            
:ref:`autoBindEvents <no-25200>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeClose <no-25201>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-25202>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-25203>`            
:ref:`bindEvent <no-25204>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-25205>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-25206>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-25207>`                   Makes this object topmost
:ref:`clear <no-25208>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-25209>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-25210>`                          This method will close the form. If force = False (default)
:ref:`closing <no-25211>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-25212>`           Given a position relative to this control, return a position relative
:ref:`copy <no-25213>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-25214>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-25215>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-25216>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-25217>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-25218>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-25219>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-25220>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-25221>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-25222>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-25223>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-25224>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-25225>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-25226>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-25227>`                       Draws text on the object at the specified position
:ref:`endHover <no-25228>`                       
:ref:`fillPreferenceDialog <no-25229>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-25230>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-25231>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-25232>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-25233>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-25234>`              
:ref:`formCoordinates <no-25235>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-25236>`                Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-25237>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-25238>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-25239>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-25240>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-25241>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-25242>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-25243>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-25244>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-25245>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-25246>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-25247>`                           Make the object invisible.
:ref:`initEvents <no-25248>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-25249>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-25250>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-25251>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-25252>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-25253>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-25254>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-25255>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-25256>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-25257>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-25258>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-25259>`                        
:ref:`paste <no-25260>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-25261>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-25262>`                    
:ref:`processDroppedFiles <no-25263>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-25264>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-25265>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-25266>`                     Raise the passed Dabo event.
:ref:`reCreate <no-25267>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-25268>`                       Recreate the object.
:ref:`redraw <no-25269>`                         Called when the object is (re)drawn.
:ref:`refresh <no-25270>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-25271>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-25272>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-25273>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-25274>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-25275>`              
:ref:`removeFromOutlinedSizers <no-25276>`       
:ref:`restoreSizeAndPosition <no-25277>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-25278>` 
:ref:`safeDestroy <no-25279>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-25280>`            Save the current size and position of this form.
:ref:`sendToBack <no-25281>`                     Places this object behind all others.
:ref:`setAll <no-25282>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-25283>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-25284>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-25285>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-25286>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-25287>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-25288>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-25289>`                  Set the status text to val.
:ref:`show <no-25290>`                           Make the object visible.
:ref:`showContainingPage <no-25291>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-25292>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-25293>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-25294>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-25295>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-25296>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-25297>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-25298>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-25299>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods
=======

.. _no-25192:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.activeControlValid(self)

   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   



-------

.. _no-25194:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.addToOutlinedSizers(self, val)



-------

.. _no-25197:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.afterSetMenuBar(self)

   Subclasses can extend the menu bar here.



-------

.. _no-25199:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)



-------

.. _no-25201:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.beforeClose(self, evt)

   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   



-------

.. _no-25210:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.close(self, force=False)

   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   



-------

.. _no-25211:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.closing(self)

   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   



-------

.. _no-25214:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.createBizobjs(self)

   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   



-------

.. _no-25229:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.fillPreferenceDialog(self, dlg)

   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   



-------

.. _no-25234:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.forceSizerOutline(self)



-------

.. _no-25240:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getMenu(self)

   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   



-------

.. _no-25242:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getObjectByRegID(self, id)

   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   



-------

.. _no-25252:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.layout(self)

   Wrap the wx sizer layout call.



-------

.. _no-25257:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.onEditRedo(self, evt)

   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   



-------

.. _no-25258:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.onEditUndo(self, evt)

   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   



-------

.. _no-25261:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.popStatusText(self)

   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   



-------

.. _no-25265:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.pushStatusText(self, txt, duration=None)

   Stores the current text of the StatusBar on a LIFO stack for later retrieval.



-------

.. _no-25270:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.refresh(self, interval=None)

   
   Repaints the form and all contained objects.
   
   This method is called repeatedly from many different places during
   a single change in the UI, so by default the actual execution is cached
   using callAfterInterval(). The default interval is 100 milliseconds. You
   can change that to suit your app needs by passing a different interval
   in milliseconds.
   
   Sometimes, though, you want to force immediate execution of the
   refresh. In these cases, pass an interval of 0 to this method, which
   means don't wait; execute now.
   



-------

.. _no-25271:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.registerObject(self, obj)

   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   



-------

.. _no-25273:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.release(self)

   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   



-------

.. _no-25274:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.reload(self)

   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   



-------

.. _no-25276:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.removeFromOutlinedSizers(self, val)



-------

.. _no-25277:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.restoreSizeAndPosition(self)

   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   



-------

.. _no-25278:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.restoreSizeAndPositionIfNeeded(self)



-------

.. _no-25279:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.safeDestroy(self)

   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   



-------

.. _no-25280:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.saveSizeAndPosition(self)

   Save the current size and position of this form.



-------

.. _no-25289:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setStatusText(self, val, immediate=False)

   Set the status text to val.



-------

.. _no-25293:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.showModal(self)

   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   



-------


Methods - inherited
=====================

.. _no-25191:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25193:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-25195:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25196:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25198:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25200:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.autoBindEvents(self, force=True)
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

.. _no-25202:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25203:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25204:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25205:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25206:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-25207:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25208:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25209:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25212:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25213:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25215:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25216:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25217:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25218:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-25219:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25220:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25221:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25222:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25223:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25224:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25225:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25226:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25227:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25228:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25230:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25231:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25232:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25233:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25235:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25236:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25237:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25238:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25239:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25241:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25243:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25244:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-25245:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25246:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25247:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25248:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25249:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25250:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25251:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25253:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.lockDisplay(self)
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

.. _no-25254:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25255:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25256:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25259:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25260:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25262:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25263:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25264:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25266:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25267:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-25268:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25269:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25272:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25275:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25281:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25282:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-25283:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25284:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25285:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-25286:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-25287:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25288:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25290:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25291:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25292:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25294:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-25295:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-25296:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25297:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25298:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-25299:

.. function:: dabo.ui.uiwx.dFormMixin.dFormMixin.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
