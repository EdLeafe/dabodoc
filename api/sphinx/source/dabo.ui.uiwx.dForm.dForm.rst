
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dForm

.. _dabo.ui.uiwx.dForm.dForm:

====================================
|doc_title|  **dForm.dForm** - class
====================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dForm**

.. inheritance-diagram:: dForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dForm.BaseForm`



|subclasses| Known Subclasses
=============================

* :ref:`dForm_6062`
* :ref:`dabo.lib.datanav.Form.Form`
* dabo.ui.uiwx.dBorderSizer.TestForm - can not provide a link
* :ref:`dabo.ui.uiwx.dDockForm.dDockForm`
* dabo.ui.uiwx.dPageFrameNoTabs.TestForm - can not provide a link
* :ref:`dabo.ui.uiwx.dRichTextBox.RichTextTestForm`
* :ref:`dabo.ui.uiwx.dSplitForm.dSplitForm`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dForm.png
          :scale: 75 %
          :target: _static/macWidgets/dForm.png
          :alt: dForm



     - .. image:: _static/winWidgets/dForm.png
          :scale: 75 %
          :target: _static/winWidgets/dForm.png
          :alt: dForm



     - .. image:: _static/nixWidgets/dForm.png
          :scale: 75 %
          :target: _static/nixWidgets/dForm.png
          :alt: dForm


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dForm.dForm

   .. automethod:: dabo.ui.uiwx.dForm.dForm.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-27527>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-27528>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-27529>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-27530>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-27531>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-27532>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-27533>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-27534>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-27535>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-27536>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-27537>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-27538>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-27539>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-27540>`                     The caption of the object. (str)
