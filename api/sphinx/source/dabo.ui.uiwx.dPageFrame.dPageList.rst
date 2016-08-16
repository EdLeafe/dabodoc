
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrame

.. _dabo.ui.uiwx.dPageFrame.dPageList:

=============================================
|doc_title|  **dPageFrame.dPageList** - class
=============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPageList**

.. inheritance-diagram:: dPageList


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



   * - .. image:: _static/macWidgets/dPageList.png
          :scale: 75 %
          :target: _static/macWidgets/dPageList.png
          :alt: dPageList



     - .. image:: _static/winWidgets/dPageList.png
          :scale: 75 %
          :target: _static/winWidgets/dPageList.png
          :alt: dPageList



     - .. image:: _static/nixWidgets/dPageList.png
          :scale: 75 %
          :target: _static/nixWidgets/dPageList.png
          :alt: dPageList


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrame.dPageList

   .. automethod:: dabo.ui.uiwx.dPageFrame.dPageList.__init__

|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`Application <no-17370>`                Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-17371>`                  Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-17372>`                  The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-17373>`                Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-17374>`                Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-17375>`            Style of line for the border drawn around the control.
:ref:`BorderStyle <no-17376>`                Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-17377>`                Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-17378>`                     The position of the bottom side of the object. This is a
:ref:`Caption <no-17379>`                    The caption of the object. (str)
:ref:`Children <no-17380>`                   Returns a list of object references to the children of
:ref:`Class <no-17381>`                      The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-17382>`           Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-17383>`       Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-17384>`         Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-17385>`         Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-17386>`           Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-17387>`         Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-17388>`     Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-17389>`         Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-17390>`         Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-17391>`             Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-17392>`             Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-17393>`                Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-17394>`            Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-17395>`            Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-17396>`          Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-17397>`            Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-17398>`       Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-17399>`           Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-17400>`              Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-17401>`                Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-17402>`        Dynamically determine the value of the MousePointer property.
:ref:`DynamicPageClass <no-17403>`           Dynamically determine the value of the PageClass property.
:ref:`DynamicPageCount <no-17404>`           Dynamically determine the value of the PageCount property.
:ref:`DynamicPosition <no-17405>`            Dynamically determine the value of the Position property.
:ref:`DynamicSelectedPage <no-17406>`        Dynamically determine the value of the SelectedPage property.
:ref:`DynamicSelectedPageNumber <no-17407>`  Dynamically determine the value of the SelectedPageNumber property.
:ref:`DynamicSize <no-17408>`                Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-17409>`          Dynamically determine the value of the StatusText property.
:ref:`DynamicTabPosition <no-17410>`         Dynamically determine the value of the TabPosition property.
:ref:`DynamicTag <no-17411>`                 Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-17412>`         Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-17413>`                 Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-17414>`        Dynamically determine the value of the Transparency property.
:ref:`DynamicUpdateInactivePages <no-17415>` Dynamically determine the value of the UpdateInactivePages property.
:ref:`DynamicVisible <no-17416>`             Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-17417>`               Dynamically determine the value of the Width property.
:ref:`Enabled <no-17418>`                    Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-17419>`                       Specifies font object for this control. (dFont)
:ref:`FontBold <no-17420>`                   Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-17421>`            Human-readable description of the current font settings. (str)
:ref:`FontFace <no-17422>`                   Specifies the font face. (str)
:ref:`FontInfo <no-17423>`                   Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-17424>`                 Specifies whether font is italicized. (bool)
:ref:`FontSize <no-17425>`                   Specifies the point size of the font. (int)
:ref:`FontUnderline <no-17426>`              Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-17427>`                  Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-17428>`                       Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-17429>`                     Specifies the height of the object. (int)
:ref:`HelpContextText <no-17430>`            Specifies the context-sensitive help text associated with this
:ref:`Hover <no-17431>`                      When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-17432>`                       Specifies the left position of the object. (int)
:ref:`ListSpacing <no-17433>`                Controls the spacing of the items in the controlling list  (int)
:ref:`LogEvents <no-17434>`                  Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-17435>`              Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-17436>`                Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-17437>`               Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-17438>`              Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-17439>`                Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-17440>`               Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-17441>`               Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-17442>`                       Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-17443>`                   Specifies the base name of the object.
:ref:`PageClass <no-17444>`                  Specifies the class of control to use for pages by default. (classRef)
:ref:`PageCount <no-17445>`                  Specifies the number of pages in the pageframe. (int)
:ref:`PageSizerClass <no-17446>`             Default sizer class for pages added automatically to this control. Set
:ref:`Pages <no-17447>`                      Returns a list of the contained pages.  (list)
:ref:`Parent <no-17448>`                     The containing object. (obj)
:ref:`Position <no-17449>`                   The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-17450>`          Reference to the Preference Management object  (dPref)
:ref:`RegID <no-17451>`                      A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-17452>`                      The position of the right side of the object. This is a
:ref:`SelectedPage <no-17453>`               References the current frontmost page.  (dPage)
:ref:`SelectedPageNumber <no-17454>`         Returns the index of the current frontmost page.  (int)
:ref:`Size <no-17455>`                       The size of the object. (tuple)
:ref:`Sizer <no-17456>`                      The sizer for the object.
:ref:`StatusText <no-17457>`                 Specifies the text that displays in the form's status bar, if any.
:ref:`TabPosition <no-17458>`                Specifies where the page tabs are located. (int)
:ref:`TabStop <no-17459>`                    Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-17460>`                        A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-17461>`                Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-17462>`                        The top position of the object. (int)
:ref:`Transparency <no-17463>`               Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-17464>`          Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateInactivePages <no-17465>`        Determines if the inactive pages are updated too. (bool)
:ref:`UseSmartFocus <no-17466>`              Determines if focus has to be restored to the last active
:ref:`Visible <no-17467>`                    Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-17468>`            Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-17469>`                      The width of the object. (int)
:ref:`WindowHandle <no-17470>`               The platform-specific handle for the window. Read-only. (long)

