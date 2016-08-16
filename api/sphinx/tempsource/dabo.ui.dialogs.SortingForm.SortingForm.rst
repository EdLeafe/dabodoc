
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.SortingForm

.. _dabo.ui.dialogs.SortingForm.SortingForm:

================================================
|doc_title|  **SortingForm.SortingForm** - class
================================================

This class affords a simple way to order a list of items.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SortingForm**

.. inheritance-diagram:: SortingForm


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



   * - no image available



     - .. image:: _static/winWidgets/SortingForm.png
          :scale: 75 %
          :target: _static/winWidgets/SortingForm.png
          :alt: SortingForm



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.SortingForm.SortingForm

   .. automethod:: dabo.ui.dialogs.SortingForm.SortingForm.__init__

|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Accepted <no-9659>`                    Specifies whether the user accepted the dialog, or canceled.  (bool)
:ref:`ActiveControl <no-9660>`               Contains a reference to the active control on the form, or None.
:ref:`Application <no-9661>`                 Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoSize <no-9662>`                    When True, the dialog resizes to fit the added controls.  (bool)
:ref:`AutoUpdateStatusText <no-9663>`        Does this form update the status text with the current record position?  (bool)
:ref:`BackColor <no-9664>`                   Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-9665>`                   The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-9666>`                 Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-9667>`                 Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-9668>`             Style of line for the border drawn around the control.
:ref:`BorderResizable <no-9669>`             Specifies whether the user can resize this form.  (bool).
:ref:`BorderStyle <no-9670>`                 Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-9671>`                 Width of the border drawn around the control, if any. (int)
:ref:`Borderless <no-9672>`                  Must be passed at construction time. When set to True, the dialog displays
:ref:`Bottom <no-9673>`                      The position of the bottom side of the object. This is a
:ref:`ButtonSizer <no-9674>`                 Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)
:ref:`ButtonSizerPosition <no-9675>`         Returns the position of the Ok/Cancel buttons in the sizer.  (int)
:ref:`CancelButton <no-9676>`                Reference to the Cancel button on the form, if present  (dButton or None).
:ref:`CancelOnEscape <no-9677>`              When True (default), pressing the Escape key will perform the same action
:ref:`Caption <no-9678>`                     The text that appears in the dialog's title bar  (str)
:ref:`Centered <no-9679>`                    Determines if the dialog is displayed centered on the screen.  (bool)
:ref:`Children <no-9680>`                    Returns a list of object references to the children of
:ref:`Choices <no-9681>`                     Items in the list to sort.   (list)
:ref:`Class <no-9682>`                       The class the object is based on. Read-only.  (class)
:ref:`Connection <no-9683>`                  The connection to the database used by this form  (dConnection)
:ref:`ControllingSizer <no-9684>`            Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-9685>`        Reference to the sizer item that control's this control's layout.
:ref:`CxnName <no-9686>`                     Name of the connection used for data access  (str)
:ref:`DroppedFileHandler <no-9687>`          Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-9688>`          Reference to the object that will handle text dropped on this control.
:ref:`DynamicAutoSize <no-9689>`             Dynamically determine the value of the AutoSize property.
:ref:`DynamicAutoUpdateStatusText <no-9690>` Dynamically determine the value of the AutoUpdateStatusText property.
:ref:`DynamicBackColor <no-9691>`            Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-9692>`          Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-9693>`      Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderResizable <no-9694>`      Dynamically determine the value of the BorderResizable property.
:ref:`DynamicBorderStyle <no-9695>`          Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-9696>`          Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-9697>`              Dynamically determine the value of the Caption property.
:ref:`DynamicCentered <no-9698>`             Dynamically determine the value of the Centered property.
:ref:`DynamicConnection <no-9699>`           Dynamically determine the value of the Connection property.
:ref:`DynamicEnabled <no-9700>`              Dynamically determine the value of the Enabled property.
:ref:`DynamicFloatOnParent <no-9701>`        Dynamically determine the value of the FloatOnParent property.
:ref:`DynamicFont <no-9702>`                 Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-9703>`             Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-9704>`             Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-9705>`           Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-9706>`             Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-9707>`        Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-9708>`            Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-9709>`               Dynamically determine the value of the Height property.
:ref:`DynamicIcon <no-9710>`                 Dynamically determine the value of the Icon property.
:ref:`DynamicLeft <no-9711>`                 Dynamically determine the value of the Left property.
:ref:`DynamicMenuBar <no-9712>`              Dynamically determine the value of the MenuBar property.
:ref:`DynamicMousePointer <no-9713>`         Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-9714>`             Dynamically determine the value of the Position property.
:ref:`DynamicShowCaption <no-9715>`          Dynamically determine the value of the ShowCaption property.
:ref:`DynamicShowStatusBar <no-9716>`        Dynamically determine the value of the ShowStatusBar property.
:ref:`DynamicSize <no-9717>`                 Dynamically determine the value of the Size property.
:ref:`DynamicStatusBar <no-9718>`            Dynamically determine the value of the StatusBar property.
:ref:`DynamicStatusText <no-9719>`           Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-9720>`                  Dynamically determine the value of the Tag property.
:ref:`DynamicToolBar <no-9721>`              Dynamically determine the value of the ToolBar property.
:ref:`DynamicToolTipText <no-9722>`          Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-9723>`                  Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-9724>`         Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-9725>`              Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-9726>`                Dynamically determine the value of the Width property.
:ref:`DynamicWindowState <no-9727>`          Dynamically determine the value of the WindowState property.
:ref:`Enabled <no-9728>`                     Specifies whether the object and children can get user input. (bool)
:ref:`FloatOnParent <no-9729>`               Specifies whether the form stays on top of the parent or not.
:ref:`FloatingPanel <no-9730>`               Small modal dialog that is designed to be used for temporary displays,
:ref:`Font <no-9731>`                        Specifies font object for this control. (dFont)
:ref:`FontBold <no-9732>`                    Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-9733>`             Human-readable description of the current font settings. (str)
:ref:`FontFace <no-9734>`                    Specifies the font face. (str)
:ref:`FontInfo <no-9735>`                    Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-9736>`                  Specifies whether font is italicized. (bool)
:ref:`FontSize <no-9737>`                    Specifies the point size of the font. (int)
:ref:`FontUnderline <no-9738>`               Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-9739>`                   Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-9740>`                        Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-9741>`                      Specifies the height of the object. (int)
:ref:`HelpButton <no-9742>`                  Reference to the Help button on the form, if present  (dButton or None).
:ref:`HelpContextText <no-9743>`             Specifies the context-sensitive help text associated with this
:ref:`Hover <no-9744>`                       When True, Mouse Enter events fire the onHover method, and
:ref:`Icon <no-9745>`                        Specifies the icon for the form.
:ref:`IdleRefreshInterval <no-9746>`         Controls how often the form is refreshed when idle.
:ref:`Left <no-9747>`                        Specifies the left position of the object. (int)
:ref:`ListCaption <no-9748>`                 Caption for the sorting list  (str)
:ref:`LogEvents <no-9749>`                   Specifies which events to log.  (list of strings)
:ref:`MDI <no-9750>`                         Returns True if this is a MDI (Multiple Document Interface) form.  (bool)
:ref:`MaximumHeight <no-9751>`               Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-9752>`                 Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-9753>`                Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBar <no-9754>`                     Specifies the menu bar instance for the form.
:ref:`MenuBarClass <no-9755>`                Specifies the menu bar class to use for the form, or None.
:ref:`MenuBarFile <no-9756>`                 Path to the .mnxml file that defines this form's menu bar  (str)
:ref:`MinimumHeight <no-9757>`               Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-9758>`                 Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-9759>`                Minimum allowable width for the control in pixels.  (int)
:ref:`Modal <no-9760>`                       Determines if the dialog is shown modal (default) or modeless.  (bool)
:ref:`MousePointer <no-9761>`                Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-9762>`                        Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-9763>`                    Specifies the base name of the object.
:ref:`NoButton <no-9764>`                    Reference to the No button on the form, if present  (dButton or None).
:ref:`OKButton <no-9765>`                    Reference to the OK button on the form, if present  (dButton or None).
:ref:`Parent <no-9766>`                      The containing object. (obj)
:ref:`Position <no-9767>`                    The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-9768>`           Reference to the Preference Management object  (dPref)
:ref:`RegID <no-9769>`                       A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-9770>`                       The position of the right side of the object. This is a
:ref:`SaveRestorePosition <no-9771>`         Specifies whether the form's position and size as set by the user
:ref:`ShowCaption <no-9772>`                 Specifies whether the caption is displayed in the title bar. (bool).
:ref:`ShowCloseButton <no-9773>`             Specifies whether a close button is displayed in the title bar. (bool).
:ref:`ShowInTaskBar <no-9774>`               Specifies whether the form is shown in the taskbar.  (bool).
:ref:`ShowMaxButton <no-9775>`               Specifies whether a maximize button is displayed in the title bar. (bool).
:ref:`ShowMenuBar <no-9776>`                 Specifies whether a menubar is created and shown automatically.
:ref:`ShowMinButton <no-9777>`               Specifies whether a minimize button is displayed in the title bar. (bool).
:ref:`ShowStatusBar <no-9778>`               Specifies whether the status bar gets automatically created.
:ref:`ShowSystemMenu <no-9779>`              Specifies whether a system menu is displayed in the title bar. (bool).
:ref:`ShowToolBar <no-9780>`                 Specifies whether the Tool bar gets automatically created.
:ref:`Size <no-9781>`                        The size of the object. (tuple)
:ref:`Sizer <no-9782>`                       The sizer for the object.
:ref:`SizersToOutline <no-9783>`             When drawing the outline of sizers, the sizer(s) to draw.
:ref:`StatusBar <no-9784>`                   Status bar for this form. (dStatusBar)
:ref:`StatusBarClass <no-9785>`              Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)
:ref:`StatusText <no-9786>`                  Text displayed in the form's status bar. (string)
:ref:`StayOnTop <no-9787>`                   Keeps the form on top of all other forms. (bool)
:ref:`Tag <no-9788>`                         A property that user code can safely use for specific purposes.
:ref:`TempForm <no-9789>`                    Used to indicate that this is a temporary form, and that its settings
:ref:`TinyTitleBar <no-9790>`                Specifies whether the title bar is small, like a tool window. (bool).
:ref:`ToolBar <no-9791>`                     Tool bar for this form. (dToolBar)
:ref:`ToolTipText <no-9792>`                 Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-9793>`                         The top position of the object. (int)
:ref:`Transparency <no-9794>`                Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-9795>`           Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-9796>`                     Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-9797>`             Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-9798>`                       The width of the object. (int)
:ref:`WindowHandle <no-9799>`                The platform-specific handle for the window. Read-only. (long)
:ref:`WindowState <no-9800>`                 Specifies the current state of the form. (int)
:ref:`YesButton <no-9801>`                   Reference to the Yes button on the form, if present  (dButton or None).

