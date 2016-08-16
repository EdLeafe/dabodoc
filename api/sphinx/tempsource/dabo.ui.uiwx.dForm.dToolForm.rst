
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dForm

.. _dabo.ui.uiwx.dForm.dToolForm:

========================================
|doc_title|  **dForm.dToolForm** - class
========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dToolForm**

.. inheritance-diagram:: dToolForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dForm.BaseForm`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dForm.dToolForm

   .. automethod:: dabo.ui.uiwx.dForm.dToolForm.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-27875>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-27876>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-27877>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-27878>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-27879>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-27880>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-27881>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-27882>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-27883>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-27884>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-27885>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-27886>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-27887>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-27888>`                     The caption of the object. (str)
:ref:`Centered <no-27889>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-27890>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-27891>`                    Returns a list of object references to the children of
:ref:`Class <no-27892>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-27893>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-27894>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-27895>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-27896>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-27897>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-27898>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-27899>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-27900>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-27901>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-27902>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-27903>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-27904>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-27905>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-27906>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-27907>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-27908>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-27909>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-27910>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-27911>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-27912>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-27913>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-27914>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-27915>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-27916>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-27917>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-27918>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-27919>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-27920>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-27921>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-27922>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-27923>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-27924>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-27925>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-27926>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-27927>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-27928>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-27929>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-27930>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-27931>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-27932>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-27933>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-27934>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-27935>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-27936>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-27937>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-27938>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-27939>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-27940>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-27941>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-27942>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-27943>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-27944>`                    Specifies the font face. (str)
:ref:`FontInfo <no-27945>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-27946>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-27947>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-27948>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-27949>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-27950>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-27951>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-27952>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-27953>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-27954>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-27955>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-27956>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-27957>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-27958>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-27959>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-27960>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-27961>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-27962>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-27963>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-27964>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-27965>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-27966>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-27967>`                Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-27968>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-27969>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-27970>`                    Specifies the base name of the object.
:ref:`Parent <no-27971>`                      The containing object. (obj)
:ref:`Position <no-27972>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-27973>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-27974>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-27975>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-27976>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-27977>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-27978>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SaveAllRows <no-27979>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-27980>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-27981>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-27982>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-27983>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-27984>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-27985>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-27986>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-27987>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-27988>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-27989>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-27990>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-27991>`                        The size of the object. (tuple)
:ref:`Sizer <no-27992>`                       The sizer for the object.
:ref:`SizersToOutline <no-27993>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-27994>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-27995>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-27996>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-27997>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-27998>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-27999>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-28000>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-28001>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-28002>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-28003>`                         The top position of the object. (int)
:ref:`Transparency <no-28004>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-28005>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-28006>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-28007>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-28008>`                       The width of the object. (int)
:ref:`WindowHandle <no-28009>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-28010>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties - inherited
========================

.. _no-27875:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27876:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27877:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27878:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27879:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27880:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27881:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27882:

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

.. _no-27883:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27884:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27885:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27886:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27887:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27888:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27889:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27890:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27891:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27892:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27893:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27894:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27895:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27896:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27897:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27898:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27899:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27900:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27901:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27902:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27903:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27904:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27905:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27906:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27907:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27908:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27909:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27910:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27911:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27912:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27913:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27914:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27915:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27916:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27917:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27918:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27919:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27920:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27921:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27922:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27923:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27924:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27925:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27926:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27927:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27928:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27929:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27930:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27931:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27932:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27933:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27934:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27935:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27936:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27937:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27938:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27939:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27940:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27941:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27942:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27943:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27944:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27945:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27946:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27947:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27948:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27949:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27950:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27951:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27952:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27953:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27954:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-27955:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27956:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27957:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27958:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27959:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27960:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27961:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27962:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27963:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27964:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27965:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27966:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27967:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27968:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27969:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27970:

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

.. _no-27971:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27972:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27973:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27974:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27975:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27976:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27977:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27978:

**RowNavigationDelay** 

