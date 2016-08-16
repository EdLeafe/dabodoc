
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Form

.. _dabo.lib.datanav.Form.Form:

==================================
|doc_title|  **Form.Form** - class
==================================


This is a dForm but with the following added controls:

+ Navigation Menu
+ Navigation ToolBar
+ PageFrame with 3 pages by default:
+ Select : Enter sql-select criteria.
+ Browse : Browse the result set and pick an item to edit.
+ Edit     : Edit the current record in the result set.





|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Form**

.. inheritance-diagram:: Form


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dForm.dForm`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Form.Form


|method_summary| Properties Summary
===================================


================================================= ========================
:ref:`ActiveControl <no-5709>`                    Contains a reference to the active control on the form, or None.
:ref:`AddChildEditPages <no-5710>`                Should the form automatically add edit pages for child bizobjs?
:ref:`Application <no-5711>`                      Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoUpdateStatusText <no-5712>`             Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-5713>`                        Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-5714>`                        The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-5715>`                      Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-5716>`                      Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-5717>`                  Style of line for the border drawn around the control.
:ref:`BorderResizable <no-5718>`                  Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-5719>`                      Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-5720>`                      Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-5721>`                           The position of the bottom side of the object. This is a
:ref:`BrowseGridClass <no-5722>`                  Specifies the class to use for the browse grid.
:ref:`BrowsePageClass <no-5723>`                  Specifies the class to use for the browse page.
:ref:`CancelChildren <no-5724>`                   Specifies whether changes are canceled from child bizobjs. (bool; default:True)
:ref:`Caption <no-5725>`                          The caption of the object. (str)
:ref:`Centered <no-5726>`                         Centers the form on the screen when set to True.  (bool)
:ref:`CheckForChanges <no-5727>`                  Specifies whether the user is prompted to save or discard changes. (bool)
:ref:`Children <no-5728>`                         Returns a list of object references to the children of
:ref:`Class <no-5729>`                            The class the object is based on. Read-only.  (class)
:ref:`Connection <no-5730>`                       The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-5731>`                 Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-5732>`             Reference to the sizer item that control's this control's layout.
:ref:`CustomSQL <no-5733>`                        Specifies custom (overridden) SQL to use.
:ref:`CxnName <no-5734>`                          Name of the connection used for data access  (str)
:ref:`DataUpdateDelay <no-5735>`                  Specifies synchronization delay in data updates from business
:ref:`DroppedFileHandler <no-5736>`               Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-5737>`               Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoUpdateStatusText <no-5738>`      Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-5739>`                 Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-5740>`               Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-5741>`           Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-5742>`           Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-5743>`               Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-5744>`               Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-5745>`                   Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-5746>`                  Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-5747>`                Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-5748>`                   Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-5749>`             Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-5750>`                      Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-5751>`                  Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-5752>`                  Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-5753>`                Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-5754>`                  Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-5755>`             Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-5756>`                 Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-5757>`                    Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-5758>`                      Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-5759>`                      Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-5760>`                   Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-5761>`              Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-5762>`                  Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-5763>`               Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-5764>`             Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-5765>`                      Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-5766>`                 Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-5767>`                Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-5768>`                       Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-5769>`                   Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-5770>`               Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-5771>`                       Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-5772>`              Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-5773>`                   Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-5774>`                     Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-5775>`               Dynamically determine the value of the WindowState property.
:ref:`EditPageClass <no-5776>`                    Specifies the class to use for the edit page.
:ref:`EnableChildRequeriesWhenBrowsing <no-5777>` Specifies whether child bizobjs are requeried automatically when the parent
:ref:`EnableChildRequeriesWhenEditing <no-5778>`  Specifies whether child bizobjs are requeried automatically when the parent
:ref:`Enabled <no-5779>`                          Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-5780>`                    Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-5781>`                    Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-5782>`                             Specifies font object for this control. (dFont)
:ref:`FontBold <no-5783>`                         Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-5784>`                  Human-readable description of the current font settings. (str)
:ref:`FontFace <no-5785>`                         Specifies the font face. (str)
:ref:`FontInfo <no-5786>`                         Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-5787>`                       Specifies whether font is italicized. (bool)
:ref:`FontSize <no-5788>`                         Specifies the point size of the font. (int)
:ref:`FontUnderline <no-5789>`                    Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-5790>`                        Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-5791>`                             Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`FormType <no-5792>`                         Specifies the type of form this is.
:ref:`Height <no-5793>`                           Specifies the height of the object. (int)
:ref:`HelpContextText <no-5794>`                  Specifies the context-sensitive help text associated with this
:ref:`Hover <no-5795>`                            When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-5796>`                             Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-5797>`              Controls how often the form is refreshed when idle.
:ref:`Left <no-5798>`                             Specifies the left position of the object. (int)
:ref:`LogEvents <no-5799>`                        Specifies which events to log.  (list of strings)
:ref:`MDI <no-5800>`                              Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-5801>`                    Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-5802>`                      Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-5803>`                     Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-5804>`                          Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-5805>`                     Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-5806>`                      Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-5807>`                    Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-5808>`                      Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-5809>`                     Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-5810>`                            Specifies whether this dForm is modal or not  (bool)
:ref:`MousePointer <no-5811>`                     Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-5812>`                             Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-5813>`                         Specifies the base name of the object.
:ref:`PageFrameStyle <no-5814>`                   Specifies the style of pageframe to set up. Valid values are:
:ref:`PageTabPosition <no-5815>`                  Specifies the location of the pageframe tabs. Valid values are:
:ref:`Parent <no-5816>`                           The containing object. (obj)
:ref:`Position <no-5817>`                         The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-5818>`                Reference to the Preference Management object  (dPref)
:ref:`PrimaryBizobj <no-5819>`                    Reference to the primary bizobj for this form  (dBizobj)
:ref:`RegID <no-5820>`                            A unique identifier used for referencing by other objects. (str)
:ref:`RequeryOnLoad <no-5821>`                    Specifies whether an automatic requery happens when the
:ref:`Right <no-5822>`                            The position of the right side of the object. This is a
:ref:`RowNavigationDelay <no-5823>`               Specifies optional delay to wait for updating the entire form when the user
:ref:`SaveAllRows <no-5824>`                      Specifies whether changes are saved to all rows, or just the current row. (bool)
:ref:`SaveChildren <no-5825>`                     Specifies whether changes are saved to child bizobjs. (bool; default:True)
:ref:`SaveRestorePosition <no-5826>`              Specifies whether the form's position and size as set by the user
:ref:`SelectPageClass <no-5827>`                  Specifies the class to use for the select page.
:ref:`SetFocusToBrowseGrid <no-5828>`             Does the focus go to the browse grid when the browse page is entered?
:ref:`ShowAdvancedQuickReport <no-5829>`          Does the 'Advanced' button appear in the Quick Report dialog?
:ref:`ShowCaption <no-5830>`                      Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-5831>`                  Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowExpandedQuickReport <no-5832>`          Can the user choose the 'expanded' quick report?
:ref:`ShowInTaskBar <no-5833>`                    Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-5834>`                    Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-5835>`                      Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-5836>`                    Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowSortFields <no-5837>`                   Can the user sort fields in the select page?
:ref:`ShowStatusBar <no-5838>`                    Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-5839>`                   Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-5840>`                      Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-5841>`                             The size of the object. (tuple)
:ref:`Sizer <no-5842>`                            The sizer for the object.
:ref:`SizersToOutline <no-5843>`                  When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-5844>`                        Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-5845>`                   Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-5846>`                       Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-5847>`                        Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-5848>`                              A property that user code can safely use for specific purposes.
:ref:`TempForm <no-5849>`                         Used to indicate that this is a temporary form, and that its settings
:ref:`Testing <no-5850>`                          Flag for use when testing elements of the form.
:ref:`TinyTitleBar <no-5851>`                     Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-5852>`                          Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-5853>`                      Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-5854>`                              The top position of the object. (int)
:ref:`Transparency <no-5855>`                     Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-5856>`                Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-5857>`                          Specifies whether the form is shown or hidden.  (bool)
:ref:`VisibleOnScreen <no-5858>`                  Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-5859>`                            The width of the object. (int)
:ref:`WindowHandle <no-5860>`                     The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-5861>`                      Specifies the current state of the form. (int)