============================================ ========================


Properties
==========

.. _no-17433:

**ListSpacing** 

Controls the spacing of the items in the controlling list  (int)



-------


Properties - inherited
========================

.. _no-17370:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17371:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17372:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17373:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17374:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17375:

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

.. _no-17376:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17377:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17378:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17379:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17380:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17381:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17382:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17383:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17384:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17385:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17386:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17387:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17388:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17389:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17390:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17391:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17392:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17393:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17394:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17395:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17396:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17397:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17398:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17399:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17400:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17401:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17402:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17403:

**DynamicPageClass** 

Dynamically determine the value of the PageClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageClass property. If DynamicPageClass is set to None (the default), PageClass
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17404:

**DynamicPageCount** 

Dynamically determine the value of the PageCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageCount property. If DynamicPageCount is set to None (the default), PageCount
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17405:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17406:

**DynamicSelectedPage** 

Dynamically determine the value of the SelectedPage property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPage property. If DynamicSelectedPage is set to None (the default), SelectedPage
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17407:

**DynamicSelectedPageNumber** 

Dynamically determine the value of the SelectedPageNumber property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPageNumber property. If DynamicSelectedPageNumber is set to None (the default), SelectedPageNumber
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17408:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17409:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17410:

**DynamicTabPosition** 

Dynamically determine the value of the TabPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabPosition property. If DynamicTabPosition is set to None (the default), TabPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17411:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17412:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17413:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17414:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17415:

**DynamicUpdateInactivePages** 

Dynamically determine the value of the UpdateInactivePages property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UpdateInactivePages property. If DynamicUpdateInactivePages is set to None (the default), UpdateInactivePages
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17416:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17417:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17418:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17419:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17420:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17421:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17422:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17423:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17424:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17425:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17426:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17427:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17428:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17429:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17430:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17431:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17432:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17434:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17435:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17436:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17437:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17438:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17439:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17440:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17441:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17442:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17443:

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

.. _no-17444:

**PageClass** 

Specifies the class of control to use for pages by default. (classRef)
    This really only applies when using the PageCount property to set the
    number of pages. If you instead use AddPage() you still need to send
    an instance as usual. Class must descend from a dabo base class.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17445:

**PageCount** 

Specifies the number of pages in the pageframe. (int)
    When using this to increase the number of pages, PageClass
    will be queried as the object to use as the page object.


Inherited from: 'wx._controls.BookCtrlBase - can not provide a link

-------

.. _no-17446:

**PageSizerClass** 

Default sizer class for pages added automatically to this control. Set
    this to None to prevent sizers from being automatically added to child
    pages. (dSizer or None)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17447:

**Pages** 

Returns a list of the contained pages.  (list)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17448:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17449:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17450:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17451:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17452:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17453:

**SelectedPage** 

References the current frontmost page.  (dPage)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17454:

**SelectedPageNumber** 

Returns the index of the current frontmost page.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17455:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17456:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17457:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17458:

**TabPosition** 

Specifies where the page tabs are located. (int)
        Top (default)
        Left
        Right
        Bottom


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17459:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-17460:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17461:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17462:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17463:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17464:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17465:

**UpdateInactivePages** 

Determines if the inactive pages are updated too. (bool)
    Setting it to False can significantly improve update performance
    of multipage forms. Default=True.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17466:

**UseSmartFocus** 

Determines if focus has to be restored to the last active
    control on page when it become selected. (bool) Default=False.
    


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17467:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17468:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17469:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17470:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-17471>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-17472>`              Occurs when a child control is created.
:ref:`Create <no-17473>`                 Occurs after the control or form is created.
:ref:`Destroy <no-17474>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-17475>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-17476>`               Occurs when the control gets the focus.
:ref:`Idle <no-17477>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-17478>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-17479>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-17480>`               
:ref:`KeyUp <no-17481>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-17482>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-17483>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-17484>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-17485>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-17486>`             
:ref:`MouseLeave <no-17487>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-17488>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-17489>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-17490>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-17491>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-17492>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-17493>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-17494>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-17495>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-17496>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-17497>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-17498>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-17499>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-17500>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-17501>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-17502>`                   Occurs when the control's position changes.
:ref:`PageChanged <no-17503>`            Occurs when a page in a pageframe-like control changes
:ref:`PageChanging <no-17504>`           Occurs when the current page in a pageframe-like control is about to change
:ref:`Paint <no-17505>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-17506>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-17507>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-17508>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-17509>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-17471:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-17472:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-17473:

**Create** 

Occurs after the control or form is created.



-------

.. _no-17474:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-17475:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-17476:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-17477:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-17478:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-17479:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-17480:

**KeyEvent** 



-------

.. _no-17481:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-17482:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-17483:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-17484:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-17485:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-17486:

**MouseEvent** 



-------

.. _no-17487:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-17488:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-17489:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-17490:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-17491:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-17492:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-17493:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-17494:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-17495:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-17496:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-17497:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-17498:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-17499:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-17500:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-17501:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-17502:

**Move** 

Occurs when the control's position changes.



-------

.. _no-17503:

**PageChanged** 

Occurs when a page in a pageframe-like control changes



-------

.. _no-17504:

**PageChanging** 

Occurs when the current page in a pageframe-like control is about to change



-------

.. _no-17505:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-17506:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-17507:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-17508:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-17509:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-17510>`   Translates a position value for a control to absolute screen position.
:ref:`addImage <no-17511>`              Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-17512>`             Instantiate object as a child of self.
:ref:`afterInit <no-17513>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-17514>`          
:ref:`afterSetProperties <no-17515>`    
:ref:`appendPage <no-17516>`            Appends the page to the pageframe, and optionally sets
:ref:`autoBindEvents <no-17517>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-17518>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforePageChange <no-17519>`      Return False from this method to prevent the page from changing.
:ref:`beforeSetProperties <no-17520>`   
:ref:`bindEvent <no-17521>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-17522>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-17523>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-17524>`          Makes this object topmost
:ref:`clear <no-17525>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-17526>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-17527>`  Given a position relative to this control, return a position relative
:ref:`copy <no-17528>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-17529>`                   Called by uiApp when the user requests a cut operation.
:ref:`cyclePages <no-17530>`            Moves through the pages by the specified amount, wrapping
:ref:`drawArc <no-17531>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-17532>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-17533>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-17534>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-17535>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-17536>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-17537>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-17538>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-17539>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-17540>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-17541>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-17542>`              Draws text on the object at the specified position
:ref:`endHover <no-17543>`              
:ref:`fitToSizer <no-17544>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-17545>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-17546>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-17547>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-17548>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-17549>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-17550>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-17551>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-17552>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-17553>`      Returns the current mouse position on the entire screen
:ref:`getPageImage <no-17554>`          Returns the index of the specified page's image in the
:ref:`getPositionInSizer <no-17555>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-17556>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-17557>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-17558>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-17559>`                  Make the object invisible.
:ref:`initEvents <no-17560>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-17561>`        Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-17562>`            Insert the page into the pageframe at the specified position,
:ref:`isContainedBy <no-17563>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-17564>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-17565>`                We need to force the control to adjust the list size.
:ref:`lockDisplay <no-17566>`           Locks the visual updates to the control.
:ref:`movePage <no-17567>`              Moves the specified 'old' page to the new position and
:ref:`moveTabOrderAfter <no-17568>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-17569>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-17570>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-17571>`               
:ref:`paste <no-17572>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-17573>`           
:ref:`processDroppedFiles <no-17574>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-17575>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-17576>`            Raise the passed Dabo event.
:ref:`reCreate <no-17577>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-17578>`              Recreate the object.
:ref:`redraw <no-17579>`                Called when the object is (re)drawn.
:ref:`refresh <no-17580>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-17581>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-17582>`               Destroys the object.
:ref:`removeDrawnObject <no-17583>`     
:ref:`removePage <no-17584>`            Removes the specified page. You can specify a page by either
:ref:`sendToBack <no-17585>`            Places this object behind all others.
:ref:`setAll <no-17586>`                Set all child object properties to the passed value.
:ref:`setFocus <no-17587>`              Sets focus to the object.
:ref:`setPageImage <no-17588>`          Sets the specified page's image to the image corresponding
:ref:`setPositionInSizer <no-17589>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-17590>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-17591>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-17592>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-17593>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-17594>`                  Make the object visible.
:ref:`showContainingPage <no-17595>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-17596>`       Display a context menu (popup) at the specified position.
:ref:`super <no-17597>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-17598>`           Remove a previously registered event binding.
:ref:`unbindKey <no-17599>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-17600>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-17601>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-17602>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-17565:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.layout(self)

   We need to force the control to adjust the list size.



