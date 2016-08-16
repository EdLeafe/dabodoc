
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dFormMain

.. _dabo.ui.uiwx.dFormMain.dFormMain:

============================================
|doc_title|  **dFormMain.dFormMain** - class
============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dFormMain**

.. inheritance-diagram:: dFormMain


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dFormMain.dFormMainBase`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dFormMain.png
          :scale: 75 %
          :target: _static/macWidgets/dFormMain.png
          :alt: dFormMain



     - .. image:: _static/winWidgets/dFormMain.png
          :scale: 75 %
          :target: _static/winWidgets/dFormMain.png
          :alt: dFormMain



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dFormMain.dFormMain

   .. automethod:: dabo.ui.uiwx.dFormMain.dFormMain.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-35892>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-35893>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-35894>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-35895>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-35896>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-35897>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-35898>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-35899>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-35900>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-35901>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-35902>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-35903>`                      The position of the bottom side of the object. This is a
:ref:`Caption <no-35904>`                     The caption of the object. (str)
:ref:`Centered <no-35905>`                    Centers the form on the screen when set to True.  (bool)
:ref:`Children <no-35906>`                    Returns a list of object references to the children of
:ref:`Class <no-35907>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-35908>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-35909>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-35910>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-35911>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-35912>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-35913>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-35914>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-35915>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-35916>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-35917>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-35918>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-35919>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-35920>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-35921>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-35922>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-35923>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-35924>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-35925>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-35926>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-35927>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-35928>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-35929>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-35930>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-35931>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-35932>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-35933>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-35934>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-35935>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-35936>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-35937>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-35938>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-35939>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-35940>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-35941>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-35942>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-35943>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-35944>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-35945>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-35946>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-35947>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-35948>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-35949>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-35950>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-35951>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-35952>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-35953>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-35954>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-35955>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-35956>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-35957>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-35958>`                    Specifies the font face. (str)
:ref:`FontInfo <no-35959>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-35960>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-35961>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-35962>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-35963>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-35964>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-35965>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-35966>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-35967>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-35968>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-35969>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-35970>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-35971>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-35972>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-35973>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-35974>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-35975>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-35976>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-35977>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-35978>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-35979>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-35980>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-35981>`                Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-35982>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-35983>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-35984>`                    Specifies the base name of the object.
:ref:`Parent <no-35985>`                      The containing object. (obj)
:ref:`Position <no-35986>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-35987>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-35988>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-35989>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-35990>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-35991>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-35992>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-35993>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-35994>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-35995>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-35996>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-35997>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-35998>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-35999>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-36000>`                        The size of the object. (tuple)
:ref:`Sizer <no-36001>`                       The sizer for the object.
:ref:`SizersToOutline <no-36002>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-36003>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-36004>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-36005>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-36006>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-36007>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-36008>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-36009>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-36010>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-36011>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-36012>`                         The top position of the object. (int)
:ref:`Transparency <no-36013>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-36014>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-36015>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-36016>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-36017>`                       The width of the object. (int)
:ref:`WindowHandle <no-36018>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-36019>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties - inherited
========================

.. _no-35892:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35893:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35894:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35895:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35896:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35897:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35898:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35899:

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

.. _no-35900:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35901:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35902:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35903:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35904:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35905:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35906:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35907:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35908:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35909:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35910:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35911:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35912:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35913:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35914:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35915:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35916:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35917:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35918:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35919:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35920:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35921:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35922:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35923:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35924:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35925:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35926:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35927:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35928:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35929:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35930:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35931:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35932:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35933:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35934:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35935:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35936:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35937:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35938:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35939:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35940:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35941:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35942:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35943:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35944:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35945:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35946:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35947:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35948:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35949:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35950:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35951:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35952:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35953:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35954:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35955:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35956:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35957:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35958:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35959:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35960:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35961:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35962:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35963:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35964:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35965:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35966:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35967:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35968:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-35969:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35970:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35971:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35972:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35973:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35974:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35975:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35976:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-35977:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35978:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35979:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35980:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35981:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35982:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35983:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35984:

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

