
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dEditableList

.. _dabo.ui.uiwx.dEditableList.dEditableList:

====================================================
|doc_title|  **dEditableList.dEditableList** - class
====================================================


Creates an editable list box, complete with buttons to control
editing, adding/deleting items, and re-ordering them.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dEditableList**

.. inheritance-diagram:: dEditableList


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.gizmos.EditableListBox - can not provide a link



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



     - .. image:: _static/winWidgets/dEditableList.png
          :scale: 75 %
          :target: _static/winWidgets/dEditableList.png
          :alt: dEditableList



     - .. image:: _static/nixWidgets/dEditableList.png
          :scale: 75 %
          :target: _static/nixWidgets/dEditableList.png
          :alt: dEditableList


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dEditableList.dEditableList

   .. automethod:: dabo.ui.uiwx.dEditableList.dEditableList.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-35678>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-35679>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-35680>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-35681>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-35682>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-35683>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-35684>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-35685>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-35686>`                 The position of the bottom side of the object. This is a
:ref:`CanAdd <no-35687>`                 Determines if the user can add new entries to the list  (bool)
:ref:`CanDelete <no-35688>`              Determines if the user can delete entries from the list  (bool)
:ref:`CanOrder <no-35689>`               Determines if the user can re-order items  (bool)
:ref:`Caption <no-35690>`                Text that appears in the top panel of the control  (str)
:ref:`Children <no-35691>`               Returns a list of object references to the children of
:ref:`Choices <no-35692>`                List that contains the entries in the control  (list)
:ref:`Class <no-35693>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-35694>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-35695>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-35696>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-35697>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-35698>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-35699>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-35700>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-35701>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-35702>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCanAdd <no-35703>`          Dynamically determine the value of the CanAdd property.
:ref:`DynamicCanDelete <no-35704>`       Dynamically determine the value of the CanDelete property.
:ref:`DynamicCanOrder <no-35705>`        Dynamically determine the value of the CanOrder property.
:ref:`DynamicCaption <no-35706>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEditable <no-35707>`        Dynamically determine the value of the Editable property.
:ref:`DynamicEnabled <no-35708>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-35709>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-35710>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-35711>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-35712>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-35713>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-35714>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-35715>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-35716>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-35717>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-35718>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-35719>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-35720>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-35721>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-35722>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-35723>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-35724>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-35725>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-35726>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-35727>`           Dynamically determine the value of the Width property.
:ref:`Editable <no-35728>`               Determines if the user can change existing entries  (bool)
:ref:`Enabled <no-35729>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-35730>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-35731>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-35732>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-35733>`               Specifies the font face. (str)
:ref:`FontInfo <no-35734>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-35735>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-35736>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-35737>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-35738>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-35739>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-35740>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-35741>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-35742>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-35743>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-35744>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-35745>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-35746>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-35747>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-35748>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-35749>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-35750>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-35751>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-35752>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-35753>`               Specifies the base name of the object.
:ref:`Parent <no-35754>`                 The containing object. (obj)
:ref:`Position <no-35755>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-35756>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-35757>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-35758>`                  The position of the right side of the object. This is a
:ref:`Size <no-35759>`                   The size of the object. (tuple)
:ref:`Sizer <no-35760>`                  The sizer for the object.
:ref:`StatusText <no-35761>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-35762>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-35763>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-35764>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-35765>`                    The top position of the object. (int)
:ref:`Transparency <no-35766>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-35767>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-35768>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-35769>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-35770>`                  The width of the object. (int)
:ref:`WindowHandle <no-35771>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-35687:

**CanAdd** 

Determines if the user can add new entries to the list  (bool)



-------

.. _no-35688:

**CanDelete** 

Determines if the user can delete entries from the list  (bool)



-------

.. _no-35689:

**CanOrder** 

Determines if the user can re-order items  (bool)



-------

.. _no-35692:

**Choices** 

List that contains the entries in the control  (list)



-------

.. _no-35703:

**DynamicCanAdd** 

Dynamically determine the value of the CanAdd property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CanAdd property. If DynamicCanAdd is set to None (the default), CanAdd
will not be dynamically evaluated.



-------

.. _no-35704:

**DynamicCanDelete** 

Dynamically determine the value of the CanDelete property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CanDelete property. If DynamicCanDelete is set to None (the default), CanDelete
will not be dynamically evaluated.



-------

.. _no-35705:

**DynamicCanOrder** 

Dynamically determine the value of the CanOrder property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CanOrder property. If DynamicCanOrder is set to None (the default), CanOrder
will not be dynamically evaluated.



-------

.. _no-35707:

**DynamicEditable** 

Dynamically determine the value of the Editable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Editable property. If DynamicEditable is set to None (the default), Editable
will not be dynamically evaluated.



-------

.. _no-35728:

**Editable** 

Determines if the user can change existing entries  (bool)



-------


Properties - inherited
========================

.. _no-35678:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35679:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35680:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35681:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35682:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35683:

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

.. _no-35684:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35685:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35686:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35690:

**Caption** 

Text that appears in the top panel of the control  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35691:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35693:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35694:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35695:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35696:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35697:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35698:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35699:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35700:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35701:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35702:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35706:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35708:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35709:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35710:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35711:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35712:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35713:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35714:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35715:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35716:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35717:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35718:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35719:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35720:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35721:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35722:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35723:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35724:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35725:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35726:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35727:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35729:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35730:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35731:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35732:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35733:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35734:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35735:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35736:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35737:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35738:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35739:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35740:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35741:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35742:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35743:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35744:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35745:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35746:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35747:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35748:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35749:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35750:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35751:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35752:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35753:

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

