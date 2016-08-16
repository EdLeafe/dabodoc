
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dReportProgress

.. _dabo.ui.uiwx.dReportProgress.dReportProgress:

========================================================
|doc_title|  **dReportProgress.dReportProgress** - class
========================================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dReportProgress**

.. inheritance-diagram:: dReportProgress


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dPanel`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dReportProgress.dReportProgress


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-19190>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-19191>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-19192>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-19193>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-19194>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-19195>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-19196>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-19197>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-19198>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-19199>`                Specifies the caption of the progress bar.
:ref:`Children <no-19200>`               Returns a list of object references to the children of
:ref:`Class <no-19201>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-19202>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-19203>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-19204>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-19205>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-19206>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-19207>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-19208>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-19209>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-19210>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-19211>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-19212>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-19213>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-19214>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-19215>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-19216>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-19217>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-19218>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-19219>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-19220>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-19221>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-19222>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-19223>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-19224>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-19225>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-19226>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-19227>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-19228>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-19229>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-19230>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-19231>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-19232>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-19233>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-19234>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-19235>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-19236>`               Specifies the font face. (str)
:ref:`FontInfo <no-19237>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-19238>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-19239>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-19240>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-19241>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-19242>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-19243>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-19244>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-19245>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-19246>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-19247>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-19248>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-19249>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-19250>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-19251>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-19252>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-19253>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-19254>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-19255>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-19256>`               Specifies the base name of the object.
:ref:`Parent <no-19257>`                 The containing object. (obj)
:ref:`Position <no-19258>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-19259>`      Reference to the Preference Management object  (dPref)
:ref:`ProcessObject <no-19260>`          Specifies the object that is processing (a dReportWriter instance, for example).
:ref:`RegID <no-19261>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-19262>`                  The position of the right side of the object. This is a
:ref:`Size <no-19263>`                   The size of the object. (tuple)
:ref:`Sizer <no-19264>`                  The sizer for the object.
:ref:`StatusText <no-19265>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-19266>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-19267>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-19268>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-19269>`                    The top position of the object. (int)
:ref:`Transparency <no-19270>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-19271>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-19272>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-19273>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-19274>`                  The width of the object. (int)
:ref:`WindowHandle <no-19275>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-19260:

**ProcessObject** 

Specifies the object that is processing (a dReportWriter instance, for example).



-------


Properties - inherited
========================

.. _no-19190:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19191:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19192:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19193:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19194:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19195:

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

.. _no-19196:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19197:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19198:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19199:

**Caption** 

Specifies the caption of the progress bar.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19200:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19201:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19202:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19203:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19204:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19205:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19206:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19207:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19208:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19209:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19210:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19211:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19212:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19213:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19214:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19215:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19216:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19217:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19218:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19219:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19220:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19221:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19222:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19223:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19224:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19225:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19226:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19227:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19228:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19229:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19230:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19231:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19232:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19233:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19234:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19235:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19236:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19237:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19238:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19239:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19240:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19241:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19242:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19243:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19244:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19245:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19246:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19247:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19248:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19249:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19250:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19251:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19252:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19253:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19254:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19255:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19256:

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

.. _no-19257:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19258:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19259:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19261:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19262:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19263:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19264:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-19265:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19266:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-19267:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19268:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19269:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19270:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19271:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19272:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19273:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19274:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19275:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-19276>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-19277>`              Occurs when a child control is created.
:ref:`Create <no-19278>`                 Occurs after the control or form is created.
:ref:`Destroy <no-19279>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-19280>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-19281>`               Occurs when the control gets the focus.
:ref:`Idle <no-19282>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-19283>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-19284>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-19285>`               
:ref:`KeyUp <no-19286>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-19287>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-19288>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-19289>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-19290>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-19291>`             
:ref:`MouseLeave <no-19292>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-19293>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-19294>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-19295>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-19296>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-19297>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-19298>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-19299>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-19300>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-19301>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-19302>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-19303>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-19304>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-19305>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-19306>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-19307>`                   Occurs when the control's position changes.
:ref:`Paint <no-19308>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-19309>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-19310>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-19311>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-19312>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-19276:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-19277:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-19278:

**Create** 

Occurs after the control or form is created.



-------

.. _no-19279:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-19280:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-19281:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-19282:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-19283:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-19284:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-19285:

**KeyEvent** 



-------

.. _no-19286:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-19287:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-19288:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-19289:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-19290:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-19291:

**MouseEvent** 



-------

.. _no-19292:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-19293:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-19294:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-19295:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-19296:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-19297:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-19298:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-19299:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-19300:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-19301:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-19302:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-19303:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-19304:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-19305:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-19306:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-19307:

**Move** 

Occurs when the control's position changes.



-------

.. _no-19308:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-19309:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-19310:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-19311:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-19312:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-19313>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-19314>`             Instantiate object as a child of self.
:ref:`afterInit <no-19315>`             
:ref:`afterInitAll <no-19316>`          
:ref:`afterSetProperties <no-19317>`    
:ref:`autoBindEvents <no-19318>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-19319>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-19320>`   
:ref:`bindEvent <no-19321>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-19322>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-19323>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-19324>`          Makes this object topmost
:ref:`cancel <no-19325>`                
:ref:`clear <no-19326>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-19327>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-19328>`  Given a position relative to this control, return a position relative
:ref:`copy <no-19329>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-19330>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-19331>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-19332>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-19333>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-19334>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-19335>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-19336>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-19337>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-19338>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-19339>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-19340>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-19341>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-19342>`              Draws text on the object at the specified position
:ref:`endHover <no-19343>`              
:ref:`fitToSizer <no-19344>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-19345>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-19346>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-19347>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-19348>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-19349>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-19350>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-19351>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-19352>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-19353>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-19354>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-19355>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-19356>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-19357>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-19358>`                  
:ref:`initEvents <no-19359>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-19360>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-19361>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-19362>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-19363>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-19364>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-19365>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-19366>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-19367>`     Given a position relative to the form, return a position relative
:ref:`onCancel <no-19368>`              
:ref:`onHover <no-19369>`               
:ref:`paste <no-19370>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-19371>`           
:ref:`processDroppedFiles <no-19372>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-19373>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-19374>`            Raise the passed Dabo event.
:ref:`reCreate <no-19375>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-19376>`              Recreate the object.
:ref:`redraw <no-19377>`                Called when the object is (re)drawn.
:ref:`refresh <no-19378>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-19379>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-19380>`               Destroys the object.
:ref:`removeDrawnObject <no-19381>`     
:ref:`sendToBack <no-19382>`            Places this object behind all others.
:ref:`setAll <no-19383>`                Set all child object properties to the passed value.
:ref:`setFocus <no-19384>`              Sets focus to the object.
:ref:`setPositionInSizer <no-19385>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-19386>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-19387>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-19388>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-19389>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-19390>`                  
:ref:`showContainingPage <no-19391>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-19392>`       Display a context menu (popup) at the specified position.
:ref:`super <no-19393>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-19394>`           Remove a previously registered event binding.
:ref:`unbindKey <no-19395>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-19396>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-19397>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-19398>`                Update the properties of this object and all contained objects.
:ref:`updateProgress <no-19399>`        