-------


Methods - inherited
=====================

.. _no-17510:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17511:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.addImage(self, img, key=None)
   :noindex:


   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17512:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-17513:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17514:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17515:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17516:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.appendPage(self, pgCls=None, caption='', imgKey=None, \**kwargs)
   :noindex:


   
   Appends the page to the pageframe, and optionally sets
   the page caption and image. The image should have already
   been added to the pageframe if it is going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17517:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.autoBindEvents(self, force=True)
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

.. _no-17518:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17519:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.beforePageChange(self, fromPage, toPage)
   :noindex:


   Return False from this method to prevent the page from changing.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17520:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17521:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17522:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17523:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-17524:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17525:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17526:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17527:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17528:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17529:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17530:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.cyclePages(self, num)
   :noindex:


   
   Moves through the pages by the specified amount, wrapping
   around the ends. Negative values move to previous pages; positive
   move through the next pages.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17531:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17532:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17533:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-17534:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17535:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17536:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17537:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17538:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17539:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17540:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17541:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17542:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17543:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17544:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17545:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17546:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17547:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17548:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17549:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17550:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17551:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17552:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17553:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17554:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getPageImage(self, pg)
   :noindex:


   
   Returns the index of the specified page's image in the
   current image list, or -1 if no image is set for the page.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17555:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17556:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-17557:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17558:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17559:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17560:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17561:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17562:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.insertPage(self, pos, pgCls=None, caption='', imgKey=None, ignoreOverride=False, \**kwargs)
   :noindex:


   
   Insert the page into the pageframe at the specified position,
   and optionally sets the page caption and image. The image
   should have already been added to the pageframe if it is
   going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17563:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17564:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17566:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.lockDisplay(self)
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

.. _no-17567:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.movePage(self, oldPgOrPos, newPos, selecting=True)
   :noindex:


   
   Moves the specified 'old' page to the new position and
   optionally selects it. If an invalid page number is passed,
   it returns False without changing anything.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17568:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17569:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17570:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17571:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17572:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17573:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17574:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17575:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17576:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17577:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17578:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17579:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17580:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17581:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17582:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17583:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17584:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.removePage(self, pgOrPos, delPage=True)
   :noindex:


   
   Removes the specified page. You can specify a page by either
   passing the page itself, or a position. If delPage is True (default),
   the page is released, and None is returned. If delPage is
   False, the page is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17585:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17586:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-17587:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17588:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setPageImage(self, pg, imgKey)
   :noindex:


   
   Sets the specified page's image to the image corresponding
   to the specified key. May also optionally pass the index of the
   image in the ImageList rather than the key.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17589:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17590:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-17591:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-17592:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17593:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17594:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17595:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17596:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17597:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17598:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-17599:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17600:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17601:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17602:

.. function:: dabo.ui.uiwx.dPageFrame.dPageList.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
