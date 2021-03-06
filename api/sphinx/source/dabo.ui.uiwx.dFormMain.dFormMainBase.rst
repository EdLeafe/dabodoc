
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dFormMain

.. _dabo.ui.uiwx.dFormMain.dFormMainBase:

================================================
|doc_title|  **dFormMain.dFormMainBase** - class
================================================

This is the main top-level form for the application.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dFormMainBase**

.. inheritance-diagram:: dFormMainBase


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dFormMain.dFormMain`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dFormMain.dFormMainBase

   .. automethod:: dabo.ui.uiwx.dFormMain.dFormMainBase.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-36168>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-36169>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-36170>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-36171>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-36172>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-36173>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-36174>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-36175>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-36176>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-36177>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-36178>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-36179>`                      The position of the bottom side of the object. This is a
:ref:`Caption <no-36180>`                     The caption of the object. (str)
:ref:`Centered <no-36181>`                    Centers the form on the screen when set to True.  (bool)
:ref:`Children <no-36182>`                    Returns a list of object references to the children of
:ref:`Class <no-36183>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-36184>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-36185>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-36186>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-36187>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-36188>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-36189>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-36190>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-36191>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-36192>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-36193>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-36194>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-36195>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-36196>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-36197>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-36198>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-36199>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-36200>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-36201>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-36202>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-36203>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-36204>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-36205>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-36206>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-36207>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-36208>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-36209>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-36210>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-36211>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-36212>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-36213>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-36214>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-36215>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-36216>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-36217>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-36218>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-36219>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-36220>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-36221>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-36222>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-36223>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-36224>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-36225>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-36226>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-36227>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-36228>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-36229>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-36230>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-36231>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-36232>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-36233>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-36234>`                    Specifies the font face. (str)
:ref:`FontInfo <no-36235>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-36236>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-36237>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-36238>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-36239>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-36240>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-36241>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-36242>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-36243>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-36244>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-36245>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-36246>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-36247>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-36248>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-36249>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-36250>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-36251>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-36252>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-36253>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-36254>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-36255>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-36256>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-36257>`                Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-36258>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-36259>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-36260>`                    Specifies the base name of the object.
:ref:`Parent <no-36261>`                      The containing object. (obj)
:ref:`Position <no-36262>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-36263>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-36264>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-36265>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-36266>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-36267>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-36268>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-36269>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-36270>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-36271>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-36272>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-36273>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-36274>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-36275>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-36276>`                        The size of the object. (tuple)
:ref:`Sizer <no-36277>`                       The sizer for the object.
:ref:`SizersToOutline <no-36278>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-36279>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-36280>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-36281>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-36282>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-36283>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-36284>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-36285>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-36286>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-36287>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-36288>`                         The top position of the object. (int)
:ref:`Transparency <no-36289>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-36290>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-36291>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-36292>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-36293>`                       The width of the object. (int)
:ref:`WindowHandle <no-36294>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-36295>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties - inherited
========================

.. _no-36168:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36169:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36170:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36171:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36172:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36173:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36174:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36175:

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

.. _no-36176:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36177:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36178:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36179:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36180:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36181:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36182:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36183:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36184:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36185:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36186:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36187:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36188:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36189:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36190:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36191:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36192:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36193:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36194:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36195:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36196:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36197:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36198:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36199:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36200:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36201:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36202:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36203:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36204:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36205:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36206:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36207:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36208:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36209:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36210:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36211:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36212:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36213:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36214:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36215:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36216:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36217:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36218:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36219:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36220:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36221:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36222:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36223:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36224:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36225:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36226:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36227:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36228:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36229:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36230:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36231:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36232:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36233:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36234:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36235:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36236:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36237:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36238:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36239:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36240:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36241:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36242:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36243:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36244:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36245:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36246:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36247:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36248:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36249:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36250:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36251:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36252:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36253:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36254:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36255:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36256:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36257:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36258:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36259:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36260:

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

