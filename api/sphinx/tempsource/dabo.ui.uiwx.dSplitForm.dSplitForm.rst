
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dSplitForm

.. _dabo.ui.uiwx.dSplitForm.dSplitForm:

==============================================
|doc_title|  **dSplitForm.dSplitForm** - class
==============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dSplitForm**

.. inheritance-diagram:: dSplitForm


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dForm.dForm`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dShell.dShellForm`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dSplitForm.png
          :scale: 75 %
          :target: _static/winWidgets/dSplitForm.png
          :alt: dSplitForm



     - .. image:: _static/nixWidgets/dSplitForm.png
          :scale: 75 %
          :target: _static/nixWidgets/dSplitForm.png
          :alt: dSplitForm


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dSplitForm.dSplitForm

   .. automethod:: dabo.ui.uiwx.dSplitForm.dSplitForm.__init__

|method_summary| Properties Summary
===================================


============================================= ========================
:ref:`ActiveControl <no-33778>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-33779>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-33780>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-33781>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-33782>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-33783>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-33784>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-33785>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-33786>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-33787>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-33788>`                 Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-33789>`                      The position of the bottom side of the object. This is a
:ref:`CancelChildren <no-33790>`              Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-33791>`                     The caption of the object. (str)
:ref:`Centered <no-33792>`                    Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-33793>`             Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-33794>`                    Returns a list of object references to the children of
:ref:`Class <no-33795>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-33796>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-33797>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-33798>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-33799>`                     Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-33800>`             Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-33801>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-33802>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-33803>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-33804>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-33805>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-33806>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-33807>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-33808>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-33809>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-33810>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-33811>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-33812>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-33813>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-33814>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-33815>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-33816>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-33817>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-33818>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-33819>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-33820>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-33821>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-33822>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-33823>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-33824>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-33825>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMinPanelSize <no-33826>`         Dynamically determine the value of the MinPanelSize property.
:ref:`DynamicMousePointer <no-33827>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicOrientation <no-33828>`          Dynamically determine the value of the Orientation property.
:ref:`DynamicPosition <no-33829>`             Dynamically determine the value of the Position property.
:ref:`DynamicSashPosition <no-33830>`         Dynamically determine the value of the SashPosition property.
:ref:`DynamicShowCaption <no-33831>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-33832>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-33833>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-33834>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-33835>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-33836>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-33837>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-33838>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-33839>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-33840>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-33841>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-33842>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-33843>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-33844>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-33845>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-33846>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-33847>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-33848>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-33849>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-33850>`                    Specifies the font face. (str)
:ref:`FontInfo <no-33851>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-33852>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-33853>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-33854>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-33855>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-33856>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-33857>`                      Specifies the height of the object. (int)
:ref:`HelpContextText <no-33858>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-33859>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-33860>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-33861>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-33862>`                        Specifies the left position of the object. (int)
:ref:`LogEvents <no-33863>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-33864>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-33865>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-33866>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-33867>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-33868>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-33869>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-33870>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinPanelSize <no-33871>`                Controls the minimum width/height of the panels.  (int)
:ref:`MinimumHeight <no-33872>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-33873>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-33874>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-33875>`                       Specifies whether this dForm is modal or not  (bool)
:ref:`MousePointer <no-33876>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-33877>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-33878>`                    Specifies the base name of the object.
:ref:`Orientation <no-33879>`                 Determines if the window splits Horizontally or Vertically.  (str)
:ref:`Panel1 <no-33880>`                      Returns the Top/Left panel.  (SplitterPanel)
:ref:`Panel2 <no-33881>`                      Returns the Bottom/Right panel.  (SplitterPanel)
:ref:`Parent <no-33882>`                      The containing object. (obj)
:ref:`Position <no-33883>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-33884>`           Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-33885>`               Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-33886>`                       A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-33887>`               Specifies whether an automatic requery happens when the
:ref:`Right <no-33888>`                       The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-33889>`          Specifies optional delay to wait for updating the entire form when the user
:ref:`SashPosition <no-33890>`                Position of the sash when the window is split.  (int)
:ref:`SaveAllRows <no-33891>`                 Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-33892>`                Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-33893>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-33894>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-33895>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-33896>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-33897>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-33898>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-33899>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-33900>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-33901>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-33902>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-33903>`                        The size of the object. (tuple)
:ref:`Sizer <no-33904>`                       The sizer for the object.
:ref:`SizersToOutline <no-33905>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`Splitter <no-33906>`                    Reference to the main splitter in the form  (dSplitter
:ref:`StatusBar <no-33907>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-33908>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-33909>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-33910>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-33911>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-33912>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-33913>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-33914>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-33915>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-33916>`                         The top position of the object. (int)
:ref:`Transparency <no-33917>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-33918>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-33919>`                     Specifies whether the form is shown or hidden.  (bool)
:ref:`VisibleOnScreen <no-33920>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-33921>`                       The width of the object. (int)
:ref:`WindowHandle <no-33922>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-33923>`                 Specifies the current state of the form. (int)

============================================= ========================


Properties
==========

.. _no-33826:

**DynamicMinPanelSize** 

Dynamically determine the value of the MinPanelSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MinPanelSize property. If DynamicMinPanelSize is set to None (the default), MinPanelSize
will not be dynamically evaluated.



-------

.. _no-33828:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-33830:

**DynamicSashPosition** 

Dynamically determine the value of the SashPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SashPosition property. If DynamicSashPosition is set to None (the default), SashPosition
will not be dynamically evaluated.



-------

.. _no-33871:

**MinPanelSize** 

Controls the minimum width/height of the panels.  (int)



-------

.. _no-33879:

**Orientation** 

Determines if the window splits Horizontally or Vertically.  (str)



-------

.. _no-33880:

**Panel1** 

Returns the Top/Left panel.  (SplitterPanel)



-------

.. _no-33881:

**Panel2** 

Returns the Bottom/Right panel.  (SplitterPanel)



-------

.. _no-33890:

**SashPosition** 

Position of the sash when the window is split.  (int)



-------

.. _no-33906:

**Splitter** 

Reference to the main splitter in the form  (dSplitter



-------


Properties - inherited
========================

.. _no-33778:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33779:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33780:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33781:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33782:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33783:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33784:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33785:

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

.. _no-33786:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33787:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33788:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33789:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33790:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33791:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33792:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33793:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33794:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33795:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33796:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33797:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33798:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33799:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33800:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33801:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33802:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33803:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33804:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33805:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33806:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33807:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33808:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33809:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33810:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33811:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33812:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33813:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33814:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33815:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33816:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33817:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33818:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33819:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33820:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33821:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33822:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33823:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33824:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33825:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33827:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33829:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33831:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33832:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33833:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33834:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33835:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33836:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33837:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33838:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33839:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33840:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33841:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33842:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33843:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33844:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33845:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33846:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33847:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33848:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33849:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33850:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33851:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33852:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33853:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33854:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33855:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33856:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33857:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33858:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33859:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33860:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-33861:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33862:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33863:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33864:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33865:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33866:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33867:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33868:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-33869:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33870:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33872:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33873:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33874:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33875:

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

.. _no-33876:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33877:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33878:

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

.. _no-33882:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33883:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33884:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33885:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33886:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33887:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33888:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-33889:

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

.. _no-33891:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33892:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33893:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33894:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33895:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33896:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33897:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33898:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33899:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33900:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33901:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33902:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33903:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33904:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-33905:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33907:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-33908:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33909:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33910:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33911:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33912:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33913:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33914:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-33915:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33916:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33917:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33918:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33919:

**Visible** 

Specifies whether the form is shown or hidden.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33920:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33921:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33922:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33923:

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
:ref:`Activate <no-33924>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-33925>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-33926>`              Occurs when a child control is created.
:ref:`Close <no-33927>`                  Occurs when the user closes the form.
:ref:`ControlNavigationEvent <no-33928>` 
:ref:`Create <no-33929>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-33930>`             Occurs when another form becomes active.
:ref:`Destroy <no-33931>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-33932>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-33933>`               Occurs when the control gets the focus.
:ref:`Idle <no-33934>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-33935>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-33936>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-33937>`               
:ref:`KeyUp <no-33938>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-33939>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-33940>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-33941>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-33942>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-33943>`             
:ref:`MouseLeave <no-33944>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-33945>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-33946>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-33947>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-33948>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-33949>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-33950>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-33951>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-33952>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-33953>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-33954>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-33955>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-33956>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-33957>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-33958>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-33959>`                   Occurs when the control's position changes.
:ref:`Paint <no-33960>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-33961>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-33962>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-33963>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-33964>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-33924:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-33925:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-33926:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-33927:

**Close** 

Occurs when the user closes the form.



-------

.. _no-33928:

**ControlNavigationEvent** 



-------

.. _no-33929:

**Create** 

Occurs after the control or form is created.



-------

.. _no-33930:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-33931:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-33932:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-33933:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-33934:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-33935:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-33936:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-33937:

**KeyEvent** 



-------

.. _no-33938:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-33939:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-33940:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-33941:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-33942:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-33943:

**MouseEvent** 



-------

.. _no-33944:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-33945:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-33946:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-33947:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-33948:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-33949:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-33950:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-33951:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-33952:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-33953:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-33954:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-33955:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-33956:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-33957:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-33958:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-33959:

**Move** 

Occurs when the control's position changes.



-------

.. _no-33960:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-33961:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-33962:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-33963:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-33964:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


================================================ ========================
:ref:`absoluteCoordinates <no-33965>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-33966>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-33967>`                      Add a bizobj to this form.
:ref:`addObject <no-33968>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-33969>`            
:ref:`afterCancel <no-33970>`                    
:ref:`afterDelete <no-33971>`                    
:ref:`afterDeleteAll <no-33972>`                 
:ref:`afterFilter <no-33973>`                    
:ref:`afterFirst <no-33974>`                     
:ref:`afterInit <no-33975>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-33976>`                   
:ref:`afterLast <no-33977>`                      
:ref:`afterNew <no-33978>`                       
:ref:`afterNext <no-33979>`                      
:ref:`afterPointerMove <no-33980>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-33981>`                     
:ref:`afterRequery <no-33982>`                   
:ref:`afterRowNavigation <no-33983>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-33984>`                      
:ref:`afterSetMenuBar <no-33985>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-33986>`          Subclass hook.
:ref:`afterSetProperties <no-33987>`             
:ref:`appendToolBarButton <no-33988>`            
:ref:`autoBindEvents <no-33989>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-33990>`                   
:ref:`beforeClose <no-33991>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-33992>`                   
:ref:`beforeDeleteAll <no-33993>`                
:ref:`beforeFilter <no-33994>`                   
:ref:`beforeFirst <no-33995>`                    
:ref:`beforeInit <no-33996>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-33997>`                     
:ref:`beforeNew <no-33998>`                      
:ref:`beforeNext <no-33999>`                     
:ref:`beforePointerMove <no-34000>`              
:ref:`beforePrior <no-34001>`                    
:ref:`beforeRequery <no-34002>`                  
:ref:`beforeSave <no-34003>`                     
:ref:`beforeSetProperties <no-34004>`            
:ref:`bindEvent <no-34005>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-34006>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-34007>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-34008>`                   Makes this object topmost
:ref:`cancel <no-34009>`                         Ask the bizobj to cancel its changes.
:ref:`clear <no-34010>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-34011>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-34012>`                          This method will close the form. If force = False (default)
:ref:`closing <no-34013>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-34014>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-34015>`           Given a position relative to this control, return a position relative
:ref:`copy <no-34016>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-34017>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-34018>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-34019>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-34020>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-34021>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-34022>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-34023>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-34024>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-34025>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-34026>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-34027>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-34028>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-34029>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-34030>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-34031>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-34032>`                       Draws text on the object at the specified position
:ref:`endHover <no-34033>`                       
:ref:`fillPreferenceDialog <no-34034>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-34035>`                         Apply a filter to the bizobj's data.
:ref:`first <no-34036>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-34037>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-34038>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-34039>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-34040>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-34041>`              
:ref:`formCoordinates <no-34042>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-34043>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-34044>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-34045>`              Return the list of bizobj's to check for changes during confirmChanges().
:ref:`getCaptureBitmap <no-34046>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-34047>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-34048>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-34049>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-34050>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-34051>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-34052>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-34053>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-34054>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-34055>`                  Returns a dictionary of property name/value pairs.
:ref:`getSQL <no-34056>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-34057>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-34058>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-34059>`                           Make the object invisible.
:ref:`initEvents <no-34060>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-34061>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-34062>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-34063>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-34064>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-34065>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-34066>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-34067>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-34068>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-34069>`                Move the record pointer to the specified row.
:ref:`new <no-34070>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-34071>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-34072>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-34073>`              Given a position relative to the form, return a position relative
:ref:`onCancel <no-34074>`                       
:ref:`onDelete <no-34075>`                       
:ref:`onEditRedo <no-34076>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-34077>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-34078>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-34079>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-34080>`                        
:ref:`onHover <no-34081>`                        
:ref:`onLast <no-34082>`                         
:ref:`onNew <no-34083>`                          
:ref:`onNext <no-34084>`                         
:ref:`onPrior <no-34085>`                        
:ref:`onRequery <no-34086>`                      Occurs when an EVT_MENU event is received by this form.
:ref:`onSave <no-34087>`                         
:ref:`paste <no-34088>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-34089>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-34090>`                    
:ref:`prior <no-34091>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-34092>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-34093>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-34094>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-34095>`                     Raise the passed Dabo event.
:ref:`reCreate <no-34096>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-34097>`                       Recreate the object.
:ref:`redraw <no-34098>`                         Called when the object is (re)drawn.
:ref:`refresh <no-34099>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-34100>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-34101>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-34102>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-34103>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-34104>`              
:ref:`removeFilter <no-34105>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-34106>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-34107>`       
:ref:`requery <no-34108>`                        Ask the bizobj to requery.
:ref:`restoreSizeAndPosition <no-34109>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-34110>` 
:ref:`safeDestroy <no-34111>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-34112>`                           Ask the bizobj to commit its changes to the backend.
:ref:`saveSizeAndPosition <no-34113>`            Save the current size and position of this form.
:ref:`sendToBack <no-34114>`                     Places this object behind all others.
:ref:`setAll <no-34115>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-34116>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-34117>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-34118>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-34119>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-34120>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-34121>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-34122>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-34123>`                  Set the status text to val.
:ref:`show <no-34124>`                           Make the object visible.
:ref:`showContainingPage <no-34125>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-34126>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-34127>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`split <no-34128>`                          
:ref:`super <no-34129>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-34130>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-34131>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-34132>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-34133>`               Immediately unlocks the display, no matter how many previous
:ref:`unsplit <no-34134>`                        
:ref:`update <no-34135>`                         Updates the contained controls with current values from the source.
:ref:`validateField <no-34136>`                  Call the bizobj for the control's DataSource. If the control's

================================================ ========================


Methods
=======

.. _no-34128:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.split(self, dir=None)



-------

.. _no-34134:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.unsplit(self)



-------


Methods - inherited
=====================

.. _no-33965:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33966:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33967:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33968:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-33969:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33970:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33971:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33972:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33973:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33974:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33975:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33976:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33977:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33978:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33979:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33980:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33981:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33982:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33983:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33984:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33985:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33986:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33987:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-33988:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33989:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.autoBindEvents(self, force=True)
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

.. _no-33990:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33991:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-33992:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33993:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33994:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33995:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33996:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-33997:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33998:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-33999:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34000:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34001:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34002:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34003:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34004:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34005:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34006:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34007:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-34008:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34009:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.cancel(self, dataSource=None, ignoreNoRecords=None)
   :noindex:


   
   Ask the bizobj to cancel its changes.
   
   This will revert back to the state of the records when they were last
   requeried or saved.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34010:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34011:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34012:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34013:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34014:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.confirmChanges(self, bizobjs=None)
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

.. _no-34015:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34016:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34017:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34018:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34019:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34020:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34021:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34022:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34023:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-34024:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34025:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34026:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34027:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34028:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34029:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34030:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34031:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34032:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34033:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34034:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34035:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34036:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34037:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34038:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34039:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34040:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34041:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34042:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34043:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34044:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34045:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getBizobjsToCheck(self)
   :noindex:


   
   Return the list of bizobj's to check for changes during confirmChanges().
   
   The default behavior is to simply check the primary bizobj, however there
   may be cases in subclasses where a different bizobj may be checked, or even
   several. In those cases, override    this method and return a list of the
   required bizobjs.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34046:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34047:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34048:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34049:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34050:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34051:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34052:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34053:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34054:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34055:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-34056:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34057:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34058:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34059:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34060:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34061:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34062:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34063:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34064:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34065:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34066:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.lockDisplay(self)
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

.. _no-34067:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34068:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34069:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34070:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34071:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34072:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34073:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34074:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onCancel(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34075:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onDelete(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34076:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34077:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34078:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34079:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34080:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34081:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34082:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34083:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onNew(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34084:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34085:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34086:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onRequery(self, evt)
   :noindex:


   Occurs when an EVT_MENU event is received by this form.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34087:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.onSave(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34088:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34089:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34090:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34091:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34092:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34093:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34094:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34095:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34096:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34097:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34098:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34099:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.refresh(self, interval=None)
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

.. _no-34100:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34101:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34102:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34103:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34104:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34105:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34106:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34107:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34108:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.requery(self, dataSource=None)
   :noindex:


   Ask the bizobj to requery.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34109:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34110:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34111:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34112:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.save(self, dataSource=None)
   :noindex:


   Ask the bizobj to commit its changes to the backend.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34113:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34114:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34115:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-34116:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34117:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34118:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-34119:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-34120:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-34121:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34122:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34123:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34124:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34125:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34126:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34127:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-34129:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34130:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34131:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34132:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34133:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34135:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.update(self, interval=None)
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

.. _no-34136:

.. function:: dabo.ui.uiwx.dSplitForm.dSplitForm.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