================================================= ========================


Properties
==========

.. _no-5710:

**AddChildEditPages** 

Should the form automatically add edit pages for child bizobjs?

    The default is False, and this property may be removed soon.



-------

.. _no-5722:

**BrowseGridClass** 

Specifies the class to use for the browse grid.



-------

.. _no-5723:

**BrowsePageClass** 

Specifies the class to use for the browse page.



-------

.. _no-5733:

**CustomSQL** 

Specifies custom (overridden) SQL to use.



-------

.. _no-5776:

**EditPageClass** 

Specifies the class to use for the edit page.



-------

.. _no-5777:

**EnableChildRequeriesWhenBrowsing** 

Specifies whether child bizobjs are requeried automatically when the parent
    RowNumber changes, while in the browse page. Default: True

    Turning this to False will result in better performance of the browse grid when
    there are lots of child bizobjs, but it may result in unintended consequences
    which is why it is True by default.



-------

.. _no-5778:

**EnableChildRequeriesWhenEditing** 

Specifies whether child bizobjs are requeried automatically when the parent
    RowNumber changes, while not in the browse page. Default: True



-------

.. _no-5792:

**FormType** 

Specifies the type of form this is.

    The type of form determines the runtime behavior. FormType can be one of:
        Normal:
            A normal dataNav form. The default.

        PickList:
            Only select/browse pages shown, and the form is modal, returning the
            Primary Key of the picked record.

        Edit:
            Modal version of normal, with no Select/Browse pages. User code sends
            the Primary Key of the record to edit.
    



-------

.. _no-5814:

**PageFrameStyle** 

Specifies the style of pageframe to set up. Valid values are:

        Tabs (default)
        List (down the side)
        Select
    



-------

.. _no-5815:

**PageTabPosition** 

Specifies the location of the pageframe tabs. Valid values are:

        Top (default)
        Left
        Right
        Bottom

        This only applies when PageFrameStyle is set to "Tabs".
    



-------

.. _no-5827:

**SelectPageClass** 

Specifies the class to use for the select page.



-------

.. _no-5828:

**SetFocusToBrowseGrid** 

Does the focus go to the browse grid when the browse page is entered?



-------

.. _no-5829:

**ShowAdvancedQuickReport** 

Does the 'Advanced' button appear in the Quick Report dialog?



-------

.. _no-5832:

**ShowExpandedQuickReport** 

Can the user choose the 'expanded' quick report?



-------

.. _no-5837:

**ShowSortFields** 

Can the user sort fields in the select page?



-------

.. _no-5850:

**Testing** 

Flag for use when testing elements of the form.



-------


Properties - inherited
========================

.. _no-5709:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5711:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5712:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5713:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5714:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5715:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5716:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5717:

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

.. _no-5718:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5719:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5720:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5721:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5724:

**CancelChildren** 

Specifies whether changes are canceled from child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5725:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5726:

**Centered** 

Centers the form on the screen when set to True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5727:

**CheckForChanges** 

Specifies whether the user is prompted to save or discard changes. (bool)

    If True (the default), when operations such as requery() or the closing
    of the form are about to occur, the user will be presented with a dialog
    box asking whether to save changes, discard changes, or cancel the
    operation that led to the dialog being presented.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5728:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5729:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5730:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5731:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5732:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5734:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5735:

**DataUpdateDelay** 

Specifies synchronization delay in data updates from business
    to UI layer. (int; default:100 [ms])

    Set to 0 or None to ensure controls reflect immediately to the data changes..


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5736:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5737:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5738:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5739:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5740:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5741:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5742:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5743:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5744:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5745:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5746:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5747:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5748:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5749:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5750:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5751:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5752:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5753:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5754:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5755:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5756:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5757:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5758:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5759:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5760:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5761:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5762:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5763:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5764:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5765:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5766:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5767:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5768:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5769:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5770:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5771:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5772:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5773:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5774:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5775:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5779:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5780:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5781:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5782:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5783:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5784:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5785:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5786:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5787:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5788:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5789:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5790:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5791:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5793:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5794:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5795:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5796:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-5797:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5798:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5799:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5800:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5801:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5802:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5803:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5804:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-5805:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5806:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5807:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5808:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5809:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5810:

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

.. _no-5811:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5812:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5813:

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

.. _no-5816:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5817:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5818:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5819:

**PrimaryBizobj** 

Reference to the primary bizobj for this form  (dBizobj)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5820:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5821:

**RequeryOnLoad** 

Specifies whether an automatic requery happens when the
    form is loaded.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5822:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5823:

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

.. _no-5824:

**SaveAllRows** 

Specifies whether changes are saved to all rows, or just the current row. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5825:

**SaveChildren** 

Specifies whether changes are saved to child bizobjs. (bool; default:True)


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5826:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5830:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5831:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5833:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5834:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5835:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5836:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5838:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5839:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5840:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5841:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5842:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-5843:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5844:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-5845:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5846:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5847:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5848:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5849:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5851:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5852:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: 'wx._windows.Frame - can not provide a link

-------

.. _no-5853:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5854:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5855:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5856:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5857:

**Visible** 

Specifies whether the form is shown or hidden.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5858:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5859:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5860:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5861:

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