:ref:`Centered <no-27541>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-27542>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-27543>`                    Returns a list of object references to the children of
:ref:`Class <no-27544>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-27545>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-27546>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-27547>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-27548>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-27549>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-27550>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-27551>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-27552>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-27553>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-27554>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-27555>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-27556>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-27557>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-27558>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-27559>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-27560>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-27561>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-27562>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-27563>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-27564>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-27565>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-27566>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-27567>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-27568>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-27569>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-27570>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-27571>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-27572>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-27573>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-27574>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-27575>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-27576>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-27577>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-27578>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-27579>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-27580>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-27581>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-27582>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-27583>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-27584>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-27585>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-27586>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-27587>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-27588>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-27589>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-27590>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-27591>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-27592>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-27593>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-27594>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-27595>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-27596>`                    Specifies the font face. (str)
:ref:`FontInfo <no-27597>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-27598>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-27599>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-27600>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-27601>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-27602>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-27603>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-27604>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-27605>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-27606>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-27607>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-27608>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-27609>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-27610>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-27611>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-27612>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-27613>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-27614>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-27615>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-27616>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-27617>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-27618>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-27619>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-27620>`                       Specifies whether this dForm is modal or not  (bool)
:ref:`MousePointer <no-27621>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-27622>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-27623>`                    Specifies the base name of the object.
:ref:`Parent <no-27624>`                      The containing object. (obj)
:ref:`Position <no-27625>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-27626>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-27627>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-27628>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-27629>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-27630>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-27631>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SaveAllRows <no-27632>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-27633>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-27634>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-27635>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-27636>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-27637>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-27638>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-27639>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-27640>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-27641>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-27642>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-27643>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-27644>`                        The size of the object. (tuple)
:ref:`Sizer <no-27645>`                       The sizer for the object.
:ref:`SizersToOutline <no-27646>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-27647>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-27648>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-27649>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-27650>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-27651>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-27652>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-27653>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-27654>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-27655>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-27656>`                         The top position of the object. (int)
:ref:`Transparency <no-27657>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-27658>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-27659>`                     Specifies whether the form is shown or hidden.  (bool)
:ref:`VisibleOnScreen <no-27660>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-27661>`                       The width of the object. (int)
:ref:`WindowHandle <no-27662>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-27663>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties
==========

.. _no-27620:

**Modal** 

Specifies whether this dForm is modal or not  (bool)

    A modal dForm runs its own event loop, blocking program flow until the
    form is hidden or closed, exactly like a dDialog does it. This property
    may only be sent to the constructor, and once instantiated you may not
    change the modality of a form. For example::

            frm = dabo.ui.dForm(Modal=True)

    will create a modal form.

    .. note::

        That a modal dForm is actually a dDialog, and as such does not
        have the ability to contain MenuBars, StatusBars, or ToolBars.

    



-------


Properties - inherited
========================

.. _no-27527:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27528:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27529:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27530:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27531:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27532:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27533:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27534:

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

.. _no-27535:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27536:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27537:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27538:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27539:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27540:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27541:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27542:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27543:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27544:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27545:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27546:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27547:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27548:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27549:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27550:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27551:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27552:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27553:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27554:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27555:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27556:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27557:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27558:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27559:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27560:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27561:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27562:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27563:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27564:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27565:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27566:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27567:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27568:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27569:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27570:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27571:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27572:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27573:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27574:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27575:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27576:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27577:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27578:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27579:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27580:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27581:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27582:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27583:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27584:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27585:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27586:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27587:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27588:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27589:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27590:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27591:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27592:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27593:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27594:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27595:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27596:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27597:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27598:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27599:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27600:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27601:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27602:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27603:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27604:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27605:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27606:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-27607:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27608:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27609:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27610:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27611:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27612:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27613:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27614:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27615:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27616:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27617:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27618:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27619:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27621:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27622:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27623:

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

.. _no-27624:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27625:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27626:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27627:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27628:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27629:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27630:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27631:

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

.. _no-27632:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27633:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27634:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27635:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27636:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27637:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27638:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27639:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27640:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27641:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27642:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27643:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27644:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27645:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-27646:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27647:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27648:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27649:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27650:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27651:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27652:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27653:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27654:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-27655:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27656:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27657:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27658:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27659:

**Visible** 

Specifies whether the form is shown or hidden.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27660:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27661:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27662:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27663:

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
:ref:`Activate <no-27664>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-27665>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-27666>`              Occurs when a child control is created.
:ref:`Close <no-27667>`                  Occurs when the user closes the form.
:ref:`ControlNavigationEvent <no-27668>` 
:ref:`Create <no-27669>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-27670>`             Occurs when another form becomes active.
:ref:`Destroy <no-27671>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-27672>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-27673>`               Occurs when the control gets the focus.
:ref:`Idle <no-27674>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-27675>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-27676>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-27677>`               
:ref:`KeyUp <no-27678>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-27679>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-27680>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-27681>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-27682>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-27683>`             
:ref:`MouseLeave <no-27684>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-27685>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-27686>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-27687>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-27688>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-27689>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-27690>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-27691>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-27692>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-27693>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-27694>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-27695>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-27696>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-27697>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-27698>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-27699>`                   Occurs when the control's position changes.
:ref:`Paint <no-27700>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-27701>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-27702>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-27703>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-27704>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-27664:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-27665:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-27666:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-27667:

**Close** 

Occurs when the user closes the form.



-------

.. _no-27668:

**ControlNavigationEvent** 



-------

.. _no-27669:

**Create** 

Occurs after the control or form is created.



-------

.. _no-27670:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-27671:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-27672:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-27673:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-27674:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-27675:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-27676:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-27677:

**KeyEvent** 



-------

.. _no-27678:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-27679:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-27680:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-27681:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-27682:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-27683:

**MouseEvent** 



-------

.. _no-27684:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-27685:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-27686:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-27687:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-27688:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-27689:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-27690:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-27691:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-27692:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-27693:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-27694:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-27695:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-27696:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-27697:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-27698:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-27699:

**Move** 

Occurs when the control's position changes.



-------

