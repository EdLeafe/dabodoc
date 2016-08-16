
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrame

.. _dabo.ui.uiwx.dPageFrame.dPageToolBar:

================================================
|doc_title|  **dPageFrame.dPageToolBar** - class
================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPageToolBar**

.. inheritance-diagram:: dPageToolBar


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`



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



   * - .. image:: _static/macWidgets/dPageToolBar.png
          :scale: 75 %
          :target: _static/macWidgets/dPageToolBar.png
          :alt: dPageToolBar



     - .. image:: _static/winWidgets/dPageToolBar.png
          :scale: 75 %
          :target: _static/winWidgets/dPageToolBar.png
          :alt: dPageToolBar



     - .. image:: _static/nixWidgets/dPageToolBar.png
          :scale: 75 %
          :target: _static/nixWidgets/dPageToolBar.png
          :alt: dPageToolBar


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrame.dPageToolBar

   .. automethod:: dabo.ui.uiwx.dPageFrame.dPageToolBar.__init__

|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Application <no-18104>`                Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-18105>`                  Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-18106>`                  The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-18107>`                Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-18108>`                Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-18109>`            Style of line for the border drawn around the control.
:ref:`BorderStyle <no-18110>`                Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-18111>`                Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-18112>`                     The position of the bottom side of the object. This is a
:ref:`Caption <no-18113>`                    The caption of the object. (str)
:ref:`Children <no-18114>`                   Returns a list of object references to the children of
:ref:`Class <no-18115>`                      The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-18116>`           Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-18117>`       Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-18118>`         Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-18119>`         Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-18120>`           Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-18121>`         Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-18122>`     Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-18123>`         Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-18124>`         Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-18125>`             Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-18126>`             Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-18127>`                Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-18128>`            Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-18129>`            Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-18130>`          Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-18131>`            Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-18132>`       Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-18133>`           Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-18134>`              Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-18135>`                Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-18136>`        Dynamically determine the value of the MousePointer property.
:ref:`DynamicPageClass <no-18137>`           Dynamically determine the value of the PageClass property.
:ref:`DynamicPageCount <no-18138>`           Dynamically determine the value of the PageCount property.
:ref:`DynamicPosition <no-18139>`            Dynamically determine the value of the Position property.
:ref:`DynamicSelectedPage <no-18140>`        Dynamically determine the value of the SelectedPage property.
:ref:`DynamicSelectedPageNumber <no-18141>`  Dynamically determine the value of the SelectedPageNumber property.
:ref:`DynamicSize <no-18142>`                Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-18143>`          Dynamically determine the value of the StatusText property.
:ref:`DynamicTabPosition <no-18144>`         Dynamically determine the value of the TabPosition property.
:ref:`DynamicTag <no-18145>`                 Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-18146>`         Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-18147>`                 Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-18148>`        Dynamically determine the value of the Transparency property.
:ref:`DynamicUpdateInactivePages <no-18149>` Dynamically determine the value of the UpdateInactivePages property.
:ref:`DynamicVisible <no-18150>`             Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-18151>`               Dynamically determine the value of the Width property.
:ref:`Enabled <no-18152>`                    Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-18153>`                       Specifies font object for this control. (dFont)
:ref:`FontBold <no-18154>`                   Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-18155>`            Human-readable description of the current font settings. (str)
:ref:`FontFace <no-18156>`                   Specifies the font face. (str)
:ref:`FontInfo <no-18157>`                   Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-18158>`                 Specifies whether font is italicized. (bool)
:ref:`FontSize <no-18159>`                   Specifies the point size of the font. (int)
:ref:`FontUnderline <no-18160>`              Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-18161>`                  Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-18162>`                       Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-18163>`                     Specifies the height of the object. (int)
:ref:`HelpContextText <no-18164>`            Specifies the context-sensitive help text associated with this
:ref:`Hover <no-18165>`                      When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-18166>`                       Specifies the left position of the object. (int)
:ref:`LogEvents <no-18167>`                  Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-18168>`              Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-18169>`                Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-18170>`               Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-18171>`              Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-18172>`                Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-18173>`               Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-18174>`               Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-18175>`                       Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-18176>`                   Specifies the base name of the object.
:ref:`PageClass <no-18177>`                  Specifies the class of control to use for pages by default. (classRef)
:ref:`PageCount <no-18178>`                  Specifies the number of pages in the pageframe. (int)
:ref:`PageSizerClass <no-18179>`             Default sizer class for pages added automatically to this control. Set
:ref:`Pages <no-18180>`                      Returns a list of the contained pages.  (list)
:ref:`Parent <no-18181>`                     The containing object. (obj)
:ref:`Position <no-18182>`                   The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-18183>`          Reference to the Preference Management object  (dPref)
:ref:`RegID <no-18184>`                      A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-18185>`                      The position of the right side of the object. This is a
:ref:`SelectedPage <no-18186>`               References the current frontmost page.  (dPage)
:ref:`SelectedPageNumber <no-18187>`         Returns the index of the current frontmost page.  (int)
:ref:`Size <no-18188>`                       The size of the object. (tuple)
:ref:`Sizer <no-18189>`                      The sizer for the object.
:ref:`StatusText <no-18190>`                 Specifies the text that displays in the form's status bar, if any.
:ref:`TabPosition <no-18191>`                Specifies where the page tabs are located. (int)
:ref:`TabStop <no-18192>`                    Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-18193>`                        A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-18194>`                Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-18195>`                        The top position of the object. (int)
:ref:`Transparency <no-18196>`               Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-18197>`          Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateInactivePages <no-18198>`        Determines if the inactive pages are updated too. (bool)
:ref:`UseSmartFocus <no-18199>`              Determines if focus has to be restored to the last active
:ref:`Visible <no-18200>`                    Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-18201>`            Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-18202>`                      The width of the object. (int)
:ref:`WindowHandle <no-18203>`               The platform-specific handle for the window. Read-only. (long)

