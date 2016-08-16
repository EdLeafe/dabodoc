
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrame

.. _dabo.ui.uiwx.dPageFrame.dDockTabs:

=============================================
|doc_title|  **dPageFrame.dDockTabs** - class
=============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDockTabs**

.. inheritance-diagram:: dDockTabs


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`
* wx.lib.agw.aui.auibook.AuiNotebook - can not provide a link



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



   * - .. image:: _static/macWidgets/dDockTabs.png
          :scale: 75 %
          :target: _static/macWidgets/dDockTabs.png
          :alt: dDockTabs



     - .. image:: _static/winWidgets/dDockTabs.png
          :scale: 75 %
          :target: _static/winWidgets/dDockTabs.png
          :alt: dDockTabs



     - .. image:: _static/nixWidgets/dDockTabs.png
          :scale: 75 %
          :target: _static/nixWidgets/dDockTabs.png
          :alt: dDockTabs


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrame.dDockTabs

   .. automethod:: dabo.ui.uiwx.dPageFrame.dDockTabs.__init__

|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Application <no-16886>`                Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-16887>`                  Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-16888>`                  The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-16889>`                Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-16890>`                Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-16891>`            Style of line for the border drawn around the control.
:ref:`BorderStyle <no-16892>`                Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-16893>`                Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-16894>`                     The position of the bottom side of the object. This is a
:ref:`Caption <no-16895>`                    The caption of the object. (str)
:ref:`Children <no-16896>`                   Returns a list of object references to the children of
:ref:`Class <no-16897>`                      The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-16898>`           Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-16899>`       Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-16900>`         Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-16901>`         Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-16902>`           Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-16903>`         Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-16904>`     Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-16905>`         Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-16906>`         Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-16907>`             Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-16908>`             Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-16909>`                Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-16910>`            Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-16911>`            Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-16912>`          Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-16913>`            Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-16914>`       Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-16915>`           Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-16916>`              Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-16917>`                Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-16918>`        Dynamically determine the value of the MousePointer property.
:ref:`DynamicPageClass <no-16919>`           Dynamically determine the value of the PageClass property.
:ref:`DynamicPageCount <no-16920>`           Dynamically determine the value of the PageCount property.
:ref:`DynamicPosition <no-16921>`            Dynamically determine the value of the Position property.
:ref:`DynamicSelectedPage <no-16922>`        Dynamically determine the value of the SelectedPage property.
:ref:`DynamicSelectedPageNumber <no-16923>`  Dynamically determine the value of the SelectedPageNumber property.
:ref:`DynamicSize <no-16924>`                Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-16925>`          Dynamically determine the value of the StatusText property.
:ref:`DynamicTabPosition <no-16926>`         Dynamically determine the value of the TabPosition property.
:ref:`DynamicTag <no-16927>`                 Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-16928>`         Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-16929>`                 Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-16930>`        Dynamically determine the value of the Transparency property.
:ref:`DynamicUpdateInactivePages <no-16931>` Dynamically determine the value of the UpdateInactivePages property.
:ref:`DynamicVisible <no-16932>`             Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-16933>`               Dynamically determine the value of the Width property.
:ref:`Enabled <no-16934>`                    Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-16935>`                       Specifies font object for this control. (dFont)
:ref:`FontBold <no-16936>`                   Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-16937>`            Human-readable description of the current font settings. (str)
:ref:`FontFace <no-16938>`                   Specifies the font face. (str)
:ref:`FontInfo <no-16939>`                   Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-16940>`                 Specifies whether font is italicized. (bool)
:ref:`FontSize <no-16941>`                   Specifies the point size of the font. (int)
:ref:`FontUnderline <no-16942>`              Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-16943>`                  Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-16944>`                       Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-16945>`                     Specifies the height of the object. (int)
:ref:`HelpContextText <no-16946>`            Specifies the context-sensitive help text associated with this
:ref:`Hover <no-16947>`                      When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-16948>`                       Specifies the left position of the object. (int)
:ref:`LogEvents <no-16949>`                  Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-16950>`              Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-16951>`                Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-16952>`               Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-16953>`              Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-16954>`                Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-16955>`               Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-16956>`               Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`MovableTabs <no-16957>`                When True (default), tabs can be re-arranged by dragging, and docked at
:ref:`Name <no-16958>`                       Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-16959>`                   Specifies the base name of the object.
:ref:`PageClass <no-16960>`                  Specifies the class of control to use for pages by default. (classRef)
:ref:`PageCount <no-16961>`                  Specifies the number of pages in the pageframe. (int)
:ref:`PageSizerClass <no-16962>`             Default sizer class for pages added automatically to this control. Set
:ref:`Pages <no-16963>`                      Returns a list of the contained pages.  (list)
:ref:`Parent <no-16964>`                     The containing object. (obj)
:ref:`Position <no-16965>`                   The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-16966>`          Reference to the Preference Management object  (dPref)
:ref:`RegID <no-16967>`                      A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-16968>`                      The position of the right side of the object. This is a
:ref:`SelectedPage <no-16969>`               References the current frontmost page.  (dPage)
:ref:`SelectedPageNumber <no-16970>`         Returns the index of the current frontmost page.  (int)
:ref:`Size <no-16971>`                       The size of the object. (tuple)
:ref:`Sizer <no-16972>`                      The sizer for the object.
:ref:`StatusText <no-16973>`                 Specifies the text that displays in the form's status bar, if any.
:ref:`TabPosition <no-16974>`                Specifies where the page tabs are located. (int)
:ref:`TabStop <no-16975>`                    Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-16976>`                        A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-16977>`                Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-16978>`                        The top position of the object. (int)
:ref:`Transparency <no-16979>`               Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-16980>`          Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateInactivePages <no-16981>`        Determines if the inactive pages are updated too. (bool)
:ref:`UseSmartFocus <no-16982>`              Determines if focus has to be restored to the last active
:ref:`Visible <no-16983>`                    Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-16984>`            Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-16985>`                      The width of the object. (int)
:ref:`WindowHandle <no-16986>`               The platform-specific handle for the window. Read-only. (long)

============================================ ========================


Properties
==========

.. _no-16957:

**MovableTabs** 

When True (default), tabs can be re-arranged by dragging, and docked at
    different sides of the control. This can only be set when the control is created.
    Default = True.  (bool)



-------


Properties - inherited
========================

.. _no-16886:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16887:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16888:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16889:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16890:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16891:

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

.. _no-16892:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16893:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16894:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16895:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16896:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16897:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16898:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16899:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16900:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16901:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16902:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16903:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16904:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16905:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16906:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16907:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16908:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16909:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16910:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16911:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16912:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16913:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16914:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16915:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16916:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16917:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16918:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16919:

**DynamicPageClass** 

Dynamically determine the value of the PageClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageClass property. If DynamicPageClass is set to None (the default), PageClass
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16920:

**DynamicPageCount** 

Dynamically determine the value of the PageCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageCount property. If DynamicPageCount is set to None (the default), PageCount
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16921:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16922:

**DynamicSelectedPage** 

Dynamically determine the value of the SelectedPage property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPage property. If DynamicSelectedPage is set to None (the default), SelectedPage
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16923:

**DynamicSelectedPageNumber** 

Dynamically determine the value of the SelectedPageNumber property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPageNumber property. If DynamicSelectedPageNumber is set to None (the default), SelectedPageNumber
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16924:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16925:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16926:

**DynamicTabPosition** 

Dynamically determine the value of the TabPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabPosition property. If DynamicTabPosition is set to None (the default), TabPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16927:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16928:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16929:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16930:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16931:

**DynamicUpdateInactivePages** 

Dynamically determine the value of the UpdateInactivePages property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UpdateInactivePages property. If DynamicUpdateInactivePages is set to None (the default), UpdateInactivePages
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16932:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16933:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16934:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16935:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16936:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16937:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16938:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16939:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16940:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16941:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16942:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16943:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16944:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16945:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16946:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16947:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16948:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16949:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16950:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16951:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16952:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16953:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16954:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16955:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16956:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16958:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16959:

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

.. _no-16960:

**PageClass** 

Specifies the class of control to use for pages by default. (classRef)
    This really only applies when using the PageCount property to set the
    number of pages. If you instead use AddPage() you still need to send
    an instance as usual. Class must descend from a dabo base class.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16961:

**PageCount** 

Specifies the number of pages in the pageframe. (int)
    When using this to increase the number of pages, PageClass
    will be queried as the object to use as the page object.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16962:

**PageSizerClass** 

Default sizer class for pages added automatically to this control. Set
    this to None to prevent sizers from being automatically added to child
    pages. (dSizer or None)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16963:

**Pages** 

Returns a list of the contained pages.  (list)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16964:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16965:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16966:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16967:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16968:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16969:

**SelectedPage** 

References the current frontmost page.  (dPage)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16970:

**SelectedPageNumber** 

Returns the index of the current frontmost page.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16971:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16972:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16973:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16974:

**TabPosition** 

Specifies where the page tabs are located. (int)
        Top (default)
        Left
        Right
        Bottom


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16975:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-16976:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16977:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16978:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16979:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16980:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16981:

**UpdateInactivePages** 

Determines if the inactive pages are updated too. (bool)
    Setting it to False can significantly improve update performance
    of multipage forms. Default=True.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16982:

**UseSmartFocus** 

Determines if focus has to be restored to the last active
    control on page when it become selected. (bool) Default=False.
    


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-16983:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16984:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16985:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16986:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-16987>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-16988>`                 Occurs after the control or form is created.
:ref:`Destroy <no-16989>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-16990>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-16991>`               Occurs when the control gets the focus.
:ref:`Idle <no-16992>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-16993>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-16994>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-16995>`               
:ref:`KeyUp <no-16996>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-16997>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-16998>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-16999>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-17000>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-17001>`             
:ref:`MouseLeave <no-17002>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-17003>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-17004>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-17005>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-17006>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-17007>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-17008>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-17009>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-17010>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-17011>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-17012>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-17013>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-17014>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-17015>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-17016>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-17017>`                   Occurs when the control's position changes.
:ref:`Paint <no-17018>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-17019>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-17020>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-17021>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-17022>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-16987:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-16988:

**Create** 

Occurs after the control or form is created.



-------

.. _no-16989:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-16990:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-16991:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-16992:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-16993:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-16994:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-16995:

**KeyEvent** 



-------

.. _no-16996:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-16997:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-16998:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-16999:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-17000:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-17001:

**MouseEvent** 



-------

.. _no-17002:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-17003:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-17004:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-17005:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-17006:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-17007:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-17008:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-17009:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-17010:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-17011:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-17012:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-17013:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-17014:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-17015:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-17016:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-17017:

**Move** 

Occurs when the control's position changes.



-------

.. _no-17018:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-17019:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-17020:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-17021:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-17022:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-17023>`           Translates a position value for a control to absolute screen position.
:ref:`addImage <no-17024>`                      Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-17025>`                     Instantiate object as a child of self.
:ref:`afterInit <no-17026>`                     Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-17027>`                  
:ref:`afterSetProperties <no-17028>`            
:ref:`appendPage <no-17029>`                    Appends the page to the pageframe, and optionally sets
:ref:`autoBindEvents <no-17030>`                Automatically bind any on*() methods to the associated event.
:ref:`base_AcceptsFocus <no-17031>`             Please use PyPanel.AcceptsFocus instead.
:ref:`base_AcceptsFocusFromKeyboard <no-17032>` Please use PyPanel.AcceptsFocusFromKeyboard instead.
:ref:`base_AddChild <no-17033>`                 Please use PyPanel.AddChild instead.
:ref:`base_DoGetBestSize <no-17034>`            Please use PyPanel.DoGetBestSize instead.
:ref:`base_DoGetClientSize <no-17035>`          Please use PyPanel.DoGetClientSize instead.
:ref:`base_DoGetPosition <no-17036>`            Please use PyPanel.DoGetPosition instead.
:ref:`base_DoGetSize <no-17037>`                Please use PyPanel.DoGetSize instead.
:ref:`base_DoGetVirtualSize <no-17038>`         Please use PyPanel.DoGetVirtualSize instead.
:ref:`base_DoMoveWindow <no-17039>`             Please use PyPanel.DoMoveWindow instead.
:ref:`base_DoSetClientSize <no-17040>`          Please use PyPanel.DoSetClientSize instead.
:ref:`base_DoSetSize <no-17041>`                Please use PyPanel.DoSetSize instead.
:ref:`base_DoSetVirtualSize <no-17042>`         Please use PyPanel.DoSetVirtualSize instead.
:ref:`base_Enable <no-17043>`                   Please use PyPanel.Enable instead.
:ref:`base_GetDefaultAttributes <no-17044>`     Please use PyPanel.GetDefaultAttributes instead.
:ref:`base_GetMaxSize <no-17045>`               Please use PyPanel.GetMaxSize instead.
:ref:`base_InitDialog <no-17046>`               Please use PyPanel.InitDialog instead.
:ref:`base_OnInternalIdle <no-17047>`           Please use PyPanel.OnInternalIdle instead.
:ref:`base_RemoveChild <no-17048>`              Please use PyPanel.RemoveChild instead.
:ref:`base_ShouldInheritColours <no-17049>`     Please use PyPanel.ShouldInheritColours instead.
:ref:`base_TransferDataFromWindow <no-17050>`   Please use PyPanel.TransferDataFromWindow instead.
:ref:`base_TransferDataToWindow <no-17051>`     Please use PyPanel.TransferDataToWindow instead.
:ref:`base_Validate <no-17052>`                 Please use PyPanel.Validate instead.
:ref:`beforeInit <no-17053>`                    Subclass hook. Called before the object is fully instantiated.
:ref:`beforePageChange <no-17054>`              Return False from this method to prevent the page from changing.
:ref:`beforeSetProperties <no-17055>`           
:ref:`bindEvent <no-17056>`                     Bind a dEvent to a callback function.
:ref:`bindEvents <no-17057>`                    Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-17058>`                       Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-17059>`                  Makes this object topmost
:ref:`clear <no-17060>`                         Clears the background of custom-drawn objects.
:ref:`clone <no-17061>`                         Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-17062>`          Given a position relative to this control, return a position relative
:ref:`copy <no-17063>`                          Called by uiApp when the user requests a copy operation.
:ref:`cut <no-17064>`                           Called by uiApp when the user requests a cut operation.
:ref:`cyclePages <no-17065>`                    Moves through the pages by the specified amount, wrapping
:ref:`drawArc <no-17066>`                       Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-17067>`                    Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-17068>`                    Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-17069>`                   Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-17070>`               Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-17071>`                  Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-17072>`                      Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-17073>`                 Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-17074>`                   Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-17075>`                 Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-17076>`          Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-17077>`                      Draws text on the object at the specified position
:ref:`endHover <no-17078>`                      
:ref:`fitToSizer <no-17079>`                    Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-17080>`                    Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-17081>`                Reset the font zoom back to zero.
:ref:`fontZoomOut <no-17082>`                   Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-17083>`               Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-17084>`               Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-17085>`              Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-17086>`             Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-17087>`              Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-17088>`              Returns the current mouse position on the entire screen
:ref:`getPageImage <no-17089>`                  Returns the index of the specified page's image in the
:ref:`getPositionInSizer <no-17090>`            Convenience method to let you call this directly on the object.
:ref:`getProperties <no-17091>`                 Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-17092>`                  Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-17093>`                 Returns a dict containing the object's sizer property info. The
:ref:`hide <no-17094>`                          Make the object invisible.
:ref:`initEvents <no-17095>`                    Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-17096>`                Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-17097>`                    Insert the page into the pageframe at the specified position,
:ref:`isContainedBy <no-17098>`                 Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-17099>`                   Call the given function on this object and all of its Children. If
:ref:`layout <no-17100>`                        Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-17101>`                   Locks the visual updates to the control.
:ref:`movePage <no-17102>`                      Moves the specified 'old' page to the new position and
:ref:`moveTabOrderAfter <no-17103>`             Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-17104>`            Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-17105>`             Given a position relative to the form, return a position relative
:ref:`onHover <no-17106>`                       
:ref:`paste <no-17107>`                         Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-17108>`                   
:ref:`processDroppedFiles <no-17109>`           Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-17110>`            Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-17111>`                    Raise the passed Dabo event.
:ref:`reCreate <no-17112>`                      Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-17113>`                      Recreate the object.
:ref:`redraw <no-17114>`                        Called when the object is (re)drawn.
:ref:`refresh <no-17115>`                       Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-17116>`           Translates an absolute screen position to position value for a control.
:ref:`release <no-17117>`                       Destroys the object.
:ref:`removeDrawnObject <no-17118>`             
:ref:`removePage <no-17119>`                    Removes the specified page. You can specify a page by either
:ref:`sendToBack <no-17120>`                    Places this object behind all others.
:ref:`setAll <no-17121>`                        Set all child object properties to the passed value.
:ref:`setFocus <no-17122>`                      Sets focus to the object.
:ref:`setPageImage <no-17123>`                  Sets the specified page's image to the image corresponding
:ref:`setPositionInSizer <no-17124>`            Convenience method to let you call this directly on the object.
:ref:`setProperties <no-17125>`                 Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-17126>`         Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-17127>`                  Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-17128>`                 Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-17129>`                          Make the object visible.
:ref:`showContainingPage <no-17130>`            If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-17131>`               Display a context menu (popup) at the specified position.
:ref:`super <no-17132>`                         This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-17133>`                   Remove a previously registered event binding.
:ref:`unbindKey <no-17134>`                     Unbind a previously bound key combination.
:ref:`unlockDisplay <no-17135>`                 Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-17136>`              Immediately unlocks the display, no matter how many previous
:ref:`update <no-17137>`                        Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-17097:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.insertPage(self, pos, pgCls=None, caption='', imgKey=None, ignoreOverride=False)

   
   Insert the page into the pageframe at the specified position,
   and optionally sets the page caption and image. The image
   should have already been added to the pageframe if it is
   going to be set here.
   