.. _no-35754:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35755:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35756:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35757:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35758:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35759:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35760:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-35761:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35762:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-35763:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35764:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35765:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35766:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35767:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35768:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35769:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35770:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35771:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-35772>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-35773>`                 Occurs after the control or form is created.
:ref:`Destroy <no-35774>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-35775>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-35776>`               Occurs when the control gets the focus.
:ref:`Idle <no-35777>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-35778>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-35779>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-35780>`               
:ref:`KeyUp <no-35781>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-35782>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-35783>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-35784>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-35785>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-35786>`             
:ref:`MouseLeave <no-35787>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-35788>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-35789>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-35790>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-35791>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-35792>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-35793>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-35794>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-35795>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-35796>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-35797>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-35798>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-35799>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-35800>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-35801>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-35802>`                   Occurs when the control's position changes.
:ref:`Paint <no-35803>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-35804>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-35805>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-35806>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-35807>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-35772:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-35773:

**Create** 

Occurs after the control or form is created.



-------

.. _no-35774:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-35775:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-35776:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-35777:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-35778:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-35779:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-35780:

**KeyEvent** 



-------

.. _no-35781:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-35782:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-35783:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-35784:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-35785:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-35786:

**MouseEvent** 



-------

.. _no-35787:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-35788:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-35789:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-35790:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-35791:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-35792:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-35793:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-35794:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-35795:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-35796:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-35797:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-35798:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-35799:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-35800:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-35801:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-35802:

**Move** 

Occurs when the control's position changes.



-------

.. _no-35803:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-35804:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-35805:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-35806:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-35807:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-35808>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-35809>`             Instantiate object as a child of self.
:ref:`afterInit <no-35810>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-35811>`          
:ref:`afterSetProperties <no-35812>`    
:ref:`autoBindEvents <no-35813>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-35814>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-35815>`   
:ref:`bindEvent <no-35816>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-35817>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-35818>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-35819>`          Makes this object topmost
:ref:`clear <no-35820>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-35821>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-35822>`  Given a position relative to this control, return a position relative
:ref:`copy <no-35823>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-35824>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-35825>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-35826>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-35827>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-35828>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-35829>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-35830>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-35831>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-35832>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-35833>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-35834>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-35835>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-35836>`              Draws text on the object at the specified position
:ref:`endHover <no-35837>`              
:ref:`fitToSizer <no-35838>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-35839>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-35840>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-35841>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-35842>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-35843>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-35844>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-35845>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-35846>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-35847>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-35848>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-35849>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-35850>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-35851>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-35852>`                  Make the object invisible.
:ref:`initEvents <no-35853>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-35854>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-35855>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-35856>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-35857>`                Calling the native Layout() method isn't sufficient, as it doesn't seem
:ref:`lockDisplay <no-35858>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-35859>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-35860>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-35861>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-35862>`               
:ref:`paste <no-35863>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-35864>`           
:ref:`processDroppedFiles <no-35865>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-35866>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-35867>`            Raise the passed Dabo event.
:ref:`reCreate <no-35868>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-35869>`              Recreate the object.
:ref:`redraw <no-35870>`                Called when the object is (re)drawn.
:ref:`refresh <no-35871>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-35872>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-35873>`               Destroys the object.
:ref:`removeDrawnObject <no-35874>`     
:ref:`sendToBack <no-35875>`            Places this object behind all others.
:ref:`setAll <no-35876>`                Set all child object properties to the passed value.
:ref:`setFocus <no-35877>`              Sets focus to the object.
:ref:`setPositionInSizer <no-35878>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-35879>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-35880>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-35881>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-35882>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-35883>`                  Make the object visible.
:ref:`showContainingPage <no-35884>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-35885>`       Display a context menu (popup) at the specified position.
:ref:`super <no-35886>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-35887>`           Remove a previously registered event binding.
:ref:`unbindKey <no-35888>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-35889>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-35890>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-35891>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-35857:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.layout(self)

   
   Calling the native Layout() method isn't sufficient, as it doesn't seem
   to call the top panel's Layout(). So we'll do it manually.
   



-------


Methods - inherited
=====================

.. _no-35808:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35809:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-35810:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35811:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35812:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35813:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.autoBindEvents(self, force=True)
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

.. _no-35814:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35815:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35816:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35817:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35818:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-35819:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35820:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35821:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35822:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35823:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35824:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35825:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35826:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35827:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-35828:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35829:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35830:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35831:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35832:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35833:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35834:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35835:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35836:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35837:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35838:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35839:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35840:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35841:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35842:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35843:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35844:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35845:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35846:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35847:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35848:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35849:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-35850:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35851:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35852:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35853:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35854:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35855:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35856:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35858:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.lockDisplay(self)
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

.. _no-35859:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35860:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35861:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35862:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35863:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35864:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35865:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35866:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35867:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35868:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-35869:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35870:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35871:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35872:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35873:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35874:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35875:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35876:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-35877:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35878:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35879:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-35880:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-35881:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35882:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35883:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35884:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35885:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35886:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-35887:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-35888:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35889:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35890:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-35891:

.. function:: dabo.ui.uiwx.dEditableList.dEditableList.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
