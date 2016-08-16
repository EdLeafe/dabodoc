
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPdfWindow

.. _dabo.ui.uiwx.dPdfWindow.dPdfWindow:

==============================================
|doc_title|  **dPdfWindow.dPdfWindow** - class
==============================================


Displays a PDF file on Windows using Adobe Acrobat Reader in a panel.

See wx.lib.pdfwin.PDFWindow for the API.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPdfWindow**

.. inheritance-diagram:: dPdfWindow


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* :ref:`dabo.ui.uiwx.dPdfWindow.Dummy`



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



     - .. image:: _static/winWidgets/dPdfWindow.png
          :scale: 75 %
          :target: _static/winWidgets/dPdfWindow.png
          :alt: dPdfWindow



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPdfWindow.dPdfWindow

   .. automethod:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-34374>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-34375>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-34376>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-34377>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-34378>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-34379>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-34380>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-34381>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-34382>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-34383>`                The caption of the object. (str)
:ref:`Children <no-34384>`               Returns a list of object references to the children of
:ref:`Class <no-34385>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-34386>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-34387>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-34388>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-34389>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-34390>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-34391>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-34392>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-34393>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-34394>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-34395>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-34396>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-34397>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-34398>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-34399>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-34400>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-34401>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-34402>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-34403>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-34404>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-34405>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-34406>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-34407>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-34408>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-34409>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-34410>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-34411>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-34412>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-34413>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-34414>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-34415>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-34416>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-34417>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-34418>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-34419>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-34420>`               Specifies the font face. (str)
:ref:`FontInfo <no-34421>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-34422>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-34423>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-34424>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-34425>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-34426>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-34427>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-34428>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-34429>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-34430>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-34431>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-34432>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-34433>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-34434>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-34435>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-34436>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-34437>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-34438>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-34439>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-34440>`               Specifies the base name of the object.
:ref:`Parent <no-34441>`                 The containing object. (obj)
:ref:`Position <no-34442>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-34443>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-34444>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-34445>`                  The position of the right side of the object. This is a
:ref:`Size <no-34446>`                   The size of the object. (tuple)
:ref:`Sizer <no-34447>`                  The sizer for the object.
:ref:`StatusText <no-34448>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-34449>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-34450>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-34451>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-34452>`                    The top position of the object. (int)
:ref:`Transparency <no-34453>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-34454>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-34455>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-34456>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-34457>`                  The width of the object. (int)
:ref:`WindowHandle <no-34458>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-34374:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34375:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34376:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34377:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34378:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34379:

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

.. _no-34380:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34381:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34382:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34383:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34384:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34385:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34386:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34387:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34388:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34389:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34390:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34391:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34392:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34393:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34394:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34395:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34396:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34397:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34398:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34399:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34400:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34401:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34402:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34403:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34404:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34405:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34406:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34407:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34408:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34409:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34410:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34411:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34412:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34413:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34414:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34415:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34416:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34417:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34418:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34419:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34420:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34421:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34422:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34423:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34424:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34425:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34426:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34427:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34428:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34429:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34430:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34431:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34432:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34433:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34434:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34435:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34436:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34437:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34438:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34439:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34440:

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

.. _no-34441:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34442:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34443:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34444:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34445:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34446:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34447:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34448:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34449:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-34450:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34451:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34452:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34453:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34454:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34455:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34456:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34457:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34458:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-34459>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-34460>`                 Occurs after the control or form is created.
:ref:`Destroy <no-34461>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-34462>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-34463>`               Occurs when the control gets the focus.
:ref:`Idle <no-34464>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-34465>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-34466>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-34467>`               
:ref:`KeyUp <no-34468>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-34469>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-34470>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-34471>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-34472>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-34473>`             
:ref:`MouseLeave <no-34474>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-34475>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-34476>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-34477>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-34478>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-34479>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-34480>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-34481>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-34482>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-34483>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-34484>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-34485>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-34486>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-34487>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-34488>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-34489>`                   Occurs when the control's position changes.
:ref:`Paint <no-34490>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-34491>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-34492>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-34493>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-34494>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-34459:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-34460:

**Create** 

Occurs after the control or form is created.



-------

.. _no-34461:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-34462:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-34463:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-34464:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-34465:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-34466:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-34467:

**KeyEvent** 



-------

.. _no-34468:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-34469:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-34470:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-34471:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-34472:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-34473:

**MouseEvent** 



-------

.. _no-34474:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-34475:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-34476:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-34477:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-34478:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-34479:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-34480:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-34481:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-34482:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-34483:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-34484:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-34485:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-34486:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-34487:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-34488:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-34489:

**Move** 

Occurs when the control's position changes.



-------

.. _no-34490:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-34491:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-34492:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-34493:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-34494:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-34495>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-34496>`             Instantiate object as a child of self.
:ref:`afterInit <no-34497>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-34498>`          
:ref:`afterSetProperties <no-34499>`    
:ref:`autoBindEvents <no-34500>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-34501>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-34502>`   
:ref:`bindEvent <no-34503>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-34504>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-34505>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-34506>`          Makes this object topmost
:ref:`clear <no-34507>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-34508>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-34509>`  Given a position relative to this control, return a position relative
:ref:`copy <no-34510>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-34511>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-34512>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-34513>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-34514>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-34515>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-34516>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-34517>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-34518>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-34519>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-34520>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-34521>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-34522>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-34523>`              Draws text on the object at the specified position
:ref:`endHover <no-34524>`              
:ref:`fitToSizer <no-34525>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-34526>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-34527>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-34528>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-34529>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-34530>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-34531>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-34532>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-34533>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-34534>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-34535>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-34536>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-34537>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-34538>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-34539>`                  Make the object invisible.
:ref:`initEvents <no-34540>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-34541>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-34542>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-34543>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-34544>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-34545>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-34546>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-34547>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-34548>`               
:ref:`paste <no-34549>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-34550>`           
:ref:`processDroppedFiles <no-34551>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-34552>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-34553>`            Raise the passed Dabo event.
:ref:`reCreate <no-34554>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-34555>`              Recreate the object.
:ref:`redraw <no-34556>`                Called when the object is (re)drawn.
:ref:`refresh <no-34557>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-34558>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-34559>`               Destroys the object.
:ref:`removeDrawnObject <no-34560>`     
:ref:`sendToBack <no-34561>`            Places this object behind all others.
:ref:`setAll <no-34562>`                Set all child object properties to the passed value.
:ref:`setFocus <no-34563>`              Sets focus to the object.
:ref:`setPositionInSizer <no-34564>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-34565>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-34566>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-34567>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-34568>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-34569>`                  Make the object visible.
:ref:`showContainingPage <no-34570>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-34571>`       Display a context menu (popup) at the specified position.
:ref:`super <no-34572>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-34573>`           Remove a previously registered event binding.
:ref:`unbindKey <no-34574>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-34575>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-34576>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-34577>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-34495:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34496:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-34497:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34498:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34499:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34500:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.autoBindEvents(self, force=True)
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

.. _no-34501:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34502:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34503:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34504:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34505:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-34506:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34507:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34508:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34509:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34510:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34511:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34512:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34513:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34514:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-34515:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34516:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34517:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34518:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34519:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34520:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34521:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34522:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34523:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34524:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34525:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34526:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34527:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34528:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34529:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34530:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34531:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34532:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34533:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34534:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34535:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34536:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-34537:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34538:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34539:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34540:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34541:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34542:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34543:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34544:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.lockDisplay(self)
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

.. _no-34545:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34546:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34547:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34548:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34549:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34550:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34551:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34552:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34553:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34554:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34555:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34556:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34557:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34558:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34559:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34560:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34561:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34562:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-34563:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34564:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34565:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-34566:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-34567:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34568:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34569:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34570:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34571:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34572:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34573:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34574:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34575:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34576:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34577:

.. function:: dabo.ui.uiwx.dPdfWindow.dPdfWindow.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
