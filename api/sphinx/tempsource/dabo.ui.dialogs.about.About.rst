
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.about

.. _dabo.ui.dialogs.about.About:

====================================
|doc_title|  **about.About** - class
====================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **About**

.. inheritance-diagram:: About


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDialog.dDialog`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/About.png
          :scale: 75 %
          :target: _static/macWidgets/About.png
          :alt: About



     - .. image:: _static/winWidgets/About.png
          :scale: 75 %
          :target: _static/winWidgets/About.png
          :alt: About



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.about.About


|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`DynamicFont <no-10000>`                Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-10001>`            Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-10002>`            Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-10003>`          Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-10004>`            Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-10005>`       Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-10006>`           Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-10007>`              Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-10008>`                Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-10009>`                Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-10010>`             Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-10011>`        Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-10012>`            Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-10013>`         Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-10014>`       Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-10015>`                Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-10016>`           Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-10017>`          Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-10018>`                 Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-10019>`             Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-10020>`         Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-10021>`                 Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-10022>`        Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-10023>`             Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-10024>`               Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-10025>`         Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-10026>`                    Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-10027>`              Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-10028>`              Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-10029>`                       Specifies font object for this control. (dFont)
:ref:`FontBold <no-10030>`                   Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-10031>`            Human-readable description of the current font settings. (str)
:ref:`FontFace <no-10032>`                   Specifies the font face. (str)
:ref:`FontInfo <no-10033>`                   Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-10034>`                 Specifies whether font is italicized. (bool)
:ref:`FontSize <no-10035>`                   Specifies the point size of the font. (int)
:ref:`FontUnderline <no-10036>`              Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-10037>`                  Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-10038>`                       Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-10039>`                     Specifies the height of the object. (int)
:ref:`HelpContextText <no-10040>`            Specifies the context-sensitive help text associated with this
:ref:`Hover <no-10041>`                      When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-10042>`                       Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-10043>`        Controls how often the form is refreshed when idle.
:ref:`Left <no-10044>`                       Specifies the left position of the object. (int)
:ref:`LogEvents <no-10045>`                  Specifies which events to log.  (list of strings)
:ref:`MDI <no-10046>`                        Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-10047>`              Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-10048>`                Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-10049>`               Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-10050>`                    Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-10051>`               Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-10052>`                Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-10053>`              Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-10054>`                Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-10055>`               Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-10056>`                      Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-10057>`               Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-10058>`                       Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-10059>`                   Specifies the base name of the object.
:ref:`Parent <no-10060>`                     The containing object. (obj)
:ref:`Position <no-10061>`                   The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-10062>`          Reference to the Preference Management object  (dPref)
:ref:`RegID <no-10063>`                      A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-10064>`                      The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-10065>`        Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-10066>`                Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-10067>`            Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-10068>`              Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-10069>`              Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-10070>`                Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-10071>`              Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-10072>`              Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-10073>`             Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-10074>`                Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-10075>`                       The size of the object. (tuple)
:ref:`Sizer <no-10076>`                      The sizer for the object.
:ref:`SizersToOutline <no-10077>`            When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-10078>`                  Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-10079>`             Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-10080>`                 Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-10081>`                  Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-10082>`                        A property that user code can safely use for specific purposes.
:ref:`TempForm <no-10083>`                   Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-10084>`               Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-10085>`                    Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-10086>`                Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-10087>`                        The top position of the object. (int)
:ref:`Transparency <no-10088>`               Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-10089>`          Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-10090>`                    Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-10091>`            Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-10092>`                      The width of the object. (int)
:ref:`WindowHandle <no-10093>`               The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-10094>`                Specifies the current state of the form. (int)
:ref:`ActiveControl <no-9963>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-9964>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-9965>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-9966>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-9967>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-9968>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-9969>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-9970>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-9971>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-9972>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-9973>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-9974>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-9975>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-9976>`                      The position of the bottom side of the object. This is a
:ref:`Caption <no-9977>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-9978>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-9979>`                    Returns a list of object references to the children of
:ref:`Class <no-9980>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-9981>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-9982>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-9983>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-9984>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-9985>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-9986>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-9987>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-9988>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-9989>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-9990>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-9991>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-9992>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-9993>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-9994>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-9995>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-9996>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-9997>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-9998>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-9999>`        Dynamically determine the value of the FloatOnParent property.

============================================ ========================


Properties - inherited
========================

.. _no-9963:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9964:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9965:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9966:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9967:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9968:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9969:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9970:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9971:

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

.. _no-9972:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9973:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9974:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9975:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9976:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9977:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9978:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9979:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9980:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9981:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9982:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9983:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9984:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9985:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9986:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9987:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9988:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9989:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9990:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9991:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9992:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9993:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9994:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9995:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9996:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9997:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9998:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9999:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10000:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10001:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10002:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10003:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10004:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10005:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10006:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10007:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10008:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10009:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10010:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10011:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10012:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10013:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10014:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10015:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10016:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10017:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10018:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10019:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10020:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10021:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10022:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10023:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10024:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10025:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10026:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10027:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10028:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10029:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10030:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10031:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10032:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10033:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10034:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10035:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10036:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10037:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10038:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10039:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10040:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10041:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10042:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-10043:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10044:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10045:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10046:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10047:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10048:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10049:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10050:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10051:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10052:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10053:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10054:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10055:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10056:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10057:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10058:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10059:

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

.. _no-10060:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10061:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10062:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10063:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10064:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10065:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10066:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10067:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10068:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10069:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10070:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10071:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10072:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10073:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10074:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10075:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10076:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-10077:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10078:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10079:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10080:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10081:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10082:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10083:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10084:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10085:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10086:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10087:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10088:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10089:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10090:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10091:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10092:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10093:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10094:

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
:ref:`Activate <no-10095>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-10096>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-10097>`              Occurs when a child control is created.
:ref:`Close <no-10098>`                  Occurs when the user closes the form.
:ref:`Create <no-10099>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-10100>`             Occurs when another form becomes active.
:ref:`Destroy <no-10101>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-10102>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-10103>`               Occurs when the control gets the focus.
:ref:`Idle <no-10104>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-10105>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-10106>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-10107>`               
:ref:`KeyUp <no-10108>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-10109>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-10110>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-10111>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-10112>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-10113>`             
:ref:`MouseLeave <no-10114>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-10115>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-10116>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-10117>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-10118>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-10119>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-10120>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-10121>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-10122>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-10123>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-10124>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-10125>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-10126>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-10127>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-10128>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-10129>`                   Occurs when the control's position changes.
:ref:`Paint <no-10130>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-10131>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-10132>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-10133>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-10134>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-10095:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-10096:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-10097:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-10098:

