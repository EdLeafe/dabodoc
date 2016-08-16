
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDialog

.. _dabo.ui.uiwx.dDialog.dDialog:

========================================
|doc_title|  **dDialog.dDialog** - class
========================================


Creates a dialog, which is a lightweight form.

Dialogs are like forms, but typically are modal and are requesting a very
specific piece of information from the user, and/or offering specific
information to the user.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDialog**

.. inheritance-diagram:: dDialog


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.dialogs.Wizard.Wizard`
* :ref:`dabo.ui.dialogs.about.About`
* :ref:`dabo.ui.dialogs.htmlAbout.HtmlAbout`
* :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dDialog.png
          :scale: 75 %
          :target: _static/macWidgets/dDialog.png
          :alt: dDialog



     - .. image:: _static/winWidgets/dDialog.png
          :scale: 75 %
          :target: _static/winWidgets/dDialog.png
          :alt: dDialog



     - .. image:: _static/nixWidgets/dDialog.png
          :scale: 75 %
          :target: _static/nixWidgets/dDialog.png
          :alt: dDialog


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDialog.dDialog

   .. automethod:: dabo.ui.uiwx.dDialog.dDialog.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-14442>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-14443>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-14444>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-14445>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-14446>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-14447>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-14448>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-14449>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-14450>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-14451>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-14452>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-14453>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-14454>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-14455>`                      The position of the bottom side of the object. This is a
:ref:`Caption <no-14456>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-14457>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-14458>`                    Returns a list of object references to the children of
:ref:`Class <no-14459>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-14460>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-14461>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-14462>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-14463>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-14464>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-14465>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-14466>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-14467>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-14468>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-14469>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-14470>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-14471>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-14472>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-14473>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-14474>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-14475>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-14476>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-14477>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-14478>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-14479>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-14480>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-14481>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-14482>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-14483>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-14484>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-14485>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-14486>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-14487>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-14488>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-14489>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-14490>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-14491>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-14492>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-14493>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-14494>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-14495>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-14496>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-14497>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-14498>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-14499>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-14500>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-14501>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-14502>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-14503>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-14504>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-14505>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-14506>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-14507>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-14508>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-14509>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-14510>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-14511>`                    Specifies the font face. (str)
:ref:`FontInfo <no-14512>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-14513>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-14514>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-14515>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-14516>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-14517>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-14518>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-14519>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-14520>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-14521>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-14522>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-14523>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-14524>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-14525>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-14526>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-14527>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-14528>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-14529>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-14530>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-14531>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-14532>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-14533>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-14534>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-14535>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-14536>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-14537>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-14538>`                    Specifies the base name of the object.
:ref:`Parent <no-14539>`                      The containing object. (obj)
:ref:`Position <no-14540>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-14541>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-14542>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-14543>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-14544>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-14545>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-14546>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-14547>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-14548>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-14549>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-14550>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-14551>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-14552>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-14553>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-14554>`                        The size of the object. (tuple)
:ref:`Sizer <no-14555>`                       The sizer for the object.
:ref:`SizersToOutline <no-14556>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-14557>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-14558>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-14559>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-14560>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-14561>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-14562>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-14563>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-14564>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-14565>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-14566>`                         The top position of the object. (int)
:ref:`Transparency <no-14567>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-14568>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-14569>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-14570>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-14571>`                       The width of the object. (int)
:ref:`WindowHandle <no-14572>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-14573>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties
==========

.. _no-14444:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)



-------

.. _no-14454:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)



-------

.. _no-14466:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.



-------

.. _no-14535:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)



-------


Properties - inherited
========================

.. _no-14442:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14443:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14445:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14446:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14447:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14448:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14449:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14450:

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

.. _no-14451:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14452:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14453:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14455:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14456:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14457:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14458:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14459:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14460:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14461:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14462:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14463:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14464:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14465:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14467:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14468:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14469:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14470:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14471:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14472:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14473:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14474:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14475:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14476:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14477:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14478:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14479:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14480:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14481:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14482:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14483:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14484:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14485:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14486:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14487:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14488:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14489:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14490:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14491:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14492:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14493:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14494:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14495:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14496:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14497:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14498:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14499:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14500:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14501:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14502:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14503:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14504:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14505:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14506:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14507:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14508:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14509:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14510:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14511:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14512:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14513:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14514:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14515:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14516:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14517:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14518:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14519:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14520:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14521:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-14522:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14523:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14524:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14525:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14526:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14527:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14528:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14529:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14530:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14531:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14532:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14533:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14534:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14536:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14537:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14538:

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

.. _no-14539:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14540:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14541:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14542:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14543:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14544:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14545:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14546:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14547:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14548:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14549:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14550:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14551:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14552:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14553:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14554:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14555:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14556:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14557:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14558:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14559:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14560:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14561:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14562:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14563:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14564:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14565:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14566:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14567:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14568:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14569:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14570:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14571:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14572:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14573:

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
:ref:`Activate <no-14574>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-14575>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-14576>`              Occurs when a child control is created.
:ref:`Close <no-14577>`                  Occurs when the user closes the form.
:ref:`Create <no-14578>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-14579>`             Occurs when another form becomes active.
:ref:`Destroy <no-14580>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-14581>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-14582>`               Occurs when the control gets the focus.
:ref:`Idle <no-14583>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-14584>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-14585>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-14586>`               
:ref:`KeyUp <no-14587>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-14588>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-14589>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-14590>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-14591>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-14592>`             
:ref:`MouseLeave <no-14593>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-14594>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-14595>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-14596>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-14597>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-14598>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-14599>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-14600>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-14601>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-14602>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-14603>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-14604>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-14605>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-14606>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-14607>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-14608>`                   Occurs when the control's position changes.
:ref:`Paint <no-14609>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-14610>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-14611>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-14612>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-14613>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-14574:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-14575:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-14576:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-14577:

**Close** 

Occurs when the user closes the form.



-------

.. _no-14578:

**Create** 

Occurs after the control or form is created.



-------

.. _no-14579:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-14580:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-14581:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-14582:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-14583:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-14584:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-14585:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-14586:

**KeyEvent** 



-------

.. _no-14587:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-14588:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-14589:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-14590:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-14591:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-14592:

**MouseEvent** 



-------

.. _no-14593:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-14594:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-14595:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-14596:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-14597:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-14598:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-14599:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-14600:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-14601:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-14602:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-14603:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-14604:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-14605:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-14606:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-14607:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-14608:

**Move** 

Occurs when the control's position changes.



-------

.. _no-14609:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-14610:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-14611:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-14612:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-14613:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-14614>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-14615>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControls <no-14616>`                    Add your custom controls to the dialog.
:ref:`addObject <no-14617>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-14618>`            
:ref:`afterAddControls <no-14619>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-14620>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-14621>`                   
:ref:`afterSetMenuBar <no-14622>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-14623>`             
:ref:`appendToolBarButton <no-14624>`            
:ref:`autoBindEvents <no-14625>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-14626>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-14627>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-14628>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-14629>`            
:ref:`bindEvent <no-14630>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-14631>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-14632>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-14633>`                   Makes this object topmost
:ref:`clear <no-14634>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-14635>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-14636>`                          This method will close the form. If force = False (default)
:ref:`closing <no-14637>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-14638>`           Given a position relative to this control, return a position relative
:ref:`copy <no-14639>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-14640>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-14641>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-14642>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-14643>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-14644>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-14645>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-14646>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-14647>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-14648>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-14649>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-14650>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-14651>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-14652>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-14653>`                       Draws text on the object at the specified position
:ref:`endHover <no-14654>`                       
:ref:`fillPreferenceDialog <no-14655>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-14656>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-14657>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-14658>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-14659>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-14660>`              
:ref:`formCoordinates <no-14661>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-14662>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-14663>`                      
:ref:`getCaptureBitmap <no-14664>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-14665>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-14666>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-14667>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-14668>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-14669>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-14670>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-14671>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-14672>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-14673>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-14674>`                           Make the object invisible.
:ref:`initEvents <no-14675>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-14676>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-14677>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-14678>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-14679>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-14680>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-14681>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-14682>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-14683>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-14684>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-14685>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-14686>`                        
:ref:`paste <no-14687>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-14688>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-14689>`                    
:ref:`processDroppedFiles <no-14690>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-14691>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-14692>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-14693>`                     Raise the passed Dabo event.
:ref:`reCreate <no-14694>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-14695>`                       Recreate the object.
:ref:`redraw <no-14696>`                         Called when the object is (re)drawn.
:ref:`refresh <no-14697>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-14698>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-14699>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-14700>`                        Need to augment this to make sure the dialog
:ref:`reload <no-14701>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-14702>`              
:ref:`removeFromOutlinedSizers <no-14703>`       
:ref:`restoreSizeAndPosition <no-14704>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-14705>` 
:ref:`safeDestroy <no-14706>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-14707>`            Save the current size and position of this form.
:ref:`sendToBack <no-14708>`                     Places this object behind all others.
:ref:`setAll <no-14709>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-14710>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-14711>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-14712>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-14713>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-14714>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-14715>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-14716>`                  Set the status text to val.
:ref:`show <no-14717>`                           
:ref:`showContainingPage <no-14718>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-14719>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-14720>`                      Show the dialog modally.
:ref:`showModeless <no-14721>`                   Show the dialog non-modally.
:ref:`super <no-14722>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-14723>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-14724>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-14725>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-14726>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-14727>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods
=======

