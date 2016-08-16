
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDockForm

.. _dabo.ui.uiwx.dDockForm.dDockForm:

============================================
|doc_title|  **dDockForm.dDockForm** - class
============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDockForm**

.. inheritance-diagram:: dDockForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dForm.dForm`



|subclasses| Known Subclasses
=============================




|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dDockForm.png
          :scale: 75 %
          :target: _static/winWidgets/dDockForm.png
          :alt: dDockForm



     - .. image:: _static/nixWidgets/dDockForm.png
          :scale: 75 %
          :target: _static/nixWidgets/dDockForm.png
          :alt: dDockForm


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDockForm.dDockForm


|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-16066>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-16067>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-16068>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-16069>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-16070>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-16071>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-16072>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-16073>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-16074>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-16075>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-16076>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-16077>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-16078>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-16079>`                     The caption of the object. (str)
:ref:`CenterPanel <no-16080>`                 Reference to the center (i.e., non-docking) panel. (read-only) (dPanel)
:ref:`Centered <no-16081>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-16082>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-16083>`                    Returns a list of object references to the children of
:ref:`Class <no-16084>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-16085>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-16086>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-16087>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-16088>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-16089>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-16090>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-16091>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-16092>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-16093>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-16094>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-16095>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-16096>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-16097>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-16098>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-16099>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-16100>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-16101>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-16102>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-16103>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-16104>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-16105>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-16106>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-16107>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-16108>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-16109>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-16110>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-16111>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-16112>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-16113>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-16114>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-16115>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-16116>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-16117>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-16118>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-16119>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-16120>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-16121>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-16122>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-16123>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-16124>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-16125>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-16126>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-16127>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-16128>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-16129>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-16130>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-16131>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-16132>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-16133>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-16134>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-16135>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-16136>`                    Specifies the font face. (str)
:ref:`FontInfo <no-16137>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-16138>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-16139>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-16140>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-16141>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-16142>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-16143>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-16144>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-16145>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-16146>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-16147>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-16148>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-16149>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-16150>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-16151>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-16152>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-16153>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-16154>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-16155>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-16156>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-16157>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-16158>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-16159>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-16160>`                       Specifies whether this dForm is modal or not  (bool)
:ref:`MousePointer <no-16161>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-16162>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-16163>`                    Specifies the base name of the object.
:ref:`Parent <no-16164>`                      The containing object. (obj)
:ref:`Position <no-16165>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-16166>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-16167>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-16168>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-16169>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-16170>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-16171>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SaveAllRows <no-16172>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-16173>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-16174>`         Specifies whether the form's position and size as set by the user
:ref:`ShowActivePanel <no-16175>`             When True, the title bar of the active pane is highlighted. Default=False  (bool)
:ref:`ShowCaption <no-16176>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-16177>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-16178>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-16179>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-16180>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-16181>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-16182>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-16183>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-16184>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-16185>`                        The size of the object. (tuple)
:ref:`Sizer <no-16186>`                       The sizer for the object.
:ref:`SizersToOutline <no-16187>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-16188>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-16189>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-16190>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-16191>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-16192>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-16193>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-16194>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-16195>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-16196>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-16197>`                         The top position of the object. (int)
:ref:`Transparency <no-16198>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-16199>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`TransparentDrag <no-16200>`             When dragging panes, do they appear transparent? Default=True  (bool)
:ref:`Visible <no-16201>`                     Specifies whether the form is shown or hidden.  (bool)
:ref:`VisibleOnScreen <no-16202>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-16203>`                       The width of the object. (int)
:ref:`WindowHandle <no-16204>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-16205>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties
==========

.. _no-16080:

**CenterPanel** 

Reference to the center (i.e., non-docking) panel. (read-only) (dPanel)



-------

.. _no-16175:

**ShowActivePanel** 

When True, the title bar of the active pane is highlighted. Default=False  (bool)



-------

.. _no-16200:

**TransparentDrag** 

When dragging panes, do they appear transparent? Default=True  (bool)



-------


