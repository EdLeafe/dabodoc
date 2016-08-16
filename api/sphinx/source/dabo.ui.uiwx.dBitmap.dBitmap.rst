
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBitmap

.. _dabo.ui.uiwx.dBitmap.dBitmap:

========================================
|doc_title|  **dBitmap.dBitmap** - class
========================================

Creates a simple bitmap control to display images on your forms.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBitmap**

.. inheritance-diagram:: dBitmap


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* :ref:`dabo.ui.uiwx.dImageMixin.dImageMixin`



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



   * - .. image:: _static/macWidgets/dBitmap.png
          :scale: 75 %
          :target: _static/macWidgets/dBitmap.png
          :alt: dBitmap



     - .. image:: _static/winWidgets/dBitmap.png
          :scale: 75 %
          :target: _static/winWidgets/dBitmap.png
          :alt: dBitmap



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBitmap.dBitmap

   .. automethod:: dabo.ui.uiwx.dBitmap.dBitmap.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-19400>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-19401>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-19402>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-19403>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-19404>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-19405>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-19406>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-19407>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-19408>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-19409>`                The caption of the object. (str)
:ref:`Children <no-19410>`               Returns a list of object references to the children of
:ref:`Class <no-19411>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-19412>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-19413>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-19414>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-19415>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-19416>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-19417>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-19418>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-19419>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-19420>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-19421>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-19422>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-19423>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-19424>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-19425>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-19426>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-19427>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-19428>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-19429>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-19430>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-19431>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-19432>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-19433>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-19434>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-19435>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-19436>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-19437>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-19438>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-19439>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-19440>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-19441>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-19442>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-19443>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-19444>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-19445>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-19446>`               Specifies the font face. (str)
:ref:`FontInfo <no-19447>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-19448>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-19449>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-19450>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-19451>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-19452>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-19453>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-19454>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-19455>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-19456>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-19457>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-19458>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-19459>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-19460>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-19461>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-19462>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-19463>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-19464>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-19465>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-19466>`               Specifies the base name of the object.
:ref:`Parent <no-19467>`                 The containing object. (obj)
:ref:`Position <no-19468>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-19469>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-19470>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-19471>`                  The position of the right side of the object. This is a
:ref:`Size <no-19472>`                   The size of the object. (tuple)
:ref:`Sizer <no-19473>`                  The sizer for the object.
:ref:`StatusText <no-19474>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-19475>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-19476>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-19477>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-19478>`                    The top position of the object. (int)
:ref:`Transparency <no-19479>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-19480>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-19481>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-19482>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-19483>`                  The width of the object. (int)
:ref:`WindowHandle <no-19484>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-19400:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19401:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19402:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19403:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19404:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19405:

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

.. _no-19406:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19407:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19408:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19409:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19410:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19411:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19412:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19413:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19414:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19415:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19416:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19417:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19418:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19419:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19420:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19421:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19422:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19423:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19424:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19425:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19426:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19427:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19428:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19429:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19430:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19431:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19432:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19433:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19434:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19435:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19436:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19437:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19438:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19439:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19440:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19441:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19442:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19443:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19444:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19445:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19446:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19447:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19448:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19449:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19450:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19451:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19452:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19453:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19454:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19455:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19456:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19457:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19458:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19459:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19460:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19461:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19462:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19463:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19464:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19465:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19466:

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

.. _no-19467:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19468:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19469:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19470:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19471:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19472:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19473:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19474:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19475:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-19476:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19477:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19478:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19479:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19480:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19481:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19482:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19483:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19484:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-19485>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-19486>`                 Occurs after the control or form is created.
:ref:`Destroy <no-19487>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-19488>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-19489>`               Occurs when the control gets the focus.
:ref:`Idle <no-19490>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-19491>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-19492>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-19493>`               
:ref:`KeyUp <no-19494>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-19495>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-19496>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-19497>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-19498>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-19499>`             
:ref:`MouseLeave <no-19500>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-19501>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-19502>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-19503>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-19504>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-19505>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-19506>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-19507>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-19508>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-19509>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-19510>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-19511>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-19512>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-19513>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-19514>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-19515>`                   Occurs when the control's position changes.
:ref:`Paint <no-19516>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-19517>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-19518>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-19519>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-19520>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-19485:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-19486:

