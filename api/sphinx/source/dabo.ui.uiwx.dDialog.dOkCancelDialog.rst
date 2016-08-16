
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDialog

.. _dabo.ui.uiwx.dDialog.dOkCancelDialog:

================================================
|doc_title|  **dDialog.dOkCancelDialog** - class
================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dOkCancelDialog**

.. inheritance-diagram:: dOkCancelDialog


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.dialogs.HotKeyEditor.HotKeyEditor`
* :ref:`dabo.ui.dialogs.PreferenceDialog.PreferenceDialog`
* :ref:`dabo.ui.dialogs.SortingForm.SortingForm`
* :ref:`dabo.ui.dialogs.login.Login`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDialog.dOkCancelDialog

   .. automethod:: dabo.ui.uiwx.dDialog.dOkCancelDialog.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`Accepted <no-14728>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-14729>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-14730>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-14731>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-14732>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-14733>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-14734>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-14735>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-14736>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-14737>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-14738>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-14739>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-14740>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-14741>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-14742>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-14743>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-14744>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-14745>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-14746>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-14747>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-14748>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-14749>`                    Returns a list of object references to the children of
:ref:`Class <no-14750>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-14751>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-14752>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-14753>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-14754>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-14755>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-14756>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-14757>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-14758>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-14759>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-14760>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-14761>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-14762>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-14763>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-14764>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-14765>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-14766>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-14767>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-14768>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-14769>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-14770>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-14771>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-14772>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-14773>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-14774>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-14775>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-14776>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-14777>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-14778>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-14779>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-14780>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-14781>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-14782>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-14783>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-14784>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-14785>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-14786>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-14787>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-14788>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-14789>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-14790>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-14791>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-14792>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-14793>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-14794>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-14795>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-14796>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-14797>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-14798>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-14799>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-14800>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-14801>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-14802>`                    Specifies the font face. (str)
:ref:`FontInfo <no-14803>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-14804>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-14805>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-14806>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-14807>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-14808>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-14809>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-14810>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-14811>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-14812>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-14813>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-14814>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-14815>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-14816>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-14817>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-14818>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-14819>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-14820>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-14821>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-14822>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-14823>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-14824>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-14825>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-14826>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-14827>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-14828>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-14829>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-14830>`                    Specifies the base name of the object.
:ref:`NoButton <no-14831>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-14832>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-14833>`                      The containing object. (obj)
:ref:`Position <no-14834>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-14835>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-14836>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-14837>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-14838>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-14839>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-14840>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-14841>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-14842>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-14843>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-14844>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-14845>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-14846>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-14847>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-14848>`                        The size of the object. (tuple)
:ref:`Sizer <no-14849>`                       The sizer for the object.
:ref:`SizersToOutline <no-14850>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-14851>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-14852>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-14853>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-14854>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-14855>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-14856>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-14857>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-14858>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-14859>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-14860>`                         The top position of the object. (int)
:ref:`Transparency <no-14861>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-14862>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-14863>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-14864>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-14865>`                       The width of the object. (int)
:ref:`WindowHandle <no-14866>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-14867>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-14868>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================= ========================


Properties - inherited
========================

.. _no-14728:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14729:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14730:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14731:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14732:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14733:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14734:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14735:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14736:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14737:

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

.. _no-14738:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14739:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14740:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14741:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14742:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14743:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14744:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14745:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14746:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14747:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14748:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14749:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14750:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14751:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14752:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14753:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14754:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14755:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14756:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14757:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14758:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14759:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14760:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14761:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14762:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14763:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14764:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14765:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14766:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14767:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14768:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14769:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14770:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14771:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14772:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14773:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14774:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14775:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14776:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14777:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14778:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14779:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14780:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14781:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14782:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14783:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14784:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14785:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14786:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14787:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14788:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14789:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14790:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14791:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14792:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14793:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14794:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14795:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14796:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14797:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14798:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14799:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14800:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14801:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14802:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14803:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14804:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14805:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14806:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14807:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14808:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14809:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14810:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14811:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14812:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14813:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-14814:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14815:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14816:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14817:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14818:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14819:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14820:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14821:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14822:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14823:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14824:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14825:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14826:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14827:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14828:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14829:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14830:

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