======================================= ========================


Methods
=======

.. _no-19315:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.afterInit(self)



-------

.. _no-19325:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.cancel(self)



-------

.. _no-19358:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.hide(self)



-------

.. _no-19368:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.onCancel(self, evt)



-------

.. _no-19390:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.show(self)



-------

.. _no-19399:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.updateProgress(self, val, range_)



-------


Methods - inherited
=====================

.. _no-19313:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19314:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-19316:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19317:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19318:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.autoBindEvents(self, force=True)
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

.. _no-19319:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19320:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19321:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19322:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19323:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-19324:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19326:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19327:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19328:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19329:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19330:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19331:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19332:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19333:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-19334:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19335:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19336:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19337:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19338:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19339:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19340:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19341:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19342:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19343:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19344:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19345:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19346:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19347:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19348:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19349:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19350:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19351:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19352:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19353:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19354:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19355:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-19356:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19357:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19359:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19360:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19361:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19362:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19363:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-19364:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.lockDisplay(self)
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

.. _no-19365:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19366:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19367:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19369:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19370:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19371:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19372:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19373:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19374:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19375:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-19376:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19377:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19378:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19379:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19380:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19381:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19382:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19383:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-19384:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19385:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19386:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-19387:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-19388:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19389:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19391:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19392:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19393:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-19394:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-19395:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19396:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19397:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-19398:

.. function:: dabo.ui.uiwx.dReportProgress.dReportProgress.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