============================================ ========================


Properties
==========

.. _no-9681:

**Choices** 

Items in the list to sort.   (list)



-------

.. _no-9748:

**ListCaption** 

Caption for the sorting list  (str)



-------


Properties - inherited
========================

.. _no-9659:

**Accepted** 

Specifies whether the user accepted the dialog, or canceled.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9660:

**ActiveControl** 

Contains a reference to the active control on the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9661:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9662:

**AutoSize** 

When True, the dialog resizes to fit the added controls.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9663:

**AutoUpdateStatusText** 

Does this form update the status text with the current record position?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9664:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9665:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9666:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9667:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9668:

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

.. _no-9669:

**BorderResizable** 

Specifies whether the user can resize this form.  (bool).

    The default is True for dForm and False for dDialog.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9670:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9671:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9672:

**Borderless** 

Must be passed at construction time. When set to True, the dialog displays
    without a title bar or borders  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9673:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9674:

**ButtonSizer** 

Returns a reference to the sizer controlling the Ok/Cancel buttons.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9675:

**ButtonSizerPosition** 

Returns the position of the Ok/Cancel buttons in the sizer.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9676:

**CancelButton** 

Reference to the Cancel button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9677:

**CancelOnEscape** 

When True (default), pressing the Escape key will perform the same action
    as clicking the Cancel button. If no Cancel button is present but there is a No button,
    the No behavior will be executed. If neither button is present, the default button's
    action will be executed  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9678:

**Caption** 

The text that appears in the dialog's title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9679:

**Centered** 

Determines if the dialog is displayed centered on the screen.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9680:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9682:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9683:

**Connection** 

The connection to the database used by this form  (dConnection)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9684:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9685:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9686:

**CxnName** 

Name of the connection used for data access  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9687:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9688:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9689:

**DynamicAutoSize** 

Dynamically determine the value of the AutoSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoSize property. If DynamicAutoSize is set to None (the default), AutoSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9690:

**DynamicAutoUpdateStatusText** 

Dynamically determine the value of the AutoUpdateStatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
AutoUpdateStatusText property. If DynamicAutoUpdateStatusText is set to None (the default), AutoUpdateStatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9691:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9692:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9693:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9694:

**DynamicBorderResizable** 

Dynamically determine the value of the BorderResizable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderResizable property. If DynamicBorderResizable is set to None (the default), BorderResizable
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9695:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9696:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9697:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9698:

**DynamicCentered** 

Dynamically determine the value of the Centered property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Centered property. If DynamicCentered is set to None (the default), Centered
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9699:

**DynamicConnection** 

Dynamically determine the value of the Connection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Connection property. If DynamicConnection is set to None (the default), Connection
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9700:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9701:

**DynamicFloatOnParent** 

Dynamically determine the value of the FloatOnParent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FloatOnParent property. If DynamicFloatOnParent is set to None (the default), FloatOnParent
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9702:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9703:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9704:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9705:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9706:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9707:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9708:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9709:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9710:

**DynamicIcon** 

Dynamically determine the value of the Icon property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Icon property. If DynamicIcon is set to None (the default), Icon
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9711:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9712:

**DynamicMenuBar** 

Dynamically determine the value of the MenuBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MenuBar property. If DynamicMenuBar is set to None (the default), MenuBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9713:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9714:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9715:

**DynamicShowCaption** 

Dynamically determine the value of the ShowCaption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaption property. If DynamicShowCaption is set to None (the default), ShowCaption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9716:

**DynamicShowStatusBar** 

Dynamically determine the value of the ShowStatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowStatusBar property. If DynamicShowStatusBar is set to None (the default), ShowStatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9717:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9718:

**DynamicStatusBar** 

Dynamically determine the value of the StatusBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusBar property. If DynamicStatusBar is set to None (the default), StatusBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9719:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9720:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9721:

**DynamicToolBar** 

Dynamically determine the value of the ToolBar property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolBar property. If DynamicToolBar is set to None (the default), ToolBar
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9722:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9723:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9724:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9725:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9726:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9727:

**DynamicWindowState** 

Dynamically determine the value of the WindowState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WindowState property. If DynamicWindowState is set to None (the default), WindowState
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9728:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9729:

**FloatOnParent** 

Specifies whether the form stays on top of the parent or not.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9730:

**FloatingPanel** 

Small modal dialog that is designed to be used for temporary displays,
    similar to context menus, but which can contain any controls.
    (read-only) (dDialog)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9731:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9732:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9733:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9734:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9735:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9736:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9737:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9738:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9739:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9740:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9741:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9742:

**HelpButton** 

Reference to the Help button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9743:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9744:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9745:

**Icon** 

Specifies the icon for the form.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.


Inherited from: 'wx._windows.TopLevelWindow - can not provide a link

-------

.. _no-9746:

**IdleRefreshInterval** 

Controls how often the form is refreshed when idle.

    If you notice a lot of flicker when a form is 'doing nothing', increase
    this value. Likewise, if you notice that changes are not reflected as
    readily as you wish, decrease it. The value is in milliseconds; the
    default is 1000.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9747:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9749:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9750:

**MDI** 

Returns True if this is a MDI (Multiple Document Interface) form.  (bool)

    Otherwise, returns False if this is a SDI (Single Document Interface) form.
    Users on Microsoft Windows seem to expect MDI, while on other platforms SDI is
    preferred.

    See also: the dabo.MDI global setting.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9751:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9752:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9753:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9754:

**MenuBar** 

Specifies the menu bar instance for the form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9755:

**MenuBarClass** 

Specifies the menu bar class to use for the form, or None.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9756:

**MenuBarFile** 

Path to the .mnxml file that defines this form's menu bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9757:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9758:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9759:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9760:

**Modal** 

Determines if the dialog is shown modal (default) or modeless.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9761:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9762:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9763:

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

.. _no-9764:

**NoButton** 

Reference to the No button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9765:

**OKButton** 

Reference to the OK button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9766:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9767:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9768:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9769:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9770:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9771:

**SaveRestorePosition** 

Specifies whether the form's position and size as set by the user
        will get saved and restored in the next session. Default is True for
        forms and False for dialogs.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9772:

**ShowCaption** 

Specifies whether the caption is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9773:

**ShowCloseButton** 

Specifies whether a close button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9774:

**ShowInTaskBar** 

Specifies whether the form is shown in the taskbar.  (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9775:

**ShowMaxButton** 

Specifies whether a maximize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9776:

**ShowMenuBar** 

Specifies whether a menubar is created and shown automatically.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9777:

**ShowMinButton** 

Specifies whether a minimize button is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9778:

**ShowStatusBar** 

Specifies whether the status bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9779:

**ShowSystemMenu** 

Specifies whether a system menu is displayed in the title bar. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9780:

**ShowToolBar** 

Specifies whether the Tool bar gets automatically created.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9781:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9782:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-9783:

**SizersToOutline** 

When drawing the outline of sizers, the sizer(s) to draw.
    Default=self.Sizer  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9784:

**StatusBar** 

Status bar for this form. (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9785:

**StatusBarClass** 

Class to be used for this form's status bar. Default=dStatusBar (dStatusBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9786:

**StatusText** 

Text displayed in the form's status bar. (string)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9787:

**StayOnTop** 

Keeps the form on top of all other forms. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9788:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9789:

**TempForm** 

Used to indicate that this is a temporary form, and that its settings
    should not be persisted. Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9790:

**TinyTitleBar** 

Specifies whether the title bar is small, like a tool window. (bool).


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9791:

**ToolBar** 

Tool bar for this form. (dToolBar)


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9792:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9793:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9794:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9795:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9796:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9797:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9798:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9799:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9800:

**WindowState** 

Specifies the current state of the form. (int)

            Normal
            Minimized
            Maximized
            FullScreen


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9801:

**YesButton** 

Reference to the Yes button on the form, if present  (dButton or None).


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`Activate <no-9802>`               Occurs when the form or application becomes active.
:ref:`BackgroundErased <no-9803>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-9804>`              Occurs when a child control is created.
:ref:`Close <no-9805>`                  Occurs when the user closes the form.
:ref:`Create <no-9806>`                 Occurs after the control or form is created.
:ref:`Deactivate <no-9807>`             Occurs when another form becomes active.
:ref:`Destroy <no-9808>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-9809>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-9810>`               Occurs when the control gets the focus.
:ref:`Idle <no-9811>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-9812>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-9813>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-9814>`               
:ref:`KeyUp <no-9815>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-9816>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-9817>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-9818>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-9819>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-9820>`             
:ref:`MouseLeave <no-9821>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-9822>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-9823>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-9824>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-9825>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-9826>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-9827>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-9828>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-9829>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-9830>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-9831>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-9832>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-9833>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-9834>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-9835>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-9836>`                   Occurs when the control's position changes.
:ref:`Paint <no-9837>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-9838>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-9839>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-9840>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-9841>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-9802:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-9803:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-9804:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-9805:

**Close** 

Occurs when the user closes the form.



-------

.. _no-9806:

**Create** 

Occurs after the control or form is created.



-------

.. _no-9807:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-9808:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-9809:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-9810:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-9811:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-9812:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-9813:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-9814:

**KeyEvent** 



-------

.. _no-9815:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-9816:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-9817:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-9818:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-9819:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-9820:

**MouseEvent** 



-------

.. _no-9821:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-9822:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-9823:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-9824:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-9825:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-9826:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-9827:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-9828:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-9829:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-9830:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-9831:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-9832:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-9833:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-9834:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-9835:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-9836:

**Move** 

Occurs when the control's position changes.



-------

.. _no-9837:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-9838:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-9839:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-9840:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-9841:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-9842>`            Translates a position value for a control to absolute screen position.
:ref:`activeControlValid <no-9843>`             Force the control-with-focus to fire its KillFocus code.
:ref:`addControlSequence <no-9844>`             This takes a sequence of 3-tuples or 3-lists, and adds controls
:ref:`addControls <no-9845>`                    
:ref:`addObject <no-9846>`                      Instantiate object as a child of self.
:ref:`addToOutlinedSizers <no-9847>`            
:ref:`afterAddControls <no-9848>`               This is a hook, called at the appropriate time by the framework.
:ref:`afterInit <no-9849>`                      Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-9850>`                   
:ref:`afterSetMenuBar <no-9851>`                Subclasses can extend the menu bar here.
:ref:`afterSetProperties <no-9852>`             
:ref:`appendToolBarButton <no-9853>`            
:ref:`autoBindEvents <no-9854>`                 Automatically bind any on*() methods to the associated event.
:ref:`beforeAddControls <no-9855>`              This is a hook, called at the appropriate time by the framework.
:ref:`beforeClose <no-9856>`                    Hook method. Returning False will prevent the form from
:ref:`beforeInit <no-9857>`                     Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-9858>`            
:ref:`bindEvent <no-9859>`                      Bind a dEvent to a callback function.
:ref:`bindEvents <no-9860>`                     Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-9861>`                        Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-9862>`                   Makes this object topmost
:ref:`clear <no-9863>`                          Clears the background of custom-drawn objects.
:ref:`clone <no-9864>`                          Create another object just like the passed object. It assumes that the
:ref:`close <no-9865>`                          This method will close the form. If force = False (default)
:ref:`closing <no-9866>`                        Stub method to be customized in subclasses. At this point,
:ref:`containerCoordinates <no-9867>`           Given a position relative to this control, return a position relative
:ref:`copy <no-9868>`                           Called by uiApp when the user requests a copy operation.
:ref:`createBizobjs <no-9869>`                  Can be overridden in instances to create the bizobjs this form needs.
:ref:`cut <no-9870>`                            Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-9871>`                        Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-9872>`                     Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-9873>`                     Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-9874>`                    Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-9875>`                Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-9876>`                   Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-9877>`                       Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-9878>`                  Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-9879>`                    Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-9880>`                  Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-9881>`           Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-9882>`                       Draws text on the object at the specified position
:ref:`endHover <no-9883>`                       
:ref:`fillPreferenceDialog <no-9884>`           This method is called with a reference to the pref dialog. It can be overridden
:ref:`fitToSizer <no-9885>`                     Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-9886>`                     Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-9887>`                 Reset the font zoom back to zero.
:ref:`fontZoomOut <no-9888>`                    Zoom out on the font, by setting a lower point size.
:ref:`forceSizerOutline <no-9889>`              
:ref:`formCoordinates <no-9890>`                Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-9891>`                Return the fully qualified name of the object.
:ref:`getBizobj <no-9892>`                      
:ref:`getCaptureBitmap <no-9893>`               Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-9894>`              Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-9895>`               Returns an object that locks the current display when created, and
:ref:`getMenu <no-9896>`                        Get the navigation menu for this form.
:ref:`getMousePosition <no-9897>`               Returns the current mouse position on the entire screen
:ref:`getObjectByRegID <no-9898>`               Given a RegID value, this will return a reference to the
:ref:`getPositionInSizer <no-9899>`             Convenience method to let you call this directly on the object.
:ref:`getProperties <no-9900>`                  Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-9901>`                   Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-9902>`                  Returns a dict containing the object's sizer property info. The
:ref:`hide <no-9903>`                           Make the object invisible.
:ref:`initEvents <no-9904>`                     Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-9905>`                 Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-9906>`                  Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-9907>`                    Call the given function on this object and all of its Children. If
:ref:`layout <no-9908>`                         Wrap the wx sizer layout call.
:ref:`lockDisplay <no-9909>`                    Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-9910>`              Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-9911>`             Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-9912>`              Given a position relative to the form, return a position relative
:ref:`onEditRedo <no-9913>`                     If you want your form to respond to the Redo menu item in
:ref:`onEditUndo <no-9914>`                     If you want your form to respond to the Undo menu item in
:ref:`onHover <no-9915>`                        
:ref:`paste <no-9916>`                          Called by uiApp when the user requests a paste operation.
:ref:`popStatusText <no-9917>`                  Restores the StatusText to the last value pushed on the stack. If there
:ref:`posIsWithin <no-9918>`                    
:ref:`processDroppedFiles <no-9919>`            Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-9920>`             Handler for text dropped on the control. Override in your
:ref:`pushStatusText <no-9921>`                 Stores the current text of the StatusBar on a LIFO stack for later retrieval.
:ref:`raiseEvent <no-9922>`                     Raise the passed Dabo event.
:ref:`reCreate <no-9923>`                       Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-9924>`                       Recreate the object.
:ref:`redraw <no-9925>`                         Called when the object is (re)drawn.
:ref:`refresh <no-9926>`                        Repaints the form and all contained objects.
:ref:`registerObject <no-9927>`                 Stores a reference to the passed object using the RegID key
:ref:`relativeCoordinates <no-9928>`            Translates an absolute screen position to position value for a control.
:ref:`release <no-9929>`                        Need to augment this to make sure the dialog
:ref:`reload <no-9930>`                         Tells the application to check for a newer version of the form, and if there is,
:ref:`removeDrawnObject <no-9931>`              
:ref:`removeFromOutlinedSizers <no-9932>`       
:ref:`restoreSizeAndPosition <no-9933>`         Restore the saved window geometry for this form.
:ref:`restoreSizeAndPositionIfNeeded <no-9934>` 
:ref:`runCancel <no-9935>`                      
:ref:`runHelp <no-9936>`                        
:ref:`runNo <no-9937>`                          
:ref:`runOK <no-9938>`                          
:ref:`runYes <no-9939>`                         
:ref:`safeDestroy <no-9940>`                    Since the callAfter to close() was added, I'm getting a lot
:ref:`saveSizeAndPosition <no-9941>`            Save the current size and position of this form.
:ref:`sendToBack <no-9942>`                     Places this object behind all others.
:ref:`setAll <no-9943>`                         Set all child object properties to the passed value.
:ref:`setEscapeButton <no-9944>`                Set which button gets hit when Esc pressed.
:ref:`setFocus <no-9945>`                       Sets focus to the object.
:ref:`setPositionInSizer <no-9946>`             Convenience method to let you call this directly on the object.
:ref:`setProperties <no-9947>`                  Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-9948>`          Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-9949>`                   Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-9950>`                  Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-9951>`                  Set the status text to val.
:ref:`show <no-9952>`                           
:ref:`showContainingPage <no-9953>`             If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-9954>`                Display a context menu (popup) at the specified position.
:ref:`showModal <no-9955>`                      Show the dialog modally.
:ref:`showModeless <no-9956>`                   Show the dialog non-modally.
:ref:`super <no-9957>`                          This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-9958>`                    Remove a previously registered event binding.
:ref:`unbindKey <no-9959>`                      Unbind a previously bound key combination.
:ref:`unlockDisplay <no-9960>`                  Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-9961>`               Immediately unlocks the display, no matter how many previous
:ref:`update <no-9962>`                         Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-9845:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.addControls(self)



-------


Methods - inherited
=====================

.. _no-9842:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9843:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.activeControlValid(self)
   :noindex:


   
   Force the control-with-focus to fire its KillFocus code.
   
   The bizobj will only get its field updated during the control's
   KillFocus code. This function effectively commands that update to
   happen before it would have otherwise occurred.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9844:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.addControlSequence(self, seq)
   :noindex:


   
   This takes a sequence of 3-tuples or 3-lists, and adds controls
   to the dialog as a grid of labels and data controls. The first element of
   the list/tuple is the prompt, the second is the data type, and the third
   is the RegID used to retrieve the entered value.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9846:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-9847:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.addToOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9848:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.afterAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9849:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9850:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9851:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.afterSetMenuBar(self)
   :noindex:


   Subclasses can extend the menu bar here.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9852:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9853:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.appendToolBarButton(self, name, pic, toggle=False, tip='', help='', \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9854:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.autoBindEvents(self, force=True)
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

.. _no-9855:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.beforeAddControls(self)
   :noindex:


   This is a hook, called at the appropriate time by the framework.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9856:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.beforeClose(self, evt)
   :noindex:


   
   Hook method. Returning False will prevent the form from
   closing. Gives you a chance to determine the status of the form
   to see if changes need to be saved, etc.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9857:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9858:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9859:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9860:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9861:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-9862:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9863:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9864:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9865:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.close(self, force=False)
   :noindex:


   
   This method will close the form. If force = False (default)
   the beforeClose methods will be called, and these will have
   an opportunity to conditionally block the form from closing.
   If force=True, the form is closed without any chance of
   preventing it.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9866:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.closing(self)
   :noindex:


   
   Stub method to be customized in subclasses. At this point,
   the form is going to close. If you need to do something that might
   prevent the form from closing, code it in the beforeClose()
   method instead.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9867:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9868:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9869:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.createBizobjs(self)
   :noindex:


   
   Can be overridden in instances to create the bizobjs this form needs.
   It is provided so that tools such as the Class Designer can create skeleton
   code that the user can later enhance.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9870:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9871:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9872:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9873:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-9874:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9875:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9876:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9877:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9878:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9879:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9880:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9881:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9882:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9883:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9884:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.fillPreferenceDialog(self, dlg)
   :noindex:


   
   This method is called with a reference to the pref dialog. It can be overridden
   in subclasses to add application-specific content to the pref dialog. To add a
   new page to the dialog, call the dialog's addCategory() method, passing the caption
   for that page. It will return a reference to the newly-created page, to which you
   then add your controls.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9885:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9886:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9887:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9888:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9889:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.forceSizerOutline(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9890:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9891:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9892:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getBizobj(self, \*args, \**kwargs)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9893:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9894:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9895:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9896:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getMenu(self)
   :noindex:


   
   Get the navigation menu for this form.
   
   Every form maintains an internal menu of actions appropriate to itself.
   For instance, a dForm with a primary bizobj will maintain a menu with
   'requery', 'save', 'next', etc. choices.
   
   This function sets up the internal menu, which can optionally be
   inserted into the mainForm's menu bar during SetFocus.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9897:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9898:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getObjectByRegID(self, id)
   :noindex:


   
   Given a RegID value, this will return a reference to the
   associated object, if any. If not, returns None.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9899:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9900:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-9901:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9902:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9903:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9904:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9905:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9906:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9907:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9908:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.layout(self)
   :noindex:


   Wrap the wx sizer layout call.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9909:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.lockDisplay(self)
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

.. _no-9910:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9911:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9912:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9913:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.onEditRedo(self, evt)
   :noindex:


   
   If you want your form to respond to the Redo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9914:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.onEditUndo(self, evt)
   :noindex:


   
   If you want your form to respond to the Undo menu item in
   the Edit menu that is installed in the Dabo base menu, override
   this method, and either return nothing, or return something other
   than False.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9915:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9916:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9917:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.popStatusText(self)
   :noindex:


   
   Restores the StatusText to the last value pushed on the stack. If there
   are no values in the stack, nothing is changed.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9918:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9919:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9920:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9921:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.pushStatusText(self, txt, duration=None)
   :noindex:


   Stores the current text of the StatusBar on a LIFO stack for later retrieval.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9922:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9923:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-9924:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9925:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9926:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.refresh(self, interval=None)
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

.. _no-9927:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.registerObject(self, obj)
   :noindex:


   
   Stores a reference to the passed object using the RegID key
   property of the object for later retrieval. You may reference the
   object as if it were a child object of this form; i.e., by using simple
   dot notation, with the RegID as the 'name' of the object.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9928:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9929:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.release(self)
   :noindex:


   
   Need to augment this to make sure the dialog
   is removed from the app's forms collection.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9930:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.reload(self)
   :noindex:


   
   Tells the application to check for a newer version of the form, and if there is,
   to replace this instance with an instance of the newer class.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9931:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9932:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.removeFromOutlinedSizers(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9933:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.restoreSizeAndPosition(self)
   :noindex:


   
   Restore the saved window geometry for this form.
   
   Ask dApp for the last saved setting of height, width, left, and top,
   and set those properties on this form.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9934:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.restoreSizeAndPositionIfNeeded(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9935:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.runCancel(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9936:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.runHelp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9937:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.runNo(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9938:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.runOK(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9939:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.runYes(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9940:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.safeDestroy(self)
   :noindex:


   
   Since the callAfter to close() was added, I'm getting a lot
   of dead object warnings. This should fix that.
   


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9941:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.saveSizeAndPosition(self)
   :noindex:


   Save the current size and position of this form.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9942:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9943:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-9944:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setEscapeButton(self, btn=None)
   :noindex:


   
   Set which button gets hit when Esc pressed.
   
   CancelOnEscape must be True for this to work.
   


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dStandardButtonDialog`

-------

.. _no-9945:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9946:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9947:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-9948:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-9949:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9950:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9951:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.setStatusText(self, val, immediate=False)
   :noindex:


   Set the status text to val.


Inherited from: :ref:`dabo.ui.uiwx.dFormMixin.dFormMixin`

-------

.. _no-9952:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.show(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9953:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9954:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9955:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.showModal(self)
   :noindex:


   Show the dialog modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9956:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.showModeless(self)
   :noindex:


   Show the dialog non-modally.


Inherited from: :ref:`dabo.ui.uiwx.dDialog.dDialog`

-------

.. _no-9957:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-9958:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-9959:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9960:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9961:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-9962:

.. function:: dabo.ui.dialogs.SortingForm.SortingForm.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
