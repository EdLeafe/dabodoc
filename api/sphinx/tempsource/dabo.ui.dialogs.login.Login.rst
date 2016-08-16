
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.login

.. _dabo.ui.dialogs.login.Login:

====================================
|doc_title|  **login.Login** - class
====================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Login**

.. inheritance-diagram:: Login


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dOkCancelDialog`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/Login.png
          :scale: 75 %
          :target: _static/macWidgets/Login.png
          :alt: Login



     - .. image:: _static/winWidgets/Login.png
          :scale: 75 %
          :target: _static/winWidgets/Login.png
          :alt: Login



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.login.Login


|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Accepted <no-8848>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-8849>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-8850>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-8851>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-8852>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-8853>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-8854>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-8855>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-8856>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-8857>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-8858>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-8859>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-8860>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-8861>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-8862>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-8863>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-8864>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-8865>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-8866>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-8867>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-8868>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-8869>`                    Returns a list of object references to the children of
:ref:`Class <no-8870>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-8871>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-8872>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-8873>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-8874>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-8875>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-8876>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-8877>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-8878>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-8879>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-8880>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-8881>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-8882>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-8883>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-8884>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-8885>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-8886>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-8887>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-8888>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-8889>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-8890>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-8891>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-8892>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-8893>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-8894>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-8895>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-8896>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-8897>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-8898>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-8899>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-8900>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-8901>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-8902>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-8903>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-8904>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-8905>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-8906>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-8907>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-8908>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-8909>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-8910>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-8911>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-8912>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-8913>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-8914>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-8915>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-8916>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-8917>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-8918>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-8919>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-8920>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-8921>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-8922>`                    Specifies the font face. (str)
:ref:`FontInfo <no-8923>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-8924>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-8925>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-8926>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-8927>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-8928>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-8929>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-8930>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-8931>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-8932>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-8933>`                        Specifies the icon for the form.
:ref:`IconFile <no-8934>`                    Specifies the icon to use.
:ref:`IdleRefreshInterval <no-8935>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-8936>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-8937>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-8938>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-8939>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-8940>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-8941>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-8942>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-8943>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-8944>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-8945>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-8946>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-8947>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-8948>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-8949>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-8950>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-8951>`                    Specifies the base name of the object.
:ref:`NoButton <no-8952>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-8953>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-8954>`                      The containing object. (obj)
:ref:`Position <no-8955>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-8956>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-8957>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-8958>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-8959>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-8960>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-8961>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-8962>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-8963>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-8964>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-8965>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-8966>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-8967>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-8968>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-8969>`                        The size of the object. (tuple)
:ref:`Sizer <no-8970>`                       The sizer for the object.
:ref:`SizersToOutline <no-8971>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-8972>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-8973>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-8974>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-8975>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-8976>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-8977>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-8978>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-8979>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-8980>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-8981>`                         The top position of the object. (int)
:ref:`Transparency <no-8982>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-8983>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-8984>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-8985>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-8986>`                       The width of the object. (int)
:ref:`WindowHandle <no-8987>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-8988>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-8989>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================ ========================


Properties
==========

.. _no-8934:

**IconFile** 

Specifies the icon to use.



-------


Properties - inherited
========================

.. _no-8848:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8849:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8850:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8851:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8852:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8853:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8854:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8855:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8856:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8857:

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

.. _no-8858:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8859:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8860:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8861:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8862:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8863:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8864:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8865:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8866:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8867:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8868:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8869:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8870:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8871:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8872:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8873:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8874:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8875:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8876:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8877:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8878:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8879:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8880:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8881:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8882:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8883:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8884:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8885:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8886:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8887:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8888:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8889:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8890:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8891:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8892:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8893:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8894:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8895:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8896:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8897:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8898:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8899:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8900:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8901:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8902:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8903:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8904:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8905:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8906:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8907:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8908:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8909:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8910:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8911:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8912:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8913:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8914:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8915:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8916:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8917:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8918:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8919:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8920:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8921:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8922:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8923:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8924:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8925:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8926:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8927:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8928:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8929:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8930:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8931:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8932:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8933:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-8935:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8936:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8937:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8938:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8939:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8940:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8941:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8942:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8943:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8944:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8945:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8946:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8947:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8948:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-8949:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8950:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8951:

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

.. _no-8952:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8953:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-8954:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8955:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8956:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8957:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8958:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8959:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8960:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8961:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8962:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8963:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8964:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8965:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8966:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8967:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8968:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8969:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8970:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8971:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8972:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8973:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8974:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8975:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8976:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8977:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8978:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8979:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8980:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8981:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8982:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8983:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8984:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8985:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8986:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8987:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8988:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-8989:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`Activate <no-8990>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-8991>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-8992>`              Occurs when a child control is created.
:ref:`Close <no-8993>`                  Occurs when the user closes the form.
:ref:`Create <no-8994>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-8995>`             Occurs when another form becomes active.
:ref:`Destroy <no-8996>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-8997>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-8998>`               Occurs when the control gets the focus.
:ref:`Idle <no-8999>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-9000>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-9001>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-9002>`               
:ref:`KeyUp <no-9003>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-9004>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-9005>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-9006>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-9007>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-9008>`             
:ref:`MouseLeave <no-9009>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-9010>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-9011>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-9012>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-9013>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-9014>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-9015>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-9016>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-9017>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-9018>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-9019>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-9020>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-9021>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-9022>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-9023>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-9024>`                   Occurs when the control's position changes.
:ref:`Paint <no-9025>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-9026>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-9027>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-9028>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-9029>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-8990:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-8991:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-8992:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-8993:

**Close** 

Occurs when the user closes the form.



-------

.. _no-8994:

**Create** 

Occurs after the control or form is created.



-------

.. _no-8995:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-8996:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-8997:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-8998:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-8999:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-9000:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-9001:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-9002:

**KeyEvent** 



-------

.. _no-9003:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-9004:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-9005:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-9006:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-9007:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-9008:

**MouseEvent** 



-------

.. _no-9009:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-9010:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-9011:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-9012:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-9013:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-9014:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-9015:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-9016:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-9017:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-9018:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-9019:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-9020:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-9021:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-9022:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-9023:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-9024:

**Move** 

Occurs when the control's position changes.



-------

.. _no-9025:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-9026:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-9027:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-9028:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-9029:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-9030>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-9031>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControlSequence <no-9032>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-9033>`                    
:ref:`addObject <no-9034>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-9035>`            
:ref:`afterAddControls <no-9036>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-9037>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-9038>`                   
:ref:`afterSetMenuBar <no-9039>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-9040>`             
:ref:`appendToolBarButton <no-9041>`            
:ref:`autoBindEvents <no-9042>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-9043>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-9044>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-9045>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-9046>`            
:ref:`bindEvent <no-9047>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-9048>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-9049>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-9050>`                   Makes this object topmost
:ref:`clear <no-9051>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-9052>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-9053>`                          This method will close the form. If force = False (default)
:ref:`closing <no-9054>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-9055>`           Given a position relative to this control, return a position relative
:ref:`copy <no-9056>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-9057>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-9058>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-9059>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-9060>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-9061>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-9062>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-9063>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-9064>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-9065>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-9066>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-9067>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-9068>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-9069>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-9070>`                       Draws text on the object at the specified position
:ref:`endHover <no-9071>`                       
:ref:`fillPreferenceDialog <no-9072>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-9073>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-9074>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-9075>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-9076>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-9077>`              
:ref:`formCoordinates <no-9078>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-9079>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-9080>`                      
:ref:`getCaptureBitmap <no-9081>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-9082>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-9083>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-9084>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-9085>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-9086>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-9087>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-9088>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-9089>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-9090>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-9091>`                           Make the object invisible.
:ref:`initEvents <no-9092>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-9093>`                 
:ref:`isContainedBy <no-9094>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-9095>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-9096>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-9097>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-9098>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-9099>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-9100>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-9101>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-9102>`                     If you want your form to respond to the Undo menu item in
:ref:`onEnterKey <no-9103>`                     
:ref:`onHover <no-9104>`                        
:ref:`paste <no-9105>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-9106>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-9107>`                    
:ref:`processDroppedFiles <no-9108>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-9109>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-9110>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-9111>`                     Raise the passed Dabo event.
:ref:`reCreate <no-9112>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-9113>`                       Recreate the object.
:ref:`redraw <no-9114>`                         Called when the object is (re)drawn.
:ref:`refresh <no-9115>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-9116>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-9117>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-9118>`                        Need to augment this to make sure the dialog
:ref:`reload <no-9119>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-9120>`              
:ref:`removeFromOutlinedSizers <no-9121>`       
:ref:`restoreSizeAndPosition <no-9122>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-9123>` 
:ref:`runCancel <no-9124>`                      
:ref:`runHelp <no-9125>`                        
:ref:`runNo <no-9126>`                          
:ref:`runOK <no-9127>`                          
:ref:`runYes <no-9128>`                         
:ref:`safeDestroy <no-9129>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-9130>`            Save the current size and position of this form.
:ref:`sendToBack <no-9131>`                     Places this object behind all others.
:ref:`setAll <no-9132>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-9133>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-9134>`                       Sets focus to the object.
:ref:`setMessage <no-9135>`                     
:ref:`setPositionInSizer <no-9136>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-9137>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-9138>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-9139>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-9140>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-9141>`                  Set the status text to val.
:ref:`show <no-9142>`                           
:ref:`showContainingPage <no-9143>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-9144>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-9145>`                      Show the dialog modally.
:ref:`showModeless <no-9146>`                   Show the dialog non-modally.
:ref:`super <no-9147>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-9148>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-9149>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-9150>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-9151>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-9152>`                         Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-9033:

.. function:: dabo.ui.dialogs.login.Login.addControls(self)



-------

.. _no-9093:

.. function:: dabo.ui.dialogs.login.Login.initProperties(self)



-------

.. _no-9103:

.. function:: dabo.ui.dialogs.login.Login.onEnterKey(self, evt)



-------

.. _no-9124:

.. function:: dabo.ui.dialogs.login.Login.runCancel(self)



-------

.. _no-9127:

.. function:: dabo.ui.dialogs.login.Login.runOK(self)



-------

.. _no-9135:

.. function:: dabo.ui.dialogs.login.Login.setMessage(self, message)



-------


Methods - inherited
=====================

.. _no-9030:

.. function:: dabo.ui.dialogs.login.Login.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9031:

.. function:: dabo.ui.dialogs.login.Login.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9032:

.. function:: dabo.ui.dialogs.login.Login.addControlSequence(self, seq)
   :noindex:


   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9034:

.. function:: dabo.ui.dialogs.login.Login.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-9035:

.. function:: dabo.ui.dialogs.login.Login.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9036:

.. function:: dabo.ui.dialogs.login.Login.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9037:

.. function:: dabo.ui.dialogs.login.Login.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9038:

.. function:: dabo.ui.dialogs.login.Login.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9039:

.. function:: dabo.ui.dialogs.login.Login.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9040:

.. function:: dabo.ui.dialogs.login.Login.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9041:

.. function:: dabo.ui.dialogs.login.Login.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9042:

.. function:: dabo.ui.dialogs.login.Login.autoBindEvents(self, force=True)
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

.. _no-9043:

.. function:: dabo.ui.dialogs.login.Login.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9044:

.. function:: dabo.ui.dialogs.login.Login.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9045:

.. function:: dabo.ui.dialogs.login.Login.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9046:

.. function:: dabo.ui.dialogs.login.Login.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9047:

.. function:: dabo.ui.dialogs.login.Login.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9048:

.. function:: dabo.ui.dialogs.login.Login.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9049:

.. function:: dabo.ui.dialogs.login.Login.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-9050:

.. function:: dabo.ui.dialogs.login.Login.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9051:

.. function:: dabo.ui.dialogs.login.Login.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9052:

.. function:: dabo.ui.dialogs.login.Login.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9053:

.. function:: dabo.ui.dialogs.login.Login.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9054:

.. function:: dabo.ui.dialogs.login.Login.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9055:

.. function:: dabo.ui.dialogs.login.Login.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9056:

.. function:: dabo.ui.dialogs.login.Login.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9057:

.. function:: dabo.ui.dialogs.login.Login.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9058:

.. function:: dabo.ui.dialogs.login.Login.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9059:

.. function:: dabo.ui.dialogs.login.Login.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9060:

.. function:: dabo.ui.dialogs.login.Login.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9061:

.. function:: dabo.ui.dialogs.login.Login.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-9062:

.. function:: dabo.ui.dialogs.login.Login.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9063:

.. function:: dabo.ui.dialogs.login.Login.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9064:

.. function:: dabo.ui.dialogs.login.Login.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9065:

.. function:: dabo.ui.dialogs.login.Login.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9066:

.. function:: dabo.ui.dialogs.login.Login.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9067:

.. function:: dabo.ui.dialogs.login.Login.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9068:

.. function:: dabo.ui.dialogs.login.Login.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9069:

.. function:: dabo.ui.dialogs.login.Login.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9070:

.. function:: dabo.ui.dialogs.login.Login.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9071:

.. function:: dabo.ui.dialogs.login.Login.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9072:

.. function:: dabo.ui.dialogs.login.Login.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9073:

.. function:: dabo.ui.dialogs.login.Login.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9074:

.. function:: dabo.ui.dialogs.login.Login.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9075:

.. function:: dabo.ui.dialogs.login.Login.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9076:

.. function:: dabo.ui.dialogs.login.Login.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9077:

.. function:: dabo.ui.dialogs.login.Login.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9078:

.. function:: dabo.ui.dialogs.login.Login.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9079:

.. function:: dabo.ui.dialogs.login.Login.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9080:

.. function:: dabo.ui.dialogs.login.Login.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9081:

.. function:: dabo.ui.dialogs.login.Login.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9082:

.. function:: dabo.ui.dialogs.login.Login.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9083:

.. function:: dabo.ui.dialogs.login.Login.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9084:

.. function:: dabo.ui.dialogs.login.Login.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9085:

.. function:: dabo.ui.dialogs.login.Login.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9086:

.. function:: dabo.ui.dialogs.login.Login.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9087:

.. function:: dabo.ui.dialogs.login.Login.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9088:

.. function:: dabo.ui.dialogs.login.Login.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-9089:

.. function:: dabo.ui.dialogs.login.Login.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9090:

.. function:: dabo.ui.dialogs.login.Login.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9091:

.. function:: dabo.ui.dialogs.login.Login.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9092:

.. function:: dabo.ui.dialogs.login.Login.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9094:

.. function:: dabo.ui.dialogs.login.Login.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9095:

.. function:: dabo.ui.dialogs.login.Login.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9096:

.. function:: dabo.ui.dialogs.login.Login.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9097:

.. function:: dabo.ui.dialogs.login.Login.lockDisplay(self)
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

.. _no-9098:

.. function:: dabo.ui.dialogs.login.Login.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9099:

.. function:: dabo.ui.dialogs.login.Login.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9100:

.. function:: dabo.ui.dialogs.login.Login.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9101:

.. function:: dabo.ui.dialogs.login.Login.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9102:

.. function:: dabo.ui.dialogs.login.Login.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9104:

.. function:: dabo.ui.dialogs.login.Login.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9105:

.. function:: dabo.ui.dialogs.login.Login.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9106:

.. function:: dabo.ui.dialogs.login.Login.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9107:

.. function:: dabo.ui.dialogs.login.Login.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9108:

.. function:: dabo.ui.dialogs.login.Login.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9109:

.. function:: dabo.ui.dialogs.login.Login.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9110:

.. function:: dabo.ui.dialogs.login.Login.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9111:

.. function:: dabo.ui.dialogs.login.Login.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9112:

.. function:: dabo.ui.dialogs.login.Login.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9113:

.. function:: dabo.ui.dialogs.login.Login.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9114:

.. function:: dabo.ui.dialogs.login.Login.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9115:

.. function:: dabo.ui.dialogs.login.Login.refresh(self, interval=None)
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

.. _no-9116:

.. function:: dabo.ui.dialogs.login.Login.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9117:

.. function:: dabo.ui.dialogs.login.Login.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9118:

.. function:: dabo.ui.dialogs.login.Login.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9119:

.. function:: dabo.ui.dialogs.login.Login.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9120:

.. function:: dabo.ui.dialogs.login.Login.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9121:

.. function:: dabo.ui.dialogs.login.Login.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9122:

.. function:: dabo.ui.dialogs.login.Login.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9123:

.. function:: dabo.ui.dialogs.login.Login.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9125:

.. function:: dabo.ui.dialogs.login.Login.runHelp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9126:

.. function:: dabo.ui.dialogs.login.Login.runNo(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9128:

.. function:: dabo.ui.dialogs.login.Login.runYes(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9129:

.. function:: dabo.ui.dialogs.login.Login.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9130:

.. function:: dabo.ui.dialogs.login.Login.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9131:

.. function:: dabo.ui.dialogs.login.Login.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9132:

.. function:: dabo.ui.dialogs.login.Login.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-9133:

.. function:: dabo.ui.dialogs.login.Login.setEscapeButton(self, btn=None)
   :noindex:


   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9134:

.. function:: dabo.ui.dialogs.login.Login.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9136:

.. function:: dabo.ui.dialogs.login.Login.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9137:

.. function:: dabo.ui.dialogs.login.Login.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-9138:

.. function:: dabo.ui.dialogs.login.Login.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-9139:

.. function:: dabo.ui.dialogs.login.Login.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9140:

.. function:: dabo.ui.dialogs.login.Login.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9141:

.. function:: dabo.ui.dialogs.login.Login.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9142:

.. function:: dabo.ui.dialogs.login.Login.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9143:

.. function:: dabo.ui.dialogs.login.Login.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9144:

.. function:: dabo.ui.dialogs.login.Login.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9145:

.. function:: dabo.ui.dialogs.login.Login.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9146:

.. function:: dabo.ui.dialogs.login.Login.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9147:

.. function:: dabo.ui.dialogs.login.Login.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9148:

.. function:: dabo.ui.dialogs.login.Login.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9149:

.. function:: dabo.ui.dialogs.login.Login.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9150:

.. function:: dabo.ui.dialogs.login.Login.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9151:

.. function:: dabo.ui.dialogs.login.Login.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9152:

.. function:: dabo.ui.dialogs.login.Login.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
