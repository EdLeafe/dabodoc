
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dForm

.. _dabo.ui.uiwx.dForm.BaseForm:

=======================================
|doc_title|  **dForm.BaseForm** - class
=======================================


Creates a bizobj-aware form.

dForm knows how to handle one or more dBizobjs, providing proxy methods
like next(), last(), save(), and requery().




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **BaseForm**

.. inheritance-diagram:: BaseForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dForm.dBorderlessForm`
* :ref:`dabo.ui.uiwx.dForm.dForm`
* :ref:`dabo.ui.uiwx.dForm.dToolForm`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dForm.BaseForm

   .. automethod:: dabo.ui.uiwx.dForm.BaseForm.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-26843>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-26844>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-26845>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-26846>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-26847>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-26848>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-26849>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-26850>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-26851>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-26852>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-26853>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-26854>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-26855>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-26856>`                     The caption of the object. (str)
:ref:`Centered <no-26857>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-26858>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-26859>`                    Returns a list of object references to the children of
:ref:`Class <no-26860>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-26861>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-26862>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-26863>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-26864>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-26865>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-26866>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-26867>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-26868>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-26869>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-26870>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-26871>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-26872>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-26873>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-26874>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-26875>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-26876>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-26877>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-26878>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-26879>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-26880>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-26881>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-26882>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-26883>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-26884>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-26885>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-26886>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-26887>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-26888>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-26889>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-26890>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-26891>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-26892>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-26893>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-26894>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-26895>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-26896>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-26897>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-26898>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-26899>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-26900>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-26901>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-26902>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-26903>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-26904>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-26905>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-26906>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-26907>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-26908>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-26909>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-26910>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-26911>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-26912>`                    Specifies the font face. (str)
:ref:`FontInfo <no-26913>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-26914>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-26915>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-26916>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-26917>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-26918>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-26919>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-26920>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-26921>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-26922>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-26923>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-26924>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-26925>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-26926>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-26927>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-26928>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-26929>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-26930>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-26931>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-26932>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-26933>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-26934>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-26935>`                Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-26936>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-26937>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-26938>`                    Specifies the base name of the object.
:ref:`Parent <no-26939>`                      The containing object. (obj)
:ref:`Position <no-26940>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-26941>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-26942>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-26943>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-26944>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-26945>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-26946>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SaveAllRows <no-26947>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-26948>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-26949>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-26950>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-26951>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-26952>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-26953>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-26954>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-26955>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-26956>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-26957>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-26958>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-26959>`                        The size of the object. (tuple)
:ref:`Sizer <no-26960>`                       The sizer for the object.
:ref:`SizersToOutline <no-26961>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-26962>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-26963>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-26964>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-26965>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-26966>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-26967>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-26968>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-26969>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-26970>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-26971>`                         The top position of the object. (int)
:ref:`Transparency <no-26972>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-26973>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-26974>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-26975>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-26976>`                       The width of the object. (int)
:ref:`WindowHandle <no-26977>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-26978>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties
==========

.. _no-26855:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)



-------

.. _no-26858:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.



-------

.. _no-26865:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..



-------

.. _no-26942:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)



-------

.. _no-26944:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)



-------

.. _no-26946:

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
    



-------

.. _no-26947:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)



-------

.. _no-26948:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)



-------


Properties - inherited
========================

.. _no-26843:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26844:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26845:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26846:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26847:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26848:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26849:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26850:

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

.. _no-26851:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26852:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26853:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26854:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26856:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26857:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26859:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26860:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26861:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26862:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26863:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26864:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26866:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26867:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26868:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26869:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26870:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26871:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26872:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26873:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26874:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26875:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26876:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26877:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26878:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26879:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26880:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26881:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26882:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26883:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26884:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26885:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26886:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26887:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26888:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26889:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26890:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26891:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26892:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26893:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26894:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26895:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26896:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26897:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26898:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26899:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26900:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26901:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26902:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26903:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26904:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26905:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26906:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26907:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26908:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26909:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26910:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26911:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26912:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26913:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26914:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26915:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26916:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26917:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26918:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26919:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26920:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26921:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26922:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26923:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26924:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26925:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26926:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26927:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26928:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26929:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26930:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26931:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26932:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26933:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26934:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26935:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26936:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26937:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26938:

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