-------


Methods - inherited
=====================

.. _no-17023:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17024:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.addImage(self, img, key=None)
   :noindex:


   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17025:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-17026:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17027:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17028:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17029:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.appendPage(self, pgCls=None, caption='', imgKey=None, \**kwargs)
   :noindex:


   
   Appends the page to the pageframe, and optionally sets
   the page caption and image. The image should have already
   been added to the pageframe if it is going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17030:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.autoBindEvents(self, force=True)
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

.. _no-17031:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_AcceptsFocus(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AcceptsFocus instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17032:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_AcceptsFocusFromKeyboard(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AcceptsFocusFromKeyboard instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17033:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_AddChild(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AddChild instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17034:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoGetBestSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetBestSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17035:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoGetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetClientSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17036:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoGetPosition(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetPosition instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17037:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoGetSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17038:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoGetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetVirtualSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17039:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoMoveWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoMoveWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17040:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoSetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetClientSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17041:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoSetSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17042:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_DoSetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetVirtualSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17043:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_Enable(*args, \**kwargs)
   :noindex:


   Please use PyPanel.Enable instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17044:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_GetDefaultAttributes(*args, \**kwargs)
   :noindex:


   Please use PyPanel.GetDefaultAttributes instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17045:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_GetMaxSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.GetMaxSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17046:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_InitDialog(*args, \**kwargs)
   :noindex:


   Please use PyPanel.InitDialog instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17047:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_OnInternalIdle(*args, \**kwargs)
   :noindex:


   Please use PyPanel.OnInternalIdle instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17048:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_RemoveChild(*args, \**kwargs)
   :noindex:


   Please use PyPanel.RemoveChild instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17049:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_ShouldInheritColours(*args, \**kwargs)
   :noindex:


   Please use PyPanel.ShouldInheritColours instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17050:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_TransferDataFromWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.TransferDataFromWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17051:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_TransferDataToWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.TransferDataToWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17052:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.base_Validate(*args, \**kwargs)
   :noindex:


   Please use PyPanel.Validate instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17053:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17054:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.beforePageChange(self, fromPage, toPage)
   :noindex:


   Return False from this method to prevent the page from changing.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17055:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17056:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17057:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17058:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-17059:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17060:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17061:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17062:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17063:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17064:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17065:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.cyclePages(self, num)
   :noindex:


   
   Moves through the pages by the specified amount, wrapping
   around the ends. Negative values move to previous pages; positive
   move through the next pages.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17066:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17067:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17068:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-17069:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17070:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17071:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17072:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17073:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17074:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17075:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17076:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17077:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17078:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17079:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17080:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17081:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17082:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17083:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17084:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17085:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17086:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17087:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17088:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17089:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getPageImage(self, pg)
   :noindex:


   
   Returns the index of the specified page's image in the
   current image list, or -1 if no image is set for the page.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17090:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17091:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-17092:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17093:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17094:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17095:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17096:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17098:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17099:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17100:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.layout(self)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17101:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.lockDisplay(self)
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

.. _no-17102:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.movePage(self, oldPgOrPos, newPos, selecting=True)
   :noindex:


   
   Moves the specified 'old' page to the new position and
   optionally selects it. If an invalid page number is passed,
   it returns False without changing anything.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17103:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17104:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17105:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17106:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17107:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17108:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17109:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17110:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17111:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17112:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17113:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17114:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17115:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17116:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17117:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17118:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17119:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.removePage(self, pgOrPos, delPage=True)
   :noindex:


   
   Removes the specified page. You can specify a page by either
   passing the page itself, or a position. If delPage is True (default),
   the page is released, and None is returned. If delPage is
   False, the page is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17120:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17121:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-17122:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17123:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setPageImage(self, pg, imgKey)
   :noindex:


   
   Sets the specified page's image to the image corresponding
   to the specified key. May also optionally pass the index of the
   image in the ImageList rather than the key.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17124:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17125:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-17126:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-17127:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17128:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17129:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17130:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17131:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17132:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17133:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17134:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17135:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17136:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17137:

.. function:: dabo.ui.uiwx.dPageFrame.dDockTabs.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