============================================ ========================


Properties - inherited
========================

.. _no-18104:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18105:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18106:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18107:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18108:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18109:

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

.. _no-18110:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18111:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18112:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18113:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18114:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18115:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18116:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18117:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18118:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18119:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18120:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18121:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18122:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18123:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18124:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18125:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18126:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18127:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18128:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18129:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18130:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18131:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18132:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18133:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18134:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18135:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18136:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18137:

**DynamicPageClass** 

Dynamically determine the value of the PageClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageClass property. If DynamicPageClass is set to None (the default), PageClass
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18138:

**DynamicPageCount** 

Dynamically determine the value of the PageCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageCount property. If DynamicPageCount is set to None (the default), PageCount
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18139:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18140:

**DynamicSelectedPage** 

Dynamically determine the value of the SelectedPage property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPage property. If DynamicSelectedPage is set to None (the default), SelectedPage
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18141:

**DynamicSelectedPageNumber** 

Dynamically determine the value of the SelectedPageNumber property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPageNumber property. If DynamicSelectedPageNumber is set to None (the default), SelectedPageNumber
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18142:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18143:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18144:

**DynamicTabPosition** 

Dynamically determine the value of the TabPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabPosition property. If DynamicTabPosition is set to None (the default), TabPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18145:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18146:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18147:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18148:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18149:

**DynamicUpdateInactivePages** 

Dynamically determine the value of the UpdateInactivePages property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UpdateInactivePages property. If DynamicUpdateInactivePages is set to None (the default), UpdateInactivePages
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18150:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18151:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18152:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18153:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18154:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18155:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18156:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18157:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18158:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18159:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18160:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18161:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18162:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18163:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18164:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18165:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18166:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18167:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18168:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18169:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18170:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18171:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18172:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18173:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18174:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18175:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18176:

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

.. _no-18177:

**PageClass** 

Specifies the class of control to use for pages by default. (classRef)
    This really only applies when using the PageCount property to set the
    number of pages. If you instead use AddPage() you still need to send
    an instance as usual. Class must descend from a dabo base class.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18178:

**PageCount** 

Specifies the number of pages in the pageframe. (int)
    When using this to increase the number of pages, PageClass
    will be queried as the object to use as the page object.


Inherited from: 'wx._controls.BookCtrlBase - can not provide a link

-------

.. _no-18179:

**PageSizerClass** 

Default sizer class for pages added automatically to this control. Set
    this to None to prevent sizers from being automatically added to child
    pages. (dSizer or None)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18180:

**Pages** 

Returns a list of the contained pages.  (list)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18181:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18182:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18183:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18184:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18185:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18186:

**SelectedPage** 

References the current frontmost page.  (dPage)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18187:

**SelectedPageNumber** 

Returns the index of the current frontmost page.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18188:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18189:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-18190:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18191:

**TabPosition** 

Specifies where the page tabs are located. (int)
        Top (default)
        Left
        Right
        Bottom


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18192:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-18193:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18194:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18195:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18196:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18197:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18198:

**UpdateInactivePages** 

Determines if the inactive pages are updated too. (bool)
    Setting it to False can significantly improve update performance
    of multipage forms. Default=True.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18199:

**UseSmartFocus** 

Determines if focus has to be restored to the last active
    control on page when it become selected. (bool) Default=False.
    


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18200:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18201:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18202:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18203:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-18204>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-18205>`                 Occurs after the control or form is created.
:ref:`Destroy <no-18206>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-18207>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-18208>`               Occurs when the control gets the focus.
:ref:`Idle <no-18209>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-18210>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-18211>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-18212>`               
:ref:`KeyUp <no-18213>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-18214>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-18215>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-18216>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-18217>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-18218>`             
:ref:`MouseLeave <no-18219>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-18220>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-18221>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-18222>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-18223>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-18224>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-18225>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-18226>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-18227>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-18228>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-18229>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-18230>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-18231>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-18232>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-18233>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-18234>`                   Occurs when the control's position changes.
:ref:`Paint <no-18235>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-18236>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-18237>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-18238>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-18239>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-18204:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-18205:

**Create** 

Occurs after the control or form is created.



-------

.. _no-18206:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-18207:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-18208:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-18209:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-18210:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-18211:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-18212:

**KeyEvent** 



-------

.. _no-18213:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-18214:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-18215:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-18216:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-18217:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-18218:

**MouseEvent** 



-------

.. _no-18219:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-18220:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-18221:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-18222:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-18223:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-18224:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-18225:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-18226:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-18227:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-18228:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-18229:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-18230:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-18231:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-18232:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-18233:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-18234:

**Move** 

Occurs when the control's position changes.



-------

.. _no-18235:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-18236:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-18237:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-18238:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-18239:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-18240>`   Translates a position value for a control to absolute screen position.
:ref:`addImage <no-18241>`              Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-18242>`             Instantiate object as a child of self.
:ref:`afterInit <no-18243>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-18244>`          
:ref:`afterSetProperties <no-18245>`    
:ref:`appendPage <no-18246>`            Appends the page to the pageframe, and optionally sets
:ref:`autoBindEvents <no-18247>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-18248>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforePageChange <no-18249>`      Return False from this method to prevent the page from changing.
:ref:`beforeSetProperties <no-18250>`   
:ref:`bindEvent <no-18251>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-18252>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-18253>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-18254>`          Makes this object topmost
:ref:`clear <no-18255>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-18256>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-18257>`  Given a position relative to this control, return a position relative
:ref:`copy <no-18258>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-18259>`                   Called by uiApp when the user requests a cut operation.
:ref:`cyclePages <no-18260>`            Moves through the pages by the specified amount, wrapping
:ref:`drawArc <no-18261>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-18262>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-18263>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-18264>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-18265>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-18266>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-18267>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-18268>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-18269>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-18270>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-18271>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-18272>`              Draws text on the object at the specified position
:ref:`endHover <no-18273>`              
:ref:`fitToSizer <no-18274>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-18275>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-18276>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-18277>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-18278>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-18279>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-18280>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-18281>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-18282>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-18283>`      Returns the current mouse position on the entire screen
:ref:`getPageImage <no-18284>`          Returns the index of the specified page's image in the
:ref:`getPositionInSizer <no-18285>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-18286>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-18287>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-18288>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-18289>`                  Make the object invisible.
:ref:`initEvents <no-18290>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-18291>`        Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-18292>`            Insert the page into the pageframe at the specified position,
:ref:`isContainedBy <no-18293>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-18294>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-18295>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-18296>`           Locks the visual updates to the control.
:ref:`movePage <no-18297>`              Moves the specified 'old' page to the new position and
:ref:`moveTabOrderAfter <no-18298>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-18299>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-18300>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-18301>`               
:ref:`paste <no-18302>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-18303>`           
:ref:`processDroppedFiles <no-18304>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-18305>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-18306>`            Raise the passed Dabo event.
:ref:`reCreate <no-18307>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-18308>`              Recreate the object.
:ref:`redraw <no-18309>`                Called when the object is (re)drawn.
:ref:`refresh <no-18310>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-18311>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-18312>`               Destroys the object.
:ref:`removeDrawnObject <no-18313>`     
:ref:`removePage <no-18314>`            Removes the specified page. You can specify a page by either
:ref:`sendToBack <no-18315>`            Places this object behind all others.
:ref:`setAll <no-18316>`                Set all child object properties to the passed value.
:ref:`setFocus <no-18317>`              Sets focus to the object.
:ref:`setPageImage <no-18318>`          Sets the specified page's image to the image corresponding
:ref:`setPositionInSizer <no-18319>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-18320>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-18321>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-18322>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-18323>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-18324>`                  Make the object visible.
:ref:`showContainingPage <no-18325>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-18326>`       Display a context menu (popup) at the specified position.
:ref:`super <no-18327>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-18328>`           Remove a previously registered event binding.
:ref:`unbindKey <no-18329>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-18330>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-18331>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-18332>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-18314:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.removePage(self, pgOrPos, delPage=True)

   
   Removes the specified page. You can specify a page by either
   passing the page itself, or a position. If delPage is True (default),
   the page is released, and None is returned. If delPage is
   False, the page is returned. There is a bug in the wx.Toolbook class
   that breaks the link between the toolbar buttons and their pages
   when a page is removed, so this attempts to work around this.
   