.. _no-26939:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26940:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26941:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26943:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26945:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26949:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26950:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26951:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26952:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26953:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26954:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26955:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26956:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26957:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26958:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26959:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26960:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26961:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26962:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26963:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26964:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26965:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26966:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26967:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26968:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26969:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-26970:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26971:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26972:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26973:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26974:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26975:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26976:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26977:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26978:

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
:ref:`BackgroundErased <no-26979>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-26980>`                 Occurs after the control or form is created.
:ref:`Destroy <no-26981>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-26982>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-26983>`               Occurs when the control gets the focus.
:ref:`Idle <no-26984>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-26985>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-26986>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-26987>`               
:ref:`KeyUp <no-26988>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-26989>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-26990>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-26991>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-26992>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-26993>`             
:ref:`MouseLeave <no-26994>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-26995>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-26996>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-26997>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-26998>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-26999>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-27000>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-27001>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-27002>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-27003>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-27004>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-27005>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-27006>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-27007>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-27008>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-27009>`                   Occurs when the control's position changes.
:ref:`Paint <no-27010>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-27011>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-27012>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-27013>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-27014>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-26979:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-26980:

**Create** 

Occurs after the control or form is created.



-------

.. _no-26981:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-26982:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-26983:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-26984:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-26985:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-26986:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-26987:

**KeyEvent** 



-------

.. _no-26988:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-26989:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-26990:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-26991:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-26992:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-26993:

**MouseEvent** 



-------

.. _no-26994:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-26995:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-26996:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-26997:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-26998:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-26999:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-27000:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-27001:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-27002:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-27003:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-27004:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-27005:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-27006:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-27007:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-27008:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-27009:

**Move** 

Occurs when the control's position changes.



-------

.. _no-27010:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-27011:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-27012:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-27013:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-27014:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-27015>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-27016>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-27017>`                      Add a bizobj to this form.
:ref:`addObject <no-27018>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-27019>`            
:ref:`afterCancel <no-27020>`                    
:ref:`afterDelete <no-27021>`                    
:ref:`afterDeleteAll <no-27022>`                 
:ref:`afterFilter <no-27023>`                    
:ref:`afterFirst <no-27024>`                     
:ref:`afterInit <no-27025>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-27026>`                   
:ref:`afterLast <no-27027>`                      
:ref:`afterNew <no-27028>`                       
:ref:`afterNext <no-27029>`                      
:ref:`afterPointerMove <no-27030>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-27031>`                     
:ref:`afterRequery <no-27032>`                   
:ref:`afterRowNavigation <no-27033>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-27034>`                      
:ref:`afterSetMenuBar <no-27035>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-27036>`          Subclass hook.
:ref:`afterSetProperties <no-27037>`             
:ref:`appendToolBarButton <no-27038>`            
:ref:`autoBindEvents <no-27039>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-27040>`                   
:ref:`beforeClose <no-27041>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-27042>`                   
:ref:`beforeDeleteAll <no-27043>`                
:ref:`beforeFilter <no-27044>`                   
:ref:`beforeFirst <no-27045>`                    
:ref:`beforeInit <no-27046>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-27047>`                     
:ref:`beforeNew <no-27048>`                      
:ref:`beforeNext <no-27049>`                     
:ref:`beforePointerMove <no-27050>`              
:ref:`beforePrior <no-27051>`                    
:ref:`beforeRequery <no-27052>`                  
:ref:`beforeSave <no-27053>`                     
:ref:`beforeSetProperties <no-27054>`            
:ref:`bindEvent <no-27055>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-27056>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-27057>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-27058>`                   Makes this object topmost
:ref:`cancel <no-27059>`                         Ask the bizobj to cancel its changes.
:ref:`clear <no-27060>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-27061>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-27062>`                          This method will close the form. If force = False (default)
:ref:`closing <no-27063>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-27064>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-27065>`           Given a position relative to this control, return a position relative
:ref:`copy <no-27066>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-27067>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-27068>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-27069>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-27070>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-27071>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-27072>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-27073>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-27074>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-27075>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-27076>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-27077>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-27078>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-27079>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-27080>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-27081>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-27082>`                       Draws text on the object at the specified position
:ref:`endHover <no-27083>`                       
:ref:`fillPreferenceDialog <no-27084>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-27085>`                         Apply a filter to the bizobj's data.
:ref:`first <no-27086>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-27087>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-27088>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-27089>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-27090>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-27091>`              
:ref:`formCoordinates <no-27092>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-27093>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-27094>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-27095>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-27096>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-27097>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-27098>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-27099>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-27100>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-27101>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-27102>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-27103>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-27104>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-27105>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-27106>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-27107>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-27108>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-27109>`                           Make the object invisible.
:ref:`initEvents <no-27110>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-27111>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-27112>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-27113>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-27114>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-27115>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-27116>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-27117>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-27118>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-27119>`                Move the record pointer to the specified row.
:ref:`new <no-27120>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-27121>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-27122>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-27123>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-27124>`                       
:ref:`onDelete <no-27125>`                       
:ref:`onEditRedo <no-27126>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-27127>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-27128>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-27129>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-27130>`                        
:ref:`onHover <no-27131>`                        
:ref:`onLast <no-27132>`                         
:ref:`onNew <no-27133>`                          
:ref:`onNext <no-27134>`                         
:ref:`onPrior <no-27135>`                        
:ref:`onRequery <no-27136>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onSave <no-27137>`                         
:ref:`paste <no-27138>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-27139>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-27140>`                    
:ref:`prior <no-27141>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-27142>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-27143>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-27144>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-27145>`                     Raise the passed Dabo event.
:ref:`reCreate <no-27146>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-27147>`                       Recreate the object.
:ref:`redraw <no-27148>`                         Called when the object is (re)drawn.
:ref:`refresh <no-27149>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-27150>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-27151>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-27152>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-27153>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-27154>`              
:ref:`removeFilter <no-27155>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-27156>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-27157>`       
:ref:`requery <no-27158>`                        Ask the bizobj to requery.
:ref:`restoreSizeAndPosition <no-27159>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-27160>` 
:ref:`safeDestroy <no-27161>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-27162>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-27163>`            Save the current size and position of this form.
:ref:`sendToBack <no-27164>`                     Places this object behind all others.
:ref:`setAll <no-27165>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-27166>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-27167>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-27168>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-27169>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-27170>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-27171>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-27172>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-27173>`                  Set the status text to val.
:ref:`show <no-27174>`                           Make the object visible.
:ref:`showContainingPage <no-27175>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-27176>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-27177>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-27178>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-27179>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-27180>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-27181>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-27182>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-27183>`                         Updates the contained controls with current values from the source.
:ref:`validateField <no-27184>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods
=======

.. _no-27017:

.. function:: dabo.ui.uiwx.dForm.BaseForm.addBizobj(self, bizobj)

   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   



-------

.. _no-27020:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterCancel(self)



-------

.. _no-27021:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterDelete(self)



-------

.. _no-27022:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterDeleteAll(self)



-------

.. _no-27023:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterFilter(self)



-------

.. _no-27024:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterFirst(self)



-------

.. _no-27027:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterLast(self)



-------

.. _no-27028:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterNew(self)



-------

.. _no-27029:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterNext(self)



-------

.. _no-27030:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterPointerMove(self)

   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   



-------

.. _no-27031:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterPrior(self)



-------

.. _no-27032:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterRequery(self)



-------

.. _no-27033:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterRowNavigation(self)

   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   



-------

.. _no-27034:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterSave(self)



-------

.. _no-27036:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterSetPrimaryBizobj(self)

   Subclass hook.



-------

.. _no-27040:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeCancel(self)



-------

.. _no-27042:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeDelete(self)



-------

.. _no-27043:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeDeleteAll(self)



-------

.. _no-27044:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeFilter(self)



-------

.. _no-27045:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeFirst(self)



-------

.. _no-27047:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeLast(self)



-------

.. _no-27048:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeNew(self)



-------

.. _no-27049:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeNext(self)



-------

.. _no-27050:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforePointerMove(self)



-------

.. _no-27051:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforePrior(self)



-------

.. _no-27052:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeRequery(self)



-------

.. _no-27053:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeSave(self)



-------

.. _no-27059:

.. function:: dabo.ui.uiwx.dForm.BaseForm.cancel(self, dataSource=None, ignoreNoRecords=None)

   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   



-------

.. _no-27064:

.. function:: dabo.ui.uiwx.dForm.BaseForm.confirmChanges(self, bizobjs=None)

   
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
   



-------

.. _no-27069:

.. function:: dabo.ui.uiwx.dForm.BaseForm.delete(self, dataSource=None, message=None, prompt=True)

   Ask the bizobj to delete the current record.



-------

.. _no-27070:

.. function:: dabo.ui.uiwx.dForm.BaseForm.deleteAll(self, dataSource=None, message=None)

   Ask the primary bizobj to delete all records from the recordset.



-------

.. _no-27085:

.. function:: dabo.ui.uiwx.dForm.BaseForm.filter(self, dataSource=None, fld=None, expr=None, op='=')

   Apply a filter to the bizobj's data.



-------

.. _no-27086:

.. function:: dabo.ui.uiwx.dForm.BaseForm.first(self, dataSource=None)

   Ask the bizobj to move to the first record.



-------

.. _no-27094:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getBizobj(self, dataSource=None, parentBizobj=None)

   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   



-------

.. _no-27095:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getBizobjsToCheck(self)

   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   



-------

.. _no-27097:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getConfirmChangesQueryMessage(self, changedBizList)

   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   



-------

.. _no-27099:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getCurrentRecordText(self, dataSource=None, grid=None)

   Get the text to describe which record is current.



-------

.. _no-27106:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getSQL(self, dataSource=None)

   Get the current SQL from the bizobj.



-------

.. _no-27114:

.. function:: dabo.ui.uiwx.dForm.BaseForm.last(self, dataSource=None)

   Ask the bizobj to move to the last record.



-------

.. _no-27119:

.. function:: dabo.ui.uiwx.dForm.BaseForm.moveToRowNumber(self, rowNumber, dataSource=None)

   Move the record pointer to the specified row.



-------

.. _no-27120:

.. function:: dabo.ui.uiwx.dForm.BaseForm.new(self, dataSource=None)

   Ask the bizobj to add a new record to the recordset.



-------

.. _no-27121:

.. function:: dabo.ui.uiwx.dForm.BaseForm.next(self, dataSource=None)

   Ask the bizobj to move to the next record.



-------

.. _no-27122:

.. function:: dabo.ui.uiwx.dForm.BaseForm.notifyUser(self, msg, title=None, severe=False, exception=None)

   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   



-------

.. _no-27124:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onCancel(self, evt)



-------

.. _no-27125:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onDelete(self, evt)



-------

.. _no-27128:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)

   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   



-------

.. _no-27129:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onFieldValidationPassed(self, ctrl, ds, df, val)

   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   



-------

.. _no-27130:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onFirst(self, evt)



-------

.. _no-27132:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onLast(self, evt)



-------

.. _no-27133:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onNew(self, evt)



-------

.. _no-27134:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onNext(self, evt)



-------

.. _no-27135:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onPrior(self, evt)



-------

.. _no-27136:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onRequery(self, evt)

   Occurs when an EVT_MENU event is received by this form.



-------

.. _no-27137:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onSave(self, evt)



-------

.. _no-27141:

.. function:: dabo.ui.uiwx.dForm.BaseForm.prior(self, dataSource=None)

   Ask the bizobj to move to the previous record.



-------

.. _no-27155:

.. function:: dabo.ui.uiwx.dForm.BaseForm.removeFilter(self, dataSource=None)

   Remove the most recently applied filter from the bizobj's data.



-------

.. _no-27156:

.. function:: dabo.ui.uiwx.dForm.BaseForm.removeFilters(self, dataSource=None)

   Remove all filters from the bizobj's data.



-------

.. _no-27158:

.. function:: dabo.ui.uiwx.dForm.BaseForm.requery(self, dataSource=None)

   Ask the bizobj to requery.



-------

.. _no-27162:

.. function:: dabo.ui.uiwx.dForm.BaseForm.save(self, dataSource=None)

   Ask the bizobj to commit its changes to the backend.



-------

.. _no-27170:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setSQL(self, sql, dataSource=None)

   Set the SQL for the bizobj.



-------

.. _no-27183:

.. function:: dabo.ui.uiwx.dForm.BaseForm.update(self, interval=None)

   
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
   



-------

.. _no-27184:

.. function:: dabo.ui.uiwx.dForm.BaseForm.validateField(self, ctrl)

   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   



-------


Methods - inherited
=====================

.. _no-27015:

.. function:: dabo.ui.uiwx.dForm.BaseForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27016:

.. function:: dabo.ui.uiwx.dForm.BaseForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27018:

.. function:: dabo.ui.uiwx.dForm.BaseForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-27019:

.. function:: dabo.ui.uiwx.dForm.BaseForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27025:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27026:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27035:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27037:

.. function:: dabo.ui.uiwx.dForm.BaseForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27038:

.. function:: dabo.ui.uiwx.dForm.BaseForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27039:

.. function:: dabo.ui.uiwx.dForm.BaseForm.autoBindEvents(self, force=True)
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

.. _no-27041:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27046:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27054:

.. function:: dabo.ui.uiwx.dForm.BaseForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27055:

.. function:: dabo.ui.uiwx.dForm.BaseForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27056:

.. function:: dabo.ui.uiwx.dForm.BaseForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27057:

.. function:: dabo.ui.uiwx.dForm.BaseForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-27058:

.. function:: dabo.ui.uiwx.dForm.BaseForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27060:

.. function:: dabo.ui.uiwx.dForm.BaseForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27061:

.. function:: dabo.ui.uiwx.dForm.BaseForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27062:

.. function:: dabo.ui.uiwx.dForm.BaseForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27063:

.. function:: dabo.ui.uiwx.dForm.BaseForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27065:

.. function:: dabo.ui.uiwx.dForm.BaseForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27066:

.. function:: dabo.ui.uiwx.dForm.BaseForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27067:

.. function:: dabo.ui.uiwx.dForm.BaseForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27068:

.. function:: dabo.ui.uiwx.dForm.BaseForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27071:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27072:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27073:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-27074:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27075:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27076:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27077:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27078:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27079:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27080:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27081:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27082:

.. function:: dabo.ui.uiwx.dForm.BaseForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27083:

.. function:: dabo.ui.uiwx.dForm.BaseForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27084:

.. function:: dabo.ui.uiwx.dForm.BaseForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27087:

.. function:: dabo.ui.uiwx.dForm.BaseForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27088:

.. function:: dabo.ui.uiwx.dForm.BaseForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27089:

.. function:: dabo.ui.uiwx.dForm.BaseForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27090:

.. function:: dabo.ui.uiwx.dForm.BaseForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27091:

.. function:: dabo.ui.uiwx.dForm.BaseForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27092:

.. function:: dabo.ui.uiwx.dForm.BaseForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27093:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27096:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27098:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27100:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27101:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27102:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27103:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27104:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27105:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-27107:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27108:

.. function:: dabo.ui.uiwx.dForm.BaseForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27109:

.. function:: dabo.ui.uiwx.dForm.BaseForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27110:

.. function:: dabo.ui.uiwx.dForm.BaseForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27111:

.. function:: dabo.ui.uiwx.dForm.BaseForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27112:

.. function:: dabo.ui.uiwx.dForm.BaseForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27113:

.. function:: dabo.ui.uiwx.dForm.BaseForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27115:

.. function:: dabo.ui.uiwx.dForm.BaseForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27116:

.. function:: dabo.ui.uiwx.dForm.BaseForm.lockDisplay(self)
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

.. _no-27117:

.. function:: dabo.ui.uiwx.dForm.BaseForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27118:

.. function:: dabo.ui.uiwx.dForm.BaseForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27123:

.. function:: dabo.ui.uiwx.dForm.BaseForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27126:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27127:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27131:

.. function:: dabo.ui.uiwx.dForm.BaseForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27138:

.. function:: dabo.ui.uiwx.dForm.BaseForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27139:

.. function:: dabo.ui.uiwx.dForm.BaseForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27140:

.. function:: dabo.ui.uiwx.dForm.BaseForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27142:

.. function:: dabo.ui.uiwx.dForm.BaseForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27143:

.. function:: dabo.ui.uiwx.dForm.BaseForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27144:

.. function:: dabo.ui.uiwx.dForm.BaseForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27145:

.. function:: dabo.ui.uiwx.dForm.BaseForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27146:

.. function:: dabo.ui.uiwx.dForm.BaseForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27147:

.. function:: dabo.ui.uiwx.dForm.BaseForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27148:

.. function:: dabo.ui.uiwx.dForm.BaseForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27149:

.. function:: dabo.ui.uiwx.dForm.BaseForm.refresh(self, interval=None)
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

.. _no-27150:

.. function:: dabo.ui.uiwx.dForm.BaseForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27151:

.. function:: dabo.ui.uiwx.dForm.BaseForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27152:

.. function:: dabo.ui.uiwx.dForm.BaseForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27153:

.. function:: dabo.ui.uiwx.dForm.BaseForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27154:

.. function:: dabo.ui.uiwx.dForm.BaseForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27157:

.. function:: dabo.ui.uiwx.dForm.BaseForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27159:

.. function:: dabo.ui.uiwx.dForm.BaseForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27160:

.. function:: dabo.ui.uiwx.dForm.BaseForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27161:

.. function:: dabo.ui.uiwx.dForm.BaseForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27163:

.. function:: dabo.ui.uiwx.dForm.BaseForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27164:

.. function:: dabo.ui.uiwx.dForm.BaseForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27165:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-27166:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27167:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27168:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-27169:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-27171:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27172:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27173:

.. function:: dabo.ui.uiwx.dForm.BaseForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27174:

.. function:: dabo.ui.uiwx.dForm.BaseForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27175:

.. function:: dabo.ui.uiwx.dForm.BaseForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27176:

.. function:: dabo.ui.uiwx.dForm.BaseForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27177:

.. function:: dabo.ui.uiwx.dForm.BaseForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27178:

.. function:: dabo.ui.uiwx.dForm.BaseForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27179:

.. function:: dabo.ui.uiwx.dForm.BaseForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27180:

.. function:: dabo.ui.uiwx.dForm.BaseForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27181:

.. function:: dabo.ui.uiwx.dForm.BaseForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27182:

.. function:: dabo.ui.uiwx.dForm.BaseForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
