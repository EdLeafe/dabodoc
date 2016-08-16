
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrame

.. _dabo.ui.uiwx.dPageFrame.dPageFrame:

==============================================
|doc_title|  **dPageFrame.dPageFrame** - class
==============================================


Creates a pageframe, which can contain an unlimited number of pages,
each of which should be a subclass/instance of the dPage class.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPageFrame**

.. inheritance-diagram:: dPageFrame


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



   * - .. image:: _static/macWidgets/dPageFrame.png
          :scale: 75 %
          :target: _static/macWidgets/dPageFrame.png
          :alt: dPageFrame



     - .. image:: _static/winWidgets/dPageFrame.png
          :scale: 75 %
          :target: _static/winWidgets/dPageFrame.png
          :alt: dPageFrame



     - .. image:: _static/nixWidgets/dPageFrame.png
          :scale: 75 %
          :target: _static/nixWidgets/dPageFrame.png
          :alt: dPageFrame


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrame.dPageFrame

   .. automethod:: dabo.ui.uiwx.dPageFrame.dPageFrame.__init__

|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Application <no-17138>`                Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-17139>`                  Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-17140>`                  The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-17141>`                Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-17142>`                Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-17143>`            Style of line for the border drawn around the control.
:ref:`BorderStyle <no-17144>`                Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-17145>`                Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-17146>`                     The position of the bottom side of the object. This is a
:ref:`Caption <no-17147>`                    The caption of the object. (str)
:ref:`Children <no-17148>`                   Returns a list of object references to the children of
:ref:`Class <no-17149>`                      The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-17150>`           Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-17151>`       Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-17152>`         Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-17153>`         Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-17154>`           Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-17155>`         Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-17156>`     Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-17157>`         Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-17158>`         Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-17159>`             Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-17160>`             Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-17161>`                Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-17162>`            Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-17163>`            Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-17164>`          Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-17165>`            Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-17166>`       Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-17167>`           Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-17168>`              Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-17169>`                Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-17170>`        Dynamically determine the value of the MousePointer property.
:ref:`DynamicPageClass <no-17171>`           Dynamically determine the value of the PageClass property.
:ref:`DynamicPageCount <no-17172>`           Dynamically determine the value of the PageCount property.
:ref:`DynamicPosition <no-17173>`            Dynamically determine the value of the Position property.
:ref:`DynamicSelectedPage <no-17174>`        Dynamically determine the value of the SelectedPage property.
:ref:`DynamicSelectedPageNumber <no-17175>`  Dynamically determine the value of the SelectedPageNumber property.
:ref:`DynamicSize <no-17176>`                Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-17177>`          Dynamically determine the value of the StatusText property.
:ref:`DynamicTabPosition <no-17178>`         Dynamically determine the value of the TabPosition property.
:ref:`DynamicTag <no-17179>`                 Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-17180>`         Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-17181>`                 Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-17182>`        Dynamically determine the value of the Transparency property.
:ref:`DynamicUpdateInactivePages <no-17183>` Dynamically determine the value of the UpdateInactivePages property.
:ref:`DynamicVisible <no-17184>`             Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-17185>`               Dynamically determine the value of the Width property.
:ref:`Enabled <no-17186>`                    Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-17187>`                       Specifies font object for this control. (dFont)
:ref:`FontBold <no-17188>`                   Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-17189>`            Human-readable description of the current font settings. (str)
:ref:`FontFace <no-17190>`                   Specifies the font face. (str)
:ref:`FontInfo <no-17191>`                   Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-17192>`                 Specifies whether font is italicized. (bool)
:ref:`FontSize <no-17193>`                   Specifies the point size of the font. (int)
:ref:`FontUnderline <no-17194>`              Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-17195>`                  Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-17196>`                       Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-17197>`                     Specifies the height of the object. (int)
:ref:`HelpContextText <no-17198>`            Specifies the context-sensitive help text associated with this
:ref:`Hover <no-17199>`                      When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-17200>`                       Specifies the left position of the object. (int)
:ref:`LogEvents <no-17201>`                  Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-17202>`              Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-17203>`                Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-17204>`               Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-17205>`              Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-17206>`                Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-17207>`               Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-17208>`               Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-17209>`                       Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-17210>`                   Specifies the base name of the object.
:ref:`PageClass <no-17211>`                  Specifies the class of control to use for pages by default. (classRef)
:ref:`PageCount <no-17212>`                  Specifies the number of pages in the pageframe. (int)
:ref:`PageSizerClass <no-17213>`             Default sizer class for pages added automatically to this control. Set
:ref:`Pages <no-17214>`                      Returns a list of the contained pages.  (list)
:ref:`Parent <no-17215>`                     The containing object. (obj)
:ref:`Position <no-17216>`                   The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-17217>`          Reference to the Preference Management object  (dPref)
:ref:`RegID <no-17218>`                      A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-17219>`                      The position of the right side of the object. This is a
:ref:`SelectedPage <no-17220>`               References the current frontmost page.  (dPage)
:ref:`SelectedPageNumber <no-17221>`         Returns the index of the current frontmost page.  (int)
:ref:`Size <no-17222>`                       The size of the object. (tuple)
:ref:`Sizer <no-17223>`                      The sizer for the object.
:ref:`StatusText <no-17224>`                 Specifies the text that displays in the form's status bar, if any.
:ref:`TabPosition <no-17225>`                Specifies where the page tabs are located. (int)
:ref:`TabStop <no-17226>`                    Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-17227>`                        A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-17228>`                Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-17229>`                        The top position of the object. (int)
:ref:`Transparency <no-17230>`               Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-17231>`          Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateInactivePages <no-17232>`        Determines if the inactive pages are updated too. (bool)
:ref:`UseSmartFocus <no-17233>`              Determines if focus has to be restored to the last active
:ref:`Visible <no-17234>`                    Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-17235>`            Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-17236>`                      The width of the object. (int)
:ref:`WindowHandle <no-17237>`               The platform-specific handle for the window. Read-only. (long)

============================================ ========================


Properties - inherited
========================

.. _no-17138:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17139:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17140:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17141:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17142:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17143:

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

.. _no-17144:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17145:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17146:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17147:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17148:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17149:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17150:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17151:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17152:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17153:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17154:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17155:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17156:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17157:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17158:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17159:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17160:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17161:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17162:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17163:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17164:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17165:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17166:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17167:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17168:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17169:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17170:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17171:

**DynamicPageClass** 

Dynamically determine the value of the PageClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageClass property. If DynamicPageClass is set to None (the default), PageClass
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17172:

**DynamicPageCount** 

Dynamically determine the value of the PageCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageCount property. If DynamicPageCount is set to None (the default), PageCount
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17173:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17174:

**DynamicSelectedPage** 

Dynamically determine the value of the SelectedPage property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPage property. If DynamicSelectedPage is set to None (the default), SelectedPage
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17175:

**DynamicSelectedPageNumber** 

Dynamically determine the value of the SelectedPageNumber property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPageNumber property. If DynamicSelectedPageNumber is set to None (the default), SelectedPageNumber
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17176:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17177:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17178:

**DynamicTabPosition** 

Dynamically determine the value of the TabPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabPosition property. If DynamicTabPosition is set to None (the default), TabPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17179:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17180:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17181:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17182:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17183:

**DynamicUpdateInactivePages** 

Dynamically determine the value of the UpdateInactivePages property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UpdateInactivePages property. If DynamicUpdateInactivePages is set to None (the default), UpdateInactivePages
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17184:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17185:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17186:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17187:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17188:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17189:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17190:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17191:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17192:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17193:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17194:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17195:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17196:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17197:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17198:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17199:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17200:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17201:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17202:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17203:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17204:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17205:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17206:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17207:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17208:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17209:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17210:

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

.. _no-17211:

**PageClass** 

Specifies the class of control to use for pages by default. (classRef)
    This really only applies when using the PageCount property to set the
    number of pages. If you instead use AddPage() you still need to send
    an instance as usual. Class must descend from a dabo base class.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17212:

**PageCount** 

Specifies the number of pages in the pageframe. (int)
    When using this to increase the number of pages, PageClass
    will be queried as the object to use as the page object.


Inherited from: 'wx._controls.BookCtrlBase - can not provide a link

-------

.. _no-17213:

**PageSizerClass** 

Default sizer class for pages added automatically to this control. Set
    this to None to prevent sizers from being automatically added to child
    pages. (dSizer or None)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17214:

**Pages** 

Returns a list of the contained pages.  (list)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17215:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17216:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17217:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17218:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17219:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17220:

**SelectedPage** 

References the current frontmost page.  (dPage)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17221:

**SelectedPageNumber** 

Returns the index of the current frontmost page.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17222:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17223:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17224:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17225:

**TabPosition** 

Specifies where the page tabs are located. (int)
        Top (default)
        Left
        Right
        Bottom


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17226:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-17227:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17228:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17229:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17230:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17231:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17232:

**UpdateInactivePages** 

Determines if the inactive pages are updated too. (bool)
    Setting it to False can significantly improve update performance
    of multipage forms. Default=True.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17233:

**UseSmartFocus** 

Determines if focus has to be restored to the last active
    control on page when it become selected. (bool) Default=False.
    


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17234:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17235:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17236:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17237:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-17238>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-17239>`              Occurs when a child control is created.
:ref:`Create <no-17240>`                 Occurs after the control or form is created.
:ref:`Destroy <no-17241>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-17242>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-17243>`               Occurs when the control gets the focus.
:ref:`Idle <no-17244>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-17245>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-17246>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-17247>`               
:ref:`KeyUp <no-17248>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-17249>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-17250>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-17251>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-17252>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-17253>`             
:ref:`MouseLeave <no-17254>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-17255>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-17256>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-17257>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-17258>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-17259>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-17260>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-17261>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-17262>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-17263>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-17264>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-17265>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-17266>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-17267>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-17268>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-17269>`                   Occurs when the control's position changes.
:ref:`PageChanged <no-17270>`            Occurs when a page in a pageframe-like control changes
:ref:`PageChanging <no-17271>`           Occurs when the current page in a pageframe-like control is about to change
:ref:`Paint <no-17272>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-17273>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-17274>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-17275>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-17276>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-17238:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-17239:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-17240:

**Create** 

Occurs after the control or form is created.



-------

.. _no-17241:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-17242:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-17243:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-17244:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-17245:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-17246:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-17247:

**KeyEvent** 



-------

.. _no-17248:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-17249:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-17250:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-17251:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-17252:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-17253:

**MouseEvent** 



-------

.. _no-17254:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-17255:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-17256:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-17257:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-17258:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-17259:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-17260:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-17261:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-17262:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-17263:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-17264:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-17265:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-17266:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-17267:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-17268:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-17269:

**Move** 

Occurs when the control's position changes.



-------

.. _no-17270:

**PageChanged** 

Occurs when a page in a pageframe-like control changes



-------

.. _no-17271:

**PageChanging** 

Occurs when the current page in a pageframe-like control is about to change



-------

.. _no-17272:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-17273:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-17274:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-17275:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-17276:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-17277>`   Translates a position value for a control to absolute screen position.
:ref:`addImage <no-17278>`              Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-17279>`             Instantiate object as a child of self.
:ref:`afterInit <no-17280>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-17281>`          
:ref:`afterSetProperties <no-17282>`    
:ref:`appendPage <no-17283>`            Appends the page to the pageframe, and optionally sets
:ref:`autoBindEvents <no-17284>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-17285>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforePageChange <no-17286>`      Return False from this method to prevent the page from changing.
:ref:`beforeSetProperties <no-17287>`   
:ref:`bindEvent <no-17288>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-17289>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-17290>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-17291>`          Makes this object topmost
:ref:`clear <no-17292>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-17293>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-17294>`  Given a position relative to this control, return a position relative
:ref:`copy <no-17295>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-17296>`                   Called by uiApp when the user requests a cut operation.
:ref:`cyclePages <no-17297>`            Moves through the pages by the specified amount, wrapping
:ref:`drawArc <no-17298>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-17299>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-17300>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-17301>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-17302>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-17303>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-17304>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-17305>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-17306>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-17307>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-17308>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-17309>`              Draws text on the object at the specified position
:ref:`endHover <no-17310>`              
:ref:`fitToSizer <no-17311>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-17312>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-17313>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-17314>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-17315>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-17316>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-17317>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-17318>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-17319>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-17320>`      Returns the current mouse position on the entire screen
:ref:`getPageImage <no-17321>`          Returns the index of the specified page's image in the
:ref:`getPositionInSizer <no-17322>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-17323>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-17324>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-17325>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-17326>`                  Make the object invisible.
:ref:`initEvents <no-17327>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-17328>`        Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-17329>`            Insert the page into the pageframe at the specified position,
:ref:`isContainedBy <no-17330>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-17331>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-17332>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-17333>`           Locks the visual updates to the control.
:ref:`movePage <no-17334>`              Moves the specified 'old' page to the new position and
:ref:`moveTabOrderAfter <no-17335>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-17336>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-17337>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-17338>`               
:ref:`paste <no-17339>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-17340>`           
:ref:`processDroppedFiles <no-17341>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-17342>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-17343>`            Raise the passed Dabo event.
:ref:`reCreate <no-17344>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-17345>`              Recreate the object.
:ref:`redraw <no-17346>`                Called when the object is (re)drawn.
:ref:`refresh <no-17347>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-17348>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-17349>`               Destroys the object.
:ref:`removeDrawnObject <no-17350>`     
:ref:`removePage <no-17351>`            Removes the specified page. You can specify a page by either
:ref:`sendToBack <no-17352>`            Places this object behind all others.
:ref:`setAll <no-17353>`                Set all child object properties to the passed value.
:ref:`setFocus <no-17354>`              Sets focus to the object.
:ref:`setPageImage <no-17355>`          Sets the specified page's image to the image corresponding
:ref:`setPositionInSizer <no-17356>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-17357>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-17358>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-17359>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-17360>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-17361>`                  Make the object visible.
:ref:`showContainingPage <no-17362>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-17363>`       Display a context menu (popup) at the specified position.
:ref:`super <no-17364>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-17365>`           Remove a previously registered event binding.
:ref:`unbindKey <no-17366>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-17367>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-17368>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-17369>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-17277:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17278:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.addImage(self, img, key=None)
   :noindex:


   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17279:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-17280:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17281:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17282:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17283:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.appendPage(self, pgCls=None, caption='', imgKey=None, \**kwargs)
   :noindex:


   
   Appends the page to the pageframe, and optionally sets
   the page caption and image. The image should have already
   been added to the pageframe if it is going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17284:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.autoBindEvents(self, force=True)
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

.. _no-17285:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17286:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.beforePageChange(self, fromPage, toPage)
   :noindex:


   Return False from this method to prevent the page from changing.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17287:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17288:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17289:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17290:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-17291:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17292:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17293:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17294:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17295:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17296:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17297:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.cyclePages(self, num)
   :noindex:


   
   Moves through the pages by the specified amount, wrapping
   around the ends. Negative values move to previous pages; positive
   move through the next pages.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17298:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17299:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17300:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-17301:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17302:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17303:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17304:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17305:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17306:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17307:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17308:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17309:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17310:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17311:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17312:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17313:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17314:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17315:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17316:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17317:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17318:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17319:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17320:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17321:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getPageImage(self, pg)
   :noindex:


   
   Returns the index of the specified page's image in the
   current image list, or -1 if no image is set for the page.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17322:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17323:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-17324:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17325:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17326:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17327:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17328:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17329:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.insertPage(self, pos, pgCls=None, caption='', imgKey=None, ignoreOverride=False, \**kwargs)
   :noindex:


   
   Insert the page into the pageframe at the specified position,
   and optionally sets the page caption and image. The image
   should have already been added to the pageframe if it is
   going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17330:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17331:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17332:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.layout(self)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17333:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.lockDisplay(self)
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

.. _no-17334:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.movePage(self, oldPgOrPos, newPos, selecting=True)
   :noindex:


   
   Moves the specified 'old' page to the new position and
   optionally selects it. If an invalid page number is passed,
   it returns False without changing anything.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17335:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17336:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17337:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17338:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17339:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17340:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17341:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17342:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17343:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17344:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17345:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17346:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17347:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17348:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17349:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17350:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17351:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.removePage(self, pgOrPos, delPage=True)
   :noindex:


   
   Removes the specified page. You can specify a page by either
   passing the page itself, or a position. If delPage is True (default),
   the page is released, and None is returned. If delPage is
   False, the page is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17352:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17353:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-17354:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17355:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setPageImage(self, pg, imgKey)
   :noindex:


   
   Sets the specified page's image to the image corresponding
   to the specified key. May also optionally pass the index of the
   image in the ImageList rather than the key.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17356:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17357:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-17358:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-17359:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17360:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17361:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17362:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17363:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17364:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17365:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17366:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17367:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17368:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17369:

.. function:: dabo.ui.uiwx.dPageFrame.dPageFrame.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