Properties - inherited
========================

.. _no-16066:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16067:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16068:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16069:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16070:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16071:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16072:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16073:

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

.. _no-16074:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16075:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16076:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16077:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16078:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16079:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16081:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16082:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16083:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16084:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16085:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16086:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16087:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16088:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16089:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16090:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16091:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16092:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16093:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16094:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16095:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16096:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16097:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16098:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16099:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16100:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16101:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16102:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16103:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16104:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16105:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16106:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16107:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16108:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16109:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16110:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16111:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16112:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16113:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16114:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16115:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16116:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16117:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16118:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16119:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16120:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16121:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16122:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16123:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16124:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16125:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16126:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16127:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16128:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16129:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16130:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16131:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16132:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16133:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16134:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16135:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16136:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16137:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16138:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16139:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16140:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16141:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16142:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16143:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16144:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16145:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16146:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-16147:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16148:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16149:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16150:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16151:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16152:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16153:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16154:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-16155:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16156:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16157:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16158:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16159:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16160:

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

    


Inherited from: :ref:`dabo.ui.uiwx.dForm.dForm`

-------

.. _no-16161:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16162:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16163:

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

.. _no-16164:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16165:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16166:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16167:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16168:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16169:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16170:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16171:

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

.. _no-16172:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16173:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16174:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16176:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16177:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16178:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16179:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16180:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16181:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16182:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16183:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16184:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16185:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16186:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16187:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16188:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-16189:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16190:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16191:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16192:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16193:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16194:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16195:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-16196:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16197:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16198:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16199:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16201:

**Visible** 