======================================= ========================
:ref:`Activate <no-5862>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-5863>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-5864>`              Occurs when a child control is created.
:ref:`Close <no-5865>`                  Occurs when the user closes the form.
:ref:`ControlNavigationEvent <no-5866>` 
:ref:`Create <no-5867>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-5868>`             Occurs when another form becomes active.
:ref:`Destroy <no-5869>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-5870>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-5871>`               Occurs when the control gets the focus.
:ref:`Idle <no-5872>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-5873>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-5874>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-5875>`               
:ref:`KeyUp <no-5876>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-5877>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-5878>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-5879>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-5880>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-5881>`             
:ref:`MouseLeave <no-5882>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-5883>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-5884>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-5885>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-5886>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-5887>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-5888>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-5889>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-5890>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-5891>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-5892>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-5893>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-5894>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-5895>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-5896>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-5897>`                   Occurs when the control's position changes.
:ref:`Paint <no-5898>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-5899>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-5900>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-5901>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-5902>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-5862:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-5863:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-5864:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-5865:

**Close** 

Occurs when the user closes the form.



-------

.. _no-5866:

**ControlNavigationEvent** 



-------

.. _no-5867:

**Create** 

Occurs after the control or form is created.



-------

.. _no-5868:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-5869:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-5870:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-5871:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-5872:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-5873:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-5874:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-5875:

**KeyEvent** 



-------

.. _no-5876:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-5877:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-5878:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-5879:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-5880:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-5881:

**MouseEvent** 



-------

.. _no-5882:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-5883:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-5884:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-5885:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-5886:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-5887:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-5888:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-5889:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-5890:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-5891:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-5892:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-5893:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-5894:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-5895:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-5896:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-5897:

**Move** 

Occurs when the control's position changes.



-------

.. _no-5898:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-5899:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-5900:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-5901:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-5902:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-5903>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-5904>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addBizobj <no-5905>`                      Add a bizobj to this form.
:ref:`addEditPage <no-5906>`                    Called when it is time to add the edit page for the passed datasource.
:ref:`addEditPages <no-5907>`                   Called when it is time to add the edit page(s).
:ref:`addObject <no-5908>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-5909>`            
:ref:`afterCancel <no-5910>`                    
:ref:`afterDelete <no-5911>`                    
:ref:`afterDeleteAll <no-5912>`                 
:ref:`afterFilter <no-5913>`                    
:ref:`afterFirst <no-5914>`                     
:ref:`afterInit <no-5915>`                      
:ref:`afterInitAll <no-5916>`                   
:ref:`afterLast <no-5917>`                      
:ref:`afterNew <no-5918>`                       
:ref:`afterNext <no-5919>`                      
:ref:`afterPointerMove <no-5920>`               Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterPrior <no-5921>`                     
:ref:`afterRequery <no-5922>`                   
:ref:`afterRowNavigation <no-5923>`             Called after the PrimaryBizobj's RowNumber has changed,
:ref:`afterSave <no-5924>`                      
:ref:`afterSetMenuBar <no-5925>`                Subclasses can extend the menu bar here.
:ref:`afterSetPrimaryBizobj <no-5926>`          Subclass hook.
:ref:`afterSetProperties <no-5927>`             
:ref:`afterSetupPageFrame <no-5928>`            
:ref:`appendToolBarButton <no-5929>`            
:ref:`autoBindEvents <no-5930>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeCancel <no-5931>`                   
:ref:`beforeClose <no-5932>`                    Hook method. Returning False will prevent the form from
:ref:`beforeDelete <no-5933>`                   
:ref:`beforeDeleteAll <no-5934>`                
:ref:`beforeFilter <no-5935>`                   
:ref:`beforeFirst <no-5936>`                    
:ref:`beforeInit <no-5937>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeLast <no-5938>`                     
:ref:`beforeNew <no-5939>`                      
:ref:`beforeNext <no-5940>`                     
:ref:`beforePointerMove <no-5941>`              
:ref:`beforePrior <no-5942>`                    
:ref:`beforeRequery <no-5943>`                  
:ref:`beforeSave <no-5944>`                     
:ref:`beforeSetProperties <no-5945>`            
:ref:`beforeSetupPageFrame <no-5946>`           
:ref:`bindEvent <no-5947>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-5948>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-5949>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-5950>`                   Makes this object topmost
:ref:`cancel <no-5951>`                         
:ref:`clear <no-5952>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-5953>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-5954>`                          This method will close the form. If force = False (default)
:ref:`closing <no-5955>`                        Stub method to be customized in subclasses. At this point,
:ref:`confirmChanges <no-5956>`                 Ask the user if they want to save changes, discard changes, or cancel.
:ref:`containerCoordinates <no-5957>`           Given a position relative to this control, return a position relative
:ref:`copy <no-5958>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-5959>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-5960>`                            Called by uiApp when the user requests a cut operation.
:ref:`delete <no-5961>`                         Ask the bizobj to delete the current record.
:ref:`deleteAll <no-5962>`                      Ask the primary bizobj to delete all records from the recordset.
:ref:`drawArc <no-5963>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-5964>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-5965>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-5966>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-5967>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-5968>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-5969>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-5970>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-5971>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-5972>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-5973>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-5974>`                       Draws text on the object at the specified position
:ref:`enableQuickReport <no-5975>`              
:ref:`endHover <no-5976>`                       
:ref:`fillPreferenceDialog <no-5977>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`filter <no-5978>`                         Apply a filter to the bizobj's data.
:ref:`first <no-5979>`                          Ask the bizobj to move to the first record.
:ref:`fitToSizer <no-5980>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-5981>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-5982>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-5983>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-5984>`              
:ref:`formCoordinates <no-5985>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-5986>`                Return the fully qualified name of the object.
:ref:`getAutoReportForm_expanded <no-5987>`     
:ref:`getAutoReportForm_list <no-5988>`         
:ref:`getBizobj <no-5989>`                      Return the bizobj with the passed dataSource. If no
:ref:`getBizobjsToCheck <no-5990>`              The primary bizobj may be for one of the child pages.
:ref:`getCaptureBitmap <no-5991>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getConfirmChangesQueryMessage <no-5992>`  Return the "Save Changes?" message for use in the query dialog.
:ref:`getContainingPage <no-5993>`              Return the dPage or WizardPage that contains self.
:ref:`getCurrentRecordText <no-5994>`           Get the text to describe which record is current.
:ref:`getDisplayLocker <no-5995>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-5996>`                        
:ref:`getMousePosition <no-5997>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-5998>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-5999>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-6000>`                  Returns a dictionary of property name/value pairs.
:ref:`getReportForm <no-6001>`                  Returns the rfxml to generate a report for the dataset.
:ref:`getSQL <no-6002>`                         Get the current SQL from the bizobj.
:ref:`getSizerProp <no-6003>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-6004>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-6005>`                           Make the object invisible.
:ref:`initEvents <no-6006>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-6007>`                 
:ref:`isContainedBy <no-6008>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-6009>`                    Call the given function on this object and all of its Children. If
:ref:`last <no-6010>`                           Ask the bizobj to move to the last record.
:ref:`layout <no-6011>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-6012>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-6013>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-6014>`             Moves this object's tab order before the passed obj.
:ref:`moveToRowNumber <no-6015>`                Move the record pointer to the specified row.
:ref:`new <no-6016>`                            Ask the bizobj to add a new record to the recordset.
:ref:`next <no-6017>`                           Ask the bizobj to move to the next record.
:ref:`notifyUser <no-6018>`                     Displays an alert messagebox for the user. You can customize
:ref:`objectCoordinates <no-6019>`              Given a position relative to the form, return a position relative
:ref:`onBrowseRecords <no-6020>`                Occurs when the user chooses to browse the record set.
:ref:`onCancel <no-6021>`                       
:ref:`onConfigGrid <no-6022>`                   
:ref:`onDelete <no-6023>`                       
:ref:`onEditCurrentRecord <no-6024>`            Occurs when the user chooses to edit the current record.
:ref:`onEditRedo <no-6025>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-6026>`                     If you want your form to respond to the Undo menu item in
:ref:`onFieldValidationFailed <no-6027>`        Basic handling of field-level validation failure. You should
:ref:`onFieldValidationPassed <no-6028>`        Basic handling when field-level validation succeeds.
:ref:`onFirst <no-6029>`                        
:ref:`onHover <no-6030>`                        
:ref:`onLast <no-6031>`                         
:ref:`onNew <no-6032>`                          
:ref:`onNext <no-6033>`                         
:ref:`onPrior <no-6034>`                        
:ref:`onQuickReport <no-6035>`                  
:ref:`onRequery <no-6036>`                      Override the dForm behavior by running the requery through the select page.
:ref:`onSave <no-6037>`                         
:ref:`onSetSelectionCriteria <no-6038>`         Occurs when the user chooses to set the selection criteria.
:ref:`onShowSQL <no-6039>`                      
:ref:`paste <no-6040>`                          Called by uiApp when the user requests a paste operation.
:ref:`pickRecord <no-6041>`                     This form is a picklist, and the user chose a record in the grid.
:ref:`popStatusText <no-6042>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-6043>`                    
:ref:`prior <no-6044>`                          Ask the bizobj to move to the previous record.
:ref:`processDroppedFiles <no-6045>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-6046>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-6047>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-6048>`                     Raise the passed Dabo event.
:ref:`reCreate <no-6049>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-6050>`                       Recreate the object.
:ref:`redraw <no-6051>`                         Called when the object is (re)drawn.
:ref:`refresh <no-6052>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-6053>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-6054>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-6055>`                        Instead of just destroying the object, make sure that
:ref:`reload <no-6056>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-6057>`              
:ref:`removeFilter <no-6058>`                   Remove the most recently applied filter from the bizobj's data.
:ref:`removeFilters <no-6059>`                  Remove all filters from the bizobj's data.
:ref:`removeFromOutlinedSizers <no-6060>`       
:ref:`requery <no-6061>`                        
:ref:`restoreSizeAndPosition <no-6062>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-6063>` 
:ref:`safeDestroy <no-6064>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`save <no-6065>`                           
:ref:`saveSizeAndPosition <no-6066>`            Save the current size and position of this form.
:ref:`sendToBack <no-6067>`                     Places this object behind all others.
:ref:`setAll <no-6068>`                         Set all child object properties to the passed value.
:ref:`setFocus <no-6069>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-6070>`             Convenience method to let you call this directly on the object.
:ref:`setPrimaryBizobjToDefault <no-6071>`      This method is called when we leave an editing page. The
:ref:`setProperties <no-6072>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-6073>`          Sets a group of properties on the object all at once. This
:ref:`setSQL <no-6074>`                         Set the SQL for the bizobj.
:ref:`setSizerProp <no-6075>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-6076>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-6077>`                  Set the status text to val.
:ref:`setupMenu <no-6078>`                      Set up the action menu for this frame.
:ref:`setupPageFrame <no-6079>`                 Set up the select/browse/edit/n pageframe.
:ref:`setupSaveCancelButtons <no-6080>`         
:ref:`setupToolBar <no-6081>`                   
:ref:`show <no-6082>`                           Make the object visible.
:ref:`showContainingPage <no-6083>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-6084>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-6085>`                      Shows the form in a modal fashion. Other forms can still be
:ref:`super <no-6086>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-6087>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-6088>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-6089>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-6090>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-6091>`                         Updates the contained controls with current values from the source.
:ref:`validateField <no-6092>`                  Call the bizobj for the control's DataSource. If the control's

=============================================== ========================


Methods
=======

.. _no-5906:

.. function:: dabo.lib.datanav.Form.Form.addEditPage(self, ds, title)

   Called when it is time to add the edit page for the passed datasource.



-------

.. _no-5907:

.. function:: dabo.lib.datanav.Form.Form.addEditPages(self, ds)

   Called when it is time to add the edit page(s).



-------

.. _no-5915:

.. function:: dabo.lib.datanav.Form.Form.afterInit(self)



-------

.. _no-5928:

.. function:: dabo.lib.datanav.Form.Form.afterSetupPageFrame(self)



-------

.. _no-5946:

.. function:: dabo.lib.datanav.Form.Form.beforeSetupPageFrame(self)



-------

.. _no-5951:

.. function:: dabo.lib.datanav.Form.Form.cancel(self, dataSource=None)



-------

.. _no-5975:

.. function:: dabo.lib.datanav.Form.Form.enableQuickReport(self)



-------

.. _no-5987:

.. function:: dabo.lib.datanav.Form.Form.getAutoReportForm_expanded(self)



-------

.. _no-5988:

.. function:: dabo.lib.datanav.Form.Form.getAutoReportForm_list(self)



-------

.. _no-5990:

.. function:: dabo.lib.datanav.Form.Form.getBizobjsToCheck(self)

   
   The primary bizobj may be for one of the child pages.
   Therefore, we should return the main bizobj here
   



-------

.. _no-5996:

.. function:: dabo.lib.datanav.Form.Form.getMenu(self)



-------

.. _no-6001:

.. function:: dabo.lib.datanav.Form.Form.getReportForm(self, mode)

   
   Returns the rfxml to generate a report for the dataset.
   
   The mode is one of "list" or "expanded", and determines the format of the
   report output. "list" basically mimics the browse grid, with one line per
   record, and the columns as specified in the browse grid. "expanded" mimics
   the edit page, with any number of lines for each record.
   
   The rfxml can come from a few places, in descending precedence:
   
       1) if self.ReportForm["list"] or self.ReportForm["expanded"] exists,
          that will be used.    *** NOT IMPLEMENTED YET ***
       2) if self.ReportFormFile["list"] or self.ReportFormFile["expanded"] exists,
          that will be used.    *** NOT IMPLEMENTED YET ***
       3) if self.Application.HomeDirectory/reports/datanav-<cursorname>-(list|expanded).rfxml
          exists, that will be used. IOW, drop in a properly named rfxml file into
          the reports directory underneath your application home, and it will be used
          automatically.
       4) a generic report form will be generated. If mode=="list", the fields displayed
          will be as defined in the browse page. If mode=="expanded", the fields displayed
          will be as defined in the edit page.
   
   



-------

.. _no-6007:

.. function:: dabo.lib.datanav.Form.Form.initProperties(self)



-------

.. _no-6020:

.. function:: dabo.lib.datanav.Form.Form.onBrowseRecords(self, evt)

   Occurs when the user chooses to browse the record set.



-------

.. _no-6021:

.. function:: dabo.lib.datanav.Form.Form.onCancel(self, evt)



-------

.. _no-6022:

.. function:: dabo.lib.datanav.Form.Form.onConfigGrid(self, evt)



-------

.. _no-6023:

.. function:: dabo.lib.datanav.Form.Form.onDelete(self, evt)



-------

.. _no-6024:

.. function:: dabo.lib.datanav.Form.Form.onEditCurrentRecord(self, evt)

   Occurs when the user chooses to edit the current record.



-------

.. _no-6032:

.. function:: dabo.lib.datanav.Form.Form.onNew(self, evt)



-------

.. _no-6035:

.. function:: dabo.lib.datanav.Form.Form.onQuickReport(self, evt)



-------

.. _no-6036:

.. function:: dabo.lib.datanav.Form.Form.onRequery(self, evt)

   
   Override the dForm behavior by running the requery through the select page.
   



-------

.. _no-6038:

.. function:: dabo.lib.datanav.Form.Form.onSetSelectionCriteria(self, evt)

   Occurs when the user chooses to set the selection criteria.



-------

.. _no-6039:

.. function:: dabo.lib.datanav.Form.Form.onShowSQL(self, evt)



-------

.. _no-6041:

.. function:: dabo.lib.datanav.Form.Form.pickRecord(self)

   This form is a picklist, and the user chose a record in the grid.



-------

.. _no-6061:

.. function:: dabo.lib.datanav.Form.Form.requery(self, dataSource=None, _fromSelectPage=False)



-------

.. _no-6065:

.. function:: dabo.lib.datanav.Form.Form.save(self, dataSource=None)



-------

.. _no-6071:

.. function:: dabo.lib.datanav.Form.Form.setPrimaryBizobjToDefault(self, ds)

   
   This method is called when we leave an editing page. The
   intent is that if we move to another editing page, it will set the
   form's primary bizobj to the appropriate one for that page,
   so we don't need to do anything. But if they switch to the
   browse or select page, we want to set the primary bizobj back
   to the one for the form's main table.
   



-------

.. _no-6078:

.. function:: dabo.lib.datanav.Form.Form.setupMenu(self)

   
   Set up the action menu for this frame.
   
   Called when the form is created.
   



-------

.. _no-6079:

.. function:: dabo.lib.datanav.Form.Form.setupPageFrame(self)

   
   Set up the select/browse/edit/n pageframe.
   
   Default behavior is to set up a 3-page pageframe with 'Select',
   'Browse', and 'Edit' pages. User may override and/or extend in
   subclasses and overriding self.beforeSetupPageFrame(),
   self.setupPageFrame, and/or self.afterSetupPageFrame().
   



-------

.. _no-6080:

.. function:: dabo.lib.datanav.Form.Form.setupSaveCancelButtons(self)



-------

.. _no-6081:

.. function:: dabo.lib.datanav.Form.Form.setupToolBar(self)



-------


Methods - inherited
=====================

.. _no-5903:

.. function:: dabo.lib.datanav.Form.Form.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5904:

.. function:: dabo.lib.datanav.Form.Form.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5905:

.. function:: dabo.lib.datanav.Form.Form.addBizobj(self, bizobj)
   :noindex:


   
   Add a bizobj to this form.
   
   Make the bizobj the form's primary bizobj if it is the first bizobj to
   be added. For convenience, return the bizobj to the caller
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5908:

.. function:: dabo.lib.datanav.Form.Form.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-5909:

.. function:: dabo.lib.datanav.Form.Form.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5910:

.. function:: dabo.lib.datanav.Form.Form.afterCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5911:

.. function:: dabo.lib.datanav.Form.Form.afterDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5912:

.. function:: dabo.lib.datanav.Form.Form.afterDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5913:

.. function:: dabo.lib.datanav.Form.Form.afterFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5914:

.. function:: dabo.lib.datanav.Form.Form.afterFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5916:

.. function:: dabo.lib.datanav.Form.Form.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5917:

.. function:: dabo.lib.datanav.Form.Form.afterLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5918:

.. function:: dabo.lib.datanav.Form.Form.afterNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5919:

.. function:: dabo.lib.datanav.Form.Form.afterNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5920:

.. function:: dabo.lib.datanav.Form.Form.afterPointerMove(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   and the form has been updated.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5921:

.. function:: dabo.lib.datanav.Form.Form.afterPrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5922:

.. function:: dabo.lib.datanav.Form.Form.afterRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5923:

.. function:: dabo.lib.datanav.Form.Form.afterRowNavigation(self)
   :noindex:


   
   Called after the PrimaryBizobj's RowNumber has changed,
   but before the form updates.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5924:

.. function:: dabo.lib.datanav.Form.Form.afterSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5925:

.. function:: dabo.lib.datanav.Form.Form.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5926:

.. function:: dabo.lib.datanav.Form.Form.afterSetPrimaryBizobj(self)
   :noindex:


   Subclass hook.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5927:

.. function:: dabo.lib.datanav.Form.Form.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5929:

.. function:: dabo.lib.datanav.Form.Form.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5930:

.. function:: dabo.lib.datanav.Form.Form.autoBindEvents(self, force=True)
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

.. _no-5931:

.. function:: dabo.lib.datanav.Form.Form.beforeCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5932:

.. function:: dabo.lib.datanav.Form.Form.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5933:

.. function:: dabo.lib.datanav.Form.Form.beforeDelete(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5934:

.. function:: dabo.lib.datanav.Form.Form.beforeDeleteAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5935:

.. function:: dabo.lib.datanav.Form.Form.beforeFilter(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5936:

.. function:: dabo.lib.datanav.Form.Form.beforeFirst(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5937:

.. function:: dabo.lib.datanav.Form.Form.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5938:

.. function:: dabo.lib.datanav.Form.Form.beforeLast(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5939:

.. function:: dabo.lib.datanav.Form.Form.beforeNew(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5940:

.. function:: dabo.lib.datanav.Form.Form.beforeNext(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5941:

.. function:: dabo.lib.datanav.Form.Form.beforePointerMove(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5942:

.. function:: dabo.lib.datanav.Form.Form.beforePrior(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5943:

.. function:: dabo.lib.datanav.Form.Form.beforeRequery(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5944:

.. function:: dabo.lib.datanav.Form.Form.beforeSave(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5945:

.. function:: dabo.lib.datanav.Form.Form.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5947:

.. function:: dabo.lib.datanav.Form.Form.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5948:

.. function:: dabo.lib.datanav.Form.Form.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-5949:

.. function:: dabo.lib.datanav.Form.Form.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-5950:

.. function:: dabo.lib.datanav.Form.Form.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5952:

.. function:: dabo.lib.datanav.Form.Form.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5953:

.. function:: dabo.lib.datanav.Form.Form.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5954:

.. function:: dabo.lib.datanav.Form.Form.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5955:

.. function:: dabo.lib.datanav.Form.Form.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5956:

.. function:: dabo.lib.datanav.Form.Form.confirmChanges(self, bizobjs=None)
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

.. _no-5957:

.. function:: dabo.lib.datanav.Form.Form.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5958:

.. function:: dabo.lib.datanav.Form.Form.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5959:

.. function:: dabo.lib.datanav.Form.Form.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5960:

.. function:: dabo.lib.datanav.Form.Form.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5961:

.. function:: dabo.lib.datanav.Form.Form.delete(self, dataSource=None, message=None, prompt=True)
   :noindex:


   Ask the bizobj to delete the current record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5962:

.. function:: dabo.lib.datanav.Form.Form.deleteAll(self, dataSource=None, message=None)
   :noindex:


   Ask the primary bizobj to delete all records from the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5963:

.. function:: dabo.lib.datanav.Form.Form.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5964:

.. function:: dabo.lib.datanav.Form.Form.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5965:

.. function:: dabo.lib.datanav.Form.Form.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-5966:

.. function:: dabo.lib.datanav.Form.Form.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5967:

.. function:: dabo.lib.datanav.Form.Form.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5968:

.. function:: dabo.lib.datanav.Form.Form.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5969:

.. function:: dabo.lib.datanav.Form.Form.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5970:

.. function:: dabo.lib.datanav.Form.Form.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5971:

.. function:: dabo.lib.datanav.Form.Form.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5972:

.. function:: dabo.lib.datanav.Form.Form.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5973:

.. function:: dabo.lib.datanav.Form.Form.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5974:

.. function:: dabo.lib.datanav.Form.Form.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5976:

.. function:: dabo.lib.datanav.Form.Form.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5977:

.. function:: dabo.lib.datanav.Form.Form.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5978:

.. function:: dabo.lib.datanav.Form.Form.filter(self, dataSource=None, fld=None, expr=None, op='=')
   :noindex:


   Apply a filter to the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5979:

.. function:: dabo.lib.datanav.Form.Form.first(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the first record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5980:

.. function:: dabo.lib.datanav.Form.Form.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5981:

.. function:: dabo.lib.datanav.Form.Form.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5982:

.. function:: dabo.lib.datanav.Form.Form.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5983:

.. function:: dabo.lib.datanav.Form.Form.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-5984:

.. function:: dabo.lib.datanav.Form.Form.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5985:

.. function:: dabo.lib.datanav.Form.Form.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5986:

.. function:: dabo.lib.datanav.Form.Form.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-5989:

.. function:: dabo.lib.datanav.Form.Form.getBizobj(self, dataSource=None, parentBizobj=None)
   :noindex:


   
   Return the bizobj with the passed dataSource. If no
   dataSource is passed, getBizobj() will return the primary bizobj.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5991:

.. function:: dabo.lib.datanav.Form.Form.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5992:

.. function:: dabo.lib.datanav.Form.Form.getConfirmChangesQueryMessage(self, changedBizList)
   :noindex:


   
   Return the "Save Changes?" message for use in the query dialog.
   
   The default is to return "Do you wish to save your changes?". Subclasses
   can override with whatever message they want, possibly iterating the
   changed bizobj list to introspect the exact changes made to construct the
   message.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5993:

.. function:: dabo.lib.datanav.Form.Form.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5994:

.. function:: dabo.lib.datanav.Form.Form.getCurrentRecordText(self, dataSource=None, grid=None)
   :noindex:


   Get the text to describe which record is current.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-5995:

.. function:: dabo.lib.datanav.Form.Form.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5997:

.. function:: dabo.lib.datanav.Form.Form.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-5998:

.. function:: dabo.lib.datanav.Form.Form.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-5999:

.. function:: dabo.lib.datanav.Form.Form.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6000:

.. function:: dabo.lib.datanav.Form.Form.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-6002:

.. function:: dabo.lib.datanav.Form.Form.getSQL(self, dataSource=None)
   :noindex:


   Get the current SQL from the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6003:

.. function:: dabo.lib.datanav.Form.Form.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6004:

.. function:: dabo.lib.datanav.Form.Form.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6005:

.. function:: dabo.lib.datanav.Form.Form.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6006:

.. function:: dabo.lib.datanav.Form.Form.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6008:

.. function:: dabo.lib.datanav.Form.Form.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6009:

.. function:: dabo.lib.datanav.Form.Form.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6010:

.. function:: dabo.lib.datanav.Form.Form.last(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the last record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6011:

.. function:: dabo.lib.datanav.Form.Form.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6012:

.. function:: dabo.lib.datanav.Form.Form.lockDisplay(self)
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

.. _no-6013:

.. function:: dabo.lib.datanav.Form.Form.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6014:

.. function:: dabo.lib.datanav.Form.Form.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6015:

.. function:: dabo.lib.datanav.Form.Form.moveToRowNumber(self, rowNumber, dataSource=None)
   :noindex:


   Move the record pointer to the specified row.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6016:

.. function:: dabo.lib.datanav.Form.Form.new(self, dataSource=None)
   :noindex:


   Ask the bizobj to add a new record to the recordset.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6017:

.. function:: dabo.lib.datanav.Form.Form.next(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the next record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6018:

.. function:: dabo.lib.datanav.Form.Form.notifyUser(self, msg, title=None, severe=False, exception=None)
   :noindex:


   
   Displays an alert messagebox for the user. You can customize
   this in your own classes if you prefer a different display.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6019:

.. function:: dabo.lib.datanav.Form.Form.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6025:

.. function:: dabo.lib.datanav.Form.Form.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6026:

.. function:: dabo.lib.datanav.Form.Form.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6027:

.. function:: dabo.lib.datanav.Form.Form.onFieldValidationFailed(self, ctrl, ds, df, val, err)
   :noindex:


   
   Basic handling of field-level validation failure. You should
   override it with your own code to handle this failure
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6028:

.. function:: dabo.lib.datanav.Form.Form.onFieldValidationPassed(self, ctrl, ds, df, val)
   :noindex:


   
   Basic handling when field-level validation succeeds.
   You should override it with your own code to handle this event
   appropriately for your application.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6029:

.. function:: dabo.lib.datanav.Form.Form.onFirst(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6030:

.. function:: dabo.lib.datanav.Form.Form.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6031:

.. function:: dabo.lib.datanav.Form.Form.onLast(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6033:

.. function:: dabo.lib.datanav.Form.Form.onNext(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6034:

.. function:: dabo.lib.datanav.Form.Form.onPrior(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6037:

.. function:: dabo.lib.datanav.Form.Form.onSave(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6040:

.. function:: dabo.lib.datanav.Form.Form.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6042:

.. function:: dabo.lib.datanav.Form.Form.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6043:

.. function:: dabo.lib.datanav.Form.Form.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6044:

.. function:: dabo.lib.datanav.Form.Form.prior(self, dataSource=None)
   :noindex:


   Ask the bizobj to move to the previous record.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6045:

.. function:: dabo.lib.datanav.Form.Form.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6046:

.. function:: dabo.lib.datanav.Form.Form.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6047:

.. function:: dabo.lib.datanav.Form.Form.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6048:

.. function:: dabo.lib.datanav.Form.Form.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6049:

.. function:: dabo.lib.datanav.Form.Form.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-6050:

.. function:: dabo.lib.datanav.Form.Form.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6051:

.. function:: dabo.lib.datanav.Form.Form.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6052:

.. function:: dabo.lib.datanav.Form.Form.refresh(self, interval=None)
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

.. _no-6053:

.. function:: dabo.lib.datanav.Form.Form.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6054:

.. function:: dabo.lib.datanav.Form.Form.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6055:

.. function:: dabo.lib.datanav.Form.Form.release(self)
   :noindex:


   
   Instead of just destroying the object, make sure that
   we close it properly and clean up any references to it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6056:

.. function:: dabo.lib.datanav.Form.Form.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6057:

.. function:: dabo.lib.datanav.Form.Form.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6058:

.. function:: dabo.lib.datanav.Form.Form.removeFilter(self, dataSource=None)
   :noindex:


   Remove the most recently applied filter from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6059:

.. function:: dabo.lib.datanav.Form.Form.removeFilters(self, dataSource=None)
   :noindex:


   Remove all filters from the bizobj's data.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6060:

.. function:: dabo.lib.datanav.Form.Form.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6062:

.. function:: dabo.lib.datanav.Form.Form.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6063:

.. function:: dabo.lib.datanav.Form.Form.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6064:

.. function:: dabo.lib.datanav.Form.Form.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6066:

.. function:: dabo.lib.datanav.Form.Form.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6067:

.. function:: dabo.lib.datanav.Form.Form.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6068:

.. function:: dabo.lib.datanav.Form.Form.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-6069:

.. function:: dabo.lib.datanav.Form.Form.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6070:

.. function:: dabo.lib.datanav.Form.Form.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6072:

.. function:: dabo.lib.datanav.Form.Form.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-6073:

.. function:: dabo.lib.datanav.Form.Form.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-6074:

.. function:: dabo.lib.datanav.Form.Form.setSQL(self, sql, dataSource=None)
   :noindex:


   Set the SQL for the bizobj.


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------

.. _no-6075:

.. function:: dabo.lib.datanav.Form.Form.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6076:

.. function:: dabo.lib.datanav.Form.Form.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6077:

.. function:: dabo.lib.datanav.Form.Form.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6082:

.. function:: dabo.lib.datanav.Form.Form.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6083:

.. function:: dabo.lib.datanav.Form.Form.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6084:

.. function:: dabo.lib.datanav.Form.Form.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6085:

.. function:: dabo.lib.datanav.Form.Form.showModal(self)
   :noindex:


   
   Shows the form in a modal fashion. Other forms can still be
   activated, but all controls are disabled.
   
   .. note::
       wxPython does not currently support this. DO NOT USE this method.
   
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-6086:

.. function:: dabo.lib.datanav.Form.Form.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-6087:

.. function:: dabo.lib.datanav.Form.Form.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-6088:

.. function:: dabo.lib.datanav.Form.Form.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6089:

.. function:: dabo.lib.datanav.Form.Form.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6090:

.. function:: dabo.lib.datanav.Form.Form.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-6091:

.. function:: dabo.lib.datanav.Form.Form.update(self, interval=None)
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

.. _no-6092:

.. function:: dabo.lib.datanav.Form.Form.validateField(self, ctrl)
   :noindex:


   
   Call the bizobj for the control's DataSource. If the control's
   value is rejected for field validation reasons, a
   BusinessRuleViolation exception will be raised, and the form
   can then respond to this.
   


Inherited from: :ref:`dabo.ui.uiwx.dForm.BaseForm`

-------


|