.. _no-27700:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-27701:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-27702:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-27703:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-27704:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-27705>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-27706>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-27707>`                      Add a bizobj to this form.
:ref:`addObject <no-27708>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-27709>`            
:ref:`afterCancel <no-27710>`                    
:ref:`afterDelete <no-27711>`                    
:ref:`afterDeleteAll <no-27712>`                 
:ref:`afterFilter <no-27713>`                    
:ref:`afterFirst <no-27714>`                     
:ref:`afterInit <no-27715>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-27716>`                   
:ref:`afterLast <no-27717>`                      
:ref:`afterNew <no-27718>`                       
:ref:`afterNext <no-27719>`                      
:ref:`afterPointerMove <no-27720>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-27721>`                     
:ref:`afterRequery <no-27722>`                   
:ref:`afterRowNavigation <no-27723>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-27724>`                      
:ref:`afterSetMenuBar <no-27725>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-27726>`          Subclass hook.
:ref:`afterSetProperties <no-27727>`             
:ref:`appendToolBarButton <no-27728>`            
:ref:`autoBindEvents <no-27729>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-27730>`                   
:ref:`beforeClose <no-27731>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-27732>`                   
:ref:`beforeDeleteAll <no-27733>`                
:ref:`beforeFilter <no-27734>`                   
:ref:`beforeFirst <no-27735>`                    
:ref:`beforeInit <no-27736>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-27737>`                     
:ref:`beforeNew <no-27738>`                      
:ref:`beforeNext <no-27739>`                     
:ref:`beforePointerMove <no-27740>`              
:ref:`beforePrior <no-27741>`                    
:ref:`beforeRequery <no-27742>`                  
:ref:`beforeSave <no-27743>`                     
:ref:`beforeSetProperties <no-27744>`            
:ref:`bindEvent <no-27745>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-27746>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-27747>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-27748>`                   Makes this object topmost
:ref:`cancel <no-27749>`                         Ask the bizobj to cancel its changes.
:ref:`clear <no-27750>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-27751>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-27752>`                          This method will close the form. If force = False (default)
:ref:`closing <no-27753>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-27754>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-27755>`           Given a position relative to this control, return a position relative
:ref:`copy <no-27756>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-27757>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-27758>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-27759>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-27760>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-27761>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-27762>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-27763>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-27764>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-27765>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-27766>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-27767>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-27768>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-27769>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-27770>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-27771>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-27772>`                       Draws text on the object at the specified position
:ref:`endHover <no-27773>`                       
:ref:`fillPreferenceDialog <no-27774>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-27775>`                         Apply a filter to the bizobj's data.
:ref:`first <no-27776>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-27777>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-27778>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-27779>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-27780>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-27781>`              
:ref:`formCoordinates <no-27782>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-27783>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-27784>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-27785>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-27786>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-27787>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-27788>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-27789>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-27790>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-27791>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-27792>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-27793>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-27794>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-27795>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-27796>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-27797>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-27798>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-27799>`                           Make the object invisible.
:ref:`initEvents <no-27800>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-27801>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-27802>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-27803>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-27804>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-27805>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-27806>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-27807>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-27808>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-27809>`                Move the record pointer to the specified row.
:ref:`new <no-27810>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-27811>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-27812>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-27813>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-27814>`                       
:ref:`onDelete <no-27815>`                       
:ref:`onEditRedo <no-27816>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-27817>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-27818>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-27819>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-27820>`                        
:ref:`onHover <no-27821>`                        
:ref:`onLast <no-27822>`                         
:ref:`onNew <no-27823>`                          
:ref:`onNext <no-27824>`                         
:ref:`onPrior <no-27825>`                        
:ref:`onRequery <no-27826>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onSave <no-27827>`                         
:ref:`paste <no-27828>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-27829>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-27830>`                    
:ref:`prior <no-27831>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-27832>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-27833>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-27834>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-27835>`                     Raise the passed Dabo event.
:ref:`reCreate <no-27836>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-27837>`                       Recreate the object.
:ref:`redraw <no-27838>`                         Called when the object is (re)drawn.
:ref:`refresh <no-27839>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-27840>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-27841>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-27842>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-27843>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-27844>`              
:ref:`removeFilter <no-27845>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-27846>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-27847>`       
:ref:`requery <no-27848>`                        Ask the bizobj to requery.
:ref:`restoreSizeAndPosition <no-27849>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-27850>` 
:ref:`safeDestroy <no-27851>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-27852>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-27853>`            Save the current size and position of this form.
:ref:`sendToBack <no-27854>`                     Places this object behind all others.
:ref:`setAll <no-27855>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-27856>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-27857>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-27858>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-27859>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-27860>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-27861>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-27862>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-27863>`                  Set the status text to val.
:ref:`show <no-27864>`                           Make the object visible.
:ref:`showContainingPage <no-27865>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-27866>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-27867>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-27868>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-27869>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-27870>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-27871>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-27872>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-27873>`                         Updates the contained controls with current values from the source.
:ref:`validateField <no-27874>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods - inherited
=====================

