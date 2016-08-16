
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrameMixin

.. _dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin:

========================================================
|doc_title|  **dPageFrameMixin.dPageFrameMixin** - class
========================================================

Creates a container for an unlimited number of pages.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPageFrameMixin**

.. inheritance-diagram:: dPageFrameMixin


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.ui.uiwx.dPageFrame.dDockTabs`
* :ref:`dabo.ui.uiwx.dPageFrame.dPageFrame`
* :ref:`dabo.ui.uiwx.dPageFrame.dPageList`
* :ref:`dabo.ui.uiwx.dPageFrame.dPageSelect`
* :ref:`dabo.ui.uiwx.dPageFrame.dPageStyled`
* :ref:`dabo.ui.uiwx.dPageFrame.dPageToolBar`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin

   .. automethod:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.__init__

|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Application <no-16657>`                Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-16658>`                  Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-16659>`                  The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-16660>`                Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-16661>`                Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-16662>`            Style of line for the border drawn around the control.
:ref:`BorderStyle <no-16663>`                Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-16664>`                Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-16665>`                     The position of the bottom side of the object. This is a
:ref:`Caption <no-16666>`                    The caption of the object. (str)
:ref:`Children <no-16667>`                   Returns a list of object references to the children of
:ref:`Class <no-16668>`                      The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-16669>`           Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-16670>`       Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-16671>`         Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-16672>`         Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-16673>`           Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-16674>`         Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-16675>`     Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-16676>`         Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-16677>`         Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-16678>`             Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-16679>`             Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-16680>`                Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-16681>`            Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-16682>`            Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-16683>`          Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-16684>`            Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-16685>`       Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-16686>`           Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-16687>`              Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-16688>`                Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-16689>`        Dynamically determine the value of the MousePointer property.
:ref:`DynamicPageClass <no-16690>`           Dynamically determine the value of the PageClass property.
:ref:`DynamicPageCount <no-16691>`           Dynamically determine the value of the PageCount property.
:ref:`DynamicPosition <no-16692>`            Dynamically determine the value of the Position property.
:ref:`DynamicSelectedPage <no-16693>`        Dynamically determine the value of the SelectedPage property.
:ref:`DynamicSelectedPageNumber <no-16694>`  Dynamically determine the value of the SelectedPageNumber property.
:ref:`DynamicSize <no-16695>`                Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-16696>`          Dynamically determine the value of the StatusText property.
:ref:`DynamicTabPosition <no-16697>`         Dynamically determine the value of the TabPosition property.
:ref:`DynamicTag <no-16698>`                 Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-16699>`         Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-16700>`                 Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-16701>`        Dynamically determine the value of the Transparency property.
:ref:`DynamicUpdateInactivePages <no-16702>` Dynamically determine the value of the UpdateInactivePages property.
:ref:`DynamicVisible <no-16703>`             Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-16704>`               Dynamically determine the value of the Width property.
:ref:`Enabled <no-16705>`                    Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-16706>`                       Specifies font object for this control. (dFont)
:ref:`FontBold <no-16707>`                   Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-16708>`            Human-readable description of the current font settings. (str)
:ref:`FontFace <no-16709>`                   Specifies the font face. (str)
:ref:`FontInfo <no-16710>`                   Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-16711>`                 Specifies whether font is italicized. (bool)
:ref:`FontSize <no-16712>`                   Specifies the point size of the font. (int)
:ref:`FontUnderline <no-16713>`              Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-16714>`                  Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-16715>`                       Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-16716>`                     Specifies the height of the object. (int)
:ref:`HelpContextText <no-16717>`            Specifies the context-sensitive help text associated with this
:ref:`Hover <no-16718>`                      When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-16719>`                       Specifies the left position of the object. (int)
:ref:`LogEvents <no-16720>`                  Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-16721>`              Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-16722>`                Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-16723>`               Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-16724>`              Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-16725>`                Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-16726>`               Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-16727>`               Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-16728>`                       Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-16729>`                   Specifies the base name of the object.
:ref:`PageClass <no-16730>`                  Specifies the class of control to use for pages by default. (classRef)
:ref:`PageCount <no-16731>`                  Specifies the number of pages in the pageframe. (int)
:ref:`PageSizerClass <no-16732>`             Default sizer class for pages added automatically to this control. Set
:ref:`Pages <no-16733>`                      Returns a list of the contained pages.  (list)
:ref:`Parent <no-16734>`                     The containing object. (obj)
:ref:`Position <no-16735>`                   The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-16736>`          Reference to the Preference Management object  (dPref)
:ref:`RegID <no-16737>`                      A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-16738>`                      The position of the right side of the object. This is a
:ref:`SelectedPage <no-16739>`               References the current frontmost page.  (dPage)
:ref:`SelectedPageNumber <no-16740>`         Returns the index of the current frontmost page.  (int)
:ref:`Size <no-16741>`                       The size of the object. (tuple)
:ref:`Sizer <no-16742>`                      The sizer for the object.
:ref:`StatusText <no-16743>`                 Specifies the text that displays in the form's status bar, if any.
:ref:`TabPosition <no-16744>`                Specifies where the page tabs are located. (int)
:ref:`TabStop <no-16745>`                    Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-16746>`                        A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-16747>`                Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-16748>`                        The top position of the object. (int)
:ref:`Transparency <no-16749>`               Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-16750>`          Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateInactivePages <no-16751>`        Determines if the inactive pages are updated too. (bool)
:ref:`UseSmartFocus <no-16752>`              Determines if focus has to be restored to the last active
:ref:`Visible <no-16753>`                    Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-16754>`            Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-16755>`                      The width of the object. (int)
:ref:`WindowHandle <no-16756>`               The platform-specific handle for the window. Read-only. (long)