**Create** 

Occurs after the control or form is created.



-------

.. _no-19487:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-19488:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-19489:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-19490:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-19491:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-19492:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-19493:

**KeyEvent** 



-------

.. _no-19494:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-19495:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-19496:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-19497:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-19498:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-19499:

**MouseEvent** 



-------

.. _no-19500:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-19501:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-19502:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-19503:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-19504:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-19505:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-19506:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-19507:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-19508:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-19509:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-19510:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-19511:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-19512:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-19513:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-19514:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-19515:

**Move** 

Occurs when the control's position changes.



-------

.. _no-19516:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-19517:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-19518:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-19519:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-19520:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-19521>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-19522>`             Instantiate object as a child of self.
:ref:`afterInit <no-19523>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-19524>`          
:ref:`afterSetProperties <no-19525>`    
:ref:`autoBindEvents <no-19526>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-19527>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-19528>`   
:ref:`bindEvent <no-19529>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-19530>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-19531>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-19532>`          Makes this object topmost
:ref:`clear <no-19533>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-19534>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-19535>`  Given a position relative to this control, return a position relative
:ref:`copy <no-19536>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-19537>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-19538>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-19539>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-19540>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-19541>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-19542>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-19543>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-19544>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-19545>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-19546>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-19547>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-19548>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-19549>`              Draws text on the object at the specified position
:ref:`endHover <no-19550>`              
:ref:`fitToSizer <no-19551>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-19552>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-19553>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-19554>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-19555>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-19556>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-19557>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-19558>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-19559>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-19560>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-19561>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-19562>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-19563>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-19564>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-19565>`                  Make the object invisible.
:ref:`initEvents <no-19566>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-19567>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-19568>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-19569>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-19570>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-19571>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-19572>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-19573>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-19574>`               
:ref:`paste <no-19575>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-19576>`           
:ref:`processDroppedFiles <no-19577>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-19578>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-19579>`            Raise the passed Dabo event.
:ref:`reCreate <no-19580>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-19581>`              Recreate the object.
:ref:`redraw <no-19582>`                Called when the object is (re)drawn.
:ref:`refresh <no-19583>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-19584>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-19585>`               Destroys the object.
:ref:`removeDrawnObject <no-19586>`     
:ref:`sendToBack <no-19587>`            Places this object behind all others.
:ref:`setAll <no-19588>`                Set all child object properties to the passed value.
:ref:`setFocus <no-19589>`              Sets focus to the object.
:ref:`setPositionInSizer <no-19590>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-19591>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-19592>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-19593>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-19594>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-19595>`                  Make the object visible.
:ref:`showContainingPage <no-19596>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-19597>`       Display a context menu (popup) at the specified position.
:ref:`super <no-19598>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-19599>`           Remove a previously registered event binding.
:ref:`unbindKey <no-19600>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-19601>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-19602>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-19603>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-19521:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19522:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-19523:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19524:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19525:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19526:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.autoBindEvents(self, force=True)
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

.. _no-19527:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19528:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19529:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19530:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19531:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-19532:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19533:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19534:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19535:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19536:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19537:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19538:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19539:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19540:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-19541:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19542:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19543:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19544:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19545:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19546:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19547:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19548:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19549:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19550:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19551:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19552:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19553:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19554:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19555:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19556:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19557:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19558:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19559:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19560:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19561:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19562:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-19563:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19564:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19565:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19566:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19567:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19568:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19569:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19570:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.lockDisplay(self)
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

.. _no-19571:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19572:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19573:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19574:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19575:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19576:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19577:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19578:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19579:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19580:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19581:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19582:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19583:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19584:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19585:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19586:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19587:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19588:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-19589:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19590:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19591:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-19592:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-19593:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19594:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19595:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19596:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19597:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19598:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19599:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19600:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19601:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19602:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19603:

.. function:: dabo.ui.uiwx.dBitmap.dBitmap.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