Specifies optional delay to wait for updating the entire form when the user
    is navigating the records. (int; default=0 [ms])

    Set to 0 or None to ensure that all controls reflect immediately to the data changes.
    Setting to a positive non-zero value will result in the following behavior:

    As the row number changes, dEvents.RowNavigation events will fire and the
    afterRowNavigation() hook method will be called, allowing your form code to update a
    specific set of controls so the user knows the records are being navigated. The
    default behavior will reflect the current row number in the form's status bar as
    row navigation is occurring.

    After a navigation and the RowNavigationDelay has passed, the form will be
    completely updated and refreshed. dEvents.RowNumChanged will be fired, and the
    hook afterPointerMove() will be called.

    Recommended setting if non-zero: 250 [ms]. Values under that result in the timer
    firing before the user can navigate again, although this will be dependent on your
    specific situation.
    


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27979:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27980:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27981:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27982:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27983:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27984:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27985:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27986:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27987:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27988:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27989:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27990:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27991:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27992:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27993:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27994:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27995:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27996:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27997:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27998:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27999:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28000:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28001:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-28002:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28003:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28004:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28005:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28006:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28007:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28008:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28009:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28010:

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
:ref:`BackgroundErased <no-28011>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-28012>`                 Occurs after the control or form is created.
:ref:`Destroy <no-28013>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-28014>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-28015>`               Occurs when the control gets the focus.
:ref:`Idle <no-28016>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-28017>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-28018>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-28019>`               
:ref:`KeyUp <no-28020>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-28021>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-28022>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-28023>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-28024>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-28025>`             
:ref:`MouseLeave <no-28026>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-28027>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-28028>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-28029>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-28030>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-28031>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-28032>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-28033>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-28034>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-28035>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-28036>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-28037>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-28038>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-28039>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-28040>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-28041>`                   Occurs when the control's position changes.
:ref:`Paint <no-28042>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-28043>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-28044>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-28045>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-28046>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-28011:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-28012:

**Create** 

Occurs after the control or form is created.



-------

.. _no-28013:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-28014:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-28015:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-28016:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-28017:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-28018:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-28019:

**KeyEvent** 



-------

.. _no-28020:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-28021:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-28022:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-28023:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-28024:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-28025:

**MouseEvent** 



-------

.. _no-28026:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-28027:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-28028:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-28029:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-28030:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-28031:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-28032:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-28033:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-28034:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-28035:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-28036:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-28037:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-28038:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-28039:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-28040:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-28041:

**Move** 

Occurs when the control's position changes.



-------

.. _no-28042:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-28043:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-28044:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-28045:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-28046:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-28047>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-28048>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-28049>`                      Add a bizobj to this form.
:ref:`addObject <no-28050>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-28051>`            
:ref:`afterCancel <no-28052>`                    
:ref:`afterDelete <no-28053>`                    
:ref:`afterDeleteAll <no-28054>`                 
:ref:`afterFilter <no-28055>`                    
:ref:`afterFirst <no-28056>`                     
:ref:`afterInit <no-28057>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-28058>`                   
:ref:`afterLast <no-28059>`                      
:ref:`afterNew <no-28060>`                       
:ref:`afterNext <no-28061>`                      
:ref:`afterPointerMove <no-28062>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-28063>`                     
:ref:`afterRequery <no-28064>`                   
:ref:`afterRowNavigation <no-28065>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-28066>`                      
:ref:`afterSetMenuBar <no-28067>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-28068>`          Subclass hook.
:ref:`afterSetProperties <no-28069>`             
:ref:`appendToolBarButton <no-28070>`            
:ref:`autoBindEvents <no-28071>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-28072>`                   
:ref:`beforeClose <no-28073>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-28074>`                   
:ref:`beforeDeleteAll <no-28075>`                
:ref:`beforeFilter <no-28076>`                   
:ref:`beforeFirst <no-28077>`                    
:ref:`beforeInit <no-28078>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-28079>`                     
:ref:`beforeNew <no-28080>`                      
:ref:`beforeNext <no-28081>`                     
:ref:`beforePointerMove <no-28082>`              
:ref:`beforePrior <no-28083>`                    
:ref:`beforeRequery <no-28084>`                  
:ref:`beforeSave <no-28085>`                     
:ref:`beforeSetProperties <no-28086>`            
:ref:`bindEvent <no-28087>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-28088>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-28089>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-28090>`                   Makes this object topmost
:ref:`cancel <no-28091>`                         Ask the bizobj to cancel its changes.
:ref:`clear <no-28092>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-28093>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-28094>`                          This method will close the form. If force = False (default)
:ref:`closing <no-28095>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-28096>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-28097>`           Given a position relative to this control, return a position relative
:ref:`copy <no-28098>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-28099>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-28100>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-28101>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-28102>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-28103>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-28104>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-28105>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-28106>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-28107>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-28108>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-28109>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-28110>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-28111>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-28112>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-28113>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-28114>`                       Draws text on the object at the specified position
:ref:`endHover <no-28115>`                       
:ref:`fillPreferenceDialog <no-28116>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-28117>`                         Apply a filter to the bizobj's data.
:ref:`first <no-28118>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-28119>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-28120>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-28121>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-28122>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-28123>`              
:ref:`formCoordinates <no-28124>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-28125>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-28126>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-28127>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-28128>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-28129>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-28130>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-28131>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-28132>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-28133>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-28134>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-28135>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-28136>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-28137>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-28138>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-28139>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-28140>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-28141>`                           Make the object invisible.
:ref:`initEvents <no-28142>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-28143>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-28144>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-28145>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-28146>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-28147>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-28148>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-28149>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-28150>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-28151>`                Move the record pointer to the specified row.
:ref:`new <no-28152>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-28153>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-28154>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-28155>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-28156>`                       
:ref:`onDelete <no-28157>`                       
:ref:`onEditRedo <no-28158>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-28159>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-28160>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-28161>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-28162>`                        
:ref:`onHover <no-28163>`                        
:ref:`onLast <no-28164>`                         
:ref:`onNew <no-28165>`                          
:ref:`onNext <no-28166>`                         
:ref:`onPrior <no-28167>`                        
:ref:`onRequery <no-28168>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onSave <no-28169>`                         
:ref:`paste <no-28170>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-28171>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-28172>`                    
:ref:`prior <no-28173>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-28174>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-28175>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-28176>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-28177>`                     Raise the passed Dabo event.
:ref:`reCreate <no-28178>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-28179>`                       Recreate the object.
:ref:`redraw <no-28180>`                         Called when the object is (re)drawn.
:ref:`refresh <no-28181>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-28182>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-28183>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-28184>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-28185>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-28186>`              
:ref:`removeFilter <no-28187>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-28188>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-28189>`       
:ref:`requery <no-28190>`                        Ask the bizobj to requery.
:ref:`restoreSizeAndPosition <no-28191>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-28192>` 
:ref:`safeDestroy <no-28193>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-28194>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-28195>`            Save the current size and position of this form.
:ref:`sendToBack <no-28196>`                     Places this object behind all others.
:ref:`setAll <no-28197>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-28198>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-28199>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-28200>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-28201>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-28202>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-28203>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-28204>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-28205>`                  Set the status text to val.
:ref:`show <no-28206>`                           Make the object visible.
:ref:`showContainingPage <no-28207>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-28208>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-28209>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-28210>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-28211>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-28212>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-28213>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-28214>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-28215>`                         Updates the contained controls with current values from the source.
:ref:`validateField <no-28216>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods - inherited
=====================

.. _no-28047:

.. function:: dabo.ui.uiwx.dForm.dToolForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28048:

.. function:: dabo.ui.uiwx.dForm.dToolForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28049:

.. function:: dabo.ui.uiwx.dForm.dToolForm.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28050:

.. function:: dabo.ui.uiwx.dForm.dToolForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-28051:

.. function:: dabo.ui.uiwx.dForm.dToolForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28052:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28053:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28054:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28055:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28056:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28057:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28058:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28059:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28060:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28061:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28062:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28063:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28064:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28065:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28066:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28067:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28068:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28069:

.. function:: dabo.ui.uiwx.dForm.dToolForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28070:

.. function:: dabo.ui.uiwx.dForm.dToolForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28071:

.. function:: dabo.ui.uiwx.dForm.dToolForm.autoBindEvents(self, force=True)
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

.. _no-28072:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28073:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28074:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28075:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28076:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28077:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28078:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28079:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28080:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28081:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28082:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28083:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28084:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28085:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28086:

.. function:: dabo.ui.uiwx.dForm.dToolForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28087:

.. function:: dabo.ui.uiwx.dForm.dToolForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28088:

.. function:: dabo.ui.uiwx.dForm.dToolForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28089:

.. function:: dabo.ui.uiwx.dForm.dToolForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-28090:

.. function:: dabo.ui.uiwx.dForm.dToolForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28091:

.. function:: dabo.ui.uiwx.dForm.dToolForm.cancel(self, dataSource=None, ignoreNoRecords=None)
   :noindex:


   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28092:

.. function:: dabo.ui.uiwx.dForm.dToolForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28093:

.. function:: dabo.ui.uiwx.dForm.dToolForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28094:

.. function:: dabo.ui.uiwx.dForm.dToolForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28095:

.. function:: dabo.ui.uiwx.dForm.dToolForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28096:

.. function:: dabo.ui.uiwx.dForm.dToolForm.confirmChanges(self, bizobjs=None)
   :noindex:


   
   Ask the user if they want to save changes, discard changes, or cancel.
   
   The user will be queried if the form's CheckForChanges property is True, and
   if there are any pending changes on the form's bizobjs as specified in either
   the 'bizobjs' parameter, or, if no parameter is sent, the return value of
   getBizobjsToCheck().
   
   If all the above are True, the dialog will be presented. "Yes" will cause
   all changes to be saved. "No" will discard any changes before proceeding
   with the operation that caused confirmChanges() to be called in the first
   place (e.g. a requery() or the form being closed). "Cancel" will not save
   any changes, but also cancel the requery or form close.
   
   See also: getBizobjsToCheck() method, CheckForChanges property.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28097:

.. function:: dabo.ui.uiwx.dForm.dToolForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28098:

.. function:: dabo.ui.uiwx.dForm.dToolForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28099:

.. function:: dabo.ui.uiwx.dForm.dToolForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28100:

.. function:: dabo.ui.uiwx.dForm.dToolForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28101:

.. function:: dabo.ui.uiwx.dForm.dToolForm.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28102:

.. function:: dabo.ui.uiwx.dForm.dToolForm.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28103:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28104:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28105:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-28106:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28107:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28108:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28109:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28110:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28111:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28112:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28113:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28114:

.. function:: dabo.ui.uiwx.dForm.dToolForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28115:

.. function:: dabo.ui.uiwx.dForm.dToolForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28116:

.. function:: dabo.ui.uiwx.dForm.dToolForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28117:

.. function:: dabo.ui.uiwx.dForm.dToolForm.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28118:

.. function:: dabo.ui.uiwx.dForm.dToolForm.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28119:

.. function:: dabo.ui.uiwx.dForm.dToolForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28120:

.. function:: dabo.ui.uiwx.dForm.dToolForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28121:

.. function:: dabo.ui.uiwx.dForm.dToolForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28122:

.. function:: dabo.ui.uiwx.dForm.dToolForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28123:

.. function:: dabo.ui.uiwx.dForm.dToolForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28124:

.. function:: dabo.ui.uiwx.dForm.dToolForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28125:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28126:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28127:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getBizobjsToCheck(self)
   :noindex:


   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28128:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28129:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28130:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28131:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28132:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28133:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28134:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28135:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28136:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28137:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-28138:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28139:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28140:

.. function:: dabo.ui.uiwx.dForm.dToolForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28141:

.. function:: dabo.ui.uiwx.dForm.dToolForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28142:

.. function:: dabo.ui.uiwx.dForm.dToolForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28143:

.. function:: dabo.ui.uiwx.dForm.dToolForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28144:

.. function:: dabo.ui.uiwx.dForm.dToolForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28145:

.. function:: dabo.ui.uiwx.dForm.dToolForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28146:

.. function:: dabo.ui.uiwx.dForm.dToolForm.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28147:

.. function:: dabo.ui.uiwx.dForm.dToolForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28148:

.. function:: dabo.ui.uiwx.dForm.dToolForm.lockDisplay(self)
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

.. _no-28149:

.. function:: dabo.ui.uiwx.dForm.dToolForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28150:

.. function:: dabo.ui.uiwx.dForm.dToolForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28151:

.. function:: dabo.ui.uiwx.dForm.dToolForm.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28152:

.. function:: dabo.ui.uiwx.dForm.dToolForm.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28153:

.. function:: dabo.ui.uiwx.dForm.dToolForm.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28154:

.. function:: dabo.ui.uiwx.dForm.dToolForm.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28155:

.. function:: dabo.ui.uiwx.dForm.dToolForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28156:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onCancel(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28157:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onDelete(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28158:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28159:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28160:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28161:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28162:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28163:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28164:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28165:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onNew(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28166:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28167:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28168:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onRequery(self, evt)
   :noindex:


   Occurs when an EVT_MENU event is received by this form.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28169:

.. function:: dabo.ui.uiwx.dForm.dToolForm.onSave(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28170:

.. function:: dabo.ui.uiwx.dForm.dToolForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28171:

.. function:: dabo.ui.uiwx.dForm.dToolForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28172:

.. function:: dabo.ui.uiwx.dForm.dToolForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28173:

.. function:: dabo.ui.uiwx.dForm.dToolForm.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28174:

.. function:: dabo.ui.uiwx.dForm.dToolForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28175:

.. function:: dabo.ui.uiwx.dForm.dToolForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28176:

.. function:: dabo.ui.uiwx.dForm.dToolForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28177:

.. function:: dabo.ui.uiwx.dForm.dToolForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28178:

.. function:: dabo.ui.uiwx.dForm.dToolForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28179:

.. function:: dabo.ui.uiwx.dForm.dToolForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28180:

.. function:: dabo.ui.uiwx.dForm.dToolForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28181:

.. function:: dabo.ui.uiwx.dForm.dToolForm.refresh(self, interval=None)
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

.. _no-28182:

.. function:: dabo.ui.uiwx.dForm.dToolForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28183:

.. function:: dabo.ui.uiwx.dForm.dToolForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28184:

.. function:: dabo.ui.uiwx.dForm.dToolForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28185:

.. function:: dabo.ui.uiwx.dForm.dToolForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28186:

.. function:: dabo.ui.uiwx.dForm.dToolForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28187:

.. function:: dabo.ui.uiwx.dForm.dToolForm.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28188:

.. function:: dabo.ui.uiwx.dForm.dToolForm.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28189:

.. function:: dabo.ui.uiwx.dForm.dToolForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28190:

.. function:: dabo.ui.uiwx.dForm.dToolForm.requery(self, dataSource=None)
   :noindex:


   Ask the bizobj to requery.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28191:

.. function:: dabo.ui.uiwx.dForm.dToolForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28192:

.. function:: dabo.ui.uiwx.dForm.dToolForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28193:

.. function:: dabo.ui.uiwx.dForm.dToolForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28194:

.. function:: dabo.ui.uiwx.dForm.dToolForm.save(self, dataSource=None)
   :noindex:


   Ask the bizobj to commit its changes to the backend.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28195:

.. function:: dabo.ui.uiwx.dForm.dToolForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28196:

.. function:: dabo.ui.uiwx.dForm.dToolForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28197:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-28198:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28199:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28200:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-28201:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-28202:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28203:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28204:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28205:

.. function:: dabo.ui.uiwx.dForm.dToolForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28206:

.. function:: dabo.ui.uiwx.dForm.dToolForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28207:

.. function:: dabo.ui.uiwx.dForm.dToolForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28208:

.. function:: dabo.ui.uiwx.dForm.dToolForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28209:

.. function:: dabo.ui.uiwx.dForm.dToolForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-28210:

.. function:: dabo.ui.uiwx.dForm.dToolForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28211:

.. function:: dabo.ui.uiwx.dForm.dToolForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-28212:

.. function:: dabo.ui.uiwx.dForm.dToolForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28213:

.. function:: dabo.ui.uiwx.dForm.dToolForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28214:

.. function:: dabo.ui.uiwx.dForm.dToolForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28215:

.. function:: dabo.ui.uiwx.dForm.dToolForm.update(self, interval=None)
   :noindex:


   
   Updates the contained controls with current values from the source.
   
   This method is called repeatedly from many different places during
   a single change in the UI, so by default the actual execution is cached
   using callAfterInterval(). The default interval is the value of the
   DataUpdateDelay property, which in turn defaults to 100 milliseconds. You
   can change that to suit your app needs by passing a different interval
   in milliseconds.
   
   Sometimes, though, you want to force immediate execution of the
   update. In these cases, pass an interval of 0 to this method, which
   means don't wait; execute now.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-28216:

.. function:: dabo.ui.uiwx.dForm.dToolForm.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