Specifies whether the form is shown or hidden.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16202:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16203:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16204:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16205:

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
:ref:`Activate <no-16206>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-16207>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-16208>`              Occurs when a child control is created.
:ref:`Close <no-16209>`                  Occurs when the user closes the form.
:ref:`ControlNavigationEvent <no-16210>` 
:ref:`Create <no-16211>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-16212>`             Occurs when another form becomes active.
:ref:`Destroy <no-16213>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-16214>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-16215>`               Occurs when the control gets the focus.
:ref:`Idle <no-16216>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-16217>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-16218>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-16219>`               
:ref:`KeyUp <no-16220>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-16221>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-16222>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-16223>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-16224>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-16225>`             
:ref:`MouseLeave <no-16226>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-16227>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-16228>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-16229>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-16230>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-16231>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-16232>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-16233>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-16234>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-16235>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-16236>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-16237>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-16238>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-16239>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-16240>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-16241>`                   Occurs when the control's position changes.
:ref:`Paint <no-16242>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-16243>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-16244>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-16245>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-16246>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-16206:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-16207:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-16208:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-16209:

**Close** 

Occurs when the user closes the form.



-------

.. _no-16210:

**ControlNavigationEvent** 



-------

.. _no-16211:

**Create** 

Occurs after the control or form is created.



-------

.. _no-16212:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-16213:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-16214:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-16215:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-16216:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-16217:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-16218:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-16219:

**KeyEvent** 



-------

.. _no-16220:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-16221:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-16222:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-16223:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-16224:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-16225:

**MouseEvent** 



-------

.. _no-16226:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-16227:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-16228:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-16229:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-16230:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-16231:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-16232:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-16233:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-16234:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-16235:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-16236:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-16237:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-16238:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-16239:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-16240:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-16241:

**Move** 

Occurs when the control's position changes.



-------

.. _no-16242:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-16243:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-16244:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-16245:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-16246:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-16247>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-16248>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-16249>`                      Add a bizobj to this form.
:ref:`addObject <no-16250>`                      To support the old addObject() syntax, we need to re-direct the request
:ref:`addPanel <no-16251>`                       Adds a dockable panel to the form.
:ref:`addToOutlinedSizers <no-16252>`            
:ref:`afterCancel <no-16253>`                    
:ref:`afterDelete <no-16254>`                    
:ref:`afterDeleteAll <no-16255>`                 
:ref:`afterFilter <no-16256>`                    
:ref:`afterFirst <no-16257>`                     
:ref:`afterInit <no-16258>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-16259>`                   
:ref:`afterLast <no-16260>`                      
:ref:`afterNew <no-16261>`                       
:ref:`afterNext <no-16262>`                      
:ref:`afterPointerMove <no-16263>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-16264>`                     
:ref:`afterRequery <no-16265>`                   
:ref:`afterRowNavigation <no-16266>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-16267>`                      
:ref:`afterSetMenuBar <no-16268>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-16269>`          Subclass hook.
:ref:`afterSetProperties <no-16270>`             
:ref:`appendToolBarButton <no-16271>`            
:ref:`autoBindEvents <no-16272>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-16273>`                   
:ref:`beforeClose <no-16274>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-16275>`                   
:ref:`beforeDeleteAll <no-16276>`                
:ref:`beforeFilter <no-16277>`                   
:ref:`beforeFirst <no-16278>`                    
:ref:`beforeInit <no-16279>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-16280>`                     
:ref:`beforeNew <no-16281>`                      
:ref:`beforeNext <no-16282>`                     
:ref:`beforePointerMove <no-16283>`              
:ref:`beforePrior <no-16284>`                    
:ref:`beforeRequery <no-16285>`                  
:ref:`beforeSave <no-16286>`                     
:ref:`beforeSetProperties <no-16287>`            
:ref:`bindEvent <no-16288>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-16289>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-16290>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-16291>`                   Makes this object topmost
:ref:`cancel <no-16292>`                         Ask the bizobj to cancel its changes.
:ref:`clear <no-16293>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-16294>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-16295>`                          This method will close the form. If force = False (default)
:ref:`closing <no-16296>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-16297>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-16298>`           Given a position relative to this control, return a position relative
:ref:`copy <no-16299>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-16300>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-16301>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-16302>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-16303>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-16304>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-16305>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-16306>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-16307>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-16308>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-16309>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-16310>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-16311>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-16312>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-16313>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-16314>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-16315>`                       Draws text on the object at the specified position
:ref:`endHover <no-16316>`                       
:ref:`fillPreferenceDialog <no-16317>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-16318>`                         Apply a filter to the bizobj's data.
:ref:`first <no-16319>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-16320>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-16321>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-16322>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-16323>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-16324>`              
:ref:`formCoordinates <no-16325>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-16326>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-16327>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-16328>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-16329>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-16330>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-16331>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-16332>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-16333>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-16334>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-16335>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-16336>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-16337>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-16338>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-16339>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-16340>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-16341>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-16342>`                           Make the object invisible.
:ref:`initEvents <no-16343>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-16344>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-16345>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-16346>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-16347>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-16348>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-16349>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-16350>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-16351>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-16352>`                Move the record pointer to the specified row.
:ref:`new <no-16353>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-16354>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-16355>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-16356>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-16357>`                       
:ref:`onChildBorn <no-16358>`                    
:ref:`onDelete <no-16359>`                       
:ref:`onEditRedo <no-16360>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-16361>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-16362>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-16363>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-16364>`                        
:ref:`onHover <no-16365>`                        
:ref:`onLast <no-16366>`                         
:ref:`onNew <no-16367>`                          
:ref:`onNext <no-16368>`                         
:ref:`onPrior <no-16369>`                        
:ref:`onRequery <no-16370>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onSave <no-16371>`                         
:ref:`paste <no-16372>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-16373>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-16374>`                    
:ref:`prior <no-16375>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-16376>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-16377>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-16378>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-16379>`                     Raise the passed Dabo event.
:ref:`reCreate <no-16380>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-16381>`                       Recreate the object.
:ref:`redraw <no-16382>`                         Called when the object is (re)drawn.
:ref:`refresh <no-16383>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-16384>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-16385>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-16386>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-16387>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-16388>`              
:ref:`removeFilter <no-16389>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-16390>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-16391>`       
:ref:`requery <no-16392>`                        Ask the bizobj to requery.
:ref:`restoreSizeAndPosition <no-16393>`         Restore the panel layout, if possible, then call the default behavior.
:ref:`restoreSizeAndPositionIfNeeded <no-16394>` 
:ref:`safeDestroy <no-16395>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-16396>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-16397>`            Save the panel layout info, then call the default behavior.
:ref:`sendToBack <no-16398>`                     Places this object behind all others.
:ref:`setAll <no-16399>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-16400>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-16401>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-16402>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-16403>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-16404>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-16405>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-16406>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-16407>`                  Set the status text to val.
:ref:`show <no-16408>`                           Make the object visible.
:ref:`showContainingPage <no-16409>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-16410>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-16411>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-16412>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-16413>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-16414>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-16415>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-16416>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-16417>`                         
:ref:`validateField <no-16418>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods
=======

.. _no-16250:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.addObject(self, classRef, Name=None, \*args, \**kwargs)

   
   To support the old addObject() syntax, we need to re-direct the request
   to the center panel.
   



-------

.. _no-16251:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.addPanel(self, \*args, \**kwargs)

   Adds a dockable panel to the form.



-------

.. _no-16358:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onChildBorn(self, evt)



-------

.. _no-16393:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.restoreSizeAndPosition(self)

   Restore the panel layout, if possible, then call the default behavior.



-------

.. _no-16397:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.saveSizeAndPosition(self)

   Save the panel layout info, then call the default behavior.



-------

.. _no-16417:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.update(self, interval=None)



-------


Methods - inherited
=====================

.. _no-16247:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16248:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16249:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16252:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16253:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16254:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16255:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16256:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16257:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16258:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16259:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16260:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16261:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16262:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16263:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16264:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16265:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16266:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16267:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16268:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16269:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16270:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16271:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16272:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.autoBindEvents(self, force=True)
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

.. _no-16273:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16274:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16275:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16276:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16277:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16278:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16279:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16280:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16281:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16282:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16283:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16284:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16285:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16286:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16287:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16288:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16289:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16290:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-16291:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16292:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.cancel(self, dataSource=None, ignoreNoRecords=None)
   :noindex:


   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16293:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16294:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16295:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16296:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16297:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.confirmChanges(self, bizobjs=None)
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

.. _no-16298:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16299:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16300:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16301:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16302:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16303:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16304:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16305:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16306:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-16307:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16308:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16309:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16310:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16311:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16312:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16313:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16314:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16315:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16316:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16317:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16318:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16319:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16320:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16321:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16322:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16323:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16324:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16325:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16326:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16327:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16328:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getBizobjsToCheck(self)
   :noindex:


   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16329:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16330:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16331:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16332:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16333:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16334:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16335:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16336:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16337:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16338:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-16339:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16340:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16341:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16342:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16343:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16344:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16345:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16346:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16347:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16348:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16349:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.lockDisplay(self)
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

.. _no-16350:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16351:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16352:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16353:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16354:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16355:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16356:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16357:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onCancel(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16359:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onDelete(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16360:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16361:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16362:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16363:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16364:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16365:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16366:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16367:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onNew(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16368:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16369:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16370:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onRequery(self, evt)
   :noindex:


   Occurs when an EVT_MENU event is received by this form.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16371:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.onSave(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16372:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16373:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16374:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16375:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16376:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16377:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16378:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16379:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16380:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16381:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16382:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16383:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.refresh(self, interval=None)
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

.. _no-16384:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16385:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16386:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16387:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16388:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16389:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16390:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16391:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16392:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.requery(self, dataSource=None)
   :noindex:


   Ask the bizobj to requery.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16394:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16395:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16396:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.save(self, dataSource=None)
   :noindex:


   Ask the bizobj to commit its changes to the backend.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16398:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16399:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-16400:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16401:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16402:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-16403:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-16404:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-16405:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16406:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16407:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16408:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16409:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16410:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16411:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-16412:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16413:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16414:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16415:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16416:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16418:

.. function:: dabo.ui.uiwx.dDockForm.dDockForm.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