-------


Methods - inherited
=====================

.. _no-18240:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18241:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.addImage(self, img, key=None)
   :noindex:


   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18242:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-18243:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18244:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18245:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18246:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.appendPage(self, pgCls=None, caption='', imgKey=None, \**kwargs)
   :noindex:


   
   Appends the page to the pageframe, and optionally sets
   the page caption and image. The image should have already
   been added to the pageframe if it is going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18247:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.autoBindEvents(self, force=True)
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

.. _no-18248:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18249:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.beforePageChange(self, fromPage, toPage)
   :noindex:


   Return False from this method to prevent the page from changing.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18250:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18251:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18252:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18253:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-18254:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18255:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18256:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18257:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18258:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18259:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18260:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.cyclePages(self, num)
   :noindex:


   
   Moves through the pages by the specified amount, wrapping
   around the ends. Negative values move to previous pages; positive
   move through the next pages.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18261:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18262:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18263:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-18264:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18265:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18266:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18267:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18268:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18269:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18270:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18271:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18272:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18273:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18274:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18275:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18276:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18277:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18278:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18279:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18280:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18281:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18282:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18283:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18284:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getPageImage(self, pg)
   :noindex:


   
   Returns the index of the specified page's image in the
   current image list, or -1 if no image is set for the page.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18285:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18286:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-18287:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18288:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18289:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18290:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18291:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18292:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.insertPage(self, pos, pgCls=None, caption='', imgKey=None, ignoreOverride=False, \**kwargs)
   :noindex:


   
   Insert the page into the pageframe at the specified position,
   and optionally sets the page caption and image. The image
   should have already been added to the pageframe if it is
   going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18293:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18294:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18295:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.layout(self)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18296:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.lockDisplay(self)
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

.. _no-18297:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.movePage(self, oldPgOrPos, newPos, selecting=True)
   :noindex:


   
   Moves the specified 'old' page to the new position and
   optionally selects it. If an invalid page number is passed,
   it returns False without changing anything.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18298:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18299:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18300:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18301:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18302:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18303:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18304:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18305:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18306:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18307:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18308:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18309:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18310:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18311:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18312:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18313:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18315:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18316:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-18317:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18318:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setPageImage(self, pg, imgKey)
   :noindex:


   
   Sets the specified page's image to the image corresponding
   to the specified key. May also optionally pass the index of the
   image in the ImageList rather than the key.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18319:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18320:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-18321:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-18322:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18323:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18324:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18325:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18326:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18327:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18328:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18329:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18330:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18331:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18332:

.. function:: dabo.ui.uiwx.dPageFrame.dPageToolBar.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