**Close** 

Occurs when the user closes the form.



-------

.. _no-10099:

**Create** 

Occurs after the control or form is created.



-------

.. _no-10100:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-10101:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-10102:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-10103:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-10104:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-10105:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-10106:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-10107:

**KeyEvent** 



-------

.. _no-10108:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-10109:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-10110:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-10111:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-10112:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-10113:

**MouseEvent** 



-------

.. _no-10114:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-10115:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-10116:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-10117:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-10118:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-10119:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-10120:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-10121:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-10122:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-10123:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-10124:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-10125:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-10126:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-10127:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-10128:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-10129:

**Move** 

Occurs when the control's position changes.



-------

.. _no-10130:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-10131:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-10132:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-10133:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-10134:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-10135>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-10136>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControls <no-10137>`                    
:ref:`addObject <no-10138>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-10139>`            
:ref:`afterAddControls <no-10140>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-10141>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-10142>`                   
:ref:`afterSetMenuBar <no-10143>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-10144>`             
:ref:`appendToolBarButton <no-10145>`            
:ref:`autoBindEvents <no-10146>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-10147>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-10148>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-10149>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-10150>`            
:ref:`bindEvent <no-10151>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-10152>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-10153>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-10154>`                   Makes this object topmost
:ref:`clear <no-10155>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-10156>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-10157>`                          This method will close the form. If force = False (default)
:ref:`closing <no-10158>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-10159>`           Given a position relative to this control, return a position relative
:ref:`copy <no-10160>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-10161>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-10162>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-10163>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-10164>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-10165>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-10166>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-10167>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-10168>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-10169>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-10170>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-10171>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-10172>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-10173>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-10174>`                       Draws text on the object at the specified position
:ref:`endHover <no-10175>`                       
:ref:`fillPreferenceDialog <no-10176>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-10177>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-10178>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-10179>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-10180>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-10181>`              
:ref:`formCoordinates <no-10182>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-10183>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-10184>`                      
:ref:`getCaptureBitmap <no-10185>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-10186>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-10187>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-10188>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-10189>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-10190>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-10191>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-10192>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-10193>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-10194>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-10195>`                           Make the object invisible.
:ref:`initEvents <no-10196>`                     
:ref:`initProperties <no-10197>`                 
:ref:`isContainedBy <no-10198>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-10199>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-10200>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-10201>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-10202>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-10203>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-10204>`              Given a position relative to the form, return a position relative
:ref:`onClear <no-10205>`                        
:ref:`onClose <no-10206>`                        
:ref:`onCopyInfo <no-10207>`                     Copy the system information to the Clipboard
:ref:`onEditRedo <no-10208>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-10209>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-10210>`                        
:ref:`paste <no-10211>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-10212>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-10213>`                    
:ref:`processDroppedFiles <no-10214>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-10215>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-10216>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-10217>`                     Raise the passed Dabo event.
:ref:`reCreate <no-10218>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-10219>`                       Recreate the object.
:ref:`redraw <no-10220>`                         Called when the object is (re)drawn.
:ref:`refresh <no-10221>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-10222>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-10223>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-10224>`                        Need to augment this to make sure the dialog
:ref:`reload <no-10225>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-10226>`              
:ref:`removeFromOutlinedSizers <no-10227>`       
:ref:`restoreSizeAndPosition <no-10228>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-10229>` 
:ref:`safeDestroy <no-10230>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-10231>`            Save the current size and position of this form.
:ref:`sendToBack <no-10232>`                     Places this object behind all others.
:ref:`setAll <no-10233>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-10234>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-10235>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-10236>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-10237>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-10238>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-10239>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-10240>`                  Set the status text to val.
:ref:`show <no-10241>`                           
:ref:`showContainingPage <no-10242>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-10243>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-10244>`                      Show the dialog modally.
:ref:`showModeless <no-10245>`                   Show the dialog non-modally.
:ref:`super <no-10246>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-10247>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-10248>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-10249>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-10250>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-10251>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods
=======