.. _no-14616:

.. function:: dabo.ui.uiwx.dDialog.dDialog.addControls(self)

   
   Add your custom controls to the dialog.
   
   This is a hook, called at the appropriate time by the framework.
   



-------

.. _no-14619:

.. function:: dabo.ui.uiwx.dDialog.dDialog.afterAddControls(self)

   This is a hook, called at the appropriate time by the framework.



-------

.. _no-14626:

.. function:: dabo.ui.uiwx.dDialog.dDialog.beforeAddControls(self)

   This is a hook, called at the appropriate time by the framework.



-------

.. _no-14663:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getBizobj(self, \*args, \**kwargs)



-------

.. _no-14700:

.. function:: dabo.ui.uiwx.dDialog.dDialog.release(self)

   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   



-------

.. _no-14717:

.. function:: dabo.ui.uiwx.dDialog.dDialog.show(self)



-------

.. _no-14720:

.. function:: dabo.ui.uiwx.dDialog.dDialog.showModal(self)

   Show the dialog modally.



-------

.. _no-14721:

.. function:: dabo.ui.uiwx.dDialog.dDialog.showModeless(self)

   Show the dialog non-modally.



-------


Methods - inherited
=====================

.. _no-14614:

.. function:: dabo.ui.uiwx.dDialog.dDialog.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14615:

.. function:: dabo.ui.uiwx.dDialog.dDialog.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14617:

.. function:: dabo.ui.uiwx.dDialog.dDialog.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-14618:

.. function:: dabo.ui.uiwx.dDialog.dDialog.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14620:

.. function:: dabo.ui.uiwx.dDialog.dDialog.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14621:

.. function:: dabo.ui.uiwx.dDialog.dDialog.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14622:

.. function:: dabo.ui.uiwx.dDialog.dDialog.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14623:

.. function:: dabo.ui.uiwx.dDialog.dDialog.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14624:

.. function:: dabo.ui.uiwx.dDialog.dDialog.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14625:

.. function:: dabo.ui.uiwx.dDialog.dDialog.autoBindEvents(self, force=True)
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

.. _no-14627:

.. function:: dabo.ui.uiwx.dDialog.dDialog.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14628:

.. function:: dabo.ui.uiwx.dDialog.dDialog.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14629:

.. function:: dabo.ui.uiwx.dDialog.dDialog.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14630:

.. function:: dabo.ui.uiwx.dDialog.dDialog.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14631:

.. function:: dabo.ui.uiwx.dDialog.dDialog.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14632:

.. function:: dabo.ui.uiwx.dDialog.dDialog.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-14633:

.. function:: dabo.ui.uiwx.dDialog.dDialog.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14634:

.. function:: dabo.ui.uiwx.dDialog.dDialog.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14635:

.. function:: dabo.ui.uiwx.dDialog.dDialog.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14636:

.. function:: dabo.ui.uiwx.dDialog.dDialog.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14637:

.. function:: dabo.ui.uiwx.dDialog.dDialog.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14638:

.. function:: dabo.ui.uiwx.dDialog.dDialog.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14639:

.. function:: dabo.ui.uiwx.dDialog.dDialog.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14640:

.. function:: dabo.ui.uiwx.dDialog.dDialog.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14641:

.. function:: dabo.ui.uiwx.dDialog.dDialog.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14642:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14643:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14644:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-14645:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14646:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14647:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14648:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14649:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14650:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14651:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14652:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14653:

.. function:: dabo.ui.uiwx.dDialog.dDialog.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14654:

.. function:: dabo.ui.uiwx.dDialog.dDialog.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14655:

.. function:: dabo.ui.uiwx.dDialog.dDialog.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14656:

.. function:: dabo.ui.uiwx.dDialog.dDialog.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14657:

.. function:: dabo.ui.uiwx.dDialog.dDialog.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14658:

.. function:: dabo.ui.uiwx.dDialog.dDialog.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14659:

.. function:: dabo.ui.uiwx.dDialog.dDialog.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14660:

.. function:: dabo.ui.uiwx.dDialog.dDialog.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14661:

.. function:: dabo.ui.uiwx.dDialog.dDialog.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14662:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14664:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14665:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14666:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14667:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14668:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14669:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14670:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14671:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-14672:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14673:

.. function:: dabo.ui.uiwx.dDialog.dDialog.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14674:

.. function:: dabo.ui.uiwx.dDialog.dDialog.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14675:

.. function:: dabo.ui.uiwx.dDialog.dDialog.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14676:

.. function:: dabo.ui.uiwx.dDialog.dDialog.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14677:

.. function:: dabo.ui.uiwx.dDialog.dDialog.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14678:

.. function:: dabo.ui.uiwx.dDialog.dDialog.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14679:

.. function:: dabo.ui.uiwx.dDialog.dDialog.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14680:

.. function:: dabo.ui.uiwx.dDialog.dDialog.lockDisplay(self)
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

.. _no-14681:

.. function:: dabo.ui.uiwx.dDialog.dDialog.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14682:

.. function:: dabo.ui.uiwx.dDialog.dDialog.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14683:

.. function:: dabo.ui.uiwx.dDialog.dDialog.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14684:

.. function:: dabo.ui.uiwx.dDialog.dDialog.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14685:

.. function:: dabo.ui.uiwx.dDialog.dDialog.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14686:

.. function:: dabo.ui.uiwx.dDialog.dDialog.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14687:

.. function:: dabo.ui.uiwx.dDialog.dDialog.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14688:

.. function:: dabo.ui.uiwx.dDialog.dDialog.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14689:

.. function:: dabo.ui.uiwx.dDialog.dDialog.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14690:

.. function:: dabo.ui.uiwx.dDialog.dDialog.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14691:

.. function:: dabo.ui.uiwx.dDialog.dDialog.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14692:

.. function:: dabo.ui.uiwx.dDialog.dDialog.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14693:

.. function:: dabo.ui.uiwx.dDialog.dDialog.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14694:

.. function:: dabo.ui.uiwx.dDialog.dDialog.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14695:

.. function:: dabo.ui.uiwx.dDialog.dDialog.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14696:

.. function:: dabo.ui.uiwx.dDialog.dDialog.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14697:

.. function:: dabo.ui.uiwx.dDialog.dDialog.refresh(self, interval=None)
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

.. _no-14698:

.. function:: dabo.ui.uiwx.dDialog.dDialog.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14699:

.. function:: dabo.ui.uiwx.dDialog.dDialog.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14701:

.. function:: dabo.ui.uiwx.dDialog.dDialog.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14702:

.. function:: dabo.ui.uiwx.dDialog.dDialog.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14703:

.. function:: dabo.ui.uiwx.dDialog.dDialog.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14704:

.. function:: dabo.ui.uiwx.dDialog.dDialog.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14705:

.. function:: dabo.ui.uiwx.dDialog.dDialog.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14706:

.. function:: dabo.ui.uiwx.dDialog.dDialog.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14707:

.. function:: dabo.ui.uiwx.dDialog.dDialog.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14708:

.. function:: dabo.ui.uiwx.dDialog.dDialog.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14709:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-14710:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14711:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14712:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-14713:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-14714:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14715:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14716:

.. function:: dabo.ui.uiwx.dDialog.dDialog.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14718:

.. function:: dabo.ui.uiwx.dDialog.dDialog.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14719:

.. function:: dabo.ui.uiwx.dDialog.dDialog.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14722:

.. function:: dabo.ui.uiwx.dDialog.dDialog.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14723:

.. function:: dabo.ui.uiwx.dDialog.dDialog.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14724:

.. function:: dabo.ui.uiwx.dDialog.dDialog.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14725:

.. function:: dabo.ui.uiwx.dDialog.dDialog.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14726:

.. function:: dabo.ui.uiwx.dDialog.dDialog.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14727:

.. function:: dabo.ui.uiwx.dDialog.dDialog.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