.. _no-14831:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14832:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14833:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14834:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14835:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14836:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14837:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14838:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14839:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14840:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14841:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14842:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14843:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14844:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14845:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14846:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14847:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14848:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14849:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-14850:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14851:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14852:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14853:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14854:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14855:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14856:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14857:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14858:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14859:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14860:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14861:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14862:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14863:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14864:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14865:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14866:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14867:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14868:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`Activate <no-14869>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-14870>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-14871>`              Occurs when a child control is created.
:ref:`Close <no-14872>`                  Occurs when the user closes the form.
:ref:`Create <no-14873>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-14874>`             Occurs when another form becomes active.
:ref:`Destroy <no-14875>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-14876>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-14877>`               Occurs when the control gets the focus.
:ref:`Idle <no-14878>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-14879>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-14880>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-14881>`               
:ref:`KeyUp <no-14882>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-14883>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-14884>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-14885>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-14886>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-14887>`             
:ref:`MouseLeave <no-14888>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-14889>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-14890>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-14891>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-14892>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-14893>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-14894>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-14895>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-14896>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-14897>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-14898>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-14899>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-14900>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-14901>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-14902>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-14903>`                   Occurs when the control's position changes.
:ref:`Paint <no-14904>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-14905>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-14906>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-14907>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-14908>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-14869:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-14870:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-14871:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-14872:

**Close** 

Occurs when the user closes the form.



-------

.. _no-14873:

**Create** 

Occurs after the control or form is created.



-------

.. _no-14874:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-14875:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-14876:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-14877:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-14878:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-14879:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-14880:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-14881:

**KeyEvent** 



-------

.. _no-14882:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-14883:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-14884:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-14885:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-14886:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-14887:

**MouseEvent** 



-------

.. _no-14888:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-14889:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-14890:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-14891:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-14892:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-14893:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-14894:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-14895:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-14896:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-14897:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-14898:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-14899:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-14900:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-14901:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-14902:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-14903:

**Move** 

Occurs when the control's position changes.



-------

.. _no-14904:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-14905:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-14906:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-14907:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-14908:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-14909>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-14910>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControlSequence <no-14911>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-14912>`                    Use this method to add controls to the dialog. The standard buttons will be added
:ref:`addObject <no-14913>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-14914>`            
:ref:`afterAddControls <no-14915>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-14916>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-14917>`                   
:ref:`afterSetMenuBar <no-14918>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-14919>`             
:ref:`appendToolBarButton <no-14920>`            
:ref:`autoBindEvents <no-14921>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-14922>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-14923>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-14924>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-14925>`            
:ref:`bindEvent <no-14926>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-14927>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-14928>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-14929>`                   Makes this object topmost
:ref:`clear <no-14930>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-14931>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-14932>`                          This method will close the form. If force = False (default)
:ref:`closing <no-14933>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-14934>`           Given a position relative to this control, return a position relative
:ref:`copy <no-14935>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-14936>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-14937>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-14938>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-14939>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-14940>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-14941>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-14942>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-14943>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-14944>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-14945>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-14946>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-14947>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-14948>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-14949>`                       Draws text on the object at the specified position
:ref:`endHover <no-14950>`                       
:ref:`fillPreferenceDialog <no-14951>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-14952>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-14953>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-14954>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-14955>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-14956>`              
:ref:`formCoordinates <no-14957>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-14958>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-14959>`                      
:ref:`getCaptureBitmap <no-14960>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-14961>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-14962>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-14963>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-14964>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-14965>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-14966>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-14967>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-14968>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-14969>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-14970>`                           Make the object invisible.
:ref:`initEvents <no-14971>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-14972>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-14973>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-14974>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-14975>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-14976>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-14977>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-14978>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-14979>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-14980>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-14981>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-14982>`                        
:ref:`paste <no-14983>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-14984>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-14985>`                    
:ref:`processDroppedFiles <no-14986>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-14987>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-14988>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-14989>`                     Raise the passed Dabo event.
:ref:`reCreate <no-14990>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-14991>`                       Recreate the object.
:ref:`redraw <no-14992>`                         Called when the object is (re)drawn.
:ref:`refresh <no-14993>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-14994>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-14995>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-14996>`                        Need to augment this to make sure the dialog
:ref:`reload <no-14997>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-14998>`              
:ref:`removeFromOutlinedSizers <no-14999>`       
:ref:`restoreSizeAndPosition <no-15000>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-15001>` 
:ref:`runCancel <no-15002>`                      
:ref:`runHelp <no-15003>`                        
:ref:`runNo <no-15004>`                          
:ref:`runOK <no-15005>`                          
:ref:`runYes <no-15006>`                         
:ref:`safeDestroy <no-15007>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-15008>`            Save the current size and position of this form.
:ref:`sendToBack <no-15009>`                     Places this object behind all others.
:ref:`setAll <no-15010>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-15011>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-15012>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-15013>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-15014>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-15015>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-15016>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-15017>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-15018>`                  Set the status text to val.
:ref:`show <no-15019>`                           
:ref:`showContainingPage <no-15020>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-15021>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-15022>`                      Show the dialog modally.
:ref:`showModeless <no-15023>`                   Show the dialog non-modally.
:ref:`super <no-15024>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-15025>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-15026>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-15027>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-15028>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-15029>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods - inherited
=====================

.. _no-14909:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14910:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14911:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.addControlSequence(self, seq)
   :noindex:


   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14912:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.addControls(self)
   :noindex:


   
   Use this method to add controls to the dialog. The standard buttons will be added
   after this method runs, so that they appear at the bottom of the dialog.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-14913:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-14914:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14915:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14916:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14917:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14918:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14919:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14920:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14921:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.autoBindEvents(self, force=True)
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

.. _no-14922:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14923:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14924:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14925:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14926:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14927:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-14928:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-14929:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14930:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14931:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14932:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14933:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14934:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14935:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14936:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14937:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14938:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14939:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14940:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-14941:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14942:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14943:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14944:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14945:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14946:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14947:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14948:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14949:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14950:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14951:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14952:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14953:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14954:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14955:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14956:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14957:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14958:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14959:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14960:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14961:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14962:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14963:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14964:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14965:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14966:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14967:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-14968:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14969:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14970:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14971:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14972:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-14973:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14974:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14975:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14976:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.lockDisplay(self)
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

.. _no-14977:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14978:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14979:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14980:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14981:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14982:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14983:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14984:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14985:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14986:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14987:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14988:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14989:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14990:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-14991:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14992:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14993:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.refresh(self, interval=None)
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

.. _no-14994:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14995:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14996:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-14997:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-14998:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-14999:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15000:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15001:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15002:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.runCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15003:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.runHelp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15004:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.runNo(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15005:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.runOK(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15006:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.runYes(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15007:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15008:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15009:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15010:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-15011:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setEscapeButton(self, btn=None)
   :noindex:


   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-15012:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15013:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15014:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-15015:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-15016:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15017:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15018:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-15019:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15020:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15021:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15022:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15023:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-15024:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15025:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15026:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15027:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15028:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15029:

.. function:: dabo.ui.uiwx.dDialog.dOkCancelDialog.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