============================================ ========================


Properties
==========

.. _no-16690:

**DynamicPageClass** 

Dynamically determine the value of the PageClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageClass property. If DynamicPageClass is set to None (the default), PageClass
will not be dynamically evaluated.



-------

.. _no-16691:

**DynamicPageCount** 

Dynamically determine the value of the PageCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageCount property. If DynamicPageCount is set to None (the default), PageCount
will not be dynamically evaluated.



-------

.. _no-16693:

**DynamicSelectedPage** 

Dynamically determine the value of the SelectedPage property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPage property. If DynamicSelectedPage is set to None (the default), SelectedPage
will not be dynamically evaluated.



-------

.. _no-16694:

**DynamicSelectedPageNumber** 

Dynamically determine the value of the SelectedPageNumber property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPageNumber property. If DynamicSelectedPageNumber is set to None (the default), SelectedPageNumber
will not be dynamically evaluated.



-------

.. _no-16697:

**DynamicTabPosition** 

Dynamically determine the value of the TabPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabPosition property. If DynamicTabPosition is set to None (the default), TabPosition
will not be dynamically evaluated.



-------

.. _no-16702:

**DynamicUpdateInactivePages** 

Dynamically determine the value of the UpdateInactivePages property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UpdateInactivePages property. If DynamicUpdateInactivePages is set to None (the default), UpdateInactivePages
will not be dynamically evaluated.



-------

.. _no-16730:

**PageClass** 

Specifies the class of control to use for pages by default. (classRef)
    This really only applies when using the PageCount property to set the
    number of pages. If you instead use AddPage() you still need to send
    an instance as usual. Class must descend from a dabo base class.



-------

.. _no-16731:

**PageCount** 

Specifies the number of pages in the pageframe. (int)
    When using this to increase the number of pages, PageClass
    will be queried as the object to use as the page object.



-------

.. _no-16732:

**PageSizerClass** 

Default sizer class for pages added automatically to this control. Set
    this to None to prevent sizers from being automatically added to child
    pages. (dSizer or None)



-------

.. _no-16733:

**Pages** 

Returns a list of the contained pages.  (list)



-------

.. _no-16739:

**SelectedPage** 

References the current frontmost page.  (dPage)



-------

.. _no-16740:

**SelectedPageNumber** 

Returns the index of the current frontmost page.  (int)



-------

.. _no-16744:

**TabPosition** 

Specifies where the page tabs are located. (int)
        Top (default)
        Left
        Right
        Bottom



-------

.. _no-16751:

**UpdateInactivePages** 

Determines if the inactive pages are updated too. (bool)
    Setting it to False can significantly improve update performance
    of multipage forms. Default=True.



-------

.. _no-16752:

**UseSmartFocus** 

Determines if focus has to be restored to the last active
    control on page when it become selected. (bool) Default=False.
    



-------


Properties - inherited
========================