.. _no-35985:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35986:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35987:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35988:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35989:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35990:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35991:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35992:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35993:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35994:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35995:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35996:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35997:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35998:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-35999:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36000:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-36001:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-36002:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36003:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-36004:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36005:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36006:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36007:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36008:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36009:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36010:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-36011:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36012:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36013:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36014:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36015:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36016:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36017:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36018:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36019:

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
:ref:`Activate <no-36020>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-36021>`       Occurs when a window background has been erased and needs repainting.
:ref:`Close <no-36022>`                  Occurs when the user closes the form.
:ref:`Create <no-36023>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-36024>`             Occurs when another form becomes active.
:ref:`Destroy <no-36025>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-36026>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-36027>`               Occurs when the control gets the focus.
:ref:`Idle <no-36028>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-36029>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-36030>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-36031>`               
:ref:`KeyUp <no-36032>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-36033>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-36034>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-36035>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-36036>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-36037>`             
:ref:`MouseLeave <no-36038>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-36039>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-36040>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-36041>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-36042>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-36043>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-36044>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-36045>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-36046>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-36047>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-36048>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-36049>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-36050>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-36051>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-36052>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-36053>`                   Occurs when the control's position changes.
:ref:`Paint <no-36054>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-36055>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-36056>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-36057>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-36058>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-36020:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-36021:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-36022:

**Close** 

Occurs when the user closes the form.



-------

.. _no-36023:

**Create** 

Occurs after the control or form is created.



-------

.. _no-36024:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-36025:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-36026:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-36027:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-36028:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-36029:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-36030:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-36031:

**KeyEvent** 



-------

.. _no-36032:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-36033:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-36034:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-36035:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-36036:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-36037:

**MouseEvent** 



-------

.. _no-36038:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-36039:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-36040:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-36041:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-36042:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-36043:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-36044:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-36045:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-36046:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-36047:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-36048:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-36049:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-36050:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-36051:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-36052:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-36053:

**Move** 

Occurs when the control's position changes.



-------

.. _no-36054:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-36055:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-36056:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-36057:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-36058:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-36059>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-36060>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addObject <no-36061>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-36062>`            
:ref:`afterInit <no-36063>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-36064>`                   
:ref:`afterSetMenuBar <no-36065>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-36066>`             
:ref:`appendToolBarButton <no-36067>`            
:ref:`autoBindEvents <no-36068>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeClose <no-36069>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-36070>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-36071>`            
:ref:`bindEvent <no-36072>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-36073>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-36074>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-36075>`                   Makes this object topmost
:ref:`clear <no-36076>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-36077>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-36078>`                          This method will close the form. If force = False (default)
:ref:`closing <no-36079>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-36080>`           Given a position relative to this control, return a position relative
:ref:`copy <no-36081>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-36082>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-36083>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-36084>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-36085>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-36086>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-36087>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-36088>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-36089>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-36090>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-36091>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-36092>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-36093>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-36094>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-36095>`                       Draws text on the object at the specified position
:ref:`endHover <no-36096>`                       
:ref:`fillPreferenceDialog <no-36097>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-36098>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-36099>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-36100>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-36101>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-36102>`              
:ref:`formCoordinates <no-36103>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-36104>`                Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-36105>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-36106>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-36107>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-36108>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-36109>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-36110>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-36111>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-36112>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-36113>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-36114>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-36115>`                           Make the object invisible.
:ref:`initEvents <no-36116>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-36117>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-36118>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-36119>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-36120>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-36121>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-36122>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-36123>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-36124>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-36125>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-36126>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-36127>`                        
:ref:`paste <no-36128>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-36129>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-36130>`                    
:ref:`processDroppedFiles <no-36131>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-36132>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-36133>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-36134>`                     Raise the passed Dabo event.
:ref:`reCreate <no-36135>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-36136>`                       Recreate the object.
:ref:`redraw <no-36137>`                         Called when the object is (re)drawn.
:ref:`refresh <no-36138>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-36139>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-36140>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-36141>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-36142>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-36143>`              
:ref:`removeFromOutlinedSizers <no-36144>`       
:ref:`restoreSizeAndPosition <no-36145>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-36146>` 
:ref:`safeDestroy <no-36147>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-36148>`            Save the current size and position of this form.
:ref:`sendToBack <no-36149>`                     Places this object behind all others.
:ref:`setAll <no-36150>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-36151>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-36152>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-36153>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-36154>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-36155>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-36156>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-36157>`                  Set the status text to val.
:ref:`show <no-36158>`                           Make the object visible.
:ref:`showContainingPage <no-36159>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-36160>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-36161>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-36162>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-36163>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-36164>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-36165>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-36166>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-36167>`                         Update the properties of this object and all contained objects.

================================================ ========================


Methods - inherited
=====================

.. _no-36059:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36060:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36061:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-36062:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36063:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36064:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36065:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36066:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36067:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36068:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.autoBindEvents(self, force=True)
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

.. _no-36069:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36070:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36071:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36072:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-36073:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-36074:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-36075:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36076:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36077:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36078:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36079:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36080:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36081:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36082:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36083:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36084:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36085:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36086:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-36087:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36088:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36089:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36090:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36091:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36092:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36093:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36094:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36095:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36096:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36097:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36098:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36099:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36100:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36101:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36102:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36103:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36104:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36105:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36106:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36107:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36108:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36109:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36110:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36111:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36112:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-36113:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36114:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36115:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36116:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36117:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36118:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36119:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36120:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36121:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.lockDisplay(self)
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

.. _no-36122:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36123:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36124:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36125:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36126:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36127:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36128:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36129:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36130:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36131:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36132:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36133:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36134:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36135:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-36136:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36137:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36138:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.refresh(self, interval=None)
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

.. _no-36139:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36140:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36141:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36142:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36143:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36144:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36145:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36146:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36147:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36148:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36149:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36150:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-36151:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36152:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36153:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-36154:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-36155:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36156:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36157:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36158:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36159:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36160:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36161:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-36162:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36163:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-36164:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36165:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36166:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-36167:

.. function:: dabo.ui.uiwx.dFormMain.dFormMain.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