.. _no-36261:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36262:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36263:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36264:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36265:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36266:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36267:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36268:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36269:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36270:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36271:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36272:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36273:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36274:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36275:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36276:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36277:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36278:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36279:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36280:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36281:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36282:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36283:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36284:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36285:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36286:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36287:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36288:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36289:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36290:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36291:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36292:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36293:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36294:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36295:

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
:ref:`BackgroundErased <no-36296>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-36297>`                 Occurs after the control or form is created.
:ref:`Destroy <no-36298>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-36299>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-36300>`               Occurs when the control gets the focus.
:ref:`Idle <no-36301>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-36302>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-36303>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-36304>`               
:ref:`KeyUp <no-36305>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-36306>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-36307>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-36308>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-36309>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-36310>`             
:ref:`MouseLeave <no-36311>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-36312>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-36313>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-36314>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-36315>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-36316>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-36317>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-36318>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-36319>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-36320>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-36321>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-36322>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-36323>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-36324>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-36325>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-36326>`                   Occurs when the control's position changes.
:ref:`Paint <no-36327>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-36328>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-36329>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-36330>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-36331>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-36296:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-36297:

**Create** 

Occurs after the control or form is created.



-------

.. _no-36298:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-36299:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-36300:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-36301:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-36302:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-36303:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-36304:

**KeyEvent** 



-------

.. _no-36305:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-36306:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-36307:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-36308:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-36309:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-36310:

**MouseEvent** 



-------

.. _no-36311:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-36312:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-36313:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-36314:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-36315:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-36316:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-36317:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-36318:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-36319:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-36320:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-36321:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-36322:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-36323:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-36324:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-36325:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-36326:

**Move** 

Occurs when the control's position changes.



-------

.. _no-36327:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-36328:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-36329:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-36330:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-36331:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-36332>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-36333>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addObject <no-36334>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-36335>`            
:ref:`afterInit <no-36336>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-36337>`                   
:ref:`afterSetMenuBar <no-36338>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-36339>`             
:ref:`appendToolBarButton <no-36340>`            
:ref:`autoBindEvents <no-36341>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeClose <no-36342>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-36343>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-36344>`            
:ref:`bindEvent <no-36345>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-36346>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-36347>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-36348>`                   Makes this object topmost
:ref:`clear <no-36349>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-36350>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-36351>`                          This method will close the form. If force = False (default)
:ref:`closing <no-36352>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-36353>`           Given a position relative to this control, return a position relative
:ref:`copy <no-36354>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-36355>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-36356>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-36357>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-36358>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-36359>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-36360>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-36361>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-36362>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-36363>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-36364>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-36365>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-36366>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-36367>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-36368>`                       Draws text on the object at the specified position
:ref:`endHover <no-36369>`                       
:ref:`fillPreferenceDialog <no-36370>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-36371>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-36372>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-36373>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-36374>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-36375>`              
:ref:`formCoordinates <no-36376>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-36377>`                Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-36378>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-36379>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-36380>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-36381>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-36382>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-36383>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-36384>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-36385>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-36386>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-36387>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-36388>`                           Make the object invisible.
:ref:`initEvents <no-36389>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-36390>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-36391>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-36392>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-36393>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-36394>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-36395>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-36396>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-36397>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-36398>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-36399>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-36400>`                        
:ref:`paste <no-36401>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-36402>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-36403>`                    
:ref:`processDroppedFiles <no-36404>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-36405>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-36406>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-36407>`                     Raise the passed Dabo event.
:ref:`reCreate <no-36408>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-36409>`                       Recreate the object.
:ref:`redraw <no-36410>`                         Called when the object is (re)drawn.
:ref:`refresh <no-36411>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-36412>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-36413>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-36414>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-36415>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-36416>`              
:ref:`removeFromOutlinedSizers <no-36417>`       
:ref:`restoreSizeAndPosition <no-36418>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-36419>` 
:ref:`safeDestroy <no-36420>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-36421>`            Save the current size and position of this form.
:ref:`sendToBack <no-36422>`                     Places this object behind all others.
:ref:`setAll <no-36423>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-36424>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-36425>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-36426>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-36427>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-36428>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-36429>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-36430>`                  Set the status text to val.
:ref:`show <no-36431>`                           Make the object visible.
:ref:`showContainingPage <no-36432>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-36433>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-36434>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-36435>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-36436>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-36437>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-36438>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-36439>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-36440>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods - inherited
=====================

.. _no-36332:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36333:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36334:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-36335:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36336:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36337:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36338:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36339:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36340:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36341:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.autoBindEvents(self, force=True)
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

.. _no-36342:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36343:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36344:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36345:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-36346:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-36347:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-36348:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36349:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36350:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36351:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36352:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36353:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36354:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36355:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36356:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36357:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36358:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36359:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-36360:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36361:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36362:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36363:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36364:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36365:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36366:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36367:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36368:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36369:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36370:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36371:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36372:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36373:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36374:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36375:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36376:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36377:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36378:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36379:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36380:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36381:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36382:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36383:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36384:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36385:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-36386:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36387:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36388:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36389:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36390:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36391:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36392:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36393:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36394:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.lockDisplay(self)
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

.. _no-36395:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36396:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36397:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36398:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36399:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36400:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36401:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36402:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36403:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36404:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36405:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36406:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36407:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36408:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36409:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36410:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36411:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.refresh(self, interval=None)
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

.. _no-36412:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36413:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36414:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36415:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36416:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36417:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36418:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36419:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36420:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36421:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36422:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36423:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-36424:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36425:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36426:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-36427:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-36428:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36429:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36430:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36431:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36432:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36433:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36434:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36435:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36436:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-36437:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36438:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36439:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36440:

.. function:: dabo.ui.uiwx.dFormMain.dFormMainBase.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