.. _no-16657:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16658:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16659:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16660:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16661:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16662:

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

.. _no-16663:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16664:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16665:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16666:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16667:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16668:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16669:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16670:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16671:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16672:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16673:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16674:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16675:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16676:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16677:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16678:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16679:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16680:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16681:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16682:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16683:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16684:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16685:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16686:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16687:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16688:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16689:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16692:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16695:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16696:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16698:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16699:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16700:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16701:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16703:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16704:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16705:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16706:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16707:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16708:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16709:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16710:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16711:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16712:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16713:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16714:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16715:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16716:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16717:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16718:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16719:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16720:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16721:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16722:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16723:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16724:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16725:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16726:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16727:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16728:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16729:

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

.. _no-16734:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16735:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16736:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16737:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16738:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16741:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16742:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16743:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16745:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-16746:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16747:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16748:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16749:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16750:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16753:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16754:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16755:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16756:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-16757>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-16758>`                 Occurs after the control or form is created.
:ref:`Destroy <no-16759>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-16760>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-16761>`               Occurs when the control gets the focus.
:ref:`Idle <no-16762>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-16763>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-16764>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-16765>`               
:ref:`KeyUp <no-16766>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-16767>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-16768>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-16769>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-16770>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-16771>`             
:ref:`MouseLeave <no-16772>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-16773>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-16774>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-16775>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-16776>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-16777>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-16778>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-16779>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-16780>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-16781>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-16782>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-16783>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-16784>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-16785>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-16786>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-16787>`                   Occurs when the control's position changes.
:ref:`Paint <no-16788>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-16789>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-16790>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-16791>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-16792>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-16757:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-16758:

**Create** 

Occurs after the control or form is created.



-------

.. _no-16759:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-16760:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-16761:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-16762:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-16763:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-16764:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-16765:

**KeyEvent** 



-------

.. _no-16766:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-16767:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-16768:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-16769:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-16770:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-16771:

**MouseEvent** 



-------

.. _no-16772:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-16773:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-16774:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-16775:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-16776:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-16777:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-16778:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-16779:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-16780:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-16781:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-16782:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-16783:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-16784:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-16785:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-16786:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-16787:

**Move** 

Occurs when the control's position changes.



-------

.. _no-16788:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-16789:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-16790:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-16791:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-16792:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-16793>`   Translates a position value for a control to absolute screen position.
:ref:`addImage <no-16794>`              Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-16795>`             Instantiate object as a child of self.
:ref:`afterInit <no-16796>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-16797>`          
:ref:`afterSetProperties <no-16798>`    
:ref:`appendPage <no-16799>`            Appends the page to the pageframe, and optionally sets
:ref:`autoBindEvents <no-16800>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-16801>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforePageChange <no-16802>`      Return False from this method to prevent the page from changing.
:ref:`beforeSetProperties <no-16803>`   
:ref:`bindEvent <no-16804>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-16805>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-16806>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-16807>`          Makes this object topmost
:ref:`clear <no-16808>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-16809>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-16810>`  Given a position relative to this control, return a position relative
:ref:`copy <no-16811>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-16812>`                   Called by uiApp when the user requests a cut operation.
:ref:`cyclePages <no-16813>`            Moves through the pages by the specified amount, wrapping
:ref:`drawArc <no-16814>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-16815>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-16816>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-16817>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-16818>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-16819>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-16820>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-16821>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-16822>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-16823>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-16824>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-16825>`              Draws text on the object at the specified position
:ref:`endHover <no-16826>`              
:ref:`fitToSizer <no-16827>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-16828>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-16829>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-16830>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-16831>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-16832>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-16833>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-16834>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-16835>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-16836>`      Returns the current mouse position on the entire screen
:ref:`getPageImage <no-16837>`          Returns the index of the specified page's image in the
:ref:`getPositionInSizer <no-16838>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-16839>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-16840>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-16841>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-16842>`                  Make the object invisible.
:ref:`initEvents <no-16843>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-16844>`        Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-16845>`            Insert the page into the pageframe at the specified position,
:ref:`isContainedBy <no-16846>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-16847>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-16848>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-16849>`           Locks the visual updates to the control.
:ref:`movePage <no-16850>`              Moves the specified 'old' page to the new position and
:ref:`moveTabOrderAfter <no-16851>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-16852>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-16853>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-16854>`               
:ref:`paste <no-16855>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-16856>`           
:ref:`processDroppedFiles <no-16857>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-16858>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-16859>`            Raise the passed Dabo event.
:ref:`reCreate <no-16860>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-16861>`              Recreate the object.
:ref:`redraw <no-16862>`                Called when the object is (re)drawn.
:ref:`refresh <no-16863>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-16864>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-16865>`               Destroys the object.
:ref:`removeDrawnObject <no-16866>`     
:ref:`removePage <no-16867>`            Removes the specified page. You can specify a page by either
:ref:`sendToBack <no-16868>`            Places this object behind all others.
:ref:`setAll <no-16869>`                Set all child object properties to the passed value.
:ref:`setFocus <no-16870>`              Sets focus to the object.
:ref:`setPageImage <no-16871>`          Sets the specified page's image to the image corresponding
:ref:`setPositionInSizer <no-16872>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-16873>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-16874>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-16875>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-16876>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-16877>`                  Make the object visible.
:ref:`showContainingPage <no-16878>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-16879>`       Display a context menu (popup) at the specified position.
:ref:`super <no-16880>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-16881>`           Remove a previously registered event binding.
:ref:`unbindKey <no-16882>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-16883>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-16884>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-16885>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-16794:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.addImage(self, img, key=None)

   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   