.. _no-27705:

.. function:: dabo.ui.uiwx.dForm.dForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27706:

.. function:: dabo.ui.uiwx.dForm.dForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27707:

.. function:: dabo.ui.uiwx.dForm.dForm.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27708:

.. function:: dabo.ui.uiwx.dForm.dForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-27709:

.. function:: dabo.ui.uiwx.dForm.dForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27710:

.. function:: dabo.ui.uiwx.dForm.dForm.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27711:

.. function:: dabo.ui.uiwx.dForm.dForm.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27712:

.. function:: dabo.ui.uiwx.dForm.dForm.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27713:

.. function:: dabo.ui.uiwx.dForm.dForm.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27714:

.. function:: dabo.ui.uiwx.dForm.dForm.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27715:

.. function:: dabo.ui.uiwx.dForm.dForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27716:

.. function:: dabo.ui.uiwx.dForm.dForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27717:

.. function:: dabo.ui.uiwx.dForm.dForm.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27718:

.. function:: dabo.ui.uiwx.dForm.dForm.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27719:

.. function:: dabo.ui.uiwx.dForm.dForm.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27720:

.. function:: dabo.ui.uiwx.dForm.dForm.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27721:

.. function:: dabo.ui.uiwx.dForm.dForm.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27722:

.. function:: dabo.ui.uiwx.dForm.dForm.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27723:

.. function:: dabo.ui.uiwx.dForm.dForm.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27724:

.. function:: dabo.ui.uiwx.dForm.dForm.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27725:

.. function:: dabo.ui.uiwx.dForm.dForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27726:

.. function:: dabo.ui.uiwx.dForm.dForm.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27727:

.. function:: dabo.ui.uiwx.dForm.dForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27728:

.. function:: dabo.ui.uiwx.dForm.dForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27729:

.. function:: dabo.ui.uiwx.dForm.dForm.autoBindEvents(self, force=True)
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

.. _no-27730:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27731:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27732:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27733:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27734:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27735:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27736:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27737:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27738:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27739:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27740:

.. function:: dabo.ui.uiwx.dForm.dForm.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27741:

.. function:: dabo.ui.uiwx.dForm.dForm.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27742:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27743:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27744:

.. function:: dabo.ui.uiwx.dForm.dForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27745:

.. function:: dabo.ui.uiwx.dForm.dForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27746:

.. function:: dabo.ui.uiwx.dForm.dForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27747:

.. function:: dabo.ui.uiwx.dForm.dForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-27748:

.. function:: dabo.ui.uiwx.dForm.dForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27749:

.. function:: dabo.ui.uiwx.dForm.dForm.cancel(self, dataSource=None, ignoreNoRecords=None)
   :noindex:


   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27750:

.. function:: dabo.ui.uiwx.dForm.dForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27751:

.. function:: dabo.ui.uiwx.dForm.dForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27752:

.. function:: dabo.ui.uiwx.dForm.dForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27753:

.. function:: dabo.ui.uiwx.dForm.dForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27754:

.. function:: dabo.ui.uiwx.dForm.dForm.confirmChanges(self, bizobjs=None)
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

.. _no-27755:

.. function:: dabo.ui.uiwx.dForm.dForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27756:

.. function:: dabo.ui.uiwx.dForm.dForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27757:

.. function:: dabo.ui.uiwx.dForm.dForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27758:

.. function:: dabo.ui.uiwx.dForm.dForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27759:

.. function:: dabo.ui.uiwx.dForm.dForm.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27760:

.. function:: dabo.ui.uiwx.dForm.dForm.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27761:

.. function:: dabo.ui.uiwx.dForm.dForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27762:

.. function:: dabo.ui.uiwx.dForm.dForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27763:

.. function:: dabo.ui.uiwx.dForm.dForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-27764:

.. function:: dabo.ui.uiwx.dForm.dForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27765:

.. function:: dabo.ui.uiwx.dForm.dForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27766:

.. function:: dabo.ui.uiwx.dForm.dForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27767:

.. function:: dabo.ui.uiwx.dForm.dForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27768:

.. function:: dabo.ui.uiwx.dForm.dForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27769:

.. function:: dabo.ui.uiwx.dForm.dForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27770:

.. function:: dabo.ui.uiwx.dForm.dForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27771:

.. function:: dabo.ui.uiwx.dForm.dForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27772:

.. function:: dabo.ui.uiwx.dForm.dForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27773:

.. function:: dabo.ui.uiwx.dForm.dForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27774:

.. function:: dabo.ui.uiwx.dForm.dForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27775:

.. function:: dabo.ui.uiwx.dForm.dForm.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27776:

.. function:: dabo.ui.uiwx.dForm.dForm.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27777:

.. function:: dabo.ui.uiwx.dForm.dForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27778:

.. function:: dabo.ui.uiwx.dForm.dForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27779:

.. function:: dabo.ui.uiwx.dForm.dForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27780:

.. function:: dabo.ui.uiwx.dForm.dForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27781:

.. function:: dabo.ui.uiwx.dForm.dForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27782:

.. function:: dabo.ui.uiwx.dForm.dForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27783:

.. function:: dabo.ui.uiwx.dForm.dForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27784:

.. function:: dabo.ui.uiwx.dForm.dForm.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27785:

.. function:: dabo.ui.uiwx.dForm.dForm.getBizobjsToCheck(self)
   :noindex:


   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27786:

.. function:: dabo.ui.uiwx.dForm.dForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27787:

.. function:: dabo.ui.uiwx.dForm.dForm.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27788:

.. function:: dabo.ui.uiwx.dForm.dForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27789:

.. function:: dabo.ui.uiwx.dForm.dForm.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27790:

.. function:: dabo.ui.uiwx.dForm.dForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27791:

.. function:: dabo.ui.uiwx.dForm.dForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27792:

.. function:: dabo.ui.uiwx.dForm.dForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27793:

.. function:: dabo.ui.uiwx.dForm.dForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27794:

.. function:: dabo.ui.uiwx.dForm.dForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27795:

.. function:: dabo.ui.uiwx.dForm.dForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-27796:

.. function:: dabo.ui.uiwx.dForm.dForm.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27797:

.. function:: dabo.ui.uiwx.dForm.dForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27798:

.. function:: dabo.ui.uiwx.dForm.dForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27799:

.. function:: dabo.ui.uiwx.dForm.dForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27800:

.. function:: dabo.ui.uiwx.dForm.dForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27801:

.. function:: dabo.ui.uiwx.dForm.dForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27802:

.. function:: dabo.ui.uiwx.dForm.dForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27803:

.. function:: dabo.ui.uiwx.dForm.dForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27804:

.. function:: dabo.ui.uiwx.dForm.dForm.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27805:

.. function:: dabo.ui.uiwx.dForm.dForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27806:

.. function:: dabo.ui.uiwx.dForm.dForm.lockDisplay(self)
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

.. _no-27807:

.. function:: dabo.ui.uiwx.dForm.dForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27808:

.. function:: dabo.ui.uiwx.dForm.dForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27809:

.. function:: dabo.ui.uiwx.dForm.dForm.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27810:

.. function:: dabo.ui.uiwx.dForm.dForm.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27811:

.. function:: dabo.ui.uiwx.dForm.dForm.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27812:

.. function:: dabo.ui.uiwx.dForm.dForm.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27813:

.. function:: dabo.ui.uiwx.dForm.dForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27814:

.. function:: dabo.ui.uiwx.dForm.dForm.onCancel(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27815:

.. function:: dabo.ui.uiwx.dForm.dForm.onDelete(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27816:

.. function:: dabo.ui.uiwx.dForm.dForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27817:

.. function:: dabo.ui.uiwx.dForm.dForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27818:

.. function:: dabo.ui.uiwx.dForm.dForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27819:

.. function:: dabo.ui.uiwx.dForm.dForm.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27820:

.. function:: dabo.ui.uiwx.dForm.dForm.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27821:

.. function:: dabo.ui.uiwx.dForm.dForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27822:

.. function:: dabo.ui.uiwx.dForm.dForm.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27823:

.. function:: dabo.ui.uiwx.dForm.dForm.onNew(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27824:

.. function:: dabo.ui.uiwx.dForm.dForm.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27825:

.. function:: dabo.ui.uiwx.dForm.dForm.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27826:

.. function:: dabo.ui.uiwx.dForm.dForm.onRequery(self, evt)
   :noindex:


   Occurs when an EVT_MENU event is received by this form.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27827:

.. function:: dabo.ui.uiwx.dForm.dForm.onSave(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27828:

.. function:: dabo.ui.uiwx.dForm.dForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27829:

.. function:: dabo.ui.uiwx.dForm.dForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27830:

.. function:: dabo.ui.uiwx.dForm.dForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27831:

.. function:: dabo.ui.uiwx.dForm.dForm.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27832:

.. function:: dabo.ui.uiwx.dForm.dForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27833:

.. function:: dabo.ui.uiwx.dForm.dForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27834:

.. function:: dabo.ui.uiwx.dForm.dForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27835:

.. function:: dabo.ui.uiwx.dForm.dForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27836:

.. function:: dabo.ui.uiwx.dForm.dForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-27837:

.. function:: dabo.ui.uiwx.dForm.dForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27838:

.. function:: dabo.ui.uiwx.dForm.dForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27839:

.. function:: dabo.ui.uiwx.dForm.dForm.refresh(self, interval=None)
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

.. _no-27840:

.. function:: dabo.ui.uiwx.dForm.dForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27841:

.. function:: dabo.ui.uiwx.dForm.dForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27842:

.. function:: dabo.ui.uiwx.dForm.dForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27843:

.. function:: dabo.ui.uiwx.dForm.dForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27844:

.. function:: dabo.ui.uiwx.dForm.dForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27845:

.. function:: dabo.ui.uiwx.dForm.dForm.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27846:

.. function:: dabo.ui.uiwx.dForm.dForm.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27847:

.. function:: dabo.ui.uiwx.dForm.dForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27848:

.. function:: dabo.ui.uiwx.dForm.dForm.requery(self, dataSource=None)
   :noindex:


   Ask the bizobj to requery.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27849:

.. function:: dabo.ui.uiwx.dForm.dForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27850:

.. function:: dabo.ui.uiwx.dForm.dForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27851:

.. function:: dabo.ui.uiwx.dForm.dForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27852:

.. function:: dabo.ui.uiwx.dForm.dForm.save(self, dataSource=None)
   :noindex:


   Ask the bizobj to commit its changes to the backend.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27853:

.. function:: dabo.ui.uiwx.dForm.dForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27854:

.. function:: dabo.ui.uiwx.dForm.dForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27855:

.. function:: dabo.ui.uiwx.dForm.dForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-27856:

.. function:: dabo.ui.uiwx.dForm.dForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27857:

.. function:: dabo.ui.uiwx.dForm.dForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27858:

.. function:: dabo.ui.uiwx.dForm.dForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-27859:

.. function:: dabo.ui.uiwx.dForm.dForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-27860:

.. function:: dabo.ui.uiwx.dForm.dForm.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-27861:

.. function:: dabo.ui.uiwx.dForm.dForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27862:

.. function:: dabo.ui.uiwx.dForm.dForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27863:

.. function:: dabo.ui.uiwx.dForm.dForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27864:

.. function:: dabo.ui.uiwx.dForm.dForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27865:

.. function:: dabo.ui.uiwx.dForm.dForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27866:

.. function:: dabo.ui.uiwx.dForm.dForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27867:

.. function:: dabo.ui.uiwx.dForm.dForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-27868:

.. function:: dabo.ui.uiwx.dForm.dForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-27869:

.. function:: dabo.ui.uiwx.dForm.dForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-27870:

.. function:: dabo.ui.uiwx.dForm.dForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27871:

.. function:: dabo.ui.uiwx.dForm.dForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27872:

.. function:: dabo.ui.uiwx.dForm.dForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-27873:

.. function:: dabo.ui.uiwx.dForm.dForm.update(self, interval=None)
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

.. _no-27874:

.. function:: dabo.ui.uiwx.dForm.dForm.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