.. _no-10137:

.. function:: dabo.ui.dialogs.about.About.addControls(self)



-------

.. _no-10196:

.. function:: dabo.ui.dialogs.about.About.initEvents(self)



-------

.. _no-10197:

.. function:: dabo.ui.dialogs.about.About.initProperties(self)



-------

.. _no-10205:

.. function:: dabo.ui.dialogs.about.About.onClear(self, evt)



-------

.. _no-10206:

.. function:: dabo.ui.dialogs.about.About.onClose(self, evt=None)



-------

.. _no-10207:

.. function:: dabo.ui.dialogs.about.About.onCopyInfo(self, evt)

   Copy the system information to the Clipboard



-------


Methods - inherited
=====================

.. _no-10135:

.. function:: dabo.ui.dialogs.about.About.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10136:

.. function:: dabo.ui.dialogs.about.About.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10138:

.. function:: dabo.ui.dialogs.about.About.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-10139:

.. function:: dabo.ui.dialogs.about.About.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10140:

.. function:: dabo.ui.dialogs.about.About.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10141:

.. function:: dabo.ui.dialogs.about.About.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10142:

.. function:: dabo.ui.dialogs.about.About.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10143:

.. function:: dabo.ui.dialogs.about.About.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10144:

.. function:: dabo.ui.dialogs.about.About.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10145:

.. function:: dabo.ui.dialogs.about.About.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10146:

.. function:: dabo.ui.dialogs.about.About.autoBindEvents(self, force=True)
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

.. _no-10147:

.. function:: dabo.ui.dialogs.about.About.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10148:

.. function:: dabo.ui.dialogs.about.About.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10149:

.. function:: dabo.ui.dialogs.about.About.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10150:

.. function:: dabo.ui.dialogs.about.About.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10151:

.. function:: dabo.ui.dialogs.about.About.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10152:

.. function:: dabo.ui.dialogs.about.About.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10153:

.. function:: dabo.ui.dialogs.about.About.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-10154:

.. function:: dabo.ui.dialogs.about.About.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10155:

.. function:: dabo.ui.dialogs.about.About.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10156:

.. function:: dabo.ui.dialogs.about.About.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10157:

.. function:: dabo.ui.dialogs.about.About.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10158:

.. function:: dabo.ui.dialogs.about.About.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10159:

.. function:: dabo.ui.dialogs.about.About.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10160:

.. function:: dabo.ui.dialogs.about.About.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10161:

.. function:: dabo.ui.dialogs.about.About.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10162:

.. function:: dabo.ui.dialogs.about.About.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10163:

.. function:: dabo.ui.dialogs.about.About.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10164:

.. function:: dabo.ui.dialogs.about.About.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10165:

.. function:: dabo.ui.dialogs.about.About.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-10166:

.. function:: dabo.ui.dialogs.about.About.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10167:

.. function:: dabo.ui.dialogs.about.About.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10168:

.. function:: dabo.ui.dialogs.about.About.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10169:

.. function:: dabo.ui.dialogs.about.About.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10170:

.. function:: dabo.ui.dialogs.about.About.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10171:

.. function:: dabo.ui.dialogs.about.About.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10172:

.. function:: dabo.ui.dialogs.about.About.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10173:

.. function:: dabo.ui.dialogs.about.About.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10174:

.. function:: dabo.ui.dialogs.about.About.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10175:

.. function:: dabo.ui.dialogs.about.About.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10176:

.. function:: dabo.ui.dialogs.about.About.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10177:

.. function:: dabo.ui.dialogs.about.About.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10178:

.. function:: dabo.ui.dialogs.about.About.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10179:

.. function:: dabo.ui.dialogs.about.About.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10180:

.. function:: dabo.ui.dialogs.about.About.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10181:

.. function:: dabo.ui.dialogs.about.About.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10182:

.. function:: dabo.ui.dialogs.about.About.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10183:

.. function:: dabo.ui.dialogs.about.About.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10184:

.. function:: dabo.ui.dialogs.about.About.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10185:

.. function:: dabo.ui.dialogs.about.About.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10186:

.. function:: dabo.ui.dialogs.about.About.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10187:

.. function:: dabo.ui.dialogs.about.About.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10188:

.. function:: dabo.ui.dialogs.about.About.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10189:

.. function:: dabo.ui.dialogs.about.About.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10190:

.. function:: dabo.ui.dialogs.about.About.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10191:

.. function:: dabo.ui.dialogs.about.About.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10192:

.. function:: dabo.ui.dialogs.about.About.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-10193:

.. function:: dabo.ui.dialogs.about.About.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10194:

.. function:: dabo.ui.dialogs.about.About.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10195:

.. function:: dabo.ui.dialogs.about.About.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10198:

.. function:: dabo.ui.dialogs.about.About.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10199:

.. function:: dabo.ui.dialogs.about.About.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10200:

.. function:: dabo.ui.dialogs.about.About.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10201:

.. function:: dabo.ui.dialogs.about.About.lockDisplay(self)
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

.. _no-10202:

.. function:: dabo.ui.dialogs.about.About.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10203:

.. function:: dabo.ui.dialogs.about.About.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10204:

.. function:: dabo.ui.dialogs.about.About.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10208:

.. function:: dabo.ui.dialogs.about.About.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10209:

.. function:: dabo.ui.dialogs.about.About.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10210:

.. function:: dabo.ui.dialogs.about.About.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10211:

.. function:: dabo.ui.dialogs.about.About.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10212:

.. function:: dabo.ui.dialogs.about.About.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10213:

.. function:: dabo.ui.dialogs.about.About.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10214:

.. function:: dabo.ui.dialogs.about.About.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10215:

.. function:: dabo.ui.dialogs.about.About.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10216:

.. function:: dabo.ui.dialogs.about.About.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10217:

.. function:: dabo.ui.dialogs.about.About.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10218:

.. function:: dabo.ui.dialogs.about.About.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-10219:

.. function:: dabo.ui.dialogs.about.About.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10220:

.. function:: dabo.ui.dialogs.about.About.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10221:

.. function:: dabo.ui.dialogs.about.About.refresh(self, interval=None)
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

.. _no-10222:

.. function:: dabo.ui.dialogs.about.About.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10223:

.. function:: dabo.ui.dialogs.about.About.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10224:

.. function:: dabo.ui.dialogs.about.About.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10225:

.. function:: dabo.ui.dialogs.about.About.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10226:

.. function:: dabo.ui.dialogs.about.About.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10227:

.. function:: dabo.ui.dialogs.about.About.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10228:

.. function:: dabo.ui.dialogs.about.About.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10229:

.. function:: dabo.ui.dialogs.about.About.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10230:

.. function:: dabo.ui.dialogs.about.About.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10231:

.. function:: dabo.ui.dialogs.about.About.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10232:

.. function:: dabo.ui.dialogs.about.About.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10233:

.. function:: dabo.ui.dialogs.about.About.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-10234:

.. function:: dabo.ui.dialogs.about.About.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10235:

.. function:: dabo.ui.dialogs.about.About.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10236:

.. function:: dabo.ui.dialogs.about.About.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-10237:

.. function:: dabo.ui.dialogs.about.About.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-10238:

.. function:: dabo.ui.dialogs.about.About.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10239:

.. function:: dabo.ui.dialogs.about.About.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10240:

.. function:: dabo.ui.dialogs.about.About.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-10241:

.. function:: dabo.ui.dialogs.about.About.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10242:

.. function:: dabo.ui.dialogs.about.About.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10243:

.. function:: dabo.ui.dialogs.about.About.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10244:

.. function:: dabo.ui.dialogs.about.About.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10245:

.. function:: dabo.ui.dialogs.about.About.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-10246:

.. function:: dabo.ui.dialogs.about.About.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-10247:

.. function:: dabo.ui.dialogs.about.About.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-10248:

.. function:: dabo.ui.dialogs.about.About.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10249:

.. function:: dabo.ui.dialogs.about.About.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10250:

.. function:: dabo.ui.dialogs.about.About.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-10251:

.. function:: dabo.ui.dialogs.about.About.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