-------

.. _no-16799:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.appendPage(self, pgCls=None, caption='', imgKey=None, \**kwargs)

   
   Appends the page to the pageframe, and optionally sets
   the page caption and image. The image should have already
   been added to the pageframe if it is going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   



-------

.. _no-16802:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.beforePageChange(self, fromPage, toPage)

   Return False from this method to prevent the page from changing.



-------

.. _no-16813:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.cyclePages(self, num)

   
   Moves through the pages by the specified amount, wrapping
   around the ends. Negative values move to previous pages; positive
   move through the next pages.
   



-------

.. _no-16837:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getPageImage(self, pg)

   
   Returns the index of the specified page's image in the
   current image list, or -1 if no image is set for the page.
   



-------

.. _no-16845:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.insertPage(self, pos, pgCls=None, caption='', imgKey=None, ignoreOverride=False, \**kwargs)

   
   Insert the page into the pageframe at the specified position,
   and optionally sets the page caption and image. The image
   should have already been added to the pageframe if it is
   going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   



-------

.. _no-16848:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.layout(self)

   Wrap the wx version of the call, if possible.



-------

.. _no-16850:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.movePage(self, oldPgOrPos, newPos, selecting=True)

   
   Moves the specified 'old' page to the new position and
   optionally selects it. If an invalid page number is passed,
   it returns False without changing anything.
   



-------

.. _no-16867:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.removePage(self, pgOrPos, delPage=True)

   
   Removes the specified page. You can specify a page by either
   passing the page itself, or a position. If delPage is True (default),
   the page is released, and None is returned. If delPage is
   False, the page is returned.
   



-------

.. _no-16871:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setPageImage(self, pg, imgKey)

   
   Sets the specified page's image to the image corresponding
   to the specified key. May also optionally pass the index of the
   image in the ImageList rather than the key.
   



-------


Methods - inherited
=====================

.. _no-16793:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16795:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-16796:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16797:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16798:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16800:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.autoBindEvents(self, force=True)
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

.. _no-16801:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16803:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16804:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16805:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16806:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-16807:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16808:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16809:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16810:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16811:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16812:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16814:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16815:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16816:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-16817:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16818:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16819:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16820:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16821:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16822:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16823:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16824:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16825:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16826:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16827:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16828:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16829:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16830:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16831:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16832:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16833:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16834:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16835:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16836:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16838:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16839:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-16840:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16841:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16842:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16843:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16844:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16846:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16847:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16849:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.lockDisplay(self)
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

.. _no-16851:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16852:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16853:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16854:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16855:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16856:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16857:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16858:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16859:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16860:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16861:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16862:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16863:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16864:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16865:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16866:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16868:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16869:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-16870:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16872:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16873:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-16874:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-16875:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16876:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16877:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16878:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16879:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16880:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16881:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16882:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16883:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16884:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16885:

.. function:: dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
